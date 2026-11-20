// Measures Lemon Squeezy's public components in every state reachable
// without signing in, submitting a form, purchasing, or starting OAuth.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and one crop per component and state
// into components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, DOCS, AUTH, launch, open, hideConsent, styleOf, crop, centre, RAW } from './lib.mjs';
import { datePrior } from '../merge-dates.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
// Start from the committed readings so a run that fails part-way never drops a component it did
// not reach (measure-gated.mjs adds its entries to the same file).
// Dates: every state carries its own `read` date, and kept states keep theirs
// (merge-dates.mjs). _meta.captured keeps the earlier date until this run reads
// something, so a rerun that fails throughout never redates old readings;
// _meta.lastAttempt is the date of this run.
const prior = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
const RUN = new Date().toLocaleDateString('en-CA');
const priorCaptured = prior._meta && prior._meta.captured;
const out = {
  _meta: { ...prior._meta, captured: priorCaptured || RUN, lastAttempt: RUN, product: 'Lemon Squeezy', route: 'public-web' },
  components: datePrior({ ...prior.components }, priorCaptured),
};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current, context;

async function newPage(key, url, { mobile = false } = {}) {
  current = key;
  if (page) await page.close().catch(() => {});
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, url);
  await open(page, url, { wait: 1600 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4).catch(() => {});
  await page.waitForTimeout(180);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await page.keyboard.down('Shift');
    await loc.evaluate((el) => el.focus());
    await page.keyboard.up('Shift');
    ok = await loc.evaluate((el) => document.activeElement === el);
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
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 12); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, read: RUN };
    out._meta.captured = RUN; // a reading succeeded in this run
    log('  ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style.backgroundColor, s.style.color);
  } catch (e) {
    failState(key, state, e);
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

// A failed re-read keeps the committed reading and notes the failure beside it; a state with no
// earlier reading records the error.
function failState(key, state, e) {
  const states = out.components[key].states;
  const prior = states[state];
  const msg = String(e.message || e).slice(0, 200);
  states[state] = prior && !prior.error ? { ...prior, recaptureError: msg, recaptureRun: RUN } : { error: msg, read: RUN };
}

function comp(key, meta) {
  const prev = out.components[key];
  out.components[key] = {
    page: current,
    url: meta.url,
    title: meta.title,
    group: meta.group,
    desc: meta.desc,
    selector: meta.sel,
    states: { ...(prev?.states || {}) },
  };
}

async function S(key, target, list, meta, opts = {}) {
  comp(key, meta);
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    if (Object.keys(out.components[key].states).length) out.components[key].recaptureMissed = new Date().toLocaleDateString('en-CA');
    else out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  for (const st of list) {
    let undo;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      let via = 'at rest';
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true, timeout: 3000 }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.waitForTimeout(250);
        via = 'clicked into the field; nothing typed that is submitted';
      } else if (st === 'filled') {
        await loc.click({ timeout: 3000 });
        await page.keyboard.type('name@example.com', { delay: 8 });
        await page.waitForTimeout(200);
        undo = async () => {
          await loc.focus();
          await page.keyboard.press('Meta+a');
          await page.keyboard.press('Backspace');
        };
        via = 'typed name@example.com, then deleted; nothing submitted';
      } else if (st === 'open') {
        await loc.click({ timeout: 3000 });
        await page.waitForTimeout(450);
        via = 'own disclosure opened; no form submitted';
      } else if (st === 'checked') {
        await loc.click({ timeout: 3000 });
        await page.waitForTimeout(200);
        undo = async () => { await loc.click().catch(() => {}); };
        via = 'checkbox toggled, then restored; nothing submitted';
      }
      const measureLoc = opts.measure?.[st] ? opts.measure[st]() : loc;
      await measure(key, st, measureLoc, { ...opts, via });
    } catch (e) {
      failState(key, st, e);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const q = (sel) => page.locator(sel);

const { browser, context: ctx } = await launch({ width: 1440, height: 900, dpr: 2 });
context = ctx;

try {
  await newPage('home', BASE + '/');
  const home = BASE + '/';

  await S('nav-button', q('.nav_button').first(), B4, {
    url: home, title: 'Nav pill', group: 'button',
    desc: 'White pill in the marketing nav. Text is "Start with Managed Payments". Radius 40px.',
    sel: '.nav_button',
  });

  await S('button-primary', q('.button-primary').first(), B4, {
    url: home, title: 'Primary button', group: 'button',
    desc: 'Frosted white pill on the dark hero. Label "Explore Managed Payments".',
    sel: '.button-primary',
  });

  await S('nav-link', q('.nav_link').first(), B4, {
    url: home, title: 'Nav link', group: 'link',
    desc: 'Docs / Help text links in the marketing nav.',
    sel: '.nav_link',
  });

  await S('banner', q('.banner').first(), ['default'], {
    url: home, title: 'Shutdown banner', group: 'banner',
    desc: 'Yellow announcement bar: sign-ups closed, shutdown 31 March 2027.',
    sel: '.banner',
  }, { pad: 0 });

  await S('footer-link', q('.footer_component a').filter({ hasText: 'Privacy' }).first(), B4, {
    url: home, title: 'Footer link', group: 'link',
    desc: 'Legal link in the blue footer.',
    sel: '.footer_component a',
  });

  await S('faq', q('.section-faq.landing-page .accordion_question, .landing-page .accordion_question').first(), ['default', 'hover', 'open'], {
    url: home, title: 'FAQ row', group: 'accordion',
    desc: 'Numbered FAQ question on the home page. Opened by its own disclosure.',
    sel: '.accordion_question',
  });

  await S('logo', q('.nav_logo-link, .w-nav-brand').first(), ['default'], {
    url: home, title: 'Wordmark', group: 'logo',
    desc: 'Lemon Squeezy wordmark in the nav.',
    sel: '.nav_logo-link',
  });

  await newPage('pricing', BASE + '/pricing');
  await S('price-card', q('h2').filter({ hasText: /5%|\$0/ }).first(), ['default'], {
    url: BASE + '/pricing', title: 'Price', group: 'card',
    desc: 'Published price headline on the pricing page.',
    sel: 'h2',
  }, { pad: 24 });

  await S('text-link', q('.text-style-link').first(), B4, {
    url: BASE + '/pricing', title: 'Inline link', group: 'link',
    desc: 'Violet inline link on the pricing page.',
    sel: '.text-style-link',
  });

  await newPage('help', BASE + '/help');
  await S('button-orchid', q('.button-primary-small').first(), B4, {
    url: BASE + '/help', title: 'Orchid pill', group: 'button',
    desc: 'Translucent orchid pill on the help centre ("View the docs").',
    sel: '.button-primary-small',
  });

  await newPage('about', BASE + '/about');
  await S('button-yellow', q('.button-primary-small.background-color-yellow-500, a.background-color-yellow-500').first(), B4, {
    url: BASE + '/about', title: 'Yellow pill', group: 'button',
    desc: 'Yellow founder pill on About.',
    sel: '.background-color-yellow-500',
  });
  await S('button-green', q('a.background-color-green-500').first(), ['default', 'hover'], {
    url: BASE + '/about', title: 'Green pill', group: 'button',
    desc: 'Green founder pill on About.',
    sel: '.background-color-green-500',
  });
  await S('button-purple', q('a.background-color-purple-500').first(), ['default', 'hover'], {
    url: BASE + '/about', title: 'Purple pill', group: 'button',
    desc: 'Purple founder pill on About.',
    sel: '.background-color-purple-500',
  });

  await newPage('docs', DOCS + '/help');
  await S('docs-search', q('button').filter({ hasText: /search/i }).first(), B4, {
    url: DOCS + '/help', title: 'Search button', group: 'button',
    desc: 'Docs search trigger. Opens a search dialog; the query is not submitted as a form to an account.',
    sel: 'button[aria-label*=search]',
  });
  await S('docs-nav', q('a').filter({ hasText: /^Getting paid$/ }).first(), B4, {
    url: DOCS + '/help', title: 'Docs nav row', group: 'list-row',
    desc: 'Sidebar row in the Mintlify docs nav.',
    sel: 'docs sidebar link',
  });
  await S('docs-cta', q('a').filter({ hasText: /Managed Payments/ }).first(), B4, {
    url: DOCS + '/help', title: 'Docs pill CTA', group: 'button',
    desc: 'White pill in the docs header.',
    sel: 'header pill',
  });

  // Open the docs search dialog and crop it. Typing a query is a local filter,
  // not a form submit. We open it and leave the field empty.
  await reset();
  const searchBtn = q('button').filter({ hasText: /search/i }).first();
  if (await searchBtn.count()) {
    await searchBtn.click().catch(() => {});
    await page.waitForTimeout(600);
    const dialog = q('[role="dialog"], [cmdk-dialog], [data-search], input[placeholder*="Search" i], input[type="search"]').first();
    if (await dialog.count()) {
      await S('docs-search-dialog', q('[role="dialog"]').first(), ['default'], {
        url: DOCS + '/help', title: 'Search dialog', group: 'dialog',
        desc: 'Docs search dialog opened from its own button. No query submitted.',
        sel: '[role="dialog"]',
      }, { pad: 8 });
    }
    await page.keyboard.press('Escape').catch(() => {});
  }

  await newPage('login', AUTH + '/login');
  const login = AUTH + '/login';
  await S('login-google', q('a').filter({ hasText: /Google/ }).first(), B4, {
    url: login, title: 'Google button', group: 'button',
    desc: 'OAuth button on the sign-in card. Measured, never followed.',
    sel: 'a[href*="google"]',
  });
  await S('login-email', q('input[type="email"], input[name="email"]').first(), ['default', 'hover', 'focus-visible', 'focused', 'filled'], {
    url: login, title: 'Email field', group: 'text-field',
    desc: 'Email field on the sign-in card. Sample text typed and deleted. Nothing submitted.',
    sel: 'input[type=email]',
  });
  await S('login-password', q('input[type="password"]').first(), ['default', 'focused'], {
    url: login, title: 'Password field', group: 'text-field',
    desc: 'Password field at rest and focused. Nothing typed.',
    sel: 'input[type=password]',
  });
  await S('login-submit', q('button[type="submit"], button.btn-primary').first(), ['default', 'hover', 'focus-visible', 'pressed'], {
    url: login, title: 'Sign-in button', group: 'button',
    desc: 'Purple submit on the sign-in card. States forced with CSS. Never clicked.',
    sel: 'button.btn-primary',
  });
  await S('login-remember', q('input[type="checkbox"]').first(), ['default', 'checked', 'focus-visible'], {
    url: login, title: 'Remember me', group: 'checkbox',
    desc: 'Remember-me checkbox. Toggled and restored. Nothing submitted.',
    sel: 'input[type=checkbox]',
  });
  await S('login-link', q('a').filter({ hasText: /Forgot your password/ }).first(), B4, {
    url: login, title: 'Secondary link', group: 'link',
    desc: 'Forgot-password link. Measured, never followed.',
    sel: 'a[href*="password"]',
  });

  await newPage('register', 'https://auth.lemonsqueezy.com/register');
  await S('select-country', q('select').first(), ['default', 'focused'], {
    url: 'https://auth.lemonsqueezy.com/register', title: 'Country select', group: 'select',
    desc: 'Country select on the business-intent step. Opened for focus only. Nothing submitted.',
    sel: 'select',
  });
  await S('register-name', q('input[type="text"]').first(), ['default', 'focused'], {
    url: 'https://auth.lemonsqueezy.com/register', title: 'Text field', group: 'text-field',
    desc: 'Business name field. Focused, never filled, never submitted.',
    sel: 'input[type=text]',
  });

  // Mobile menu, 390.
  await page.close().catch(() => {});
  const mob = await context.browser().newContext({
    viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true,
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  });
  page = await mob.newPage();
  cdp = await mob.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = 'mobile-home';
  await open(page, BASE + '/', { wait: 1600 });
  await S('menu-button', q('.w-nav-button, .nav_menu-mobile-button').first(), ['default', 'hover'], {
    url: home, title: 'Menu button', group: 'icon-button',
    desc: 'Hamburger that opens the mobile nav. Opened for the menu shot, never used to sign in.',
    sel: '.w-nav-button',
  });
  const menuBtn = q('.w-nav-button, .nav_menu-mobile-button').first();
  if (await menuBtn.count()) {
    await menuBtn.click().catch(() => {});
    await page.waitForTimeout(500);
    await S('mobile-menu', q('.w-nav-menu').first(), ['default'], {
      url: home, title: 'Mobile menu', group: 'menu',
      desc: 'Opened mobile nav overlay.',
      sel: '.w-nav-menu',
    }, { pad: 0 });
  }
  await mob.close();
} finally {
  save();
  await browser.close();
}
console.log('wrote', OUT, 'components', Object.keys(out.components).length);
