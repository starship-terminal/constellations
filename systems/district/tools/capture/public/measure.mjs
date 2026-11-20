// Measures district.in's public components in every state reachable without
// an account and writes raw/components-computed.json + component crops.
// district.in is one product signed out: public booking surfaces — the home
// feed (/), listing pages (/movies/, /events/, /events/comedy), an artist
// page and a ticket page — paint the DDS light theme by default; a forced
// html[data-theme=dark] pass measures the real dark declarations.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, learnPlace, scrubPlace, PLACE_WORDS } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
// No city or distance is ever written (lib.mjs): until a page's location line was read, nothing is saved.
const save = () => {
  if (!PLACE_WORDS.size) { console.error('not saving: the location line was never found, so the city could not be masked'); process.exitCode = 1; return; }
  fs.writeFileSync(OUT, JSON.stringify(scrubPlace(out), null, 1) + '\n');
};
const ARTIST = '/events/samay-raina/artist';
const TICKETS = '/events/all-stars-live-apr12-2026-buy-tickets';
const URLS = { home: '/', homeDark: '/', movies: '/movies/', events: '/events/', comedy: '/events/comedy', artist: ARTIST, tickets: TICKETS, mobile: '/movies/' };
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

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, theme = null } = {}) {
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
  if (!(await learnPlace(page)) && !PLACE_WORDS.size) log('  ! location line not found on', key, '- nothing is saved until it is');
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
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').replace(/(?<!Under )\b\d+(?:\.\d+)?\s?km\b/g, '[distance]').slice(0, 40).replace(/\n/g, '|') });
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
    // from an unknown earlier run: its date stays unknown (null).
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
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

// The first element matching `sel` that sits inside the viewport. Carousels
// keep off-screen slide titles "visible" to Playwright (x < 0), and the first
// visible h1/h2 was a slide title, not the listing heading (mv-h1, ev-h1,
// cm-h1 in the 2026-11 run).
async function onScreen(sel) {
  await page.evaluate((s) => {
    document.querySelectorAll('[data-m-onscreen]').forEach((n) => n.removeAttribute('data-m-onscreen'));
    const el = [...document.querySelectorAll(s)].find((e) => {
      const r = e.getBoundingClientRect();
      const shown = e.checkVisibility ? e.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true }) : true;
      return shown && r.width > 0 && r.height > 0 && r.left >= 0 && r.right <= innerWidth && r.bottom > 0 && r.top < innerHeight;
    });
    if (el) el.setAttribute('data-m-onscreen', '1');
  }, sel);
  return q('[data-m-onscreen]');
}

// Whether the page paints dark: a dark, fully opaque body background (a
// translucent one shows the page behind it). Checking the attribute the
// script itself just set would always pass.
const paintsDark = () => page.evaluate(() => {
  const [r, g, b, a = 1] = (getComputedStyle(document.body).backgroundColor.match(/[\d.]+/g) || []).map(Number);
  return a === 1 && (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255 < 0.25;
}).catch(() => false);
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
  chrome: 'App chrome', feed: 'Home feed', cards: 'Content cards',
  listing: 'Listing page', detail: 'Event / artist detail', dark: 'Dark theme (data-theme=dark)',
  mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.chrome;
  await S('nv-bar', q('header, nav, div').filter({ has: page.locator('a[href="/movies/"]') }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Top nav', desc: 'The fixed app bar — District mark, category tabs, search and location.', sel: 'header w/ category links' }, { noScroll: true });
  await S('nv-mark', q('a[href="https://www.district.in"], a[href="/"], header a').and(page.locator(':visible')).first(), B4, { group: g, title: 'District mark', desc: 'The District logo link in the top nav; measured, never followed.', sel: 'logo link' }, { noScroll: true });
  await S('nv-tab', q('a[href="/movies/"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Category tab', desc: 'The Movies tab in the top category row — a real link; measured, never followed.', sel: 'a[href=/movies/]' }, { noScroll: true });
  await S('nv-tab-active', q('a[href="/"]').filter({ hasText: /for you/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Category tab (For you)', desc: 'The "For you" home tab — the selected state of the category row.', sel: 'For you tab' }, { noScroll: true });
  await S('nv-search', q('a[href*="/search"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Search field', desc: 'The search affordance linking to /search; hover/focus measured, never followed.', sel: 'search link' }, { noScroll: true });
  const gf = G.feed;
  await S('hm-h1', await domFind(page, /near you|artists in|happening|sports mania/i, { sel: 'span.text-center, span[class*="text-center"]', tag: 'hmh', minW: 60, minH: 14 }), ['default'], { group: gf, title: 'Page heading', desc: 'The home feed heading.', sel: 'feed heading' }, { noScroll: true });
  await S('hm-section', await domFind(page, /artists in|happening at venues|sports mania|movies near/i, { sel: 'span.text-center, span[class*="text-center"]', tag: 'hms', nth: 1, minW: 60, minH: 14 }), ['default'], { group: gf, title: 'Section heading', desc: 'A feed section heading (artists / movies / events rail).', sel: 'section heading' });
  const gc = G.cards;
  await S('mc-card', q('a[href*="movie-tickets-"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: gc, title: 'Movie card', desc: 'A movie card — poster art, title, certificate and language; hover measured, never followed.', sel: 'a[href*=movie-tickets-]' });
  await S('mc-title', q('a[href*="movie-tickets-"]').first().locator('h1, h2, h3, h4, p, [class*="line-clamp"]').and(page.locator(':visible')).first(), ['default'], { group: gc, title: 'Movie title', desc: 'The title line inside a movie card.', sel: 'card title' });
  await S('ar-card', q('a[href*="/artist"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: gc, title: 'Artist card', desc: 'An artist card in the circular headshot rail (Samay Raina, ALAN WALKER…); hover measured, never followed.', sel: 'a[href*=/artist]' });
  await S('ev-card', q('a[href$="/venue-guide"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: gc, title: 'Event card', desc: 'An event card with date and venue; hover measured, never followed.', sel: 'a[href$=/venue-guide]' });
  await S('ft-bar', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Site footer', desc: 'The District sitemap footer.', sel: 'footer' }, { before: SETTLE });
  save();
}

async function homeDark() {
  if (!(await newPage('homeDark', { url: BASE + '/' }))) return;
  await sheetsFor('homeDark');
  await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await page.waitForTimeout(1500);
  // A dark pass that did not paint dark must not write dark-named readings
  // from light values: the page counts as failed, so earlier readings stay.
  if (!(await paintsDark())) { log('  ! data-theme=dark did not paint a dark body; homeDark skipped'); failedPages.add('homeDark'); return; }
  const g = G.dark;
  await S('dk-body', q('body'), ['default'], { group: g, title: 'Dark body', desc: 'The page background with data-theme=dark applied — the real dark surface the DDS declares.', sel: 'body[data-theme=dark]' }, { noScroll: true });
  await S('dk-nav', q('header, nav, div').filter({ has: page.locator('a[href="/movies/"]') }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Dark nav', desc: 'The top nav under the dark theme.', sel: 'dark header' }, { noScroll: true });
  await S('dk-card', q('a[href*="movie-tickets-"]:has(img), a[href$="/venue-guide"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Dark card', desc: 'A content card under the dark theme.', sel: 'dark card' });
  save();
}

async function movies() {
  if (!(await newPage('movies'))) return;
  await sheetsFor('movies');
  await chrome('movies');
  const g = G.listing;
  await S('mv-h1', await onScreen('h1, h2, h3'), ['default'], { group: g, title: 'Movies heading', desc: 'The "Movies in <city>" listing heading.', sel: 'movies h1' }, { noScroll: true });
  await S('mv-chip', q('a, button, div, span').filter({ hasText: /^(hindi|english|tamil|telugu|2d|imax|u|ua13|a)$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Filter chip', desc: 'A language/format filter chip on the listing; measured, never toggled.', sel: 'filter chip' }, { noScroll: true });
  await S('mv-card', q('a[href*="movie-tickets-MV"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: G.cards, title: 'Listing movie card', desc: 'A movie card on the listing grid; hover measured, never followed.', sel: 'a[href*=movie-tickets-MV]' });
  await S('mv-cert', q('a[href*="movie-tickets-MV"]').first().locator('div, span, p').filter({ hasText: /^(u|ua13\+|a)$/i }).and(page.locator(':visible')).first(), ['default'], { group: G.cards, title: 'Certificate badge', desc: 'The censor-certificate chip on a movie card (U / UA13+ / A).', sel: 'cert chip' });
  save();
}

async function events() {
  if (!(await newPage('events'))) return;
  await sheetsFor('events');
  await chrome('events');
  const g = G.listing;
  await S('ev-h1', await onScreen('h1, h2'), ['default'], { group: g, title: 'Events heading', desc: 'The events listing heading.', sel: 'events h1' }, { noScroll: true });
  await S('ev-listcard', q('a[href$="/venue-guide"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: G.cards, title: 'Listing event card', desc: 'An event card on the listing; hover measured, never followed.', sel: 'a[href$=/venue-guide]' });
  await S('ev-price', await domFind(page, /₹\s*\d/i, { sel: 'span, p, div', tag: 'evp', minW: 20, minH: 8 }), ['default'], { group: G.cards, title: 'Event price', desc: 'A "₹1499 onwards" price line on an event card.', sel: 'price text' });
  save();
}

async function comedy() {
  if (!(await newPage('comedy'))) return;
  await sheetsFor('comedy');
  await chrome('comedy');
  const g = G.listing;
  await S('cm-h1', await onScreen('h1, h2'), ['default'], { group: g, title: 'Comedy heading', desc: 'The comedy events listing heading.', sel: 'comedy h1' }, { noScroll: true });
  await S('cm-filter', q('a, button, [role="button"]').filter({ hasText: /^\s*(date|price|city|sort by)\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Filter control', desc: 'A listing filter control; measured, never opened.', sel: 'filter' }, { noScroll: true });
  save();
}

async function artist() {
  if (!(await newPage('artist', { wait: 15000 }))) return;
  await sheetsFor('artist');
  await chrome('artist');
  const g = G.detail;
  await S('at-h1', q('span.dds-text-3xl, h1, h2, h3').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Artist name', desc: 'The artist page display name.', sel: 'artist h1' }, { noScroll: true });
  await S('at-show', q('a[href*="buy-tickets"], a[href*="/events/"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: g, title: 'Show card', desc: 'An upcoming-show card on the artist page; hover measured, never followed.', sel: 'show card' });
  await S('at-book', q('a, button').filter({ hasText: /^\s*(book( now| tickets)?|buy tickets)\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Book CTA', desc: 'The booking link on the artist page — the show card itself navigates to the ticket page; measured at every paintable state, never followed — booking gates on the Zomato account.', sel: 'booking card-link' }, { noScroll: true });
  save();
}

async function tickets() {
  if (!(await newPage('tickets', { wait: 15000 }))) return;
  await sheetsFor('tickets');
  await chrome('tickets');
  const g = G.detail;
  await S('tk-h1', q('h1, h2, h3').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Event title', desc: 'The event detail title on the ticket page.', sel: 'ticket h1' }, { noScroll: true });
  await S('tk-date', q('span.dds-text-offer, span.dds-text-base').filter({ hasText: /(sat|sun|mon|tue|wed|thu|fri|apr|may|jan|feb|mar|nov)/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Date pill', desc: 'A date/time selector pill; measured, never confirmed.', sel: 'date pill' }, { noScroll: true });
  await S('tk-price', q('span').filter({ hasText: /₹\d/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Ticket price', desc: 'The ticket price line.', sel: 'price' });
  await S('tk-book', q('button').filter({ hasText: /book|proceed|pay|continue/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Book button', desc: 'The primary Book/Proceed CTA; hover/focus measured, never pressed — payment gates on the Zomato account.', sel: 'Book CTA' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/movies/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-bar', q('header, nav, div').filter({ has: page.locator('a') }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The phone app bar at 390px.', sel: 'mobile header' }, { noScroll: true });
  await S('m-tab', q('a[href="/movies/"], a[href="/dining/"], a[href="/events/"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile tab', desc: 'A category tab at 390px.', sel: 'mobile tab' }, { noScroll: true });
  await S('m-card', q('a[href*="movie-tickets-"]:has(img), a[href$="/venue-guide"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile card', desc: 'A content card at 390px.', sel: 'mobile card' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); district.in signs one product into one site — booking surfaces (BeVietnamPro UI, PassengerSerif display) over the DDS token layer, painted light by default; dark flips via html[data-theme=dark] and is measured on a forced pass';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, homeDark, movies, events, comedy, artist, tickets, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
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
