// Measures dub.co's public components in every state reachable without
// signing in, submitting a form or creating anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home links pricing compare customers sales login register docs docs-dark footer mobile
// (kebab-case page arguments are accepted; an argument naming no page is an
// error, never a silent skip).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dub.co is three signed-out surfaces: the Next.js marketing site (Tailwind
// over the --bg-*/--content-*/--border-* + shadcn token layer, Satoshi/Inter/
// Geist Mono), the auth cards on /login and /register (the app.dub.co shell —
// measured, never filled past a typed sample deleted again, never submitted),
// and the Mintlify docs/help surface (the only place a real theme toggle
// exists: html.dark via localStorage isDarkMode). Nothing is sent, submitted
// or signed into: the only presses are local UI toggles — the header Product
// mega-menu (hover), the Monthly/Yearly pricing toggle, the FAQ accordion,
// the docs theme dropdown and the mobile menu. The Mintlify AI assistant and
// any promo/cookie overlay are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', links: '/links', partners: '/partners', pricing: '/pricing', customers: '/customers', enterprise: '/enterprise', compare: '/compare/bitly', sales: '/contact/sales', login: '/login', register: '/register', docs: '/docs', 'docs-dark': '/docs', help: '/help', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
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
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
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
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, radio, accordion). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|log in with email|create|create account|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|start for free|start \d+-day trial|claim|share|export|continue|continue with|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image, or falls back to marking a painted descendant.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

// markPainted returns a never-matching locator on a miss, never null, so a
// `marked || fallback` never falls back: choose by count() instead.
const orElse = async (loc, fallback) => ((loc && (await loc.count())) ? loc : fallback);

// Sets the docs surface's theme through its own "Change theme preference"
// dropdown (a local UI toggle; the preference lives in localStorage). Returns
// true only once <html> carries the class the chosen option paints — a false
// means the run must not write dark-named evidence over a light page.
async function docsTheme(theme) {
  const t = q('button[aria-label="Change theme preference"]').filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  const opt = q('[role="menu"] *, [role="menuitem"], [role="option"], [class*="popover" i] *').filter({ hasText: new RegExp(`^\\s*${theme}\\s*$`) }).first();
  if (!(await opt.count())) return false;
  await opt.click({ timeout: 5000 }).catch(() => opt.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return page.evaluate((wantDark) => document.documentElement.classList.contains('dark') === wantDark, theme === 'Dark')
    .catch(() => false);
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', pricing: 'Pricing',
  compare: 'Compare (vs Bitly)', customers: 'Customers', sales: 'Contact sales form',
  auth: 'Log in and sign up', docs: 'Docs and help (Mintlify)', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The top nav: wordmark, Product/Solutions/Resources dropdowns, Customers and Pricing links, Log in and the black Sign-up pill.', sel: 'nav' }, { noScroll: true });
  await S('logo', q('nav a[href="/"], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Dub wordmark anchor.', sel: 'first header link' }, { noScroll: true });
  await S('nav-trigger', q('button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Product button that opens the mega-menu on hover; toggled, never followed.', sel: 'nav button "Product"' }, { noScroll: true });
  await S('nav-link', q('nav a').filter({ hasText: /^\s*(Customers|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain nav link (Customers/Pricing).', sel: 'nav a "Customers"' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in button', desc: 'The bordered Log-in button; measured never followed.', sel: 'a "Log in"' }, { noScroll: true });
  await S('nav-cta', q('a').filter({ hasText: /^\s*Sign [Uu]p\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up CTA', desc: 'The black Sign-up pill; measured never followed.', sel: 'a "Sign up"' }, { noScroll: true });
  // The Product trigger opens the mega-menu on hover; keep the pointer put
  // while the panel and one of its links are read (noReset), then move away.
  try {
    const t = q('button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1400); }
  } catch (e) { log('  ! dropdown hover failed', String(e.message).split('\n')[0]); }
  const panel = await markPainted('a[href*="partners"], a[href*="links"], a[href*="analytics"], a[href*="api"]', 'm-panel', { minW: 300, minH: 150 }).catch(() => null);
  await S('nav-dropdown', await orElse(panel, q('[data-radix-popper-content-wrapper], [class*="popover" i]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The Product mega-menu panel, opened by its own trigger on hover.', sel: 'product mega-menu panel' }, { noScroll: true, noReset: true });
  // The menu closes as soon as the pointer leaves the trigger, so a reset()
  // between states used to let the global text locator slip to a same-named
  // link further down the page — every state must read one element inside the
  // open panel: scope to the marked panel (the popover wrappers as fallback)
  // and re-hover the trigger before each state instead of resetting.
  const openMenu = async () => { const t = q('button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(); if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1200); } };
  await S('menu-link', q('[data-m-mark="m-panel"] a, [data-radix-popper-content-wrapper] a, [class*="popover" i] a').filter({ hasText: /Dub Partners|Dub Links|Dub Analytics|Dub API/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu item', desc: 'A product link inside the opened mega-menu; the menu is held open while its states are read.', sel: 'mega-menu link inside the open panel' }, { noScroll: true, noReset: true,
    open: openMenu,
    before: { default: openMenu, hover: openMenu, 'focus-visible': openMenu, pressed: openMenu } });
  await page.keyboard.press('Escape'); await page.mouse.move(700, 300); await page.waitForTimeout(500);
  const h = G.hero;
  await S('hero-badge', q('a, div, span').filter({ hasText: /Introducing our Startup Program/i }).filter({ visible: true }).last(), B4, { group: h, title: 'Announcement pill', desc: 'The "Introducing our Startup Program / Learn more" pill above the headline; measured never followed.', sel: 'announcement pill' });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The display headline ("Turn clicks into revenue"), Satoshi.', sel: 'h1' });
  await S('hero-lede', q('p').filter({ hasText: /link attribution|modern link/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The paragraph under the headline.', sel: 'hero lede' });
  await S('hero-cta', q('a, button').filter({ hasText: /^\s*Start for free\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Primary CTA', desc: 'The black "Start for free" button; measured never followed.', sel: '"Start for free"' });
  await S('hero-demo', q('a, button').filter({ hasText: /^\s*Get a demo\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Demo button', desc: 'The bordered "Get a demo" button; measured never followed.', sel: '"Get a demo"' });
  await S('hero-tab', q('button, a, [role="tab"]').filter({ hasText: /^\s*(Affiliate Programs|Conversion Analytics|Short Links)\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Feature tab', desc: 'An icon tab over the product demo (Affiliate Programs / Conversion Analytics / Short Links).', sel: 'feature tab' });
  // The hero's rendered app mock is a stack of div.rounded-t-lg panels (one
  // per feature tab); mark the first large enough to be the browser-frame
  // panel rather than relying on text that changes with the active tab.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-demo"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll('div[class*="rounded-t-lg"]')].find((n) => { const r = n.getBoundingClientRect(); return r.width >= 500 && r.height >= 300; });
    if (el) el.setAttribute('data-m-mark', 'm-demo');
  }).catch(() => {});
  await S('demo-panel', q('[data-m-mark="m-demo"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Product demo panel', desc: 'The rendered dashboard mock under the hero — a published demo illustration, not the real app.', sel: 'dashboard demo panel' });
  save();
}

async function links() {
  if (!(await newPage('links'))) return;
  const g = G.hero;
  await S('links-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product page headline', desc: 'The /links product-page h1 ("Short links with superpowers").', sel: 'h1 on /links' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('billing-toggle', q('button').filter({ hasText: /^\s*Yearly/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'The Monthly/Yearly period toggle ("10% discount + 12x usage upfront"), read on its Yearly option at rest, on hover, on keyboard focus and forced pressed; never clicked or checked out.', sel: 'button "Yearly"' }, { noScroll: true });
  await S('plan-name', q('h2, h3').filter({ hasText: /^\s*(Business|Advanced|Enterprise)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name.', sel: 'plan name' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^\s*\$\d+\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure.', sel: 'plan price' });
  await S('plan-cta', q('a, button').filter({ hasText: /^\s*Start 14-day trial\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Start 14-day trial" action; measured never followed.', sel: '"Start 14-day trial"' });
  const planCard = await markPainted('h2, h3', 'm-plan', { minW: 220, minH: 300 }).catch(() => null);
  await S('plan-card', await orElse(planCard, q('[class*="card" i]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Plan card', desc: 'The shared pricing panel holding all three plan columns (Business / Advanced / Enterprise).', sel: 'plan card' });
  await S('faq-trigger', q('button').filter({ hasText: /free trial|refund|cancel/i }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ accordion', desc: 'A billing-FAQ accordion trigger, read closed: at rest, on hover, on keyboard focus and forced pressed.', sel: 'faq accordion button' });
  save();
}

async function compare() {
  if (!(await newPage('compare'))) return;
  const g = G.compare;
  await S('cmp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Compare headline', desc: 'The "Dub vs Bitly" page heading.', sel: 'h1 on /compare/bitly' }, { noScroll: true });
  const tbl = q('table').filter({ visible: true }).first();
  if (await tbl.count()) {
    await S('cmp-table', tbl, ['default'], { group: g, title: 'Comparison table', desc: 'The feature comparison table (Dub vs Bitly).', sel: 'table' });
    await S('cmp-check', q('td svg, td [class*="check" i], td').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison cell', desc: 'A cell in the comparison table.', sel: 'comparison td' });
  } else {
    await S('cmp-row', q('[class*="grid" i], li, tr').filter({ hasText: /custom domain|analytics|link/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison row', desc: 'A feature comparison row.', sel: 'comparison row' });
  }
  save();
}

async function customers() {
  if (!(await newPage('customers'))) return;
  const g = G.customers;
  await S('cust-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Customers headline', desc: 'The "Meet our customers" heading.', sel: 'h1 on /customers' }, { noScroll: true });
  // The story tile is the painted anchor itself (a.group …, ~144x480 dark);
  // a larger painted ancestor would be the whole logos section.
  const card = await markPainted('a[href*="/customers/"]', 'm-cust', { minW: 120, minH: 100 }).catch(() => null);
  await S('customer-card', await orElse(card, q('a[href*="/customers/"]').filter({ visible: true }).first()), B4, { group: g, title: 'Customer card', desc: 'A customer story card/logo tile; measured never followed.', sel: 'customer card' });
  save();
}

async function sales() {
  if (!(await newPage('sales', { wait: 9000 }))) return;
  await sheetsFor('sales');
  await chrome('sales');
  const g = G.sales;
  // The contact card is a centred div.max-w-[800px] (white, on the neutral-50
  // section) — markPainted from an input walks past it to the page shell, so
  // address the card directly.
  await S('sales-card', q('div[class*="max-w-[800px]"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact form card', desc: 'The centred Talk-to-sales card; never filled past a deleted sample, never submitted.', sel: 'sales form card' });
  await S('sales-email', q('input[type="email"], input[name="email"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The work-email input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('sales-message', q('textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Message textarea', desc: 'The "Tell us about your company\'s needs" textarea; focused only.', sel: 'textarea' });
  await S('sales-topic', q('button').filter({ hasText: /^\s*(Tools|Legal|Links|Partners|Analytics)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Topic option', desc: 'A selectable topic pill on the contact form (Tools/Legal/…), read unselected: at rest, on hover, on keyboard focus and forced pressed; never submitted.', sel: 'topic pill button' });
  await S('sales-submit', q('button[type="submit"], button').filter({ hasText: /^\s*Send message\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Send button', desc: 'The Send-message submit; measured, never pressed (a press would submit the form).', sel: 'button "Send message"' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  // The app.dub.co login page paints a transparent column, not a filled card:
  // the centred auth block is div.w-full.max-w-sm (heading + form + SSO row).
  await S('login-card', q('[class*="max-w-sm"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The centred sign-in column (heading, email form, SSO buttons); never filled past a deleted sample, never submitted.', sel: 'login card' });
  await S('email-field', q('input[type="email"], input[name="email"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('email-submit', q('button').filter({ hasText: /^\s*Log in with email\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Email submit', desc: 'The "Log in with email" submit; measured, never pressed (a press would start a sign-in).', sel: 'button "Log in with email"' });
  await S('oauth-google', q('button, a').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO', desc: 'The Continue-with-Google button; measured, never followed.', sel: '"Continue with Google"' });
  await S('oauth-github', q('button, a').filter({ hasText: /Continue with GitHub/i }).filter({ visible: true }).first(), B4, { group: g, title: 'GitHub SSO', desc: 'The Continue-with-GitHub button; measured, never followed.', sel: '"Continue with GitHub"' });
  await S('oauth-saml', q('button, a').filter({ hasText: /SAML SSO/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SAML SSO', desc: 'The Continue-with-SAML-SSO button; measured, never followed.', sel: '"Continue with SAML SSO"' });
  await S('auth-link', q('a').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Auth switch link', desc: 'The "Sign up" link under the card; measured never followed.', sel: 'a "Sign up"' });
  save();
}

async function register() {
  if (!(await newPage('register', { wait: 9000 }))) return;
  const g = G.auth;
  await S('register-card', q('[class*="max-w-sm"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Register card', desc: 'The centred create-account column; never filled or submitted.', sel: 'register card' });
  await S('register-field', q('input[type="email"], input[name="email"], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Register email field', desc: 'The signup email input; focused only, never filled or submitted.', sel: 'register input[type=email]' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 10000 }))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  // Mintlify's real sidebar is nav#sidebar-content; a bare `nav` picks up the
  // "Contact support / Dashboard" top bar instead. Wait for it to hydrate.
  await q('nav#sidebar-content').first().waitFor({ state: 'attached', timeout: 12000 }).catch(() => {});
  await S('docs-sidebar', q('nav#sidebar-content, aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar', desc: 'The left docs navigation column.', sel: 'docs sidebar' }, { noScroll: true });
  await S('docs-nav-item', q('nav#sidebar-content a, nav#sidebar-content button').filter({ hasText: /^\s*(Quickstart|Introduction|Installation|Links API|How attribution works)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item', desc: 'A sidebar navigation item.', sel: 'docs nav item' }, { noScroll: true });
  await S('docs-search', q('button[aria-label="Open search"], button').filter({ hasText: /Search\.\.\./ }).filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger', desc: 'The "Search… ⌘K" trigger; measured, the palette was never opened.', sel: '"Search…"' }, { noScroll: true });
  await S('docs-theme', q('button[aria-label="Change theme preference"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme toggle', desc: 'The "Change theme preference" button; its dropdown supplied the docs dark shots.', sel: 'theme preference button' }, { noScroll: true });
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline', desc: 'The docs page h1 (Introduction).', sel: 'docs h1' }, { noScroll: true });
  await S('docs-copy', q('button[aria-label="Copy page"], button').filter({ hasText: /Copy page/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy-page button', desc: 'The "Copy page" action; measured, never pressed.', sel: '"Copy page"' });
  await S('docs-feedback', q('button').filter({ hasText: /^\s*(Yes|No)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Feedback button', desc: 'A docs "Was this helpful" Yes/No button; measured, never pressed (a press would send feedback).', sel: 'feedback Yes button' });
  // The docs landing cards were never captured: an earlier global `a` lookup
  // for them read the "API Reference" top navigation tab. The nav tab is real
  // evidence, kept under its own name; a docs card entry waits for a capture
  // that scopes to the page content (main/article), not the nav-tabs chrome.
  await S('docs-nav-tab', q('[class*="nav-tabs" i] a, header a, nav a').filter({ hasText: /API reference|Quickstart|Concepts/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav tab', desc: 'The docs surface\'s top navigation tab (API Reference); measured never followed.', sel: 'docs top nav tab' });
  save();
}

async function docsDark() {
  if (!(await newPage('docs-dark', { wait: 10000 }))) return;
  const g = G.docs;
  if (!(await docsTheme('Dark'))) {
    log('  ! docs theme toggle did not apply Dark; the dk-docs-* entries keep their earlier readings instead of saving light evidence under dark names');
    failedPages.add('docs-dark');
    return;
  }
  await S('dk-docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline (dark)', desc: 'The docs h1 with html.dark painted — the real dark theme.', sel: 'docs h1 dark' }, { noScroll: true });
  await S('dk-docs-sidebar', q('nav#sidebar-content, aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar (dark)', desc: 'The left nav column in dark.', sel: 'docs sidebar dark' }, { noScroll: true });
  await S('dk-docs-nav-item', q('nav#sidebar-content a, nav#sidebar-content button').filter({ hasText: /^\s*(Quickstart|Introduction|Installation|Links API|How attribution works)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item (dark)', desc: 'A sidebar item in dark.', sel: 'docs nav item dark' }, { noScroll: true });
  await S('dk-docs-copy', q('button[aria-label="Copy page"], button').filter({ hasText: /Copy page/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy-page button (dark)', desc: 'The "Copy page" action in dark.', sel: '"Copy page" dark' });
  await S('dk-docs-search', q('button[aria-label="Open search"], button').filter({ hasText: /Search\.\.\./ }).filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger (dark)', desc: 'The "Search…" trigger in dark.', sel: '"Search…" dark' }, { noScroll: true });
  if (!(await docsTheme('Light'))) log('  ! docs theme toggle did not return to Light');
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: wordmark, social icons and the Product/Solutions/Resources/Tools/Company link columns.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Docs|Blog|About/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-link', q('footer a[aria-label], footer a[href*="twitter"], footer a[href*="github"], footer a[href*="linkedin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon link', desc: 'A social icon button in the footer (Twitter/GitHub/LinkedIn/YouTube).', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  // At 390 the top bar is a sticky div, not a nav element (both navs are
  // display:none): logo left, round menu button right.
  await S('m-nav', q('[class*="sticky"][class*="top-0"], header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The sticky top bar at 390 (wordmark + menu button).', sel: 'top bar at 390' }, { noScroll: true });
  const menu = q('button').filter({ visible: true }).filter({ has: page.locator('svg') }).first();
  const menuBtn = (await q('button.z-30').filter({ visible: true }).count()) ? q('button.z-30').filter({ visible: true }).first() : menu;
  await S('m-menu-button', menuBtn, ['default'], { group: g, title: 'Menu button', desc: 'The round menu toggle in the mobile nav.', sel: 'mobile menu button' }, { noScroll: true });
  try {
    if (await menuBtn.count()) { await menuBtn.click({ timeout: 5000 }).catch(() => menuBtn.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[class*="fixed"][class*="inset-0"], [role="dialog"], [class*="drawer" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  await S('m-nav-item', q('nav a, nav button, [role="dialog"] a, [role="dialog"] button, body a, body button').filter({ hasText: /^\s*(Product|Solutions|Resources|Customers|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened mobile menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing pages paint light only; /docs and /help paint light or dark through their own theme toggle';
out._meta.tool = 'tools/capture/public/measure.mjs';
// Page arguments may be written kebab-case on the command line (`docs-dark`
// for the docsDark page); a name that still matches no page fails loudly —
// silently skipping a misspelt page used to leave stale entries looking
// freshly measured.
const plan = { home, links, pricing, compare, customers, sales, login, register, docs, docsDark, footer, mobile };
const pages = process.argv.slice(2).map((p) => p.replace(/-([a-z])/g, (_, c) => c.toUpperCase()));
const unknown = pages.filter((p) => !(p in plan));
if (unknown.length) {
  console.error(`unknown page argument(s): ${unknown.join(', ')} — known pages: ${Object.keys(plan).join(', ')}`);
  process.exit(1);
}
const { browser, context: ctx0 } = await launch();
context = ctx0;
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav item), so the
  // delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
