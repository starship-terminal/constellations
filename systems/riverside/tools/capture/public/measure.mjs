// Measures riverside.com's public components in every state reachable without
// signing in, uploading, purchasing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing faq blog login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// riverside.com is a Webflow build in one light theme. Login and Start for
// Free are measured, never followed. Forms are focused, never submitted.
// Cookie dialogs are hidden, never answered. Google and Apple are never clicked.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', faq: '/faq', blog: '/blog', login: '/login' };
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

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
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
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
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
        if (!opts.fillText) throw new Error('filled state skipped: no sample text configured, and nothing is typed into a live field');
        await page.keyboard.type(opts.fillText, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = 'typed the configured sample, then deleted; nothing sent';
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

// Clicks a UI toggle (accordion, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|choose|talk to sales|contact us|play|launch video|explore|install|connect|try|view demo plans)$/i;
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
  shell: 'Shell and navigation', hero: 'Home', pricing: 'Pricing',
  faq: 'FAQ', blog: 'Blog', login: 'Login wall', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  const nav = q('.w-nav').first();
  await S('header', nav, ['default'], { group: g, title: 'Header', desc: 'The Webflow top bar: logo, Platform, Solutions, Resources, For Business, Pricing, Login, Start for Free.', sel: '.w-nav' }, { noScroll: true });
  await S('logo', q('a.c-updated-nav-logo, a.w-nav-brand').first(), ['default'], { group: g, title: 'Logo', sel: 'a.w-nav-brand' }, { noScroll: true });
  await S('nav-dropdown', q('.nav-dropdown-toggle--updated').filter({ hasText: /^Platform$/ }).first(), B4, { group: g, title: 'Nav dropdown', desc: 'Platform toggle. Opens a menu already in the DOM. Measured, then closed.', sel: '.nav-dropdown-toggle--updated' }, { noScroll: true });
  await S('nav-menu', q('.nav-dropdown-toggle--updated').filter({ hasText: /^Platform$/ }).first(), ['opened'], { group: g, title: 'Platform menu', desc: 'The opened Platform dropdown. Crop is the list.', sel: '.w-dropdown-list' }, { noScroll: true, cropLoc: q('.w-dropdown-list').filter({ visible: true }).first() });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.click(700, 600).catch(() => {});
  await page.waitForTimeout(300);
  await S('nav-link', q('a.c-nav-link').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', sel: 'a.c-nav-link' }, { noScroll: true });
  await S('nav-login', q('a.c-nav-link--login, a').filter({ hasText: /^Login$/ }).first(), B4, { group: g, title: 'Login link', desc: 'Header Login. Measured, never followed. It opens the studio wall.', sel: 'a.c-nav-link--login' }, { noScroll: true });
  await S('nav-cta', q('a.c-updated-nav-button').filter({ hasText: /Start for Free/ }).first(), B4, { group: g, title: 'Start for Free', desc: 'Header CTA. Measured, never followed. It opens the register wall.', sel: 'a.c-updated-nav-button' }, { noScroll: true });

  const h = G.hero;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a.main-button').filter({ hasText: /Start for Free/ }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero Start for Free. Measured, never followed.', sel: 'a.main-button' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 5000 }))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  const tab = q('[role="tab"], .w-tab-link').filter({ hasText: /^Pro$/ }).first();
  await S('plan-tab', tab, ['default', 'hover', 'focus-visible', 'selected'], { group: g, title: 'Plan tab', desc: 'The Pro pricing tab. A local UI state. Checkout was never opened.', sel: '[role=tab] Pro' });
  const card = q('.w-tab-pane, [class*="pricing"], [class*="plan"]').filter({ visible: true }).first();
  if (await card.count()) await S('plan-card', card, ['default'], { group: g, title: 'Plan panel', sel: 'pricing panel' });
  save();
}

async function faq() {
  if (!(await newPage('faq', { wait: 4500 }))) return;
  const g = G.faq;
  await S('faq-title', q('h1').first(), ['default'], { group: g, title: 'FAQ title', sel: 'h1' }, { noScroll: true });
  const item = q('summary, .faq-question, [class*="accordion"] [role="button"], .w-dropdown-toggle').filter({ visible: true });
  let target = null;
  const n = await item.count();
  for (let i = 0; i < Math.min(n, 16); i++) {
    const text = ((await item.nth(i).innerText().catch(() => '')) || '').trim();
    if (text.length > 16 && text.length < 180 && !/cookie|platform|english/i.test(text)) { target = item.nth(i); break; }
  }
  if (target) {
    await S('faq-question', target, B4, { group: g, title: 'FAQ question', sel: 'faq toggle' });
    await S('faq-open', target, ['opened'], { group: g, title: 'FAQ question, open', desc: 'The same question after its own toggle.', sel: 'faq toggle' });
  }
  save();
}

async function blog() {
  if (!(await newPage('blog', { wait: 4500 }))) return;
  const g = G.blog;
  await S('blog-title', q('h1').first(), ['default'], { group: g, title: 'Blog title', sel: 'h1' }, { noScroll: true });
  const card = q('a').filter({ hasText: /How to/ }).first();
  if (await card.count()) await S('blog-card', card, ['default', 'hover'], { group: g, title: 'Blog card', desc: 'A published post card. Measured, never followed in this pass.', sel: 'a blog card' });
  const email = q('input[type="email"]').first();
  if (await email.count()) await S('newsletter-field', email, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only. Nothing typed. Nothing submitted.', sel: 'input[type=email]' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 4000 }))) return;
  const g = G.login;
  await S('login-title', q('h1').first(), ['default'], { group: g, title: 'Login title', sel: 'h1' }, { noScroll: true });
  const email = q('input[type="email"], input[name="email"], input[autocomplete="username"]').first();
  if (await email.count()) await S('login-email', email, ['default', 'focused'], { group: g, title: 'Login email', desc: 'Focused only. Nothing typed. Nothing submitted.', sel: 'login email' });
  const pass = q('input[type="password"]').first();
  if (await pass.count()) await S('login-password', pass, ['default', 'focused'], { group: g, title: 'Login password', desc: 'Focused only. Nothing typed. Nothing submitted.', sel: 'input[type=password]' });
  const sso = q('button, a').filter({ hasText: /Google|Apple|SSO/ }).first();
  if (await sso.count()) await S('login-sso', sso, ['default'], { group: g, title: 'SSO button', desc: 'Visible on the wall. Never clicked.', sel: 'SSO' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  const g = G.footer;
  const legal = q('a').filter({ hasText: /^Privacy$/ }).first();
  if (await legal.count()) {
    await S('footer-link', legal, B4, { group: g, title: 'Footer legal link', sel: 'a Privacy' });
  }
  const social = q('a[aria-label*="Facebook" i], a[aria-label*="Youtube" i], a[href*="youtube.com"]').first();
  if (await social.count()) await S('footer-social', social, ['default', 'hover'], { group: g, title: 'Footer social icon', sel: 'social link' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 5000 }))) return;
  const g = G.mobile;
  await S('m-header', q('.w-nav').first(), ['default'], { group: g, title: 'Mobile header', sel: '.w-nav' }, { noScroll: true });
  const menuBtn = q('.w-nav-button').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The hamburger after its own toggle.', sel: '.w-nav-button' }, { noScroll: true, cropLoc: q('.w-nav-menu').filter({ visible: true }).first() });
  const mLink = q('a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'Read inside the open menu.', sel: 'a Pricing' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, faq, blog, login, mobile };
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
