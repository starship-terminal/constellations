// Measures digg.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home dark tech story profile login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// digg.com (the 2025 reboot) paints both themes signed out: the sidebar theme
// pill cycles System -> Light -> Dark -> System, so the dark pass toggles it
// locally and measures real dark paint. The public surface is the trending
// feed (story cards with the digg-it vote pill, comment count, source avatar
// cluster and "N Sources" link), a category feed, a story page, /u/<source>
// profiles and the Clerk auth forms. Classes are Tailwind utilities, so specs
// select by data hooks (data-post-*/data-slot), role, aria-label or text.
// Nothing is sent or signed into: the only presses are local UI toggles — the
// Trending sort dropdown and the theme pill — and the vote pill, digg it
// button, nav links, source links and Continue buttons are measured, never
// followed. The cookie banner is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, setTheme } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const STORY = '/world-business/k7vz2u4u';
const URLS = { home: '/', dark: '/', tech: '/tech', story: STORY, profile: '/u/wired', login: '/login', signup: '/sign-up', mobile: '/' };
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
  if (theme && !(await setTheme(page, theme))) {
    // Never record light paint under d-* names: abort the page so the dark
    // group records missing rather than mislabelled evidence.
    log('  ! theme pill did not reach', theme, '— skipping', key);
    failedPages.add(key); await page.close(); await ctx.close(); return false;
  }
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
  shell: 'Left sidebar', feed: 'Feed controls', card: 'Story card',
  rail: 'Right rail', story: 'Story page', auth: 'Sign-in / sign-up',
  profile: 'Source profile', dark: 'Dark theme', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];
// The story card container that wraps a [data-post-headline].
const cardOf = (loc) => loc.locator('xpath=ancestor::*[@data-slot="item"][1]');

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g0 = G.shell;
  await S('sb-home', q('a[class*="peer/menu-button"]').filter({ hasText: /^\s*home\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Sidebar item (active)', desc: 'The Home row in the left sidebar — icon + label pill, painted selected on the feed; measured, never followed.', sel: 'a.peer/menu-button Home' }, { noScroll: true });
  await S('sb-tech', q('a[class*="peer/menu-button"]').filter({ hasText: /technology/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Sidebar item', desc: 'A category row in the left sidebar (Technology, with its badge icon); measured, never followed.', sel: 'a.peer/menu-button Technology' }, { noScroll: true });
  await S('sb-pill', q('button').filter({ hasText: /^(system|light|dark)$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Theme pill', desc: 'The sidebar theme pill (System / Light / Dark cycle); pressed is CDP-forced — the real cycle is exercised by the dark pass.', sel: 'theme pill button' }, { noScroll: true });
  await S('sb-login', q('a, button').filter({ hasText: /^\s*log ?in\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Log in link', desc: 'The sidebar Log in link to /login; measured, never followed.', sel: 'Log in' }, { noScroll: true });
  await S('sb-signup', q('a, button').filter({ hasText: /^\s*sign ?up\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g0, title: 'Sign up CTA', desc: 'The blue Sign up button at the foot of the sidebar; measured, never followed.', sel: 'Sign up' }, { noScroll: true });
  const gf = G.feed;
  await S('feed-trending', q('button').filter({ hasText: /^\s*trending\s*$/i }).and(page.locator(':visible')).first(), [...B4, 'opened'], { group: gf, title: 'Sort dropdown', desc: 'The Trending sort trigger over the feed; its opened state is a local dropdown of sort options.', sel: 'Trending button' }, { before: SETTLE, allowLink: true });
  await S('feed-compact', q('button').filter({ hasText: /^\s*compact\s*$/i }).and(page.locator(':visible')).first(), B4, { group: gf, title: 'Density toggle', desc: 'The Compact density control beside the sort dropdown; measured, never toggled.', sel: 'Compact button' }, { before: SETTLE });
  const gc = G.card;
  await S('post-card', cardOf(q('[data-post-headline]').and(page.locator(':visible')).first()), ['default'], { group: gc, title: 'Story card', desc: 'A feed story card: category chip, headline, summary, vote pill, comment link and source cluster, thumbnail at right.', sel: 'post item' });
  await S('post-headline', q('[data-post-headline]').and(page.locator(':visible')).first(), B4, { group: gc, title: 'Card headline', desc: 'The card’s stretched headline link (data-post-headline); measured, never followed.', sel: 'data-post-headline' });
  await S('post-summary', cardOf(q('[data-post-headline]').first()).locator('p').filter({ hasText: /.{60,}/ }).and(page.locator(':visible')).first(), ['default'], { group: gc, title: 'Card summary', desc: 'The one-two line summary under the headline.', sel: 'card p' });
  await S('post-vote', cardOf(q('[data-post-headline]').first()).locator('button').and(page.locator(':visible')).first(), B4, { group: gc, title: 'Vote pill', desc: 'The digg-it vote pill on the card (icon + odometer count); pressed is CDP-forced — a real press would cast a vote.', sel: 'vote button' });
  await S('post-comment', cardOf(q('[data-post-headline]').first()).locator('a[data-feed-conversation-link], a[data-slot="button"]').and(page.locator(':visible')).first(), B4, { group: gc, title: 'Comment link', desc: 'The comment-count link on the card; measured, never followed.', sel: 'comment link' });
  await S('post-avatars', cardOf(q('[data-post-headline]').first()).locator('a[data-slot="popover-anchor"]').and(page.locator(':visible')).first(), B4, { group: gc, title: 'Source avatar', desc: 'A source avatar in the card’s cluster (popover anchor, initials); measured, never followed.', sel: 'source avatar' });
  await S('post-sources', cardOf(q('[data-post-headline]').first()).locator('a[data-post-link-role="meta"]').and(page.locator(':visible')).first(), B4, { group: gc, title: 'Sources link', desc: 'The "N Sources, updated Xm ago" meta link; measured, never followed.', sel: 'sources meta link' });
  await S('post-thumb', cardOf(q('[data-post-headline]').first()).locator('img').and(page.locator(':visible')).last(), ['default'], { group: gc, title: 'Card thumbnail', desc: 'The story’s right-side thumbnail inside the card.', sel: 'card img' });
  const gr = G.rail;
  await S('rail-contribs', q('[data-slot="card"]').filter({ hasText: /top contributors/i }).and(page.locator(':visible')).first(), ['default'], { group: gr, title: 'Top Contributors', desc: 'The right-rail "Top Contributors" ranked panel.', sel: 'contributors panel' });
  await S('rail-posts', q('[data-slot="card"]').filter({ hasText: /top posts yesterday/i }).and(page.locator(':visible')).first(), ['default'], { group: gr, title: 'Top Posts panel', desc: 'The right-rail "Top Posts Yesterday" list with thumbnails.', sel: 'top posts panel' });
  const gf2 = G.footer;
  await S('site-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: gf2, title: 'Site footer', desc: 'The mono sitemap footer (About / Contact / Privacy Policy / Terms / Community Guidelines / © digg).', sel: 'footer' }, { before: SETTLE });
  save();
}

async function dark() {
  if (!(await newPage('dark', { theme: 'dark' }))) return;
  await sheetsFor('dark');
  await chrome('dark');
  const g = G.dark;
  await S('d-card', cardOf(q('[data-post-headline]').and(page.locator(':visible')).first()), ['default'], { group: g, title: 'Card (dark)', desc: 'A feed story card measured with the dark theme painted via the sidebar pill.', sel: 'post item (dark)' });
  await S('d-headline', q('[data-post-headline]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Headline (dark)', desc: 'The card headline under the dark theme.', sel: 'data-post-headline (dark)' });
  await S('d-vote', cardOf(q('[data-post-headline]').first()).locator('button').and(page.locator(':visible')).first(), B4, { group: g, title: 'Vote pill (dark)', desc: 'The digg-it vote pill under the dark theme.', sel: 'vote button (dark)' });
  await S('d-signup', q('a, button').filter({ hasText: /^\s*sign ?up\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign up (dark)', desc: 'The blue Sign up CTA under the dark theme.', sel: 'Sign up (dark)' });
  await S('d-trending', q('button').filter({ hasText: /^\s*trending\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sort dropdown (dark)', desc: 'The Trending sort trigger under the dark theme.', sel: 'Trending (dark)' });
  await S('d-rail', q('[data-slot="card"]').filter({ hasText: /top contributors/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Rail panel (dark)', desc: 'The Top Contributors panel under the dark theme.', sel: 'rail panel (dark)' });
  save();
}

async function tech() {
  if (!(await newPage('tech'))) return;
  await sheetsFor('tech');
  await chrome('tech');
  await S('cat-title', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: G.feed, title: 'Category heading', desc: 'The Technology feed heading.', sel: 'category h1' }, { noScroll: true });
  await S('cat-tech-active', q('a[class*="peer/menu-button"]').filter({ hasText: /technology/i }).and(page.locator(':visible')).first(), ['default'], { group: G.shell, title: 'Sidebar item (selected)', desc: 'The Technology sidebar row on /tech — the painted selected state of a category item.', sel: 'sidebar Technology (active)' }, { noScroll: true });
  await S('cat-card', cardOf(q('[data-post-headline]').and(page.locator(':visible')).first()), ['default'], { group: G.card, title: 'Category card', desc: 'A story card on the Technology feed — same anatomy as the trending card.', sel: 'category post item' });
  save();
}

async function story() {
  if (!(await newPage('story'))) return;
  await sheetsFor('story');
  await chrome('story');
  const g = G.story;
  await S('st-kicker', q('p, span, div').filter({ hasText: /^\s*report\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'REPORT kicker', desc: 'The tracked-out REPORT label over the story headline.', sel: 'REPORT label' }, { noScroll: true });
  await S('st-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Story headline', desc: 'The serif story headline.', sel: 'story h1' }, { noScroll: true });
  await S('st-summary', q('p').filter({ hasText: /.{60,}/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Story summary', desc: 'The one-two line summary under the headline.', sel: 'story summary' }, { noScroll: true });
  await S('st-vote', q('button').filter({ hasText: /digg/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'digg it button', desc: 'The "digg it" vote pill under the headline (icon + count); pressed is CDP-forced — a real press would cast a vote.', sel: 'digg it button' }, { noScroll: true });
  await S('st-sources', q('a, button').filter({ hasText: /\d+\s+sources/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sources meta', desc: 'The "N Sources, first seen Xh ago" meta cluster; measured, never followed.', sel: 'sources meta' }, { noScroll: true });
  // One right-rail card holds both TODAY'S RANK and COMBINED VIEWS — a
  // "rank card" selector lands on this same 376x384 panel, so there is a
  // single st-stat component, not a second card.
  await S('st-stat', q('[data-slot="card"]').filter({ hasText: /combined views/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Stat card', desc: 'The right-rail stat card — TODAY\'S RANK over COMBINED VIEWS and the like/comment/save counts.', sel: 'stat card' });
  await S('st-srclist', q('[data-slot="card"]').filter({ hasText: /sources/i }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Sources list', desc: 'The right-rail "N Sources" list of source posts.', sel: 'sources list' });
  await S('st-tldr', q('p, span, div, h2, h3').filter({ hasText: /^\s*tldr\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'TLDR label', desc: 'The tracked TLDR section label over the summary prose.', sel: 'TLDR label' });
  await S('st-para', q('p').filter({ hasText: /.{150,}/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'TLDR paragraph', desc: 'A body paragraph in the TLDR section.', sel: 'story p' });
  await S('st-crumb', q('main a, main button').filter({ hasText: /world & business|technology|science|sports|gaming|entertainment|\bai\b/i }).and(page.locator(':visible')).first(), B4, { group: G.shell, title: 'Category crumb', desc: 'The category chip link beside the back button; measured, never followed.', sel: 'story crumb' }, { noScroll: true });
  save();
}

async function profile() {
  if (!(await newPage('profile'))) return;
  await sheetsFor('profile');
  await chrome('profile');
  const g = G.profile;
  await S('pf-name', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Profile name', desc: 'The source profile heading (@wired).', sel: 'profile h1' }, { noScroll: true });
  await S('pf-card', cardOf(q('[data-post-headline]').and(page.locator(':visible')).first()), ['default'], { group: g, title: 'Profile story card', desc: 'A story card in the source’s profile feed.', sel: 'profile post item' });
  save();
}

async function login() {
  if (!(await newPage('login'))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  await S('lg-h1', q('h1, h2').filter({ hasText: /welcome back/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Sign-in heading', desc: '"Welcome back!" — the Clerk sign-in card heading.', sel: 'login h1' }, { noScroll: true });
  await S('lg-google', q('button').filter({ hasText: /continue with google/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Google OAuth', desc: 'The "Continue with Google" outline button; measured, never followed.', sel: 'oauth google' }, { noScroll: true });
  await S('lg-x', q('button').filter({ hasText: /continue with x/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'X OAuth', desc: 'The "Continue with X / Twitter" outline button; measured, never followed.', sel: 'oauth x' }, { noScroll: true });
  await S('lg-email', q('input[name="identifier"], input[type="text"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Email field', desc: 'The "Enter your email address" identifier field; the filled state types an address then deletes it — nothing is submitted.', sel: '#identifier-field' }, { noScroll: true, fillText: 'name@example.com' });
  await S('lg-pass', q('input[type="password"]').and(page.locator(':visible')).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password field; focused via a click-in, never filled.', sel: '#password-field' }, { noScroll: true });
  await S('lg-continue', q('button').filter({ hasText: /^\s*continue\s*$/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Continue button', desc: 'The blue Continue submit; hover/focus measured, never pressed — it would submit the sign-in.', sel: 'Continue button' }, { noScroll: true });
  await S('lg-signup', q('a').filter({ hasText: /^\s*sign ?up\s*$/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Don’t have an account? Sign up" link under the form; measured, never followed.', sel: 'login sign up' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup'))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.auth;
  await S('su-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Sign-up heading', desc: 'The Clerk sign-up card heading.', sel: 'signup h1' }, { noScroll: true });
  await S('su-email', q('input[type="text"], input[name="identifier"], input[type="email"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Sign-up email', desc: 'The sign-up identifier field; the filled state types an address then deletes it — nothing is submitted.', sel: 'signup field' }, { noScroll: true, fillText: 'name@example.com' });
  await S('su-continue', q('button').filter({ hasText: /^\s*continue\s*$/i }).and(page.locator(':visible')).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sign-up Continue', desc: 'The sign-up Continue submit; hover/focus measured, never pressed.', sel: 'signup continue' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-bar', q('header, nav, [class*="sticky"], [class*="fixed"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone top bar (digg wordmark + menu trigger).', sel: 'mobile bar' }, { noScroll: true });
  await S('m-card', cardOf(q('[data-post-headline]').and(page.locator(':visible')).first()), ['default'], { group: g, title: 'Mobile card', desc: 'A story card at 390px.', sel: 'mobile post item' });
  await S('m-vote', cardOf(q('[data-post-headline]').first()).locator('button').and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile vote pill', desc: 'The digg-it vote pill at 390px.', sel: 'mobile vote' });
  await S('m-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); digg.com paints light and dark themes signed out — dark readings come from the sidebar pill cycle';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, dark, tech, story, profile, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a sidebar item's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a[class*="peer/menu-button"]');
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
