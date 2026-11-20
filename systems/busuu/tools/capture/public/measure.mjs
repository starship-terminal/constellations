// Measures busuu.com's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home premium course register login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// busuu.com is a Bootstrap marketing front over a React (styled-components)
// app: marketing classes are semantic, app surfaces carry generated sc-*
// names, so specs select by role and structure. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — nav dropdowns, period
// options and the mobile menu. The OneTrust consent stack is hidden, never
// answered; the register flow's language picker is measured, never chosen.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', premium: '/en/premium', course: '/en/course/learn-spanish-online', register: '/en/register', login: '/en/login' };
let page, cdp, current, context, run;
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
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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
  shell: 'Shell and navigation', home: 'Home', premium: 'Premium', course: 'Course pages',
  forms: 'Signup and login', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header, .main-header-simplified').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The marketing header: logo, Learn for free, Log in, For Educators/Businesses.', sel: 'header.main-header-simplified' }, { noScroll: true });
  await S('logo', q('a.nav-dropdown__logo, nav a:has(svg), nav a:has(img)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The wordmark anchor (a.nav-dropdown__logo, a labelled svg), top-left of the nav bar.', sel: 'a.nav-dropdown__logo' }, { noScroll: true });
  await S('nav-link', q('.nav-dropdown__btn, .responsive-nav a, nav a').filter({ hasText: /Log\s*in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The nav\'s Log-in outline button (a.nav-dropdown__btn.btn--outline-default); measured, never followed.', sel: '.nav-dropdown__btn.btn--outline-default' }, { noScroll: true });
  await S('cta-signup', q('header a').filter({ hasText: /Learn for free|Get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup CTA', desc: 'The header CTA; links to signup, measured never followed.', sel: 'header signup CTA' }, { noScroll: true });
  // The dropdown panel only. `.nav-dropdown` is the class of the whole nav bar
  // (nav.nav-dropdown, 1400 x 40), so it recorded the bar; the panel is
  // div.main-nav-dropdown with its ul.main-nav-dropdown__list, which shows only
  // while the menu is open. If it is closed, S() records the entry missing.
  await S('nav-dropdown', q('div.main-nav-dropdown, ul.main-nav-dropdown__list').filter({ visible: true }).first(), B4, { group: g, title: 'Nav dropdown', desc: 'The language/product dropdown panel in the header.', sel: 'div.main-nav-dropdown' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1, .header-simplified__title').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', sel: 'h1.header-simplified__title' }, { noScroll: true });
  await S('hero-cta', q('main a, main button, section a, section button').filter({ hasText: /Start learning|Get started|Learn for free/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero action; measured never followed.', sel: 'hero CTA (main/section scope)' });
  await S('hero-sub', q('main p, section p, .header-simplified p').filter({ hasText: /Busuu understands|another language|speak up|goal/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline.', sel: 'hero lede paragraph' });
  await S('flag-card', q('[data-cy="HomePage__flagModule"] a, [data-cy="HomePage__flagModule"] li, [class*="flag" i] a').filter({ visible: true }).first(), B4, { group: h, title: 'Language card', desc: 'A language entry in the flag module.', sel: 'flag module item' });
  save();
}

async function premium() {
  if (!(await newPage('premium', { url: BASE + '/en/premium', wait: 12000 }))) return;
  await sheetsFor('premium');
  await chrome('premium');
  const g = G.premium;
  await S('premium-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Premium title', sel: 'h1/h2 on /en/premium' }, { noScroll: true });
  await S('period-toggle', q('button, [role="tab"], a, span').filter({ hasText: /1 month|12 months/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Period toggle', desc: 'A billing-period option (12 months/1 month).', sel: 'period option' }, { noScroll: true });
  await S('plan-card', q('div').filter({ hasText: /Get Premium/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Plan card', desc: 'A Premium plan tier card (the Get Premium column).', sel: 'deepest div containing Get Premium' });
  await S('plan-price', q('p, span').filter({ hasText: /\$[0-9]+\.[0-9]{2}\/month|\$\d+\.\d{2}$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A monthly price figure inside a tier card.', sel: 'price text' });
  await S('plan-cta', q('a, button').filter({ hasText: /Get Premium/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A Get Premium action; measured never followed.', sel: 'Get Premium button' });
  await S('save-badge', q('p, span').filter({ hasText: /SAVE\s*\d+%/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Save badge', desc: 'A SAVE n% label on the plan cards.', sel: 'p with SAVE n%' });
  save();
}

async function course() {
  if (!(await newPage('course', { url: BASE + '/en/course/learn-spanish-online', wait: 9000 }))) return;
  const g = G.course;
  await S('course-title', q('h2').filter({ hasText: /Discover|Spanish/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Course page title', desc: 'The visible display heading (the semantic h1 is clipped for accessibility).', sel: 'h2 course display heading' }, { noScroll: true });
  await S('course-cta', q('main a, section a, main button').filter({ hasText: /Start|Learn|Try|Sign/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Course CTA', desc: 'The course page action: the anchor computes transparent and its child button paints the green fill on a 100px radius over the blue band; measured, never followed.', sel: 'course page CTA' });
  await S('course-section', q('main h2, section h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', sel: 'course page h2' });
  save();
}

async function register() {
  if (!(await newPage('register', { url: BASE + '/en/register', wait: 12000 }))) return;
  const g = G.forms;
  await S('language-item', q('button, a, li, [role="button"]').filter({ hasText: /English\s*26M|English learners|^English/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Language option', desc: 'A language choice in the signup flow; measured never chosen.', sel: 'language option' }, { noScroll: true });
  await S('register-title', q('h1, h2, [role="heading"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup heading', sel: 'register heading' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer, .main-footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The main-footer: link columns, social, legal.', sel: '.main-footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .main-footer__list a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: '.main-footer a' }, { noScroll: true });
  await S('social-icon', q('.main-footer__credits-socials a, footer a[href*="facebook"], footer a[href*="twitter"], footer a[href*="instagram"], footer a[href*="youtube"], footer a[href*="linkedin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', sel: 'footer social link' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header, .main-header-simplified').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  // The kebab is an empty <a> wrapping span.responsive-nav__icon (the control
  // fixup.mjs clicks for the menu shots); it is a local UI toggle.
  const kebab = q('span.responsive-nav__icon').filter({ visible: true }).first();
  await S('m-menu-button', kebab, ['default'], { group: g, title: 'Menu button', desc: 'The kebab toggle: an empty anchor wrapping span.responsive-nav__icon.', sel: 'span.responsive-nav__icon' }, { noScroll: true });
  try {
    if (await kebab.count()) {
      await kebab.click({ timeout: 5000 }).catch(() => kebab.evaluate((el) => (el.closest('a') || el).click()));
      await page.waitForTimeout(1600);
    }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('.main-nav-dropdown__list, .nav-dropdown__list, .responsive-nav nav, .responsive-nav ul').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The kebab dropdown, opened by its own toggle.', sel: 'opened responsive nav list' }, { noScroll: true });
  await S('m-nav-item', q('.main-nav-dropdown__link').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened responsive nav dropdown.', sel: '.main-nav-dropdown__link' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1, .header-simplified__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, premium, course, register, login: () => {}, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'login') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header');
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
