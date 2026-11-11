// Measures boords.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing script-timer ai-storyboard signup login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// boords.com is a Next.js/Tailwind app: classes are utilities plus a few
// semantic names (card-surface, nav-menu-trigger), so specs select by role
// and structure. Nothing is sent, bought or signed into: the only presses
// are local UI toggles — the site menu, nav flyouts, billing tabs, accordions
// and the script timer's options. Forms are focused/filled, never submitted;
// consent overlays are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', 'script-timer': '/script-timer', 'ai-storyboard': '/ai-storyboard-generator', signup: '/signup', login: '/login' };
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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  tools: 'Public tools', pages: 'Product pages', forms: 'Sign-in and demo forms',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header pill', desc: 'The floating rounded-full header bar: logo, nav, menu button, Book a demo.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /Pricing|Blog|Changelog/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', sel: 'header a' }, { noScroll: true });
  await S('nav-trigger', q('button.nav-menu-trigger').filter({ visible: true }).first(), B4, { group: g, title: 'Nav dropdown', desc: 'A nav-menu-trigger in the header; opens a flyout.', sel: 'button.nav-menu-trigger' }, { noScroll: true });
  await S('nav-trigger-open', q('button.nav-menu-trigger').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Nav dropdown, open', desc: 'After its own toggle; the opened flyout shows in the crop.', sel: 'button.nav-menu-trigger', cropLoc: q('header').first() }, { noScroll: true });
  await S('menu-button', q('button[aria-label="Open menu"]').filter({ visible: true }).first(), B4, { group: g, title: 'Menu button', desc: 'The round icon button that opens the site menu.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  await S('cta-demo', q('a[href^="/demo"]').filter({ visible: true }).first(), B4, { group: g, title: 'Book a demo CTA', desc: 'The header CTA; links to the demo form, measured never followed.', sel: 'a[href^="/demo"]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a, section a').filter({ hasText: /Try|Start|Free|Get started|Sign up/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero action; measured never followed.', sel: 'main a CTA' });
  await S('hero-sub', q('main p, section p').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede paragraph under the headline.', sel: 'hero paragraph' });
  await S('feature-card', q('main .card-surface, section .card-surface').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature card', desc: 'A card-surface section card on the home page.', sel: '.card-surface' });
  await S('feature-link', q('main a').filter({ hasText: /Learn more|See how|Explore|Read/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Feature link', sel: 'main link' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 9000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1/h2 on /pricing' }, { noScroll: true });
  await S('billing-tab', q('button[role="tab"]').filter({ visible: true }).first(), B4, { group: g, title: 'Billing tab', desc: 'A monthly/yearly billing tab; toggled for the yearly screenshot, left on default.', sel: 'button[role="tab"]' }, { noScroll: true });
  await S('plan-card', q('main .card-surface, [class*="card-surface"]').filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Plan card', desc: 'One plan tier card (the rounded-card surfaces).', sel: '.card-surface' });
  await S('plan-price', q('.card-surface span').filter({ hasText: /\$\d/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan price figure inside a tier card.', sel: '.card-surface span with a $ amount' });
  await S('plan-cta', q('.card-surface a').filter({ hasText: /Get Solo|Get Pro|Get Team|Try|Start/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A tier action; measured never followed or pressed.', sel: 'plan card CTA' });
  await S('feature-row', q('.card-surface button[aria-expanded], section button[aria-expanded]').filter({ visible: true }).first(), B4, { group: g, title: 'Feature row', desc: 'A comparison-table row/accordion.', sel: 'button[aria-expanded]' });
  await S('feature-row-open', q('.card-surface button[aria-expanded], section button[aria-expanded]').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Feature row, open', desc: 'The accordion row after its own toggle.', sel: 'button[aria-expanded]' });
  save();
}

async function toolsPages() {
  if (!(await newPage('script-timer', { url: BASE + '/script-timer', wait: 9000 }))) return;
  await sheetsFor('script-timer');
  const g = G.tools;
  await S('timer-display', q('[class*="timer" i], [role="timer"], time, output').filter({ visible: true }).first(), ['default'], { group: g, title: 'Timer display', desc: 'The script timer readout on the public tool page.', sel: 'timer element' }, { noScroll: true });
  await S('timer-field', q('textarea').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Script field', desc: 'The paste-your-script textarea; filled with sample text and cleared, never submitted.', sel: 'textarea', fillText: 'A hero drags three frames onto the board.' });
  await S('timer-toggle', q('button[aria-pressed]').filter({ visible: true }).first(), B4, { group: g, title: 'Timer toggle', desc: 'An aria-pressed option toggle on the timer.', sel: 'button[aria-pressed]' });
  save();
}

async function prodPages() {
  if (!(await newPage('ai-storyboard', { url: BASE + '/ai-storyboard-generator', wait: 8000 }))) return;
  const g = G.pages;
  await S('page-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product page title', sel: 'h1 on /ai-storyboard-generator' }, { noScroll: true });
  await S('page-cta', q('main a').filter({ hasText: /Try|Start|Free|Generate|Make/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Product page CTA', sel: 'main CTA' });
  save();
}

async function forms() {
  if (!(await newPage('signup', { url: BASE + '/signup', wait: 9000 }))) return;
  const g = G.forms;
  await S('signup-form', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup form', desc: 'The public signup card; fields focused/filled only, never submitted.', sel: 'form' }, { noScroll: true });
  await S('signup-field', q('form input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Signup field', sel: 'form input', fillText: 'name@example.com' }, { noScroll: true });
  await S('signup-submit', q('form button[type="submit"], form button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup submit', desc: 'The form submit; measured at rest, never pressed.', sel: 'form submit' }, { noScroll: true });
  if (!(await newPage('login', { url: BASE + '/login', wait: 7000 }))) { save(); return; }
  await S('login-form', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login form', desc: 'The login card; never used.', sel: 'form' }, { noScroll: true });
  await S('login-field', q('form input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Login field', sel: 'form input on /login' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: link columns, social, legal.', sel: 'footer' }, { noScroll: true });
  const fl = q('footer a').filter({ visible: true }).first();
  await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="twitter"], footer a[href*="x.com"], footer a[href*="linkedin"], footer a[href*="youtube"], footer a[href*="instagram"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', sel: 'footer social link' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('button[aria-label="Open menu"]').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  await S('m-menu-open', menu, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the opened menu shows in the crop.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  await S('m-nav-item', q('[class*="menu" i] a, nav a, header a').filter({ hasText: /./ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened menu overlay.', sel: 'menu overlay a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, 'script-timer': toolsPages, 'ai-storyboard': prodPages, signup: forms, login: () => {}, mobile };
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
