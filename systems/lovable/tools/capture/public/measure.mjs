// Measures lovable.dev public components without signing in or submitting.
//
//   PLAYWRIGHT=... node measure.mjs [home|pricing|login|docs|mobile]
import fs from 'node:fs';
import path from 'node:path';
import { BASE, DOCS, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= { product: 'lovable', captured: new Date().toISOString().slice(0, 10) };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  pricing: BASE + '/pricing',
  login: BASE + '/login',
  docs: DOCS + '/introduction/welcome',
  'enterprise-form': BASE + '/enterprise-form',
};

let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
const opened = new Set();
run = new Date().toISOString().slice(0, 10);

async function newPage(key, { mobile = false, wait = 3500 } = {}) {
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
  const cleared = await open(page, URLS[key], { wait }).catch((e) => { log('  open failed', key, String(e.message || e).slice(0, 120)); return false; });
  const blocked = !cleared || await page.evaluate(() => /just a moment|verify you are human/i.test(document.title + (document.body.innerText || '').slice(0, 200))).catch(() => true);
  if (blocked) { log('  BLOCKED', key); sectionBlocked = true; await page.close(); await ctx.close(); return false; }
  opened.add(key);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  context._pageCtx = ctx;
  return true;
}

async function endPage() {
  await page.close().catch(() => {});
  if (context._pageCtx) await context._pageCtx.close().catch(() => {});
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(180);
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
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(280);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(280);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

let currentSection = null;   // the measure section (home, mobile, ...) that owns a component
let sectionBlocked = false;  // a page of the current section was blocked or failed to open

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, section: currentSection, run, url: URLS[current] }, meta);
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
      try { file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

const NEVER = /^(send|submit|sign in|log in|login|sign up|get started|continue|continue with google|continue with github|continue with apple|book a demo|start building|start building for free|create your account)$/i;

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    out.components[key].missing = true;
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.focus()));
        await page.waitForTimeout(300);
        via = 'clicked into the field; nothing submitted';
      } else if (st === 'filled') {
        await loc.click({ timeout: 4000 });
        await page.keyboard.type('name@example.com', { delay: 8 });
        await page.waitForTimeout(250);
        undo = async () => {
          await loc.focus();
          await page.keyboard.press('ControlOrMeta+a');
          await page.keyboard.press('Backspace');
        };
        via = 'typed a sample address, then deleted; nothing submitted';
      } else if (st === 'opened' || st === 'expanded') {
        const t = await loc.evaluate((el) => (el.innerText || el.getAttribute('aria-label') || '').trim());
        if (NEVER.test(t)) throw new Error('toggle refused: ' + t);
        await loc.click({ timeout: 4000 });
        await page.waitForTimeout(600);
        via = 'own toggle; nothing submitted';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st]().catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const G = {
  shell: 'Shell and navigation',
  home: 'Home',
  pricing: 'Pricing',
  login: 'Log in',
  docs: 'Docs',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The marketing bar: wordmark, Solutions and Resources menus, Community, Enterprise, Pricing, Security, Log in and Get started.', sel: 'header' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-menu', q('header button').filter({ hasText: /^Solutions$/ }).first(), B4, { group: g, title: 'Solutions menu button', sel: 'header button Solutions' }, { noScroll: true });
  await S('nav-menu-open', q('header button').filter({ hasText: /^Solutions$/ }).first(), ['opened'], { group: g, title: 'Solutions menu, open', desc: 'The Solutions button after its own press. The menu is local; no destination was followed.', sel: 'header button Solutions' }, { noScroll: true, after: { opened: async () => { await page.keyboard.press('Escape'); } } });
  await S('nav-login', q('header a').filter({ hasText: /^Log in$/ }).first(), B4, { group: g, title: 'Log in pill', desc: 'The white pill in the header. Measured, never followed.', sel: 'header a Log in' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /^Get started$/ }).first(), B4, { group: g, title: 'Get started pill', desc: 'The inverse pill in the header. Measured, never followed. Following it would open the sign-up page.', sel: 'header a Get started' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: 'The first heading on the home page, Camera Plain Variable.', sel: 'h1' }, { noScroll: true });
  await S('prompt-field', q('[role="textbox"]').first(), ['default', 'focused'], { group: h, title: 'Prompt field', desc: 'The home composer. Focused only. Nothing was typed into a send path and nothing was submitted.', sel: '[role=textbox]' }, { noScroll: true });
  await S('prompt-build', q('button').filter({ hasText: /^Build$/ }).first(), B4, { group: g, title: 'Build mode chip', desc: 'The Build chip under the composer. Measured, never used to start a build.', sel: 'button Build' }, { noScroll: true });
  await S('icon-button', q('button[aria-label="Additional actions"]').first(), B4, { group: h, title: 'Additional actions', desc: 'The icon button beside the composer. Its menu was not opened.', sel: 'button[aria-label=Additional actions]' }, { noScroll: true });
  save();
  await endPage();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  await S('billing-monthly', q('button').filter({ hasText: /^Monthly$/ }).first(), B4, { group: g, title: 'Monthly segment', sel: 'button Monthly' }, { noScroll: true });
  await S('billing-yearly', q('button').filter({ hasText: /^Yearly/ }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Yearly segment', desc: 'The unselected Yearly segment. Switching it is a local toggle, not a purchase.', sel: 'button Yearly' }, { noScroll: true });
  await S('plan-cta', q('a').filter({ hasText: /^Get started$/ }).nth(1), B4, { group: g, title: 'Plan CTA', desc: 'A plan card Get started link. Measured, never followed. Following it would open sign-up.', sel: 'a Get started in a plan card' });
  await S('credit-select', q('[role="combobox"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Credit amount select', desc: 'The credit-tier combobox on a paid plan. Its list was not opened, so no checkout started.', sel: '[role=combobox]' });
  await S('faq-item', q('button').filter({ hasText: /What is a credit/ }).first(), ['default', 'hover', 'focus-visible', 'expanded'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ row. Expanded locally.', sel: 'button What is a credit' });
  save();
  await endPage();
}

async function login() {
  if (!(await newPage('login'))) return;
  const g = G.login;
  await S('login-title', q('h1').first(), ['default'], { group: g, title: 'Log in title', sel: 'h1' }, { noScroll: true });
  await S('oauth-google', q('button').filter({ hasText: /Continue with Google/ }).first(), B4, { group: g, title: 'Continue with Google', desc: 'OAuth button. Measured, never pressed. Pressing it would start a sign-in.', sel: 'button Continue with Google' });
  await S('oauth-github', q('button').filter({ hasText: /Continue with GitHub/ }).first(), ['default'], { group: g, title: 'Continue with GitHub', desc: 'OAuth button. Measured at rest, never pressed.', sel: 'button Continue with GitHub' });
  await S('login-field', q('input[type="email"], input[name="email"], input[placeholder*="mail" i], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The log-in email field. Sample text was typed and deleted. Continue was never pressed, so no sign-in was submitted.', sel: 'email input' });
  await S('login-continue', q('button').filter({ hasText: /^Continue$/ }).first(), B4, { group: g, title: 'Continue', desc: 'The email continue button. Measured, never pressed. Pressing it would submit a sign-in.', sel: 'button Continue' });
  await S('login-signup-link', q('a').filter({ hasText: /Create your account/ }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Create your account link', desc: 'The link to sign-up. Measured, never followed.', sel: 'a Create your account' });
  save();
  await endPage();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  const g = G.docs;
  await S('docs-title', q('h1').first(), ['default'], { group: g, title: 'Docs title', sel: 'h1' }, { noScroll: true });
  await S('docs-search', q('button').filter({ hasText: /Search/ }).first(), B4, { group: g, title: 'Search button', desc: 'The docs search trigger. Its dialog was opened in the page capture, not submitted.', sel: 'button Search' }, { noScroll: true });
  await S('docs-nav', q('a').filter({ hasText: /^Welcome to Lovable$/ }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Docs nav row', desc: 'The current sidebar row.', sel: 'a Welcome to Lovable' }, { noScroll: true });
  await S('docs-cta', q('a').filter({ hasText: /Start building for free/ }).first(), B4, { group: g, title: 'Start building for free', desc: 'The docs header CTA. Measured, never followed. Following it would open sign-up.', sel: 'a Start building for free' }, { noScroll: true });
  await S('docs-theme', q('button[aria-label="Change theme preference"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Theme preference', desc: 'The docs theme control. Its menu was not used to change the account, and the page was left on the theme it loaded in.', sel: 'button Change theme preference' }, { noScroll: true });
  save();
  await endPage();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menu = q('button').filter({ hasText: /Navigation menu|Menu/ }).first();
  await S('m-menu', menu, ['default', 'pressed', 'opened'], { group: g, title: 'Mobile menu button', desc: 'The phone nav button. Opened locally.', sel: 'button Navigation menu' }, { noScroll: true });
  save();
  await endPage();
}

const arg = (process.argv[2] || 'all').split(',').filter(Boolean);
const { browser, context: root } = await launch();
context = root;
const want = (k) => arg.includes('all') || arg.includes(k);
// Sections that ran to the end with every page opened. A component is pruned only when the section that owns it (c.section)
// finished this run and did not measure it again: a section that was not selected or failed part-way
// keeps its earlier readings, and home and mobile, which share the home page, prune only their own
// (the kit's prune, restored in the 2026-11 audit). A reading saved before c.section existed is kept.
const finishedSections = new Set();
async function section(name, fn) {
  currentSection = name;
  sectionBlocked = false;
  await fn();
  // A section whose page never opened returns early without measuring; it is not finished, so its
  // saved readings stay.
  if (!sectionBlocked) finishedSections.add(name);
}
try {
  if (want('home')) await section('home', home);
  if (want('pricing')) await section('pricing', pricing);
  if (want('login')) await section('login', login);
  if (want('docs')) await section('docs', docs);
  if (want('mobile')) await section('mobile', mobile);
} finally {
  for (const [key, c] of Object.entries(out.components)) if (finishedSections.has(c.section) && !touched.has(key)) { delete out.components[key]; log('dropped stale', key); }
  for (const [key, c] of Object.entries(out.components)) {
    if (!finishedSections.has(c.section) || !listed.has(key)) continue;
    for (const st of Object.keys(c.states || {})) if (!listed.get(key).has(st)) { delete c.states[st]; log('dropped stale state', key, st); }
  }
  save();
  await browser.close();
}
log('components', Object.keys(out.components).length);
