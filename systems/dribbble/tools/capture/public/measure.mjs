// Measures dribbble.com's public components in every state reachable without
// signing in, following, liking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shots shot designer designers jobs search stories login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dribbble.com is a Rails app in three CSS eras: the legacy mini-master bundle
// (hardcoded values, Mona Sans), Vite/Shoelace components (--sl-* tokens, the
// --sl-color-primary-* ramp re-bound to the Dribbble pink), and Algolia/
// intl-tel-input vendor styles. The signed-out shot feed is a teaser (one card
// then a "Sign up to continue" wall); designer profiles, the designers
// directory, jobs, search, stories and the auth cards paint fully. Nothing is
// sent, filled, followed, liked or signed into: the only presses are local UI
// toggles — the Explore dropdown, the mobile menu. The WELCOME20 banner stays
// (it is page content, measured as a component); the floating project-brief
// card, the Google One Tap prompt and any consent overlay are hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', shots: '/shots/popular', shot: '/shots/27884620-Hotel-Tango-Distillery-Illustrations',
  designer: '/Moonsight', designers: '/designers', jobs: '/jobs', search: '/search?q=logo',
  stories: '/stories', login: '/session/new', signup: '/signup',
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

// Clicks a UI toggle (dropdown, menu, tab). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|next|confirm|follow|like|hire me|get in touch|post|upload)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
// markLargest/domFind return a never-matching locator on a miss, never throw, so a
// `.catch(() => fallback)` never fell back: choose by count() instead.
const orElse = async (loc, fallback) => ((loc && (await loc.count())) ? loc : fallback);

// Transitions and animations declared in every readable sheet, by selector.
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
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
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

// Marks the largest visible element matching sel — for media frames whose
// wrapper classes vary (the shot image on a shot page).
async function markLargest(sel, tag, { minW = 80, minH = 60 } = {}) {
  const ok = await page.evaluate(([s, t, w, h]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const els = [...document.querySelectorAll(s)].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width >= w && r.height >= h;
    });
    const m = els.sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height
      - a.getBoundingClientRect().width * a.getBoundingClientRect().height)[0];
    if (!m) return false;
    m.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, minW, minH]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image, or falls back to marking a painted descendant.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, maxW = Infinity, maxH = Infinity, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, W, H, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && r.width <= W && r.height <= H && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && r.width <= W && r.height <= H && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, maxW, maxH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', home: 'Home', feed: 'Shot feed', shot: 'Shot detail',
  profile: 'Designer profile', directory: 'Designers directory', jobs: 'Jobs board',
  search: 'Search', auth: 'Log in and sign up', stories: 'Stories (blog)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { promo: 'close' }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.site-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The site nav bar (div.site-nav): the script Dribbble wordmark, the Explore/Hire-Talent/Get-Hired/Community dropdown triggers, the pink Start-Project-Brief link, Sign up and the dark Log-in pill.', sel: '.site-nav' }, { noScroll: true });
  await S('logo', q('a.site-nav__logo, .site-nav a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The script Dribbble wordmark anchor.', sel: 'a.site-nav__logo' }, { noScroll: true });
  await S('nav-trigger', q('.site-nav a, .site-nav button').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Explore link that opens the header dropdown on hover; hovered, never followed.', sel: 'a.site-nav-main__link "Explore"' }, { noScroll: true });
  await S('nav-link', q('.site-nav a, .site-nav button').filter({ hasText: /^\s*Community\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'The Community dropdown trigger.', sel: 'a.site-nav-main__link "Community"' }, { noScroll: true });
  // nav-link-pink (Start Project Brief, site-nav-main__link--pink) exists in
  // the DOM but paints 0x0 at 1440 wide on the home page — a documented gap,
  // not a measurement.
  await S('signup-link', q('.site-nav a[href="/signups/new"], .site-nav a[href="/signup"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The plain Sign-up header action; measured never followed.', sel: '.site-nav__signup' }, { noScroll: true });
  await S('login-btn', q('.site-nav a[href="/session/new"], a.btn2[href="/session/new"]').filter({ visible: true }).first(), B4, { group: g, title: 'Log-in button', desc: 'The dark Log-in pill (btn2--medium); measured never followed.', sel: '.site-nav__login.btn2' }, { noScroll: true });
  // The Explore trigger opens its dropdown on hover; keep the pointer put
  // while the panel is read (noReset), then Escape to close.
  const explore = q('.site-nav a, .site-nav button').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).first();
  try {
    if (await explore.count()) { await explore.hover({ timeout: 5000 }); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! dropdown hover failed', String(e.message).split('\n')[0]); }
  const panel = q('ul.site-nav-sub, .site-nav-sub').filter({ visible: true }).first();
  await S('nav-dropdown', panel, ['default'], { group: g, title: 'Nav dropdown', desc: 'The Explore dropdown panel (ul.site-nav-sub: Popular, New and Noteworthy, category links), opened by hovering its own trigger.', sel: 'ul.site-nav-sub' }, { noScroll: true, noReset: true });
  const openExplore = async () => { const t = q('.site-nav a, .site-nav button').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).first(); if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(800); } };
  // The panel is hover-driven: the trigger is re-hovered before every state so
  // the link is visible when the action runs.
  await S('menu-link', q('ul.site-nav-sub a, .site-nav-sub a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened Explore dropdown (each state re-hovers the Explore trigger first).', sel: '.site-nav-sub a' }, { noScroll: true, noReset: true,
    open: openExplore,
    before: { hover: openExplore, 'focus-visible': openExplore, pressed: openExplore } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.home;
  await S('promo-banner', q('div, aside').filter({ hasText: /WELCOME20|% off/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Promo banner', desc: 'The WELCOME20 offer strip under the header — page content, measured where it sits; its Get-Started action was never pressed.', sel: 'promo banner' }, { noScroll: true });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Work with the world\'s best" display headline; one word rotates and paints the Dribbble pink.', sel: 'h1' });
  await S('hero-accent', q('h1 span, h1 em, h1 a, h1 strong').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero accent word', desc: 'The rotating accent word inside the headline.', sel: 'h1 accent span' });
  // Scoped to the hero checklist (ul.home-header__list): a page-wide li match
  // lands on the Hire Talent nav item instead.
  await S('hero-check', q('ul[class*="home-header" i] li, [class*="home-header" i] li, main li').filter({ hasText: /generate your brief|browse real design|hire top-rated|proposals/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero checklist item', desc: 'A pink-check bullet under the hero (li.home-header__list-item).', sel: '.home-header__list li' });
  await S('hero-cta', q('a, button').filter({ hasText: /Start Your Project Brief/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Start Your Project Brief" dark pill; measured never followed.', sel: '"Start Your Project Brief"' });
  await S('hero-media', q('.home-header-media, .home-header-right__media-container, [class*="home-header-media" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero media card', desc: 'The shot media panel beside the hero copy (figure.home-header-media, the animated designer-work card).', sel: '.home-header-media' });
  await S('view-tab', q('label, [role="tab"], drb-toggle-tab').filter({ hasText: /^\s*(Shots|Designers|Services)\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'View tab', desc: 'A Shots/Designers/Services tab (a segmented-control label) over the search strip.', sel: 'segmented control label' });
  await S('home-search', q('input[type="search"], input[placeholder*="interested" i], input[placeholder*="looking" i], form input').filter({ visible: true }).first(), ['default', 'focused'], { group: h, title: 'Search field', desc: 'The "What type of design are you interested in?" pill field; focused only, never submitted.', sel: 'home search input' });
  await S('search-go', q('button[type="submit"], button[class*="search" i], [class*="search__btn" i]').filter({ visible: true }).first(), B4, { group: h, title: 'Search button', desc: 'The pink circle search button (btn2--circle); measured never pressed.', sel: 'search submit button' });
  await S('tag-chip', q('a').filter({ hasText: /^\s*(dashboard|landing page|mobile app|portfolio|ecommerce|animation|illustration|onboarding)\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Tag chip', desc: 'A Popular-search tag link under the field.', sel: 'popular tag a' });
  await S('sort-select', q('button, a, [role="combobox"], select').filter({ hasText: /^\s*Popular\s*$/ }).filter({ visible: true }).last(), B4, { group: h, title: 'Sort control', desc: 'The "Popular" sort dropdown; its list was never opened.', sel: '"Popular" control' });
  save();
}

async function feed() {
  if (!(await newPage('shots', { wait: 10000 }))) return;
  await sheetsFor('shots');
  await chrome('shots');
  const g = G.feed;
  await S('search-input', q('.site-nav input, input[type="search"], input[name="q"], input[placeholder*="looking" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: G.shell, title: 'Header search field', desc: 'The "What are you looking for?" header field on inner pages; focused only, never submitted.', sel: '.site-nav search input' }, { noScroll: true });
  await S('scope-select', q('.site-nav-search__dropdown-trigger, .site-nav button, .site-nav select, .site-nav [role="combobox"]').filter({ hasText: /^\s*(Shots|Designers|Services)\s*$/ }).filter({ visible: true }).first(), B4, { group: G.shell, title: 'Scope dropdown', desc: 'The Shots scope selector beside the header search field (site-nav-search__dropdown-trigger); its list was never opened.', sel: '.site-nav-search__dropdown-trigger' }, { noScroll: true });
  await S('shot-card', q('[class*="shot-thumbnail" i], [class*="shot-card" i], li[class*="shot" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Shot card', desc: 'The one card the signed-out feed paints before the wall: image, designer avatar + name, PRO/PRO+ badge, like and view counts.', sel: 'shot card' });
  await S('shot-title', q('a[href*="/shots/2"], [class*="shot-title" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Shot card link', desc: 'The card\'s shot link (the image anchor carrying the title).', sel: 'shot card link' });
  await S('pro-badge', q('[class*="badge" i], span').filter({ hasText: /^\s*PRO\+?\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'PRO badge', desc: 'The small PRO/PRO+ membership chip on the card.', sel: 'PRO badge' });
  await S('stat-count', q('[class*="count" i], span, li').filter({ hasText: /^\s*[\d.]+\s*[kKmM]?\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Like/view count', desc: 'A heart/eye count on the shot card.', sel: 'shot stat count' });
  await S('wall-cta', q('a, button').filter({ hasText: /Sign up to continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up wall', desc: 'The "Sign up to continue" pill that ends the signed-out feed; measured never followed — the signed-in feed is the boundary.', sel: '"Sign up to continue"' });
  await S('category-tile', q('a[href*="/shots/popular/"], a[href*="/designers"], [class*="categor" i] a').filter({ hasText: /Branding|Illustration|Web Design|Mobile|Typography|Print|Product Design|Animation/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category tile', desc: 'A browse-category tile (Branding, Illustration…) under the wall.', sel: 'category tile' });
  save();
}

async function shot() {
  if (!(await newPage('shot', { wait: 10000 }))) return;
  await sheetsFor('shot');
  await chrome('shot');
  const g = G.shot;
  await S('shot-detail-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shot title', desc: 'The shot page headline.', sel: 'h1 on the shot page' }, { noScroll: true });
  await S('shot-author', q('a[href^="/"][class*="avatar" i], [class*="shot-user" i] a, [class*="author" i] a').filter({ visible: true }).first(), B4, { group: g, title: 'Shot author', desc: 'The designer attribution row (avatar, name, Follow).', sel: 'shot author block' });
  await S('shot-follow', q('a, button').filter({ hasText: /^\s*Follow\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Follow button', desc: 'The Follow action under the author; measured never pressed.', sel: '"Follow"' });
  await S('shot-cta', q('a, button').filter({ hasText: /Get in touch/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-in-touch button', desc: 'The dark hire pill on the shot page; measured never followed.', sel: '"Get in touch"' });
  await S('shot-icon-btn', q('button[aria-label*="like" i], button[aria-label*="save" i], button[class*="like" i], button[class*="save" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Like/save icon button', desc: 'A heart/bookmark round button beside the CTA; measured never pressed.', sel: 'like or save icon button' });
  await S('shot-media', await orElse(await markLargest('main img, article img, figure img, [class*="media" i] img, [class*="shot" i] img', 'm-shot-media', { minW: 300, minH: 200 }).catch(() => null), q('main img').first()), ['default'], { group: g, title: 'Shot media', desc: 'The big shot image frame (largest image in main).', sel: 'largest main img' });
  await S('rail-btn', q('[class*="rail" i] button, aside button, [class*="sidebar" i] button').filter({ visible: true }).first(), B4, { group: g, title: 'Action rail button', desc: 'A button on the right-hand action rail (like/share/info).', sel: 'right rail button' });
  save();
}

async function profile() {
  if (!(await newPage('designer', { wait: 10000 }))) return;
  await sheetsFor('designer');
  await chrome('designer');
  const g = G.profile;
  await S('profile-avatar', q('[class*="avatar" i] img, [class*="profile" i] img, img[alt*="avatar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile avatar', desc: 'The designer\'s round avatar.', sel: 'profile avatar' }, { noScroll: true });
  await S('profile-name', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile name', desc: 'The designer/agency display name heading.', sel: 'profile h1' });
  await S('profile-headline', q('.masthead-intro h2, .masthead-content h2, main h2, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile headline', desc: 'The designer\'s tagline block (masthead-intro h2) under the name.', sel: '.masthead-intro h2' });
  await S('profile-stat', q('.masthead-stats .stat, .masthead-stats > *').filter({ hasText: /followers|following|likes/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile stat', desc: 'A followers/following/likes stat (.masthead-stats .stat) under the headline.', sel: '.masthead-stats .stat' });
  await S('profile-cta', q('a, button').filter({ hasText: /Get in touch/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-in-touch button', desc: 'The dark hire pill on the profile; measured never followed.', sel: '"Get in touch"' });
  await S('profile-follow', q('a, button').filter({ hasText: /^\s*Follow\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Follow button', desc: 'The white Follow pill; measured never pressed.', sel: '"Follow"' });
  await S('profile-icon-btn', q('button[aria-label*="save" i], button[aria-label*="bookmark" i], a[aria-label*="save" i], button[class*="bookmark" i], a[class*="bookmark" i], [class*="profile" i] button, [class*="profile" i] a[class*="icon" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Icon button', desc: 'The icon-only action beside Follow (save/message); measured never pressed.', sel: 'profile icon button' });
  await S('profile-tab', q('a, button, [role="tab"]').filter({ hasText: /^\s*(Work|Services|Reviews|Collections|Liked Shots|Members|About)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Profile tab', desc: 'A tab in the Work/Services/Reviews/Collections bar.', sel: 'profile tab' });
  await S('profile-sort', q('button, a, [role="combobox"], select').filter({ hasText: /Recent Shots|Most Recent/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Work sort control', desc: 'The "Recent Shots" dropdown over the work grid; its list was never opened.', sel: '"Recent Shots" control' });
  await S('profile-shot-card', q('[class*="shot-thumbnail" i], .dribbble-shot, [class*="shot-card" i], ol li[class*="shot" i], ol li a[href*="/shots/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Work grid card', desc: 'A shot card in the designer\'s work grid.', sel: 'work grid card' });
  save();
}

async function directory() {
  if (!(await newPage('designers', { wait: 10000 }))) return;
  await sheetsFor('designers');
  await chrome('designers');
  const g = G.directory;
  await S('dir-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Directory title', desc: 'The "Hire Top Freelance Designers" heading.', sel: 'h1 on /designers' }, { noScroll: true });
  await S('topic-chip', q('a').filter({ hasText: /^\s*(logo design|landing page|mobile app|web design|ux design|framer|branding|social media|animation|typography)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Topic chip', desc: 'A Popular topic link under the directory heading.', sel: 'popular topic a' });
  await S('filter-select', q('button, a, [role="combobox"], select, details').filter({ hasText: /^\s*(Categories|Budget|Location|Rating|More)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter control', desc: 'A filter dropdown over the directory (Categories/Budget/Location/Rating/More); its list was never opened.', sel: 'filter dropdown' });
  await S('designer-card', q('.resume-user-card, [class*="designer" i][class*="card" i], [class*="service-card" i], li article, article').filter({ visible: true }).first(), B4, { group: g, title: 'Designer card', desc: 'A freelancer card (resume-user-card): avatar, name, PRO+/SELECT badges, star rating, projects count, rate, location, response time, work strip and skill chips.', sel: '.resume-user-card' });
  await S('designer-name', q('h2, h3, a').filter({ hasText: /\b(LAB|STUDIO)\b|®|™/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Designer name', desc: 'The freelancer\'s display name on the card.', sel: 'designer card name' });
  await S('badge-select', q('[class*="badge" i], span').filter({ hasText: /^\s*(SELECT|PRO\+?)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SELECT badge', desc: 'The SELECT/PRO+ membership chip on the card.', sel: 'SELECT badge' });
  await S('rating', await orElse(await domFind(page, /\d\.\d\s*\(\d+\)/, { sel: 'span, div, a, li', tag: 'm-rating', leaf: true }).catch(() => null), q('span, div').filter({ hasText: /\d\.\d\s*\(\d+\)/ }).filter({ visible: true }).first()), ['default'], { group: g, title: 'Star rating', desc: 'The 4.9 (158) star-rating figure.', sel: 'star rating' });
  await S('designer-meta', await orElse(await domFind(page, /projects completed|Responds in|Services available|From \$[\d,]+/i, { sel: 'span, li, div', tag: 'm-meta', leaf: true }).catch(() => null), q('span, li, div').filter({ hasText: /projects completed|Responds in|Services available/i }).filter({ visible: true }).first()), ['default'], { group: g, title: 'Designer meta', desc: 'A projects-completed / response-time / services meta item.', sel: 'designer meta' });
  await S('promoted-tag', await orElse(await domFind(page, /^\s*Promoted\s*$/, { sel: 'span, div, a', tag: 'm-promo', leaf: true }).catch(() => null), q('span').filter({ hasText: /Promoted/ }).filter({ visible: true }).first()), ['default'], { group: g, title: 'Promoted tag', desc: 'The small "Promoted" disclosure label.', sel: '"Promoted"' });
  await S('designer-cta', q('a, button').filter({ hasText: /Get in touch/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-in-touch button', desc: 'The dark hire pill on the card; measured never followed.', sel: '"Get in touch"' });
  await S('bookmark-btn', q('.resume-user-card button, .resume-user-card a').filter({ hasNotText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Bookmark icon button', desc: 'The icon-only save/bookmark button on the card; measured never pressed.', sel: '.resume-user-card icon-only control' });
  await S('skill-chip-dark', q('a, span, li').filter({ hasText: /Expert|Partner/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Skill chip, dark', desc: 'The dark certified chip ("Webflow Expert").', sel: 'dark skill chip' });
  await S('skill-chip', q('a, span, li').filter({ hasText: /^\s*(wireframing|app design|product design|mobile app|responsive web|web design)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Skill chip', desc: 'A light skill tag on the card.', sel: 'skill chip' });
  save();
}

async function jobsPage() {
  if (!(await newPage('jobs', { wait: 10000 }))) return;
  await sheetsFor('jobs');
  await chrome('jobs');
  const g = G.jobs;
  await S('jobs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Jobs title', desc: 'The jobs-board heading.', sel: 'h1 on /jobs' }, { noScroll: true });
  await S('job-card', q('[class*="job" i][class*="card" i], article, li[class*="job" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Job card', desc: 'A posting card: logo, role, company, location/type tags.', sel: 'job card' });
  // Scoped inside the posting cards (li.job-list-item): page-wide h2/h3/a/
  // span/li matches land on the site-nav logo link and the Hire Talent nav
  // item, not on the job list. The role title is an h4.job-board-job-title.
  await S('job-title', q('li[class*="job" i] h4, li[class*="job" i] h3, li[class*="job" i] h2, [class*="job" i][class*="card" i] h4, [class*="job" i][class*="card" i] h2, [class*="job" i][class*="card" i] h3, article h4, article h2, article h3').filter({ hasText: /designer|design/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Job title', desc: 'A role title on a posting (h4.job-board-job-title inside li.job-list-item).', sel: 'job title inside a job card' });
  await S('job-tag', q('li[class*="job" i] [class*="location" i], li[class*="job" i] [class*="tag" i], [class*="job" i][class*="card" i] [class*="location" i], [class*="job" i][class*="card" i] span, article span, article li').filter({ hasText: /remote|full.?time|contract|freelance|hybrid|onsite|on-site/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Job tag', desc: 'A remote/contract/location tag on the posting (span.location inside li.job-list-item).', sel: 'job tag inside a job card' });
  await S('job-apply', q('a, button').filter({ hasText: /apply/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apply button', desc: 'The apply action; measured never followed.', sel: '"Apply"' });
  save();
}

async function searchPage() {
  if (!(await newPage('search', { wait: 10000 }))) return;
  await sheetsFor('search');
  await chrome('search');
  const g = G.search;
  await S('search-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search title', desc: 'The query heading ("Logo").', sel: 'h1 on /search' }, { noScroll: true });
  await S('search-desc', q('main p, h1 + p, p').filter({ hasText: /logo|graphic|symbol/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Search description', desc: 'The dictionary-style definition line under the query.', sel: 'search definition' });
  await S('related-link', q('a').filter({ hasText: /^\s*(branding|icon|logotype|vector|typography|identity)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Related link', desc: 'A Related: tag link under the definition.', sel: 'related link' });
  await S('filter-tab', q('a, button, [role="tab"]').filter({ hasText: /^\s*(Discover|Animation|Branding|Illustration|Mobile|Print|Product Design|Typography|Web)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter tab', desc: 'A category tab over the results grid.', sel: 'filter tab' });
  await S('filter-sort', q('button, a, [role="combobox"], select').filter({ hasText: /^\s*Popular\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sort control', desc: 'The "Popular" sort dropdown; its list was never opened.', sel: '"Popular" control' });
  await S('filters-btn', q('button, a').filter({ hasText: /^\s*Filters\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Filters button', desc: 'The Filters toggle at the end of the tab row; measured, its panel was never opened.', sel: '"Filters" button' });
  await S('grid-shot-card', q('[class*="shot-thumbnail" i], [class*="shot-card" i], li[class*="shot" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Grid shot card', desc: 'A shot card in the results grid: image, avatar + name, PRO+ chip, like and view counts.', sel: 'results shot card' });
  save();
}

async function storiesPage() {
  if (!(await newPage('stories', { wait: 10000 }))) return;
  await sheetsFor('stories');
  await chrome('stories');
  const g = G.stories;
  await S('stories-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Stories title', desc: 'The blog\'s heading or featured story title.', sel: 'h1/h2 on /stories' }, { noScroll: true });
  await S('story-card', q('article, [class*="story" i][class*="card" i], li a[href*="/stories/"], a[href*="/stories/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Story card', desc: 'An article card in the blog index.', sel: 'story card' });
  // Scoped to the categories rail (ul.blog-cat in the secondary column): a
  // page-wide span/a match lands on the site-nav logo link.
  await S('story-tag', q('ul.blog-cat a, .blog-cat a, .secondary ul a, [class*="categor" i] a').filter({ hasText: /interview|inspiration|process|community|playbook|behind the scenes/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Story tag', desc: 'A category link on the stories index (ul.blog-cat: Interviews, Inspiration, Process, Community).', sel: 'ul.blog-cat a' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  const g = G.auth;
  const card = q('.auth-screen, .auth-layout__content, section.container2').filter({ visible: true }).first();
  await S('login-card', card, ['default'], { group: g, title: 'Login card', desc: 'The "Welcome back" form card (auth-layout__content) on the split layout; never filled or submitted. The Continue-with-Google action is a Google-rendered GSI element — hidden as a third-party prompt like every other overlay, never answered, so it is documented as a gap rather than measured.', sel: '.auth-layout__content' });
  await S('email-field', q('input[type="email"], input[name*="email" i], input[type="text"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The "Enter email or username" input; sample text was typed and deleted, nothing sent.', sel: 'auth email input' });
  await S('continue-btn', q('button[type="submit"], button, a').filter({ hasText: /^\s*Continue\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The dark Continue submit; measured, never pressed (a press would submit).', sel: '"Continue"' });
  await S('auth-link', q('a').filter({ hasText: /Sign up|Terms|Privacy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Auth link', desc: 'A Terms / Privacy / Sign-up link under the card actions.', sel: 'auth link' });
  await S('auth-art', await orElse(await markLargest('img, [class*="art" i], [class*="image" i], aside', 'm-auth-art', { minW: 200, minH: 300 }).catch(() => null), q('main').first()), ['default'], { group: g, title: 'Auth illustration panel', desc: 'The painted half of the split layout (a shot fills it, credited bottom-right).', sel: 'auth side panel' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  const g = G.auth;
  const card = q('.auth-screen, .auth-layout__content, section.container2').filter({ visible: true }).first();
  await S('signup-card', card, ['default'], { group: g, title: 'Signup card', desc: 'The "Welcome to Dribbble" form card; never filled or submitted.', sel: '.auth-layout__content' });
  await S('signup-field', q('input[type="email"], input[name*="email" i], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Signup email field', desc: 'The "Enter email address" input; focused only, never filled or submitted.', sel: 'signup input' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer, .site-footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: script wordmark, link columns (For designers/Hire designers/Company), social icons and the legal row.', sel: 'footer / .site-footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .site-footer a').filter({ hasText: /For designers|Hire talent|Inspiration|Advertising|Blog|About|Support|Terms|Privacy|Jobs/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A text link in the footer bottom bar (For designers / Hire talent / …); the category cards above it are measured separately.', sel: 'footer bottom-bar a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="pinterest"], .site-footer a[href*="instagram"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', desc: 'A social-icon link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.site-nav, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: '.site-nav at 390' }, { noScroll: true });
  const menu = q('button[aria-label*="menu" i], .site-nav button').filter({ visible: true }).last();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header menu toggle.', sel: 'header menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[class*="fixed"][class*="inset-0"], [role="dialog"], header + div, nav').filter({ hasText: /Explore|Shots|Sign up/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  await S('m-search', q('input[type="search"], input[placeholder*="interested" i], input[placeholder*="looking" i], form input').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile search field', sel: 'search input/link at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
const pages = process.argv.slice(2);
const plan = { home, feed, shot, profile, directory, jobsPage, searchPage, storiesPage, login, signup, mobile };
// The documented page names are the URLS keys (jobs, shots, designer, ...);
// the plan functions name their passes instead (jobsPage, feed, profile).
// Translate before filtering or a targeted refresh silently selects nothing.
const PLAN_FOR = Object.fromEntries(Object.keys(plan).map((k) => [k, k]));
for (const [pub, pk] of Object.entries({ shots: 'feed', designer: 'profile', designers: 'directory', jobs: 'jobsPage', search: 'searchPage', stories: 'storiesPage' })) PLAN_FOR[pub] = pk;
const unknown = pages.filter((p) => !PLAN_FOR[p]);
if (unknown.length) { console.error('unknown page(s):', unknown.join(', '), '— known:', Object.keys(PLAN_FOR).join(' ')); process.exit(2); }
const wanted = new Set(pages.map((p) => PLAN_FOR[p]));
const order = Object.keys(plan).filter((k) => !wanted.size || wanted.has(k));
// A full run re-stamps the capture date; a targeted run leaves it — most
// components still carry their earlier readings under the original date.
if (!pages.length) out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints light — the only declared dark scope is the Algolia search dropdown\'s vendor vars';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
let runDone = false;
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!wanted.size || wanted.has('home')) await footer();
  if (!wanted.size || wanted.has('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the header), so the
  // delta is meaningful.
  if (!wanted.size || wanted.has('home')) await reducedMotion('home', '.site-nav'); // the bar is div.site-nav; there is no <header>
  runDone = true;
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only on a full run that reached every
    // planned pass: a crashed run never visits the later pages, so their
    // entries keep earlier readings under their original provenance, the
    // same as an edge-blocked route's.
    if (!touched.has(key) && !pages.length && runDone && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
