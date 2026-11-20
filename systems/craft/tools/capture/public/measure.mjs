// Measures craft.do's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing download pages mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// craft.do is a Next.js app on Tailwind v4 utilities with a :root --color-*
// layer; the public surface paints light only. Specs select by role,
// aria-label, text or structure (utility classes are too dense to name).
// There is no auth card on www.craft.do (Log in links out to docs.craft.do,
// never followed); Try Craft Free leads to /download, never used. The only
// presses are local UI toggles: the billing switch and the mobile nav button.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', pricing: '/pricing', download: '/download', imagine: '/imagine', learn: '/learn', write: '/write' };
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
  await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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

// Marks the opened mobile nav overlay: the smallest visible ancestor that
// holds the nav rows and the Try Craft Free / Log in actions.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div, nav, section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.height > innerHeight * 0.4 && r.width > innerWidth * 0.6
        && /Product/i.test(t) && /Pricing/i.test(t) && t.length < 3000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks the PLUS plan card on /pricing: the smallest visible card-height div
// whose text starts with PLUS.
async function markPlanCard() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('main div')].filter((el) => {
      const t = (el.innerText || '').trim();
      const r = el.getBoundingClientRect();
      return t.startsWith('PLUS') && r.height > 400 && r.width < 500;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'plancard');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  download: 'Download', pages: 'Product pages', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The floating pill header: the CRAFT wordmark, Product / Imagine / Community / Pricing / Learn / Download links, Log in and the black Try Craft Free pill.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The CRAFT wordmark anchor.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('header a, nav a').filter({ hasText: /^\s*(Product|Imagine|Pricing|Learn|Download)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header nav link; measured, never followed.', sel: 'header Product link' }, { noScroll: true });
  await S('try-cta', q('header a, header button, nav a').filter({ hasText: /^\s*Try Craft Free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Try Craft Free pill', desc: 'The black "Try Craft Free" header pill (leads to /download); measured, never followed.', sel: 'header Try Craft Free' }, { noScroll: true });
  await S('login-link', q('header a, nav a').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The "Log in" header link (points at docs.craft.do); measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 66px Untitled Serif hero ("Your space for notes, tasks, and big ideas") over the sky collage.', sel: 'h1' });
  await S('hero-cta', q('main a, main button').filter({ hasText: /^\s*Try Craft Free\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The white 48px "Try Craft Free" hero pill (leads to /download); measured, never followed.', sel: 'hero Try Craft Free' });
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Choose The Plan That\u2019s Right For You".', sel: 'h1' }, { noScroll: true });
  await S('billing-toggle', q('button').filter({ hasText: /^\s*(Yearly|Monthly)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'A segment of the Yearly/Monthly billing switch (112x40 inside a pill); toggled locally for the shot, never submitted.', sel: 'Yearly button' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Plan card', desc: 'The PLUS plan card (name, serif price, /month, feature list, CTA); measured, never used.', sel: 'PLUS card' });
  await S('plan-price', q('main *').filter({ hasText: /^\s*\$\d+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A 54px Untitled Serif price figure on a plan card.', sel: 'serif price' });
  await S('team-card', q('main [class*="shadow-block"]').filter({ visible: true }).filter({ hasText: /team/i }).last(), ['default'], { group: g, title: 'Team card', desc: 'The TEAM plan card — the shadow-block variant.', sel: '.shadow-block card' });
  await S('faq-row', q('button').filter({ hasText: /\?/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ row', desc: 'A pricing FAQ accordion row (shadcn-style ring on focus-visible); toggled locally.', sel: 'FAQ accordion row' });
}

async function download() {
  if (!(await newPage('download'))) return;
  await chrome('download');
  const g = G.download;
  await S('dl-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Download headline', desc: '"Get Craft for Free".', sel: 'h1' }, { noScroll: true });
  await S('dl-btn', q('main a, main button').filter({ hasText: /Mac|iPhone|iPad|Windows|Android|Download/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Platform button', desc: 'A platform download action; measured, never followed.', sel: 'download platform button' });
}

async function prodPages() {
  for (const [key, url, sel, title] of [
    ['imagine-h1', 'imagine', 'h1', 'Imagine headline'],
    ['learn-h1', 'learn', 'h1', 'Learn headline'],
    ['write-h1', 'write', 'h1', 'Write headline'],
  ]) {
    if (!(await newPage(url))) continue;
    const g = G.pages;
    await S(key, q(sel).filter({ visible: true }).first(), ['default'], { group: g, title, desc: `The ${url} page heading.`, sel }, { noScroll: true });
  }
  if (!(await newPage('imagine'))) return;
  const g = G.pages;
  await S('imagine-card', q('main a').filter({ hasText: /Blog|Tracker|Log|Journal/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Template card', desc: 'A template card on /imagine (Blog Publisher, Reading Tracker); measured, never followed.', sel: 'imagine template card' });
}

async function footer() {
  if (!(await newPage('home'))) return;
  await chrome('home-footer');
  const g = G.footer;
  const ft = q('footer').filter({ visible: true }).last();
  await ft.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', ft, ['default'], { group: g, title: 'Footer', desc: 'The footer: link columns, the app badges and the legal row.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="youtube"], footer a[href*="linkedin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button, nav button').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The header menu button that opens the nav overlay.', sel: 'header menu button' }, { noScroll: true });
  if (await menu.count()) {
    try {
      await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click()));
      await page.waitForTimeout(1600);
      await markMobileMenu();
    } catch (e) { log('  ! menu open failed', String(e.message).slice(0, 80)); }
  }
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened nav overlay: the Product / Imagine / Pricing rows with Try Craft Free and Log in.', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*(Product|Imagine|Pricing|Learn|Download|Community)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu row', desc: 'A row inside the opened nav overlay.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-download', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /Download for (iOS|Mac|iPad)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile download CTA', desc: 'The black "Download for iOS" pill at the foot of the mobile menu; measured, never followed.', sel: 'mobile menu Download for iOS' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); craft.do paints a single light surface';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, download, prodPages, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k === "prodPages" ? "pages" : k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // link), so the delta is meaningful.
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
