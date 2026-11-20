// Measures fiverr.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs xvfb-run -a node measure.mjs [page ...]
//
// Pages: home categories subcategory search gig seller join login logo-maker
// about selling how-it-works mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fiverr.com is a React app on atomic hashed classes: its served sheets
// declare ~1,290 custom properties on :root, all named by content hash
// (--_103bn0w …) — a token-free layer with no semantic names to alias, so
// every value is a measured computed style. One light theme is
// painted; the hero search form's `dark` class is a component skin, not a
// site theme. Specs select by role, aria-label or text (the classes are
// hashed). Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the "Sidebar menu" drawer, the search page's filter
// dropdowns, the gig page's package tabs and FAQ accordion — and the fields
// (hero search, join, login) are typed into and cleared, never submitted.
// Join, Sign in, Continue, Contact me, Continue-with-* and every CTA are
// measured, never followed. A PerimeterX challenge is a boundary: it is
// never pressed or held, and a challenged page is logged as BLOCKED and left
// out. The UserWay widget and any consent layer are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { safeUrl } from '../safe-url.mjs';
import { BASE, LOGIN_URL, JOIN_URL, M, launch, launchBrowser, patch, open, closePromo, isChallenged, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', categories: '/categories', subcategory: '/categories/graphics-design/creative-logo-design', search: '/search/gigs?query=logo%20design', gig: null, seller: null, join: JOIN_URL, login: LOGIN_URL, 'logo-maker': '/logo-maker', about: '/about-us', selling: '/start_selling', 'how-it-works': '/cp/how-fiverr-works', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
let gigPath = null, sellerPath = null;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
const failedPages = new Set();
// Pages this run actually reached and measured — only these may prune their
// untouched entries below. A page function that returns before its newPage
// (gig/seller with no discovered URL, say) never lands here, so a retry run
// can never erase earlier gig/seller readings it never visited.
const finishedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|it needs a human touch|human challenge requires verification|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null } = {}) {
  current = key;
  const b = context.browser();
  // Keep one context per viewport and navigate between pages inside it. Bot
  // check: recorded as a boundary, not bypassed: a page that arrives
  // challenged is logged as BLOCKED and recorded as a failed page, with no
  // retry on fresh contexts and no clearance cookie saved or replayed.
  for (let tries = 0; tries < 1; tries++) {
    if (!liveCtx || liveCtx.__mobile !== mobile) {
      if (liveCtx) await liveCtx.close().catch(() => {});
      const ctx = liveCtx = await b.newContext(mobile
        ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
        : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
      ctx.__mobile = mobile;
      await patch(ctx);
      page = await ctx.newPage();
      cdp = await ctx.newCDPSession(page);
      await cdp.send('DOM.enable');
      await cdp.send('CSS.enable');
      page.setDefaultTimeout(8000);
    }
    log('open', key, mobile ? '(mobile)' : '');
    const opened = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
    if (opened && !(await blocked())) {
      finishedPages.add(key);
      await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
      return true;
    }
    log('  BLOCKED (bot check, boundary)', key);
    if (liveCtx) await liveCtx.close().catch(() => {});
    liveCtx = null;
  }
  failedPages.add(key);
  return false;
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
  Object.assign(c, { page: current, run, url: URLS[current] && safeUrl(URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
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
        else {
          await toggle(loc, { allowLink: opts.allowLink });
          await page.waitForTimeout(900);
          // A collapsible that reports expansion must still be open when its
          // "opened" reading is taken; a control without the attribute is
          // trusted (some toggles expose no state).
          const expanded = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
          if (expanded === 'false') throw new Error('the opened state measured closed (aria-expanded="false" after the toggle)');
          via = 'own toggle';
        }
      } else if (st === 'closed') {
        await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
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

// Clicks a UI toggle (dropdown, menu, accordion, sheet trigger). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|join fiverr|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|contact me|order|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Index of the first element matching sel whose box/node passes predSrc —
// for the cases a locator alone cannot scope: an off-screen twin (the closed
// drawer's own footer sits at x=-480) or an inline link matching a card's
// text. predSrc is a JS expression over `el` and `r` (its bounding rect).
async function nthOf(sel, predSrc) {
  return page.evaluate(([s, src]) => {
    const keep = new Function('el', 'r', `return (${src});`);
    return [...document.querySelectorAll(s)].findIndex((el) => keep(el, el.getBoundingClientRect()));
  }, [sel, predSrc]).catch(() => -1);
}

// The hero search form on the home page — the `dark`-skinned pill inside the
// hero band. The header carries a second search form (its 42px field sits in
// the top bar), so the spec must exclude every form inside the site chrome
// or hero-search/hero-search-input read the header's field instead.
const HERO_FORM = 'form[class*="search-form"]:not(.main-header form):not(header form)';
async function heroForm() {
  let loc = q(HERO_FORM).filter({ visible: true }).first();
  if (!(await loc.count())) {
    // Fallback: any form holding an input, painted below the header band.
    const i = await nthOf('form', 'el.querySelector("input") && r.width > 200 && r.y > 100');
    if (i >= 0) loc = q('form').nth(i);
  }
  return loc;
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
    await p.waitForTimeout(8000);
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
  shell: 'Site chrome', home: 'Home', directory: 'Categories and directory',
  search: 'Search results', gig: 'Gig page', sellerPage: 'Seller profile',
  auth: 'Join and sign-in edge', resources: 'Logo maker, about and selling',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's "Sidebar menu" drawer: the hamburger button whose
// ARTICLE panel (Browse categories, locale/currency, Join Fiverr/Sign in)
// slides in from the left edge. A local UI toggle; its links were never
// followed. Escape closes it afterwards.
const DRAWER_SEL = 'article, nav, aside, [role="dialog"], [class*="drawer" i], [class*="sidebar" i]';
async function openSidebar() {
  const open = () => page.evaluate(() => {
    const art = [...document.querySelectorAll('article, nav, aside, [role="dialog"], [class*="drawer" i], [class*="sidebar" i]')].find((x) => {
      const r = x.getBoundingClientRect();
      return /browse categories/i.test(x.innerText || '') && r.x >= -40 && r.width > 300;
    });
    return !!art;
  }).catch(() => false);
  if (await open()) return 'the categories drawer was already open';
  // The UserWay accessibility trigger matches the same label query — never
  // click the widget; the hamburger is the page's own chrome.
  const cand = page.locator('button[aria-label*="idebar" i], button[aria-label*="menu" i], button:has-text("Sidebar menu")').filter({ visible: true });
  const n = await cand.count();
  if (!n) return 'no Sidebar menu toggle';
  for (let i = 0; i < n; i++) {
    const b = cand.nth(i);
    if (await b.evaluate((el) => !!el.closest('.uw-sl, .uwy, .userway_buttons_wrapper, [id*="userway" i], [class*="userway" i]')).catch(() => false)) continue;
    for (let t = 0; t < 2; t++) {
      await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
      await page.waitForTimeout(1000);
      if (await open()) return 'clicked "Sidebar menu" to open the categories drawer';
      await b.focus().catch(() => {});
      await page.keyboard.press('Enter');
      await page.waitForTimeout(1000);
      if (await open()) return 'focused "Sidebar menu" and pressed Enter to open the categories drawer';
    }
  }
  return 'activated "Sidebar menu"; the drawer did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('.main-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The sticky top bar on every public page: the Fiverr wordmark, the Sidebar-menu hamburger, "Connect to your AI", the EN locale button, Become a Seller, Sign in and the green Join pill.', sel: '.main-header' }, { noScroll: true });
  await S('mkt-logo', q('.main-header a[href^="/?"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Fiverr wordmark in the header, linking home.', sel: 'main-header home link' }, { noScroll: true });
  // The hamburger: pick the first visible candidate with a real box — a
  // sr-only twin (skip/menu a11y control) can match the label query at 0x0.
  const hamBox = await page.evaluate(() => {
    const uw = '.uw-sl, .uwy, .userway_buttons_wrapper, [id*="userway" i], [class*="userway" i]';
    for (const b of document.querySelectorAll('button[aria-label*="idebar" i], button[aria-label*="menu" i], button')) {
      const t = (b.getAttribute('aria-label') || b.innerText || '');
      if (!/sidebar|menu/i.test(t) || b.closest(uw)) continue;
      const r = b.getBoundingClientRect();
      if (r.width > 8 && r.height > 8 && r.y < 120) {
        const arr = [...document.querySelectorAll('button')].indexOf(b);
        return arr;
      }
    }
    return -1;
  }).catch(() => -1);
  let ham = hamBox >= 0 ? q('button').nth(hamBox) : null;
  if (!ham) {
    // Same box discipline without the y bound: a label/text match alone can
    // land on a 0x0 sr-only twin, the drawer's own off-screen control or the
    // UserWay accessibility trigger (its skip-link button matches the same
    // label query parked at y=-70).
    const hi = await nthOf('button', '/sidebar|menu/i.test(el.getAttribute("aria-label") || el.innerText || "") && !el.closest(\'.uw-sl, .uwy, .userway_buttons_wrapper, [id*="userway" i], [class*="userway" i]\') && r.width > 8 && r.height > 8 && r.x > -2 && r.y > -2');
    ham = hi >= 0 ? q('button').nth(hi) : q('button[aria-label*="idebar" i], button:has-text("Sidebar menu")').filter({ visible: true }).first();
  }
  await S('sidebar-btn', ham, [...B4, 'opened'], { group: g, title: 'Sidebar menu button', desc: 'The header hamburger that opens the Browse-categories drawer — a local UI toggle; the opened state was measured after its own click.', sel: 'button Sidebar menu' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-ai', q('button').filter({ hasText: /^Connect to your AI$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Connect to your AI button', desc: 'The header "Connect to your AI" button (the Fiverr AI-assistant entry); measured, never pressed.', sel: 'button Connect to your AI' }, { noScroll: true });
  await S('nav-locale', q('button').filter({ hasText: /^EN$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Locale button', desc: 'The "EN" header button — a local UI toggle for the language list; measured, never toggled.', sel: 'button EN' }, { noScroll: true });
  await S('nav-seller', q('a').filter({ hasText: /^Become a Seller$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Become a Seller link', desc: 'The header "Become a Seller" link to /start_selling; measured, never followed.', sel: 'a Become a Seller' }, { noScroll: true });
  await S('nav-signin', q('a').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in link', desc: 'The header "Sign in" link to /login; measured, never followed.', sel: 'a Sign in' }, { noScroll: true });
  await S('nav-join', q('a').filter({ hasText: /^Join$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Join CTA', desc: 'The green "Join" header pill to /join — the primary header action; measured, never followed.', sel: 'a Join' }, { noScroll: true });
  await S('cat-nav', q('a').filter({ hasText: /^Graphics & Design$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category nav link', desc: 'A category-strip link under the header (Trending, Graphics & Design, Programming & Tech, …); measured, never followed.', sel: 'a Graphics & Design' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Our freelancers will take it from here" — the home hero display heading over the dark hero band.', sel: 'h1' }, { noScroll: true });
  const hf = await heroForm();
  await S('hero-search', hf, ['default'], { group: h, title: 'Hero search form', desc: 'The hero search field — the `dark`-skinned pill inside the light page: an input plus its submit button.', sel: 'hero form.search-form (the header search excluded)' }, { noScroll: true });
  await S('hero-search-input', hf.locator('input').filter({ visible: true }).first(), FIELD, { group: h, title: 'Hero search field', desc: 'The "Search for any service" input inside the dark search form; focused and typed into then cleared — never searched.', sel: 'hero search-form input' }, { noScroll: true, fillText: 'logo design' });
  const heroBtn = (await hf.locator('button[type="submit"]').count())
    ? hf.locator('button[type="submit"]').filter({ visible: true }).first()
    : hf.locator('button').filter({ visible: true }).last();
  await S('hero-search-btn', heroBtn, B4, { group: h, title: 'Search submit', desc: 'The search submit button inside the hero form; its states were measured but it was never clicked — nothing was searched.', sel: 'hero search-form submit' }, { noScroll: true });
  await S('popular-chip', q('button, a').filter({ hasText: /^(Website Development|Logo Design|Video Editing|AI Development|SEO|Software Development|Data Science|Architecture|e-Commerce|Social Media|Voice Over|UGC Videos)/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Popular-service chip', desc: 'A "Popular services" pill under the hero (Website Development, Logo Design, …); measured, never followed.', sel: 'popular service chip' });
  // A category card is a tile (image + label, card-sized), not the inline
  // category-strip link the text match alone first finds — pick the first
  // category anchor painted at card size, preferring one carrying media.
  const cardIdx = await page.evaluate(() => {
    const re = /^(Programming & Tech|Graphics & Design|Digital Marketing|Video & Animation|Writing & Translation|Music & Audio|Business|AI Services|Photography|Consulting|Finance|Data|Personal Growth)/;
    const els = [...document.querySelectorAll('a[href]')];
    const cards = els.filter((a) => {
      const r = a.getBoundingClientRect();
      return re.test((a.innerText || '').trim()) && r.width >= 120 && r.height >= 60;
    });
    const el = cards.find((a) => a.querySelector('img, picture, video, canvas')) || cards[0];
    return el ? els.indexOf(el) : -1;
  }).catch(() => -1);
  const catCard = cardIdx >= 0
    ? q('a[href]').nth(cardIdx)
    : q('a').filter({ hasText: /^(Programming & Tech|Graphics & Design|Digital Marketing|Video & Animation)$/ }).filter({ visible: true }).last();
  await S('cat-card', catCard, ['default', 'hover'], { group: h, title: 'Category card', desc: 'A service-category card tile further down the home page; measured, never followed.', sel: 'category card tile' });
  await S('section-h2', q('main h2, h2').filter({ hasText: /Make it all happen|success on Fiverr|Popular services/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading ("Make it all happen with freelancers", …).', sel: 'h2' });
  await S('trust-badge', q('[class*="rat" i], [class*="star" i]').filter({ hasText: /4\.|rating|★/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Rating badge', desc: 'A star-rating badge on the page (seller ratings, reviews strip); recorded missing when none renders.', sel: 'rating badge' });
  const f = G.footer;
  // The page footer, not the off-screen twin: the closed categories drawer
  // carries its own <footer> (Join Fiverr / Sign in) parked at x=-480, which
  // a bare `footer` query reads first. The page footer is the widest
  // on-screen footer lowest in the document; its descendants scope the
  // footer-link/locale/currency specs below.
  const footIdx = await page.evaluate(() => {
    const els = [...document.querySelectorAll('footer')];
    let best = -1, bestY = -1;
    els.forEach((el, i) => {
      const r = el.getBoundingClientRect();
      if (r.x > -2 && r.width > 600 && r.y > bestY) { best = i; bestY = r.y; }
    });
    return best;
  }).catch(() => -1);
  const foot = footIdx >= 0 ? q('footer').nth(footIdx) : q('body > footer, footer').filter({ visible: true }).last();
  await S('footer', foot, ['default'], { group: f, title: 'Footer', desc: 'The page footer: category sitemap columns, company links, social icons and the language/currency buttons.', sel: 'the on-screen page footer (the drawer\'s off-screen footer excluded)' });
  await S('footer-link', foot.locator('a').filter({ hasText: /^Careers$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Careers' });
  await S('footer-locale', foot.locator('button').filter({ hasText: /^English$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer locale button', desc: 'The "English" button in the footer — a local UI toggle for the locale list; measured, never toggled.', sel: 'footer button English' });
  await S('footer-currency', foot.locator('button').filter({ hasText: /SGD|USD|\$\s*[A-Z]{3}/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Currency button', desc: 'The currency button in the footer ("S$ SGD" for this client — prices localize); measured, never toggled.', sel: 'footer currency button' });
  save();
}

async function drawer() {
  // The open drawer is measured on the home page via the sidebar toggle.
  if (!(await newPage('home'))) return;
  const g = G.shell;
  // The closed drawer stays mounted off the left edge (x < 0), so a bare
  // hasText match can bind to it — or, when the drawer never opened, to the
  // page's own article/nav that happens to carry the same words (a 1440x5000
  // whole-page reading). Open the drawer first, then bind to the panel that
  // is actually painted at the left edge.
  await openSidebar();
  const di = await nthOf(DRAWER_SEL, '/browse categories/i.test(el.innerText || "") && r.x >= -40 && r.width > 250 && r.width < 900 && r.height < 2500');
  const dl = di >= 0 ? q(DRAWER_SEL).nth(di) : q('.drawer-panel-not-found');
  await S('drawer', dl, ['default'], { group: g, title: 'Categories drawer', desc: 'The "Browse categories" drawer the Sidebar-menu hamburger slides in from the left: category tree links, English/currency buttons, Join Fiverr and Sign in. Its links were never followed.', sel: 'article Browse categories' }, { noReset: true });
  await S('drawer-item', dl.locator('a, button').filter({ hasText: /^(Graphics & Design|Programming & Tech)$/ }).first(), B4, { group: g, title: 'Drawer category link', desc: 'A category link inside the open drawer; measured, never followed.', sel: 'drawer category link' }, { open: openSidebar, noReset: true, allowLink: true });
  await S('drawer-join', dl.locator('button, a').filter({ hasText: /^Join Fiverr$/ }).first(), B4, { group: g, title: 'Drawer Join button', desc: 'The "Join Fiverr" button at the drawer\'s foot; measured, never pressed.', sel: 'drawer Join Fiverr' }, { open: openSidebar, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  save();
}

async function categories() {
  if (!(await newPage('categories'))) return;
  await sheetsFor('categories');
  await chrome('categories');
  const g = G.directory;
  await S('dir-h2', q('h1, h2').filter({ hasText: /Fiverr Gigs|Directory|one stop shop/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Directory heading', desc: '"Fiverr Gigs® Directory" — the /categories services-directory masthead.', sel: 'directory heading' }, { noScroll: true });
  await S('dir-cat-link', q('a').filter({ hasText: /^Graphics & Design$/ }).filter({ visible: true }).last(), ['default', 'hover'], { group: g, title: 'Directory category link', desc: 'A top-category link in the services directory; measured, never followed.', sel: 'directory Graphics & Design' });
  await S('dir-sub-link', q('a').filter({ hasText: /^(Logo Design|Creative Logo Design|Brand Style Guides|Website Design)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Directory subcategory link', desc: 'A subcategory link nested under a top category in the directory; measured, never followed.', sel: 'directory subcategory link' });
  save();
}

async function subcategory() {
  if (!(await newPage('subcategory'))) return;
  await sheetsFor('subcategory');
  await chrome('subcategory');
  const g = G.directory;
  await S('sub-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Subcategory heading', desc: 'The subcategory masthead on /categories/graphics-design/creative-logo-design.', sel: 'subcategory h1' }, { noScroll: true });
  await S('breadcrumb', q('a').filter({ hasText: /^Graphics & Design$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Breadcrumb link', desc: 'The category breadcrumb link back up the tree; measured, never followed.', sel: 'breadcrumb Graphics & Design' }, { noScroll: true });
  await S('related-chip', q('a, button').filter({ hasText: /^(Minimalist|Hand Drawn|3D|Vintage|Mascot|Flat|Signature)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Related-search chip', desc: 'A related-search/style chip row on the subcategory page; measured, never followed.', sel: 'subcategory related chip' });
  save();
}

async function search() {
  if (!(await newPage('search', { wait: 11000 }))) return;
  await sheetsFor('search');
  await chrome('search');
  const g = G.search;
  await S('search-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Results headline', desc: '"Results for logo design" — the search-results masthead.', sel: 'search h1' }, { noScroll: true });
  await S('filter-btn', q('button').filter({ hasText: /^(Budget|Delivery Time|Seller Details|Service Options|Category|Pro services)$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Filter button', desc: 'A results-filter dropdown trigger (Category, Service Options, Seller Details, Budget, Delivery Time) — a local UI toggle; the opened state was measured after its own click, then closed.', sel: 'filter dropdown button' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('sort-btn', q('button, [role="combobox"]').filter({ hasText: /^(Sort by|Best Seller|Recommended|Newest)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sort control', desc: 'The "Sort by" results control; measured at rest, never toggled.', sel: 'sort control' }, { noScroll: true });
  // A gig listing card: thumbnail, seller row, rating, price, collect heart.
  const card = q('a[href]').filter({ hasText: /Level \d|Top Rated|Fiverr's Choice|★|4\.\d/ }).locator('xpath=ancestor::*[self::li or self::div][.//img][1]').filter({ visible: true }).first();
  if (!(await card.count())) {
    const alt = q('a[href]').filter({ hasText: /Level \d|Top Rated|4\.\d/ }).filter({ visible: true }).first();
    await S('gig-card', alt, ['default', 'hover'], { group: g, title: 'Gig card', desc: 'A gig listing card (thumbnail, seller name, rating, starting price, collect heart); measured, never followed.', sel: 'gig result card' });
  } else {
    await S('gig-card', card, ['default', 'hover'], { group: g, title: 'Gig card', desc: 'A gig listing card (thumbnail, seller name, rating, starting price, collect heart); measured, never followed.', sel: 'gig result card' });
  }
  await S('gig-heart', q('button[aria-label*="ollect" i], button[aria-label*="avorite" i], button[aria-label*="like" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Collect button', desc: 'A gig card\'s heart/collect button; measured, never pressed (a collect would write to an account).', sel: 'collect button' });
  await S('gig-price', await domFind(page, /^(From |Starting at )?(S\$|US\$|\$)\s?\d/i, { sel: 'span, p, div, a', tag: 'gp', minW: 20 }), ['default'], { group: g, title: 'Card price', desc: 'The "From S$xx" starting price on a gig card — localized to this client\'s currency (SGD).', sel: 'gig card price' });
  await S('seller-badge', await domFind(page, /^(Top Rated|Level \d|Fiverr's Choice|New)/i, { sel: 'span, div', tag: 'sb', minW: 20 }), ['default'], { group: g, title: 'Seller badge', desc: 'A seller-level badge on a gig card (Top Rated, Level 2, …); recorded at rest.', sel: 'seller level badge' });
  const { gig, seller } = await page.evaluate(() => {
    const cards = [...document.querySelectorAll('a[href]')].map((a) => a.getAttribute('href') || '');
    const gigHref = cards.find((h) => /^\/[^/]+\/[^/]{8,}/.test(h) && !h.startsWith('/categories') && !h.startsWith('/search') && !/join|login|start_selling|logo-maker|cp\//.test(h));
    return { gig: gigHref, seller: gigHref ? '/' + gigHref.split('/')[1] : null };
  }).catch(() => ({}));
  if (gig) gigPath = gig;
  if (seller) sellerPath = seller;
  // Recorded through safeUrl: a scraped href can carry a query or a tracking id.
  out._meta.gigPage = { gig: gig && safeUrl(BASE + gig), seller: seller && safeUrl(BASE + seller), note: 'the first gig card on /search/gigs?query=logo%20design — a live public gig and its seller profile, loaded directly' };
  save();
}

async function gig() {
  if (!gigPath) { log('gig skipped — no gig URL (run search first)'); return; }
  URLS.gig = gigPath;
  if (!(await newPage('gig', { url: BASE + gigPath, wait: 11000 }))) return;
  await sheetsFor('gig');
  await chrome('gig');
  const g = G.gig;
  await S('gig-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Gig headline', desc: 'The gig page\'s "I will …" title.', sel: 'gig h1' }, { noScroll: true });
  await S('gig-breadcrumb', q('a').filter({ hasText: /^(Graphics & Design|Logo Design|Creative Logo Design)$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Gig breadcrumb', desc: 'The category breadcrumb on the gig page; measured, never followed.', sel: 'gig breadcrumb' }, { noScroll: true });
  await S('pkg-tablist', q('[role="tablist"], nav').filter({ hasText: /BASIC|STANDARD|PREMIUM/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Package tabs', desc: 'The Basic/Standard/Premium package tablist on the pricing card.', sel: 'package tablist' });
  await S('pkg-tab-on', q('[role="tab"][aria-selected="true"], a[aria-selected="true"], [class*="active" i]').filter({ hasText: /BASIC|STANDARD|PREMIUM/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Selected package tab', desc: 'The selected package tab (Basic) in the pricing card.', sel: 'selected package tab' });
  await S('pkg-tab', q('[role="tab"], button, a').filter({ hasText: /^(STANDARD|PREMIUM|VIP)$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Package tab', desc: 'An unselected package tab (Standard/Premium) in the pricing card; measured at rest, never switched (switching re-prices the card).', sel: 'package tab' });
  await S('pkg-price', await domFind(page, /^(S\$|US\$|\$|SGD|USD)\s?\d/i, { sel: 'span, p, div, h3, b', tag: 'pp', minW: 20 }), ['default'], { group: g, title: 'Package price', desc: 'The selected package\'s price on the pricing card — localized (SGD for this client).', sel: 'package price' });
  await S('gig-continue', q('button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The pricing card\'s green "Continue" button; its states were measured but it was never pressed — it leads to checkout.', sel: 'gig Continue' });
  await S('gig-contact', q('button').filter({ hasText: /^Contact me$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact me button', desc: 'The "Contact me" button beside Continue; measured, never pressed (it fronts a sign-in wall).', sel: 'gig Contact me' });
  await S('seller-card', q('div, aside, section').filter({ hasText: /Get to know|About the seller|orders in queue/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Seller card', desc: 'The "Get to know" seller card (avatar, level, rating, location).', sel: 'seller card' });
  await S('faq-acc', q('button, [role="button"], summary').filter({ hasText: /\?/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the gig page\'s FAQ section; the opened state was measured after clicking it — a local UI toggle.', sel: 'gig FAQ row' });
  await S('review-card', q('div, article, li').filter({ hasText: /★|out of 5|stars?/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Review card', desc: 'A review block in the gig\'s reviews list (reviewer name, star rating, review text).', sel: 'gig review card' });
  await S('tag-chip', q('a').filter({ hasText: /^(logo design|minimalist|brand|business logo|vector)/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Related tag', desc: 'A related-tag chip under the gig (Related tags); measured, never followed.', sel: 'gig related tag' });
  save();
}

async function seller() {
  if (!sellerPath) { log('seller skipped — no seller URL (run search first)'); return; }
  URLS.seller = sellerPath;
  if (!(await newPage('seller', { url: BASE + sellerPath, wait: 11000 }))) return;
  await sheetsFor('seller');
  await chrome('seller');
  const g = G.sellerPage;
  await S('seller-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Seller headline', desc: 'The seller profile\'s name/headline.', sel: 'seller h1' }, { noScroll: true });
  await S('seller-contact', q('button').filter({ hasText: /^Contact me$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Profile Contact me', desc: 'The "Contact me" button on the seller profile; measured, never pressed.', sel: 'seller Contact me' });
  await S('seller-gig-card', q('a[href]').filter({ hasText: /From |Starting at|\$\d/ }).locator('xpath=ancestor::*[self::li or self::div][.//img][1]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Profile gig card', desc: 'A gig card on the seller profile\'s listings grid; measured, never followed.', sel: 'seller gig card' });
  save();
}

async function join() {
  if (!(await newPage('join', { wait: 10000 }))) return;
  await sheetsFor('join');
  await chrome('join');
  const g = G.auth;
  await S('join-panel', q('form, main, [class*="sign" i]').filter({ hasText: /Create a new account|Success starts here/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Join panel', desc: 'The /join sign-up card — "Create a new account" with the Continue-with-* SSO buttons and the email join path.', sel: 'join panel' }, { noScroll: true });
  await S('join-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO (join)', desc: 'The "Continue with Google" button on /join; measured, never pressed.', sel: 'join Continue with Google' }, { noScroll: true });
  await S('join-apple', q('button').filter({ hasText: /Continue with Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple SSO (join)', desc: 'The "Continue with Apple" button on /join; measured, never pressed.', sel: 'join Continue with Apple' }, { noScroll: true });
  await S('join-email-btn', q('button').filter({ hasText: /email|Continue/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Email join button', desc: 'The e-mail join button on /join; measured, never pressed.', sel: 'join email button' }, { noScroll: true });
  await S('join-field', q('input[type="email"], input[type="text"], input[name*="email" i], input[name*="username" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Join field', desc: 'A join form field (e-mail/username); focused and typed into then cleared — never submitted. Recorded missing when /join renders SSO-only.', sel: 'join input' }, { noScroll: true, fillText: 'name@example.com' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('login-panel', q('form, main, [class*="sign" i], [class*="login" i]').filter({ hasText: /Sign in to your account|Success starts here/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login panel', desc: 'The /login card — "Sign in to your account" with the Continue-with-* SSO buttons and the username/password form.', sel: 'login panel' }, { noScroll: true });
  await S('login-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO (login)', desc: 'The "Continue with Google" button on /login; measured, never pressed.', sel: 'login Continue with Google' }, { noScroll: true });
  await S('login-email', q('input[type="text"], input[type="email"], input[name*="email" i], input[name*="username" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email/username field', desc: 'The username-or-e-mail input on the sign-in form; focused and typed into then cleared — never submitted.', sel: 'login username input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-password', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The password input on the sign-in form; focused and typed into then cleared — never submitted.', sel: 'login password input' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /^(Sign in|Log in|Continue)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in submit', desc: 'The sign-in form\'s submit button; its states were measured but it was never clicked — nothing was submitted.', sel: 'login submit' }, { noScroll: true });
  save();
}

async function logoMaker() {
  if (!(await newPage('logo-maker'))) return;
  await sheetsFor('logo-maker');
  const g = G.resources;
  await S('lm-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo maker headline', desc: 'The /logo-maker masthead.', sel: 'logo-maker h1' }, { noScroll: true });
  await S('lm-cta', q('a, button').filter({ hasText: /^(Make a logo|Create|Start|Get started|Try)/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Logo maker CTA', desc: 'The logo maker\'s primary CTA; measured, never followed.', sel: 'logo-maker CTA' });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  const g = G.resources;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: 'The /about-us masthead ("ABOUT US" eyebrow, "Making way for breakthroughs").', sel: 'about h1' }, { noScroll: true });
  await S('about-cta', q('a, button').filter({ hasText: /^(Learn more|Read more|See how|Explore)/i }).filter({ visible: true }).first(), B4, { group: g, title: 'About link', desc: 'A marketing link on /about-us; measured, never followed.', sel: 'about link' });
  save();
}

async function selling() {
  if (!(await newPage('selling'))) return;
  await sheetsFor('selling');
  const g = G.resources;
  await S('sell-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Selling headline', desc: 'The /start_selling masthead ("Turn your expertise into a global business").', sel: 'selling h1' }, { noScroll: true });
  await S('sell-cta', q('button, a').filter({ hasText: /^(Create your profile|Get started|Become a seller)/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Seller CTA', desc: 'The "Create your profile" / "Get started" CTA on /start_selling; measured, never followed.', sel: 'selling CTA' });
  await S('sell-cat', q('button').filter({ hasText: /^(Programming & Tech|AI Services|Graphic & Design|Digital Marketing|Consulting)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Selling category chip', desc: 'A category chip on the seller landing page; measured, never toggled.', sel: 'selling category chip' });
  save();
}

async function howItWorks() {
  if (!(await newPage('how-it-works'))) return;
  await sheetsFor('how-it-works');
  const g = G.resources;
  await S('hiw-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'How-it-works headline', desc: 'The /cp/how-fiverr-works masthead.', sel: 'how-fiverr-works h1' }, { noScroll: true });
  await S('hiw-step', q('h2, h3, div').filter({ hasText: /^4 simple steps|Meet Fiverr Go|steps to your success/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Steps section', desc: 'A step block on the how-it-works explainer.', sel: 'how-fiverr-works steps' });
  await S('hiw-faq', q('button, [role="button"], summary').filter({ hasText: /\?/ }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'HIW FAQ accordion', desc: 'A question row in the page\'s FAQ section; the opened state was measured after clicking it — a local UI toggle.', sel: 'how-fiverr-works FAQ row' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('.main-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the hamburger, the Fiverr wordmark and the Join/sign-in controls.', sel: 'mobile main-header' }, { noScroll: true });
  const ham = q('button[aria-label*="idebar" i], button:has-text("Sidebar menu")').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The hamburger that opens the categories drawer — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile Sidebar menu' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q(DRAWER_SEL).filter({ hasText: /Browse categories/ }).first(), ['default'], { group: g, title: 'Mobile drawer', desc: 'The categories drawer open at 390 wide (Browse categories tree plus locale/currency and Join/Sign-in at its foot); its links were never followed.', sel: 'mobile categories drawer' }, { open: openSidebar, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  const mhf = await heroForm();
  await S('m-search-input', mhf.locator('input, input[type="search"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Mobile search field', desc: 'The hero search input at 390 wide (the header search excluded); focused, never searched.', sel: 'mobile hero search input' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every public page paints the single light theme (the hero search form\'s `dark` class is a component skin, not a site theme); prices localize — this client saw SGD';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, drawer, categories, subcategory, search, gig, seller, join, login, logoMaker, about, selling, howItWorks, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the header Join
  // pill's hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.main-header a[href^="/join"]');
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
