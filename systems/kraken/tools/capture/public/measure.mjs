// Measures Kraken's public components. Signed-out only.
// OneTrust is hidden, never clicked. Sign-in and sign-up fields are focused
// for their computed style; nothing is typed and nothing is submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, hideConsent, styleOf, crop, centre, RAW, chromium } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
// Earlier readings are loaded and merged, so a run that dies mid-page keeps every component
// it did not reach instead of writing a file without them.
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
out.components ??= {};
// Each refreshed component carries its own run date; _meta.captured moves only when the whole
// run finishes, so retained readings never take a date they were not measured on.
const RUN = new Date().toLocaleDateString('en-CA');
out._meta = { ...(out._meta || {}), product: 'kraken', route: 'public-web', lastRun: RUN };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current;

async function newPage(key, url, { mobile = false, wait = 4000 } = {}) {
  current = key;
  const { browser, context } = await launch(mobile
    ? { width: 390, height: 844, mobile: true }
    : { width: 1440, height: 900, dpr: 1 });
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, url);
  await open(page, url, { wait });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return { browser, context };
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4).catch(() => {});
  await page.waitForTimeout(180);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(250);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(280);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const target = loc.filter({ visible: true }).first();
    const s = await styleOf(target);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, target, `${key}-${state}`, opts.pad ?? 6); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message || e).slice(0, 120));
  }
}

async function S(key, loc, list, meta, opts = {}) {
  out.components[key] = {
    run: RUN,
    page: current,
    title: meta.title,
    group: meta.group,
    desc: meta.desc || '',
    selector: meta.sel || '',
    states: {},
  };
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count().catch(() => 0))) {
    out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  for (const st of list) {
    let undo;
    let via = 'at rest';
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(target);
      await hideConsent(page);
      if (st === 'hover') {
        await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true, timeout: 3000 }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await target.click({ timeout: 3000 });
        await page.waitForTimeout(250);
        via = 'clicked into the field; nothing typed';
      } else if (st === 'selected') {
        await target.click({ timeout: 3000 });
        await page.waitForTimeout(400);
        via = 'clicked a tab; no navigation';
      }
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 180) };
      log('  !', key, st, String(e.message || e).slice(0, 100));
    }
    if (undo) await undo().catch(() => {});
  }
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function markVisible(page, predicateSource) {
  return page.evaluate((src) => {
    // A page whose CSP forbids eval makes new Function throw; that is a missed match, not a
    // reason to abort the whole run.
    let pred;
    try { pred = new Function('el', src); } catch { return false; }
    const all = [...document.querySelectorAll('a, button, input, [role="tab"], h1, header, footer, table, tr')];
    const el = all.find((node) => {
      const r = node.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return false;
      if (r.bottom < 0 || r.top > innerHeight + 40) return false;
      try { return pred(node); } catch { return false; }
    });
    document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
    if (!el) return false;
    el.setAttribute('data-m-mark', '1');
    return true;
  }, predicateSource);
}

async function run() {
  // Home, light.
  let session = await newPage('home', BASE + '/');
  const g = 'Shell';
  await S('header', page.locator('header').first(), ['default'], { group: g, title: 'Top bar', desc: 'The marketing header: wordmark, product links, search, language, Log in and Sign up.', sel: 'header' }, { noScroll: true });
  if (await markVisible(page, `return el.tagName==='A' && (el.innerText||'').trim()==='Sign up' && el.getBoundingClientRect().top<80 && el.getBoundingClientRect().width>40`)) {
    await S('nav-signup', page.locator('[data-m-mark="1"]'), B4, { group: g, title: 'Sign up, nav', desc: 'Primary purple pill in the header. Measured, never followed.', sel: 'header a "Sign up"' }, { noScroll: true });
  }
  if (await markVisible(page, `return el.tagName==='A' && (el.innerText||'').trim()==='Log in' && el.getBoundingClientRect().top<80`)) {
    await S('nav-login', page.locator('[data-m-mark="1"]'), B4, { group: g, title: 'Log in, nav', desc: 'Neutral wash pill. Measured, never followed.', sel: 'header a "Log in"' }, { noScroll: true });
  }
  if (await markVisible(page, `return el.tagName==='BUTTON' && (el.getAttribute('aria-label')||'')==='Search' && el.getBoundingClientRect().top<80 && el.getBoundingClientRect().width>8`)) {
    await S('search-button', page.locator('[data-m-mark="1"]'), B4, { group: g, title: 'Search icon button', desc: 'Opens the search dialog. The dialog itself is captured as a screenshot; this crop is the trigger.', sel: 'button[aria-label=Search]' }, { noScroll: true });
  }
  await S('hero-title', page.locator('h1').first(), ['default'], { group: 'Home', title: 'Hero title', desc: 'Kraken-Brand display on the magic-light page.', sel: 'h1' }, { noScroll: true });
  if (await markVisible(page, `const t=(el.innerText||'').trim(); return (el.tagName==='A'||el.tagName==='BUTTON') && t==='Try Kraken' && el.getBoundingClientRect().width>60`)) {
    await S('hero-cta', page.locator('[data-m-mark="1"]'), B4, { group: 'Home', title: 'Try Kraken', desc: 'Primary high button, 48px, radius 12, purple #7132f5. Measured, never followed.', sel: 'Try Kraken' }, { noScroll: true });
  }
  if (await markVisible(page, `return el.getAttribute('role')==='tab' && (el.innerText||'').trim()==='Crypto'`)) {
    await S('market-tab', page.locator('[data-m-mark="1"]'), ['default', 'focus-visible'], { group: 'Home', title: 'Market tab, selected', desc: 'The Crypto tab on the prices strip.', sel: '[role=tab] Crypto' });
  }
  if (await markVisible(page, `return el.getAttribute('role')==='tab' && /Futures/.test(el.innerText||'')`)) {
    await S('market-tab-idle', page.locator('[data-m-mark="1"]'), ['default', 'hover', 'selected'], { group: 'Home', title: 'Market tab', desc: 'An unselected tab. selected clicks it; the panel swaps, nothing is submitted.', sel: '[role=tab] Futures' });
  }
  if (await markVisible(page, `return el.tagName==='TR' && /Bitcoin/.test(el.innerText||'') && el.getBoundingClientRect().width>400`)) {
    await S('price-row', page.locator('[data-m-mark="1"]'), ['default', 'hover'], { group: 'Home', title: 'Price row', desc: 'A market row: asset, price, 24h change, market cap.', sel: 'tr Bitcoin' });
  }
  await S('footer', page.locator('footer').first(), ['default'], { group: 'Home', title: 'Footer', desc: 'The marketing footer band.', sel: 'footer' });
  save();
  await session.context.close();
  await session.browser.close();

  // Prices.
  session = await newPage('prices', BASE + '/prices');
  await S('prices-title', page.locator('h1').first(), ['default'], { group: 'Prices', title: 'Prices title', sel: 'h1' }, { noScroll: true });
  if (await markVisible(page, `return el.tagName==='INPUT' && el.getBoundingClientRect().width>80 && el.getBoundingClientRect().top<700`)) {
    await S('prices-search', page.locator('[data-m-mark="1"]'), ['default', 'focused', 'focus-visible'], { group: 'Prices', title: 'Prices search field', desc: 'Focused only. Nothing typed, nothing submitted.', sel: 'input' }, { noScroll: true });
  }
  save();
  await session.context.close();
  await session.browser.close();

  // Pro, dark.
  session = await newPage('pro', BASE + '/pro');
  await S('pro-title', page.locator('h1').first(), ['default'], { group: 'Pro', title: 'Pro hero title', desc: 'Kraken-Brand on the magic-dark page.', sel: 'h1' }, { noScroll: true });
  if (await markVisible(page, `const t=(el.innerText||'').replace(/\\s+/g,' ').trim(); return (el.tagName==='A'||el.tagName==='BUTTON') && /Create free account|Get a free account/.test(t) && el.getBoundingClientRect().width>80 && el.getBoundingClientRect().height>30 && el.getBoundingClientRect().top<700`)) {
    await S('pro-cta', page.locator('[data-m-mark="1"]'), B4, { group: 'Pro', title: 'Create free account', desc: 'Neutral-high button on the dark Pro page: near-white fill, near-black text. Measured, never followed.', sel: 'Create free account' }, { noScroll: true });
  }
  save();
  await session.context.close();
  await session.browser.close();

  // Sign-up boundary. Focus the email field, type nothing, submit nothing.
  session = await newPage('signup', BASE + '/sign-up', { wait: 5000 });
  await S('signup-title', page.locator('h1').first(), ['default'], { group: 'Account boundary', title: 'Create account title', desc: 'The public sign-up card. The form was not submitted.', sel: 'h1' }, { noScroll: true });
  if (await markVisible(page, `return el.tagName==='INPUT' && (el.type==='email' || el.type==='text' || /email/i.test(el.name||'') || /email/i.test(el.getAttribute('placeholder')||'') || /email/i.test(el.getAttribute('aria-label')||'')) && el.getBoundingClientRect().width>80`)) {
    await S('signup-email', page.locator('[data-m-mark="1"]'), ['default', 'focused', 'focus-visible'], { group: 'Account boundary', title: 'Email field', desc: 'Focused for its ring. Nothing typed.', sel: 'input email' }, { noScroll: true });
  }
  if (await markVisible(page, `const t=(el.innerText||'').trim(); return (el.tagName==='BUTTON'||el.tagName==='A') && t==='Continue' && el.getBoundingClientRect().width>40`)) {
    await S('signup-continue', page.locator('[data-m-mark="1"]'), ['default', 'hover', 'focus-visible', 'pressed'], { group: 'Account boundary', title: 'Continue', desc: 'The submit control, measured with a forced :active. Never clicked for real.', sel: 'button Continue' }, { noScroll: true });
  }
  save();
  await session.context.close();
  await session.browser.close();

  // Sign-in boundary on id.kraken.com. Focus only.
  session = await newPage('signin', 'https://id.kraken.com/sign-in', { wait: 5000 });
  if (await markVisible(page, `return el.tagName==='INPUT' && (el.name==='username' || el.type==='text') && el.getBoundingClientRect().width>80 && el.getBoundingClientRect().top<500`)) {
    await S('signin-email', page.locator('[data-m-mark="1"]'), ['default', 'focused'], { group: 'Account boundary', title: 'Sign-in email', desc: 'id.kraken.com sign-in field at rest and focused. Nothing typed, nothing submitted.', sel: 'input[name=username]' }, { noScroll: true });
  }
  if (await markVisible(page, `return el.tagName==='INPUT' && el.type==='password' && el.getBoundingClientRect().width>80`)) {
    await S('signin-password', page.locator('[data-m-mark="1"]'), ['default'], { group: 'Account boundary', title: 'Sign-in password', desc: 'At rest. Nothing typed.', sel: 'input[type=password]' }, { noScroll: true });
  }
  if (await markVisible(page, `const t=(el.innerText||'').trim(); return el.tagName==='BUTTON' && t==='Continue' && el.getBoundingClientRect().width>40 && el.getBoundingClientRect().top<600`)) {
    await S('signin-continue', page.locator('[data-m-mark="1"]'), ['default', 'hover', 'pressed'], { group: 'Account boundary', title: 'Sign-in continue', desc: 'Measured, never clicked.', sel: 'button Continue' }, { noScroll: true });
  }
  save();
  await session.context.close();
  await session.browser.close();

  // Phone header.
  session = await newPage('mobile-home', BASE + '/', { mobile: true, wait: 4000 });
  await S('m-header', page.locator('header').first(), ['default'], { group: 'Mobile', title: 'Phone header', desc: '390px header.', sel: 'header' }, { noScroll: true });
  await S('m-hero', page.locator('h1').first(), ['default'], { group: 'Mobile', title: 'Phone hero title', sel: 'h1' }, { noScroll: true });
  save();
  await session.context.close();
  await session.browser.close();

  const n = Object.keys(out.components).length;
  const states = Object.values(out.components).reduce((a, c) => a + Object.keys(c.states || {}).length, 0);
  log('done', n, 'components', states, 'states');
  out._meta.captured = RUN;   // every page ran
  save();
}

await run();
