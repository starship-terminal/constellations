// Measures missiveapp.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing docs mobile footer.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// missiveapp.com is a Webflow marketing site; components are found by roles,
// landmark scoping (main vs header/footer) and stable text. Nothing is sent
// or signed into: the only presses are local UI toggles — the nav flyout, a
// pricing FAQ and the mobile menu. Log in, Try for free, the plan CTAs and
// both forms are measured, never followed or submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, cropRect, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', docs: '/docs' };
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
  await page.addStyleTag({ content: '*{caret-color:transparent!important}#ketch-banner,#lanyard_root{display:none!important}' });
  await page.waitForFunction(() => {
    const nav = document.querySelector(window.innerWidth < 700 ? '.navbar.mobile-only' : '.navbar:not(.mobile-only)');
    if (!nav) return false;
    const cs = getComputedStyle(nav);
    return cs.display !== 'none' && nav.getBoundingClientRect().height > 20;
  }, { timeout: 15000 }).catch(() => log('  nav not painted'));
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
      } catch (e) {
        // The element re-rendered between the style read and the crop (Next.js
        // hydration), so the locator no longer resolves: clip the viewport
        // shot from the rect we just measured instead — same pixels, noted.
        try {
          file = s.rect && await cropRect(page, s.rect, `${key}-${state}`, opts.pad ?? 8);
          if (file) s.cropVia = 'rect clip (element re-rendered)';
        } catch (e2) { s.cropError = String(e.message || e).slice(0, 120); }
      }
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
  docs: 'Docs', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 4000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  const nav = q('.navbar:not(.mobile-only)');
  await S('header', nav, ['default'], { group: g, title: 'Header', desc: 'The desktop nav: logo, Product, Pricing, Customers, Resources, Log in, Book a demo, Try for free.', sel: '.navbar:not(.mobile-only)' }, { noScroll: true });
  await S('logo', nav.locator('a[href="/"]').first(), ['default'], { group: g, title: 'Logo', sel: '.navbar a[href="/"]' }, { noScroll: true });
  await S('nav-link', nav.locator('a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A top-level nav link. Measured, never followed.', sel: 'nav a Pricing' }, { noScroll: true });
  await S('nav-login', nav.locator('a').filter({ hasText: /^Log in$/ }).first(), B4, { group: g, title: 'Log in link', desc: 'Opens the mail.missiveapp.com login wall. Measured, never followed.', sel: 'nav a Log in' }, { noScroll: true });
  await S('nav-demo', nav.locator('a').filter({ hasText: /Book a demo/ }).first(), B4, { group: g, title: 'Book a demo', desc: 'Opens an external Calendly page. Measured, never followed.', sel: 'nav a Book a demo' }, { noScroll: true });
  await S('nav-cta', nav.locator('a').filter({ hasText: /Try for free/ }).first(), B4, { group: g, title: 'Try for free', desc: 'Opens the signup wall. Measured, never followed.', sel: 'nav a Try for free' }, { noScroll: true });
  const fly = nav.locator('.w-dropdown-toggle').filter({ hasText: 'Product' }).first();
  await S('flyout-trigger', fly, B4, { group: g, title: 'Product menu trigger', desc: 'The nav item that opens the Product mega menu.', sel: '.w-dropdown-toggle Product' }, { noScroll: true });
  await S('flyout-open', fly, ['opened'], { group: g, title: 'Product menu, open', desc: 'The Product mega menu after hover. Links are recorded in site-tree.md and not followed here.', sel: 'Product dropdown' }, { noScroll: true, open: async () => { await fly.hover(); await page.waitForTimeout(800); }, cropLoc: nav.locator('.navbar-submenu, .floating-menu').first(), pad: 4 });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a').filter({ hasText: /Try for free/ }).nth(1), B4, { group: h, title: 'Hero CTA', desc: 'The hero Try for free. Measured, never followed.', sel: 'hero Try for free' });
  await S('hero-secondary', q('a, div, button').filter({ hasText: /^Watch demo$/ }).first(), ['default', 'hover'], { group: h, title: 'Watch demo', desc: 'Opens the on-page demo lightbox. Measured, not submitted.', sel: 'Watch demo' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', sel: 'h2' });
  await S('tab', q('.w-tab-link').first(), ['default', 'hover'], { group: h, title: 'Feature tab', desc: 'An in-page tab. Selecting it does not navigate.', sel: '.w-tab-link' });
  await S('card', q('a[href^="/customers/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Customer story card', desc: 'A story card. Measured, not opened in this pass.', sel: 'a[href^="/customers/"]' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1/h2' }, { noScroll: true });
  const plan = q('body').getByText('Starter', { exact: true }).first().locator('xpath=ancestor::div[contains(@class,"card") or contains(@class,"pricing")][1]');
  await S('plan-card', q('.w-layout-grid, [class*="pricing"]').locator('div').filter({ hasText: /^Starter/ }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan column. Its CTA goes to the signup wall and is not followed.', sel: 'pricing plan' });
  const faq = q('.w-dropdown-toggle').filter({ hasText: /Can I try Missive/ }).first();
  await S('faq-question', faq, B4, { group: g, title: 'FAQ question', sel: 'pricing FAQ' });
  await S('faq-open', faq, ['opened'], { group: g, title: 'FAQ, open', desc: 'The pricing FAQ after its own toggle.', sel: 'pricing FAQ' }, { cropLoc: faq.locator('xpath=ancestor::div[contains(@class,"w-dropdown")][1]') });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 4000 }))) return;
  const g = G.docs;
  await S('docs-title', q('h1').first(), ['default'], { group: g, title: 'Docs title', sel: 'h1' }, { noScroll: true });
  const field = q('input[name="search-input"], input[type="text"]').filter({ visible: true }).first();
  if (await field.count()) await S('docs-search', field, ['default', 'focused'], { group: g, title: 'Docs search', desc: 'Focused only. Nothing typed, nothing submitted.', sel: 'input[name=search-input]' }, { noScroll: true });
  const area = q('textarea').filter({ visible: true }).first();
  if (await area.count()) await S('docs-chat', area, ['default', 'focused'], { group: g, title: 'Docs chat field', desc: 'The help chat field. Focused only. Nothing typed or sent.', sel: 'textarea' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const foot = q('.is-footer, footer').filter({ visible: true }).first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: '.is-footer' });
  const fl = q('.is-footer a, footer a').filter({ hasText: /^Features$/ }).filter({ visible: true }).first();
  if (await fl.count()) await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a Features' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('.navbar.mobile-only').first(), ['default'], { group: g, title: 'Mobile header', sel: '.navbar.mobile-only' }, { noScroll: true });
  const menuBtn = q('.navbar.mobile-only .menu-mobile-toggle').first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: '.menu-mobile-toggle' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The phone menu after its own toggle.', sel: '.menu-mobile-toggle' }, { cropLoc: q('.navbar.mobile-only .menu-mobile-list'), pad: 0 });
  const mLink = q('.navbar.mobile-only a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first();
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
const plan = { home, pricing, docs, mobile };
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
