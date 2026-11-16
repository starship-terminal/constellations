// Measures gladia.io's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home product pricing demo library blog docs-home docs login
//        signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// gladia.io is four public stacks signed out. The marketing pages are a
// static server-rendered site on the declared :root token layer, painted
// dark by default; /library carries body.light-mode and paints the light
// scope, and /blog is a legacy Webflow stack on its own stylesheets, also
// light. docs.gladia.io is a Mintlify site with its own token layer and a
// real light/dark preference. app.gladia.io / and /signup are the product
// shell's only signed-out surfaces, painted dark. The class names are
// semantic (.site-nav, .mega-menu, button[data-menu]), so specs select by
// class, data attribute, aria-label or text. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the header's
// mega-menu triggers (hover intent, the site's own activation), the
// pricing-mode Async/Real-time toggle, the pricing FAQ accordions and the
// mobile "Open menu" button; the demo-request, calculator and auth fields
// are typed into and cleared, never submitted; every CTA, submit, SSO and
// sign-in control is measured, never followed.
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
  home: '/', product: '/product/speech-to-text-api', pricing: '/pricing',
  demo: '/demo-request', library: '/library', blog: '/blog',
  'docs-home': DOCS_BASE + '/chapters/introduction',
  docs: DOCS_BASE + '/chapters/pre-recorded-stt/quickstart',
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
  await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  // A fresh successful pass clears the stale miss flag — it is re-stamped
  // below only if this run actually misses or fails a listed state.
  delete out.components[key].recaptureMissed;
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
        // A click is how a user lands in a text field, but on a toggle control
        // (checkbox, radio, range, select, button or its ARIA form) a click
        // flips the value instead of only focusing it — the pricing
        // calculator's checkbox and range live in this branch. Those get a
        // real keyboard focus so the at-rest reading still stands.
        const toggleCtl = await fld.evaluate((el) => el.matches('input[type="checkbox"], input[type="radio"], input[type="range"], input[type="file"], select, button, [role="checkbox"], [role="radio"], [role="switch"], [role="slider"], [role="combobox"]')).catch(() => false);
        if (toggleCtl) {
          const how = await kbFocus(fld);
          via = how === 'focus failed' ? 'focus failed' : `keyboard focus (${how}), never clicked`;
        } else {
          await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
          await page.waitForTimeout(400);
          via = 'clicked into the field';
        }
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
// First candidate that paints a real box. Playwright's { visible: true }
// lets through nodes inside zero-height wrappers and clipped overlays
// (header.site-nav wraps the fixed nav.navbar, a hidden checkbox input sits
// behind its styled label, a closed mega-menu keeps zero-sized links), so
// "visible" alone is not an honest measurement target — the box is.
async function sized(loc, { minW = 1, minH = 1 } = {}) {
  const n = await loc.count().catch(() => 0);
  for (let i = 0; i < n; i++) {
    const el = loc.nth(i);
    const box = await el.boundingBox().catch(() => null);
    if (box && box.width >= minW && box.height >= minH) return el;
  }
  return loc.filter({ visible: true }).first();
}
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', demo: 'Demo request form',
  auth: 'Login and signup (app shell)', products: 'Product pages',
  resources: 'Blog, library and marketing indexes',
  docs: 'Docs site (Mintlify)', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens one of the header's mega-menu panels: the nav carries
// button[data-menu="product|solutions|developers|resources|company"] whose
// aria-expanded flips while .mega-menu and the matching .mega-menu-panel take
// .is-visible. The site's own activation is hover intent (mouseover) with
// keyboard focus + Enter the fallback — a local UI toggle, never a link.
// Escape closes it afterwards.
async function openMegaMenu(name = 'product') {
  const btn = q(`button[data-menu="${name}"]`).filter({ visible: true }).first();
  if (!(await btn.count())) return `no data-menu="${name}" trigger`;
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true'
    || (await q('.mega-menu.is-visible').count()) > 0;
  if (await open()) return 'the mega-menu was already open';
  for (let i = 0; i < 4; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(900);
    if (await open()) return `hovered the "${name}" trigger to open the mega-menu`;
    await btn.focus().catch(() => {});
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return `focused the "${name}" trigger and pressed Enter to open the mega-menu`;
    await page.keyboard.press('Escape').catch(() => {});
  }
  return `activated "${name}"; the mega-menu did not report open`;
}

// Opens the mobile nav: the "Open menu" navbar-menu-toggle button whose
// aria-expanded flips while .mobile-nav takes .is-visible. Pointer first,
// then Enter.
async function openMobileMenu() {
  const b = q('button.navbar-menu-toggle, button[aria-label="Open menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = async () => (await b.getAttribute('aria-expanded').catch(() => null)) === 'true'
    || (await q('.mobile-nav.is-open, .mobile-nav.is-visible, .mobile-nav[aria-hidden="false"], #mobileNav[aria-hidden="false"]').count()) > 0;
  if (await open()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked "Open menu" to open the nav overlay';
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(900);
    if (await open()) return 'focused "Open menu" and pressed Enter to open the nav overlay';
  }
  return 'activated "Open menu"; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // header.site-nav is a zero-height wrapper — the painted bar is the fixed
  // nav.navbar inside it; measuring the wrapper reported 0px tall.
  await S('mkt-header', await sized(q('header.site-nav nav.navbar, nav.navbar'), { minW: 100, minH: 20 }), ['default'], { group: g, title: 'Site header', desc: 'The floating rounded glass navbar at the top of every marketing page: the Gladia wordmark, the Product/Solutions/Developers/Resources/Company mega-menu triggers, Pricing, "Request a demo" and the signup CTA.', sel: 'header.site-nav nav.navbar' }, { noScroll: true });
  await S('mkt-logo', q('header a.navbar-logo, header a[aria-label="Gladia"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The inline-SVG Gladia symbol + wordmark in the header, linking home.', sel: 'header a.navbar-logo' }, { noScroll: true });
  await S('nav-menu-btn', q('button[data-menu="product"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mega-menu trigger', desc: 'The "Product" header button — a hover-intent trigger whose aria-expanded flips while the mega-menu mounts (the opened panel is the mega-panel component below). Hover is the site\'s own activation, focus+Enter the fallback.', sel: 'button[data-menu=product]' }, { noScroll: true });
  await S('mega-panel', q('.mega-menu .mega-menu-panel, #mega-panel-product').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The product mega-menu panel opened by the "Product" trigger — glass card with product and feature links; its links were never followed.', sel: '.mega-menu-panel' }, { open: () => openMegaMenu('product'), noScroll: true, noReset: true });
  await S('mega-item', q('.mega-menu a').filter({ hasText: /Speech|Real-time|Audio/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega-menu item', desc: 'A product link inside the opened mega-menu; measured, never followed.', sel: '.mega-menu a' }, { open: () => openMegaMenu('product'), noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', q('header a, nav a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-demo', q('header a, nav a').filter({ hasText: /Request a demo|Book a demo/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo link', desc: 'The "Request a demo" header link to /demo-request; measured, never followed.', sel: 'header a Request a demo' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /Start.*free|Get started|Sign up/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header CTA', desc: 'The header signup CTA (the brand-purple fill) linking to app.gladia.io/signup; measured, never followed.', sel: 'header signup CTA' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: 'The home masthead display heading on the dark :root surface.', sel: 'h1' }, { noScroll: true });
  // A page-wide /new/i text match catches hidden links first (the closed
  // mega-menu's "New ..." callout measures 0x0) — take the first that paints;
  // the current pill is .announce-pill reading "Live".
  await S('hero-badge', await sized(q('[class*="badge"], [class*="pill"], [class*="announc"], a').filter({ hasText: /Solaria|\bnew\b|announc|\bLive\b/i }), { minW: 30, minH: 12 }), ['default'], { group: h, title: 'Hero badge', desc: 'The announcement badge/pill above the hero headline; measured, never followed.', sel: 'hero badge' }, { noScroll: true });
  await S('section-h2', await domFind(page, /\S{6,}/, { sel: 'h2', tag: 'h2', minW: 200, minH: 40 }), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page — a display-size h2, so transient microcopy never counts.', sel: 'h2 (display size)' });
  await S('glass-card', q('.glass-card, [class*="b__card"], [class*="glass"]').filter({ hasText: /\S{4,}/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Glass card', desc: 'A frosted-glass marketing card (the site\'s --bg-glass + blur + hairline border treatment); measured, never followed.', sel: '.glass-card' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: sitemap columns, social icons, legal links and the Gladia mark.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /Docs|API|Pricing/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a' });
  save();
}

async function product() {
  if (!(await newPage('product'))) return;
  await sheetsFor('product');
  await chrome('product');
  const g = G.products;
  await S('prod-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product headline', desc: 'The /product/speech-to-text-api masthead on the dark surface.', sel: 'h1' }, { noScroll: true });
  await S('prod-cta', q('a, button').filter({ hasText: /Start.*free|Get started|Try|Request a demo/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'A call-to-action on the product page; measured, never followed.', sel: 'product page CTA' });
  // The sample container is pre.stt-dev-code__body; a bare [class*="code"]
  // matches the stt-lang__code language label ("EN") first, and inline <code>
  // is a different component — only a real block counts here.
  const prodCode = (await q('pre.stt-dev-code__body').count()) ? q('pre.stt-dev-code__body') : q('pre').filter({ hasText: /\S{8,}/ });
  await S('prod-code', prodCode.filter({ visible: true }).first(), ['default'], { group: g, title: 'Code sample', desc: 'A code sample block on the product page — mono face on an elevated surface.', sel: 'pre.stt-dev-code__body' });
  await S('prod-feature', q('h2, h3').filter({ hasText: /\S{4,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature heading', desc: 'A feature section heading on the product page.', sel: 'product h2/h3' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('price-mode-async', q('button[data-pricing-mode="async"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Pricing mode: Async', desc: 'The "Async" half of the pricing-mode segmented toggle (data-pricing-mode, aria-pressed); a local UI toggle that re-prices the grid — the opened state was measured after its own toggle.', sel: 'button[data-pricing-mode=async]' }, { noScroll: true });
  await S('price-mode-rt', q('button[data-pricing-mode="realtime"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Pricing mode: Real-time', desc: 'The "Real-time" half of the pricing-mode segmented toggle; a local UI toggle — the opened state was measured after its own toggle, then the async side was restored.', sel: 'button[data-pricing-mode=realtime]' }, { noScroll: true });
  await S('plan-card', q('.pricing-card').filter({ hasText: /€|hour|credit|month|Custom/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A plan card on /pricing — one column of the pricing grid (.pricing-grid--plans > .pricing-card): name, per-hour price, feature list and its CTA.', sel: '.pricing-card' });
  // Scoped inside the pricing card: a page-wide CTA text filter matches
  // unrelated marketing links (a hidden "Startup Studio ... credits" link in
  // the closed mega-menu won the race once).
  await S('plan-cta', await sized(q('.pricing-card a, .pricing-card button').filter({ hasText: /Start|credit|Contact|Talk to|Get started|free/ }), { minW: 40, minH: 20 }), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s primary action ("Start with 50€ free credits" or the enterprise contact link); measured, never followed.', sel: '.pricing-card CTA' });
  await S('calc-hours', q('#calc-hours, input[name="calc-hours"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Calculator hours field', desc: 'The pricing calculator\'s hours-per-month number input (default 500); typed into then cleared — a local UI control, nothing submitted.', sel: '#calc-hours' }, { fillText: '500' });
  await S('calc-range', q('input.pricing-calc__range, input[type="range"][aria-label*="Hours"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Calculator range', desc: 'The "Hours of audio per month" range slider in the calculator; measured at rest, never dragged.', sel: 'pricing-calc range input' });
  await S('calc-feature', q('input[type="checkbox"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Calculator feature checkbox', desc: 'A feature add-on checkbox in the pricing calculator (summarization, sentiment, translation, NER, PII); a local UI control — measured, never toggled.', sel: 'calculator checkbox' });
  await S('faq-acc', q('[aria-expanded], details, summary, button').filter({ hasText: /\?/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the pricing FAQ; the opened state was measured after its own toggle — a local UI toggle.', sel: 'pricing FAQ row' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 11000 }))) return;
  await sheetsFor('demo');
  await chrome('demo');
  const g = G.demo;
  await S('demo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo headline', desc: 'The /demo-request masthead over the sales form.', sel: 'h1' }, { noScroll: true });
  await S('demo-email', q('#demo-email, input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The work-e-mail input on the demo-request form; focused and typed into then cleared — never submitted.', sel: '#demo-email' }, { noScroll: true, fillText: 'name@example.com' });
  await S('demo-name', q('#demo-first-name, input[name="first"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'First-name field', desc: 'The first-name input on the demo-request form; focused and typed into then cleared — never submitted.', sel: '#demo-first-name' }, { fillText: 'Alex' });
  await S('demo-company-size', q('#demo-company-size, select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Company-size select', desc: 'The company-size select on the demo-request form; measured at rest, never changed.', sel: '#demo-company-size' });
  // The checkbox input itself is visually hidden behind its styled label;
  // measure the label (the visible control) but focus the real input inside
  // it — the label is not focusable, the input is.
  await S('demo-terms', await sized(q('label:has(input[type="checkbox"]), .contact-form__checkbox, [class*="checkbox"]'), { minW: 10, minH: 10 }), ['default', 'focused'], { group: g, title: 'Terms checkbox', desc: 'The required terms-acceptance checkbox on the demo-request form (the input is visually hidden behind its styled label); measured at rest, never toggled.', sel: 'demo terms checkbox label' }, { fieldLoc: q('label.form-checkbox input[type="checkbox"], form input[type="checkbox"], input[type="checkbox"]') });
  await S('demo-submit', q('#demo-form-btn, button[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The demo-request form\'s submit button; its states were measured but the button was never clicked — the form was never sent.', sel: '#demo-form-btn' }, { noScroll: true });
  save();
}

async function library() {
  if (!(await newPage('library'))) return;
  await sheetsFor('library');
  const g = G.resources;
  await S('lib-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library headline', desc: 'The /library masthead — the one marketing page that carries body.light-mode and paints the light token scope.', sel: 'h1' }, { noScroll: true });
  await S('lib-card', q('a').filter({ has: q('img') }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A content card on the library index; measured, never followed.', sel: 'library card link' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  const g = G.resources;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog headline', desc: 'The /blog index masthead on the legacy Webflow stack — its own stylesheets, painted light.', sel: 'h1' }, { noScroll: true });
  await S('blog-card', q('a').filter({ has: q('img') }).filter({ hasText: /\S{6,}/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Article card', desc: 'An article card in the blog index; measured, never followed.', sel: 'blog article card' });
  save();
}

async function docsHome() {
  if (!(await newPage('docs-home', { url: DOCS_BASE + '/chapters/introduction' }))) return;
  await sheetsFor('docs-home');
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline', desc: 'The docs introduction masthead on the Mintlify stack.', sel: 'docs h1' }, { noScroll: true });
  await S('docs-nav-link', q('nav a, aside a').filter({ hasText: /Introduction|Quickstart|Models/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sidebar link', desc: 'A sidebar navigation link in the docs tree; measured, never followed.', sel: 'docs sidebar link' }, { noScroll: true });
  save();
}

async function docs() {
  if (!(await newPage('docs', { url: DOCS_BASE + '/chapters/pre-recorded-stt/quickstart' }))) return;
  await sheetsFor('docs');
  const g = G.docs;
  await S('docs-h1b', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Doc page headline', desc: '"Quickstart" — a docs article headline on the Mintlify stack.', sel: 'docs article h1' }, { noScroll: true });
  // Mintlify mounts more than one search control; the first match can be the
  // hidden mobile one (0x0), so take the first candidate with a real box.
  await S('docs-search', await sized(q('button[aria-label*="search" i], button[id*="search" i], button:has-text("Search"), [class*="search" i] button'), { minW: 20, minH: 20 }), B4, { group: g, title: 'Search trigger', desc: 'The docs\' search button — a local UI toggle for the search overlay; measured, never opened.', sel: 'docs search button' }, { noScroll: true });
  await S('docs-theme-btn', q('button[id*="theme" i], button[aria-label*="theme" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme toggle', desc: 'The docs\' theme-preference control — a local UI toggle that flips the Mintlify page between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass).', sel: 'docs theme button' }, { noScroll: true });
  await S('docs-code', q('pre').filter({ hasText: /\S{4,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A code block on the docs article; Mintlify\'s own syntax-highlight layer paints these. Inline code (`transcribe()` and friends) is a different element and never counts.', sel: 'docs pre' });
  await S('docs-tab', q('[role="tab"], button').filter({ hasText: /Python|JavaScript|cURL|TypeScript/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Code-language tab', desc: 'A language tab on a docs code sample; a local UI toggle — measured, never switched.', sel: 'docs code tab' });
  save();
}

async function login() {
  if (!(await newPage('login', { url: LOGIN_URL, wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('login-panel', q('main, [class*="card"], [class*="panel"], [class*="auth"]').filter({ hasText: /Sign in|Log in|Continue with|Email/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The sign-in card on app.gladia.io/ — the shell\'s only signed-out landing: fields, SSO and the sign-in action. Measured, never submitted.', sel: 'app.gladia.io login card' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The e-mail input on the sign-in shell; focused and typed into then cleared — never submitted.', sel: 'login email input' }, { fillText: 'name@example.com' });
  await S('login-password', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The password input on the sign-in shell; focused and typed into then cleared — never submitted.', sel: 'login password input' }, { fillText: 'password' });
  await S('login-sso', q('button, a').filter({ hasText: /Continue with|Google|GitHub|SSO|Microsoft/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: 'A "Continue with" SSO button on the sign-in shell; measured, never pressed.', sel: 'login SSO button' }, { noScroll: true });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /Sign in|Log in|Continue/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The sign-in action; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login submit' }, { noScroll: true });
  await S('login-signup-link', q('a').filter({ hasText: /Sign up|Create|Register/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The sign-up link on the login shell; measured, never followed.', sel: 'login sign-up link' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { url: SIGNUP_URL, wait: 10000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.auth;
  await S('signup-panel', q('main, [class*="card"], [class*="panel"], [class*="auth"]').filter({ hasText: /Sign up|Create|Continue with|Email/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup panel', desc: 'The sign-up card on app.gladia.io/signup; measured, never submitted.', sel: 'app.gladia.io/signup card' }, { noScroll: true });
  await S('signup-email', q('input[type="email"], input[name*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (signup)', desc: 'The e-mail input on the sign-up shell; focused and typed into then cleared — never submitted.', sel: 'signup email input' }, { fillText: 'name@example.com' });
  await S('signup-sso', q('button, a').filter({ hasText: /Continue with|Google|GitHub|SSO|Microsoft/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button (signup)', desc: 'A "Continue with" SSO button on /signup; measured, never pressed.', sel: 'signup SSO button' }, { noScroll: true });
  await S('signup-submit', q('button[type="submit"], button').filter({ hasText: /Sign up|Create|Continue|Get started/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up button', desc: 'The sign-up action; measured, never clicked — nothing was submitted.', sel: 'signup submit' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  // header.site-nav is a zero-height wrapper — the painted bar is nav.navbar.
  await S('m-topbar', await sized(q('header.site-nav nav.navbar, nav.navbar'), { minW: 100, minH: 20 }), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the wordmark and the "Open menu" button.', sel: 'mobile nav.navbar' }, { noScroll: true });
  const ham = q('button.navbar-menu-toggle, button[aria-label="Open menu"]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The "Open menu" button — a local UI toggle; the opened state was measured after activating it.', sel: 'navbar-menu-toggle' }, { noScroll: true, allowLink: true });
  // The drawer is div#mobileNav.mobile-nav, which takes .is-open while its
  // aria-hidden flips to false. It must be selected by name — a bare
  // [role="dialog"] fallback matches the Axeptio consent widget first.
  await S('m-drawer', q('#mobileNav, .mobile-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The navigation sheet opened by the menu button (div#mobileNav.mobile-nav, .is-open while aria-hidden flips to false); its links were never followed.', sel: '#mobileNav.mobile-nav' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every www.gladia.io marketing page paints the dark :root token layer except /library (body.light-mode, light) and /blog (legacy Webflow stack, light); docs.gladia.io is a Mintlify site with its own layer and a real light/dark preference; app.gladia.io / and /signup are the product shell, painted dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, product, pricing, demo, library, blog, 'docs-home': docsHome, docs, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header.site-nav a, header a');
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
