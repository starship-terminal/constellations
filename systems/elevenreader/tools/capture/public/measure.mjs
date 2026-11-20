// Measures elevenreader.io's public components in every state reachable
// without signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home explore pricing audiobook compare signin signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// elevenreader.io is a Next.js marketing site over Tailwind v4 (a declared
// --themed-*/--color-* token layer with a .dark scope that nothing on the
// public surface applies, f-* type styles, Inter + Waldenburg HT): the home,
// pricing, explore, collections, genres, free-audiobooks, iconic-voices,
// compare and blog pages, one public audiobook page, and the /reader/sign-in
// and sign-up cards. Nothing is sent, bought or signed into: the only presses
// are local UI toggles — the header Discover mega-menu, the Monthly/Annual
// billing toggle, a FAQ <details>, a footer column and the mobile menu.
// The Cookiebot banner is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, CROPS, REF, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', explore: '/explore', pricing: '/pricing',
  audiobook: '/audiobooks/the-art-of-war-audiobook/CrZjqfHD4d1FYEemlTHB',
  compare: '/compare', signin: '/reader/sign-in', signup: '/reader/sign-up',
};
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
      } catch (e) {
        s.cropError = String(e.message || e).slice(0, 120);
        // The PNG is saved before post-processing runs: a failed quantize or
        // convert must not unlink an image that landed on disk. Keep the path
        // next to the error so the documents still print the crop.
        const png = path.join(CROPS, `${key}-${state}.png`);
        if (fs.existsSync(png)) file = path.relative(REF, png);
      }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
// A <details> opened for its `open` reading is closed again, or the next entry on
// the same node (its summary) is read open but labelled default.
const closeDetails = async (l) => { await l.filter({ visible: true }).first().evaluate((el) => { el.open = false; }); await page.waitForTimeout(400); };


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
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
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

// Marks the widest element matching sel: for repeated media like the hero
// orbit's cover cards, where first-match lands on an edge-on card.
async function markWidest(sel, tag) {
  const ok = await page.evaluate(([s, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const els = [...document.querySelectorAll(s)].filter((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!els.length) return false;
    els.sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width);
    els[0].setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home sections',
  explore: 'Explore catalog', pricing: 'Pricing', audiobook: 'Audiobook page',
  compare: 'Compare', auth: 'Sign in and sign up',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The promo banner is the thin strip above the header (bg #F5F3F1).
  await S('promo-banner', q('div[class*="bg-[#F5F3F1]"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The announcement strip above the header (a #F5F3F1 band, here the Black-Friday offer).', sel: 'div.bg-[#F5F3F1]' }, { noScroll: true });
  await S('promo-cta', q('div[class*="bg-[#F5F3F1]"] a, a').filter({ hasText: /Get this offer/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Promo CTA', desc: 'The Get-this-offer pill inside the banner; measured never followed (it opens the subscribe flow).', sel: 'a "Get this offer"' }, { noScroll: true });
  // The header is a div bar (no <header> element): logo, the radix Main nav,
  // Sign in and the dark Start-listening pill.
  await S('header', q('div:has(> nav[aria-label="Main"])').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The top bar: wordmark, the Main nav (Explore, Discover, Pricing, For Authors, Upload & Listen), Sign in and the dark Start-listening pill.', sel: 'div:has(> nav[aria-label="Main"])' }, { noScroll: true });
  await S('logo', q('nav[aria-label="Main"] ~ * a, div.z-10 a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The ElevenReader wordmark anchor (a 140x15 webp).', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('nav[aria-label="Main"] a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header nav link (rounded-full, hover bg-surface).', sel: 'nav a "Pricing"' }, { noScroll: true });
  await S('nav-discover', q('button[aria-label="Discover"]').filter({ visible: true }).first(), B4, { group: g, title: 'Discover trigger', desc: 'The chevron button that opens the Discover mega-menu; toggled for the panel readings, then closed.', sel: 'button[aria-label="Discover"]' }, { noScroll: true });
  await S('nav-signin', q('a').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The outlined Sign-in pill (bg-default + border, hover bg-surface); measured never followed.', sel: 'a "Sign in"' }, { noScroll: true });
  await S('nav-cta', q('a').filter({ hasText: /Start listening/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The dark Start-listening-free pill (bg-inverse text-inverse, hover bg-darkest); measured never followed.', sel: 'a "Start listening free"' }, { noScroll: true });
  // The Discover trigger opens the mega-menu (genres, collections, the free
  // audiobook cover grid); keep the menu open while the panel and one link
  // are read (noReset), then Escape to close.
  const openDiscover = async () => {
    const t = q('button[aria-label="Discover"]').filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1200); }
  };
  try { await openDiscover(); } catch (e) { log('  ! discover open failed', String(e.message).split('\n')[0]); }
  const panel = await markPainted('a[href*="/genres/"], a[href*="/collections/"]', 'm-panel', { minW: 300, minH: 150 }).catch(() => null);
  await S('nav-dropdown', await orElse(panel, q('[class*="absolute"][class*="top-full"]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Discover mega-menu', desc: 'The Discover dropdown panel (Popular Genres, Trending Collections, Free Audiobooks cover grid), opened by its own trigger.', sel: 'discover panel' }, { noScroll: true, noReset: true });
  await S('menu-link', q('a').filter({ hasText: /^\s*(Romance|Mystery|Science Fiction|Fantasy|Horror|Fan Fiction)\b/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A genre link inside the opened mega-menu.', sel: 'mega-menu a' }, { noScroll: true, noReset: true, open: openDiscover });
  await S('menu-heading', q('p, div, span, h3, h4').filter({ hasText: /^\s*(Popular Genres|Trending Collections|Free Audiobooks)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu column heading', desc: 'A column heading inside the mega-menu.', sel: 'mega-menu heading' }, { noScroll: true, noReset: true, open: openDiscover });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.hero;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 60px Waldenburg display headline (40px under lg).', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('h2, p').filter({ hasText: /Read aloud your books/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The 18px opacity-60 lede under the headline.', sel: 'hero lede (opacity-60)' });
  await S('hero-cta', q('main a:not([tabindex="-1"])').filter({ hasText: /Start listening free/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The dark Start-listening-free pill under the lede; measured never followed.', sel: 'main a "Start listening free"' });
  await S('hero-cta-2', q('main a:not([tabindex="-1"])').filter({ hasText: /Upload &\s*listen|Explore the library/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary CTA', desc: 'The white shadowed pill beside the dark CTA (bg-default, layered ring shadow, active scale-98).', sel: 'hero secondary pill' });
  // The 3D book-orbit carousel under the hero: one cover card measured as the
  // product's media tile (rounded-md, gray-300 backing, grab cursor).
  await S('book-cover', await markWidest('[data-card-index]', 'm-cover'), ['default', 'hover'], { group: h, title: 'Book cover card', desc: 'A cover card in the hero orbit carousel (rounded-md, cover img on a gray-300 backing); the front-most (widest) card is read.', sel: '[data-card-index]' });
  const s = G.home;
  await S('eyebrow', q('h2').filter({ hasText: /Read anything aloud/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Section eyebrow', desc: 'The small medium-weight section eyebrow (opacity-60).', sel: 'h2 eyebrow' });
  await S('section-h3', q('h3').filter({ hasText: /This is how listening should feel/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A 36px Waldenburg section heading (30px under lg).', sel: 'h3.font-waldenburg' });
  await S('book-link', q('a[class*="underline-offset-2"]').filter({ visible: true }).first(), B4, { group: s, title: 'Book link', desc: 'A title link in a book row (text-inherit, underline on hover/focus).', sel: 'a.underline-offset-2' });
  await S('genre-chip', q('button').filter({ hasText: /^\s*(Fantasy|Mystery & Thriller|Romance|True Crime|Adventure|Fiction)\s*$/ }).filter({ visible: true }).first(), B4, { group: s, title: 'Genre chip', desc: 'A genre filter chip in Trending genres (rounded-full); measured, never pressed (a press navigates).', sel: 'genre chip button' });
  await S('view-all', q('a').filter({ hasText: /^\s*View all\s*$/i }).filter({ visible: true }).first(), B4, { group: s, title: 'View-all link', desc: 'The ghost View-all link on a section rail.', sel: 'a "View all"' });
  await S('try-cta', q('a').filter({ hasText: /^\s*Try it free\s*$/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Try-free CTA', desc: 'A mid-page Try-it-free white pill (bg-default shadow, active scale-98); measured never followed.', sel: 'a "Try it free"' });
  // FAQ: the page's own <details> accordions. The open reading is the same
  // node after its own summary was clicked (a local UI toggle).
  const openSummary = async (loc) => {
    const sm = loc.locator('summary').first();
    await sm.click({ timeout: 4000 }).catch(() => sm.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    return 'opened by its own summary';
  };
  const faq = q('details[name="homepage-faq"], details').filter({ hasText: /What voices are available|How much does/i }).filter({ visible: true }).first();
  await S('faq-item', faq, ['default', 'open'], { group: s, title: 'FAQ item', desc: 'A homepage FAQ <details>; the open state is the item after its own summary was clicked.', sel: 'details[name=homepage-faq]' }, { before: { open: openSummary }, after: { open: closeDetails } });
  await S('faq-summary', q('details summary').filter({ hasText: /What voices|How much/i }).filter({ visible: true }).first(), B4, { group: s, title: 'FAQ summary', desc: 'The clickable FAQ question row (with the +/- indicator); a press toggles its details.', sel: 'details summary' });
  save();
}

async function explore() {
  if (!(await newPage('explore'))) return;
  await sheetsFor('explore');
  await chrome('explore');
  const g = G.explore;
  await S('explore-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Explore headline', desc: 'The "Find your next audiobook" Waldenburg heading (text-4xl lg).', sel: 'h1 on /explore' }, { noScroll: true });
  await S('rail-h2', q('h2').filter({ hasText: /Top picks|What's trending/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Rail heading', desc: 'A carousel rail heading (Top picks, What\'s trending).', sel: 'rail h2' });
  await S('coverflow-card', q('[data-coverflow-card]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Coverflow card', desc: 'A cover card in an explore rail (2:3 cover on bg-hovered, rounded-md shadow-lg, group-hover scale-105).', sel: '[data-coverflow-card]' });
  await S('book-title', q('[data-coverflow-card] ~ a, [data-slide-index] a').filter({ visible: true }).first(), B4, { group: g, title: 'Book title link', desc: 'The title link under a cover (text-base font-medium, group-hover underline).', sel: 'coverflow title a' });
  await S('book-meta', q('[data-slide-index] span[variant="subtle"], [data-slide-index] span[class*="text-label"], a[href*="/audiobooks/"] span[variant="subtle"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Book meta', desc: 'An author/length label under a cover (variant=subtle, text-label).', sel: 'coverflow span[variant=subtle]' });
  await S('genre-link', q('a[href*="/genres/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Genre link', desc: 'A genre link in the catalog; measured never followed.', sel: 'a[href*="/genres/"]' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1, h3').filter({ hasText: /Your reading, made effortless/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The 60px Waldenburg pricing display heading.', sel: 'pricing display h3' }, { noScroll: true });
  await S('billing-off', q('button').filter({ hasText: /^\s*Monthly\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing option (idle)', desc: 'The unselected Monthly segment (#57534F text, hover black), read at rest, on hover, on keyboard focus and forced pressed; never clicked or checked out.', sel: 'button "Monthly"' }, { noScroll: true });
  await S('billing-on', q('button').filter({ hasText: /Annual/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing option (selected)', desc: 'The selected Annual segment (white pill, ring shadow, the green Save-25% chip).', sel: 'button "Annual"' }, { noScroll: true });
  await S('save-badge', q('span').filter({ hasText: /^\s*Save\s+\d+%\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Save badge', desc: 'The green Save-25% chip inside the Annual segment (#E1F5E0 bg, #307D18 text).', sel: 'span "Save 25%"' }, { noScroll: true });
  const card = await markPainted('h4, [class*="plan" i]', 'm-plan', { minW: 220, minH: 260 }).catch(() => null);
  await S('plan-card', await orElse(card, q('div[class*="rounded"][class*="border"], div[class*="shadow"]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted ancestor of the plan name).', sel: 'plan card' });
  await S('plan-name', q('h4, h3, p, div').filter({ hasText: /^\s*(Free|Ultra|Premium|Plus)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name.', sel: 'plan name' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^\s*\$\d+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure.', sel: 'plan price' });
  await S('plan-cta', q('a, button').filter({ hasText: /free trial|Get started|Try free|Start free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action (Start-3-day-free-trial pill); measured never followed.', sel: 'plan CTA' });
  // Scope to a page section: bare `li` and even `main li` land on nav rows —
  // the header menu lives outside main but a fixed clone of it sits inside —
  // while the plan feature rows are `section` descendants.
  await S('feature-li', q('main section li').filter({ hasText: /\S{5,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row', desc: 'A feature row inside a plan card or the "Everything you unlock" list.', sel: 'main section li' });
  save();
}

async function audiobook() {
  if (!(await newPage('audiobook', { wait: 9000 }))) return;
  await sheetsFor('audiobook');
  await chrome('audiobook');
  const g = G.audiobook;
  await S('ab-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Title', desc: 'The audiobook title heading.', sel: 'h1' });
  await S('ab-cover', q('main img[sizes="100vw"], main img').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cover', desc: 'The square audiobook cover (8px radius, blurred-thumb placeholder).', sel: 'audiobook cover img' }, { cropLoc: q('main img[sizes="100vw"], main img').filter({ visible: true }).first() });
  await S('ab-preview', q('button').filter({ hasText: /^\s*Preview\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Preview button', desc: 'The audio Preview button (speaker icon); measured, never pressed (a press plays audio).', sel: 'button "Preview"' });
  await S('ab-chip', q('div').filter({ hasText: /^\s*Audio only\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Format chip', desc: 'The "Audio only" format chip.', sel: '"Audio only" chip' });
  // The bare `a` first-match landed on the header's Explore pill; scope to the
  // page body so the link is the audiobook's breadcrumb above the title.
  await S('ab-crumb', q('main a').filter({ hasText: /^\s*(Explore|History|Audiobooks|Fantasy|Fiction)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Breadcrumb link', desc: 'A breadcrumb link (Explore / genre) above the title.', sel: 'main breadcrumb a' });
  await S('ab-author', q('a[href*="/authors/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Author link', desc: 'The By-author link under the title.', sel: 'a[href*="/authors/"]' });
  await S('ab-row', q('a[href*="/audiobooks/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Related title link', desc: 'A related-audiobook link in "More from" / "You may also like".', sel: 'related a' });
  save();
}

async function compare() {
  if (!(await newPage('compare', { wait: 9000 }))) return;
  await sheetsFor('compare');
  await chrome('compare');
  const g = G.compare;
  await S('cmp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Compare title', desc: 'The "ElevenReader vs. other text to speech apps" heading.', sel: 'h1 on /compare' });
  await S('cmp-table', q('table').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison table', desc: 'The apps comparison table (header row + feature rows).', sel: 'table' }, { pad: 4 });
  await S('cmp-th', q('table th').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table head cell', desc: 'A header cell in the comparison table.', sel: 'table th' });
  await S('cmp-td', q('table td').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table cell', desc: 'A body cell in the comparison table (a check/cross or text).', sel: 'table td' });
  await S('cmp-link', q('main a').filter({ hasText: /vs\.|alternative|comparison/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Comparison link', desc: 'A link to an in-depth comparison page.', sel: 'compare a' });
  save();
}

// Presses a "…with email" toggle that only expands the sr-only credential
// form (aria-expanded, no request is sent); NEVER refuses a bare "Sign in"
// but this button's text is "Sign in with email" — still, we click the
// toggle element directly rather than through toggle() so the intent is
// explicit and logged.
async function revealEmailForm(sel) {
  const t = q(sel).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  const info = await t.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || '').trim() }));
  if (info.type === 'submit') return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  log('   revealed email form via "' + info.text + '" (aria-expanded toggle, nothing sent)');
  return true;
}

async function signin() {
  if (!(await newPage('signin', { wait: 9000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.auth;
  // The card is a max-w-90 column on the bare page (transparent on white):
  // measured as its container, not a painted surface.
  await S('signin-card', q('div[class*="max-w-90"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The centred sign-in card column (max-w-90: logo, OAuth buttons, the revealed email form, the Create-account footer); never filled or submitted.', sel: 'div.max-w-90' });
  await S('sso-google', q('button').filter({ hasText: /Sign in with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google button', desc: 'The Sign-in-with-Google pill (bg-dark, hover bg-overlay-darker); measured never pressed.', sel: 'button "Sign in with Google"' });
  await S('sso-apple', q('button').filter({ hasText: /Sign in with Apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple button', desc: 'The Sign-in-with-Apple pill (bg-inverse, hover opacity-80); measured never pressed.', sel: 'button "Sign in with Apple"' });
  await S('signin-secondary', q('button').filter({ hasText: /Sign in with email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Email-signin button', desc: 'The outlined Sign-in-with-email pill under the OAuth buttons; it toggles the credential form (pressed after its own readings).', sel: 'button "Sign in with email"' });
  await S('create-link', q('a').filter({ hasText: /Create account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create-account link', desc: 'The card footer\'s Create-account link; measured never followed.', sel: 'a "Create account"' });
  // The email form is sr-only until "Sign in with email" expands it — a local
  // UI toggle that sends nothing. Fields are only measured once painted.
  await revealEmailForm('button:has-text("Sign in with email")');
  await S('email-field', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input (rounded-full, border-gray-alpha-200, focus-ring) after the email toggle was pressed; sample text was typed and deleted, nothing sent.', sel: 'input#email' });
  await S('password-field', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input after the email toggle; focused only, never filled or submitted.', sel: 'input#password' });
  await S('forgot-btn', q('button').filter({ hasText: /Forgot password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password button', desc: 'The Forgot-password link-button beside the Password label (opens a dialog; measured, never pressed).', sel: 'button "Forgot password"' });
  await S('signin-submit', q('form button[type="submit"], button[type="submit"]').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in submit', desc: 'The form\'s Sign-in submit (bg-inverse pill) after the email toggle; measured, never pressed (a press would submit).', sel: 'button[type=submit]' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  const g = G.auth;
  await S('signup-card', q('div[class*="max-w-90"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up card', desc: 'The centred create-account card column (max-w-90: logo, heading, OAuth buttons, legal copy); never filled or submitted.', sel: 'div.max-w-90' });
  await S('signup-google', q('button').filter({ hasText: /Sign up with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-up button', desc: 'The Sign-up-with-Google pill; measured never pressed.', sel: 'button "Sign up with Google"' });
  await S('signup-legal', q('p').filter({ hasText: /Terms of Service|Privacy Policy/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal copy', desc: 'The small legal consent paragraph on the sign-up card.', sel: 'signup legal p' });
  await S('signup-email-btn', q('button[data-signup-email-toggle]').filter({ visible: true }).first(), B4, { group: g, title: 'Email-signup button', desc: 'The outlined Sign-up-with-email pill; it toggles the credential form (pressed after its own readings).', sel: 'button[data-signup-email-toggle]' });
  await revealEmailForm('button[data-signup-email-toggle], button:has-text("Sign up with email")');
  await S('signup-field', q('input[type="email"], input[autocomplete="email"], input[name="email"], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Signup email field', desc: 'The signup email input after the email toggle; focused only, never filled or submitted.', sel: 'signup input[type=email]' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: the big Footer heading, the <details> link columns, legal and app badges.', sel: 'footer' }, { noScroll: true });
  // The desktop footer lays the same columns out flat: a muted <p> heading
  // over a <ul> (the <details> accordions are lg:hidden and live on mobile).
  await S('footer-col', q('footer p').filter({ hasText: /^\s*(Use Cases|Browse|Compare)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer column heading', desc: 'A muted column heading (text-lighter 13px) over a footer link list.', sel: 'footer column p' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Iconic Voices|Read Aloud PDF|Sign Up/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link (effect-focus-underline).', sel: 'footer a' }, { noScroll: true });
  await S('cookie-btn', q('footer button').filter({ hasText: /Cookie Settings/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie-settings button', desc: 'The Cookie Settings text-button in the legal column; measured, never pressed (a press opens the consent preferences).', sel: 'footer button "Cookie Settings"' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-promo', q('div[class*="bg-[#F5F3F1]"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile promo banner', sel: 'banner at 390' }, { noScroll: true });
  await S('m-header', q('button[aria-label="Open menu"]').locator('xpath=ancestor::div[.//a[@href="/"]][1]'), ['default'], { group: g, title: 'Mobile header', desc: 'The 390px top bar: wordmark and the Open-menu button.', sel: 'header bar at 390' }, { noScroll: true });
  const menu = q('button[aria-label="Open menu"]').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The hamburger button in the mobile header.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[role="dialog"], [class*="fixed"][class*="inset-0"]').filter({ hasText: /Explore|Pricing/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen menu the hamburger opens (nav items plus Sign-in/Start-listening pills).', sel: 'mobile menu panel' }, { noScroll: true });
  await S('m-nav-item', q('[role="dialog"] a, [role="dialog"] button, body a, body button').filter({ hasText: /^\s*(Pricing|For Authors|Upload & Listen|Discover)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened mobile menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  // The mobile footer turns the link columns into <details> accordions.
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  const mOpen = async (loc) => {
    const sm = loc.locator('summary').first();
    await sm.click({ timeout: 4000 }).catch(() => sm.evaluate((el) => el.click()));
    await page.waitForTimeout(900);
    return 'opened by its own summary';
  };
  await S('m-footer-col', q('footer details').filter({ hasText: /Use Cases|Browse|Compare/ }).filter({ visible: true }).first(), ['default', 'open'], { group: g, title: 'Mobile footer column', desc: 'A footer <details> link column (lg:hidden — the mobile-only accordion); the open state is the column after its own summary was tapped.', sel: 'footer details at 390' }, { noScroll: true, before: { open: mOpen }, after: { open: closeDetails } });
  await S('m-footer-summary', q('footer summary').filter({ hasText: /Use Cases|Browse|Compare/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile footer summary', desc: 'The tappable footer column row (f-ui-04 with the chevron pair).', sel: 'footer summary at 390' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints light — the stylesheet\'s .dark scope never applies on the public pages';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, explore, pricing, audiobook, compare, signin, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the orbit carousel's
  // motion-reduce:duration-0 transform), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '[aria-label="Book carousel"] > div');
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
