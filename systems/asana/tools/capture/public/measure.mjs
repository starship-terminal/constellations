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
const URLS = { home: '/', pricing: '/pricing', sales: '/sales', gate: '/create-account' };
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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  gate: 'Create account gate', sales: 'Contact sales',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The top nav: logo, Pricing link, Log in, Contact sales, Get started.', sel: 'header/nav' }, { noScroll: true });
  await S('logo', q('a[class*="logo-link"], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', sel: 'a[class*=logo-link]' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A top-level nav link. Measured, never followed.', sel: 'a:has-text("Pricing")' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The Log in nav action. Measured, never followed.', sel: 'a:has-text("Log in")' }, { noScroll: true });
  await S('nav-sales', q('a').filter({ hasText: /^Contact sales$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact sales button', desc: 'The secondary CTA. Measured, never followed.', sel: 'a:has-text("Contact sales")' }, { noScroll: true });
  await S('nav-cta', q('a').filter({ hasText: /^Get started$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get started button', desc: 'The primary CTA. Measured, never followed.', sel: 'a:has-text("Get started")' }, { noScroll: true });
  const fly = q('a[class*="flyout-link"], nav button, nav a').filter({ hasText: /Product|Solutions|Asana AI/i }).filter({ visible: true }).first();
  await S('flyout-trigger', fly, B4, { group: g, title: 'Flyout trigger', desc: 'The nav item opening the product flyout.', sel: 'nav flyout trigger' }, { noScroll: true });
  await S('flyout-open', fly, ['opened'], { group: g, title: 'Flyout, open', desc: 'The nav after a hover opens the flyout; the crop is the opened panel.', sel: 'nav flyout trigger' }, { open: async () => { await fly.hover(); await page.waitForTimeout(1200); return 'mouse hover'; }, cropLoc: q('[class*="flyout"]:not(a):not(li), nav[class*="flyout"], [role="dialog"]').filter({ visible: true }).last(), pad: 0 });

  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  const hcta = q('a').filter({ hasText: /Get started|Try free|See pricing/i }).filter({ visible: true }).nth(1);
  await S('hero-cta', hcta, B4, { group: h, title: 'Hero CTA', desc: 'A hero action. Measured, never followed.', sel: 'hero CTA' });
  await S('caps-label', q('[class*="caps"], h3, h4').filter({ hasText: /AI TEAMMATES|ASANA/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Caps label', desc: 'A small-caps eyebrow label.', sel: 'caps eyebrow' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', sel: 'h2' });
  const card = q('a').filter({ has: q('img') }).filter({ visible: true }).nth(2);
  await S('card', card, ['default', 'hover'], { group: h, title: 'Card', desc: 'A linked feature/customer card.', sel: 'card link' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1/h2' }, { noScroll: true });
  const toggle = q('button[role="switch"], [role="switch"], button[class*="toggle"], label[class*="toggle"]').filter({ visible: true }).first();
  if (await toggle.count()) await S('billing-toggle', toggle, B4, { group: g, title: 'Billing toggle', desc: 'The monthly/annual switch. Measured, never switched.', sel: 'billing toggle' }, { noScroll: true });
  const plan = q('h3:has-text("Personal"), h3:has-text("Starter")').first().locator('xpath=ancestor::*[self::section or self::div][3]');
  await S('plan-card', plan, ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan column.', sel: 'plan card' });
  const pcta = q('a, button').filter({ hasText: /Get started|Try for free|Buy now|Contact sales/i }).filter({ visible: true }).nth(1);
  await S('plan-cta', pcta, B4, { group: g, title: 'Plan CTA', desc: 'A plan action. Measured, never followed.', sel: 'plan CTA' });
  const faq = q('button[aria-expanded], details summary').filter({ visible: true }).first();
  await S('faq-question', faq, B4, { group: g, title: 'FAQ question', sel: 'pricing FAQ' });
  await S('faq-open', faq, ['opened'], { group: g, title: 'FAQ, open', desc: 'The row after its own toggle.', sel: 'pricing FAQ' }, { cropLoc: faq.locator('xpath=ancestor::*[self::details or self::li or self::section or self::div][1]') });
  save();
}

async function gate() {
  if (!(await newPage('gate'))) return;
  const g = G.gate;
  await S('gate-title', q('main h1, main h2, [role="heading"], main [class*="heading" i], main [class*="title" i], main strong').filter({ visible: true }).first(), ['default'], { group: g, title: 'Gate title', sel: 'gate heading' }, { noScroll: true });
  const field = q('input').filter({ visible: true }).first();
  if (await field.count()) await S('gate-field', field, ['default', 'focused'], { group: g, title: 'Gate field', desc: 'Focused only; nothing typed or sent.', sel: 'gate input' }, { noScroll: true });
  const cta = q('button, a').filter({ hasText: /Continue|Get started|Sign up|Create/i }).filter({ visible: true }).first();
  await S('gate-cta', cta, B4, { group: g, title: 'Gate CTA', desc: 'The form action. Measured, never pressed.', sel: 'gate CTA' });
  const sso = q('a, button').filter({ hasText: /Google|SSO|Apple/i }).filter({ visible: true }).first();
  if (await sso.count()) await S('gate-sso', sso, B4, { group: g, title: 'SSO button', desc: 'A single-sign-on option. Measured, never pressed.', sel: 'SSO button' });
  save();
}

async function sales() {
  if (!(await newPage('sales'))) return;
  const g = G.sales;
  await S('sales-title', q('h1, h2, h3, [role="heading"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sales title', sel: 'h1/h2/h3' }, { noScroll: true });
  const field = q('input').filter({ visible: true }).first();
  if (await field.count()) await S('sales-field', field, ['default', 'focused'], { group: g, title: 'Sales field', desc: 'Focused only; nothing typed or sent.', sel: 'form input' });
  const sel = q('select, [role="combobox"], [role="listbox"]').filter({ visible: true }).first();
  if (await sel.count()) await S('sales-select', sel, B4, { group: g, title: 'Sales select', desc: 'A form dropdown. Measured, never opened.', sel: 'form select' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const foot = q('footer').filter({ visible: true }).first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: 'footer' });
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  if (await fl.count()) await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
  const soc = q('footer a[aria-label], footer a[href*="linkedin"], footer a[href*="twitter"]').filter({ visible: true }).first();
  if (await soc.count()) await S('footer-social', soc, B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('button[aria-label*="menu" i], [class*="hamburger"], button[class*="menu"], button[class*="nav"]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'menu button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The bar after its own toggle; the crop is the opened nav panel.', sel: 'menu button' }, { cropLoc: q('nav, [role="dialog"], [class*="drawer"], [class*="menu"]').filter({ visible: true }).last(), pad: 0 });
  const mLink = q('a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first();
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
const plan = { home, pricing, gate, sales, mobile };
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
