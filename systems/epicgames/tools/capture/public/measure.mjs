// Measures epicgames.com's public components in every state reachable without
// signing in, buying, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: discover browse product freegames news download signin sitehome help mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// epicgames.com paints one theme — dark — across three generations of the
// public surface: the egs-v2 storefront (store.epicgames.com Discover, product
// pages, free-games, news, download — hashed eds_370_* tokens, Inter), the
// legacy emotion-styled browse grid (css-* classes, a real filters rail and
// sort dropdown), the www.epicgames.com OpenSans marketing page, the dark
// /help support centre and the MUI /id/login dialog. The global nav and
// footer are <egs-navigation>/<egs-footer> web components — Playwright
// locators pierce their open shadow roots. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the Genre filter accordion,
// the New Release sort dropdown, the mobile hamburger — and the two search
// fields are typed into and cleared, never submitted. Get, Add to Cart,
// Wishlist, Sign in, Download and Continue are measured, never pressed or
// followed. Cloudflare challenges fresh contexts at random; newPage retries
// on a fresh context, never clicks the check.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, WWW, M, launch, patch, open, closePromo, clearChallenge, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, LAUNCH_ARGS, chromium } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  discover: '/en-US/', browse: '/en-US/browse', product: '/en-US/p/fortnite',
  freegames: '/en-US/free-games', news: '/en-US/news', download: '/en-US/download',
  signin: WWW + '/id/login/epic', sitehome: WWW + '/site/en-US/home', help: WWW + '/help/en-US/',
  mobile: '/en-US/',
};
let page, cdp, current, browser, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes Cloudflare gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
const failedPages = new Set();
// Pages whose function ran to the end this run: only their components may
// lose states a spec no longer lists (a crash mid-page must not prune).
const completedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|complete a security check/i.test(t) || document.title === 'Just a moment...' || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const u = url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]);
  let ctx = null;
  for (let i = 0; i < 4 && !ctx; i++) {
    const c = await browser.newContext(mobile
      ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
      : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(c);
    const p = await c.newPage();
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (await clearChallenge(p, { tries: 6, step: 1800 })) { ctx = c; page = p; break; }
    await c.close();
  }
  if (!ctx) { log('open', key, 'BLOCKED'); failedPages.add(key); return false; }
  liveCtx = ctx;
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const seen = [];
    const walk = (root) => {
      for (const el of root.querySelectorAll('*')) {
        if (el.shadowRoot) walk(el.shadowRoot);
        const cs = getComputedStyle(el);
        if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
        const r = el.getBoundingClientRect();
        if (r.width < 40 || r.height < 10) continue;
        seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
      }
    };
    walk(document);
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
  // The global nav lives inside <egs-navigation>'s shadow root, where
  // document.activeElement is the host: ask the element itself (:focus,
  // :focus-within), as the dock base this fork came from does.
  const hasFocus = (el) => el.matches(':focus') || el.matches(':focus-within')
    || el === document.activeElement || el.contains(document.activeElement);
  let ok = await loc.evaluate(hasFocus);
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate(hasFocus);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  // Clear stale markers inside shadow roots too, then mark the target.
  await page.evaluate(() => {
    const clear = (r) => { r.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')); for (const e of r.querySelectorAll('*')) if (e.shadowRoot) clear(e.shadowRoot); };
    clear(document);
  });
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  // DOM.querySelector never pierces shadow roots, so the flattened document is
  // walked to find the marker — pierce:true also exposes shadowRoots, which is
  // how the nav buttons inside <egs-navigation> get a real nodeId.
  const { root } = await cdp.send('DOM.getDocument', { depth: -1, pierce: true });
  const find = (n) => {
    if (n.attributes) for (let i = 0; i < n.attributes.length; i += 2) if (n.attributes[i] === 'data-m-force') return n.nodeId;
    for (const c of n.children || []) { const r = find(c); if (r) return r; }
    for (const s of n.shadowRoots || []) { const r = find(s); if (r) return r; }
    return 0;
  };
  const nodeId = find(root);
  if (!nodeId) throw new Error('forcePseudo: node not found');
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
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be
        // the element at rest saved as its focus. Record the miss instead and
        // drop the crop an earlier run saved for this state (the kit's branch).
        const prev = out.components[key].states[st];
        const old = prev?.crop && path.resolve(RAW, '..', prev.crop);
        const crops = path.resolve(RAW, '..', 'components', 'crops');
        if (old && old.startsWith(crops + path.sep)) fs.rmSync(old, { force: true });
        out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via };
        log('  -', key, st, 'skipped: focus failed');
      } else await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, accordion trigger). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|continue|create|create an account|add|add to cart|add to wishlist|download|buy|buy now|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get|get started|claim|claim now|install|share|export|select|try again|redeem|gift)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

// Marks the widest visible element matching `sel` (a page can carry a hidden
// duplicate input for another breakpoint — the widest painted one is the
// target) and returns a locator for it.
async function widest(sel, { tag = 'w', minW = 60, minH = 6, text = null, pick = 'max' } = {}) {
  const ok = await page.evaluate(([s, t, w, h, re, pickMode]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const rx = re ? new RegExp(re, 'i') : null;
    const els = [...document.querySelectorAll(s)].filter((n) => {
      if (rx && !rx.test(n.innerText || n.textContent || n.getAttribute('aria-label') || '')) return false;
      const r = n.getBoundingClientRect();
      const cs = getComputedStyle(n);
      return r.width >= w && r.height >= h && cs.visibility !== 'hidden' && cs.opacity !== '0' && cs.display !== 'none';
    }).sort((a, b) => pickMode === 'min'
      ? a.getBoundingClientRect().width - b.getBoundingClientRect().width
      : b.getBoundingClientRect().width - a.getBoundingClientRect().width);
    if (!els.length) return false;
    els[0].setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, minW, minH, text, pick]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
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
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    for (let t = 0; t < 8; t++) { if (!/just a moment/i.test(await p.title())) break; await p.waitForTimeout(2000); }
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
  nav: 'Global navigation', shell: 'Store shell', discover: 'Discover', browse: 'Browse (legacy grid)',
  product: 'Product page', freegames: 'Free games', news: 'News', download: 'Launcher download',
  signin: 'Sign-in dialog', sitehome: 'Marketing home', help: 'Support centre', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// The Discover search box: focused, typed into for its suggestion layer and
// cleared — never submitted (no Enter; typed last on the page anyway).
async function searchFocus() {
  const f = q('input[placeholder*="earch" i], input[type="search"]').filter({ visible: true }).first();
  await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
  await page.waitForTimeout(400);
  return 'clicked into the search field';
}

// The legacy browse page's Genre accordion header opens its checkbox group —
// a local UI toggle.
async function openGenre() {
  // Idempotent: the previous entry may have left the group open; only toggle
  // when no checkbox row is painted inside the rail yet.
  // The checkbox inputs are visually hidden, so detect the open group by the
  // expanded accordion button or by checkbox rows already painted.
  const expanded = await q('aside button[aria-expanded="true"], aside [class*="accordion" i] [aria-expanded="true"]').filter({ hasText: /genre/i }).first().isVisible().catch(() => false);
  const rows = await q('aside label:has(input[type="checkbox"]), aside [role="checkbox"]:visible').count().catch(() => 0);
  if (expanded || rows > 0) return 'Genre group already open';
  const b = q('button').filter({ hasText: /^\s*Genre\s*$/ }).filter({ visible: true }).first();
  if (!(await b.count())) return 'no Genre accordion';
  await toggle(b);
  await page.waitForTimeout(900);
  return 'clicked Genre to open the filter group';
}

// The New Release sort control opens a listbox of sort options — a local UI
// toggle; an option is never picked.
async function openSort() {
  // The nav bar also renders <li role="menuitem"> items (e.g. "News"), so the
  // open check must look for the sort options' own texts.
  const open = await q('[role="menuitem"], [role="option"], [role="menuitemradio"]').filter({ hasText: /new release|alphabetical|relevance|price|release date/i }).filter({ visible: true }).first().isVisible().catch(() => false);
  if (open) return 'sort menu already open';
  const b = q('button, [role="combobox"]').filter({ hasText: /new release|sort|alphabetical|price/i }).filter({ visible: true }).first();
  if (!(await b.count())) return 'no sort control';
  await toggle(b);
  await page.waitForTimeout(900);
  return 'clicked the sort control to open the options';
}

async function discover() {
  if (!(await newPage('discover'))) return;
  await sheetsFor('discover');
  await chrome('discover');
  const nav = G.nav;
  await S('egs-nav', q('egs-navigation').first(), ['default'], { group: nav, title: 'Global nav', desc: 'The <egs-navigation> web component over every store page: Epic Games mark, STORE, Support, Distribute, the globe locale picker, Sign in and the blue Download pill. Shadow-DOM host; children measured through it.', sel: 'egs-navigation' }, { noScroll: true, pad: 4 });
  await S('nav-signin', q('button, a').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: nav, title: 'Sign in button', desc: 'The dark Sign-in pill in the global nav; links to the sign-in flow, measured never followed.', sel: 'nav Sign in' }, { noScroll: true });
  await S('nav-download', q('button, a').filter({ hasText: /^\s*Download\s*$/i }).filter({ visible: true }).first(), B4, { group: nav, title: 'Download button', desc: 'The blue Download pill in the global nav; measured never followed.', sel: 'nav Download' }, { noScroll: true });
  await S('nav-distribute', q('button, a').filter({ hasText: /^\s*Distribute\s*$/i }).filter({ visible: true }).first(), B4, { group: nav, title: 'Distribute menu', desc: 'The Distribute dropdown in the global nav; measured, never opened.', sel: 'nav Distribute' }, { noScroll: true });
  await S('nav-locale', q('button[aria-label*="language" i], button[aria-label*="region" i], button[aria-label*="locale" i], button[aria-label*="English" i]').filter({ visible: true }).first(), B4, { group: nav, title: 'Locale button', desc: 'The globe locale picker in the global nav; measured, never opened.', sel: 'nav globe' }, { noScroll: true });
  const sh = G.shell;
  await S('store-tabs', q('nav[class*="topNav" i], nav:has(a:text-is("Discover"))').filter({ visible: true }).first(), ['default'], { group: sh, title: 'Store tab bar', desc: 'The second bar under the global nav: search field plus Discover/Browse/News.', sel: 'nav._topNav' }, { noScroll: true });
  await S('store-tab', q('a[class*="navLink" i]').filter({ hasText: /^\s*Discover\s*$/ }).filter({ visible: true }).first(), B4, { group: sh, title: 'Store tab', desc: 'The active "Discover" tab link; measured, never followed.', sel: 'a.navLink Discover' }, { noScroll: true });
  const d = G.discover;
  await S('hero-slide', q('a[class*="slideLink" i]').filter({ visible: true }).first(), ['default'], { group: d, title: 'Hero slide', desc: 'The giant carousel slide (art + promo copy + Save Now) on Discover; measured, never followed.', sel: 'a.slideLink' }, { noScroll: true });
  await S('hero-cta', q('button, a').filter({ hasText: /^\s*Save Now\s*$/i }).filter({ visible: true }).first(), B4, { group: d, title: 'Hero CTA', desc: 'The white "Save Now" pill on the hero slide; measured, never followed.', sel: 'hero Save Now' }, { noScroll: true });
  await S('carousel-thumb', q('button[class*="carouselButton" i], a[class*="carouselButton" i]').filter({ visible: true }).first(), B4, { group: d, title: 'Carousel rail item', desc: 'A thumbnail button in the hero carousel rail ("Go to slide N"); measured, its own slide state pressed by hover only.', sel: 'button.carouselButton' }, { noScroll: true });
  await S('pager-next', q('button[aria-label="Next page"]').filter({ visible: true }).first(), B4, { group: d, title: 'Carousel pager', desc: 'The right-chevron "Next page" rail control under a card shelf.', sel: 'button[aria-label="Next page"]' });
  await S('game-card', q('a[class*="cardLink" i]').filter({ visible: true }).first(), B4, { group: d, title: 'Game card', desc: 'A store card (cover, title, price line, wishlist corner) in a Discover shelf; measured, never followed.', sel: 'a.cardLink' });
  await S('card-price', await domFind(page, /SGD [\d.]+|Free|Coming Soon/, { sel: 'span, div, p', tag: 'price', minW: 20, minH: 8 }), ['default'], { group: d, title: 'Price line', desc: 'The price/Free/Coming-Soon line inside a game card (region-priced, SGD on this run).', sel: 'card price span' });
  await S('card-wishlist', q('button[aria-label*="wishlist" i]').filter({ visible: true }).first(), B4, { group: d, title: 'Card wishlist button', desc: 'The plus-corner "Add … to wishlist" icon button on a card; measured, never toggled.', sel: 'button[aria-label*="wishlist"]' });
  await S('view-more', q('button, a').filter({ hasText: /^\s*View More\s*$/i }).filter({ visible: true }).first(), B4, { group: d, title: 'View More', desc: 'The shelf "View More" ghost button; measured, never followed.', sel: 'View More' });
  const f = G.footer;
  await S('egs-footer', q('egs-footer, footer').filter({ visible: true }).last(), ['default'], { group: f, title: 'Global footer', desc: 'The <egs-footer> web component at the bottom of every store page.', sel: 'egs-footer' }, { noScroll: true });
  // The search field is measured last: typing may open a results layer.
  await S('search-field', await widest('input', { tag: 'sf', minW: 100 }), FIELD, { group: sh, title: 'Search field', desc: 'The "Search store" field in the store tab bar; focused and typed into then cleared — never submitted.', sel: 'store search input' }, { noScroll: true, fillText: 'fort' });
  save();
}

async function browse() {
  if (!(await newPage('browse'))) return;
  await sheetsFor('browse');
  await chrome('browse');
  const b = G.browse;
  await S('b-h1', await widest('h1', { tag: 'bh', minW: 80, minH: 20 }), ['default'], { group: b, title: 'Browse heading', desc: '"Popular Genres" — the display heading on the legacy browse page (a second "Browse" h1 is screen-reader-only).', sel: 'h1 Popular Genres' }, { noScroll: true });
  await S('b-genre-card', q('a').filter({ hasText: /^\s*Action Games\s*$/ }).filter({ visible: true }).first(), B4, { group: b, title: 'Genre card', desc: 'A "Popular Genres" tile (art + label) linking to a filtered browse; measured, never followed.', sel: 'a genre tile' }, { noScroll: true });
  await S('b-sort', q('button, [role="combobox"]').filter({ hasText: /new release|alphabetical|price|sort/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: b, title: 'Sort dropdown', desc: 'The "New Release" sort control above the grid; opened with its own toggle for the listbox state — an option was never picked.', sel: 'sort button' }, { noScroll: true });
  await S('b-sort-item', q('[role="menuitem"], [role="option"], [role="menuitemradio"]').filter({ hasText: /new release|alphabetical|price|relevance|release/i }).filter({ visible: true }).first(), ['default'], { group: b, title: 'Sort option', desc: 'An option inside the opened sort menu (button[role=menuitem]); measured, never picked.', sel: 'sort menuitem' }, { open: openSort, noScroll: true, noReset: true });
  await S('b-card', q('a').filter({ hasText: /SGD|USD|Free|Coming Soon/i }).filter({ visible: true }).nth(2), B4, { group: b, title: 'Grid game card', desc: 'A game card in the legacy browse grid (cover, title, price, wishlist corner); measured, never followed.', sel: 'browse grid card' });
  await S('b-wishlist', q('button[aria-label="Add to Wishlist"]').filter({ visible: true }).first(), B4, { group: b, title: 'Grid wishlist button', desc: 'The "Add to Wishlist" corner button on a grid card; measured, never toggled.', sel: 'button[aria-label="Add to Wishlist"]' });
  await S('b-filters', q('aside').filter({ hasText: /filters/i }).filter({ visible: true }).first(), ['default'], { group: b, title: 'Filters rail', desc: 'The right-hand Filters aside: Events/Genre/Features/Types/Platform/Subscriptions accordions over a filter search.', sel: 'aside Filters' }, { noScroll: true });
  await S('b-filter-group', q('button').filter({ hasText: /^\s*Genre\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: b, title: 'Filter accordion', desc: 'The "Genre" collapsible in the Filters rail; opened with its own toggle for the checkbox group — nothing was checked.', sel: 'Genre accordion button' }, { noScroll: true });
  // widest() marks its element immediately, so the group must be open first;
  // S's own open:openGenre then sees it open and leaves it alone.
  await openGenre();
  await S('b-checkbox', await widest('aside div', { tag: 'cbx', minW: 80, minH: 15, text: 'action', pick: 'min' }), ['default'], { group: b, title: 'Filter checkbox', desc: 'A checkbox row inside the opened Genre group (the control is a styled div, the input is visually hidden); never checked.', sel: 'genre checkbox row' }, { open: openGenre, noScroll: true, noReset: true });
  await S('b-filter-search', q('aside input').filter({ visible: true }).first(), ['default', 'focused'], { group: b, title: 'Filter search', desc: 'The "Filters" keyword field at the top of the rail; focused, never submitted.', sel: 'filters input' }, { noScroll: true });
  await S('b-pagination', q('nav[aria-label*="pagination" i]').filter({ visible: true }).first(), ['default'], { group: b, title: 'Pagination', desc: 'The numbered pagination under the grid.', sel: 'pagination nav' });
  await S('b-page-link', q('nav[aria-label*="pagination" i] a, nav[aria-label*="pagination" i] button').filter({ visible: true }).first(), B4, { group: b, title: 'Page number', desc: 'A page number inside the pagination; measured, never followed.', sel: 'pagination item' });
  save();
}

async function product() {
  if (!(await newPage('product'))) return;
  await sheetsFor('product');
  await chrome('product');
  const p = G.product;
  await S('p-title', q('h1').filter({ visible: true }).first(), ['default'], { group: p, title: 'Product title', desc: 'The game title heading (Fortnite) at the top of the product page.', sel: 'product h1' }, { noScroll: true });
  await S('p-rating', await domFind(page, /competitive players|quickly understood|4\.\d/, { sel: 'div, section', tag: 'rating', minW: 100, minH: 20 }), ['default'], { group: p, title: 'Rating block', desc: 'The "4.3" Epic Player Ratings strip with its audience descriptors.', sel: 'rating block' }, { noScroll: true });
  await S('p-subnav', q('ul[class*="subnav" i] a, ul[class*="subnav" i] li').filter({ hasText: /^\s*Overview\s*$/ }).filter({ visible: true }).first(), B4, { group: p, title: 'Product tab', desc: 'The active "Overview" tab in the product subnav (Overview/Add-Ons/Experiences/FAQ); measured, never followed.', sel: 'subnav Overview' }, { noScroll: true });
  await S('p-stage-next', q('button[aria-label="Next image"]').filter({ visible: true }).first(), B4, { group: p, title: 'Gallery arrow', desc: 'The right "Next image" arrow over the media stage; measured, never pressed.', sel: 'button[aria-label="Next image"]' });
  await S('p-thumb', q('button[class*="thumbnail" i]').filter({ visible: true }).first(), ['default'], { group: p, title: 'Gallery thumbnail', desc: 'A thumbnail button in the media strip ("Slide N of 9"); measured, never pressed.', sel: 'button.thumbnail' });
  await S('p-get', q('button').filter({ hasText: /^\s*Get\s*$/ }).filter({ visible: true }).first(), B4, { group: p, title: 'Get button', desc: 'The blue "Get" primary action in the buy panel; measured, never pressed.', sel: 'buy panel Get' }, { noScroll: true });
  await S('p-cart', q('button').filter({ hasText: /^\s*Add to Cart\s*$/i }).filter({ visible: true }).first(), B4, { group: p, title: 'Add to Cart', desc: 'The square "Add to Cart" icon button beside Get; measured, never pressed.', sel: 'buy panel Add to Cart' }, { noScroll: true });
  await S('p-wishlist', q('button').filter({ hasText: /^\s*Wishlist\s*$/i }).filter({ visible: true }).first(), B4, { group: p, title: 'Wishlist button', desc: 'The outlined "Wishlist" button under the buy panel; measured, never pressed.', sel: 'buy panel Wishlist' }, { noScroll: true });
  await S('p-price', await domFind(page, /^\s*(Free|SGD [\d.]+)\s*$/, { sel: 'div, span', tag: 'pprice', minW: 20, minH: 10 }), ['default'], { group: p, title: 'Buy price', desc: 'The "Free"/price line above the buy actions.', sel: 'buy price' }, { noScroll: true });
  await S('p-share', q('button').filter({ hasText: /^\s*Share\s*$/ }).filter({ visible: true }).first(), B4, { group: p, title: 'Share button', desc: 'The "Share" ghost button beside Report in the buy rail; measured, never pressed.', sel: 'buy rail Share' }, { noScroll: true });
  await S('p-tag', q('a').filter({ hasText: /^\s*(Action|Shooter|Co-op|Competitive|Multiplayer|Single Player)\s*$/ }).filter({ visible: true }).first(), B4, { group: p, title: 'Tag chip', desc: 'A genre tag chip under the description; links to a filtered browse, measured never followed.', sel: 'tag chip' });
  await S('p-ratings-badge', q('a[href*="globalratings" i], a[href*="esrb" i], a[href*="pegi" i]').filter({ visible: true }).first(), B4, { group: p, title: 'Ratings badge', desc: 'The age-ratings badge link (globalratings.com); measured, never followed.', sel: 'ratings badge link' });
  await S('p-h2', q('h2').filter({ hasText: /experiences|everything you love|add-ons/i }).filter({ visible: true }).first(), ['default'], { group: p, title: 'Section heading', desc: 'A section heading inside the product overview.', sel: 'product h2' });
  await S('p-addon-row', q('a').filter({ hasText: /fortnite reload|lego|festival|quest pack|v-bucks/i }).filter({ visible: true }).first().locator('xpath=ancestor-or-self::*[self::li or self::div][1]'), ['default', 'hover'], { group: p, title: 'Add-on row', desc: 'An Add-Ons/Experiences row (art, title, Add-to-Cart, wishlist); measured, never followed.', sel: 'add-on row' });
  await S('p-sysreq-tab', q('button').filter({ hasText: /^\s*(Windows|Mac)\s*$/ }).filter({ visible: true }).first(), B4, { group: p, title: 'Requirements tab', desc: 'A platform tab in System Requirements; measured, never switched.', sel: 'sysreq tab' });
  await S('p-follow', q('a[aria-label*="follow" i], a[aria-label*="discord" i], a[aria-label*="homepage" i]').filter({ visible: true }).first(), B4, { group: p, title: 'Follow icon', desc: 'A social icon link in Follow Us (Discord/homepage); measured, never followed.', sel: 'follow icon link' });
  save();
}

async function freegames() {
  if (!(await newPage('freegames'))) return;
  await sheetsFor('freegames');
  await chrome('freegames');
  const f = G.freegames;
  await S('fg-h1', await widest('h1, h2', { tag: 'fgh', minW: 60, minH: 16 }), ['default'], { group: f, title: 'Free Games heading', desc: 'The "Free Games" display heading (the h1 itself is screen-reader-only).', sel: 'free-games heading' }, { noScroll: true });
  await S('fg-cta', q('a, button').filter({ hasText: /install mobile|claim now/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Giveaway CTA', desc: 'The blue "Install Mobile and Claim Now" action in the Free Giveaway panel; links out to the mobile app, measured never followed.', sel: 'free giveaway CTA' });
  await S('fg-card', await widest('div, a', { tag: 'fgc', minW: 300, minH: 250, text: 'free now|coming soon', pick: 'min' }), B4, { group: f, title: 'Free game card', desc: 'A "Free Now"/"Coming Soon" game card on the free-games shelf; measured, never followed.', sel: 'free-games card' });
  await S('fg-badge', await domFind(page, /free now\s*[-–—]|coming soon/i, { sel: 'span, div, p', tag: 'fgb', minW: 30, minH: 10 }), ['default'], { group: f, title: 'Free-now badge', desc: 'The "Free Now - <date>" status label on a free-games card.', sel: 'Free Now badge' });
  save();
}

async function news() {
  if (!(await newPage('news'))) return;
  await sheetsFor('news');
  const n = G.news;
  await S('n-h1', q('h1, h2').filter({ hasText: /news/i }).filter({ visible: true }).first(), ['default'], { group: n, title: 'News heading', desc: 'The "Epic Games News" heading.', sel: 'news heading' }, { noScroll: true });
  await S('n-card', await widest('div, article, li', { tag: 'nc', minW: 400, minH: 300, text: '\\d+d?\\s*ago', pick: 'min' }), B4, { group: n, title: 'Article card', desc: 'A news article card (hero image, "Nd ago", headline, Read more); measured, never followed.', sel: 'news article card' });
  await S('n-readmore', q('a, span, div').filter({ hasText: /^\s*Read more\s*$/i }).filter({ visible: true }).first(), B4, { group: n, title: 'Read more link', desc: 'The "Read more" caption link inside an article card; measured, never followed.', sel: 'Read more' });
  save();
}

async function download() {
  if (!(await newPage('download'))) return;
  await sheetsFor('download');
  const d = G.download;
  await S('d-h1', await widest('h1, h2', { tag: 'dh', minW: 60, minH: 16 }), ['default'], { group: d, title: 'Download heading', desc: 'The "Download the Epic Games Launcher" heading (the h1 itself is screen-reader-only).', sel: 'download heading' }, { noScroll: true });
  await S('d-cta', await widest('a, button', { tag: 'dcta', minW: 60, minH: 16, text: 'windows|mac|download' }), B4, { group: d, title: 'Download CTA', desc: 'The launcher download action (Windows/Mac); measured, never followed.', sel: 'download CTA' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 9000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const s = G.signin;
  await S('s-dialog', q('[class*="MuiPaper" i], [role="dialog"] > div').filter({ hasText: /sign in/i }).filter({ visible: true }).last(), ['default'], { group: s, title: 'Sign-in dialog', desc: 'The "Sign in to Epic Games" MUI modal (the MuiPaper card): Epic mark, e-mail field, Continue, console and social providers. Measured as a form, never submitted.', sel: 'signin MuiPaper' }, { noScroll: true });
  await S('s-title', q('h1, h2, [class*="title" i]').filter({ hasText: /sign in to epic games/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Sign-in title', desc: '"Sign in to Epic Games" in the dialog.', sel: 'signin title' }, { noScroll: true });
  await S('s-field-email', q('input[type="email"], input[name*="mail" i], input[autocomplete*="mail" i], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: s, title: 'Email field', desc: 'The "Email address" input; focused and typed into then cleared — never submitted.', sel: 'signin email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('s-continue', q('button').filter({ hasText: /^\s*Continue\s*$/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Continue button', desc: 'The blue "Continue" submit; its states were measured but it was never clicked — nothing was submitted.', sel: 'signin Continue' }, { noScroll: true });
  await S('s-create', q('a, button').filter({ hasText: /create an account/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Create-account link', desc: 'The "Create an account" link; measured, never followed.', sel: 'signin Create an account' }, { noScroll: true });
  await S('s-console', q('[role="button"], button, a').filter({ hasText: /playstation|xbox|nintendo/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Console provider', desc: 'A console sign-in tile (PlayStation/Xbox/Nintendo, MuiListItemButton divs); measured, never followed.', sel: 'console provider tile' }, { noScroll: true });
  await S('s-social', q('[role="button"], button, a').filter({ hasText: /^\s*(google|steam|disney|sign in with apple|facebook|lego)/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Social provider', desc: 'A "Other ways to sign in" provider tile (Google/Steam/Disney/Apple/Facebook/LEGO); measured, never followed.', sel: 'social provider tile' }, { noScroll: true });
  save();
}

async function sitehome() {
  if (!(await newPage('sitehome'))) return;
  await sheetsFor('sitehome');
  const w = G.sitehome;
  // Mark one tile before S(): the carousel rotates, and a locator that
  // re-resolves per state read a different product tile in each state.
  await q('a, div').filter({ hasText: /^\s*(UNREAL\s*ENGINE|FORTNITE|ROCKET\s*LEAGUE|STORE|ROBO\s*RECALL|UNREAL\s*TOURNAMENT)\s*EXPLORE\s*$/i }).filter({ visible: true }).first()
    .evaluate((el) => el.setAttribute('data-m', 'w-tile')).catch(() => {});
  await S('w-tile', q('[data-m="w-tile"]'), B4, { group: w, title: 'Product tile', desc: 'A giant product tile (UNREAL ENGINE / FORTNITE / ROCKET LEAGUE / STORE) with its EXPLORE action on the OpenSans marketing home; measured, never followed.', sel: 'marketing tile' });
  await S('w-explore', q('a, button, span').filter({ hasText: /^\s*EXPLORE\s*$/i }).filter({ visible: true }).first(), B4, { group: w, title: 'Explore link', desc: 'The EXPLORE caption on a product tile; measured, never followed.', sel: 'EXPLORE' });
  save();
}

async function help() {
  if (!(await newPage('help', { wait: 12000 }))) return;
  await sheetsFor('help');
  await chrome('help');
  const h = G.help;
  await S('h-h1', q('h1, h2').filter({ hasText: /how can we help/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Help heading', desc: '"How can we help?" on the dark support centre.', sel: 'help h1' }, { noScroll: true });
  await S('h-search', await widest('input', { tag: 'hs', minW: 200 }), FIELD, { group: h, title: 'Support search', desc: 'The "Search support..." field; focused and typed into then cleared — never submitted.', sel: 'help search input' }, { noScroll: true, fillText: 'refund' });
  await S('h-tile', q('a[class*="Tile" i], a[class*="GoToTile" i]').filter({ hasText: /self-service|explore topics|enterprise/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Help tile', desc: 'A support-category tile (Self-service/Explore topics/Games/Enterprise, a.Tile); measured, never followed.', sel: 'help a.Tile' });
  await S('h-status', await domFind(page, /server status/i, { sel: 'div, a, span', tag: 'hst', minW: 60, minH: 10 }), ['default'], { group: h, title: 'Server status chip', desc: 'The "Server status" indicator, top right; measured never followed.', sel: 'server status' }, { noScroll: true });
  // Not `button:has(svg)`: with .last() it caught the "Back to top" button.
  await S('h-chat', q('button[aria-label*="chat" i], button[aria-label*="help" i], [class*="chat" i] button').filter({ hasNotText: /back to top/i }).filter({ visible: true }).last(), B4, { group: h, title: 'Chat launcher', desc: 'The round chat button bottom right; measured, never pressed.', sel: 'chat bubble' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/en-US/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  const sh = G.nav;
  await S('m-egs-nav', q('egs-navigation').first(), ['default'], { group: sh, title: 'Global nav (mobile)', desc: 'The <egs-navigation> at 390px.', sel: 'egs-navigation (390)' }, { noScroll: true, pad: 4 });
  // Not `button:has(svg)` or the ecosystem switcher: the union caught the
  // "Epic Ecosystem Dropdown" button first.
  await S('m-hamburger', q('button[aria-label*="menu" i]:not([aria-label*="ecosystem" i]), button[aria-label*="navigation" i]:not([aria-label*="ecosystem" i])').filter({ hasNotText: /ecosystem/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Hamburger', desc: 'The mobile menu button; measured, the drawer itself is captured in screenshots.', sel: 'mobile menu button' }, { noScroll: true });
  await S('m-hero', q('a[class*="slideLink" i], a[class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero card', desc: 'The first card of the mobile store home.', sel: 'mobile first card' }, { noScroll: true });
  await S('m-card', q('a').filter({ hasText: /SGD|Free|Coming Soon/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile game card', desc: 'A game card on the mobile discover feed.', sel: 'mobile card' });
  await S('m-search', await widest('input', { tag: 'ms', minW: 80 }), FIELD, { group: g, title: 'Mobile search', desc: 'The mobile search field; focused and typed into then cleared — never submitted.', sel: 'mobile search input' }, { noScroll: true, fillText: 'fort' });
  save();
}

const ALL = { discover, browse, product, freegames, news, download, signin, sitehome, help, mobile };
const wanted = process.argv.slice(2);
const unknown = wanted.filter((k) => !(k in ALL));
if (unknown.length) {
  console.error(`unknown page argument(s): ${unknown.join(', ')} — known pages: ${Object.keys(ALL).join(', ')}`);
  process.exit(1);
}
run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); dark is the only painted public theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.product = 'epicgames.com';
out._meta.note = 'public signed-out capture; nothing bought, submitted or signed into';
browser = await chromium.launch({ args: LAUNCH_ARGS });
for (const k of Object.keys(ALL)) {
  if (wanted.length && !wanted.includes(k)) continue;
  try { await ALL[k](); if (!failedPages.has(k)) completedPages.add(k); } catch (e) { log('PAGE FAILED', k, String(e.message).slice(0, 140)); }
}
await reducedMotion('discover', 'a[class*="slideLink" i]');
await reducedMotion('product', 'button');
// Prune components whose page failed and which this run never touched —
// blocked runs must not erase last run's evidence, so only untouched keys
// from pages that actually loaded get removed.
for (const [k, c] of Object.entries(out.components)) {
  if (!touched.has(k) && !failedPages.has(c.page) && c.page && URLS[c.page]) {
    if (!wanted.length || wanted.includes(c.page)) {
      delete out.components[k];
      continue;
    }
  }
  // States a spec no longer lists are pruned only after their page finished
  // this run, so a blocked or partial run never drops evidence.
  const want = listed.get(k);
  if (want && touched.has(k) && completedPages.has(c.page)) {
    for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
}
save();
log('done:', Object.keys(out.components).length, 'components;', failedPages.size ? `blocked: ${[...failedPages].join(',')}` : 'no blocked pages');
await browser.close();
