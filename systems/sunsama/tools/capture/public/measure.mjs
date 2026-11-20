// Measures Sunsama's public components in every state reachable without
// signing in, typing an email, or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing explore mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// butter.video is a Next.js marketing app (styled-components, index-style__*
// classes) whose /explore, /blocks and /templates pages hand off to a dark MUI
// app shell (MuiButtonBase/css-* classes) that is public signed-out. Nothing
// is sent, bought or signed into: the only presses are local UI toggles — the
// nav dropdown, the billing period buttons and the mobile menu. The iubenda
// consent banner is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', compare: '/compare', blog: '/blog',
  signup: '/start/signup', feature: '/features/daily-planning',
  integration: '/integrations/asana', protips: '/pro-tips',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
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
  await open(page, url || BASE + URLS[key], { wait, promo });
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
        throw new Error('filled refused: this capture does not type into fields');
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|start for free|try for free|try it today)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  compare: 'Compare', feature: 'Feature demo', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 2500 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.navbar, .w-nav').first(), ['default'], { group: g, title: 'Header', desc: 'The Webflow nav: logo, flat links, Login, Start for Free. No hover menu.', sel: '.navbar' }, { noScroll: true });
  await S('logo', q('.navbar a[href="/"], .brand').first(), ['default'], { group: g, title: 'Logo', desc: 'The home link in the nav.', sel: '.navbar a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('.w-nav a, .navbar_link, a.nav-link').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A flat nav link. Opens a page. Does not open a menu.', sel: 'a Pricing' }, { noScroll: true });
  await S('nav-login', q('a.navlinkitem.login').first(), B4, { group: g, title: 'Login link', desc: 'Opens https://app.sunsama.com/login. Measured, never followed. The duplicate ondesktop copy is hidden at 1440.', sel: 'a.navlinkitem.login' }, { noScroll: true });
  await S('nav-cta', q('a[href="/start/signup"]').first(), B4, { group: g, title: 'Start for Free', desc: 'Header CTA to /start/signup. Measured, never followed.', sel: 'a[href=/start/signup]' }, { noScroll: true });
  await S('ai-pill', q('button.ss-pill').first(), B4, { group: G.home, title: 'AI assistant pill', desc: 'Opens the in-page assistant dialog. Not a signup.', sel: 'button.ss-pill' });
  await S('ai-panel', q('.ss-panel').first(), ['opened'], { group: G.home, title: 'AI assistant panel', desc: 'The dialog the pill opens. Tabs swap setup steps. Close is .ss-panel_close.', sel: '.ss-panel' }, { open: async () => { await q('button.ss-pill').first().click(); await page.waitForTimeout(500); }, noToggle: true });
  await S('ai-tab', q('button.ss-panel_tile').filter({ hasText: /ChatGPT/ }).first(), ['default', 'hover', 'pressed', 'selected'], { group: G.home, title: 'Assistant tab', desc: 'A tab inside the assistant panel. Swaps the step pane.', sel: 'button.ss-panel_tile' }, { open: async () => { await q('button.ss-pill').first().click(); await page.waitForTimeout(400); }, noReset: true, before: { selected: async (loc) => { await loc.click(); await page.waitForTimeout(300); return 'clicked the tab'; } } });
  await S('hero-title', q('.headlinemain').first(), ['default'], { group: G.home, title: 'Hero title', desc: 'The homepage headline. It is a div.headlinemain, not an h1.', sel: '.headlinemain' });
  await S('cta-primary', q('a').filter({ hasText: /^Try for free$/ }).first(), B4, { group: G.home, title: 'Primary CTA', desc: 'The hero Try for free link to /start/signup. Measured, never followed.', sel: 'a Try for free' });
  await S('slider-next', q('.sliderarrow.w-slider-arrow-right').first(), B4, { group: G.home, title: 'Slider next', desc: 'Advances the homepage testimonial slider. No new page.', sel: '.w-slider-arrow-right' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 2200 }))) return;
  await chrome('pricing');
  await S('price-card', q('.pricing-card, .pricetable_card, .price-card, .w-layout-grid > div').filter({ hasText: /Pro Plan|per month/ }).first(), ['default'], { group: G.pricing, title: 'Price card', desc: 'The public Pro price. No billing toggle on the page.', sel: 'price card' });
  await S('faq-title', q('.about-philosophy_title').first(), ['default'], { group: G.pricing, title: 'FAQ title', desc: 'A pricing FAQ heading. The answer is already visible. Not a disclosure.', sel: '.about-philosophy_title' });
  save();
}

async function compare() {
  if (!(await newPage('compare', { wait: 2200 }))) return;
  await S('compare-tab', q('.compare_tab-link').nth(1), ['default', 'hover', 'pressed', 'selected'], { group: G.compare, title: 'Compare tab', desc: 'A competitor logo tab. Swaps the comparison pane. Logo is Motion.', sel: '.compare_tab-link' }, { before: { selected: async (loc) => { await loc.click(); await page.waitForTimeout(300); return 'clicked the tab'; } } });
  save();
}

async function feature() {
  if (!(await newPage('feature', { wait: 2200 }))) return;
  await S('demo-button', q('.ap-demo_go').first(), B4, { group: G.feature, title: 'Plan my day', desc: 'Starts the in-page planning demo. Stays on the page. Not a form submit.', sel: '.ap-demo_go' });
  await S('demo-panel', q('.ap-demo').first(), ['opened'], { group: G.feature, title: 'Planning demo', desc: 'The demo panel after Plan my day.', sel: '.ap-demo' }, { open: async () => { await q('.ap-demo_go').first().click(); await page.waitForTimeout(600); }, noToggle: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 2000 }))) return;
  await S('signup-title', q('h1').first(), ['default'], { group: 'Signup wall', title: 'Signup heading', desc: 'The public signup wall. Email was not typed. The form was not submitted.', sel: 'h1' });
  await S('signup-field', q('#email-form input[type="email"]').first(), ['default', 'focus-visible'], { group: 'Signup wall', title: 'Signup email field', desc: 'Email field on the signup wall. Nothing typed. Nothing submitted.', sel: '#email-form input[type=email]' });
  save();
}

async function integration() {
  if (!(await newPage('integration', { wait: 2200 }))) return;
  await S('lightbox-link', q('a.w-lightbox, .w-lightbox').first(), ['default'], { group: 'Integrations', title: 'See how it works', desc: 'A Webflow lightbox trigger on the integration page. The control is an image link, so text matching misses it. States beyond default are Not captured this pass.', sel: 'a.w-lightbox' });
  save();
}

async function protips() {
  if (!(await newPage('protips', { wait: 2200 }))) return;
  await S('category-button', q('.pt-select__button').first(), ['default', 'hover', 'focus-visible', 'opened'], { group: 'Pro tips', title: 'Category combobox', desc: 'Opens the public tip-category listbox. No search text typed.', sel: '.pt-select__button' }, { before: { opened: async (loc) => { await loc.click(); await page.waitForTimeout(300); return 'opened the listbox'; } } });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 1800 }))) return;
  await S('footer', q('.footer').first(), ['default'], { group: G.footer, title: 'Footer', desc: 'Product, platform, and legal links. Newsletter field is present and was not filled.', sel: '.footer' });
  await S('footer-link', q('.footer a').filter({ hasText: /^Privacy$/ }).first(), B4, { group: G.footer, title: 'Footer link', desc: 'A legal footer link.', sel: '.footer a' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 2200 }))) return;
  const g = G.mobile;
  await S('m-header', q('.navbar, .w-nav').first(), ['default'], { group: g, title: 'Mobile header', desc: 'The 390 header. The desktop link row is hidden.', sel: '.navbar at 390' }, { noScroll: true });
  await S('m-menu-button', q('.menu-button-2').first(), B4, { group: g, title: 'Menu button', desc: 'Opens the phone nav overlay. aria-controls=w-nav-overlay-0.', sel: '.menu-button-2' }, { noScroll: true });
  try {
    await q('.menu-button-2').click({ timeout: 4000 });
    await page.waitForTimeout(600);
  } catch (e) { log('  ! mobile menu', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('.w-nav-overlay').first(), ['default'], { group: g, title: 'Mobile menu', desc: 'The opened overlay: Features, Integrations, Pricing, Love, About, Blog, Login.', sel: '.w-nav-overlay' }, { noScroll: true, crop: false });
  await S('m-nav-item', q('.w-nav-overlay a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened phone menu.', sel: '.w-nav-overlay a' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); public marketing site paints light only';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, compare, feature, signup, integration, protips, footer, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a.button, .navbar a, button.ss-pill');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
