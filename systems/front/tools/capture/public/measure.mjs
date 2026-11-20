// Measures front.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing product request-demo signup signin signin-dark
//        signup-app forgot help help-article dev dev-ref mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// front.com is four public stacks signed out. The marketing pages are a
// Next.js + Tailwind app whose design layer is compiled into bespoke classes
// (.button-primary-violet, .surface-l*, .text-display*) under three section
// themes ([data-theme=theme-dark-violet] the plum default, theme-white,
// theme-gray); the marketing page itself offers no theme switch. app.frontapp.com
// is the product SPA: its auth shell paints the real --color-* token layer and
// honours html[data-theme="dark"] (set via the front-theme-preference
// localStorage key; the dark pass sets it with an init script and a dark
// context). help.front.com is Front's own Knowledge Base product, and
// dev.frontapp.com is the ReadMe vendor platform. Both embed Front's own
// Companion messenger (companion.frontapp.com, the @layer tokens sheet with
// the product's full --color-* vocabulary).
//
// Nothing is sent, booked, created or signed into. The only presses are local
// UI toggles: the header's Product/Solutions/Resources mega menus, the pricing
// billing switch and FAQ disclosures, the mobile burger, the help centre's own
// nav. The OneTrust banner is hidden, never answered; the Qualified "Quinn"
// launcher is measured at rest, never opened. Sign in, Request a demo, Try for
// free, the auth buttons and the form submits are measured, never followed or
// pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, HELP, DEV, SIGNIN_URL, SIGNUP_URL, FORGOT_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', product: '/product', 'request-demo': '/request-demo', signup: '/signup',
  signin: SIGNIN_URL, 'signin-dark': SIGNIN_URL, 'signup-app': SIGNUP_URL, forgot: FORGOT_URL,
  help: HELP + '/', 'help-article': HELP + '/en/', dev: DEV + '/docs/welcome', 'dev-ref': DEV + '/reference/getting-started',
  mobile: '/',
};
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

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null, theme = 'light' } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: theme });
  await patch(ctx);
  // The app shell reads front-theme-preference from localStorage and falls
  // back to prefers-color-scheme; set both so the dark pass is the product's
  // own switch, not an emulated paint.
  if (theme === 'dark') await ctx.addInitScript(() => { try { localStorage.setItem('front-theme-preference', 'dark'); } catch { /* before origin */ } });
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', theme === 'dark' ? '(dark)' : '');
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|get started for free|claim|share|export|select|continue|continue with.*|claim this offer|try again|try for free|request a demo|talk to sales|book a demo)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', forms: 'Demo and signup forms',
  auth: 'Auth shell (app.frontapp.com)', help: 'Help centre (help.front.com)',
  dev: 'Developer portal (dev.frontapp.com)', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens a header mega menu by its button label: Product | Solutions |
// Resources. A pointer click is the activation, keyboard Enter the fallback —
// a local UI toggle, never a link. Escape closes it afterwards.
const megaMenu = (label) => async () => {
  const btn = page.locator('header button').filter({ hasText: new RegExp(`^${label}$`) }).first();
  if (!(await btn.count())) return `no ${label} trigger`;
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return `the ${label} menu was already open`;
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(800);
    if (await open()) return `clicked the "${label}" trigger to open the mega menu`;
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(800);
    if (await open()) return `focused the "${label}" trigger and pressed Enter to open the mega menu`;
  }
  return `activated "${label}"; the menu did not report open`;
};

// Opens the mobile nav: the burger button labelled "Open menu". Pointer first,
// then Enter.
async function openMobileMenu() {
  const b = page.locator('button.button-mobile-menu-trigger, button[aria-label*="menu" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = async () => (await b.getAttribute('aria-expanded').catch(() => null)) === 'true' || await page.locator('[class*="mobile-menu" i][class*="open" i], nav[class*="open" i]').first().isVisible().catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the burger to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused the burger and pressed Enter to open the nav overlay';
  }
  return 'activated the burger; the overlay did not report open';
}

async function home() {
  if (!(await newPage('home', { wait: 10000, promo: 'none' }))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The Qualified widget is measured at rest before anything is hidden —
  // a vendor surface, never opened or typed into.
  await S('quinn-launcher', q('#qualified-multimodal-host, [id*="qualified" i] iframe, iframe[id*="q-widget" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Quinn widget (vendor)', desc: 'The Qualified "Quinn" chat widget host pinned bottom-right — a vendor surface, measured at rest and never opened or typed into.', sel: '#qualified-multimodal-host' }, { noScroll: true, crop: false });
  await closePromo(page);
  await chrome('home');
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar on every marketing page: the Front wordmark, Product/Solutions/Resources mega-menu triggers, AI, Customers, Pricing, Sign in, Request a demo and Try for free.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Front wordmark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-menu-btn', q('header button').filter({ hasText: /^Product$/ }).first(), [...B4, 'opened'], { group: g, title: 'Mega-menu trigger', desc: 'The "Product" header button — a local UI toggle whose mega menu mounts under the header; the opened state was measured after its own click (aria-expanded had to stay true).', sel: 'header button Product' }, { noScroll: true });
  await S('nav-panel', q('header [class*="shadow-header" i], header [class*="rounded-20" i]').filter({ hasText: /Platform Overview|Omnichannel|Autopilot/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The panel opened by the "Product" trigger (product entries with icons and descriptions); its links were never followed.', sel: 'product mega-menu panel' }, { open: megaMenu('Product'), noScroll: true, noReset: true });
  await S('nav-menu-item', q('header a').filter({ hasText: /Omnichannel|Autopilot|Ticketing|Copilot/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega-menu item', desc: 'A product entry inside the opened mega menu; measured, never followed.', sel: 'mega menu item' }, { open: megaMenu('Product'), noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', q('header a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-signin', q('header a').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The "Sign in" header link to app.frontapp.com/signin; measured, never followed.', sel: 'header a Sign in' }, { noScroll: true });
  await S('nav-demo', q('header a, header button').filter({ hasText: /^Request a demo$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Request-demo button', desc: 'The "Request a demo" header action (a bordered secondary button); links to /request-demo, measured never followed.', sel: 'header Request a demo' }, { noScroll: true });
  await S('nav-try', q('header a, header button').filter({ hasText: /^Try for free$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Try-free button', desc: 'The "Try for free" header action; links to /signup, measured never followed.', sel: 'header Try for free' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"All your teams. All your AI agents. One place to …" — the display1 masthead.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').locator('xpath=following::*[self::p or self::div][1]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subcopy', desc: 'The paragraph under the hero headline (text-p1).', sel: 'hero p' });
  await S('hero-cta', q('main a, main button, section a, section button, a, button').filter({ hasText: /^Request demo$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Request demo" button under the hero copy — the hero\'s single CTA; links to /request-demo, measured never followed.', sel: 'hero Request demo' });
  await S('section-heading', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'The first h2 section heading below the hero.', sel: 'h2' });
  await S('dark-violet-section', q('[data-theme="theme-dark-violet"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Plum section', desc: 'A section themed [data-theme=theme-dark-violet] — the marketing site\'s signature dark-plum surface (surface-l0 #300c41, text-primary #f8f1fe).', sel: '[data-theme=theme-dark-violet]' }, { crop: false });
  await S('gray-section', q('[data-theme="theme-gray"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Gray section', desc: 'A section themed [data-theme=theme-gray].', sel: '[data-theme=theme-gray]' }, { crop: false });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Site footer', desc: 'The footer on every marketing page — "The AI customer operations platform.", the link columns, certifications and legal row.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ visible: true }).first(), ['default', 'hover'], { group: f, title: 'Footer link', desc: 'A link in the footer columns; measured, never followed.', sel: 'footer a' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: 'The first heading on /pricing (the page carries no h1; the first h2 is measured instead).', sel: 'pricing h1/h2' }, { noScroll: true });
  await S('billing-toggle', q('label:has(input.peer), [role="switch"], [class*="switch" i]').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Billing switch', desc: 'The "Billed Annually"/"SAVE 24%" switch — a local UI toggle that repaints the plan prices; the opened state is the monthly-billed side, toggled and restored.', sel: 'pricing billing switch' }, { allowLink: true, noScroll: true });
  // A plan tier card is a rounded-[24px] white column inside the pricing grid —
  // an unscoped first match hits the full-width "Front AI Add-ons" section.
  await S('plan-card', q('div[class*="bg-white"][class*="rounded-[24px]"], [class*="grid-cols-4"] > *').filter({ hasText: /\/seat\/mo|per seat/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing tier card (name, price per seat/month, feature list, CTA) — the Starter column of the plan grid.', sel: 'plan card' });
  // The CTA inside a plan card, never the header's same-named button.
  await S('plan-cta', q('div[class*="bg-white"][class*="rounded-[24px]"] button, [class*="grid-cols-4"] button').filter({ hasText: /^Try for Free$|^Request a Demo$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Try for Free" action (the first tier column\'s button); links to /signup, measured never followed.', sel: 'plan card Try for Free' });
  await S('sales-link', q('a, button').filter({ hasText: /^Talk to sales$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Talk-to-sales link', desc: 'The "Talk to sales" action in the pricing hero; links to /request-demo, measured never followed.', sel: 'Talk to sales' }, { noScroll: true });
  await S('faq-item', q('button').filter({ hasText: /What is a seat\?/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ disclosure', desc: 'A "Frequently asked questions" disclosure button ("What is a seat?") — a local UI toggle whose answer mounts below; opened by its own click, left open for the shot.', sel: 'pricing FAQ disclosure' });
  await S('faq-answer', q('div, p').filter({ hasText: /A seat is/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'FAQ answer', desc: 'The answer text revealed by the FAQ disclosure.', sel: 'FAQ answer' }, { open: async () => { const b = q('button').filter({ hasText: /What is a seat\?/ }).first(); if (await b.count()) { const e = await b.getAttribute('aria-expanded').catch(() => null); if (e !== 'true') { await b.click(); await page.waitForTimeout(800); } } } });
  save();
}

async function product() {
  if (!(await newPage('product'))) return;
  await sheetsFor('product');
  const g = G.home;
  await S('product-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product headline', desc: 'The /product masthead.', sel: 'h1' }, { noScroll: true });
  await S('product-cta', q('main a, main button, section a, section button, a, button').filter({ hasText: /^Request demo$|^Try for free$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'The primary action on the product page; measured never followed.', sel: 'product CTA' });
  await S('feature-card', q('a[class*="col-span" i], a[class*="rounded-2" i]').filter({ hasText: /Customer Story|hours|saved|%|faster|CSAT/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Customer-story card', desc: 'A customer-outcome stat card on the product page (rounded-20, the grid cells that link into customer stories); measured, never followed.', sel: 'product stat card' });
  save();
}

async function requestDemo() {
  if (!(await newPage('request-demo', { wait: 9000 }))) return;
  await sheetsFor('request-demo');
  const g = G.forms;
  await S('demo-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo heading', desc: 'The first heading on /request-demo (no h1 ships; the first h2 is measured).', sel: 'request-demo h1/h2' }, { noScroll: true });
  await S('demo-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Work email field', desc: 'The work-email input on the demo form; focused and typed into then cleared — the form was never submitted.', sel: 'request-demo input[type=email]' }, { fillText: 'name@example.com' });
  await S('demo-field', q('select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Company-size select', desc: 'The company-size select on the demo form; focused, never changed or submitted.', sel: 'request-demo select' });
  // Scope to the form: an unscoped first match is the header's own "Request a
  // demo" button, not the submit under the fields.
  await S('demo-submit', q('form button, form [type="submit"], main button').filter({ hasText: /Request|Submit|Get|Book|Continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo submit', desc: 'The demo form\'s submit button; its states were measured but the button was never clicked — the form was never sent.', sel: 'request-demo form submit' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  await sheetsFor('signup');
  const g = G.forms;
  await S('signup-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup headline', desc: 'The marketing /signup masthead.', sel: 'signup h1' }, { noScroll: true });
  await S('signup-field', q('input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Signup field', desc: 'The first field on the marketing signup form; focused and typed into then cleared — the form was never submitted.', sel: 'signup input' }, { fillText: 'name@example.com' });
  await S('signup-submit', q('button[type="submit"], button, a, input[type="submit"]').filter({ hasText: /^Submit$|Get started|Try for free|Create|Continue|Sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup submit', desc: 'The marketing signup form\'s submit button (the rounded-[64px] "Submit" under the e-mail field); measured, never pressed.', sel: 'signup submit' });
  save();
}

// The signin card's component set. `p` prefixes the component keys so the
// dark pass keeps its own readings instead of overwriting the light ones.
async function signinCommon(key, g, p = 'app') {
  await sheetsFor(key);
  await chrome(key);
  const dark = p === 'appd' ? ' under [data-theme=dark]' : '';
  await S(p + '-panel', q('form, [class*="card" i], [class*="panel" i], main').filter({ hasText: /Sign in|email|Google/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth panel' + dark, desc: 'The sign-in card on app.frontapp.com' + dark + ' — the elevated panel holding the e-mail field, Continue, the SSO buttons and the legal links.', sel: 'signin card' }, { noScroll: true });
  await S(p + '-email', q('input[type="email"], input[name="email"], input[autocomplete="username"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field' + dark, desc: 'The e-mail input on the sign-in form' + dark + '; focused and typed into then cleared — Enter was never pressed and nothing was submitted.', sel: 'signin input[type=email]' }, { fillText: 'name@example.com' });
  await S(p + '-continue', q('button[type="submit"], button').filter({ hasText: /Continue|Sign in|Log in|Next/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button' + dark, desc: 'The sign-in form\'s primary button' + dark + ' (the --color-bg-fill-brand fill); measured, never pressed.', sel: 'signin Continue' }, { noScroll: true });
  await S(p + '-sso', q('button, a').filter({ hasText: /Google|SSO|Microsoft|Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button' + dark, desc: 'A single-sign-on button on the auth shell' + dark + '; measured, never pressed.', sel: 'signin SSO' }, { noScroll: true });
  await S(p + '-forgot', q('a').filter({ hasText: /Forgot|forgot/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot link' + dark, desc: 'The "Forgot password" link to /forgot-password; measured, never followed.', sel: 'signin Forgot' }, { noScroll: true });
  save();
}

async function signin() { if (await newPage('signin', { wait: 12000 })) await signinCommon('signin', G.auth, 'app'); }
async function signinDark() {
  if (!(await newPage('signin-dark', { wait: 12000, url: SIGNIN_URL, theme: 'dark' }))) return;
  // Confirm the shell actually painted the dark theme; if it did not, record
  // the miss rather than minting a "dark" reading of a light page.
  const theme = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
  log('  data-theme =', theme);
  if (theme !== 'dark') failedPages.add('signin-dark');
  else await signinCommon('signin-dark', G.auth, 'appd');
}
async function signupApp() {
  if (!(await newPage('signup-app', { wait: 12000, url: SIGNUP_URL }))) return;
  await sheetsFor('signup-app');
  const g = G.auth;
  await S('signup-panel', q('form, [class*="card" i], [class*="panel" i], main').filter({ hasText: /Sign up|email|Google|Create/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup panel', desc: 'The create-account card on app.frontapp.com/signup.', sel: 'signup card' }, { noScroll: true });
  await S('signup-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Signup email field', desc: 'The e-mail input on the product signup form; typed into then cleared — never submitted.', sel: 'signup email' }, { fillText: 'name@example.com' });
  // signup-app-submit, not signup-submit: the marketing /signup pass owns the
  // bare key, and a shared key had this pass overwrite its measurements.
  await S('signup-app-submit', q('button[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Signup submit (app)', desc: 'The submit on app.frontapp.com/signup — the route paints the same auth card as /signin (email, password, "Sign in"); measured, never pressed.', sel: 'app signup submit' }, { noScroll: true });
  save();
}
async function forgot() {
  if (!(await newPage('forgot', { wait: 12000, url: FORGOT_URL }))) return;
  await sheetsFor('forgot');
  const g = G.auth;
  await S('forgot-panel', q('form, [class*="card" i], [class*="panel" i], main').filter({ hasText: /password|email/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Reset panel', desc: 'The reset-password card on app.frontapp.com/forgot-password.', sel: 'forgot card' }, { noScroll: true });
  await S('forgot-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Reset email field', desc: 'The e-mail input on the reset form; typed into then cleared — never submitted.', sel: 'forgot email' }, { fillText: 'name@example.com' });
  await S('forgot-submit', q('button[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Reset submit', desc: 'The submit on /forgot-password — the route paints the same auth card as /signin, so no dedicated reset button exists signed out; measured, never pressed.', sel: 'forgot submit' }, { noScroll: true });
  save();
}

async function help() {
  if (!(await newPage('help', { url: HELP + '/', wait: 9000 }))) return;
  await sheetsFor('help');
  const g = G.help;
  await S('help-header', q('header, [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Help header', desc: 'The help centre\'s own header (Front\'s Knowledge Base product): the mark, the nav and the search.', sel: 'help header' }, { noScroll: true });
  await S('help-search', q('input[type="search"], input[placeholder*="Search" i], form[role="search"] input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The help centre\'s search input; focused and typed into then cleared — no search was submitted.', sel: 'help search input' }, { fillText: 'channels' });
  await S('help-card', q('a.kb-category-card, [class*="category-card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Category card', desc: 'A help-category card (kb-category-card) on the help home; measured, never followed.', sel: 'help category card' });
  await S('help-card-2', q('a.kb-category-card, [class*="category-card" i]').filter({ visible: true }).nth(1), ['default', 'hover'], { group: g, title: 'Category card (second)', desc: 'A second help-category card on the help home — the home lists categories, not article links; measured, never followed.', sel: 'help category card 2' });
  save();
}

async function helpArticle() {
  // Follow one reader's own click into the first article the centre lists.
  if (!(await newPage('help-article', { url: HELP + '/en/', wait: 9000 }))) return;
  const a = page.locator('a[href*="/articles/"], main a').filter({ hasText: /\S{6,}/ }).first();
  const href = await a.getAttribute('href').catch(() => null);
  if (href) { await page.goto(new URL(href, HELP).href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {}); await page.waitForTimeout(6000); await closePromo(page); }
  out._meta.helpArticleUrl = safeUrl(page.url());
  await sheetsFor('help-article');
  const g = G.help;
  await S('helpa-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: 'A help article headline inside Front\'s Knowledge Base product.', sel: 'help article h1' }, { noScroll: true });
  await S('helpa-body', q('article:has(p), [class*="article" i]:has(p), main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'The article body column (--article-* vars paint the prose).', sel: 'help article body' }, { crop: false });
  await S('helpa-crumb', q('nav a, [class*="breadcrumb" i] a, a').filter({ hasText: /\S{3,}/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Breadcrumb link', desc: 'A breadcrumb or section link on the article page; measured, never followed.', sel: 'help article link' }, { noScroll: true });
  save();
}

async function dev() {
  if (!(await newPage('dev', { url: DEV + '/docs/welcome', wait: 10000 }))) return;
  await sheetsFor('dev');
  const g = G.dev;
  await S('dev-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Dev header', desc: 'The developer portal\'s header — the ReadMe vendor platform skinned to Front.', sel: 'dev header' }, { noScroll: true });
  await S('dev-search', q('button, input').filter({ hasText: /Search/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger', desc: 'The portal\'s search control — a local UI toggle for the search overlay; measured at rest, never opened.', sel: 'dev search' }, { noScroll: true });
  await S('dev-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Doc headline', desc: 'A docs headline on dev.frontapp.com (ReadMe).', sel: 'dev h1' }, { noScroll: true });
  await S('dev-side-link', q('nav a, aside a, [class*="sidebar" i] a').filter({ hasText: /\S{3,}/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sidebar link', desc: 'A sidebar navigation link in the docs tree; measured, never followed.', sel: 'dev sidebar link' });
  save();
}

async function devRef() {
  if (!(await newPage('dev-ref', { url: DEV + '/reference/getting-started', wait: 10000 }))) return;
  await sheetsFor('dev-ref');
  const g = G.dev;
  await S('devref-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Reference headline', desc: 'An API-reference page headline on the ReadMe stack.', sel: 'dev ref h1' }, { noScroll: true });
  await S('devref-code', q('pre, code').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A code block on the reference page.', sel: 'dev pre/code' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the wordmark, the CTAs and the burger.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Burger button', desc: 'The mobile menu button — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile menu button' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('nav, [role="dialog"], [class*="mobile-menu" i], div[class*="fixed" i]').filter({ hasText: /Pricing/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The navigation overlay opened by the burger (the same destinations as the desktop header); its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-cta', q('a, button').filter({ hasText: /^Request demo$|^Try for free$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The hero action at 390 wide; measured never followed.', sel: 'mobile CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); front.com marketing pages paint the Tailwind-compiled layer under section themes [data-theme=theme-dark-violet]/theme-white/theme-gray (no page-level switch); app.frontapp.com\'s auth shell paints the --color-* token layer, dark via html[data-theme="dark"]; help.front.com is Front\'s Knowledge Base product; dev.frontapp.com is ReadMe';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, product, 'request-demo': requestDemo, signup, signin, 'signin-dark': signinDark, 'signup-app': signupApp, forgot, help, 'help-article': helpArticle, dev, 'dev-ref': devRef, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href*="/signup"], header a[href*="/request-demo"]');
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
