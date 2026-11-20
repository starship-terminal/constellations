// Measures gofundme.com's public components in every state reachable without
// signing in, donating or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home discover search fundraiser pricing signin create mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// www.gofundme.com is a Next.js app on its "hrt" design system: the declared
// token layer is the ~700 `--hrt-*` custom properties on :root (the consumer
// light theme; the [data-theme="pro"] layer in the CSS never paints on these
// surfaces). The /c/* marketing pages (pricing, how-it-works, …) are the
// WordPress content stack — an older hrt-base-* layer over wp-* blocks —
// measured as a second public system. /sign-in is the auth boundary: the
// Welcome card (Google/Apple/email + Continue) paints for a signed-out
// visitor — in some headless passes the island fails to hydrate and only a
// shell records. The form is measured, never submitted.
//
// Nothing is sent, bought or signed into: the only activations are local UI
// toggles — a header dropdown (hover), the mobile nav button. The wizard's
// postcode field is typed into and cleared, never submitted; "Donate now",
// "Share", "Message", "Continue", "Sign in" and every CTA are measured,
// never followed. The Transcend consent layer is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', discover: '/discover', search: '/s?q=medical', pricing: '/c/pricing', signin: LOGIN_URL, create: '/create/fundraiser/category', mobile: '/', fundraiser: null };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null, allowEmpty = false } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!allowEmpty && await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink });
          await page.waitForTimeout(900);
          // A collapsible that reports expansion must still be open when its
          // "opened" reading is taken; a control without the attribute is
          // trusted (some toggles expose no state).
          const expanded = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
          if (expanded === 'false') throw new Error('the opened state measured closed (aria-expanded="false" after the toggle)');
          via = 'own toggle';
        }
      } else if (st === 'closed') {
        await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, accordion, sheet trigger). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|get started for free|claim|share|export|select|continue|continue with.*|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(8000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'Site chrome', home: 'Home', discover: 'Discover', search: 'Search',
  fundraiser: 'Fundraiser page', pricing: 'Pricing (content stack)', create: 'Start-a-fundraiser wizard',
  auth: 'Sign-in boundary', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's Donate mega-dropdown: hover on the first
// .hrt-header-dropdown-button opens the panel, which carries
// .hrt-header-dropdown-content--open (closed panels stay mounted with
// visibility:hidden — the class, not the rect, is the state). The panel is
// tagged data-mjs-panel so the spec locator is a plain attribute match; its
// links are never followed.
async function openHeaderMenu() {
  const open = async () => page.evaluate(() => {
    const el = document.querySelector('.hrt-header-dropdown-content--open');
    if (!el) return false;
    el.setAttribute('data-mjs-panel', '1');
    return true;
  }).catch(() => false);
  if (await open()) return 'a header dropdown was already open';
  const btn = page.locator('button.hrt-header-dropdown-button').filter({ hasText: /^Donate/ }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Donate trigger';
  for (let i = 0; i < 4; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(1200);
    if (await open()) return 'hovered the "Donate" trigger to open the dropdown';
    if (i === 1) await btn.click({ timeout: 3000 }).catch(() => {});
  }
  return 'hovered "Donate"; the dropdown did not report open';
}

// Opens the mobile nav overlay at 390 wide. gofundme.com replaces the
// desktop header row with a hamburger button; the overlay it opens is a
// fixed panel carrying the nav links.
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body *')].filter((x) => {
      if (x === document.body || x === document.documentElement) return false;
      const cs = getComputedStyle(x);
      const r = x.getBoundingClientRect();
      const t = (x.innerText || '');
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.width > 300 && r.height > 400
        && /Donate|Fundraise|Start a GoFundMe/.test(t) && /Sign in|Discover|Search/.test(t);
    }).sort((a, b) => a.innerText.length - b.innerText.length)[0];
    if (!el) return false;
    el.setAttribute('data-mjs-overlay', '1');
    return true;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('button[aria-label="menu" i], button.hrt-icon-button[aria-label], button[aria-label*="navigation" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the menu toggle to open the mobile nav';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused the menu toggle and pressed Enter to open the mobile nav';
  }
  return 'activated the nav toggle; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];
const B4H = ['default', 'hover', 'focus-visible', 'pressed'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell, h = G.home, f = G.footer;
  await S('mkt-promo', q('.hrt-global-promo-banner').filter({ visible: true }).first(), ['default'], { group: g, title: 'Global promo banner', desc: 'The dismissal strip above the header ("Introducing the Kind 50…"); its close icon-button was never pressed.', sel: '.hrt-global-promo-banner' }, { noScroll: true });
  await S('mkt-header', q('header, .hrt-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The sticky bar on every consumer page: the GoFundMe mark, Donate/Fundraise/About dropdown triggers, Search, "Sign in" and "Start a GoFundMe".', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"], .hrt-header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The GoFundMe mark in the header, linking home.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-search', q('a[class*="search-button" i], header a').filter({ hasText: /^Search$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Nav search button', desc: 'The "Search" header button (search-field styling) to /s; measured, never followed.', sel: 'header Search button' }, { noScroll: true });
  await S('nav-donate-dd', q('button.hrt-header-dropdown-button').filter({ hasText: /^Donate/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Nav dropdown trigger', desc: 'The "Donate" header item whose dropdown opens on hover (panel measured next; links never followed).', sel: 'button.hrt-header-dropdown-button Donate' }, { noScroll: true });
  await S('nav-panel', q('[data-mjs-panel]'), ['default'], { group: g, title: 'Header dropdown panel', desc: 'The mega-dropdown panel under "Donate" (multi-column link groups); opened by hovering the trigger, its links never followed.', sel: '.hrt-header-dropdown-content--open' }, { open: openHeaderMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(1438, 890).catch(() => {});
  await S('nav-about-dd', q('button.hrt-header-dropdown-button').filter({ hasText: /^About/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'About dropdown trigger', desc: 'The "About" header item — the right-aligned dropdown trigger; its panel was never opened beyond the one menu reading.', sel: 'button.hrt-header-dropdown-button About' }, { noScroll: true });
  await S('nav-signin', q('header a, .hrt-header a, header + * a').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Sign in link', desc: 'The "Sign in" header link (tertiary button styling) to /sign-in; measured, never followed.', sel: 'header Sign in' }, { noScroll: true });
  await S('nav-start', q('header a, .hrt-header a').filter({ hasText: /^Start a GoFundMe$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Header CTA', desc: 'The pill "Start a GoFundMe" header button (secondary hierarchy); links to the wizard, measured never followed.', sel: 'header Start a GoFundMe' }, { noScroll: true });

  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"Where successful fundraisers start" — the home hero display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('[class*="hero" i] a.hrt-button, main a.hrt-button--hierarchy-primary').filter({ hasText: /^Start a GoFundMe$/ }).filter({ visible: true }).first(), B4H, { group: h, title: 'Hero CTA', desc: 'The primary "Start a GoFundMe" button in the hero; links to the wizard, measured never followed.', sel: 'hero Start a GoFundMe' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  await S('collection-btn', q('button[class*="collection-selector" i]').filter({ visible: true }).first(), B4H, { group: h, title: 'Collection selector', desc: 'A "Happening worldwide"-style collection filter pill; measured at rest, never toggled (toggling would re-filter the rail).', sel: 'collection-selector button' });
  await S('card-media-tag', q('.hrt-media-tag, .hrt-tag').filter({ visible: true }).first(), ['default'], { group: h, title: 'Media tag', desc: 'A location tag chip overlaid on a fundraiser card image ("Blaine, Minnesota" and neighbours).', sel: '.hrt-media-tag' });
  await S('pause-motion-btn', q('button[aria-label*="pause" i], button[aria-label*="motion" i]').filter({ visible: true }).first(), B4H, { group: h, title: 'Pause-motion icon button', desc: 'The reduced-motion control on the how-it-works steps; an icon-only button, measured never pressed.', sel: 'button[aria-label*="pause" i]' });
  await S('carousel-btn', q('button[aria-label*="forward" i], button[aria-label*="next" i]').filter({ visible: true }).first(), B4H, { group: h, title: 'Carousel arrow', desc: 'A forward arrow icon-button on a fundraiser rail; measured never pressed (it would scroll the rail).', sel: 'button[aria-label*="forward" i]' });
  await S('merch-card', q('[class*="merch-card" i] a, a[class*="merch-card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Featured merch card', desc: 'A featured-topic merch card link (large image card); measured at rest and on hover, never followed.', sel: 'merch-card link' });

  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: column links, social icons, the locale selector and the Transcend consent link.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /^Careers$/ }).first(), B4H, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Careers' });
  await S('footer-more', q('footer button').filter({ hasText: /More resources|Resources/ }).filter({ visible: true }).first(), B4H, { group: f, title: 'Footer accordion', desc: 'A footer accordion button ("More resources"); measured at rest, never toggled.', sel: 'footer More resources button' });
  await S('locale-btn', q('footer button, footer a').filter({ hasText: /United States|English/ }).filter({ visible: true }).last(), B4H, { group: f, title: 'Locale selector', desc: 'The "United States · English" locale control in the footer; measured, never opened (opening would offer a locale switch).', sel: 'footer locale button' });
  await S('cookie-btn', q('.transcend-consent-link, footer button, footer a').filter({ hasText: /Manage Cookie Preferences/i }).filter({ visible: true }).first(), B4H, { group: f, title: 'Cookie preferences link', desc: 'The "Manage Cookie Preferences" Transcend footer control; measured, never pressed (it would open the consent manager).', sel: '.transcend-consent-link' });
  save();
}

async function discover() {
  if (!(await newPage('discover'))) return;
  const g = G.discover;
  await S('disc-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Discover headline', desc: 'The /discover masthead ("Fundraisers" and the result count).', sel: 'h1' }, { noScroll: true });
  await S('disc-cat-btn', q('button').filter({ hasText: /Show more categories|categories/i }).filter({ visible: true }).first(), B4H, { group: g, title: 'Category expander', desc: 'The "Show more categories" button under the category chips; measured at rest, never toggled.', sel: 'Show more categories' });
  // The fundraiser grid mounts when it scrolls into view (intersection-lazy):
  // scroll through the page once so the card selectors have something to hit.
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.4));
  await page.waitForTimeout(2500);
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.8));
  await page.waitForTimeout(2500);
  await S('fundraiser-card', q('[class*="fundraiser-card_container" i], [class*="fundraiserCard" i], .hrt-fundraiser-card').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Fundraiser card', desc: 'A discover-grid fundraiser card (image, location tag, title, raised line, progress bar); measured at rest and on hover, never followed.', sel: '[class*=fundraiser-card]' });
  await S('card-title', q('[class*="fundraiser-card" i] h3, h3[class*="fundraiser-card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card title', desc: 'The fundraiser title inside a discover card.', sel: '.fundraiser-card title' });
  await S('card-goal-bar', q('[class*="fundraiser-card" i] progress, [class*="fundraiser-card" i] [class*="progressBar" i], .hrt-goal-bar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Goal bar (card)', desc: 'The progress element inside a discover card.', sel: 'card progress' });
  await S('card-location', q('[class*="mediaTag" i], .hrt-media-tag').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card location tag', desc: 'The location tag chip overlaid on a card image.', sel: '[class*=mediaTag]' });
  save();
}

async function search() {
  if (!(await newPage('search'))) return;
  const g = G.search;
  await S('s-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search headline', desc: 'The /s results masthead.', sel: 'h1' }, { noScroll: true });
  await S('s-card', q('[class*="fundraiser-card_container" i], [class*="fundraiserCard" i], .hrt-fundraiser-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search result card', desc: 'A fundraiser card in the /s?q=medical results grid; measured, never followed.', sel: '[class*=fundraiser-card]' });
  await S('s-avatar', q('.hrt-avatar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Avatar', desc: 'An hrt-avatar on a search result (the organiser image).', sel: '.hrt-avatar' });
  save();
}

async function fundraiser() {
  if (!(await newPage('fundraiser', { url: null, wait: 12000 }))) return;
  const g = G.fundraiser;
  await S('f-title', await domFind(page, /\S/, { sel: 'h1', tag: 'ft', minW: 100, minH: 10 }), ['default'], { group: g, title: 'Fundraiser title', desc: 'The campaign title h1 on a public /f/<slug> page.', sel: 'h1' }, { noScroll: true });
  await S('f-raised', q('h2, [class*="raised" i], [class*="amount" i]').filter({ hasText: /raised/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Raised amount', desc: 'The "$X raised of $Y goal" line.', sel: 'raised amount line' }, { noScroll: true });
  await S('f-goal-bar', q('[class*="progress-meter" i], .hrt-goal-bar, main progress, [class*="progressBar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Goal bar (fundraiser)', desc: 'The progress element beside the raised line (a progress-meter on the campaign pages).', sel: 'progress-meter' }, { noScroll: true });
  await S('f-donate', q('a[class*="donate-button" i], a[class*="donateButton" i]').filter({ visible: true }).first(), B4H, { group: g, title: 'Donate button', desc: 'The primary "Donate now" button; all four states measured, the button never pressed — no donation was ever started.', sel: 'a.donate-button' }, { noScroll: true });
  await S('f-share', q('xpath=//a[not(ancestor::header)] | //button[not(ancestor::header)]').filter({ hasText: /^Share$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Share button', desc: 'The secondary "Share" button; states measured, never pressed.', sel: 'Share' }, { noScroll: true });
  await S('f-message', q('xpath=//a[not(ancestor::header)] | //button[not(ancestor::header)]').filter({ hasText: /^Message$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Message button', desc: 'The "Message" button beside Share; states measured, never pressed.', sel: 'Message' }, { noScroll: true });
  await S('f-readmore', q('xpath=//a[not(ancestor::header)] | //button[not(ancestor::header)]').filter({ hasText: /^Read more$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Read more', desc: 'The text-button expanding the campaign story; measured at rest, never toggled.', sel: 'Read more' });
  await S('f-avatar', q('.hrt-avatar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Organiser avatar', desc: 'The organiser avatar in the campaign meta row.', sel: '.hrt-avatar' });
  // The "Donations" section is deep in the document under content-visibility;
  // scroll it into view first so the heading reports a real box.
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.7));
  await page.waitForTimeout(2000);
  await S('f-donations-h2', await domFind(page, /^Donations/, { sel: 'h2, h3', tag: 'fdh', minW: 80, minH: 10 }), ['default'], { group: g, title: 'Donations heading', desc: 'The "Donations (N)" section heading above the supporter list.', sel: 'h2 Donations' });
  await S('f-media-nav', q('button[aria-label*="next" i], button[aria-label*="forward" i]').filter({ visible: true }).first(), B4H, { group: g, title: 'Media viewer arrow', desc: 'An arrow icon-button on the fundraiser media viewer; measured never pressed.', sel: 'media next button' });
  await S('f-report', q('button, a').filter({ hasText: /Report fundraiser/i }).filter({ visible: true }).first(), B4H, { group: g, title: 'Report link', desc: 'The "Report fundraiser" text-button; measured, never pressed.', sel: 'Report fundraiser' });
  await S('f-collection', q('button[class*="collection-selector" i]').filter({ visible: true }).first(), B4H, { group: g, title: 'Collection pill (page)', desc: 'The "Nearby"-style collection filter pill on the related-fundraisers rail; measured at rest, never toggled.', sel: 'collection-selector button' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  // /c/* pages are the WordPress content stack — an older hrt-base-*
  // component layer over wp-* blocks, not the consumer app's hrt button
  // hierarchy. Measurements here document that second public system.
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Simple pricing, powerful fundraising" — the /c/pricing masthead on the WordPress content stack.', sel: 'h1' }, { noScroll: true });
  await S('price-toggle', q('input.toggle').filter({ visible: true }).first().locator('xpath=..'), B4H, { group: g, title: 'Audience toggle', desc: 'An "Individual or business / Certified nonprofit" segment toggle on the fee section; measured at rest, never switched (switching would re-tab the fees).', sel: 'input.toggle wrapper' });
  await S('price-faq', q('input[name^="faq"]').filter({ visible: true }).first().locator('xpath=..'), ['default', 'hover'], { group: g, title: 'FAQ row', desc: 'A CSS-disclosure FAQ row (checkbox + label) in the pricing FAQ; measured at rest, never opened.', sel: 'faq checkbox row' });
  // Every hrt-base-button on /c/pricing lives in the shared header, so the
  // content CTA must come from the page body only — wp-block buttons first.
  await S('wp-button', q('xpath=(//a[contains(@class,"wp-block-button") or contains(@class,"hrt-base-button")] | //button[contains(@class,"wp-block-button")])[not(ancestor::header) and not(ancestor::nav) and not(ancestor::footer)]').filter({ hasNotText: /skip to content/i }).filter({ visible: true }).first(), B4H, { group: g, title: 'Content CTA', desc: 'A wp-block button on the content stack; measured, never followed.', sel: 'wp-block-button' });
  await S('wp-locale', q('select.wp-language-switcher').filter({ visible: true }).first(), B4H, { group: g, title: 'Locale select (content stack)', desc: 'The WordPress language switcher in the content-stack footer; measured, never changed.', sel: 'select.wp-language-switcher' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { url: LOGIN_URL, wait: 15000, allowEmpty: true }))) return;
  const g = G.auth;
  // /sign-in is the auth boundary: the Welcome card — "Sign in with Google",
  // "Continue with Apple", the email field and "Continue" — paints for a
  // signed-out visitor. (In some headless passes the island fails to hydrate
  // and only a shell records.) Every control is measured, none pressed: a
  // press would start an auth or account action.
  // The island hydrates asynchronously: give the Welcome card up to 20s to
  // mount before treating the pass as a shell-only reading.
  await page.waitForSelector('input[type="email"], input[placeholder*="mail" i], form', { timeout: 20000 }).catch(() => {});
  const emailLoc = q('input[type="email"], input[placeholder*="mail" i], form input').filter({ visible: true }).first();
  // The card has no semantic wrapper (no form/main), so measure the nearest
  // ancestor of the email field that also holds a button — the Welcome card.
  const cardLoc = (await emailLoc.count())
    ? emailLoc.locator('xpath=ancestor::*[.//button or .//a[@role="button"]][1]')
    : q('form, main, body');
  await S('signin-shell', cardLoc.filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The /sign-in document: the Welcome card a signed-out visitor gets — Google/Apple buttons, an email field and Continue. Never submitted.', sel: 'sign-in form' }, { noScroll: true });
  await S('signin-email', emailLoc, FIELD, { group: g, title: 'Email field', desc: 'The "Email Address" field on the sign-in card; focused, typed into and cleared — never submitted.', sel: 'input[type=email]' }, { fillText: 'name@example.com' });
  await S('signin-continue', q('button, [role="button"]').filter({ hasText: /^Continue\b/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Continue button', desc: 'The sign-in card\'s primary "Continue" button; all four states measured with hover/focus/forced-active only — it was never clicked.', sel: 'Continue' });
  await S('signin-google', q('button, a, [role="button"]').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4H, { group: g, title: 'Google button', desc: 'The "Sign in with Google" button; measured at rest and on hover/focus, never pressed (a press would start OAuth).', sel: 'Sign in with Google' });
  save();
}

async function create() {
  if (!(await newPage('create'))) return;
  const g = G.create;
  await S('create-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wizard headline', desc: '"Let\'s begin your fundraising journey" — the /create/fundraiser/category masthead, captured at rest before any step was submitted.', sel: 'h1' }, { noScroll: true });
  await S('create-country', q('select.hrt-select-field-select').filter({ visible: true }).first(), B4H, { group: g, title: 'Country select', desc: 'The "Select your country" select; measured at rest, never changed (changing would re-price the currency).', sel: 'select.hrt-select-field-select' });
  await S('create-zip', q('input.hrt-text-field-input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Postcode field', desc: 'The postcode text field; focused and typed into then cleared — the step was never submitted.', sel: 'input.hrt-text-field-input' }, { fillText: '94107' });
  await S('create-pill', q('[class*="select-pills" i] label, [class*="selectPills" i] label, [class*="select-pills" i] li').filter({ visible: true }).first(), B4H, { group: g, title: 'Category pill', desc: 'A category radio pill (Animals, Business, Community…); measured at rest, never selected — selecting would be a wizard choice.', sel: 'select-pills label' });
  await S('create-continue', q('button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Continue button', desc: 'The wizard "Continue" button; states measured, never clicked — no wizard step was ever submitted.', sel: 'Continue' });
  await S('create-signin', q('a').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Wizard sign-in link', desc: 'The "Sign in" link above the wizard; measured, never followed.', sel: 'create Sign in' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  const g = G.mobile;
  await S('m-header', q('header, .hrt-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone header at 390 wide: the mark, the menu toggle and the start CTA.', sel: 'mobile header' }, { noScroll: true });
  await S('m-menu-btn', q('button[aria-label="menu" i], button.hrt-icon-button[aria-label*="menu" i]').filter({ visible: true }).first(), [...B4H, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile nav toggle' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('[data-mjs-overlay]'), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('[class*="hero" i] a.hrt-button, main a.hrt-button').filter({ hasText: /^Start a GoFundMe$/ }).filter({ visible: true }).first(), B4H, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Start a GoFundMe" button at 390 wide; measured never followed.', sel: 'mobile hero CTA' });
  save();
}

// The fundraiser page reads its slug the same way the shooter does: the first
// live /f/<slug> card on /discover.
async function resolveFundraiser() {
  if (URLS.fundraiser) return;
  try {
    const b = context.browser();
    const c2 = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
    await patch(c2);
    const p = await c2.newPage();
    await p.goto(BASE + '/discover', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(8000);
    const href = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href^="/f/"]')].find((x) => x.getBoundingClientRect().width > 0);
      return a && a.getAttribute('href');
    }).catch(() => null);
    URLS.fundraiser = href && /^\/f\/[\w-]+/.test(href) ? href.match(/^\/f\/[\w-]+/)[0] : '/f/help-jong-pil-kim-keep-mun-korean-steakhouse-alive';
    out._meta.fundraiserUrl = URLS.fundraiser;
    await c2.close();
  } catch { URLS.fundraiser = '/f/help-jong-pil-kim-keep-mun-korean-steakhouse-alive'; out._meta.fundraiserUrl = URLS.fundraiser; }
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every consumer surface on www.gofundme.com paints the :root-declared --hrt-* consumer light theme (no theme switcher exists on the consumer site; a [data-theme="pro"] layer exists in the CSS but never paints here); /c/* pages are the WordPress content stack, an older hrt-base-* layer; /sign-in is the auth boundary — the Welcome card measured signed-out, never submitted';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
await resolveFundraiser();
const pages = process.argv.slice(2);
const plan = { home, discover, search, fundraiser, pricing, signin, create, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a header link's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a, .hrt-header a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
