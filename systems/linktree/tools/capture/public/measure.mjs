// Measures linktr.ee's public components in every state reachable without
// signing in, claiming a name, or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing profile login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/.
//
// Consent overlays are hidden, never clicked. Login and register are measured
// as signed-out walls and never submitted. Claim, Select plan, Continue and
// share controls are measured, never pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, PROFILE, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/s/pricing',
  features: '/features',
  about: '/about',
  profile: PROFILE,
  login: 'https://linktr.ee/login',
};
let page, cdp, current, view, context;
const touched = new Set();
const listed = new Map();
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 5000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
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
  const url = URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key];
  const ok = await open(page, url, { wait }).then(() => true, (e) => { log('  !', key, String(e.message || e).split('\n')[0]); return false; });
  if (!ok || await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2).catch(() => {});
  await page.waitForTimeout(200);
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
  await page.waitForTimeout(300);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) throw new Error('forcePseudo: node not found');
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(350);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, view, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, (s.text || '').slice(0, 40));
  } catch (e) {
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url, view: prev.view } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  delete out.components[key].recaptureMissed;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
        await page.waitForTimeout(400);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(350);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'sample', { delay: 12 });
        await page.waitForTimeout(400);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(200); };
        via = `typed "${opts.fillText || 'sample'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        via = via || 'menu held open';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prevSt = out.components[key].states[st];
      out.components[key].states[st] = prevSt && !prevSt.error
        ? { ...prevSt, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const NEVER = /^(send|submit|sign in|log ?in|login|sign up|sign up free|continue|continue with google|continue with apple|claim|claim your linktree|get started for free|select free|select starter|select pro|select premium|select growth|select scale|select enterprise|buy|purchase|pay|checkout|subscribe|share|share profile)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  // The base's guards: a link navigates, so it is refused unless the caller allows it.
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const vis = (loc) => loc.filter({ visible: true });

const G = {
  shell: 'Shell and navigation',
  home: 'Home',
  pricing: 'Pricing',
  profile: 'Public profile',
  login: 'Sign-in wall (not submitted)',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  const g = G.shell;
  await S('navbar', vis(q('nav')).first(), ['default'], { group: g, title: 'Top navigation', desc: 'The marketing nav: Solutions, Features, Integrations, Resources, Pricing, Log in, and the Sign up free pill.', sel: 'nav' }, { noScroll: true });
  await S('nav-link', vis(q('nav a').filter({ hasText: /^Pricing$/ })).first(), B4, { group: g, title: 'Nav link', desc: 'The Pricing text link in the bar. Measured, never followed.', sel: 'nav a "Pricing"' }, { noScroll: true });
  await S('nav-login', vis(q('nav a').filter({ hasText: /^Log in$/ })).first(), B4, { group: g, title: 'Log in link', desc: 'The quiet Log in link. Measured, never followed. The login wall itself is a separate signed-out page.', sel: 'nav a "Log in"' }, { noScroll: true });
  await S('nav-signup', vis(q('nav a').filter({ hasText: /Sign up free/i })).first(), B4, { group: g, title: 'Sign up free pill', desc: 'The ink pill in the bar. Measured, never followed.', sel: 'nav a "Sign up free"' }, { noScroll: true });
  await S('nav-menu', vis(q('nav button').filter({ hasText: /^Solutions$/ })).first(), B4, { group: g, title: 'Nav menu button', desc: 'The Solutions disclosure. Opened only to record the menu panel; nothing inside was followed.', sel: 'nav button "Solutions"' }, { noScroll: true });
  await S('nav-menu-panel', q('nav a').filter({ hasText: /^Musicians$/ }).first(), ['opened'], {
    group: g, title: 'Nav menu item', desc: 'A Solutions menu item, captured after the disclosure is opened. The item has no box until the menu opens. Measured, never followed.', sel: 'nav a "Musicians"',
  }, {
    noScroll: true,
    open: async () => { await toggle(q('nav button').filter({ hasText: /^Solutions$/ }).first()); await page.waitForTimeout(600); },
  });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: '"A link in bio built for you." in Linksans.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', vis(q('a, button').filter({ hasText: /Get started for free/i })).first(), B4, { group: h, title: 'Get started for free', desc: 'The hero claim CTA. Measured, never followed and never submitted.', sel: 'a/button "Get started for free"' });
  await page.evaluate(() => {
    const inputs = [...document.querySelectorAll('input')].filter((i) => /linktr\.ee/i.test(i.placeholder || ''));
    const i = inputs.find((el) => { const r = el.getBoundingClientRect(); return r.width > 40 && r.y > 80 && r.y < 900; }) || inputs[0];
    if (!i) return;
    i.setAttribute('data-m-claim', '1');
    let n = i;
    for (let k = 0; n && k < 6; n = n.parentElement, k++) {
      const r = n.getBoundingClientRect();
      const c = getComputedStyle(n);
      if (r.height > 40 && r.height < 120 && (parseFloat(c.borderTopLeftRadius) > 8 || c.backgroundColor !== 'rgba(0, 0, 0, 0)')) {
        n.setAttribute('data-m-claimwrap', '1');
        break;
      }
    }
  });
  await S('claim-field', q('[data-m-claim="1"]'), ['default', 'focused', 'filled'], { group: h, title: 'Claim username field', desc: 'The linktr.ee/yourname field on the marketing page. A throwaway string was typed and deleted. The form was not submitted.', sel: 'input[placeholder*="linktr.ee"]' }, { fillText: 'sample' });
  await S('claim-wrap', q('[data-m-claimwrap="1"]'), ['default'], { group: h, title: 'Claim field shell', desc: 'The painted shell around the claim field.', sel: 'marked claim shell' });
  await S('claim-submit', vis(q('button').filter({ hasText: /Claim your Linktree/i })).first(), B4, { group: h, title: 'Claim your Linktree', desc: 'The claim button beside the field. Measured, never pressed for real.', sel: 'button "Claim your Linktree"' });
  await S('footer', q('footer').first(), ['default'], { group: h, title: 'Footer', desc: 'The purple footer band with the claim field repeated and the product columns.', sel: 'footer' }, { crop: false });
  await S('footer-link', vis(q('footer a').filter({ hasText: /^About$/ })).first(), B4, { group: h, title: 'Footer link', desc: 'A company-column link. Measured, never followed.', sel: 'footer a "About"' });
  save();
  await page.context().close();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  await S('plan-card', vis(q('h3').filter({ hasText: /^Pro$/ })).first(), ['default'], { group: g, title: 'Plan name', desc: 'The Pro plan heading on the public pricing page. Selecting a plan was never clicked.', sel: 'h3 "Pro"' });
  await S('plan-select', vis(q('a').filter({ hasText: /^Try free for 7 days$/ })).first(), B4, { group: g, title: 'Try free for 7 days', desc: 'The Pro plan link. Measured, never followed. Checkout was not opened.', sel: 'a "Try free for 7 days"' });
  await S('plan-free', vis(q('a').filter({ hasText: /^Get started$/ })).first(), ['default', 'hover'], { group: g, title: 'Get started', desc: 'The free-plan link on the pricing page. Measured, never followed.', sel: 'a "Get started"' });
  save();
  await page.context().close();
}

async function profile() {
  if (!(await newPage('profile', { wait: 6500 }))) return;
  const g = G.profile;
  await S('profile-title', q('h1').first(), ['default'], { group: g, title: 'Profile name', desc: 'The public Linktree profile title (the official linktr.ee page).', sel: 'h1' }, { noScroll: true });
  await S('profile-share', vis(q('button[aria-label="Share profile"]')).first(), B4, { group: g, title: 'Share profile', desc: 'The share icon button on a public profile. Its name is an aria-label. Measured, never pressed, so no share sheet was sent.', sel: 'button[aria-label="Share profile"]' }, { noScroll: true });
  await S('profile-tab', vis(q('button').filter({ hasText: /^Links$/ })).first(), B4, { group: g, title: 'Profile tab', desc: 'The Links tab on the public profile.', sel: 'button "Links"' }, { noScroll: true });
  await S('profile-tab-shop', vis(q('button').filter({ hasText: /^Shop$/ })).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Shop tab', desc: 'The unselected Shop tab. Not selected, so the page content was not swapped.', sel: 'button "Shop"' }, { noScroll: true });
  await S('profile-social', vis(q('button').filter({ hasText: /Instagram$/ })).first(), ['default', 'hover'], { group: g, title: 'Social icon button', desc: 'A social icon on the public profile. Measured, never followed.', sel: 'button "Linktree Instagram"' }, { noScroll: true });
  await S('profile-link', vis(q('a').filter({ hasText: /boost your credibility|YouTube Tools|Podcasts/i })).first(), ['default', 'hover'], { group: g, title: 'Profile link card', desc: 'A published link card on the official profile. Measured, never followed.', sel: 'profile link card' });
  await S('profile-badge', vis(q('button').filter({ hasText: /^Verified$/ })).first(), ['default'], { group: g, title: 'Verified badge', desc: 'The verified badge on the official profile.', sel: 'button "Verified"' }, { noScroll: true });
  save();
  await page.context().close();
}

async function login() {
  if (!(await newPage('login', { wait: 5000 }))) return;
  const g = G.login;
  await S('login-title', q('h1').first(), ['default'], { group: g, title: 'Login title', desc: 'The signed-out login wall. Nothing was submitted.', sel: 'h1' }, { noScroll: true });
  await S('login-field', vis(q('input[name="username"], input[type="text"], input[type="email"]')).first(), ['default', 'focused'], { group: g, title: 'Login field', desc: 'The email or username field. Focused only. Nothing was typed and the form was not submitted.', sel: 'input username' }, { noScroll: true });
  await S('login-continue', vis(q('button').filter({ hasText: /^Continue$/ })).first(), B4, { group: g, title: 'Continue', desc: 'The primary continue button. Measured, never pressed.', sel: 'button "Continue"' }, { noScroll: true });
  await S('login-google', vis(q('button').filter({ hasText: /Continue with Google/i })).first(), ['default', 'hover'], { group: g, title: 'Continue with Google', desc: 'The Google button on the signed-out wall. Measured, never pressed.', sel: 'button "Continue with Google"' }, { noScroll: true });
  await S('login-signup', vis(q('a, button').filter({ hasText: /^Sign up$/ })).first(), ['default', 'hover'], { group: g, title: 'Sign up link', desc: 'The sign-up link on the login wall. Measured, never followed.', sel: 'Sign up' }, { noScroll: true });
  save();
  await page.context().close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-navbar', vis(q('nav')).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The marketing nav at 390 wide, with the menu toggle.', sel: 'nav' }, { noScroll: true });
  await S('m-menu', vis(q('button[aria-label="Toggle menu"]')).first(), B4, { group: g, title: 'Menu toggle', desc: 'The mobile menu button. Its name is an aria-label. Opened once for the menu link.', sel: 'button[aria-label="Toggle menu"]' }, { noScroll: true });
  await S('m-signup', vis(q('a, button').filter({ hasText: /Sign up free|Get started for free/i })).first(), ['default'], { group: g, title: 'Mobile signup', desc: 'The signup control at 390 wide. Measured, never followed.', sel: 'signup' }, { noScroll: true });
  await S('m-menu-panel', vis(q('a').filter({ hasText: /^Pricing$/ })).first(), ['opened'], {
    group: g, title: 'Mobile menu link', desc: 'A link inside the opened mobile menu. Measured, never followed.', sel: 'a "Pricing"',
  }, {
    noScroll: true,
    open: async () => { await toggle(q('button[aria-label="Toggle menu"]').first()); await page.waitForTimeout(600); },
  });
  save();
  await page.context().close();
}

const run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, profile, login, mobile };
try {
  for (const k of Object.keys(plan)) {
    if (pages.length && !pages.includes(k)) continue;
    await plan[k]();
  }
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has((c.page || '') + '|' + cview)) delete out.components[key];
    }
  }
  // The same for states (the kit's stale-state prune): a state an earlier run
  // recorded that this run's spec no longer lists goes.
  for (const [key, c] of Object.entries(out.components)) {
    if (pages.length || !touched.has(key) || !listed.has(key)) continue;
    for (const st of Object.keys(c.states || {})) if (!listed.get(key).has(st)) { delete c.states[st]; log('dropped stale state', key, st); }
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
