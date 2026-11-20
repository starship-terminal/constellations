// Measures fingerprint.com's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home identification pricing demo contact blog careers resources
//        case-studies about docs docs-home login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fingerprint.com is three public stacks signed out. The marketing pages are
// an Astro + Tailwind v4 app on the declared --fpds-*/--color-* token layer,
// painted light only (the dark: utilities Tailwind emits are vestigial;
// emulated dark painted the same :root). docs.fingerprint.com is a Mintlify
// docs site with its own token layer and a real light/dark preference.
// dashboard.fingerprint.com /login and /signup are the product shell's only
// signed-out surfaces. The Astro class names are scoped (_name_hash), so
// specs select by role, aria-label, semantic attribute or text. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the
// header's Product/Use Cases/Resources dropdown triggers, the pricing FAQ
// accordions, the demo section tabs, the mobile "Mobile Menu" button; the
// contact-sales, blog-newsletter and docs fields are typed into and cleared,
// never submitted; "Submit", "Get Started", "Continue with *" and every CTA
// are measured, never followed. /demo is the product's own public demo — its
// signal panel can display this machine's IP and rough location, so shots and
// crops of it are masked before quantize (tools/redact-rules/fingerprint.json).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, DOCS_BASE, LOGIN_URL, SIGNUP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', identification: '/products/identification/', 'smart-signals': '/products/smart-signals/',
  pricing: '/pricing/', demo: '/demo/', contact: '/contact-sales/', blog: '/blog/', careers: '/careers/',
  resources: '/resources/', 'case-studies': '/case-studies/', about: '/about-us/',
  'docs-home': DOCS_BASE + '/', docs: DOCS_BASE + '/docs/quick-start-guide',
  login: LOGIN_URL, signup: SIGNUP_URL, mobile: '/',
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

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null } = {}) {
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', contact: 'Contact sales form',
  auth: 'Login and signup (dashboard shell)', demo: 'Demo surface',
  products: 'Product pages', resources: 'Blog and resource indexes',
  docs: 'Docs site (Mintlify)', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's "Product" nav-dropdown: a plain header <button> whose
// aria-expanded flips and whose panel mounts beside it. A pointer click is
// the activation, keyboard Enter the fallback — a local UI toggle, never a
// link. Escape closes it afterwards.
async function openProductMenu() {
  const btn = page.locator('header button').filter({ hasText: /^Product$/ }).first();
  if (!(await btn.count())) return 'no Product trigger';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the Product dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(700);
    if (await open()) return 'clicked the "Product" trigger to open the nav dropdown';
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the "Product" trigger and pressed Enter to open the nav dropdown';
  }
  return 'activated "Product"; the dropdown did not report open';
}

// Opens the mobile nav: the "Mobile Menu" button. Pointer first, then Enter.
async function openMobileMenu() {
  const b = page.locator('button[aria-label="Mobile Menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = async () => (await b.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked "Mobile Menu" to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused "Mobile Menu" and pressed Enter to open the nav overlay';
  }
  return 'activated "Mobile Menu"; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The sticky top bar on every marketing page: the Fingerprint wordmark, Product/Use Cases/Resources dropdown triggers, AI, Docs, Demo, Pricing, Login, Contact Sales and the "Get Started" CTA.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"], header a[href="https://fingerprint.com/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Fingerprint wordmark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-dropdown-btn', q('header button').filter({ hasText: /^Product$/ }).first(), [...B4, 'opened'], { group: g, title: 'Nav dropdown trigger', desc: 'The "Product" header button — aria-expanded flips and the dropdown panel mounts beside it. The opened state was measured after its own toggle click; aria-expanded had to stay true.', sel: 'header button Product' }, { noScroll: true });
  await S('nav-panel', q('header').locator('div[class*="absolute"]').filter({ hasText: /Device Intelligence|Smart Signals/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Product dropdown panel', desc: 'The dropdown panel opened by the "Product" trigger (Device Intelligence, Smart Signals, product entries); its links were never followed.', sel: 'product dropdown panel' }, { open: openProductMenu, noScroll: true, noReset: true });
  await S('nav-menu-item', q('header').locator('a').filter({ hasText: /Identification/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Dropdown item', desc: 'The "Identification" item inside the opened product dropdown; measured, never followed.', sel: 'product dropdown item' }, { open: openProductMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', q('header a, nav a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-login', q('header a, nav a').filter({ hasText: /^Login$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The "Login" header link to dashboard.fingerprint.com/login; measured, never followed.', sel: 'header a Login' }, { noScroll: true });
  await S('nav-cta', q('header a, nav a').filter({ hasText: /^Get Started$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The orange "Get Started" header pill (the brand-primary fill); links to dashboard.fingerprint.com/signup, measured never followed.', sel: 'header a Get Started' }, { noScroll: true });
  await S('chat-btn', q('button[aria-label="Open the chat"]').filter({ visible: true }).first(), B4, { group: g, title: 'Chat launcher', desc: 'The floating "Open the chat" support-widget launcher pinned bottom-right; measured, never opened.', sel: 'button Open the chat' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"Identify Every Visitor" — the fp-hero-block masthead.', sel: 'h1' }, { noScroll: true });
  await S('hero-pill', q('a[href*="claude-duet"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'News pill', desc: 'The "New — We now detect Claude Duet" announcement pill above the headline; links to a blog post, measured never followed.', sel: 'hero news pill' }, { noScroll: true });
  await S('prompt-expander', q('button').filter({ hasText: /^Prompt$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: h, title: 'Install prompt expander', desc: 'The "Prompt" expander in the hero that reveals the get-started prompt text and the AI-tool install links; opened by its own toggle.', sel: 'hero Prompt expander' });
  await S('install-btn', q('button').filter({ hasText: /Install Fingerprint with AI/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Install button', desc: 'The "Install Fingerprint with AI" hero button — a local UI toggle that reveals install options; measured, never toggled.', sel: 'hero Install Fingerprint with AI' });
  await S('section-h2', await domFind(page, /\S{6,}/, { sel: 'h2', tag: 'h2', minW: 200, minH: 40 }), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page ("Not all bots are bad Not all humans are good") — a display-size h2, so transient microcopy such as a widget\'s error heading never counts.', sel: 'h2 (display size)' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: the newsletter subscribe field, the Product/Use Cases/Resources/Developers columns, social icons and company links.', sel: 'footer' });
  await S('newsletter-field', q('footer input[type="email"], footer input[name="email"]').filter({ visible: true }).first(), FIELD, { group: f, title: 'Newsletter field', desc: 'The "Email address*" subscribe input in the footer; focused and typed into then cleared — never subscribed.', sel: 'footer input[type=email]' }, { fillText: 'name@example.com' });
  await S('subscribe-btn', q('button[aria-label="Subscribe to newsletter"]').filter({ visible: true }).first(), B4, { group: f, title: 'Subscribe button', desc: 'The newsletter subscribe button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'footer Subscribe to newsletter' });
  await S('footer-link', q('footer a').filter({ hasText: /Smart Signals/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Smart Signals' });
  save();
}

async function identification() {
  if (!(await newPage('identification'))) return;
  await sheetsFor('identification');
  await chrome('identification');
  const g = G.products;
  await S('prod-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product headline', desc: '"Device identification_" — the /products/identification masthead.', sel: 'h1' }, { noScroll: true });
  await S('prod-select', q('select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Demo select', desc: 'The native <select> in the page\'s interactive identification demo (a region/device picker); measured at rest, never changed.', sel: 'select' });
  await S('prod-cta', q('a, button').filter({ hasText: /Get [Ss]tarted|Contact [Ss]ales|Talk to/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'A "Get started" call-to-action on the product page; measured, never followed.', sel: 'product page CTA' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Choose your plan" — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('price-slider', q('input[type="range"], input[name="billing-slider"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Identification-volume slider', desc: 'The "billing-slider" range input that re-prices the plans (20K/100K/200K/500K/1M+ identifications); measured at rest, never dragged.', sel: 'input[type=range] billing-slider' });
  await S('price-tick', q('button').filter({ hasText: /^100K$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Slider tick', desc: 'A volume tick under the slider (100K identifications); a local UI control that re-prices the grid — measured, never pressed.', sel: 'slider 100K tick' });
  await S('plan-card', q('div.rounded-2xl').filter({ has: q('h3') }).filter({ hasText: /identifications|API calls|\$|Custom/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A plan card on /pricing — one bordered column of the three-card grid (Free/Pro/Enterprise): name, price, identification allowance and its CTA.', sel: 'plan card (.rounded-2xl with h3)' });
  await S('plan-cta', q('div.rounded-2xl a, div.rounded-2xl button').filter({ hasText: /^(Get Started|Start Free|Contact Sales)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s primary action ("Start Free" on the Free/Pro cards, "Contact Sales" on Enterprise); measured, never followed.', sel: 'plan card CTA' });
  await S('compare-btn', q('button, a').filter({ hasText: /^Compare all features$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Compare features control', desc: 'The "Compare all features" control that opens the feature-comparison grid; a local UI toggle — measured at rest, never toggled.', sel: 'Compare all features' });
  await S('feature-acc', q('button, div').filter({ hasText: /^Identification Features$/ }).filter({ visible: true }).first(), ['default', 'opened', 'hover'], { group: g, title: 'Feature-group accordion', desc: 'A feature-group accordion in the comparison table ("Identification Features", "Smart Signals", "Support", ...); the opened state was measured after its own toggle click — a local UI toggle.', sel: 'feature accordion' });
  await S('faq-acc', q('[aria-expanded]').filter({ hasText: /^How does billing for Fingerprint work\?/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the pricing FAQ ("How does billing for Fingerprint work?", "Do you offer annual billing...", ...); the opened state was measured after its own toggle — a local UI toggle.', sel: 'pricing FAQ row' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 11000 }))) return;
  await sheetsFor('demo');
  await chrome('demo');
  const g = G.demo;
  await S('demo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo headline', desc: '"See Fingerprint in Action" — the /demo masthead over the live device-intelligence demo.', sel: 'h1' }, { noScroll: true });
  await S('demo-tab', q('button').filter({ hasText: /IDENTIFICATION SIGNALS/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Signal-group tab', desc: 'The "01 IDENTIFICATION SIGNALS" tab in the demo (02 BROWSER SMART SIGNALS, 03 MOBILE SMART SIGNALS are its siblings); opened by its own toggle — a local UI tab.', sel: 'demo signal tab' });
  await S('demo-signal', q('button[aria-label^="See ip address"]').filter({ visible: true }).first(), B4, { group: g, title: 'Signal reveal button', desc: 'A "See <signal> in the signals below" control that scrolls the signal panel to a row — a local UI toggle; measured, never pressed. The signal values it points at can name this machine\'s IP and rough location, so the panel\'s crops are masked before commit.', sel: 'demo signal reveal' });
  await S('demo-analyze', q('button').filter({ hasText: /^Analyze my browser again$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Re-analyze button', desc: 'The "Analyze my browser again" control — it re-runs the public demo on the visitor\'s own browser; measured, never pressed.', sel: 'Analyze my browser again' });
  await S('demo-field', q('input[placeholder="4242 4242 4242 4242"], input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Demo checkout field', desc: 'A mock card-number input inside the demo\'s fake checkout; typed into then cleared — the demo form was never placed.', sel: 'demo card input' }, { fillText: '4242 4242 4242 4242' });
  await S('demo-order', q('button').filter({ hasText: /^Place Order$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo order button', desc: 'The fake checkout\'s "Place Order" button inside the demo pane; measured, never pressed.', sel: 'demo Place Order' });
  await S('demo-login', q('button').filter({ hasText: /^Log In$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo login button', desc: 'The fake sign-in "Log In" inside the demo pane; measured, never pressed.', sel: 'demo Log In' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: '"Talk to Our Sales Team" — the /contact-sales masthead over the form.', sel: 'h1' }, { noScroll: true });
  await S('contact-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The e-mail input on the sales form; focused and typed into then cleared — never submitted.', sel: 'contact-sales input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('contact-submit', q('button[type="submit"], button').filter({ hasText: /^Submit$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The sales form\'s "Submit" button; its states were measured but the button was never clicked — the form was never sent.', sel: 'contact-sales Submit' }, { noScroll: true });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  const g = G.resources;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog headline', desc: '"Fingerprint Blog" — the /blog index masthead.', sel: 'h1' }, { noScroll: true });
  await S('blog-card', q('a').filter({ hasText: /How to|best |guide/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article card', desc: 'An article card in the blog index; measured, never followed.', sel: 'blog article card' });
  await S('blog-subscribe', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Blog subscribe field', desc: 'The newsletter e-mail input on the blog index; focused and typed into then cleared — never subscribed.', sel: 'blog input[type=email]' }, { fillText: 'name@example.com' });
  await S('blog-subscribe-btn', q('button').filter({ hasText: /^Subscribe$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Blog subscribe button', desc: 'The blog subscribe button; measured, never pressed.', sel: 'blog Subscribe' });
  save();
}

async function careers() {
  if (!(await newPage('careers'))) return;
  await sheetsFor('careers');
  const g = G.resources;
  await S('careers-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Careers headline', desc: 'The /careers masthead.', sel: 'h1' }, { noScroll: true });
  await S('careers-cta', q('a, button').filter({ hasText: /^Explore Our Jobs$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Careers CTA', desc: 'The "Explore Our Jobs" button on /careers — a local anchor to the jobs list; measured, never followed.', sel: 'careers Explore Our Jobs' });
  save();
}

async function resources() {
  if (!(await newPage('resources'))) return;
  await sheetsFor('resources');
  const g = G.resources;
  await S('res-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Resources headline', desc: 'The /resources resource-center masthead.', sel: 'h1' }, { noScroll: true });
  await S('res-card', q('main a, section a, a').filter({ has: q('img') }).filter({ hasText: /article|tutorial|webinar|guide|case study|ebook/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A resource card on the /resources index — an anchor holding a thumbnail and a kicker label (ARTICLE/TUTORIAL/..., painted by text-transform); measured, never followed.', sel: 'resources card link' });
  save();
}

async function casestudies() {
  if (!(await newPage('case-studies'))) return;
  await sheetsFor('case-studies');
  const g = G.resources;
  await S('cs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Case-studies headline', desc: 'The /case-studies index masthead.', sel: 'h1' }, { noScroll: true });
  await S('cs-card', q('main a, section a').filter({ hasText: /\S{4,}/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Case-study card', desc: 'A case-study card on the index; measured, never followed.', sel: 'case-studies card' });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  const g = G.resources;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: '"About us" — the /about-us masthead.', sel: 'h1' }, { noScroll: true });
  await S('about-value', q('h2, h3').filter({ hasText: /No Nonsense|Fail\. Learn|helpful/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Value card heading', desc: 'A "Our Values" card heading (No Nonsense., Fail. Learn. Grow., Be level 5 helpful.).', sel: 'values card heading' });
  save();
}

async function docsHome() {
  if (!(await newPage('docs-home', { url: DOCS_BASE + '/' }))) return;
  await sheetsFor('docs-home');
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline', desc: '"Welcome to Fingerprint Docs" — the docs landing masthead on the Mintlify stack.', sel: 'docs h1' }, { noScroll: true });
  await S('docs-nav-tab', q('a').filter({ hasText: /^Start$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Docs nav tab', desc: 'A docs top-nav tab (Home/Start/AI/Guides/API Reference/Changelogs); measured, never followed.', sel: 'docs nav tab' }, { noScroll: true });
  save();
}

async function docs() {
  if (!(await newPage('docs', { url: DOCS_BASE + '/docs/quick-start-guide' }))) return;
  await sheetsFor('docs');
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Doc page headline', desc: '"Quick Start Guide" — a docs article headline on the Mintlify stack.', sel: 'docs article h1' }, { noScroll: true });
  await S('docs-search', q('button[aria-label*="Open search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger', desc: 'The docs\' "Open search" button — a local UI toggle for the search overlay; measured, never opened.', sel: 'docs Open search' }, { noScroll: true });
  await S('docs-theme-btn', q('button[aria-label*="theme preference"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme toggle', desc: 'The docs\' "Change theme preference" button — a local UI toggle that flips data-theme-preference between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass).', sel: 'docs Change theme preference' }, { noScroll: true });
  await S('docs-side-link', q('nav a').filter({ hasText: /^Quick Start Guide$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sidebar link', desc: 'A sidebar navigation link in the docs tree; measured, never followed.', sel: 'docs sidebar link' });
  await S('docs-code', q('pre, code').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A code block on the docs article; the site\'s .dark syntax-highlight scope paints these.', sel: 'docs pre/code' });
  save();
}

async function login() {
  if (!(await newPage('login', { url: LOGIN_URL, wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('login-panel', q('div[class*="MuiPaper"]').filter({ hasText: /Log In|Continue with/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The dashboard-shell sign-in card on dashboard.fingerprint.com/login — the elevated MuiPaper card holding "Log In", the Google/GitHub/Microsoft SSO buttons and "Continue with email" — not the full-page main behind it.', sel: 'login .MuiPaper-root card' }, { noScroll: true });
  await S('login-google', q('button, a').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The "Continue with Google" button; measured, never pressed.', sel: 'login Continue with Google' }, { noScroll: true });
  await S('login-github', q('button, a').filter({ hasText: /Continue with GitHub/i }).filter({ visible: true }).first(), B4, { group: g, title: 'GitHub SSO button', desc: 'The "Continue with GitHub" button; measured, never pressed.', sel: 'login Continue with GitHub' }, { noScroll: true });
  await S('login-email-btn', q('button, a').filter({ hasText: /Continue with email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with email', desc: 'The "Continue with email" control that reveals the e-mail form; measured, never pressed — the form was never opened or submitted.', sel: 'login Continue with email' }, { noScroll: true });
  await S('login-signup-link', q('a').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Sign up" link beside "New to Fingerprint?"; measured, never followed.', sel: 'login Sign up' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { url: SIGNUP_URL, wait: 10000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.auth;
  await S('signup-panel', q('div[class*="MuiPaper"]').filter({ hasText: /Sign up|Continue with/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup panel', desc: 'The dashboard-shell sign-up card on dashboard.fingerprint.com/signup — the elevated MuiPaper card holding "Sign up" and the SSO/email controls, not the full-page main behind it.', sel: 'signup .MuiPaper-root card' }, { noScroll: true });
  await S('signup-google', q('button, a').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button (signup)', desc: 'The "Continue with Google" button on /signup; measured, never pressed.', sel: 'signup Continue with Google' }, { noScroll: true });
  await S('signup-email-btn', q('button, a').filter({ hasText: /Continue with email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with email (signup)', desc: 'The "Continue with email" control on /signup; measured, never pressed.', sel: 'signup Continue with email' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the wordmark, the CTA and the "Mobile Menu" button.', sel: 'mobile header' }, { noScroll: true });
  await S('m-cta', page.getByRole('link', { name: 'Get Started' }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'A "Get Started" action at 390 wide (the header pill is hidden on phones); measured never followed.', sel: 'mobile Get Started' });
  const ham = q('button[aria-label="Mobile Menu"]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The "Mobile Menu" button — a local UI toggle; the opened state was measured after activating it.', sel: 'Mobile Menu button' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('nav, [role="dialog"], div[class*="fixed"]').filter({ hasText: /Pricing/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The navigation overlay opened by the menu button (the same destinations as the desktop header); its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every marketing page on fingerprint.com paints the light FPDS/Tailwind token layer (the dark: utilities are vestigial — an emulated dark pass resolved the same :root); docs.fingerprint.com is a Mintlify site with its own layer and a real light/dark preference; dashboard.fingerprint.com /login /signup are the product shell, painted light';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, identification, pricing, demo, contact, blog, careers, resources, 'case-studies': casestudies, about, 'docs-home': docsHome, docs, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href*="dashboard.fingerprint.com/signup"]');
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
