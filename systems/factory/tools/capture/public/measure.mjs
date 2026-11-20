// Measures factory.com's (and docs.factory.com's) public components in every
// state reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home enterprise pricing product contact docs signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// Every factory.com marketing page ships <html data-theme="light">; the dark
// token layer paints inside scoped sections — the [data-dark-hero] heroes on
// /enterprise and the /product pages, .invert-color-scheme panels and the dark
// site footer — and docs.factory.com's three-way .theme-selector-button
// toggle, which is where whole-surface dark is measured (states named
// 'dark'). app.factory.ai redirects to auth.factory.ai, a dark sign-in card
// measured at rest. Specs select by role, aria-label or text. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the
// header's Product mega-menu button (hover opens .megamenu-viewport), the
// docs theme selector and the mobile "Open menu" button; the contact and
// sign-in fields are typed into and cleared, never submitted; SUBMIT,
// CONTINUE and every plan CTA are measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, DOCS, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', enterprise: '/enterprise', pricing: '/pricing', contact: '/contact', docs: DOCS + '/docs', signin: LOGIN_URL, mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Waits for the lazily-mounted HubSpot contact form's fields to appear.
async function waitForm() {
  for (let i = 0; i < 14; i++) {
    const n = await page.evaluate(() => document.querySelectorAll('input:not([type="hidden"]),textarea').length).catch(() => 0);
    if (n >= 3) return;
    await page.waitForTimeout(1500);
  }
  log('  ! contact form fields never mounted');
}

// Waits for the app.factory.ai splash to redirect into the auth.factory.ai
// sign-in card (email field + "Sign in" heading).
async function waitSignin() {
  for (let i = 0; i < 25; i++) {
    const ok = await page.evaluate(() => /sign in/i.test((document.body && document.body.innerText) || '') && !!document.querySelector('input[type="email"], input[name="email"]')).catch(() => false);
    if (ok) { await page.waitForTimeout(2500); return; }
    await page.waitForTimeout(2000);
  }
  log('  ! sign-in card never appeared');
}

// Sets the docs theme through the three-way .theme-selector-button control —
// a local UI toggle, no form, no navigation.
async function setDocsTheme(theme) {
  const btn = page.locator(`button.theme-selector-button[aria-label="Switch to ${theme} theme"]`).first();
  // a state labelled dark is only read when dark painted: a missing control
  // or a toggle that did not take throws, and the state records the error
  // instead of a light reading (2026-11 audit, finding 17-5; not run since)
  if (!(await btn.count())) throw new Error('no theme selector on this docs page');
  await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  const cur = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
  if (cur !== theme.toLowerCase()) throw new Error(`docs theme reads ${JSON.stringify(cur)} after switching to ${theme}`);
  return `docs theme selector switched to ${theme} (data-theme now ${JSON.stringify(cur)})`;
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
    // A revealed panel (a dropdown's options, an accordion's answer) is a
    // different element than the trigger: measure it beside the trigger and
    // let the opened state's crop show it, question/field included when the
    // panel locator is their shared ancestor.
    let cropTarget = opts.cropLoc || loc;
    if (state === 'opened' && opts.panel) {
      const pl = (await opts.panel()).filter({ visible: true }).first();
      // The reveal animation can lag the trigger's state flip; give the
      // panel a moment to mount before declaring the read panel-less.
      for (let i = 0; i < 8 && !(await pl.count()); i++) await page.waitForTimeout(300);
      if (await pl.count()) {
        s.panel = await styleOf(pl).catch(() => undefined);
        cropTarget = pl;
      }
    }
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, cropTarget.filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, run };
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          const lt = loc.filter({ visible: true }).first();
          const reportsOpen = (el) => el.getAttribute('aria-expanded') === 'true' || el.getAttribute('data-state') === 'open' || el.open === true || (el.closest && el.closest('details') && el.closest('details').open === true);
          // An already-open control must not be toggled — that would close it
          // and measure the collapsed state as "opened".
          const already = await lt.evaluate(reportsOpen).catch(() => false);
          if (!already) await toggle(loc, { allowLink: opts.allowLink });
          await page.waitForTimeout(900);
          // Wait out the reveal animation: a panel read before it finishes
          // measures a collapsed (or still-closed) container.
          for (let i = 0; i < 8; i++) {
            if (await lt.evaluate(reportsOpen).catch(() => false)) break;
            if (!(await lt.evaluate((el) => el.hasAttribute('aria-expanded') || el.hasAttribute('data-state') || el.tagName === 'DETAILS' || el.closest('details') !== null).catch(() => false))) break;
            await page.waitForTimeout(350);
          }
          via = already ? 'already open; the revealed panel measured without toggling' : 'own toggle';
        }
      } else if (st === 'selected') {
        await toggle(loc, { allowLink: true });
        await page.waitForTimeout(500);
        via = 'own toggle, pressed once; a local UI state, never submitted';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|book|book demo|contact sales|start building|subscribe.*|sign up)$/i;
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
  shell: 'Site chrome', home: 'Home', dark: 'Scoped dark surfaces', pricing: 'Pricing',
  contact: 'Contact form', docs: 'Docs (docs.factory.com)', signin: 'Sign-in card (auth.factory.ai)',
  mobile: 'Mobile (390 wide)', footer: 'Footer', enterprise: 'Enterprise / product pages',
};

// Opens the header's "Product" mega-menu by hovering its button — the
// .megamenu-viewport panel flips to data-state="open" on pointer hover (a
// local UI toggle; its links are never followed). Falls back to click and
// keyboard Enter when hover does not reach it.
async function openProductMenu() {
  const btn = page.locator('header button').filter({ hasText: /^Product$/ }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Product trigger';
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await open()) return 'the mega-menu was already open';
  for (let i = 0; i < 3; i++) {
    await btn.hover().catch(() => {});
    await page.waitForTimeout(800);
    if (await open()) return 'hovered the "Product" button to open the mega-menu panel';
    await btn.click({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(700);
    if (await open()) return 'clicked the "Product" button to open the mega-menu panel';
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the "Product" button and pressed Enter to open the mega-menu panel';
  }
  return 'activated "Product"; the panel did not report open';
}

// Opens the mobile nav overlay via the header's "Open menu" button — a local
// UI toggle; its links are never followed.
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body > div, body > nav, [role="dialog"], .megamenu-viewport, header nav')].find((x) => {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      const onScreen = r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
      return r.height > 300 && onScreen && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
    });
    return !!el;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('header button[aria-label*="menu" i]').first();
  const btn = (await b.count()) ? b : page.locator('header button').filter({ hasText: /open menu|close menu/i }).first();
  if (!(await btn.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    if (await open()) return 'clicked the menu button to open the nav overlay';
    await page.waitForTimeout(500);
    await btn.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the menu button and pressed Enter to open the nav overlay';
  }
  return 'activated the menu button; the overlay did not report open';
}

const FIELD = ['default', 'focused', 'filled'];
// The bordered pill CTAs (CONTACT SALES / DOWNLOAD / Get Started / BOOK DEMO):
// a <group> flex anchor or button with a border.
const CTA = 'a.group, button.group, a[class*="border"]';

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header[data-site-header], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed 72px top bar with the backdrop-blur mask: Factory wordmark, Product/Enterprise/Company mega-menu buttons, Pricing/News/Docs links, locale globe, SIGN IN, CONTACT SALES and DOWNLOAD.', sel: 'header[data-site-header]' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Factory mark-and-wordmark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-menu-btn', q('header button').filter({ hasText: /^Product$/ }).first(), [...B4, 'opened'], { group: g, title: 'Mega-menu trigger', desc: 'The "Product" header button — opens the mega-menu panel on hover (aria-expanded). The opened state was measured after a real pointer hover.', sel: 'header button Product' }, { noScroll: true, before: { opened: async (loc) => { await loc.hover(); await page.waitForTimeout(900); return 'hovered the button to open the mega-menu'; } } });
  await S('nav-panel', q('.megamenu-viewport').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The mega-menu panel opened under the header by hovering "Product"; its links were never followed.', sel: '.megamenu-viewport' }, { open: openProductMenu, noScroll: true, noReset: true });
  await S('nav-menu-item', q('.megamenu-viewport a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega-menu item', desc: 'A link inside the opened mega-menu panel; measured, never followed.', sel: '.megamenu-viewport a' }, { open: openProductMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(700, 400);
  await S('nav-link', q('header a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A header nav link (Pricing); measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-signin', q('header').getByRole('link', { name: 'Sign in' }).first(), B4, { group: g, title: 'Sign in link', desc: 'The "SIGN IN" header link to app.factory.ai; measured, never followed.', sel: 'header a SIGN IN' }, { noScroll: true });
  await S('nav-cta', q('header').getByRole('link', { name: 'Download', exact: true }).first(), B4, { group: g, title: 'Header primary CTA', desc: 'The dark "DOWNLOAD" pill in the header; links to /product/desktop, measured never followed.', sel: 'header a DOWNLOAD' }, { noScroll: true });
  await S('nav-cta2', q('header').getByRole('link', { name: /contact sales/i }).first(), B4, { group: g, title: 'Header secondary CTA', desc: 'The bordered "CONTACT SALES" pill in the header; links to /contact, measured never followed.', sel: 'header a CONTACT SALES' }, { noScroll: true });
  const h = G.home;
  await S('hero-mark', q('main svg, main [class*="mark" i], h1 + *').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero mark', desc: 'The Factory asterisk mark above the masthead.', sel: 'hero mark svg' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"AI CODING AGENTS FOR THE ENTERPRISE" — the uppercase Geist masthead.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p, h2').filter({ hasText: /Model agnostic/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subline', desc: '"Model agnostic. Deployed anywhere." — the mono tagline under the masthead.', sel: 'hero subline' }, { noScroll: true });
  await S('hero-cta', q(CTA).filter({ hasText: /^\s*DOWNLOAD\s*$/i }).filter({ visible: true }).last(), B4, { group: h, title: 'Hero CTA', desc: 'The dark "DOWNLOAD" pill in the hero; measured never followed.', sel: 'hero DOWNLOAD' });
  await S('hero-cta2', q(CTA).filter({ hasText: /BOOK DEMO/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary CTA', desc: 'The bordered "BOOK DEMO" pill beside it; measured never followed.', sel: 'hero BOOK DEMO' });
  const cmd = await domFind(page, /curl -fsSL/, { sel: 'div, code, pre, button, a', tag: 'mc', up: 'div', leaf: true, minW: 200 });
  await S('install-cmd', cmd, ['default'], { group: h, title: 'Install command', desc: 'The mono `curl -fsSL https://app.factory.ai/cli | sh` copy box under the CTAs.', sel: 'install command box' });
  await S('copy-btn', page.getByRole('button', { name: /copy code/i }).first(), B4, { group: h, title: 'Copy button', desc: 'The "Copy code" control beside the install command; measured, never clicked.', sel: 'button Copy code' });
  await S('section-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The dark page footer: sitemap columns (Resources/Company/Legal), the mark.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^Docs$/ }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link on the dark footer; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  save();
}

async function enterprise() {
  if (!(await newPage('enterprise'))) return;
  await sheetsFor('enterprise');
  await chrome('enterprise');
  const d = G.dark;
  await S('dark-hero', q('[data-container-variant="inverted"]').filter({ visible: true }).first(), ['default'], { group: d, title: 'Dark scoped section', desc: 'A [data-container-variant="inverted"] panel painting the dark token layer inside the light page — /enterprise\'s "Built for large enterprises" section.', sel: '[data-container-variant=inverted]' });
  await S('dark-h1', q('[data-container-variant="inverted"] h1, [data-container-variant="inverted"] h2, [data-container-variant="inverted"] h3').filter({ visible: true }).first(), ['default'], { group: d, title: 'Dark section headline', desc: 'The inverted section\'s heading, light ink on the near-black field.', sel: '[data-container-variant=inverted] h2' });
  await S('dark-eyebrow', q('[data-container-variant="inverted"] p, [data-container-variant="inverted"] span').filter({ hasText: /ENTERPRISE|DATA|FACTORY/i }).filter({ visible: true }).first(), ['default'], { group: d, title: 'Dark section eyebrow', desc: 'The small uppercase eyebrow label inside the inverted section.', sel: '[data-container-variant=inverted] eyebrow' });
  await S('dark-cta', q('[data-container-variant="inverted"] p').filter({ hasText: /SSO|SAML|compute|compliance/i }).filter({ visible: true }).first(), ['default'], { group: d, title: 'Dark feature label', desc: 'A feature row label inside the inverted section ("SSO + SAML") — the section carries no CTA.', sel: '[data-container-variant=inverted] feature label' });
  const g = G.enterprise;
  await S('ent-h2', q('h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading (enterprise)', desc: 'An /enterprise section heading.', sel: 'enterprise h2' });
  await S('ent-card', q('section div, section li, [class*="card" i]').filter({ hasText: /security|deploy|model|agent|sso|saml|audit/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Enterprise feature card', desc: 'An enterprise capability card on the light field.', sel: 'enterprise feature card' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The "Pricing Plans" masthead.', sel: 'h1' }, { noScroll: true });
  const pro = page.getByRole('radio', { name: 'PRO' }).first();
  await S('tier-tab', pro, [...B4, 'selected'], { group: g, title: 'Plan-tier tab', desc: 'A plan-tier switcher button (PRO/PLUS/MAX, role=radio). PRO is the page\'s own default, so another tier was selected first and the resting states read PRO unselected; the selected state was measured after clicking PRO — a local UI toggle.', sel: 'plan tier PRO' }, { noScroll: true, allowLink: true,
    open: async () => {
      // Pick a different tier first so PRO's unselected style is what the
      // default/hover/focus/pressed states measure — then wait for PRO to
      // report unselected, since a click that never landed would silently
      // re-measure the selected style as "default". The radios' accessible
      // names carry more than the tier label, so name-regex matching can
      // still resolve to PRO; walk the radios and click the first that
      // visibly isn't it.
      const radios = page.getByRole('radio').filter({ visible: true });
      let other = null;
      for (let i = 0, n = await radios.count(); i < n; i++) {
        const r = radios.nth(i);
        const t = await r.evaluate((el) => (el.innerText || el.getAttribute('aria-label') || '').trim());
        if (!/^pro\b/i.test(t)) { other = r; break; }
      }
      if (!other) return;
      await other.click({ timeout: 4000 }).catch(() => other.evaluate((el) => el.click()));
      for (let i = 0; i < 10; i++) {
        const off = await pro.evaluate((el) => el.getAttribute('aria-checked') !== 'true').catch(() => false);
        if (off) return;
        await page.waitForTimeout(300);
        if (i === 4) await other.evaluate((el) => el.click()).catch(() => {});
      }
      log('  ! tier-tab: PRO still reports selected after switching tier');
    } });
  await S('plan-card', q('div, section, li').filter({ hasText: /Pro/i }).filter({ hasText: /\$|month|mo\b/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (name, price, feature list).', sel: 'pricing plan card' });
  await S('plan-cta', q('a, button').filter({ hasText: /get started|choose|select|contact sales|start/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action; measured never followed.', sel: 'plan card CTA' });
  // The first FAQ item ships open (data-state="open", aria-expanded="true"):
  // measure a closed one so 'opened' really is a closed → opened transition.
  // The accordion lazy-mounts on approach, so scroll it in before counting —
  // a closed-item lookup against an unmounted section silently falls back to
  // the open-by-default first row. Pin the item by index, not by selector:
  // an aria-expanded="false" locator re-resolves to a different row the
  // moment the chosen one opens.
  const allFaq = q('button, [role="button"], summary').filter({ hasText: /\?/ });
  await allFaq.last().evaluate((el) => el.scrollIntoView({ block: 'center' })).catch(() => {});
  await page.waitForTimeout(1200);
  let faqIdx = 0;
  for (let i = 0, n = await allFaq.count(); i < n; i++) {
    const st_ = await allFaq.nth(i).evaluate((el) => el.getAttribute('aria-expanded') ?? el.getAttribute('data-state')).catch(() => null);
    if (st_ !== 'true' && st_ !== 'open') { faqIdx = i; break; }
  }
  const faq = allFaq.nth(faqIdx);
  await S('faq-item', faq, [...B4, 'opened'], { group: g, title: 'FAQ accordion item', desc: 'A question row in the pricing FAQ accordion; the opened state was measured after clicking the question toggle, and the revealed answer region is measured beside the button (the opened crop shows the answer).', sel: 'faq item' }, { allowLink: true,
    // The trigger's aria-controls names the exact answer region it reveals —
    // no class guessing (every accordion row keeps its region mounted, so a
    // bare [role=region] lookup can resolve to a different row's collapsed
    // panel mid-animation).
    panel: async () => {
      const cid = await faq.getAttribute('aria-controls').catch(() => null);
      if (cid) return page.locator(`[id="${cid}"]`).first();
      return faq.locator('xpath=ancestor::*[.//*[@role="region"] or .//dd or .//*[contains(@class,"answer")] or .//*[contains(@class,"panel")]][1]')
        .or(q('[role="region"], dd, [class*="answer" i], [class*="faq" i][class*="panel" i]').filter({ visible: true })).first();
    } });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await waitForm();
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: '"Bring Autonomy to your Engineering Organization" — the /contact masthead beside the form.', sel: 'h1' }, { noScroll: true });
  await S('field-firstname', q('input[name*="firstname" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'First name field', desc: 'The HubSpot First Name text input; focused and typed into then cleared — never submitted.', sel: 'input[name*=firstname]' }, { noScroll: true, fillText: 'Ada' });
  await S('field-email', q('input[type="email"], input[name*="email" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The Work Email input; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { noScroll: true });
  const sel = q('input[placeholder*="Select one" i]').filter({ visible: true }).first();
  await S('field-select', sel, [...B4, 'opened'], { group: g, title: 'Topic select', desc: 'The "Select one..." dropdown field (a HubSpot select rendered as a read-only input); the opened state was measured after clicking it — a local UI toggle, no option chosen — and the revealed options list is measured beside the field (the opened crop shows the list).', sel: 'contact select' }, { noScroll: true, allowLink: true,
    // HubSpot portals the options list out of the field's own subtree, so the
    // list itself is the panel locator and the crop.
    panel: () => q('[role="listbox"], [role="listbox"] *, ul[class*="dropdown" i], [class*="select" i][class*="menu" i], [id*="listbox" i]').filter({ visible: true }).first() });
  await S('field-msg', q('textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Message textarea', desc: 'The "how can we help" textarea; focused and typed into then cleared — never submitted.', sel: 'textarea' }, { noScroll: true, fillText: 'A short question about Droid.' });
  await S('send-btn', q('button[type="submit"], button').filter({ hasText: /^SUBMIT$/i }).first(), B4, { group: g, title: 'Submit button', desc: 'The form\'s SUBMIT button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'contact SUBMIT' }, { noScroll: true });
  save();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-header', q('header, [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs header', desc: 'The docs top bar: wordmark, Documentation/API Reference/Changelog tabs, GitHub + Discord icons, SIGN IN, DOWNLOAD, the three-way theme selector.', sel: 'docs header' }, { noScroll: true });
  await S('docs-theme-btn', q('button.theme-selector-button[aria-label="Switch to Dark theme"]').first(), B4, { group: g, title: 'Theme selector button', desc: 'One segment of the docs light/dark/system theme selector; a local UI toggle.', sel: '.theme-selector-button' }, { noScroll: true });
  await S('docs-sidebar', q('aside, nav').filter({ hasText: /Start Here|Documentation/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar', desc: 'The left navigation column of the docs.', sel: 'docs sidebar' }, { noScroll: true });
  await S('docs-nav-link', q('aside a, nav a').filter({ hasText: /Available Models/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav link', desc: 'A sidebar navigation link; measured, never followed.', sel: 'docs sidebar a' }, { noScroll: true });
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs headline', desc: '"Welcome to Factory" — the docs landing masthead.', sel: 'docs h1' }, { noScroll: true });
  await S('docs-cta', q('a, button').filter({ hasText: /CREATE AN ACCOUNT/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs CTA', desc: 'The "CREATE AN ACCOUNT" action; measured, never followed.', sel: 'docs CTA' });
  await S('docs-code', q('pre, [data-rehype-pretty-code-figure], figure').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A docs code block (rehype-pretty-code / shiki themed).', sel: 'docs pre' });
  await S('docs-card', q('a, div').filter({ hasText: /QUICKSTART GUIDE|Ship Code Faster|Start with a surface/i }).filter({ visible: true }).last(), ['default', 'hover'], { group: g, title: 'Docs link card', desc: 'A docs path card (QUICKSTART GUIDE / "Ship Code Faster"); measured, never followed.', sel: 'docs path card' });
  // Whole-surface dark: the same components re-read after the theme selector
  // switches the page to data-theme="dark".
  // The dark pass runs only when the switch really painted dark, and every
  // dark reading re-checks the root attribute first: a failed switch never
  // saves light styles as dark readings (2026-11 audit, 17-5; not run since).
  const before = { dark: async () => setDocsTheme('Dark') };
  const isDark = async () => (await page.evaluate(() => document.documentElement.getAttribute('data-theme')).catch(() => null)) === 'dark';
  let darkOk = await before.dark().then(() => true, (e) => { log('  docs dark pass skipped:', e.message); return false; });
  if (darkOk && !(await isDark())) { log('  docs page is no longer dark; remaining dark readings skipped'); darkOk = false; }
  if (darkOk) await S('docs-h1-dk', q('h1').filter({ visible: true }).first(), ['dark'], { group: g, title: 'Docs headline (dark)', desc: 'The docs masthead re-measured after the theme selector switched the page to dark.', sel: 'docs h1, dark theme' }, { noScroll: true, before });
  if (darkOk && !(await isDark())) { log('  docs page is no longer dark; remaining dark readings skipped'); darkOk = false; }
  if (darkOk) await S('docs-sidebar-dk', q('aside, nav').filter({ hasText: /Start Here|Documentation/ }).filter({ visible: true }).first(), ['dark'], { group: g, title: 'Docs sidebar (dark)', desc: 'The sidebar re-measured in dark.', sel: 'docs sidebar, dark theme' }, { noScroll: true, before: { dark: async () => 'still dark from the previous toggle' } });
  if (darkOk && !(await isDark())) { log('  docs page is no longer dark; remaining dark readings skipped'); darkOk = false; }
  if (darkOk) await S('docs-code-dk', q('pre, [data-rehype-pretty-code-figure], figure').filter({ visible: true }).first(), ['dark'], { group: g, title: 'Code block (dark)', desc: 'The code block re-measured in dark (the --shiki-dark palette).', sel: 'docs pre, dark theme' }, { noScroll: true, before: { dark: async () => 'still dark' } });
  if (darkOk && !(await isDark())) { log('  docs page is no longer dark; remaining dark readings skipped'); darkOk = false; }
  if (darkOk) await S('docs-nav-link-dk', q('aside a, nav a').filter({ hasText: /Available Models/i }).filter({ visible: true }).first(), ['dark', 'hover'], { group: g, title: 'Docs nav link (dark)', desc: 'A sidebar link re-measured in dark; measured, never followed.', sel: 'docs sidebar a, dark theme' }, { noScroll: true });
  // A skipped dark reading keeps its saved entry as it was (styles, page,
  // run and dates): marking it touched stops the end-of-run cleanup from
  // pruning it as unmeasured while the docs page still counts as finished.
  if (!darkOk) for (const k of ['docs-h1-dk', 'docs-sidebar-dk', 'docs-code-dk', 'docs-nav-link-dk']) touched.add(k);
  save();
}

async function signin() {
  current = 'signin';
  if (!(await newPage('signin', { wait: 3000 }))) return;
  await waitSignin();
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.signin;
  await S('signin-panel', q('form, main, [class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in panel', desc: 'The dark auth.factory.ai sign-in card: "Sign in", email field, Continue-with-email and Google actions.', sel: 'signin form' }, { noScroll: true });
  await S('signin-field', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The e-mail input on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'input[name=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('signin-submit', q('button').filter({ hasText: /continue with email/i }).first(), B4, { group: g, title: 'Continue with email', desc: 'The email submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'signin Continue with email' }, { noScroll: true });
  await S('signin-google', q('a, button').filter({ hasText: /continue with google/i }).first(), B4, { group: g, title: 'Continue with Google', desc: 'The Google OAuth action; measured, never followed.', sel: 'signin Continue with Google' }, { noScroll: true });
  await S('signin-signup', q('a').filter({ hasText: /sign up/i }).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Sign up" link under the card; measured, never followed.', sel: 'signin Sign up' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header[data-site-header], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header: the mark, the locale globe and the "Open menu" button — there is no header CTA pill at 390 wide.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('header button[aria-label*="menu" i]').first();
  const btn = (await ham.count()) ? ham : q('header button').filter({ hasText: /open menu|close menu/i }).first();
  await S('m-menu-btn', btn, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The "Open menu" button that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.', sel: 'mobile header menu button' }, { noScroll: true, allowLink: true });
  const drawer = q('header nav[class*="absolute" i], header nav[class*="h-full" i]').filter({ visible: true }).last();
  await S('m-drawer', drawer, ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await S('m-cta', drawer.locator('a').filter({ hasText: /^\s*DOWNLOAD\s*$/i }).last(), B4, { group: g, title: 'Mobile drawer CTA', desc: 'The "DOWNLOAD" row inside the opened nav overlay at 390 wide; measured never followed.', sel: 'mobile nav overlay DOWNLOAD' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q(CTA).filter({ hasText: /^\s*GET STARTED\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "GET STARTED" pill at 390 wide; measured never followed.', sel: 'mobile hero GET STARTED' });
  save();
}

run = new Date().toISOString();
out._meta.read = run.slice(0, 10);
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every factory.com page ships data-theme="light" with scoped [data-dark-hero]/.invert-color-scheme dark sections and a dark footer; docs.factory.com measured light then switched to dark through its theme-selector-button control; auth.factory.ai sign-in paints dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, enterprise, pricing, contact, docs, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a');
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
