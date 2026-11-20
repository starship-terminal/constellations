// Measures mailchimp.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing features about login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// mailchimp.com is a light-only marketing site signed out. The Plums/CXP
// sheets declare yellow CTAs, caviar ink, Tally / Graphik Web and Means Web.
// login.mailchimp.com is a separate signed-out card (Graphik Web) that does
// not share this layer; its values are measured, never submitted. Signup,
// the campaign builder and the account sit behind sign-in and are recorded
// as boundaries, not captured. Specs select by class, role, aria-label, id
// or text. Nothing is sent, bought or signed into. OneTrust and the home
// survey modal are hidden, never answered and never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, SIGNUP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { startRun, markRead } from './dates.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/marketing/', features: '/features/', about: '/about/', login: LOGIN_URL, mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
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
  // open() throws on a failed navigation or a challenge that never clears; treat it like BLOCKED, so
  // the page's committed readings are kept rather than replaced with the interstitial.
  const opened = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo })
    .then(() => true, (e) => { log('  OPEN FAILED', key, String(e.message).slice(0, 100)); return false; });
  if (!opened) { failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  // `run` is left as it was: markRead() moves it when a state is actually read.
  Object.assign(c, { page: current, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    markRead(out, c, state, { ...s, crop: file, via: opts.via }, run);
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message).slice(0, 200) };
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle, then left selected'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|start free trial|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|generate|generate.*|sign up|create an account|customize my experience|connect)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

async function paintedCard(loc, { minR = 8, maxW = 900 } = {}) {
  const ok = await loc.filter({ visible: true }).first().evaluate((el, { minR, maxW }) => {
    document.querySelectorAll('[data-m-card]').forEach((n) => n.removeAttribute('data-m-card'));
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && parseFloat(cs.borderTopLeftRadius) >= minR && r.width > 240 && r.width <= maxW && r.height > 120) {
        n.setAttribute('data-m-card', '1');
        return true;
      }
    }
    return false;
  }, { minR, maxW }).catch(() => false);
  return ok ? page.locator('[data-m-card="1"]') : page.locator('[data-m-card="__none__"]');
}

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
    return transitions.slice(0, 40);
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(4000);
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
  shell: 'Site chrome', promo: 'Announcement bar', home: 'Home',
  pricing: 'Pricing', features: 'Features', about: 'About',
  login: 'App log-in', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

async function openNav(name) {
  const btn = q('button.iaNav__cta[aria-haspopup]').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no ' + name + ' trigger';
  for (let i = 0; i < 3; i++) {
    const open = await btn.getAttribute('aria-expanded').catch(() => null);
    if (open === 'true') return 'clicked the "' + name + '" nav button to open its panel';
    await toggle(btn);
    await page.waitForTimeout(700);
  }
  return 'activated the "' + name + '" button; no panel reported open';
}

async function openMobileMenu() {
  const b = q('button.iaNav__menuOpen, button[aria-label="Main Menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = await b.getAttribute('aria-expanded').catch(() => null);
  if (open === 'true') return 'the mobile menu was already open';
  await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
  await page.waitForTimeout(800);
  return 'clicked Main Menu';
}

async function home() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  let g = G.promo;
  await S('announce-bar', q('a').filter({ hasText: /Start today/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Announcement link', desc: 'The trial announcement link above the nav ("Start today"). Measured, never followed. It points at pricing, not a signup submit.', sel: 'announcement Start today' }, { noScroll: true });
  g = G.shell;
  await S('site-nav', q('header.iaGlobalNav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site nav', desc: 'The header (header.iaGlobalNav): wordmark, Industries and Solutions / Integrations / Resources menus, Pricing, Search, Log In, and the yellow Start Free Trial pill. The announcement strip above it is a separate aside.', sel: 'header.iaGlobalNav' }, { noScroll: true });
  await S('nav-logo', q('a[aria-label="Mailchimp Home"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The Mailchimp wordmark linking home.', sel: 'a[aria-label=Mailchimp Home]' }, { noScroll: true });
  await S('nav-menu', q('button.iaNav__cta[aria-haspopup]').filter({ hasText: /^Resources$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Nav menu button', desc: 'The Resources button (aria-haspopup) that opens the mega menu. The opened state was measured after clicking it. Menu links were never followed.', sel: 'button.iaNav__cta Resources' }, { noScroll: true });
  await S('nav-panel', q('section.iaNav__panel.expanded').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav menu panel', desc: 'The panel opened by Resources (section.iaNav__panel.expanded). Its links were never followed.', sel: 'section.iaNav__panel.expanded' }, { open: () => openNav('Resources'), noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-link', q('a.iaNav__cta[href="/pricing/marketing/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The Pricing link in the nav. Measured, never followed.', sel: 'a.iaNav__cta[href=/pricing/marketing/]' }, { noScroll: true });
  await S('nav-login', q('a.ctaSecondary').filter({ hasText: /^Log In$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log In', desc: 'The outlined Log In pill. It points at login.mailchimp.com. Measured, never followed.', sel: 'a.ctaSecondary Log In' }, { noScroll: true });
  await S('nav-trial', q('a.ctaPrimary').filter({ hasText: /Start Free Trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Start Free Trial', desc: 'The yellow Start Free Trial pill. Measured, never followed. Signup was not started.', sel: 'a.ctaPrimary Start Free Trial' }, { noScroll: true });
  g = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline', desc: 'The home masthead, set in Means Web on the dark hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a.ctaPrimary[aria-label="Start Free Trial"]').filter({ visible: true }).first(), B4, { group: g, title: 'Hero CTA', desc: 'The hero Start Free Trial button. It points at pricing. Measured, never followed.', sel: 'a.ctaPrimary[aria-label=Start Free Trial]' });
  await S('hero-secondary', q('a.ctaArrow').filter({ hasText: /See all demos/i }).filter({ visible: true }).first(), B4, { group: g, title: 'See all demos', desc: 'The hero secondary link under the photo band. Measured, never followed.', sel: 'a.ctaArrow See all demos' });
  g = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The page footer: sitemap columns and legal links.', sel: 'footer' });
  await S('footer-link', q('footer a.cta[href="/why-mailchimp/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer sitemap link. Measured, never followed.', sel: 'footer a.cta[href=/why-mailchimp/]' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 5000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-plan', q('.singlePlan__planCardCell').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'The Standard plan card on /pricing/marketing/. The trial link was measured, never followed. Checkout was not started.', sel: '.singlePlan__planCardCell' });
  await S('price-cta', q('.singlePlan__planCardCell a.ctaBuyNow').filter({ hasText: /Start Free Trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan trial button', desc: 'The Standard plan Start Free Trial link. It points at /signup/ with a plan query. Measured, never followed. Signup was not started and checkout was not started.', sel: '.singlePlan__planCardCell a.ctaBuyNow' });
  await S('price-select', q('select[name="Number of Contacts"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contacts select', desc: 'The contacts-count select on the pricing page. Measured at rest. The value was not changed and nothing was submitted.', sel: 'select[name=Number of Contacts]' });
  await S('price-radio', q('input.av-radio').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan radio', desc: 'A trial-or-discount radio on a plan card. Measured at rest, never changed.', sel: 'input.av-radio' });
  save();
}

async function features() {
  if (!(await newPage('features', { wait: 5000 }))) return;
  await sheetsFor('features');
  const g = G.features;
  await S('feat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Features headline', desc: 'The /features/ masthead.', sel: 'h1' }, { noScroll: true });
  save();
}

async function about() {
  if (!(await newPage('about', { wait: 5000 }))) return;
  const g = G.about;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: 'The /about/ masthead. A public page that loads signed out.', sel: 'h1' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 6000, url: LOGIN_URL }))) return;
  await sheetsFor('login');
  const g = G.login;
  await S('login-panel', q('#unified-login-form, form.c-largeForm').filter({ visible: true }).first(), ['default'], { group: g, title: 'Log-in card', desc: 'The signed-out log-in card on login.mailchimp.com. A separate app from the marketing site. Nothing was submitted. Sign-in was not started.', sel: '#unified-login-form' }, { noScroll: true });
  await S('login-username', q('#username, input[name="username"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Username field', desc: 'The Username or Email field. Focused and typed into with a placeholder, then cleared. Nothing was submitted.', sel: '#username' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-submit', q('button[type="submit"], input[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Log in submit', desc: 'The Log in submit. States were measured. The button was never clicked. Sign-in was not started.', sel: 'login submit' }, { noScroll: true });
  await S('login-forgot', q('a[href*="forgot"], a').filter({ hasText: /Forgot username|Forgot password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot username', desc: 'A forgot-username or forgot-password link. Measured, never followed.', sel: 'forgot link' }, { noScroll: true });
  await S('login-create', q('a[href*="signup"]').filter({ hasText: /Create an account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create an account', desc: 'The Create an account link. Signup was not started and was not followed.', sel: 'Create an account' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, wait: 5000, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-nav', q('.iaNav, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The phone nav bar.', sel: 'mobile .iaNav' }, { noScroll: true });
  await S('m-menu', q('button.iaNav__menuOpen, button[aria-label="Main Menu"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The Main Menu button. Opened locally. Links were never followed.', sel: 'button.iaNav__menuOpen' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero', desc: 'The home masthead at 390 wide.', sel: 'mobile h1' });
  save();
}

run = process.env.CAPTURE_DATE || new Date().toISOString().slice(0, 10);
// _meta.read keeps the earlier date until a state is read (markRead); lastAttempt is this run.
startRun(out, run);
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); mailchimp.com paints light only; login.mailchimp.com is a separate signed-out card';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, features, about, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a.iaNav__cta[href="/pricing/marketing/"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');


