// Measures faire.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home category brand suppliers suppliersAll howItWorks about news
// careers largeRetailers pos markets support affiliates apply signin signup
// notfound mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// faire.com paints one light theme signed out (no theme attribute, no user
// toggle); components carry the Slate design system's fs-* classes
// (fs-button--primary/secondary/plain, fs-icon-button, fs-checkbox__input,
// fs-tag, fs-avatar) whose styles resolve from the --slate-* token layer.
// The auth surface is a dialog over the home page mounted by ?signIn=1 /
// ?signUp=1; both are measured at rest, never submitted. Product tiles link
// to ?signUp=product (the sign-up dialog) and are never followed. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the
// "All categories" dropdown, the mobile Menu button and the apply form's
// show-password icon; every form field is typed into and cleared; Sign in,
// Sign up for free, Next, Google SSO and every submit are measured, never
// followed. The OneTrust consent layer is hidden, never answered; the
// intermittent Cloudflare edge challenge is waited out, never solved.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, SIGNIN_URL, SIGNUP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', category: '/category/Home%20Decor', brand: '/brand/b_d72c56fe',
  suppliers: '/suppliers/Home%20Decor/subcategory/Candles%20%26%20Holders/Candles',
  suppliersAll: '/suppliers/All%20Brands', howItWorks: '/how-faire-works', about: '/about',
  news: '/news', careers: '/careers', largeRetailers: '/large-retailers', pos: '/point-of-sale/about',
  markets: '/markets', support: '/support', affiliates: '/affiliates', apply: '/apply',
  signin: SIGNIN_URL, signup: SIGNUP_URL, notfound: '/pagenotfound', mobile: '/',
};
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
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|next|finish|done|verify|confirm|sign up|sign up for free|sign up to buy|sign up to sell)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
  shell: 'Site chrome', home: 'Home', category: 'Category teaser', brand: 'Brand storefront',
  suppliers: 'Suppliers listings', marketing: 'Marketing pages', apply: 'Brand application (/apply)',
  signin: 'Sign-in dialog', signup: 'Sign-up dialog', support: 'Help center',
  mobile: 'Mobile (390 wide)', footer: 'Footer', dialog: 'Auth dialogs',
};

// Opens the header's "All categories" dropdown — a local UI toggle, never a
// link. Pointer activation first, keyboard Enter as the fallback, matching
// public.mjs's allCategories().
async function openCategories() {
  const btn = page.locator('button').filter({ hasText: /^\s*All categories\s*$/ }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no All categories button';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true'
    || await page.evaluate(() => !!([...document.querySelectorAll('[role="menu"],[role="listbox"],header [class*="dropdown" i],header [class*="menu" i]')].find((x) => { const r = x.getBoundingClientRect(); const cs = getComputedStyle(x); return r.height > 120 && /\S/.test(x.textContent || '') && cs.visibility !== 'hidden' && cs.opacity !== '0'; }))).catch(() => false);
  if (await open()) return 'the categories menu was already open';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    await page.waitForTimeout(800);
    if (await open()) return 'clicked the "All categories" button to open the menu';
    await btn.focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(800);
    if (await open()) return 'focused the "All categories" button and pressed Enter to open the menu';
  }
  return 'activated "All categories"; the menu did not report open';
}

// Opens the mobile nav drawer: the header's "Menu button" — a local UI
// toggle; its links are never followed.
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('[role="dialog"],body > div[class*="drawer" i],[class*="menu" i][class*="open" i]')].find((x) => {
      const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
      return r.height > 300 && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
    });
    return !!el;
  }).catch(() => false);
  if (await open()) return 'the nav drawer was already open';
  const b = page.locator('button[aria-label*="Menu" i], header button').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the Menu button to open the nav drawer';
    await b.focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(900);
    if (await open()) return 'focused the Menu button and pressed Enter to open the nav drawer';
  }
  return 'activated the Menu button; the drawer did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The white top bar: Faire wordmark, "All categories" dropdown, search field, locale button, Blog, "Sign up to sell", "Sign in" and the dark "Sign up to buy" button.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"], header a[aria-label*="Faire" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Faire wordmark in the header, linking home.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('search-field', q('input[type="search"], header input, input[placeholder*="Search" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Header search field', desc: 'The "Search wholesale products or brands" field; focused and typed into then cleared — nothing searched.', sel: 'input[type=search]' }, { noScroll: true, fillText: 'candles' });
  await S('all-categories-btn', q('button').filter({ hasText: /^\s*All categories\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'All categories button', desc: 'The rounded header dropdown trigger (rounded-[32px]); the opened state was measured after activating it — a local UI toggle, its links never followed.', sel: 'header button "All categories"' }, { noScroll: true, allowLink: true, before: { opened: async (loc) => openCategories().then((v) => { void loc; return v; }) } });
  await S('categories-panel', q('[role="menu"], [role="listbox"], header [class*="dropdown" i], header [class*="menu" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Categories menu panel', desc: 'The panel opened by "All categories"; its links were never followed.', sel: 'categories menu panel' }, { open: openCategories, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('locale-btn', q('header p').filter({ hasText: /^EN-[A-Z]{2}$/ }).filter({ visible: true }).first().locator('xpath=ancestor::div[2]'), B4, { group: g, title: 'Locale button', desc: 'The EN-US locale selector (globe + "EN-US") in the header — a div control, not a button; measured, never opened.', sel: 'header locale control' }, { noScroll: true });
  await S('nav-signin', q('header button, button').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in button', desc: 'The header "Sign in" — it mounts the sign-in dialog; measured, never pressed.', sel: 'header "Sign in"' }, { noScroll: true });
  await S('nav-sell', q('header a, a').filter({ hasText: /^\s*Sign up to sell\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up to sell link', desc: 'The header link to the brand application; measured, never followed.', sel: 'header "Sign up to sell"' }, { noScroll: true });
  await S('nav-signup-buy', q('header button.fs-button--primary, button.fs-button--primary').filter({ hasText: /Sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up to buy button', desc: 'The dark "Sign up to buy" fs-button--primary in the header; measured, never pressed.', sel: 'header .fs-button--primary' }, { noScroll: true });
  await S('nav-link', q('header a, nav a').filter({ hasText: /^\s*Blog\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The header Blog link; measured, never followed.', sel: 'header a "Blog"' }, { noScroll: true });
  await S('promo-banner', q('p, div, span').filter({ hasText: /Shop wholesale online from over 100,000 brands/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Promo banner', desc: 'The top strip above the header ("Shop wholesale online from over 100,000 brands. Sign up").', sel: 'promo strip' }, { noScroll: true });
  await S('cat-nav-link', q('header a, header li a').filter({ hasText: /^(New products|New brands|Home decor)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category nav link', desc: 'A link in the sub-header category strip ("New products", "Home decor"…); measured, never followed.', sel: 'header category a' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Find your next bestseller" — the type-fs-display display heading in inverse ink over the hero media.', sel: 'h1.type-fs-display' }, { noScroll: true });
  await S('hero-panel', q('h1').locator('xpath=ancestor::section[1]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero panel', desc: 'The hero block behind the display heading.', sel: 'hero section' }, { noScroll: true });
  await S('cta-primary', q('main button.fs-button--primary').filter({ hasText: /Sign up|Get started|Explore/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Primary button', desc: 'A dark "Sign up to buy" fs-button--primary (medium); measured, never pressed.', sel: 'main .fs-button--primary' });
  await S('cta-secondary', q('button.fs-button--secondary').filter({ visible: true }).first(), B4, { group: h, title: 'Secondary button', desc: 'An outlined "Sign up to buy" fs-button--secondary; measured, never pressed.', sel: '.fs-button--secondary' });
  await S('cta-plain', q('button.fs-button--plain').filter({ hasText: /Sign up for free|Sign up/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Plain button', desc: 'A "Sign up for free" fs-button--plain text button; measured, never pressed.', sel: '.fs-button--plain' });
  await S('pill-tab', q('main div[class*="f_c_slide_width" i], div[class*="f_c_slide_width" i]').filter({ hasText: /^(Women|Home decor|Jewelry|Books|Men|Pets)$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Featured-brands pill tab', desc: 'A rounded pill filter tab under "Featured brands" (the selected one paints dark); measured, never toggled.', sel: 'featured-brands pill' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  await S('brand-card', q('a[href*="/brand/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Brand card', desc: 'A brand tile on the home page (image, name); measured, never followed.', sel: 'a[href*=/brand/]' });
  await S('category-card', q('main a[href^="/category/"], main a[href*="/category/"]').filter({ has: page.locator('img') }).filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Category card', desc: 'A category tile (image, label); measured, never followed.', sel: 'a[href*=/category/]:has(img)' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: brand promise line, sitemap columns, locale and social links, legal row.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /About|Careers|News/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  save();
}

async function category() {
  if (!(await newPage('category'))) return;
  await sheetsFor('category');
  await chrome('category');
  const g = G.category;
  await S('cat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category headline', desc: 'The category page masthead ("Wholesale home decor for your store").', sel: 'h1' }, { noScroll: true });
  await S('cat-filter-btn', q('button').filter({ hasText: /^\s*All filters\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'All filters button', desc: 'The filters trigger on the category teaser grid; measured, never opened.', sel: 'category "All filters" button' }, { noScroll: true });
  await S('product-tile', q('a[href*="product="], a[href*="signUp"]').filter({ has: page.locator('img') }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A product card in the teaser grid (photo, name, price); clicking it mounts the sign-up dialog, so it was measured, never followed.', sel: 'product tile a:has(img)' });
  await S('brand-tile', q('main a[href*="/brand/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Brand link on card', desc: 'A brand name link inside a product card on the category page; measured, never followed.', sel: 'main a[href*=/brand/]' });
  await S('subcat-card', q('a[href*="/category/"], a[href*="/suppliers/"]').filter({ has: page.locator('img') }).filter({ visible: true }).first(), B4, { group: g, title: 'Subcategory card', desc: 'A card in the "Explore diverse styles" subcategory grid (thumbnail + label); measured, never followed.', sel: 'subcategory card a:has(img)' });
  await S('wall-field', q('input[name*="email" i], input[type="email"], input[placeholder*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Sign-up wall email field', desc: 'The "Business email address" field in the page\'s sign-up section; focused and typed into then cleared — never submitted.', sel: 'email input' }, { fillText: 'name@example.com' });
  await S('wall-submit', q('button').filter({ hasText: /Sign up|Get started|Unlock/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Sign-up wall button', desc: 'The sign-up CTA beside the email field; measured, never pressed.', sel: 'sign-up wall button' });
  save();
}

async function brand() {
  if (!(await newPage('brand'))) return;
  await sheetsFor('brand');
  await chrome('brand');
  const g = G.brand;
  await S('brand-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand headline', desc: '"54 Celsius wholesale" — the brand storefront masthead.', sel: 'h1' }, { noScroll: true });
  await S('brand-avatar', q('[class*="fs-avatar" i]').filter({ has: page.locator('img') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand avatar', desc: 'The brand\'s circular fs-avatar logo by the masthead.', sel: 'span.fs-avatar' }, { noScroll: true });
  await S('min-order-badge', q('span, div').filter({ hasText: /^US\$\d+ min$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Minimum order badge', desc: 'The "US$100 min" order-minimum label on brand tiles.', sel: '"US$X min" badge' });
  await S('brand-tab', q('a, button').filter({ hasText: /^\s*(All products|New)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Section tab', desc: 'A storefront section nav item ("All products"/"New"); measured, never followed.', sel: 'brand section tab' });
  await S('brand-product-tile', q('a[href*="product="], a[href*="signUp=product"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Brand product tile', desc: 'A product card on the brand page (photo, name, price, order minimum); it links to the sign-up dialog — measured, never followed.', sel: 'brand product tile' });
  await S('about-h2', q('h2').filter({ hasText: /^About/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'About heading', desc: 'The "About <brand>" section heading.', sel: 'h2 About' });
  await S('wall-email', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Wall email field', desc: 'The "Business email address" field in the brand page\'s sign-up wall; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { fillText: 'name@example.com' });
  save();
}

async function suppliers() {
  if (!(await newPage('suppliers'))) return;
  await sheetsFor('suppliers');
  const g = G.suppliers;
  await S('sup-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Suppliers headline', desc: 'The SEO suppliers listing masthead.', sel: 'h1' }, { noScroll: true });
  await S('supplier-row', q('a[href*="/brand/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Supplier row', desc: 'A brand row/card in the suppliers listing; measured, never followed.', sel: 'suppliers a[href*=/brand/]' });
  await S('sup-filter-link', q('a').filter({ hasText: /Skincare|Candles|Coffee|Kitchen/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Subcategory link', desc: 'A related-subcategory link; measured, never followed.', sel: 'suppliers subcategory a' });
  save();
}

async function suppliersAll() {
  if (!(await newPage('suppliersAll'))) return;
  const g = G.suppliers;
  await S('supall-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'All brands headline', desc: 'The /suppliers/All Brands masthead.', sel: 'h1' }, { noScroll: true });
  await S('supall-row', q('a[href*="/brand/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'All brands row', desc: 'A brand row in the A-Z listing; measured, never followed.', sel: 'suppliers/All a[href*=/brand/]' });
  save();
}

// One h1 + CTA + card per marketing page.
async function marketing(key, hkey, ckey, dkey, title1, ctaRe) {
  if (!(await newPage(key))) return;
  await sheetsFor(key);
  const g = G.marketing;
  await S(hkey, q('h1, h2, h3').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: title1, desc: `The ${URLS[key]} masthead.`, sel: 'h1' }, { noScroll: true });
  await S(ckey, q('a, button').filter({ hasText: ctaRe }).filter({ visible: true }).first(), B4, { group: g, title: `${title1} CTA`, desc: 'The page\'s main call to action; measured, never followed or pressed.', sel: `${key} CTA` });
  if (dkey) await S(dkey, q('a[href*="/news/"], article, [class*="card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: `${title1} card`, desc: 'A content card on the page; measured, never followed.', sel: `${key} card` });
  save();
}

async function apply() {
  if (!(await newPage('apply', { wait: 9000 }))) return;
  await sheetsFor('apply');
  await chrome('apply');
  const g = G.apply;
  await S('apply-heading', q('h1, h2, h3, h4').filter({ hasText: /Welcome! Sign up|Tell us about/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Application heading', desc: 'The /apply step heading ("Welcome! Sign up to sell on Faire." — an h4 in the f_t_displaySSerifRegular serif role).', sel: 'apply h4 heading' }, { noScroll: true });
  await S('back-btn', q('button[aria-label*="back" i], button[aria-label*="previous" i], header button, nav button').filter({ visible: true }).first(), B4, { group: g, title: 'Back button', desc: 'The "Go back" chevron icon button in the top bar; measured, never pressed.', sel: 'apply back button' }, { noScroll: true });
  await S('field-firstname', q('input[name="firstName"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'First name field', desc: 'The firstName input; focused and typed into then cleared — never submitted.', sel: 'input[name=firstName]' }, { fillText: 'Ada' });
  await S('field-lastname', q('input[name="lastName"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Last name field', desc: 'The lastName input; focused and typed into then cleared — never submitted.', sel: 'input[name=lastName]' }, { fillText: 'Lovelace' });
  await S('field-email', q('input[name="email"], input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The work-email input; focused and typed into then cleared — never submitted.', sel: 'input[name=email]' }, { fillText: 'name@example.com' });
  await S('field-phone', q('input[name="phoneNumber"], input[type="tel"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Phone field', desc: 'The phoneNumber input with its +1 country-code prefix button; focused and typed into then cleared — never submitted.', sel: 'input[name=phoneNumber]' }, { fillText: '555 000 0000' });
  await S('phone-code-btn', q('button').filter({ hasText: /^\+1$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Country code button', desc: 'The +1 country-code prefix button inside the phone field; measured, never opened.', sel: 'phone +1 button' });
  await S('field-password', q('input[name="password"], input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input (with a show-password icon); focused only — nothing was typed or submitted.', sel: 'input[name=password]' });
  await S('show-password', q('button[aria-label*="password" i], button.fs-icon-button').filter({ visible: true }).first(), B4, { group: g, title: 'Show password icon button', desc: 'The fs-icon-button--plain show/hide toggle inside the password field; measured, never pressed.', sel: 'show password button' });
  await S('checkbox-terms', q('input[name="acceptedTerms"], .fs-checkbox__input').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Terms checkbox', desc: 'The fs-checkbox for the terms consent; measured, never toggled.', sel: '.fs-checkbox__input' });
  await S('checkbox-marketing', q('input[name="marketingOptIn"], .fs-checkbox__input').filter({ visible: true }).last(), ['default'], { group: g, title: 'Marketing checkbox', desc: 'The opt-in fs-checkbox; measured, never toggled.', sel: '.fs-checkbox__input marketing' });
  await S('next-btn', q('button').filter({ hasText: /^\s*Next\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Next button', desc: 'The form\'s dark fs-button--primary "Next" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'apply Next' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 10000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.signin;
  const D = q('.fs-modal, [role="dialog"]').filter({ hasText: /Sign in to Faire/i }).filter({ visible: true }).last();
  await S('signin-dialog', D, ['default'], { group: g, title: 'Sign-in dialog', desc: 'The "Sign in to Faire" fs-modal mounted by ?signIn=1 over the home page: email + password fields, dark submit, Google and Apple SSO, a sign-up link and the close icon.', sel: '.fs-modal sign-in' }, { noScroll: true });
  await S('signin-email', D.locator('input[name="email"], input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The email input in the sign-in dialog; focused and typed into then cleared — never submitted.', sel: 'sign-in input[name=email]' }, { fillText: 'name@example.com' });
  await S('signin-password', D.locator('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field (sign-in)', desc: 'The password input in the sign-in dialog; focused only — nothing was typed or submitted.', sel: 'sign-in input[type=password]' });
  await S('signin-submit', D.locator('button').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in submit', desc: 'The dialog\'s Sign in submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'sign-in submit' });
  await S('signin-google', D.locator('button').filter({ hasText: /Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: '"Sign in with Google"; measured, never followed.', sel: 'sign-in Google button' });
  await S('signin-apple', D.locator('button').filter({ hasText: /Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple SSO button', desc: '"Sign in with Apple"; measured, never followed.', sel: 'sign-in Apple button' });
  await S('signin-signup-link', D.locator('a, button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up link (sign-in)', desc: 'The "Sign up" action inside the sign-in dialog; measured, never followed.', sel: 'sign-in Sign up' });
  await S('signin-close', D.locator('button[aria-label*="close" i], button[aria-label*="dismiss" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Dialog close button', desc: 'The dialog\'s "Close modal" icon button; measured, never pressed.', sel: 'sign-in close' });
  await S('signin-show-password', D.locator('button[aria-label*="password" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Show password icon (sign-in)', desc: 'The eye icon inside the password field; measured, never pressed.', sel: 'sign-in show password' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  const g = G.signup;
  const D = q('.fs-modal, [role="dialog"]').filter({ hasText: /wholesale|Sign up/i }).filter({ visible: true }).last();
  await S('signup-dialog', D, ['default'], { group: g, title: 'Sign-up dialog', desc: 'The "Unlock wholesale pricing" fs-modal mounted by ?signUp=1: business-email field, "Sign up for free" submit, Google and Apple SSO and a sign-in link.', sel: '.fs-modal sign-up' }, { noScroll: true });
  await S('signup-email', D.locator('input[type="email"], input[name*="email" i], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Business email field', desc: 'The business-email input in the sign-up dialog; focused and typed into then cleared — never submitted.', sel: 'sign-up email input' }, { fillText: 'name@example.com' });
  await S('signup-submit', D.locator('button').filter({ hasText: /Sign up for free|^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up submit', desc: 'The dialog\'s "Sign up for free" submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'sign-up submit' });
  await S('signup-google', D.locator('button').filter({ hasText: /Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button (sign-up)', desc: '"Sign up with Google"; measured, never followed.', sel: 'sign-up Google button' });
  await S('signup-apple', D.locator('button').filter({ hasText: /Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple SSO button (sign-up)', desc: '"Sign up with Apple"; measured, never followed.', sel: 'sign-up Apple button' });
  await S('signup-signin-link', D.locator('a, button').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in link (sign-up)', desc: 'The "Sign in" action inside the sign-up dialog; measured, never followed.', sel: 'sign-up Sign in' });
  await S('signup-close', D.locator('button[aria-label*="close" i], button[aria-label*="dismiss" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Dialog close button (sign-up)', desc: 'The dialog\'s "Close modal" icon button; measured, never pressed.', sel: 'sign-up close' });
  save();
}

async function support() {
  if (!(await newPage('support'))) return;
  await sheetsFor('support');
  const g = G.support;
  await S('help-h1', q('h1, h2, h3').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Help center headline', desc: 'The /support help-center masthead.', sel: 'h1' }, { noScroll: true });
  await S('help-search', q('input[placeholder*="Search" i], input[type="search"], input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Help search field', desc: 'The "Search retailer guides" field; focused and typed into then cleared — nothing searched.', sel: 'support search input' }, { fillText: 'shipping' });
  await S('help-link', q('a').filter({ hasText: /order|shipping|account|payment/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Help topic link', desc: 'A help topic link; measured, never followed.', sel: 'support topic a' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header: Faire mark, Menu button, Sign in.', sel: 'mobile header' }, { noScroll: true });
  await S('m-menu-btn', q('button[aria-label*="Menu" i], header button').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The header Menu button that opens the nav drawer — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile Menu button' }, { noScroll: true, allowLink: true, before: { opened: async (loc) => openMobileMenu().then((v) => { void loc; return v; }) } });
  await S('m-drawer', q('[role="dialog"], body > div[class*="drawer" i]').filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav drawer', desc: 'The nav drawer opened by the Menu button; its links were never followed.', sel: 'mobile nav drawer' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  const searchBtn = q('header button:not([aria-label])').filter({ hasNotText: /Sign in|buy/i }).filter({ visible: true }).first();
  await S('m-search-btn', searchBtn, B4, { group: g, title: 'Mobile search button', desc: 'The unlabelled magnifier icon button in the phone header; measured at rest (opening the search overlay is covered by m-search).', sel: 'mobile search icon button' }, { noScroll: true });
  await S('m-search', q('input[name="vendor-search-handler"], input[type="search"], input[placeholder*="Search" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Mobile search field', desc: 'The search field inside the overlay the magnifier button opens (a local UI toggle); focused and typed into then cleared — nothing searched.', sel: 'mobile search input' }, { fillText: 'candles', open: async () => { await searchBtn.click({ timeout: 4000 }).catch(() => searchBtn.evaluate((el) => el.click())); await page.waitForTimeout(1200); }, noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); faire.com paints one light theme with no theme attribute or user toggle';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = {
  home, category, brand, suppliers, suppliersAll, apply, signin, signup, support, notfound: () => {},
  howItWorks: () => marketing('howItWorks', 'hw-h1', 'hw-cta', null, 'How Faire works headline', /sign up|get started|learn|contact/i),
  about: () => marketing('about', 'about-h1', 'about-cta', null, 'About headline', /sign up|get started|learn|join/i),
  news: () => marketing('news', 'news-h1', 'news-cta', 'news-card', 'Newsroom headline', /read|story|press|subscribe|sign up/i),
  careers: () => marketing('careers', 'careers-h1', 'careers-cta', null, 'Careers headline', /open roles|jobs|apply|sign up|see/i),
  largeRetailers: () => marketing('largeRetailers', 'lr-h1', 'lr-cta', null, 'Large retailers headline', /contact|demo|sign up|get started|learn/i),
  pos: () => marketing('pos', 'pos-h1', 'pos-cta', null, 'Point of sale headline', /sign up|get started|learn|buy/i),
  markets: () => marketing('markets', 'markets-h1', 'markets-cta', null, 'Faire Markets headline', /register|sign up|get started|learn/i),
  affiliates: () => marketing('affiliates', 'aff-h1', 'aff-cta', null, 'Affiliates headline', /apply|sign up|join|get started/i),
  mobile,
};
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (an fs-button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header .fs-button--primary, button.fs-button--primary');
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
