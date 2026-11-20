// Measures fibery.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing templates signup login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fibery.com is a light-only marketing site signed out (Next.js, CSS
// modules: HeaderMain_*, FiberyButton_*, PricingPlans_*). There is no theme
// toggle and no dark surface. fibery.io/sign-up and fibery.io/login/ are
// the public workspace-creation wizard and sign-in, on the same stylesheets.
// Specs select by CSS-module class stems, role, aria-label or text. Nothing
// is sent, bought or signed into: the only presses are local UI toggles —
// the header's Solutions/Platform/Support dropdown triggers, the pricing
// Monthly/Yearly switch, the mobile sandwich button and the login page's
// "Continue with Email" step reveal. The sign-up prompt field is typed into
// and cleared, never submitted; the OAuth POST forms and every submit are
// measured, never pressed; every link is measured, never followed. The
// cookie consent popup and Intercom widget are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, SIGNUP_URL, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', templates: '/templates', signup: SIGNUP_URL, login: LOGIN_URL, mobile: '/' };
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
      } else if (st === 'toggled') {
        via = await opts.before?.toggled ? 'see via' : 'toggled';
        const ctl = (opts.toggleLoc || loc).filter({ visible: true }).first();
        await ctl.click({ timeout: 4000 }).catch(() => ctl.evaluate((el) => el.click()));
        await page.waitForTimeout(900);
        via = 'clicked the label/switch — a local UI toggle; prices flip, nothing is sent';
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
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|create workspace|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|sign up|sign up for free|book a demo|start without ai)$/i;
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
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', templates: 'Templates',
  signup: 'Sign-up wizard (fibery.io)', login: 'Login (fibery.io)',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens a header dropdown: the Solutions/Platform/Support menu items are
// HeaderMenuItem_expandMenu triggers whose HeaderMenuDropdown panel opens on
// hover — a local UI toggle, never a link. The panel stays open so it and one
// item can be measured; the pointer then moves away.
async function openMenu(name) {
  const item = page.locator(M('HeaderMenuItem_root')).filter({ hasText: new RegExp(`^\\s*${name}`) }).first();
  if (!(await item.count())) return `no ${name} menu item`;
  const open = async () => page.evaluate(() => {
    const d = [...document.querySelectorAll('[class*="HeaderMenuDropdown_root"]')].find((x) => {
      const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
      return r.width > 200 && r.height > 100 && cs.visibility !== 'hidden' && cs.opacity !== '0' && cs.display !== 'none';
    });
    return !!d;
  }).catch(() => false);
  if (await open()) return 'the dropdown was already open';
  await item.hover().catch(() => {});
  await page.waitForTimeout(900);
  if (await open()) return `hovered the "${name}" menu item to open its dropdown`;
  await item.focus().catch(() => {});
  await page.waitForTimeout(700);
  return `hovered/focused "${name}"; the dropdown did not report open`;
}

// Opens the mobile nav overlay: the icon-only sandwich button in the header.
async function openMobileMenu() {
  // The drawer is the header's own HeaderMainMenu_mobileMenu block: it sits in
  // the DOM at 0 height while closed and grows to ~650px when the sandwich
  // button adds HeaderMainMenu_mobileMenuOpen to the root. Its position is not
  // fixed, so size is the reliable open signal.
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('[class*="mobileMenu"], [class*="MobileMenu"], [role="dialog"]')].find((x) => {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      return r.height > 300 && /\S/.test(x.textContent || '') && cs.visibility !== 'hidden' && cs.opacity !== '0' && cs.display !== 'none';
    });
    return !!el;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator(M('HeaderMainMenu_sandwichBtn')).filter({ visible: true }).first();
  if (!(await b.count())) return 'no sandwich button';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await open()) return 'clicked the sandwich button to open the nav overlay';
    await page.waitForTimeout(500);
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the sandwich button and pressed Enter to open the nav overlay';
  }
  return 'activated the sandwich button; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];
const BTN = M('FiberyButton_root');

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar: Fibery wordmark, Solutions/Platform/Support dropdowns, Pricing, Book a demo, Log in and the dark "Sign up for free" button.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Fibery mark-and-wordmark in the header, linking home.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-item', q(M('HeaderMenuItem_menuLink')).filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'The Pricing header link; measured, never followed.', sel: '.HeaderMenuItem_menuLink Pricing' }, { noScroll: true });
  await S('nav-menu-btn', q(M('HeaderMenuItem_root') + ', ' + M('HeaderMenuItem_expandMenu')).filter({ hasText: /^\s*Solutions/ }).first(), [...B4, 'opened'], { group: g, title: 'Dropdown trigger', desc: 'The "Solutions" header item — opens the solutions dropdown panel on hover. The opened state was measured after hovering it.', sel: '.HeaderMenuItem_root Solutions' }, { noScroll: true, noToggle: true, before: { opened: async (loc) => { await loc.hover(); await page.waitForTimeout(900); return 'hovered the "Solutions" item to open the dropdown'; } } });
  await S('nav-panel', q(M('HeaderMenuDropdown_root')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Dropdown panel', desc: 'The solutions dropdown panel opened by hovering its trigger (menu tiles plus template links); its links were never followed.', sel: '.HeaderMenuDropdown_root' }, { open: () => openMenu('Solutions'), noScroll: true, noReset: true });
  await S('nav-menu-item', q(M('HeaderMenuDropdown_root') + ' a, ' + M('HeaderMenuDropdown_root') + ' [class*="MenuItemTile"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Dropdown item', desc: 'A tile inside the open dropdown panel; measured, never followed.', sel: 'dropdown menu tile' }, { open: () => openMenu('Solutions'), noScroll: true, noReset: true });
  await page.mouse.move(720, 60).catch(() => {});
  // The header carries no separate "Book a demo" action; it lives in the hero
  // as hero-cta2 ("Book a Demo", the FiberyButton outline variant).
  await S('nav-login', q('header a, header ' + M('HeaderMainMenu_loginButton')).filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The "Log in" header link to fibery.io/login; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  await S('nav-signup', q('header ' + BTN + ', header a[class*="FiberyButton"], header ' + M('FiberyButton_solid')).filter({ hasText: /Sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The dark "Sign up for free" header button — the FiberyButton solid variant; links to /sign-up, measured never followed.', sel: 'header Sign up for free' }, { noScroll: true });
  const h = G.home;
  await S('announce-bar', q('a' + M('SpillTheTea_root')).filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Announcement pill', desc: 'The announcement pill at the top of the hero ("Are we turning Fibery into yet another AI app builder?") — a link to the blog post; measured, never followed.', sel: 'a.SpillTheTea_root' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Operating system for orgs run by nerds" — the display headline.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q(M('Subtitle_root')).filter({ hasText: /modular work platform|replaces scattered/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The muted supporting paragraph under the hero headline.', sel: 'hero .Subtitle_root' }, { noScroll: true });
  await S('hero-cta', q(BTN + ', a[class*="FiberyButton"]').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The dark "Sign up" hero button (FiberyButton solid); measured never followed.', sel: 'hero Sign up' });
  await S('hero-cta2', q(BTN + ', a[class*="FiberyButton"]').filter({ hasText: /^\s*Book a Demo\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary CTA', desc: 'The outlined "Book a Demo" hero button (FiberyButton outline); measured never followed.', sel: 'hero Book a Demo' });
  await S('product-frame', q(M('MainHero_screenSide')).filter({ visible: true }).first(), ['default'], { group: h, title: 'Product video frame', desc: 'The hero product video (the looping app screencast in a framed panel beside the copy, with its pause control); a public product mock, not the signed-in app.', sel: '.MainHero_screenSide' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: sitemap columns, social icons, security/legal links.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^(Features|Pricing|Templates)$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"One platform for the whole company" — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('price-switch', q(M('PriceSwitcher_root') + ', label').filter({ hasText: /Monthly.*Yearly|Yearly.*Monthly/i }).filter({ visible: true }).first(), ['default', 'toggled'], { group: g, title: 'Billing switch', desc: 'The Monthly/Yearly billing switch (a checkbox + label control); the toggled state flips the displayed prices — a local UI toggle, nothing sent.', sel: '.PriceSwitcher_root' }, { noScroll: true });
  await S('plan-card', q(M('PricingPlans_planItem')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan tile (the Free plan: name, icon, price, feature list, CTA).', sel: '.PricingPlans_planItem' });
  await S('plan-card-paid', q(M('PricingPlans_planItem')).filter({ hasText: /Pro|Standard/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Paid plan card', desc: 'A paid plan tile beside the Free plan.', sel: '.PricingPlans_planItem Pro' });
  await S('plan-cta', q(M('PricingPlans_planItem') + ' ' + BTN + ', ' + M('PricingPlans_planItem') + ' a').filter({ hasText: /start|sign up|try|contact/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The call-to-action inside a plan tile; measured never followed.', sel: 'plan CTA' });
  await S('faq-item', q(M('QandAItem_root')).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ row ("Is there a trial period?"); the opened state expands the answer — a local UI toggle.', sel: '.QandAItem_root' }, { allowLink: false });
  await S('extend-table', q(M('PlansExtendTable_root') + ', table').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature table', desc: 'The plan-comparison feature table under the cards.', sel: '.PlansExtendTable_root, table' });
  save();
}

async function templates() {
  if (!(await newPage('templates'))) return;
  await sheetsFor('templates');
  const g = G.templates;
  await S('tpl-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Templates headline', desc: 'The /templates index headline.', sel: 'h1' }, { noScroll: true });
  await S('tpl-card', q('a' + M('CardTemplate_root')).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Template card', desc: 'A template tile on the index (the square icon, name and description, tinted by --template-color); measured, never followed.', sel: 'a.CardTemplate_root' });
  await S('tpl-icon', q('a' + M('CardTemplate_root') + ' ' + M('TemplateSingleItemIcon_templateItemSquare')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Template icon', desc: 'A coloured template glyph (the square icon tile, tinted by --template-color).', sel: '.TemplateSingleItemIcon_templateItemSquare' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.signup;
  await S('su-panel', q(M('FormWrap_root') + ', main, form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up panel', desc: 'The "Get a head start with AI" wizard step on fibery.io/sign-up: prompt field, premade solutions, the AI submit and "Start without AI".', sel: '.FormWrap_root' }, { noScroll: true });
  await S('su-field', q('textarea#promptField, ' + M('AiPromptInput_textField')).filter({ visible: true }).first(), FIELD, { group: g, title: 'Prompt field', desc: 'The AI workspace prompt textarea; focused and typed into then cleared — never submitted.', sel: 'textarea#promptField' }, { noScroll: true, fillText: 'Create a workspace for a bakery that includes suppliers and orders' });
  await S('su-submit', q(M('AiPromptInput_submitButton') + ', ' + BTN).filter({ hasText: /Create workspace/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible', 'pressed', 'enabled'], { group: g, title: 'Create workspace button', desc: 'The AI wizard submit — disabled until the prompt holds text; the enabled state was measured after typing (the text was then cleared, never submitted).', sel: 'Create workspace' }, { noScroll: true, before: { enabled: async (loc) => { const f = q('textarea#promptField').first(); await f.click().catch(() => {}); await page.keyboard.type('a small bakery', { delay: 8 }); await page.waitForTimeout(600); return 'typed into the prompt to enable the submit (cleared afterwards, never pressed)'; } }, after: { enabled: async () => { const f = q('textarea#promptField').first(); await f.focus().catch(() => {}); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); } } });
  await S('su-premade', q(M('AiPromptInput_premadeSolution')).filter({ visible: true }).first(), B4, { group: g, title: 'Premade solution', desc: 'A premade-solution chip ("Product development"); measured, never pressed — it fills the prompt.', sel: '.AiPromptInput_premadeSolution' }, { noScroll: true });
  await S('su-skip', q('button, a').filter({ hasText: /Start without AI/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Start without AI', desc: 'The "Start without AI" skip action; measured, never followed — it advances the wizard.', sel: 'Start without AI' }, { noScroll: true });
  await S('su-steps', q(M('SignupStepPagination_root') + ', ' + M('SignupStepPagination_step')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Step pagination', desc: 'The wizard step dots at the bottom (step 1 of the workspace-creation flow).', sel: '.SignupStepPagination_step' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-panel', q(M('FormWrap_root')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The "Login to Fibery" form column on fibery.io/login: OAuth buttons, Continue with Email, Workspace SSO and the sign-up switch link.', sel: '.FormWrap_root' }, { noScroll: true });
  await S('login-google', q(M('OAuthButtonLogin_formButton') + ', button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google OAuth', desc: 'The "Continue with Google" OAuth submit — its form POSTs to /login/google/start; measured, never pressed.', sel: 'Continue with Google' }, { noScroll: true });
  await S('login-ms', q(M('OAuthButtonLogin_formButton') + ', button').filter({ hasText: /Continue with Microsoft/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Microsoft OAuth', desc: 'The "Continue with Microsoft" OAuth submit; measured, never pressed.', sel: 'Continue with Microsoft' }, { noScroll: true });
  await S('login-email', q(BTN + ', button').filter({ hasText: /Continue with Email/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Email button', desc: 'The "Continue with Email" button — reveals the e-mail step of the sign-in (a local step change, not a submission); the opened state was measured after pressing it.', sel: 'Continue with Email' }, { noScroll: true, noToggle: true, before: { opened: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click())); await page.waitForTimeout(1500); return 'pressed "Continue with Email" to reveal the e-mail step — a local UI step, nothing sent'; } } });
  await S('login-email-field', q('input[type="email"], input[name*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (login)', desc: 'The e-mail input revealed by the "Continue with Email" step; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-sso', q(BTN + ', button, a').filter({ hasText: /Workspace SSO/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Workspace SSO', desc: 'The "Workspace SSO" button; measured, never followed.', sel: 'Workspace SSO' }, { noScroll: true });
  await S('login-hint', q(M('HintSideSection_root') + ', ' + M('HintItem_root')).filter({ hasText: /Did you know|dark|theme/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Hint card', desc: 'The "Did you know?" tip card beside the sign-in (the dark/system theme tip).', sel: '.HintSideSection_root, .HintItem_root' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header: Fibery mark, the sandwich button and the sign-up CTA.', sel: 'mobile header' }, { noScroll: true });
  const ham = q(M('HeaderMainMenu_sandwichBtn')).filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The icon-only sandwich button that opens the phone nav — a local UI toggle; the opened state was measured after activating it.', sel: '.HeaderMainMenu_sandwichBtn' }, { noScroll: true, noToggle: true, before: { opened: async (loc) => { const r = await openMobileMenu(); await page.waitForTimeout(600); return r; } } });
  await S('m-drawer', q(M('HeaderMainMenu_mobileMenu') + ', ' + M('HeaderMainMenu_mobileMenuWrap')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The nav drawer opened by the sandwich button — the menu list plus the Book a demo / Log in / Sign up buttons; its links were never followed.', sel: '.HeaderMainMenu_mobileMenu' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The display headline at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q(BTN + ', a[class*="FiberyButton"]').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The "Sign up" hero button at 390 wide; measured never followed.', sel: 'mobile Sign up' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); fibery.com paints one light theme with no toggle; fibery.io/sign-up and /login share the stylesheets';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, templates, signup, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[class*="FiberyButton"], header [class*="FiberyButton"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
