// Measures curater.org's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home feed taste curation profile terms mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// curater.org is a React/Vite SPA: same-origin hashed /assets/*.css carry a
// Tailwind v4 --color-* palette, a shadcn semantic set and Curater's own
// --Curater-* namespace; the page paints one light theme. Specs select by
// CSS-module class fragment ([class*="_name_"]), role, aria-label or text.
// "Sign in or create account", "Log in or sign up", "Continue with Google"
// and every outbound link are measured, never followed; toggles (search
// reveal, card menus, the mobile nav) are local UI state only.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, styleOfSelector, crop, cropSelector, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', feed: '/feed', taste: '/taste', curation: '/curation/qDNMdxe5', profile: '/ravi', terms: '/terms' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
  // Cloudflare Turnstile can greet a route: wait it out, then one retry on a
  // fresh context before recording the route as blocked this run.
  let ok = false;
  for (let tries = 0; tries < 2 && !ok; tries++) {
    await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
    ok = !(await blocked());
    if (!ok && tries === 0) { log('  challenge, one reload', key); }
  }
  if (!ok) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
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
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|buy now|buy font|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// Variant of S() for routes whose Playwright locators never resolve.
// curater.org/taste client-side redirects to /taste/soon and the navigation
// never settles: locators count matches, but every resolve dies with the
// execution context. Measuring the default state through the main world
// (same styleOf reader + clip crop) instead of locators.
async function SJ(key, sel, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: sel });
  delete out.components[key].missing;
  const found = await page.evaluate((pick) => !!eval(pick), sel.startsWith('js:') ? sel.slice(3) : `document.querySelector(${JSON.stringify(sel)})`);
  if (!found) { out.components[key].missing = true; log('  ! missing', key); return; }
  try {
    const s = await styleOfSelector(page, sel);
    if (!s) throw new Error('element not found');
    let file;
    if (opts.crop !== false) {
      try { file = await cropSelector(page, sel, `${key}-default`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    out.components[key].states.default = { ...s, crop: file, via: 'main-world query (locators never settle on this route)' };
    log('  ', key, 'default', s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    out.components[key].states.default = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, 'default', String(e.message).slice(0, 120));
  }
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
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
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks a home feed card: the smallest ancestor holding a headline and a
// thumbnail.
async function markTrendCard() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('[class*="_card_"]')].filter((el) => {
      const r = el.getBoundingClientRect();
      return el.querySelector('h1,h2,h3') && r.width > 300 && r.height > 200;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'trendcard');
  });
}

// Marks a feed curation entry: the smallest ancestor holding a curator label
// and a title link.
async function markFeedEntry() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('article, [class*="_item"], [class*="_entry"], [class*="_curation"]')].filter((el) => {
      const r = el.getBoundingClientRect();
      return el.querySelector('a') && r.width > 300 && r.height > 200;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'feedentry');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', feed: 'Feed', taste: 'TasteScope',
  curation: 'Curation', profile: 'Profile', terms: 'Legal', mobile: 'Mobile (390 wide)',
};

const CLS = (n) => `[class*="${n}"]`;

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-rail', q('nav, [class*="_nav_"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav rail', desc: 'The 48px-wide vertical icon rail (Home / Taste / Notifications / Profile / Create / Settings).', sel: 'nav._nav_*' }, { noScroll: true });
  await S('nav-button', q(`${CLS('_navButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Nav button', desc: 'A 48x48 rail icon button (Home); measured, never followed.', sel: 'nav button._navButton_*' }, { noScroll: true });
  await S('settings-btn', q(`${CLS('_settingsButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Settings button', desc: 'The 48x48 settings gear at the rail foot; measured, never followed.', sel: 'button._settingsButton_*' }, { noScroll: true });
  await S('signin-btn', q('button, a').filter({ hasText: /sign in or create account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: '"Sign in or create account" — the 259x58 auth CTA; measured, never followed.', sel: 'sign-in button' }, { noScroll: true });
  const h = G.home;
  await S('trend-header', q(`${CLS('_header_')}, header`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Trending header', desc: '"Trending on Curater / What our community has been sharing lately" + the sign-in CTA.', sel: '._header_*' }, { noScroll: true });
  await markTrendCard();
  await S('trend-card', q('[data-m-mark="trendcard"]').filter({ visible: true }).first(), B4, { group: h, title: 'Trend card', desc: 'A 544x570 trending curation card: thumbnails, headline, description, curator avatars; measured, never followed.', sel: 'div._card_*' });
  await S('card-thumb', q(`${CLS('_thumbnail_')}`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Card thumbnail', desc: 'A 100x100 curation thumbnail tile.', sel: 'a._thumbnail_*' });
  await S('card-headline', q(`${CLS('_headline_')}`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Card headline', desc: 'The curation headline (h2, 398px wide).', sel: '._headline_*' });
  await S('card-desc', q(`${CLS('_description_')}`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Card description', desc: 'The curator\'s description copy under the headline.', sel: '._description_*' });
  await S('curated-label', q(`${CLS('_curatorsLabel_')}`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Curated-by label', desc: 'The "CURATED BY" micro-label.', sel: '._curatorsLabel_*' });
  await S('card-avatar', q(`${CLS('_avatarItem_')}, ${CLS('_avatar_')}`).filter({ visible: true }).first(), ['default'], { group: h, title: 'Curator avatar', desc: 'A 24x24 curator avatar in the card.', sel: '._avatarItem_*' });
}

async function feed() {
  if (!(await newPage('feed'))) return;
  await sheetsFor('feed');
  await chrome('feed');
  const g = G.shell;
  await S('tab-button', q(`${CLS('_tabButton_')}`).filter({ hasText: /^\s*Featured\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feed tab', desc: 'A 40px feed tab (Featured / For You / More); measured, never activated.', sel: '._tabButton_*' }, { noScroll: true });
  await S('search-toggle', q(`${CLS('_searchToggle_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Search toggle', desc: 'The 20x20 search icon that reveals the search field.', sel: '._searchToggle_*' }, { noScroll: true });
  // Reveal the collapsed search field locally, measure it, leave it open.
  const st = q(`${CLS('_searchToggle_')}`).filter({ visible: true }).first();
  const openSearch = async () => { await st.click({ timeout: 3000 }); await page.waitForTimeout(700); };
  // The revealed field collapses when the pointer leaves the toggle area, so
  // the run must not reset the mouse between states: open it once and keep it.
  await S('search-field', q(`${CLS('_searchField_')}`).filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The "Search curations..." input revealed by the toggle; focused locally, never submitted.', sel: '._searchField_*' }, { noScroll: true, noReset: true, open: openSearch });
  await S('login-btn', q(`${CLS('_signInButton_')}, a, button`).filter({ hasText: /log in or sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login button', desc: '"Log in or sign up" — the header auth link; measured, never followed.', sel: '._signInButton_*' }, { noScroll: true });
  await S('nav-button-active', q(`a[class*="_navButton_"][class*="active"], a.active[class*="_navButton_"]`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav button, active', desc: 'The active rail button (the .active sibling) — its highlighted state.', sel: 'nav a.active' }, { noScroll: true });
  const f = G.feed;
  await S('feed-heading', q(`${CLS('_heading_')}, h1, h2`).filter({ hasText: /browse by themes/i }).filter({ visible: true }).first(), ['default'], { group: f, title: 'Feed heading', desc: '"Browse by themes" — the feed section heading.', sel: '._heading_*' }, { noScroll: true });
  await S('theme-card', q(`a${CLS('_card_')}`).filter({ visible: true }).first(), B4, { group: f, title: 'Theme card', desc: 'A 224x271 theme tile ("Visual Identity / 16 curations"); measured, never followed.', sel: 'a._card_*' });
  await lazyLoad();
  await markFeedEntry();
  await S('curator-label', q(`${CLS('_curatorLabel_')}`).filter({ visible: true }).first(), B4, { group: f, title: 'Curator label', desc: 'A curator chip ("Ravi", "Glauber") over a feed entry; measured, never followed.', sel: '._curatorLabel_*' });
  await S('title-link', q(`${CLS('_titleLink_')}`).filter({ visible: true }).first(), B4, { group: f, title: 'Curation title', desc: 'The large editorial curation title link; measured, never followed.', sel: '._titleLink_*' });
  await S('save-btn', q(`${CLS('_saveButton_')}`).filter({ visible: true }).first(), B4, { group: f, title: 'Save button', desc: 'The save/bookmark control ("1", "Add to my taste"); measured, never pressed.', sel: '._saveButton_*' });
  await S('media-item', q(`${CLS('_mediaItem_')}`).filter({ visible: true }).first(), ['default'], { group: f, title: 'Media tile', desc: 'A large media tile in the entry\'s mosaic (up to 1080x540).', sel: '._mediaItem_*' });
  await S('album-link', q(`${CLS('_albumLink_')}`).filter({ visible: true }).first(), B4, { group: f, title: 'Album tile', desc: 'A 540x540 album tile ("ALBUM / 8 TRACKS"); measured, never followed.', sel: '._albumLink_*' });
}

async function taste() {
  if (!(await newPage('taste', { wait: 16000 }))) return;
  await sheetsFor('taste');
  await chrome('taste');
  const g = G.taste;
  await SJ('taste-desc', '[class*="_mainDescription_"]', { group: g, title: 'TasteScope panel', desc: 'The "SOON / TasteScope — it captures all dimensions of your aesthetic identity" teaser panel.', sel: '._mainDescription_*' });
  await SJ('taste-h4', "js:[...document.querySelectorAll('h4')].find((h)=>/tastescope/i.test(h.innerText))", { group: g, title: 'TasteScope heading', desc: 'The "TasteScope" teaser heading.', sel: 'taste h4' });
  await SJ('taste-canvas', "js:[...document.querySelectorAll('canvas')].reduce((a,b)=>{const ra=a&&a.getBoundingClientRect(),rb=b.getBoundingClientRect();return (!a||rb.width>ra.width)?b:a;})", { group: g, title: 'BrandGlobe canvas', desc: 'The 1360x900 WebGL globe canvas behind the teaser.', sel: 'canvas' });
}

async function curation() {
  if (!(await newPage('curation'))) return;
  await sheetsFor('curation');
  await chrome('curation');
  const g = G.curation;
  await S('back-btn', q(`${CLS('_backButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Back button', desc: 'The 36x36 back-arrow button; measured, never followed.', sel: '._backButton_*' }, { noScroll: true });
  await S('options-btn', q(`${CLS('_hiddenOptionsButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Options button', desc: 'The 32x32 options (…) button.', sel: '._hiddenOptionsButton_*' }, { noScroll: true });
  await S('curation-h1', q(`h1${CLS('_title_')}, h1`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Curation title', desc: 'The 350x240 editorial curation title (h1).', sel: 'h1._title_*' }, { noScroll: true });
  await S('sso-btn', q(`${CLS('_signInButtonContainer_')} button, ${CLS('_signInButtonContainer_')} a, ${CLS('_signInButtonContainer_')}`).filter({ hasText: /continue with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: '"Continue with Google" — the 350x58 SSO button; measured, never pressed.', sel: '._signInButtonContainer_*' });
  await S('similar-label', q('h3').filter({ hasText: /search similar/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Similar label', desc: 'The "SEARCH SIMILAR ON" micro-heading.', sel: 'h3 similar' });
  await S('similar-btn', q(`${CLS('_button_')}`).filter({ hasText: /pinterest|cosmos/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Similar-search button', desc: 'A 132x45 outbound similar-search button (Pinterest / Cosmos); measured, never followed.', sel: 'a._button_*' });
  await S('pins-label', q('h3').filter({ hasText: /^\s*PINS\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pins label', desc: 'The "PINS" micro-heading.', sel: 'h3 pins' });
}

async function profile() {
  if (!(await newPage('profile'))) return;
  await sheetsFor('profile');
  await chrome('profile');
  const g = G.profile;
  await S('profile-name', q(`h1${CLS('_name_')}, h1`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile name', desc: 'The "Ravi Vasavan" profile heading.', sel: 'h1._name_*' }, { noScroll: true });
  await S('profile-avatar', q(`${CLS('_userAvatar_')}`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile avatar', desc: 'The 28x28 profile avatar.', sel: '._userAvatar_*' }, { noScroll: true });
  await S('tastescope-btn', q(`${CLS('_tasteScopeButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'TasteScope button', desc: 'The 129x42 "TasteScope" header button; measured, never followed.', sel: '._tasteScopeButton_*' }, { noScroll: true });
  await S('profile-bio', q(`${CLS('_description_')}`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile bio', desc: 'The curator\'s bio paragraph.', sel: '._description_*' });
  await S('profile-item', q(`article${CLS('_item_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Profile item', desc: 'A 268x380 profile curation item (category, title, saved mark, menu); measured, never followed.', sel: 'article._item_*' });
  await S('item-title', q(`h3${CLS('_title_')}, h3`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Item title', desc: 'The item\'s 268x60 title.', sel: 'h3._title_*' });
  await S('item-menu', q(`${CLS('_menuButton_')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Item menu', desc: 'The 28x28 item overflow menu; opened locally, never an action taken.', sel: '._menuButton_*' });
}

async function terms() {
  if (!(await newPage('terms'))) return;
  const g = G.terms;
  await S('legal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal heading', desc: '"Terms of Use" — the legal page heading.', sel: 'h1' }, { noScroll: true });
  await S('legal-body', q('main p, article p, [class*="content" i] p, p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal paragraph', desc: 'A body paragraph of the terms text.', sel: 'legal p' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-nav-rail', q('nav, [class*="_nav_"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav rail', sel: 'nav at 390' }, { noScroll: true });
  const menu = q(`${CLS('_mobileNavButton_')}, ${CLS('_mobileMenuButton_')}`).filter({ visible: true }).first();
  await S('m-nav-button', menu, B4, { group: g, title: 'Mobile nav button', desc: 'A rail icon button at 390px.', sel: 'nav button at 390' }, { noScroll: true });
  await S('m-signin-btn', q('button, a').filter({ hasText: /sign in or create account|log in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign-in', desc: 'The mobile sign-in CTA; measured, never followed.', sel: 'sign-in button at 390' }, { noScroll: true });
  await page.evaluate(() => { const c = [...document.querySelectorAll('h1,h2')].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 100 && r.height > 10; }); if (c[0]) c[0].setAttribute('data-m-mark', 'mhead'); });
  await S('m-heading', q('[data-m-mark="mhead"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile heading', sel: 'painted heading at 390' });
  await markTrendCard();
  await S('m-trend-card', q('[data-m-mark="trendcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile trend card', desc: 'A trend card at 390px width.', sel: 'div._card_* at 390' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); curater.org paints a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, feed, taste, curation, profile, terms, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', CLS('_navButton_'));
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
