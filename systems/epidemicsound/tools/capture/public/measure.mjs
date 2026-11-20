// Measures epidemicsound.com's public components in every state reachable
// without signing in, subscribing, starting a trial or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing genre sfx login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// epidemicsound.com paints two public themes: an ecru alternative-light
// marketing shell (home, pricing, how-it-works) and a dark catalog shell
// (/music/*, /sound-effects/*). The login/signup forms live on
// login.epidemicsound.com (Keycloak, dark) and are measured only at rest:
// fields are focused, typed into and cleared, nothing is ever submitted.
// The component library is a CSS-module design system (._button_*,
// ._iconButton_*, .TrackRow_*, .es-heading-*) so specs select by CSS-module
// class stems, role, aria-label and structure. The only presses are local UI
// toggles: the "Music" mega-menu trigger, the pricing Monthly/Yearly switch,
// the FAQ accordion and the mobile hamburger; the track-row "Play", "Like",
// "Add to playlist", "Download" and "Copy link" controls, every pricing CTA
// and the login submit are measured, never activated. The high-z cookie
// consent card is hidden by closePromo(), never answered.

import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/', genre: '/music/genres/pop/', sfx: '/sound-effects/categories/ambience/', login: '/login/', signup: '/oauth_registration/', mobile: '/music/genres/pop/' };
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

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    if (state !== 'default' && s.rect && s.rect.w === 0 && s.rect.h === 0) {
      // The element left the layout in this state (track rows swap the cover
      // button out on hover): a 0x0 box is not this state's look, so record
      // the miss instead of a reading.
      c.states[state] = { skipped: 'the element has a 0x0 box in this state (it left the layout)', via: opts.via, run, page: current, url: c.url };
      log('  -', key, state, 'skipped: 0x0');
      return;
    }
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // Each state carries its own provenance: if a later re-run updates the
    // component's page/run/url but fails before re-reading this state, the
    // kept reading still names the run it actually came from.
    c.states[state] = { ...s, crop: file, via: opts.via, run, page: current, url: c.url };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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
  const read = {};
  try {
    const b = context.browser();
    // Both settings in fresh contexts, on a control whose transition is
    // nonzero under no-preference — a reduce-only reading proves nothing.
    for (const mode of ['no-preference', 'reduce']) {
      const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: mode });
      await patch(ctx);
      const p = await ctx.newPage();
      await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(7000);
      await closePromo(p);
      read[mode] = await p.evaluate((s) => {
        const el = document.querySelector(s);
        if (!el) return null;
        const cs = getComputedStyle(el);
        return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
      }, sel).catch(() => null);
      await ctx.close();
    }
    out._meta.reducedMotion[key] = { selector: sel, noPreference: read['no-preference'], reduce: read['reduce'] };
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, ...read, error: String(e).slice(0, 120) }; }
}

const FIELD = ['default', 'focused', 'filled'];

const G = {
  shell: 'App shell and navigation', home: 'Home (alternative-light marketing)',
  pricing: 'Pricing (alternative-light)', catalog: 'Genre page (dark catalog)',
  sfx: 'Sound-effects category (dark catalog)', upsell: 'Signup upsell',
  login: 'Login and signup (Keycloak, dark)', mobile: 'Mobile (390 wide)',
  footer: 'Footer',
};

// Opens the header mega menu: the "Music" ghost button is a local
// disclosure trigger (button, not a link). Waits for genre links to appear.
async function openNavMenu() {
  const ok = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('a[href*="/music/genres/"], a[href*="/music/moods/"]')].some((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).visibility !== 'hidden'; }),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await ok(300)) return 'the mega menu was already open';
  const b = page.locator('header button').filter({ hasText: /^\s*Music\s*$/ }).filter({ visible: true }).first();
  if (!(await b.count())) return 'no Music nav trigger';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok(4000)) return 'clicked "Music" to open the mega menu';
    await page.waitForTimeout(600);
  }
  return 'clicked "Music"; the mega menu did not report open';
}

// Opens the phone nav overlay: the "Show navigation menu" icon button is a
// local disclosure trigger; Escape closes the overlay afterwards.
async function openMobileNav() {
  const ok = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('header a, header button, [class*="Drawer" i] a, [class*="Menu" i] a, [role="dialog"] a')].filter((e) => e.getBoundingClientRect().width > 40 && /pricing|log in|music|sound/i.test(e.textContent || e.getAttribute('aria-label') || '')).length >= 3,
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  const b = page.locator('button[aria-label*="navigation menu" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no mobile menu trigger';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok(4000)) return 'clicked "Show navigation menu" to open the phone nav';
    await page.waitForTimeout(600);
  }
  return 'clicked the hamburger; the nav did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The sticky top bar: ES logotype, mega-menu triggers (Music / Sound effects / Tools / License / Resources / For business), Pricing, Log in and Create free account.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[aria-label="Home"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Epidemic Sound glyph + wordmark link.', sel: 'a[aria-label=Home]' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*Music\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Nav menu trigger', desc: 'The "Music" ghost button that opens the mega menu — a local disclosure; the opened state was measured after clicking it, its links never followed.', sel: 'header button Music' }, { noScroll: true, allowLink: true });
  await S('nav-menu', q('a[href*="/music/genres/"]').filter({ visible: true }).first().locator('xpath=ancestor::div[2]'), ['default'], { group: g, title: 'Mega menu', desc: 'The dropdown opened by the "Music" trigger; its links were never followed.', sel: 'mega menu (genres-link ancestor)' }, { open: openNavMenu, noScroll: true, noReset: true });
  await S('nav-menu-item', q('a[href*="/music/genres/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega menu item', desc: 'A genre link inside the opened mega menu; measured, never followed.', sel: 'a[href*=/music/genres/]' }, { open: openNavMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', q('header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Pricing link', desc: 'The header Pricing link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('btn-login', q('header a, header button').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Log in button', desc: 'The secondary "Log in" button; links to login.epidemicsound.com, measured never followed. The header ships a hidden twin of the same link before the painted one, so the visible copy is the last match.', sel: 'header Log in (._secondary_)' }, { noScroll: true });
  await S('btn-signup', q('header a, header button').filter({ hasText: /^\s*Create free account\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create account button', desc: 'The primary "Create free account" button — black fill on the light marketing theme; measured never followed.', sel: 'header Create free account (._primary_)' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The home hero display heading (es-heading class).', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a, main button, section a, section button').filter({ hasText: /create free account|start free trial|get started/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The primary call-to-action inside the hero; measured never followed.', sel: 'hero primary CTA' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pr-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Our subscriptions" — the es-heading-xl display heading over the plan columns.', sel: 'h1' }, { noScroll: true });
  await S('billing-switch', q('input[role="switch"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Billing switch', desc: 'The Monthly/Yearly billing switch above the plans — a local toggle; the opened state is the toggled position after clicking it, never checked out.', sel: 'input[role=switch]' }, { noScroll: true, allowLink: true });
  await S('plan-name', q('h2').filter({ hasText: /^\s*Creator\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'The "Creator" plan heading (es-subheading-l) over a plan column.', sel: 'plan h2 Creator' });
  // The smallest element whose own text is a price, not the last of a
  // `main, section, div` union (that read an empty 688x384 div at y 6525).
  await S('plan-price', q('span, p, div').filter({ hasText: /^\s*(US)?\$\s?\d[\d.,]*\s*(\/\s*month|per month)?\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price line', desc: 'The price line inside a plan column.', sel: 'price text' });
  await S('plan-cta', q('a, button').filter({ hasText: /^\s*Get 30 days free\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The primary "Get 30 days free" button inside a plan column — starts a trial; measured never followed.', sel: 'Get 30 days free (._primary_ ._m_)' });
  await S('compare-h2', q('h2').filter({ hasText: /compare plans/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Compare plans heading', desc: 'The "Compare plans" heading over the feature matrix; a hidden copy precedes it in the DOM, so the painted one is the last match.', sel: 'h2 Compare plans' });
  save();
}

async function genre() {
  if (!(await newPage('genre'))) return;
  await sheetsFor('genre');
  await chrome('genre');
  const g = G.shell;
  await S('c-header', q('header[class*="sticky"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header (dark)', desc: 'The sticky header on the dark catalog theme (header.sticky.top-0); primary button reads white here.', sel: 'header.sticky' }, { noScroll: true });
  await S('c-signup', q('header[class*="sticky"] a, header[class*="sticky"] button').filter({ hasText: /^\s*Create free account\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Create account button (dark)', desc: 'The primary button on the dark theme — white fill, black text; measured never followed. Scoped to the sticky header so a lower banner of the same label cannot match.', sel: 'header.sticky Create free account' }, { noScroll: true });
  const c = G.catalog;
  await S('breadcrumbs', q('nav [class*="_breadcrumb_"], ol[class*="_breadcrumb_"], [class*="_breadcrumb_"]').filter({ visible: true }).first(), ['default'], { group: c, title: 'Breadcrumbs', desc: 'The MUSIC / GENRES / POP breadcrumb row over the genre banner.', sel: '[class*=_breadcrumb_]' }, { noScroll: true });
  await S('genre-banner', q('div[class*="_genre_"]').filter({ visible: true }).first(), ['default'], { group: c, title: 'Genre banner', desc: 'The coloured genre header card (#ff82c2 pink for pop) holding the GENRE kicker and the h1; the _genre_ module class is what paints the colour.', sel: 'div[class*=_genre_]' }, { noScroll: true });
  await S('genre-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: c, title: 'Genre heading', desc: '"Pop music" — es-heading-m, black on the pink banner.', sel: 'h1' }, { noScroll: true });
  await S('track-list', q('ul[class*="TrackList_trackList"]').filter({ visible: true }).first(), ['default'], { group: c, title: 'Track list', desc: 'The genre page track list (ul.TrackList); rows virtualise as it scrolls.', sel: 'ul[class*=TrackList_trackList]' });
  await S('track-row', q('li[class*="TrackRow_trackRow"]').filter({ visible: true }).first(), ['default', 'hover'], { group: c, title: 'Track row', desc: 'A 56px track row: album-cover play button, title, artist, duration, BPM, genre/mood tags; hover reveals row actions.', sel: 'li[class*=TrackRow_trackRow]' });
  await S('track-play', q('button[aria-label="Play"]').filter({ visible: true }).first(), B4, { group: c, title: 'Track play button', desc: "A row's album-cover play button; measured, never pressed (signed-out playback is gated anyway). On row hover the cover button leaves the layout, so its hover state is recorded as skipped, not as a reading.", sel: 'button[aria-label=Play]' });
  await S('track-like', q('button[aria-label="Like"]').filter({ visible: true }).first(), B4, { group: c, title: 'Like button', desc: "A row's heart icon button; measured, never toggled (needs an account).", sel: 'button[aria-label=Like]' });
  await S('track-similar', q('button[aria-label="Find similar"]').filter({ visible: true }).first(), B4, { group: c, title: 'Find similar button', desc: "A row's Find-similar icon button; measured, never followed.", sel: 'button[aria-label="Find similar"]' });
  await S('track-add', q('button[aria-label="Add to playlist"]').filter({ visible: true }).first(), B4, { group: c, title: 'Add to playlist button', desc: "A row's Add-to-playlist icon button; measured, never toggled (needs an account).", sel: 'button[aria-label="Add to playlist"]' });
  await S('track-download', q('button[aria-label="Download"]').filter({ visible: true }).first(), B4, { group: c, title: 'Download button', desc: "A row's Download icon button; measured, never pressed (licensed download).", sel: 'button[aria-label=Download]' });
  const u = G.upsell;
  await S('wantmore', q('h2').filter({ hasText: /want more music/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[3]'), ['default'], { group: u, title: 'Want-more banner', desc: 'The #ff82c2 pink "Want more music?" upsell card between the list and the FAQ — an accent-coloured island on the dark page.', sel: 'WantMoreBanner container' });
  await S('wantmore-cta', q('h2').filter({ hasText: /want more music/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[3]').locator('a, button').filter({ visible: true }).first(), B4, { group: u, title: 'Upsell CTA', desc: "The banner's Create-free-account button; measured never followed.", sel: 'WantMoreBanner CTA' });
  await S('faq-row', q('h2[class*="_heading_1l58k"], h2[class*="_heading_"]').filter({ hasText: /\?\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: c, title: 'FAQ accordion row', desc: 'An FAQ accordion heading at the bottom of the catalog page — a local disclosure; the opened state was measured after clicking it.', sel: 'faq heading' }, { allowLink: true });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The catalog page footer: link columns, social icon buttons, locale line.', sel: 'footer' });
  await S('social-icon', q('a[aria-label="Spotify"], a[aria-label="Instagram"]').filter({ visible: true }).first(), B4, { group: f, title: 'Social icon button', desc: 'A footer social icon button (ghost, _m_ size); measured never followed.', sel: 'a[aria-label=Spotify]' });
  save();
}

async function sfx() {
  if (!(await newPage('sfx'))) return;
  await sheetsFor('sfx');
  await chrome('sfx');
  const g = G.sfx;
  await S('sfx-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'SFX category heading', desc: 'The sound-effects category page heading on the dark theme.', sel: 'h1' }, { noScroll: true });
  await S('sfx-row', q('li[class*="TrackRow_trackRow"], [class*="TrackRow_trackRow"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'SFX track row', desc: 'An SFX track row (name, category tags, duration).', sel: 'track row' });
  await S('sfx-play', q('button[aria-label="Play"]').filter({ visible: true }).first(), B4, { group: g, title: 'SFX play button', desc: "An SFX row's play button; measured, never pressed. As on the genre list, row hover swaps the cover button out, so its hover state is recorded as skipped.", sel: 'button[aria-label=Play]' });
  await S('sfx-category-card', q('a[class*="scrollingText"][href*="/sound-effects/categories/"]').filter({ visible: true }).first(), B4, { group: g, title: 'SFX subcategory link', desc: 'A subcategory link inside a row\'s categories column (e.g. "Suburban" under Ambience) — this page has no large category card, the in-row text link is the real subcategory surface; measured, never followed.', sel: 'a[class*=scrollingText]' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('kc-card', q('.form-card, form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The dark Keycloak form-card on login.epidemicsound.com: logo, social buttons, email/password form, links.', sel: '.form-card' }, { noScroll: true });
  await S('kc-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login heading', desc: 'The "Log in" heading over the form.', sel: 'h1' }, { noScroll: true });
  await S('kc-social-google', q('a#social-google, a').filter({ hasText: /continue with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Social button', desc: 'The "Continue with Google" social button; measured, never followed.', sel: '#social-google' }, { noScroll: true });
  await S('kc-email', q('input#username, input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The login email input; focused and typed into then cleared — never submitted.', sel: 'input#username' }, { noScroll: true, fillText: 'name@example.com' });
  await S('kc-password', q('input#password, input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The login password input; focused and typed into then cleared — never submitted.', sel: 'input#password' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('kc-show-pass', q('.password-visibility-toggle, button[aria-label*="password" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Show-password button', desc: 'The eye icon button inside the password field (a local reveal toggle); measured, never clicked.', sel: '.password-visibility-toggle' }, { noScroll: true });
  await S('kc-submit', q('button#kc-login, button[type="submit"]').filter({ hasText: /log in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in submit', desc: 'The white primary submit button; its states were measured but it was never clicked — nothing was submitted.', sel: '#kc-login' }, { noScroll: true });
  await S('kc-signup-link', q('a').filter({ hasText: /create account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create-account link', desc: 'The "Create account" link over the form; measured, never followed.', sel: 'Create account' }, { noScroll: true });
  await S('kc-forgot', q('a').filter({ hasText: /forgot password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The "Forgot password?" link; measured, never followed.', sel: 'a Forgot password' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  const g = G.login;
  await S('su-card', q('.form-card, form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup card', desc: 'The Keycloak registration card; measured at rest only.', sel: '.form-card' }, { noScroll: true });
  await S('su-field', q('input[type="email"], input[type="text"], input.input-field').filter({ visible: true }).first(), FIELD, { group: g, title: 'Signup field', desc: 'A registration form input; focused and typed into then cleared — never submitted.', sel: 'signup input' }, { noScroll: true, fillText: 'name@example.com' });
  // Not `a.button`: it caught the "Continue with Google" link first.
  await S('su-submit', q('button[type="submit"], input[type="submit"]').filter({ hasText: /create|continue|sign up/i }).filter({ hasNotText: /google|apple|facebook/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup submit', desc: "The registration form's submit action; its states were measured but it was never clicked — nothing was submitted.", sel: 'signup submit' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/music/genres/pop/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar: ES glyph, Create free account, hamburger.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('button[aria-label*="navigation menu" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-hamburger', ham, [...B4, 'opened'], { group: g, title: 'Mobile hamburger', desc: 'The "Show navigation menu" icon button — a local disclosure; the opened state was measured after clicking it.', sel: 'button[aria-label*=menu]' }, { noScroll: true, allowLink: true });
  await S('m-nav-item', q('header a, [role="dialog"] a, [class*="Menu" i] a, [class*="Drawer" i] a').filter({ hasText: /^\s*Pricing\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav link', desc: 'A link inside the opened phone nav; measured, never followed.', sel: 'mobile nav Pricing' }, { open: openMobileNav, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-cta', q('header a, header button').filter({ hasText: /create free account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The Create-free-account button in the phone header; measured never followed.', sel: 'mobile Create free account' }, { noScroll: true });
  await S('m-genre-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile genre heading', desc: '"Pop music" on the phone genre banner.', sel: 'mobile h1' });
  await S('m-track-row', q('li[class*="TrackRow_trackRow"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile track row', desc: 'A 56px track row in the phone list (cover, title, artist).', sel: 'mobile track row' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); home, pricing and how-it-works paint alternative-light (ecru), the catalog and SFX pages paint dark, and the Keycloak account forms paint dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, genre, sfx, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that really transitions: the pricing
  // billing switch paints a 0.125s background-colour transition, so the
  // no-preference vs reduce delta is meaningful (the track play button's
  // transition is already 0s under both settings).
  if (!pages.length || pages.includes('pricing')) await reducedMotion('pricing', 'input[role="switch"]');
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
