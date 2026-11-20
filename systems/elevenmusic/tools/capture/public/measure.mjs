// Measures elevenmusic.io's public components in every state reachable without
// signing in, creating, submitting or buying anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home explore charts pricing login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// elevenmusic.io is one Next.js App Router product over Tailwind v4 (a
// shadcn-style semantic token layer in lab() notation: --background/--card/
// --primary/--muted/--border/--sidebar-*/--surface-*/--lighten-*/--lift-*).
// It is an app shell — a fixed left rail, a header, an inner scroller per page,
// and a bottom player bar once a track plays — painting dark by default
// (html.dark). Nothing is sent, created, booked, bought or signed into: the
// only presses are local UI toggles — the header Resources dropdown, the
// sidebar Search button (which opens the sign-in dialog), a FAQ accordion, a
// track card's Play (local media playback that mounts the player bar; Like,
// Remix, Share and every Create are measured, never pressed), the mobile
// menu and the footer theme buttons. The Cookiebot overlay and Google's
// One-Tap prompt are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, findScroller, scrollMain, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', explore: '/explore', charts: '/charts', pricing: '/pricing', login: '/login' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
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
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline|start free|get pro|remix|like|attach|publish)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the plan card is the painted parent of its name),
// or falls back to marking a painted descendant.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

// markPainted returns a never-matching locator on a miss, never null, so a
// `marked || fallback` never falls back: choose by count() instead.
const orElse = async (loc, fallback) => ((loc && (await loc.count())) ? loc : fallback);

// Marks the sidebar rail: the fixed left column that holds the logo anchor and
// the primary nav (a plain div, not a landmark element).
async function sidebarLoc(tag = 'm-sidebar') {
  const ok = await page.evaluate((t) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const logo = document.querySelector('a[aria-label="ElevenMusic"]');
    if (!logo) return false;
    for (let n = logo.parentElement; n; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width >= 200 && r.width <= 320 && r.height >= 600 && r.left < 40) { n.setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, tag);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', explore: 'Explore and browse',
  charts: 'Charts', pricing: 'Pricing', auth: 'Log in and sign up',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

async function home() {
  if (!(await newPage('home', { wait: 12000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The fixed left rail: logo, Search, nav rows, promo card, playlists.
  await S('sidebar', await sidebarLoc(), ['default'], { group: g, title: 'Sidebar', desc: 'The fixed left rail (248px): logo, Search, primary nav, the Publish-your-music promo and the Playlists list.', sel: 'the fixed left rail ancestor of the logo anchor' }, { noScroll: true });
  await S('sidebar-nav', q('a[class*="group/row"]').filter({ hasText: /^\s*Tools\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar nav item', desc: 'A primary nav row in the rail (icon + label, 36px); Explore holds the selected state on /.', sel: 'sidebar a "Tools"' }, { noScroll: true });
  await S('sidebar-action', q('button').filter({ hasText: /^\s*Composer\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar action', desc: 'A gated rail action (Composer/Chat) that prompts sign-in; measured, never pressed.', sel: 'sidebar button "Composer"' }, { noScroll: true });
  await S('sidebar-promo', q('button').filter({ hasText: /Publish your music/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar promo', desc: 'The Publish-your-music promo card in the rail (surface-1 fill, artwork chip).', sel: 'button "Publish your music"' }, { noScroll: true });
  await S('playlist-row', q('a[href^="/playlists/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Playlist row', desc: 'A media row in the rail\'s Playlists list (36px art + name + Featured tag).', sel: 'sidebar a[href^="/playlists/"]' }, { noScroll: true });
  await S('icon-button', q('button[aria-label="Search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Icon button', desc: 'The rail\'s 30px Search icon button (opens the sign-in dialog).', sel: 'button[aria-label="Search"]' }, { noScroll: true });
  await S('sidebar-collapse', q('button[aria-label="Close sidebar"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar collapse', desc: 'The 32px rail-collapse icon button; measured, never pressed.', sel: 'button[aria-label="Close sidebar"]' }, { noScroll: true });
  await S('new-playlist-btn', q('button[aria-label="New playlist"]').filter({ visible: true }).first(), B4, { group: g, title: 'New-playlist button', desc: 'The 24px + button on the Playlists heading; measured, never pressed.', sel: 'button[aria-label="New playlist"]' }, { noScroll: true });
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The app header (52px, translucent lab(0 0 0 / .95)): Main nav, Sign in, Start free.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"], a[aria-label="ElevenMusic"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The ElevenMusic wordmark/mark anchor.', sel: 'a[aria-label="ElevenMusic"]' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header nav link', desc: 'A header nav link (28px pill); measured, never followed.', sel: 'header a "Pricing"' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*Resources\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Resources trigger', desc: 'The header Resources button that opens the dropdown; toggled for the open state.', sel: 'header button "Resources"' }, { noScroll: true });
  await S('signin-btn', q('header button').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The dark Sign-in pill (surface-2 fill); measured, never pressed.', sel: 'header button "Sign in"' }, { noScroll: true });
  await S('cta-btn', q('header button').filter({ hasText: /^\s*Start free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Start-free CTA', desc: 'The white Start-free pill (primary fill); measured, never pressed.', sel: 'header button "Start free"' }, { noScroll: true });
  // The Resources dropdown opens on click (a local UI toggle); hold it open
  // while the panel and one link are read, then Escape.
  try {
    const t = q('header button').filter({ hasText: /^\s*Resources\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await clickEl(t); await page.waitForTimeout(1000); }
  } catch (e) { log('  ! resources open failed', String(e.message).split('\n')[0]); }
  // The panel is the painted ancestor of one of its own menu links.
  const mlink = q('a').filter({ hasText: /Blog|Help center|Contact|ElevenLabs/ }).filter({ visible: true }).first();
  const panel = await mlink.evaluate((el) => {
    document.querySelectorAll('[data-m-mark="m-panel"]').forEach((n) => n.removeAttribute('data-m-mark'));
    for (let n = el; n; n = n.parentElement) {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      if (r.width >= 150 && r.height >= 60 && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none')) { n.setAttribute('data-m-mark', 'm-panel'); return true; }
    }
    return false;
  }).catch(() => false);
  await S('nav-dropdown', panel ? q('[data-m-mark="m-panel"]') : mlink, ['default'], { group: g, title: 'Resources dropdown', desc: 'The Resources menu panel (popover fill, opened by its own trigger).', sel: 'painted ancestor of a Resources menu link' }, { noScroll: true, noReset: true });
  await S('menu-link', q('div[data-state="open"] a, header a').filter({ hasText: /Blog|Help center|Contact|ElevenLabs/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened Resources dropdown.', sel: 'resources menu a' }, { noScroll: true, noReset: true,
    open: async () => { const t = q('header button').filter({ hasText: /^\s*Resources\s*$/ }).filter({ visible: true }).first(); if (await t.count()) { const s = await t.getAttribute('data-state'); if (s !== 'open') await clickEl(t); await page.waitForTimeout(800); } } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Make music yours." display headline (font-display light).', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('p').filter({ hasText: /Describe a sound|remix a track|start from a loop/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The muted lede under the headline.', sel: 'hero lede' });
  await S('composer-field', q('input.bg-transparent, input[class*="bg-transparent"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Composer field', desc: 'The prompt input in the hero composer (556px); sample text was typed and deleted, nothing sent.', sel: 'hero composer input' });
  await S('attach-btn', q('button[aria-label="Attach"], button[aria-label="Add audio"]').filter({ visible: true }).first(), B4, { group: h, title: 'Attach button', desc: 'The composer\'s 36px + button (black circle); measured, never pressed.', sel: 'button[aria-label="Attach"]' });
  // The composer's send control is the white 36px circle to the field's right;
  // the sidebar's 224px Create button shares the name, so take the last match
  // (the composer sits later in the DOM, inside main).
  await S('send-button', q('button').filter({ hasText: /^\s*Create\s*$/ }).filter({ visible: true }).last(), B4, { group: h, title: 'Send button', desc: 'The composer\'s white 36px circular send button (Create); measured, never pressed.', sel: 'composer send button' });
  await S('prompt-chip', q('button').filter({ hasText: /^\s*Trap beat\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Prompt chip', desc: 'A suggestion chip under the composer (lighten-100 fill, pill).', sel: 'button "Trap beat"' });
  await S('seg-tab-on', q('[role="tab"][data-state="active"]').filter({ visible: true }).first(), B4, { group: h, title: 'Segmented tab, selected', desc: 'The selected segment (Songs) of the Songs/Sounds control (lighten-150 fill).', sel: '[role=tab][data-state=active]' });
  await S('seg-tab-off', q('[role="tab"][data-state="inactive"]').filter({ visible: true }).first(), B4, { group: h, title: 'Segmented tab', desc: 'An unselected segment (Sounds/Featured rail tabs).', sel: '[role=tab][data-state=inactive]' });
  // A demo song row is a wide (400px+) labelled button in the hero demo list.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-trow"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const t = [...document.querySelectorAll('button[aria-label]')].find((n) => { const r = n.getBoundingClientRect(); return r.width >= 400 && r.height >= 40 && r.height <= 80; });
    if (t) t.setAttribute('data-m-mark', 'm-trow');
  });
  await S('track-row', q('[data-m-mark="m-trow"]'), B4, { group: h, title: 'Track row', desc: 'A song row in the demo list (art + title + artist); measured, never pressed.', sel: 'wide labelled button in the hero demo' });
  await S('demo-card', q('button').filter({ hasText: /boom bap|Warm upright|Rhodes|soul chop/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Stem card', desc: 'A stem/description card in the hero demo (surface-1 fill).', sel: 'hero stem card' });
  await S('carousel-prev', q('button[aria-label="Previous"]').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel previous', desc: 'The 32px frosted carousel arrow.', sel: 'button[aria-label="Previous"]' });
  await S('carousel-next', q('button[aria-label="Next"]').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel next', desc: 'The 32px frosted carousel arrow.', sel: 'button[aria-label="Next"]' });
  await S('carousel-dot', q('button[aria-label^="Go to"]').filter({ visible: true }).first(), B4, { group: h, title: 'Carousel dot', desc: 'A carousel pagination dot (the active one is a white 32x6 pill).', sel: 'button[aria-label^="Go to"]' });
  await S('play-hero', q('button[aria-label^="Play "], button[aria-label="Play"]').filter({ visible: true }).first(), B4, { group: h, title: 'Round play button', desc: 'A white circular play button (36-48px); measured, never pressed here.', sel: 'button[aria-label^="Play"]' });
  save();
}

async function explore() {
  if (!(await newPage('explore', { wait: 12000 }))) return;
  await sheetsFor('explore');
  await chrome('explore');
  const g = G.explore;
  await S('sidebar-nav-selected', q('a[class*="group/row"]').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).first(), ['selected'], { group: g, title: 'Sidebar nav item, selected', desc: 'The Explore row held selected on its own page.', sel: 'sidebar a "Explore"' }, { noScroll: true, noToggle: true });
  await S('explore-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Explore title', desc: 'The "Create music" page heading.', sel: 'h1 on /explore' }, { noScroll: true });
  await S('create-nav', q('nav[aria-label="Create"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Create nav', desc: 'The pill nav under the title (Create/Composer/Styles/Sounds/Library — every item gated behind sign-in).', sel: 'nav[aria-label="Create"]' });
  await S('explore-input', q('input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Prompt input', desc: 'The "Describe your song" prompt field (556px); sample text typed and deleted, nothing sent.', sel: 'explore prompt input' });
  // The featured carousel card: the big artwork card with its Remix chip.
  await S('feature-card', await orElse(await markPainted('button[aria-label^="Play"]', 'm-feat', { minW: 200, minH: 200, maxUp: 10 }).catch(() => null), q('[role="group"]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Feature card', desc: 'The featured track\'s carousel card (artwork, title, artist, Remix chip).', sel: 'painted ancestor of the feature play button' });
  await S('play-feature', q('button[aria-label^="Play "], button[aria-label="Play track"]').filter({ visible: true }).first(), B4, { group: g, title: 'Card play button', desc: 'The 36px play control on a feature card; pressed once below to mount the player bar.', sel: 'button[aria-label^="Play "]' });
  await S('remix-chip', q('button, a').filter({ hasText: /^\s*Remix\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Remix chip', desc: 'The Remix chip on a feature card; measured, never pressed (gated).', sel: 'feature card "Remix"' });
  await S('track-card', q('[role="group"]').filter({ hasText: /v\d\.\d|Remix|v2\.5/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Track card', desc: 'A 208px track card in a shelf (artwork, title, artist, version badge); hover raises the play button.', sel: 'role=group track card' });
  await S('play-track', q('button[aria-label="Play track"]').filter({ visible: true }).first(), B4, { group: g, title: 'Track play button', desc: 'The white 32px circular play button a card raises on hover.', sel: 'button[aria-label="Play track"]' },
    { open: async () => { const c = q('[role="group"]').filter({ visible: true }).first(); if (await c.count()) await c.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(600); } });
  await S('version-badge', q('span').filter({ hasText: /^\s*v\d\.\d\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Version badge', desc: 'The "v2.5" badge on track cards.', sel: 'version badge span' });
  // A genre tile is the tile-sized ancestor of a "Play playlist" button —
  // the tiles are clickable divs, not anchors (genre anchors only appear as
  // footer text links).
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-genre"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const b = document.querySelector('button[aria-label="Play playlist"]');
    if (!b) return;
    for (let n = b; n; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width >= 120 && r.width <= 300 && r.height >= 60 && r.height <= 400) { n.setAttribute('data-m-mark', 'm-genre'); break; }
      if (r.width > 300 || r.height > 400) break;
    }
  });
  await S('genre-card', q('[data-m-mark="m-genre"]'), B4, { group: g, title: 'Genre card', desc: 'A genre tile in Genres & Moods (artwork + name + play chip).', sel: 'tile ancestor of a "Play playlist" button' });
  await S('play-genre', q('button[aria-label="Play playlist"]').filter({ visible: true }).first(), B4, { group: g, title: 'Genre play button', desc: 'The white 25px circular play button on a genre tile.', sel: 'button[aria-label="Play playlist"]' });
  await S('artist-link', q('a[href^="/artists/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Artist link', desc: 'An artist-name link under a track title; measured, never followed.', sel: 'a[href^="/artists/"]' });
  await S('shelf-heading', q('h2').filter({ hasText: /Featured|Genres|Moods|Trending|New/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Shelf heading', desc: 'A shelf heading ("Featured", "Genres & Moods").', sel: 'h2 shelf heading' });
  save();
  // Mount the player bar: press one card's own Play (local media playback —
  // Like, Remix and Share are never touched).
  try {
    const t = q('button[aria-label^="Play "], button[aria-label="Play track"]').filter({ visible: true }).first();
    if (await t.count()) { await clickEl(t); await page.waitForTimeout(3500); }
  } catch (e) { log('  ! play failed', String(e.message).split('\n')[0]); }
  const pg = 'Player';
  const pauseBtn = q('button[aria-label="Pause"]').filter({ visible: true }).first();
  const bar = await markPainted('button[aria-label="Pause"]', 'm-player', { minW: 600, minH: 40, maxUp: 12 }).catch(() => null);
  // No footer fallback: when Play mounts no player, player-bar is recorded missing, not
  // the 708px site footer under the player's name.
  await S('player-bar', bar, ['default'], { group: pg, title: 'Player bar', desc: 'The bottom transport bar mounted by pressing a card\'s Play (art, progress, transport, volume).', sel: 'painted ancestor of the pause button' }, { noScroll: true });
  await S('player-play', pauseBtn, B4, { group: pg, title: 'Player play/pause', desc: 'The transport\'s central pause button (a playing track).', sel: 'button[aria-label="Pause"]' }, { noScroll: true });
  // Previous/next carry no accessible name: they are the transport buttons
  // immediately before and after Pause in DOM order.
  await S('player-prev', pauseBtn.locator('xpath=preceding::button[1]'), B4, { group: pg, title: 'Player previous', desc: 'The transport previous button (the unlabeled control before Pause).', sel: 'button before transport Pause' }, { noScroll: true });
  await S('player-next', pauseBtn.locator('xpath=following::button[1]'), B4, { group: pg, title: 'Player next', desc: 'The transport next button (the unlabeled control after Pause).', sel: 'button after transport Pause' }, { noScroll: true });
  await S('player-repeat', q('button[aria-label="Repeat"]').filter({ visible: true }).first(), B4, { group: pg, title: 'Player repeat', desc: 'The transport repeat toggle.', sel: 'button[aria-label="Repeat"]' }, { noScroll: true });
  await S('player-volume', q('button[aria-label="Volume"]').filter({ visible: true }).first(), B4, { group: pg, title: 'Player volume', desc: 'The transport volume control.', sel: 'button[aria-label="Volume"]' }, { noScroll: true });
  await S('player-queue', q('button[aria-label="Queue"]').filter({ visible: true }).first(), B4, { group: pg, title: 'Player queue', desc: 'The transport queue button.', sel: 'button[aria-label="Queue"]' }, { noScroll: true });
  await S('player-remix', q('button[aria-label="Remix"]').filter({ visible: true }).last(), B4, { group: pg, title: 'Player remix', desc: 'The transport Remix button; measured, never pressed (gated).', sel: 'transport Remix' }, { noScroll: true });
  // The seek rail: a thin bar-height track inside the player.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-seek"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const pause = document.querySelector('button[aria-label="Pause"]');
    if (!pause) return;
    let bar = pause;
    for (let n = pause; n; n = n.parentElement) { if (n.getBoundingClientRect().width > 600) { bar = n; break; } }
    const cands = [...bar.querySelectorAll('div, [role="progressbar"], [role="slider"]')].filter((n) => { const r = n.getBoundingClientRect(); return r.width > 200 && r.height > 0 && r.height <= 12; });
    if (cands[0]) cands[0].setAttribute('data-m-mark', 'm-seek');
  });
  await S('player-progress', q('[data-m-mark="m-seek"]'), ['default'], { group: pg, title: 'Player progress', desc: 'The seek rail across the player\'s top edge.', sel: 'thin wide rail inside the player bar' }, { noScroll: true });
  save();
}

async function charts() {
  if (!(await newPage('charts', { wait: 11000 }))) return;
  await sheetsFor('charts');
  await chrome('charts');
  const g = G.charts;
  await S('charts-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Charts title', desc: 'The charts page heading.', sel: 'h1 on /charts' }, { noScroll: true });
  await S('chart-play', q('button').filter({ hasText: /^\s*Play\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Play-all button', desc: 'The white 40px Play pill at the top of the chart.', sel: 'button "Play"' });
  await S('shuffle-btn', q('button').filter({ hasText: /^\s*Shuffle\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Shuffle button', desc: 'The 40px Shuffle pill next to Play.', sel: 'button "Shuffle"' });
  await S('share-btn', q('button').filter({ hasText: /^\s*Share\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Share button', desc: 'The 32px Share pill; measured, never pressed.', sel: 'button "Share"' });
  // A chart row is the row-height ancestor of an artist link (40-120px tall).
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-crow"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const a = document.querySelector('a[href^="/artists/"]');
    if (!a) return;
    for (let n = a; n; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.height >= 40 && r.height <= 120 && r.width >= 400) { n.setAttribute('data-m-mark', 'm-crow'); break; }
    }
  });
  await S('chart-row', q('[data-m-mark="m-crow"]'), B4, { group: g, title: 'Chart row', desc: 'A ranked chart row (rank, art, title, artist, Like/Remix icons).', sel: 'row-height ancestor of an artist link' });
  await S('like-btn', q('button[aria-label="Like"]').filter({ visible: true }).first(), B4, { group: g, title: 'Like button', desc: 'A row\'s 32px heart icon button; measured, never pressed (gated).', sel: 'button[aria-label="Like"]' });
  await S('remix-btn', q('button[aria-label="Remix"]').filter({ visible: true }).first(), B4, { group: g, title: 'Remix button', desc: 'A row\'s 32px Remix icon button; measured, never pressed (gated).', sel: 'button[aria-label="Remix"]' });
  await S('chart-artist', q('a[href^="/artists/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Chart artist link', desc: 'An artist link inside a chart row.', sel: 'chart row a[href^="/artists/"]' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1, h2').filter({ hasText: /Free to start|Pro when/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Free to start. Pro when you\'re ready." heading.', sel: 'pricing heading' }, { noScroll: true });
  // Mark the two plan cards: the smallest painted ancestor of each plan
  // heading that is card-sized (bounded so the page's own painted field —
  // which is also an ancestor — can never be picked).
  const markCard = (needle, tag) => page.evaluate(([re, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const rx = new RegExp(re, 'i');
    const h = [...document.querySelectorAll('h1, h2, h3, h4, p, span, li, div')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 0 && r.width < 900 && rx.test(n.innerText || '');
    });
    if (!h) return false;
    for (let n = h; n; n = n.parentElement) {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      // The plan cards are tall (909px): bound generously but below the
      // page-sized ancestors.
      if (r.width > 300 && r.width < 900 && r.height > 250 && r.height < 1200 &&
          (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' || cs.borderTopWidth !== '0px')) { n.setAttribute('data-m-mark', t); return true; }
      if (r.width >= 900 || r.height >= 1200) break;
    }
    return false;
  }, [needle, tag]);
  const freeCard = await markCard('songs a day|^\\s*Free\\s*$', 'm-free');
  const proCard = await markCard('songs a month|^\\s*Pro\\s*$', 'm-pro');
  await S('plan-card', freeCard ? q('[data-m-mark="m-free"]') : q('[data-m-mark="__none__"]'), ['default'], { group: g, title: 'Plan card, Free', desc: 'The Free plan card (dark surface, hairline border).', sel: 'painted ancestor of the Free plan' });
  await S('plan-card-pro', proCard ? q('[data-m-mark="m-pro"]') : q('[data-m-mark="__none__"]'), ['default'], { group: g, title: 'Plan card, Pro', desc: 'The Pro plan card — an inverted white island on the dark page.', sel: 'painted ancestor of the Pro plan' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^\s*\$9\.99\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The $9.99/month price figure on the Pro card.', sel: 'Pro price figure' });
  await S('plan-feature', q('li').filter({ hasText: /songs a month|songs a day|Commercial use|Unlimited downloads/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan feature row', desc: 'A checked feature row inside a plan card.', sel: 'plan feature li' });
  await S('plan-cta-free', q('a').filter({ hasText: /^\s*Start free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA, Free', desc: 'The Start-free pill on the Free card (white fill on dark); measured, never followed.', sel: 'a "Start free"' });
  await S('plan-cta-pro', q('a').filter({ hasText: /^\s*Get Pro\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA, Pro', desc: 'The Get-Pro pill on the Pro card (dark fill on the white island); measured, never followed.', sel: 'a "Get Pro"' });
  await S('faq-item', q('button').filter({ hasText: /Is it free\?|What can I make\?/ }).filter({ visible: true }).first(), [...B4, 'expanded'], { group: g, title: 'FAQ accordion', desc: 'A pricing FAQ row (68px, border-t); the expanded state was opened by its own toggle.', sel: 'pricing faq button' },
    { before: { expanded: async (loc) => { const s = await loc.getAttribute('data-state'); if (s !== 'open') await clickEl(loc); await page.waitForTimeout(900); return 'own accordion toggle' } },
      // close it again, or faq-answer (the same row) is read open but labelled default
      after: { expanded: async (loc) => { if ((await loc.getAttribute('data-state')) === 'open') { await clickEl(loc); await page.waitForTimeout(700); } } } });
  await S('faq-answer', q('button').filter({ hasText: /Is it free\?|What can I make\?/ }).filter({ visible: true }).first().locator('xpath=ancestor::*[self::div or self::section][1]'), ['default'], { group: g, title: 'FAQ row', desc: 'The accordion item wrapper (question + answer region).', sel: 'faq item wrapper' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  // The centred auth card: the smallest painted ancestor of the Google SSO
  // button bounded to card size (the page's own painted field is an ancestor
  // too and must never be picked).
  // The auth surface on /login is not a painted card — it is a bare centred
  // 384px column on the black page. Mark the largest column still inside the
  // bounds (title + form), whatever it paints.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="m-login"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const b = [...document.querySelectorAll('button')].find((n) => /Continue with Google/.test(n.innerText || ''));
    if (!b) return;
    let best = null;
    for (let n = b; n; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width >= 300 && r.width < 900 && r.height >= 250 && r.height <= 880) { best = n; continue; }
      if (r.width >= 900 || r.height > 880) break;
    }
    if (best) best.setAttribute('data-m-mark', 'm-login');
  });
  await S('auth-card', q('[data-m-mark="m-login"]'), ['default'], { group: g, title: 'Auth column', desc: 'The centred 384px log-in/sign-up column on the bare page; nothing submitted.', sel: 'centred ancestor of the Google SSO button' });
  await S('auth-title', q('h1, h2, p').filter({ hasText: /Log in or sign up/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth title', desc: 'The "Log in or sign up" heading.', sel: 'auth heading' });
  await S('sso-google', q('button').filter({ hasText: /Continue with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO button', desc: 'The Continue-with-Google button (surface-1 fill, 40px); measured, never pressed.', sel: 'button "Continue with Google"' });
  await S('sso-apple', q('button').filter({ hasText: /Continue with Apple/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple SSO button', desc: 'The Continue-with-Apple button; measured, never pressed.', sel: 'button "Continue with Apple"' });
  await S('options-btn', q('button').filter({ hasText: /Show other options|Hide other options/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Other-options toggle', desc: 'The Show-other-options button that expands the email form in place; toggled for the expanded state, never submitted.', sel: 'button "Show other options"' });
  // Expand the email form (a local UI reveal), then measure the field, the
  // checkbox and the disabled submit.
  try {
    const t = q('button').filter({ hasText: /Show other options/ }).filter({ visible: true }).first();
    if (await t.count()) { await clickEl(t); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! options expand failed', String(e.message).split('\n')[0]); }
  await S('email-field', q('input[type="email"], input[placeholder*="email" i], input[name*="email" i], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The Enter-email-address input revealed by the options toggle; sample text was typed and deleted, nothing sent.', sel: 'login input' });
  await S('tos-checkbox', q('input[type="checkbox"], [role="checkbox"]').filter({ visible: true }).first(), B4, { group: g, title: 'Terms checkbox', desc: 'The agree-to-Terms checkbox; measured, never checked.', sel: 'login checkbox' });
  await S('continue-btn', q('button').filter({ hasText: /Continue with Email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The Continue-with-Email submit (disabled until the box is checked); measured, never pressed.', sel: 'button "Continue with Email"' });
  await S('tos-link', q('a').filter({ hasText: /Terms of Service/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Terms link', desc: 'An underlined legal link; measured, never followed.', sel: 'a "Terms of Service"' });
  await S('tryit-link', q('a').filter({ hasText: /Try it first/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Try-it link', desc: 'The muted Try-it-first link under the form.', sel: 'a "Try it first"' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 8000 }))) return;
  const g = G.footer;
  // The page scrolls inside one inner element: run it to the bottom so the
  // footer mounts, then measure.
  const sc = await findScroller(page);
  if (sc) { await scrollMain(page, 'bottom'); await page.waitForTimeout(1800); }
  else { await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight)); await page.waitForTimeout(1500); }
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The site footer inside the shell: language selector, link columns, legal and the theme control.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Browse tracks|Charts|Blog/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer column link (36px row).', sel: 'footer a' }, { noScroll: true });
  await S('lang-btn', q('button').filter({ hasText: /^\s*English\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Language selector', desc: 'The English locale button; measured, never opened.', sel: 'button "English"' }, { noScroll: true });
  await S('cookie-btn', q('button').filter({ hasText: /Cookie settings/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie settings', desc: 'The Cookie-settings button (opens Cookiebot; measured, never pressed).', sel: 'button "Cookie settings"' }, { noScroll: true });
  await S('theme-seg', q('button[aria-label="Dark theme"]').filter({ visible: true }).first().locator('xpath=ancestor::*[self::div or self::span][1]'), ['default'], { group: g, title: 'Theme control', desc: 'The System/Light/Dark segmented control in the footer.', sel: 'theme segmented control' }, { noScroll: true });
  await S('theme-dark-btn', q('button[aria-label="Dark theme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme dark button', desc: 'The Dark segment of the theme control (selected when the page paints dark).', sel: 'button[aria-label="Dark theme"]' }, { noScroll: true });
  await S('theme-light-btn', q('button[aria-label="Light theme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme light button', desc: 'The Light segment of the theme control; measured, never pressed here (the light pass toggles it).', sel: 'button[aria-label="Light theme"]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 12000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The compact header at 390: mark, Search, Start free, menu.', sel: 'header at 390' }, { noScroll: true });
  await S('m-logo', q('a[aria-label="ElevenMusic"], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile logo', desc: 'The mark at 390.', sel: 'mobile logo' }, { noScroll: true });
  await S('m-search-btn', q('button[aria-label="Open search"], button[aria-label="Search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile search button', desc: 'The header search icon at 390.', sel: 'button[aria-label="Open search"]' }, { noScroll: true });
  await S('m-cta', q('a, button').filter({ hasText: /^\s*Start free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The Start-free pill at 390.', sel: '"Start free" at 390' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The "Make music yours." headline at 390.', sel: 'h1 at 390' });
  await S('m-composer', q('input').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile composer', desc: 'The prompt field at 390.', sel: 'composer input at 390' });
  await S('m-chip', q('button').filter({ hasText: /^\s*Trap beat\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile prompt chip', desc: 'A suggestion chip at 390.', sel: 'prompt chip at 390' });
  // The bottom tab bar (Explore / Create / Library) pinned to the viewport.
  const bar = await page.evaluate(() => {
    const els = [...document.querySelectorAll('a, button')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return (cs.position === 'fixed' || cs.position === 'sticky' || r.top > 700) && r.height < 90 && r.width > 60 && /Explore/.test(n.textContent || '');
    });
    const t = els[0]; if (!t) return false;
    for (let n = t; n; n = n.parentElement) { const r = n.getBoundingClientRect(); if (r.width > 300 && r.height > 40 && r.height < 120) { n.setAttribute('data-m-mark', 'm-tabbar'); return true; } }
    return false;
  });
  await S('m-tab-bar', bar ? q('[data-m-mark="m-tabbar"]') : q('nav').filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile tab bar', desc: 'The bottom tab bar pinned to the viewport (Explore / Create / Library).', sel: 'bottom tab bar at 390' }, { noScroll: true });
  await S('m-tab', q('a, button').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Mobile tab', desc: 'A tab-bar item (the selected Explore tab).', sel: 'tab bar item' }, { noScroll: true });
  // The hamburger opens a fullscreen dialog sheet — a local UI toggle,
  // dismissed after.
  const menu = q('button[aria-label="Open menu"], header button').filter({ visible: true }).last();
  await S('m-menu-btn', menu, B4, { group: g, title: 'Mobile menu button', desc: 'The header hamburger.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  try {
    if (await menu.count()) { await clickEl(menu); await page.waitForTimeout(1400); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-sheet', q('div[role="dialog"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The fullscreen nav sheet the hamburger opens (measured, then dismissed).', sel: 'mobile menu dialog' }, { noScroll: true, noReset: true });
  await S('m-menu-link', q('div[role="dialog"] a, div[role="dialog"] button').filter({ hasText: /Pricing|Explore|Sign in/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu link', desc: 'A link inside the open nav sheet.', sel: 'sheet link' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the app paints dark by default (html.dark)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, explore, charts, pricing, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a header nav link),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a');
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
