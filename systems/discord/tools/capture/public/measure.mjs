// Measures discord.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home download nitro servers gaming server login register mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// discord.com signs two products into one site: the marketing pages
// (/, /download, /nitro — Webflow, Ggsans, the brand palette) and the app
// surfaces (/servers discovery, a /servers/<slug> detail, /login,
// /register — the real Discord design system, "gg sans", class-scoped
// themes). On the app pages the marketing chrome is wrapped in a
// .theme-light root while the app content carries .theme-dark.theme-darker,
// so light-chrome and dark-app components are measured on the same page.
// There is no theme toggle signed out: the app's light theme exists only as
// a declared sheet — a boundary, not evidence. Specs select by role,
// aria-label, text and stable CSS-module name fragments. Nothing is sent or
// signed into: the only presses are local UI toggles; Log In / Join / Share /
// Create Account buttons are measured, never followed. Promo overlays are
// hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, HIDE_LOGIN_QR } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const SERVER = '/servers/midjourney-662267976984297473';
const URLS = { home: '/', download: '/download', nitro: '/nitro', servers: '/servers', gaming: '/servers/gaming', server: SERVER, login: '/login', register: '/register', mobile: '/servers' };
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
  await page.addStyleTag({ content: HIDE_LOGIN_QR });   // again after load, in case the page replaced <head>
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
    prev.rerunError = err;
    prev.read ??= prev.run || earlierRun; // a second failed re-read keeps the first date
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
  mkt: 'Marketing chrome', hero: 'Marketing hero', page: 'Marketing page',
  disc: 'Server discovery', card: 'Server card', detail: 'Server detail',
  auth: 'Sign-in / register', mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.hero;
  await S('mk-nav', q('header.nav, header[class*="nav"]').and(page.locator(':visible')).first(), ['default'], { group: G.mkt, title: 'Marketing nav', desc: 'The fixed marketing top bar — Discord wordmark, section links, Log In pill.', sel: 'header.nav' }, { noScroll: true });
  await S('mk-nav-download', q('header.nav a').filter({ hasText: /download/i }).and(page.locator(':visible')).first(), B4, { group: G.mkt, title: 'Nav link', desc: 'The Download nav link; measured, never followed.', sel: 'header.nav a Download' }, { noScroll: true });
  await S('mk-nav-drop', q('header.nav a, header.nav div, header.nav button, header.nav [class*="w-dropdown-toggle"]').filter({ hasText: /^\s*discover/i }).and(page.locator(':visible')).first(), B4, { group: G.mkt, title: 'Nav dropdown', desc: 'The Discover nav dropdown trigger; measured, never opened through.', sel: 'nav Discover' }, { noScroll: true });
  await S('mk-nav-login', q('a[class*="login-button"], header.nav a, header.nav button').filter({ hasText: /^\s*log ?in\s*$/i }).and(page.locator(':visible')).first(), B4, { group: G.mkt, title: 'Nav Log In', desc: 'The white Log In pill in the nav; measured, never followed.', sel: 'nav Log In' }, { noScroll: true });
  await S('mk-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Hero display', desc: '"GROUP CHAT THAT\u2019S ALL FUN & GAMES" — the hero display headline in Ggsans.', sel: 'h1' }, { noScroll: true });
  await S('mk-lede', q('p[class*="hero-p"], p').filter({ hasText: /great for playing games/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Hero lede', desc: 'The hero supporting paragraph.', sel: 'p.hero-p' }, { noScroll: true });
  await S('mk-cta-download', q('a, button').filter({ hasText: /download for (linux|windows|mac)/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Hero primary CTA', desc: 'The "Download for …" white button; hover/focus measured, never followed (it would start a download).', sel: 'hero Download' }, { noScroll: true });
  await S('mk-cta-open', q('a, button').filter({ hasText: /open discord in your browser/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Hero secondary CTA', desc: 'The "Open Discord in your browser" brand-fill button; measured, never followed.', sel: 'hero Open Discord' }, { noScroll: true });
  await S('mk-footer', q('footer:not(.lottie)').and(page.locator(':visible')).last(), ['default'], { group: G.mkt, title: 'Site footer', desc: 'The marketing sitemap footer.', sel: 'footer' }, { before: SETTLE });
  save();
}

async function download() {
  if (!(await newPage('download'))) return;
  await sheetsFor('download');
  await chrome('download');
  const g = G.page;
  await S('dl-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Download heading', desc: '"Download Discord wherever you hang out" — the download page heading.', sel: 'download h1' }, { noScroll: true });
  await S('dl-cta', q('a.download-button, a.btn.download-button').and(page.locator(':visible')).first(), B4, { group: g, title: 'Download CTA', desc: 'A platform download button; measured, never followed.', sel: 'a.download-button' }, { noScroll: true });
  save();
}

async function nitro() {
  if (!(await newPage('nitro'))) return;
  await sheetsFor('nitro');
  await chrome('nitro');
  const g = G.page;
  await S('nt-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Nitro heading', desc: '"UNLOCK A WORLD OF PERKS WITH NITRO" — the Nitro page display heading.', sel: 'nitro h1' }, { noScroll: true });
  await S('nt-card', q('[class*="plan"], [class*="tier"], [class*="card"], [class*="Card"]').filter({ hasText: /nitro/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Nitro plan card', desc: 'A Nitro plan/perk card on the marketing page.', sel: 'nitro plan card' });
  await S('nt-cta', q('a, button').filter({ hasText: /subscribe|get nitro|try/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Nitro CTA', desc: 'A Nitro subscribe button; measured, never followed.', sel: 'nitro cta' }, { noScroll: true });
  save();
}

async function servers() {
  if (!(await newPage('servers'))) return;
  await sheetsFor('servers');
  await chrome('servers');
  const gd = G.disc;
  await S('ds-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: gd, title: 'Discovery heading', desc: '"DISCOVERABLE SERVERS" — the display-lg heading on the app discovery page (painted under .theme-dark.theme-darker).', sel: 'h1.display-lg' }, { noScroll: true });
  await settle();
  await S('ds-tab', q('a[class*="categoryTab"]').filter({ hasText: /gaming/i }).and(page.locator(':visible')).first(), B4, { group: gd, title: 'Category pill', desc: 'A category filter pill (Gaming) — a real link to /servers/gaming; measured, never followed.', sel: 'a.categoryTab Gaming' }, { noScroll: true });
  await S('ds-tab-all', q('a[class*="categoryTab"]').filter({ hasText: /^all/i }).and(page.locator(':visible')).first(), B4, { group: gd, title: 'Category pill (All)', desc: 'The "All" category pill — the selected state of the filter row.', sel: 'a.categoryTab All' }, { noScroll: true });
  await S('ds-search', q('[class*="searchBox"], [class*="searchBar"]').and(page.locator(':visible')).first(), ['default'], { group: gd, title: 'Search box', desc: 'The "Search servers for games and interests" field wrapper on discovery.', sel: '.searchBox' }, { noScroll: true });
  await S('ds-search-input', q('input[type="search"], [class*="searchBox"] input').and(page.locator(':visible')).first(), FIELD, { group: gd, title: 'Search input', desc: 'The discovery search input; the filled state types "fortnite" then deletes it — the query runs client-side, nothing is submitted or signed in.', sel: 'input.searchBoxInput' }, { noScroll: true, fillText: 'fortnite' });
  const gc = G.card;
  const card = q('[class*="searchListItem"], a[href^="/servers/"]').and(page.locator(':visible')).first();
  await S('sc-card', q('[class*="searchListItem"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: gc, title: 'Server card', desc: 'A discoverable-server card — banner art, icon, name, verified badge, description, member counts; hover measured, never followed.', sel: '.searchListItem' });
  await S('sc-name', q('[class*="searchListItem"]').first().locator('h1, h2, h3, [class*="name"], [class*="title"]').and(page.locator(':visible')).first(), ['default'], { group: gc, title: 'Server name', desc: 'The server name line inside the card, with its verified check.', sel: 'card name' });
  await S('sc-members', q('[class*="searchListItem"]').first().locator('div, span').filter({ hasText: /members/i }).and(page.locator(':visible')).last(), ['default'], { group: gc, title: 'Member counts', desc: 'The "N Online · N Members" line — the green presence dot plus counts.', sel: 'card members' });
  await S('sc-icon', q('[class*="searchListItem"]').first().locator('img[class*="listIconImage"], img[class*="IconImage"]').and(page.locator(':visible')).first(), ['default'], { group: gc, title: 'Server icon', desc: 'The squircle server icon overlapping the card banner.', sel: 'card img.listIconImage' });
  save();
}

async function gaming() {
  if (!(await newPage('gaming'))) return;
  await sheetsFor('gaming');
  await chrome('gaming');
  await S('gs-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: G.disc, title: 'Category heading', desc: 'The Gaming category discovery page heading.', sel: 'gaming h1' }, { noScroll: true });
  await S('gs-tab-gaming', q('a[class*="categoryTab"]').filter({ hasText: /gaming/i }).and(page.locator(':visible')).first(), ['default'], { group: G.disc, title: 'Category pill (selected)', desc: 'The Gaming pill on /servers/gaming — the painted selected state.', sel: 'a.categoryTab Gaming (selected)' }, { noScroll: true });
  save();
}

async function server() {
  if (!(await newPage('server'))) return;
  await sheetsFor('server');
  await chrome('server');
  const g = G.detail;
  await S('sv-banner', q('img, [class*="banner"], [class*="Banner"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Server banner', desc: 'The server detail page banner art.', sel: 'server banner' }, { noScroll: true });
  await S('sv-name', q('h1, h2').filter({ hasText: /midjourney/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Server name', desc: 'The server title with the verified badge — display type.', sel: 'server h1' }, { noScroll: true });
  await S('sv-members', await domFind(page, /[\d,]+\s+online/i, { sel: 'span, div, p', tag: 'svm', minW: 30, minH: 10 }), ['default'], { group: g, title: 'Member counts', desc: 'The "N Online · N Members" line under the name.', sel: 'server members' }, { noScroll: true });
  await S('sv-join', q('a, button').filter({ hasText: /join the conversation|join/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Join CTA', desc: 'The brand-fill "Join the Conversation" button; hover/focus measured, never followed — joining needs an account.', sel: 'Join button' }, { noScroll: true });
  await S('sv-share', q('button, a').filter({ hasText: /^\s*share\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Share button', desc: 'The Share button under the member counts; measured, never pressed.', sel: 'Share button' }, { noScroll: true });
  await S('sv-chip', q('a, span, div').filter({ hasText: /^(science & tech|entertainment|creative arts|collaboration|wiki & guide)$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Category chip', desc: 'A category chip in the detail sidebar; measured, never followed.', sel: 'category chip' });
  await S('sv-about', q('h2, h3, h4').filter({ hasText: /^\s*about\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'About heading', desc: 'The tracked ABOUT section label.', sel: 'about h2' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 18000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('lg-card', q('form').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Auth card', desc: 'The sign-in card on the animated brand backdrop — form fields left, QR panel right (its code hidden: it encodes a sign-in token).', sel: 'login form' }, { noScroll: true });
  await S('lg-h1', q('h1, h2, h3').filter({ hasText: /welcome back/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Sign-in heading', desc: '"Welcome back!" — the auth card heading.', sel: 'login h1' }, { noScroll: true });
  await S('lg-email', q('input[name="email"], input[type="text"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Email field', desc: 'The "Email or Phone Number" field; the filled state types an address then deletes it — nothing is submitted.', sel: 'input email' }, { noScroll: true, fillText: 'name@example.com' });
  await S('lg-pass', q('input[type="password"]').and(page.locator(':visible')).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password field with the reveal-button affordance; focused via a click-in, never filled.', sel: 'input password' }, { noScroll: true });
  await S('lg-submit', q('button').filter({ hasText: /^\s*log ?in\s*$/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Log In button', desc: 'The brand-fill Log In submit; hover/focus measured, never pressed — it would submit the sign-in.', sel: 'Log In button' }, { noScroll: true });
  await S('lg-forgot', q('a, button').filter({ hasText: /forgot your password/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Forgot link', desc: 'The "Forgot your password?" link; measured, never followed.', sel: 'forgot link' }, { noScroll: true });
  await S('lg-register', q('a, button').filter({ hasText: /^\s*register\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Register link', desc: 'The "Need an account? Register" link; measured, never followed.', sel: 'register link' }, { noScroll: true });
  await S('lg-qr', q('[class*="qrLogin"], [class*="qr"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'QR panel', desc: 'The "Log in with QR Code" panel on the card\u2019s right; the code itself is hidden before any crop (it encodes a sign-in token).', sel: 'qrLogin panel' }, { noScroll: true });
  save();
}

async function register() {
  if (!(await newPage('register', { wait: 18000 }))) return;
  await sheetsFor('register');
  await chrome('register');
  const g = G.auth;
  await S('rg-h1', q('h1, h2, h3').filter({ hasText: /create an account/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Register heading', desc: '"Create an account" — the register card heading.', sel: 'register h1' }, { noScroll: true });
  await S('rg-email', q('input[type="email"], input[name="email"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Register email', desc: 'The register email field; the filled state types an address then deletes it — nothing is submitted.', sel: 'register email' }, { noScroll: true, fillText: 'name@example.com' });
  await S('rg-submit', q('button').filter({ hasText: /create account/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Create Account', desc: 'The Create Account submit; hover/focus measured, never pressed.', sel: 'Create Account' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/servers' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-bar', q('nav, header, [class*="nav__"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The phone marketing bar over discovery.', sel: 'mobile nav' }, { noScroll: true });
  await S('m-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile heading', desc: 'The DISCOVERABLE SERVERS display at 390px.', sel: 'mobile h1' }, { noScroll: true });
  await S('m-search', q('[class*="searchBox"], input[type="search"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile search', desc: 'The discovery search field at 390px.', sel: 'mobile search' }, { noScroll: true });
  await S('m-card', q('[class*="searchListItem"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile server card', desc: 'A server card at 390px.', sel: 'mobile card' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); discord.com signs two products into one site — marketing pages (Ggsans) and app surfaces painted .theme-dark.theme-darker signed out, with marketing chrome inside a .theme-light root';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, download, nitro, servers, gaming, server, login, register, mobile };
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
