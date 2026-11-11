// Measures b150.ai's public components in every state reachable without
// joining, submitting, logging in or signing up.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home vibeathon talent resources about contact mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// b150.ai is a Next.js/Tailwind marketing site in a single painted theme
// (dark chrome, warm-cream inner pages), served in
// English; it declares no design-token custom properties, so every value is a
// computed-style measurement. Selectors key off text and the few semantic
// classes (.label, .vibeathon-link, text-ink). Headless Chrome is served a
// 200 (see lib.mjs); app.b150.ai rate-limits, so the auth links are measured
// but never followed. Nothing is sent, joined or subscribed: the only presses
// are local UI toggles — the mobile menu. Consent or promo layers are hidden
// before every measurement, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', vibeathon: '/vibeathon', talent: '/talent', resources: '/free-resources', about: '/about', contact: '/contact' };
let page, cdp, current, context, run;
let activeCtx; // the context of the current page; closed when the next route opens
const touched = new Set();
const ranPages = new Set();  // pages that actually opened this run
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /access denied|performing security verification|verifying you are human|just a moment|edgesuite\.net/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  // Close the previous route's context first: leaving every context and page
  // running until the whole pass ends keeps each route's scripts, images and
  // timers alive while later routes are measured.
  if (activeCtx) { await activeCtx.close().catch(() => {}); activeCtx = undefined; }
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  activeCtx = ctx;
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const target = URLS[key];
  await open(page, /^https?:/.test(target) ? target : BASE + target, { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); activeCtx = undefined; return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
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

// comp() merges the spec's meta into the entry and marks it touched. The
// page/run/url provenance is only written once the target is found, so a
// re-run whose selector misses keeps the earlier evidence's own page, run and
// url instead of stamping a new date on stale readings (FIELD-NOTES).
function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

function found(c) {
  delete c.missing;
  delete c.recaptureMissed;
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current]) ? URLS[current] : BASE + URLS[current] });
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
  const c = comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0,80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    c.missing = true;
    c.recaptureMissed = run;
    c.states = {}; // stale states from an earlier run are not current evidence
    return;
  }
  found(c);
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
        // a state that did not receive keyboard focus is not a captured focus
        if (via === 'focus failed') throw new Error('keyboard focus did not land on the element');
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
      } else if (st === 'picked') {
        const sel = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await sel.selectOption({ index: 1 }).catch(() => {});
        await page.waitForTimeout(500);
        undo = async () => { await sel.selectOption({ index: 0 }).catch(() => {}); };
        via = 'selectOption index 1, then restored to index 0; nothing submitted';
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (menu, accordion, swatch). Refuses a submit button and any
// control whose text names a purchase/action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|continue|vote|visit)$/i;
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
  shell: 'Shell and navigation', hero: 'Home', vibeathon: 'Vibeathon', talent: 'Talent',
  resources: 'Free resources', about: 'About', contact: 'Contact', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  ranPages.add('home');
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header, [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The top bar: wordmark, VIBEATHON/EVENTS/JOBS/MARKETPLACE/TALENT/FREE RESOURCES nav, LOGIN, SIGN UP.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The wordmark link back to /.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-item', q('header a').filter({ hasText: /^\s*EVENTS\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A top-level nav link (EVENTS). Measured, never followed.', sel: 'header a:has-text("EVENTS")' }, { noScroll: true });
  await S('login-link', q('header a[href="https://app.b150.ai"]').filter({ hasText: /log ?in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'LOGIN in the header, pointing at app.b150.ai — the app gate rate-limits; measured, never followed.', sel: 'a[href="https://app.b150.ai"]' }, { noScroll: true });
  await S('signup-btn', q('header a').filter({ hasText: /^\s*SIGN UP\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign Up button', desc: 'The SIGN UP pill to app.b150.ai/auth/signup. Measured, never followed.', sel: 'header a:has-text("SIGN UP")' }, { noScroll: true });
  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  const h = G.hero;
  await S('hero', q('main h1, [class*="hero" i]').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Don\'t wait for the future. Build it."', sel: 'main h1' });
  await S('hero-cta', q('main a').filter({ hasText: /join the beta|join beta/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'JOIN THE BETA — the primary call-to-action. Measured, never followed.', sel: ':has-text("JOIN THE BETA")' });
  await S('home-section', q('main section, main [class*="section" i]').filter({ hasText: /\S/ }).filter({ visible: true }).nth(1), ['default'], { group: h, title: 'Home section', desc: 'A content section below the hero.', sel: 'main section' });
  save();
}

async function vibeathon() {
  if (!(await newPage('vibeathon', { wait: 9000 }))) return;
  ranPages.add('vibeathon');
  const g = G.vibeathon;
  await S('vibe-title', q('h1, h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Vibeathon title', sel: 'h1' }, { noScroll: true });
  await S('vibe-card', q('main [class*="card" i], main article, main li, main section').filter({ visible: true }).first(), ['default'], { group: g, title: 'Vibeathon block', desc: 'The first card/section on the vibeathon page.', sel: 'main [class*="card"]' });
  await S('vibe-cta', q('main a, main button').filter({ hasText: /join|register|apply|sign ?up|submit|learn more/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Vibeathon CTA', desc: 'The first call-to-action on /vibeathon. Measured, never followed.', sel: 'main a:has-text("join")' });
  save();
}

async function talent() {
  if (!(await newPage('talent', { wait: 9000 }))) return;
  ranPages.add('talent');
  const g = G.talent;
  await S('talent-title', q('h1, h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Talent title', sel: 'h1' }, { noScroll: true });
  await S('talent-card', q('main [class*="card" i], main article, main ul a, main li').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Talent card', desc: 'A talent/profile card on the talent surface. Measured, never followed.', sel: 'main [class*="card"]' });
  await S('talent-cta', q('main a, main button').filter({ hasText: /join|hire|contact|apply|view|sign ?up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Talent CTA', desc: 'The first call-to-action on /talent. Measured, never followed.', sel: 'main a' });
  save();
}

async function resources() {
  if (!(await newPage('resources', { wait: 9000 }))) return;
  ranPages.add('resources');
  const g = G.resources;
  await S('res-title', q('h1, h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Resources title', sel: 'h1' }, { noScroll: true });
  await S('res-card', q('main [class*="card" i], main article, main li, main section a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A free-resource card. Measured, never followed.', sel: 'main [class*="card"]' });
  save();
}

async function about() {
  if (!(await newPage('about', { wait: 9000 }))) return;
  ranPages.add('about');
  const g = G.about;
  await S('about-title', q('h1, h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'About title', sel: 'h1' }, { noScroll: true });
  await S('about-body', q('main p, main div').filter({ hasText: /\w+(\s+\w+){10,}/ }).last().filter({ visible: true }).first(), ['default'], { group: g, title: 'About body', desc: 'A body-copy block on /about.', sel: 'main p' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 9000 }))) return;
  ranPages.add('contact');
  const g = G.contact;
  await S('contact-title', q('h1, h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', sel: 'h1' }, { noScroll: true });
  await S('contact-input', q('input[type="text"], input[type="email"], input:not([type]), textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Contact field', desc: 'A contact form field; focused only, never submitted.', sel: 'input' });
  await S('contact-email', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Contact email field', desc: 'The email input; focused only, never submitted.', sel: 'input[type="email"]' });
  await S('contact-button', q('button[type="submit"], button').filter({ hasText: /send|submit|contact/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Contact button', desc: 'The submit; measured except a real press — the form was never submitted.', sel: 'button[type="submit"]' });
  save();
}

async function footer() {
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  ranPages.add('home');
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); return; }
    await closePromo(page);
    ranPages.add('home');
  }
  const g = G.footer;
  // The footer holds section links; scroll it into view first.
  await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(1800);
  const fl = q('footer a, [class*="footer" i] a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  if (await fl.count()) {
    await S('footer', q('footer, [class*="footer" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    const nl = q('footer input[type="email"], [class*="footer" i] input[name*="email" i]').first();
    if (await nl.count()) await S('newsletter-input', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; never subscribed.', sel: 'footer input[type="email"]' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  ranPages.add('home');
  const g = G.mobile;
  await S('m-header', q('header, [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('header [class*="burger" i], header button, nav button, [class*="menu" i] button').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'header button' }, { noScroll: true });
  const drawer = q('[class*="menu" i][class*="open" i], [class*="drawer" i], nav').filter({ visible: true }).last();
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The menu button after its own toggle; the crop is the open menu layer.', sel: 'header button' }, { noScroll: true, cropLoc: drawer });
  const mLink = q('nav a, [class*="menu" i] a, header a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A row inside the opened menu.', sel: 'nav a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-cta', q('a').filter({ hasText: /join|sign ?up/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile CTA', desc: 'A JOIN/SIGN UP button on mobile.', sel: 'a:has-text("JOIN")' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, vibeathon, talent, resources, about, contact };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Only a page that actually opened may lose its untouched components; a
    // blocked or thrown route keeps its earlier readings instead of erasing
    // them with an incomplete write.
    if (!touched.has(key) && !pages.length && ranPages.has(c.page)) { delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
