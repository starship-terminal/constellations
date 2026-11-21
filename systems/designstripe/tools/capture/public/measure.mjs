// Measures visual.app's (formerly designstripe) public components in every
// state reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home assets avatars tools contact post mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// visual.app is a single light theme signed out: the marketing home, the
// public /assets library and /assets/<kind>/<set> galleries, /tools, /about,
// /contact and /blog articles. Classes are Tailwind utilities, so specs
// select by role, aria-label, structure or text. Nothing is sent or signed
// into: the only presses are local UI toggles — the home feature accordion —
// and the waitlist buttons, nav links, asset tiles and tool cards are
// measured, never followed. No consent overlay was seen.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', assets: '/assets', avatars: '/assets/avatars/replicants', tools: '/tools', contact: '/contact', post: '/blog/branding-consistency', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
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
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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

// A failed re-read must not erase an earlier successful one: keep the saved
// style and record the failed attempt beside it. comp() has already stamped
// this run's date on the component, so the kept state is pinned to the run
// that actually read it (its own run stamp, else the component's earlier run)
// and an old reading is never republished as a new one.
function keepEarlier(c, state, e, earlierRun) {
  const err = String(e.message || e).slice(0, 200);
  const prev = c.states[state];
  if (prev && prev.style) {
    // A state that already carried a rerunError before read was recorded is
    // from an unknown earlier run: its date stays unknown (null), never the
    // component's date, which a failed re-read had already advanced.
    if (prev.read === undefined) prev.read = prev.rerunError ? null : (prev.run || earlierRun);
    prev.rerunError = err;
    prev.rerunOn = run;
  } else c.states[state] = { error: err };
}

async function measure(key, state, target, opts = {}) {
  const loc = target.and(page.locator(':visible')).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    keepEarlier(c, state, e, opts.earlierRun);
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
  const loc = target.and(page.locator(':visible')).first();
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
        await (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).and(page.locator(':visible')).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).and(page.locator(':visible')).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'sample text', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'sample text'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        // noToggle: the state is read as it already paints; openedVia says why
        // it is open (an earlier toggle, or open at rest), so the record never
        // claims an interaction that did not run.
        if (opts.noToggle) via = opts.openedVia || 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          undo = () => closeOpened(key, loc, opts);
        }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, earlierRun: keep?.run });
    } catch (e) {
      keepEarlier(out.components[key], st, e, keep?.run);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Closes what an `opened` state opened. An open dropdown or menu keeps focus
// and covers the page, so every later focus-visible reading would come back
// 'focus failed'. Escape first, then the trigger again; if the trigger still
// reports aria-expanded="true" the miss is recorded on the opened state so
// the later readings on this page can be checked.
async function closeOpened(key, loc, opts) {
  const expanded = () => loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  if ((await expanded()) === 'true') { await toggle(loc, { allowLink: opts.allowLink }).catch(() => {}); await page.waitForTimeout(600); }
  if ((await expanded()) === 'true') {
    const st = out.components[key].states.opened;
    if (st) st.closeFailed = 'aria-expanded still "true" after Escape and a second toggle';
    log('  ! opened state did not close', key);
  }
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.and(page.locator(':visible')).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
// Elements inside scroll-driven reveals flicker in and out of :visible while
// the reveal animates; giving the page a beat after centre() lets the locator
// resolve the painted element instead of the pre-reveal one.
const settle = () => page.waitForTimeout(1500);
const SETTLE = { hover: settle, 'focus-visible': settle, pressed: settle, opened: settle, filled: settle, focused: settle };

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
  shell: 'Header and navigation', home: 'Home', assets: 'Asset library',
  avatars: 'Avatar set gallery', tools: 'Design tools', contact: 'Contact',
  post: 'Blog article', mobile: 'Mobile (390 wide)', footer: 'Footer',
  waitlist: 'Waitlist dialog', wheel: 'Color wheel',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const h = G.home;
  await S('hero-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Design Agents for Revenue Teams" — the serif display heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('main p, h1 + p, h1 ~ p').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Hero subcopy', desc: 'The supporting paragraph under the hero heading.', sel: 'hero p' }, { noScroll: true });
  await S('feature-acc', q('button').filter({ hasText: /Chat-driven for everyone/i }).and(page.locator(':visible')).first(), ['default','hover','focus-visible','pressed','opened'], { group: h, title: 'Feature accordion', desc: 'A monospace feature accordion row on the dark panel ("Chat-driven for everyone on the team"); its opened state is the already-expanded first row, measured as painted.', sel: 'feature accordion button' }, { before: SETTLE, noToggle: true, openedVia: 'already expanded at rest; nothing was toggled' });
  await S('feature-acc2', q('button').filter({ hasText: /Quickly personalize/i }).and(page.locator(':visible')).first(), ['default','hover','focus-visible','pressed','opened'], { group: h, title: 'Accordion (closed)', desc: 'The closed "Quickly personalize every presentation" accordion row; its opened state is toggled locally to reveal the panel copy.', sel: 'feature accordion button 2' }, { before: SETTLE });
  await S('sec-h2', q('h2').filter({ hasText: /Keep every slide|on-brand/i }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Section heading', desc: 'A serif section heading ("Keep every slide on-brand").', sel: 'h2' });
  await S('dark-h2', q('h2').filter({ hasText: /Every agent is an endpoint/i }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Dark-panel heading', desc: 'The white serif heading inside the dark feature panel ("Every agent is an endpoint").', sel: 'dark h2' });
  const f = G.footer;
  await S('site-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: f, title: 'Site footer', desc: 'The sitemap footer (BLOG / ASSET LIBRARY / DESIGN TOOLS / ABOUT / CONTACT / LINKEDIN).', sel: 'footer' }, { before: SETTLE });
  save();
}

async function assets() {
  if (!(await newPage('assets'))) return;
  await sheetsFor('assets');
  await chrome('assets');
  // The fixed top nav is shared across pages; measured here — on the home
  // page it re-mounts under the hero's scroll effects and races the reader.
  const g0 = G.shell;
  await S('mkt-nav', q('nav.fixed, nav').and(page.locator(':visible')).first(), ['default'], { group: g0, title: 'Site nav', desc: 'The fixed top nav: VISUAL wordmark, section links (WHY VISUAL? / ASSETS / TOOLS / BLOG) and the WAITLIST button.', sel: 'nav.fixed' }, { noScroll: true });
  await S('mkt-logo', q('nav.fixed a, nav.fixed svg, nav.fixed button').filter({ hasText: /^\s*visual\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g0, title: 'Logo', desc: 'The VISUAL wordmark at the left of the nav.', sel: 'nav VISUAL' }, { noScroll: true });
  await S('nav-link', q('nav.fixed a, nav.fixed button').filter({ hasText: /^\s*why visual\?\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Nav link', desc: 'A section link in the top nav ("WHY VISUAL?"); measured, never followed.', sel: 'nav WHY VISUAL?' }, { noScroll: true });
  await S('waitlist-btn', q('nav.fixed button, nav.fixed a').filter({ hasText: /^\s*waitlist\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Waitlist CTA', desc: 'The nav WAITLIST button — the product\u2019s only conversion CTA on this surface; measured, never pressed (it joins a waitlist).', sel: 'nav WAITLIST' }, { noScroll: true });
  const g = G.assets;
  await S('ast-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Library heading', desc: '"Asset Library" — the 96px serif page heading in the olive ink.', sel: 'h1' }, { noScroll: true });
  await S('ast-tile-hero', q('a[class*="aspect-square" i]').filter({ hasText: /REPLICANTS/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Hero category tile', desc: 'The featured category tile (569px rounded-xl square, "/ REPLICANTS" label over a preview); measured, never followed.', sel: 'a.aspect-square' });
  await S('ast-tile', q('a[class*="aspect-square" i]').filter({ hasText: /CREATIVES/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Category tile', desc: 'A standard category tile (280px rounded-xl square); measured, never followed.', sel: 'a.aspect-square small' });
  await S('ast-tile-img', q('a[class*="aspect-square" i] img').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Tile preview', desc: 'A category tile\u2019s preview image (object-cover inside the rounded square).', sel: 'tile img' });
  await S('ast-kind-link', q('main a, main button').filter({ hasText: /^\s*(Illustrations|Avatars)\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Kind link', desc: 'A library kind link ("Illustrations" / "Avatars") that sections the grid; measured, never followed.', sel: 'kind link' });
  save();
}

async function avatars() {
  if (!(await newPage('avatars'))) return;
  await sheetsFor('avatars');
  await chrome('avatars');
  const g = G.avatars;
  await S('av-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Set heading', desc: 'The avatar-set page heading.', sel: 'h1' }, { noScroll: true });
  await S('av-back', q('main a').filter({ hasText: /^\s*assets\s*$|^\s*asset/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Back link', desc: 'The link back to the asset library; measured, never followed.', sel: 'back link' }, { noScroll: true });
  await S('av-item', q('main a[href*="avatar-"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Avatar item', desc: 'An avatar tile in the set grid (links to its detail page); measured, never followed.', sel: 'avatar tile' });
  await S('av-thumb', q('main img').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Avatar image', desc: 'An avatar preview image in the set grid.', sel: 'avatar img' });
  await S('av-kind', q('main a, main button').filter({ hasText: /^\s*avatars\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Kind crumb', desc: 'The AVATARS kind crumb over the set grid; measured, never followed.', sel: 'kind crumb' });
  save();
}

async function tools() {
  if (!(await newPage('tools'))) return;
  await sheetsFor('tools');
  await chrome('tools');
  const g = G.tools;
  await S('tool-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Tools heading', desc: '"Design Tools" — the 96px serif page heading.', sel: 'h1' }, { noScroll: true });
  await S('tool-card', q('main a[class*="border" i], main a').filter({ hasText: /Color Wheel/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Tool card', desc: 'A tool card ("Color Wheel" — bordered white card with a breadcrumb label, title and copy); measured, never followed.', sel: 'tool card' });
  await S('tool-card2', q('main a[class*="border" i], main a').filter({ hasText: /Image Resizer/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Tool card 2', desc: 'A second tool card ("Image Resizer"), sampled for consistency.', sel: 'tool card 2' });
  await S('tool-crumb', q('main a span, main span').filter({ hasText: /^\s*colors\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Card breadcrumb', desc: 'The "colors" kind crumb on a tool card (paired with its "Tools" label).', sel: 'card crumb' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('ct-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Contact heading', desc: '"Contact" — the 96px serif page heading.', sel: 'h1' }, { noScroll: true });
  await S('ct-copy', q('main p').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Contact copy', desc: 'The supporting paragraph on the contact page.', sel: 'contact p' });
  save();
}

async function post() {
  if (!(await newPage('post'))) return;
  await sheetsFor('post');
  await chrome('post');
  const g = G.post;
  await S('post-h1', q('article h1, main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article heading', desc: 'The article title heading.', sel: 'article h1' }, { noScroll: true });
  // A body paragraph, not the one-line subtitle the first <p> was in the
  // 2026-11 run ("Plus tips to achieve it").
  await S('post-para', q('article p, main p').filter({ hasText: /\S.{80,}/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Article paragraph', desc: 'A body paragraph in the article.', sel: 'article p' });
  await S('post-link', q('article a, main a').filter({ hasNotText: /VISUAL|WHY|ASSETS|TOOLS|BLOG|WAITLIST/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Article link', desc: 'An inline link inside the article body; measured, never followed.', sel: 'article a' });
  save();
}

async function waitlist() {
  if (!(await newPage('waitlist', { url: BASE + '/' }))) return;
  await sheetsFor('waitlist');
  const btn = page.getByRole('button', { name: /^waitlist$/i }).first();
  await btn.click({ timeout: 8000 });
  await page.getByRole('dialog').waitFor({ timeout: 8000 });
  await page.waitForTimeout(500);
  const g = G.waitlist;
  await S('wl-dialog', page.getByRole('dialog'), ['default'], { group: g, title: 'Waitlist dialog', desc: 'The signup wall opened by WAITLIST. Photographed empty. Nothing was typed or submitted.', sel: '[role=dialog]' }, { noScroll: true });
  await S('wl-field', page.locator('[role=dialog] input[name="firstName"]'), ['default', 'focus-visible'], { group: g, title: 'Waitlist text field', desc: 'The First name field. Empty. Focus-visible only; nothing was typed.', sel: 'input[name=firstName]' }, { noScroll: true });
  await S('wl-email', page.locator('[role=dialog] input[name="email"]'), ['default'], { group: g, title: 'Waitlist email field', desc: 'The Work email field. Empty. Not filled.', sel: 'input[name=email]' }, { noScroll: true });
  await S('wl-select', page.locator('[role=dialog] select, [role=dialog] [role=combobox], [role=dialog] button').filter({ hasText: /company size/i }).first(), ['default'], { group: g, title: 'Company size select', desc: 'The Company size control. Not opened, so its menu is not captured.', sel: 'company size' }, { noScroll: true });
  await S('wl-submit', page.getByRole('button', { name: /join waitlist/i }).last(), ['default'], { group: g, title: 'Join waitlist submit', desc: 'The dialog submit button. Not pressed.', sel: 'dialog Join waitlist' }, { noScroll: true });
  save();
}

async function wheel() {
  if (!(await newPage('wheel', { url: BASE + '/colors/color-wheel' }))) return;
  await sheetsFor('wheel');
  const g = G.wheel;
  await S('wheel-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Tool heading', desc: '"Color Wheel" on the public tool page.', sel: 'h1' }, { noScroll: true });
  await S('wheel-hex', page.getByRole('button', { name: /^hex$/i }).first(), ['default'], { group: g, title: 'Format select', desc: 'The Hex format control beside the colour field. Not opened.', sel: 'Hex button' }, { noScroll: true });
  await S('wheel-export', page.getByRole('button', { name: /export/i }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Export button', desc: 'The public Export control. Not pressed, so no file was downloaded.', sel: 'Export' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-nav', q('nav.fixed, nav').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The phone top bar: VISUAL wordmark and the WAITLIST button.', sel: 'mobile nav' }, { noScroll: true });
  await S('m-h1', q('main h1, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The phone hero heading.', sel: 'mobile h1' });
  await S('m-acc', q('button').filter({ hasText: /Chat-driven for everyone|personalize|brand-consistency/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile accordion', desc: 'A feature accordion row on the phone; measured, never toggled here.', sel: 'mobile accordion' }, { before: SETTLE });
  await S('m-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); visual.app paints a single light theme signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, assets, avatars, tools, contact, post, waitlist, wheel, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the Create CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a, nav button');
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
