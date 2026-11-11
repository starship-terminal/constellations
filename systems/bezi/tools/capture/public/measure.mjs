// Measures bezi.com's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing mobile (the footer group also runs on home).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// bezi.com is a Framer site in one dark theme; components are found by
// role, landmark, cursor:pointer structure or stable text — the framer-*
// classes are build hashes, never selected. Nothing is sent, downloaded or
// signed into: the only press is a local UI toggle, the mobile menu trigger.
// "TRY FOR FREE", the plan CTAs, the Individual/Studio billing toggle and
// every outbound link (Docs, Discord, the footer socials) are measured in
// all states except followed or pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', about: '/about' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
// Pages that actually loaded this run (not blocked): readings may only be
// pruned for components on one of these — a blocked route must not erase
// evidence captured earlier.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
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
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
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
        if (opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (nav menu, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Marks the shallowest ancestor of a text leaf whose subtree paints a fill of
// colour `want` (Framer draws a button's fill on a sibling layer, so the
// anchor alone reads transparent). `minY` skips same-text copies in the
// header. Falls back to the leaf. Returns whether anything was marked.
const markFillParent = async (textRe, want, attr, { minY = 0 } = {}) => page.evaluate(([src, flags, a, w, miny]) => {
  const re = new RegExp(src, flags);
  const texts = [...document.querySelectorAll('a,button,div,p,span')].filter((n) => {
    const t = (n.innerText || '').trim();
    const r = n.getBoundingClientRect();
    return re.test(t) && t.length < 60 && r.width > 0 && r.y >= miny;
  });
  const leaf = texts.find((n) => !texts.some((o) => o !== n && n.contains(o))) || texts[0];
  if (!leaf) return false;
  const paints = (n) => getComputedStyle(n).backgroundColor === w;
  for (let n = leaf, i = 0; n && i < 8; i++, n = n.parentElement) {
    if (n.getBoundingClientRect().width > 700) break;
    if (paints(n) || [...n.children].some((k) => paints(k) && k.getBoundingClientRect().width >= 80)) {
      n.setAttribute(a, '1');
      return true;
    }
  }
  leaf.setAttribute(a, '1');
  return true;
}, [textRe.source, textRe.flags, attr, want, minY]);

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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Scrolls down in steps until fn() (run in-page) reports it found and marked
// its element, or the document ends. Framer mounts a section only while its
// band is near the viewport and unmounts it again when it leaves, so the mark
// has to happen where the element lives, not after a full sweep.
async function scrollFind(fn) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y <= h; y += 550) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.waitForTimeout(320);
    if (await page.evaluate(fn)) return true;
  }
  return false;
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The floating dark pill bar: the Bezi mark, the nav links (Studios, Product, Pricing, Blog, Docs, Discord) and nothing else on it.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a').first(), ['default'], { group: g, title: 'Logo', sel: 'header a:first' }, { noScroll: true });
  const navA = (t) => q('header a, nav a').filter({ hasText: t }).first();
  await S('nav-link', navA(/^Pricing$/), B4, { group: g, title: 'Nav link', sel: 'a:has-text("Pricing")' }, { noScroll: true });
  await S('nav-discord', navA(/^Discord$/), B4, { group: g, title: 'Discord link', sel: 'a:has-text("Discord")' }, { noScroll: true });
  await S('hero-title', q('h1').first(), ['default'], { group: g, title: 'Hero title', desc: '"AI for building real games" in the display face.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=following::*[self::p or self::div][string-length(normalize-space())>40][1]'), ['default'], { group: g, title: 'Hero subcopy', sel: 'first long paragraph under h1' }, { noScroll: true });
  // The anchor's own box is the text; the orange pill is a sibling layer, so
  // mark the ancestor holding both text and the #f84503 fill.
  const ctaOk = await markFillParent(/^try for free/i, 'rgb(248, 69, 3)', 'data-m-cta');
  await S('cta', ctaOk ? q('[data-m-cta="1"]') : q('[data-m-cta="__none__"]'), B4, { group: g, title: 'TRY FOR FREE button', desc: 'The orange CTA repeated across the page. Measured, never followed.', sel: 'ancestor of the TRY FOR FREE text that holds the orange fill' }, { noScroll: true });
  // The page ground: the starfield sits on the body's own fill.
  await S('page-ground', q('body'), ['default'], { group: g, title: 'Page ground', desc: 'The near-black the whole page paints on.', sel: 'body' }, { noScroll: true, crop: false });
  // The announcement line: hasText on a bare tag filter climbs to the page
  // wrapper, so mark the deepest element carrying the text, then retarget the
  // anchor that paints the strip.
  const annLoc = await domFind(page, /publicly available/i, { sel: 'div, a, p', tag: 'ann', up: 'a' });
  await S('announcement', annLoc, ['default'], { group: g, title: 'Announcement line', desc: 'The "NEW · Bezi for Unreal Engine is now publicly available" strip under the header.', sel: 'anchor of the leaf text "publicly available"' }, { noScroll: true });
  // The first h2 is an empty Framer placeholder; the visible section titles
  // mount only while their band is on screen, so mark one where it lives.
  const h2ok = await scrollFind(() => {
    const h = [...document.querySelectorAll('h2')].find((n) => (n.innerText || '').trim().length > 3 && n.getBoundingClientRect().height > 0);
    if (!h) return false;
    h.setAttribute('data-m-h2', '1');
    return true;
  });
  await S('section-title', h2ok ? q('[data-m-h2="1"]') : q('[data-m-h2="__none__"]'), ['default'], { group: g, title: 'Section title', sel: 'first visible h2, marked where it mounts' });
  const toolsBtn = q('button').filter({ hasText: /connected tools/i }).filter({ visible: true }).first();
  await S('tools-button', toolsBtn, B4, { group: g, title: 'Connected tools chip', desc: 'The "02. CONNECTED TOOLS" index button on the home page.', sel: 'button:has-text("CONNECTED TOOLS")' });
  await S('view-all', q('a').filter({ hasText: /view all/i }).first(), B4, { group: g, title: 'View all link', desc: 'The blog index link.', sel: 'a:has-text("View all")' });
  save();
}


async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1, h2').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1/h2' }, { noScroll: true });
  // The Free band's TRY FOR FREE paints dark on the light-blue card; minY
  // skips the same-text pill in the header.
  const pcOk = await markFillParent(/^try for free/i, 'rgba(0, 0, 0, 0.84)', 'data-m-plan-cta', { minY: 200 });
  await S('plan-cta', pcOk ? q('[data-m-plan-cta="1"]') : q('[data-m-plan-cta="__none__"]'), B4, { group: g, title: 'Plan CTA', desc: 'The action inside the Free trial band. Measured, never followed.', sel: 'ancestor of the plan TRY FOR FREE text that holds the dark fill' });
  await page.evaluate(() => {
    // The RECOMMENDED tag sits on the Advanced column: climb from it to the
    // first ancestor that paints a card (fill, border or shadow) at column
    // size. The Free band is a full-width strip, not a column, so the climb
    // bounds width at 200-700px.
    const tag = [...document.querySelectorAll('div, p, span')].find((n) => /^recommended$/i.test((n.innerText || '').trim()));
    if (!tag) return;
    let card = null;
    for (let n = tag, i = 0; n && i < 10; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 700 || r.height > 1000) break;
      if (r.width >= 200 && r.height >= 200) {
        const c = getComputedStyle(n);
        if (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.boxShadow !== 'none' || parseFloat(c.borderTopWidth) > 0) card = n;
      }
    }
    (card || tag.parentElement || tag).setAttribute('data-m-plan-card', '1');
  });
  await S('plan-card', q('[data-m-plan-card="1"]'), ['default'], { group: g, title: 'Plan card', sel: 'card ancestor of a plan CTA (marked in-page)' });
  save();
}


async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep another page's
  // readings under the wrong url.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[href*="linkedin" i], footer a[href*="twitter" i], footer a[href*="x.com" i], footer a[href*="youtube" i]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
    await S('footer-rating', q('footer a[href*="g2.com" i]').first(), B4, { group: g, title: 'G2 rating badge', desc: 'The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed.', sel: 'footer a[href*="g2.com"]' });
    await S('footer-legal', q('footer a').filter({ hasText: /privacy|terms|dpa|security/i }).first(), B4, { group: g, title: 'Legal link', sel: 'footer a:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const marked = await page.evaluate(() => {
    const h = document.querySelector('header');
    if (!h) return false;
    // The hamburger is a tiny icon control at the bar's right edge — on this
    // build a 14x14 nested `header` element with cursor:pointer, no text.
    const cand = [...h.querySelectorAll('*')].filter((n) => {
      const r = n.getBoundingClientRect(); const c = getComputedStyle(n);
      const iconish = n.tagName === 'BUTTON' || c.cursor === 'pointer' || (n.querySelector('svg,img') && !(n.innerText || '').trim());
      return r.width >= 12 && r.width <= 72 && r.height >= 12 && r.height <= 72 && r.x > 260 && iconish;
    });
    const el = cand[cand.length - 1];
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  const menuBtn = q('[data-m-menu="1"]');
  if (marked) {
    await S('m-menu-button', menuBtn, ['default', 'pressed'], { group: g, title: 'Mobile menu button', desc: 'The 36px trigger at the right of the mobile bar; its own press opens the menu overlay.', sel: 'header div[cursor=pointer] at right' }, { noScroll: true });
    await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The trigger after its own toggle; the open overlay shows in the crop.', sel: 'mobile menu trigger' }, { noScroll: true, cropLoc: q('body') });
    await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  }
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), dark theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components on a page that actually opened this run: a blocked
    // or unvisited route keeps its earlier readings (write new captures first,
    // prune old outputs only after a complete run).
    if (!touched.has(key) && !pages.length) { if (opened.has(c.page)) delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
