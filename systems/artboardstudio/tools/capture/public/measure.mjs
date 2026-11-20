// Measures artboard.studio's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home mockup figma mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// artboard.studio is a Webflow marketing site in one light theme; components
// are found by Webflow's semantic classes (button is-link, tab-button,
// heading-*, w-nav-*), roles and stable text. Nothing is sent or signed
// into: the only presses are local UI toggles — a mockup-category tab and
// the mobile menu. "Signup", "Mockup Library" and every editor link are
// measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', mockup: '/mockup', figma: '/figma-mockup', blog: '/blog' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
const reached = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close' } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  if (!(await open(page, BASE + URLS[key], { wait, promo }))) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  reached.add(mobile ? '@' + key : key);
  return true;
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
  // Found again: a retry's fresh readings replace the earlier miss record, so
  // the token builder stops rejecting them.
  delete out.components[key].recaptureMissed;
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        await toggle(loc, { allowLink: true });
        await page.waitForTimeout(500);
        via = 'own toggle, pressed once; a local UI state, never submitted';
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

// Clicks a UI toggle (drawer, accordion, menu). Refuses a submit button and
// any control whose text names a purchase, consent or location answer this
// kit must never take.
const NEVER = /^(accept all|only required cookies|continue to|stay in|send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|shop now|read more)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Home', mockup: 'Mockup library',
  figma: 'Figma plugin page', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('.navbar-no-shadow, header, .navbar.w-nav, nav').first(), ['default'], { group: g, title: 'Header', desc: 'The top nav: wordmark, Mockup Library and Figma plugin links, Signup.', sel: 'header' }, { noScroll: true });
  await S('logo', q('a.w-nav-brand, a:has-text("Artboard")').first(), ['default'], { group: g, title: 'Logo', sel: 'nav brand' }, { noScroll: true });
  await S('nav-link', q('a.button.is-link').filter({ hasText: /Mockup Library/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A .button.is-link nav item. Measured, never followed.', sel: 'a.button.is-link' }, { noScroll: true });
  await S('nav-signup', q('a.button.is-link').filter({ hasText: /^Signup$/ }).first(), B4, { group: g, title: 'Signup link', desc: 'The signup nav action. Measured, never followed.', sel: 'a:has-text("Signup")' }, { noScroll: true });
  // The New version / Legacy version cards live in a collapsed nav dropdown (0px); not measured.

  const h = G.home;
  await S('hero-title', q('h1, .heading-style-h1').first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  const tab = q('.tab-button.w-tab-link').first();
  await S('tab', tab, B4, { group: h, title: 'Category tab', desc: 'A mockup-category tab (Most Popular is the selected one).', sel: '.tab-button.w-tab-link' });
  await S('tab-selected', q('.tab-button.w-tab-link.w--current').first(), ['default'], { group: h, title: 'Tab, selected', sel: '.w-tab-link.w--current' });
  // Pin the tab before its toggle: once selected it gains .w--current, and a live
  // :not(.w--current) locator would re-resolve to another, unselected tab.
  await q('.tab-button.w-tab-link:not(.w--current)').filter({ visible: true }).first()
    .evaluate((el) => el.setAttribute('data-m-pick', 'tab'), null, { timeout: 5000 }).catch(() => {});
  await S('tab-switched', q('[data-m-pick="tab"]'), ['selected'], { group: h, title: 'Tab, switched', desc: 'A tab after its own toggle; the selection moves locally.', sel: '.w-tab-link' }, { after: { selected: async () => { await page.waitForTimeout(800); } } });
  await S('section-title', q('h2, .heading-2').filter({ hasText: /Mockups$/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', sel: 'h2 mockup section' });
  const card = q('.div-block-19.w-dyn-item, .w-dyn-item:has(img)').filter({ visible: true }).first();
  await S('mockup-card', card, ['default', 'hover'], { group: h, title: 'Mockup card', desc: 'A mockup preview tile link.', sel: '.div-block-19.w-dyn-item' });
  await S('plugin-cta', q('a.button.is-icon, a[class*="is-icon"]').filter({ hasText: /Install|plugin/i }).first(), B4, { group: h, title: 'Plugin CTA', desc: 'The "Install Figma plugin" icon action. Measured, never followed.', sel: 'a.button.is-icon' });
  await S('contact-cta', q('a.button.is-icon, a[class*="is-icon"]').filter({ hasText: /Contact/i }).first(), B4, { group: h, title: 'Contact CTA', desc: 'The Contact icon action. Measured, never followed.', sel: 'a:has-text("Contact")' });
  save();
}

async function mockup() {
  if (!(await newPage('mockup'))) return;
  const g = G.mockup;
  await S('lib-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library title', sel: 'h1/h2' }, { noScroll: true });
  const filt = q('input[type="search"], input[placeholder*="earch" i], input').filter({ visible: true }).first();
  if (await filt.count()) await S('search-field', filt, ['default', 'focused'], { group: g, title: 'Library search field', desc: 'Focused only; nothing typed or sent.', sel: 'search input' }, { noScroll: true });
  const chip = q('a, button').filter({ hasText: /Device|Apparel|iPhone|All/i }).filter({ visible: true }).first();
  await S('filter-chip', chip, B4, { group: g, title: 'Filter chip', desc: 'A category filter on the library. Measured, never selected.', sel: 'filter chip' });
  const card = q('a').filter({ has: q('img') }).filter({ visible: true }).nth(2);
  await S('lib-card', card, ['default', 'hover'], { group: g, title: 'Library card', desc: 'A mockup thumbnail tile.', sel: 'library tile' });
  save();
}

async function figma() {
  if (!(await newPage('figma'))) return;
  const g = G.figma;
  await S('figma-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Figma page title', sel: 'h1/h2' }, { noScroll: true });
  const cta = q('a').filter({ hasText: /Install|plugin|Try|Start/i }).filter({ visible: true }).first();
  await S('figma-cta', cta, B4, { group: g, title: 'Figma install CTA', desc: 'The page primary action. Measured, never followed.', sel: 'install CTA' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const foot = q('.footer, footer').first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: 'footer' });
  const fl = q('.footer a, footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
  const soc = q('.footer a[href*="twitter"], footer a[href*="instagram"], footer a[href*="dribbble"], footer a[aria-label]').filter({ visible: true }).first();
  if (await soc.count()) await S('footer-social', soc, B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('.navbar-no-shadow, header, .navbar.w-nav, nav').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('.w-nav-button, .menu-button, button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The bar after its own toggle; the crop is the opened nav panel.', sel: '.w-nav-button' }, { cropLoc: q('nav, .w-nav-menu, [class*="nav-menu"]').filter({ visible: true }).last(), pad: 0 });
  const mLink = q('a.button.is-link, nav a').filter({ hasText: /Mockup Library/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'Read inside the open menu.', sel: 'nav link' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, mockup, figma, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune entries this run never touched only when their page was actually
    // reached: a blocked page must not erase the readings saved under it.
    const src = c.group === G.mobile ? '@' + c.page : c.page;
    if (!touched.has(key) && !pages.length && reached.has(src)) { delete out.components[key]; continue; }
    if (!Object.keys(c.states || {}).length && !c.missing && touched.has(key)) delete out.components[key];
  }
  save();
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
