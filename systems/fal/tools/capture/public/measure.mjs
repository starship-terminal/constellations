// Measures fal.ai's public components in every state reachable without
// signing in, creating an API key, running inference or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing explore model api login docs mobile (and `motion`, the
// reduced-motion check alone).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fal.ai paints three surfaces signed out: the Webflow marketing pages (the
// bright single-theme Focal Web brand on /, /pricing, /serverless,
// /contact-sales), the Next.js app (/explore, /models/*, /login — Public
// Sans Rounded on a semantic --surface-*/--content-* token layer, themed by
// the context's prefers-color-scheme; the app pages are measured in their
// authored dark presentation) and the fumadocs docs (/docs/*, Public Sans +
// Focal headings). The login card at /login is OAuth-only signed out and is
// measured at rest — its Continue-with-* buttons are never followed, there
// are no credential fields. The only presses are local UI toggles: the
// Products menu trigger, the docs theme switcher, the model page's
// Preview/JSON result toggle and the mobile nav; "Sign in to run", "Open in
// Sandbox", "Try free", "Download", every OAuth button and every Copy
// button are measured, never activated. The .dg-consent-banner cookie card
// is hidden by closePromo(), never answered.

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
  home: '/', pricing: '/pricing', explore: '/explore',
  model: '/models/krea/v3/text-to-image', api: '/models/krea/v3/text-to-image/api',
  login: '/login', docs: '/docs/documentation', mobile: '/explore',
};
// The pages each surface is measured under: app pages paint `dark`, the
// marketing and docs pages `light`.
const SCHEME = { home: 'light', pricing: 'light', explore: 'dark', model: 'dark', api: 'dark', login: 'dark', docs: 'light', mobile: 'dark' };
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
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: SCHEME[key] }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: SCHEME[key] });
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

// Playwright's `visible` engine passes elements that sit inside a
// display:none ancestor (the docs and app pages both ship hidden
// desktop/mobile twins), so visibility alone is not enough — the first
// match with a non-empty box is the real twin.
async function firstBoxed(target, max = 80) {
  const n = Math.min(await target.count().catch(() => 0), max);
  for (let i = 0; i < n; i++) {
    const t = target.nth(i);
    const b = await t.boundingBox().catch(() => null);
    if (b && b.width > 0.5 && b.height > 0.5) return t;
  }
  return null;
}

async function measure(key, state, target, opts = {}) {
  const loc = (await firstBoxed(target.filter({ visible: true }))) || target.first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
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
  const loc = await firstBoxed(target.filter({ visible: true }));
  if (!loc || !(await loc.count())) {
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
        // Focus before clicking: overlay anchors (a.focus-ring inset-0 chips)
        // cover the field and swallow the click.
        await fld.evaluate((el) => el.focus()).catch(() => {});
        if (!(await fld.evaluate((el) => document.activeElement === el).catch(() => false))) {
          await fld.click({ timeout: 4000 }).catch(() => {});
        }
        await page.waitForTimeout(400);
        via = 'focused the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.evaluate((el) => el.focus()).catch(() => {});
        if (!(await f.evaluate((el) => document.activeElement === el).catch(() => false))) {
          await f.click({ timeout: 4000 });
        }
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
const NEVER = /^(send|submit|sign in|log ?in|login|sign up|signup|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|use sso|sign in to run|try free|try it now!?|open in sandbox|contact sales|contact support|claim this offer|try again)$/i;
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

// Whether the page changes its motion under prefers-reduced-motion: each probe
// is read in fresh contexts with `no-preference` and `reduce`. A probe only
// counts as evidence when its baseline really moves (a transition duration
// above 0s, or a running animation): an idle control proves nothing, so the
// result records `baselineMoves` and the run logs when a probe is idle.
// Probes: the pixel-decoration cells carry the app's one running animation
// (pixel-scan-sweep), and the header's Products trigger carries the 0.15s
// colour transition the controls share.
const MOTION_PROBES = [
  { label: 'pixel-decoration-cell (animation)', sel: 'path.pixel-decoration-cell' },
  { label: 'header Products trigger (transition)', sel: 'header button', text: /^\s*products\s*$/i },
];
async function reducedMotion(key) {
  out._meta.reducedMotion ??= {};
  const reads = {};
  try {
    const b = context.browser();
    for (const mode of ['no-preference', 'reduce']) {
      const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: mode, colorScheme: SCHEME[key] });
      await patch(ctx);
      const p = await ctx.newPage();
      await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(7000);
      await closePromo(p);
      reads[mode] = await p.evaluate((probes) => probes.map(({ sel, text }) => {
        const re = text ? new RegExp(text.source, text.flags) : null;
        const el = [...document.querySelectorAll(sel)].find((e) => !re || re.test((e.innerText || '').trim()));
        if (!el) return null;
        const cs = getComputedStyle(el);
        return { transition: cs.transition, animation: cs.animation, animationName: cs.animationName, transitionDuration: cs.transitionDuration, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
      }), MOTION_PROBES.map((m) => ({ sel: m.sel, text: m.text && { source: m.text.source, flags: m.text.flags } }))).catch(() => null);
      await ctx.close();
    }
    const moves = (r) => !!r && (r.animationName !== 'none' || r.transitionDuration.split(',').some((d) => parseFloat(d) > 0));
    out._meta.reducedMotion[key] = {
      note: 'Each probe is read with prefers-reduced-motion no-preference and reduce in fresh contexts; baselineMoves says whether the no-preference reading actually animates or transitions.',
      probes: MOTION_PROBES.map((m, i) => {
        const np = reads['no-preference']?.[i] ?? null, rd = reads.reduce?.[i] ?? null;
        const baselineMoves = moves(np);
        if (!baselineMoves) log(`reduced-motion probe "${m.label}" is idle under no-preference: not evidence`);
        return { label: m.label, selector: m.sel, baselineMoves, noPreference: np, reduce: rd, changedUnderReduce: !!np && !!rd && (np.animationName !== rd.animationName || np.transitionDuration !== rd.transitionDuration) };
      }),
    };
  } catch (e) { out._meta.reducedMotion[key] = { error: String(e).slice(0, 120) }; }
}

const FIELD = ['default', 'focused', 'filled'];

const G = {
  shell: 'App shell and navigation', home: 'Home (marketing)',
  pricing: 'Pricing (marketing)', catalog: 'Explore catalog (app, dark)',
  modelpg: 'Model page (app, dark)', apipg: 'API tab (app, dark)',
  login: 'Login (app, dark)', docs: 'Documentation (docs, light)',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the header's Products dropdown on the app surface: a local disclosure
// trigger (a button, not a link). Waits for product links to appear.
async function openNavMenu() {
  const ok = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('a.text-content-subtle, a[class*="menu-item" i], a[class*="dropdown" i]')].some((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).visibility !== 'hidden' && /explore|inference|serverless|compute/i.test(e.getAttribute('href') || ''); }),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await ok(300)) return 'the Products menu was already open';
  const b = page.locator('header button, header [role="button"]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
  if (!(await b.count())) return 'no Products nav trigger';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok(4000)) return 'clicked "Products" to open the menu';
    await page.waitForTimeout(600);
  }
  return 'clicked "Products"; the menu did not report open';
}

// Opens the phone nav overlay: the "Open navigation" icon button is a local
// disclosure trigger; Escape closes the overlay afterwards.
async function openMobileNav() {
  const ok = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('[class*="vaul-drawer-direction" i] a[role="menuitem"], [role="dialog"] a[role="menuitem"]')].filter((e) => e.getBoundingClientRect().width > 40).length >= 3,
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  const b = page.locator('button[aria-label*="navigation" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no mobile menu trigger';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok(4000)) return 'clicked "Open navigation" to open the phone nav';
    await page.waitForTimeout(600);
  }
  return 'clicked the hamburger; the nav did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The marketing shell is a Webflow build: the fixed bar is the element
  // carrying data-home-nav-palette (z-index 999), the links are
  // .nav-list-item anchors, the CTAs a.button inside .nav-right, the
  // dropdowns .w-dropdown toggles and the footer a section.is-footer.
  await S('mkt-header', q('div.nav-main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header', desc: 'The fixed top bar (div.nav-main, z-index 999): fal wordmark, Products / Docs / Pricing / Enterprise / Resources menus, Contact Sales and Get Started.', sel: 'div.nav-main' }, { noScroll: true });
  await S('mkt-logo', q('a.nav-logo-holder').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The fal wordmark link (a.nav-logo-holder).', sel: 'a.nav-logo-holder' }, { noScroll: true });
  await S('mkt-nav-products', q('.w-dropdown-toggle, [class*="dropdown-toggle" i]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Products menu trigger', desc: 'The Products dropdown trigger in the marketing nav — a Webflow w-dropdown disclosure; measured, its links never followed.', sel: '.w-dropdown-toggle Products' }, { noScroll: true, allowLink: true });
  await S('mkt-nav-pricing', q('a.nav-list-item').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Pricing link (marketing)', desc: 'The marketing nav Pricing link; measured, never followed.', sel: 'a.nav-list-item Pricing' }, { noScroll: true });
  await S('mkt-btn-sales', q('.nav-right:not(.is-mobile) a.button').filter({ hasText: /contact sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact Sales button (marketing)', desc: 'The secondary Contact-Sales button in the marketing header; measured, never followed.', sel: '.nav-right Contact Sales' }, { noScroll: true });
  await S('mkt-btn-start', q('.nav-right:not(.is-mobile) a.button').filter({ hasText: /get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Get Started button (marketing)', desc: 'The primary Get-Started button in the marketing header; measured, never followed.', sel: '.nav-right Get Started' }, { noScroll: true });
  const h = G.home;
  await S('mkt-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The home hero display heading — Focal Web 96px, the cyan brand colour on the dark bronze field.', sel: 'h1' }, { noScroll: true });
  // The field the hero headline sits on is the h1's section (section.background-color-darkbronze), not the h1's own transparent paint.
  await S('mkt-hero-field', q('h1').filter({ visible: true }).first().locator('xpath=ancestor::section[1]'), ['default'], { group: h, title: 'Hero field', desc: 'The home hero section: the dark bronze field (background-color-darkbronze) behind the cyan display headline.', sel: 'section ancestor of the hero h1' }, { noScroll: true });
  await S('mkt-hero-cta', q('main a, main button, section a, section button').filter({ hasText: /get started|contact sales|start building|try/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The primary call-to-action inside the hero; measured never followed.', sel: 'hero primary CTA' });
  await S('mkt-section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading (marketing)', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  const f = G.footer;
  await S('mkt-footer', q('section.is-footer, [class*="is-footer" i]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Marketing footer', desc: 'The marketing page footer (section.is-footer): link columns, socials, legal.', sel: 'section.is-footer' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pr-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The pricing page display heading.', sel: 'h1' }, { noScroll: true });
  // fal's pricing page is usage-based: GPU compute and model APIs priced in
  // div.pricing-row-table blocks. There is no billing-period toggle and no
  // plan cards — those components were probed for and honestly absent.
  await S('pr-price-table', q('.pricing-row-table, [class*="pricing-row-table" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing table', desc: 'A div.pricing-row-table block under the "Serverless & Compute Pricing" heading — fal prices GPU compute and model APIs per usage; there is no plan card or billing toggle.', sel: '.pricing-row-table' });
  await S('pr-price-row', q('.pricing-table-row, [class*="pricing-table-row" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Pricing row', desc: 'A .pricing-table-row line inside a compute/model pricing table.', sel: '.pricing-table-row' });
  await S('pr-plan-cta', q('a, button').filter({ hasText: /get started|contact sales|start free|sign up/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Plan CTA', desc: 'A call-to-action inside a plan column; measured never followed.', sel: 'plan CTA' });
  save();
}

async function explore() {
  if (!(await newPage('explore'))) return;
  await sheetsFor('explore');
  await chrome('explore');
  const g = G.shell;
  await S('app-header', q('header.dashboard-navigation-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'App header', desc: 'The app navigation header (header.dashboard-navigation-header): fal mark, Products / Documentation / Pricing / Enterprise / Resources menus, Contact Sales, Log-in, Sign-up.', sel: 'header.dashboard-navigation-header' }, { noScroll: true });
  await S('app-announce', q('button[aria-label="Dismiss announcement"]').filter({ visible: true }).first().locator('xpath=ancestor::div[2]'), ['default'], { group: g, title: 'Announcement banner', desc: 'The dismissible announcement strip above the header; the Dismiss button is measured, never pressed.', sel: 'announcement strip' }, { noScroll: true });
  await S('app-announce-x', q('button[aria-label="Dismiss announcement"]').filter({ visible: true }).first(), B4, { group: g, title: 'Dismiss-announcement button', desc: 'The X that closes the announcement strip — a local dismiss; measured, never pressed.', sel: 'button[aria-label="Dismiss announcement"]' }, { noScroll: true });
  await S('app-nav-products', q('header button, header [role="button"]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Products menu trigger (app)', desc: 'The Products dropdown trigger in the app header — a local disclosure; the opened state was measured after clicking it, its links never followed.', sel: 'header Products' }, { noScroll: true, allowLink: true });
  // The Products menu opens a wide panel — it portals out of the header, so
  // scope the menu links to the document, not the bar: product entries
  // painted text-content-subtle at ~308x65 plus a search chip row.
  await S('app-nav-menu', q('a.text-content-subtle[href="/serverless"], a.text-content-subtle[href*="/compute"], a.text-content-subtle[href*="/inference"]').filter({ visible: true }).first().locator('xpath=ancestor::div[1]'), ['default'], { group: g, title: 'Products menu', desc: 'The dropdown opened by the Products trigger (div.top-center ~322x201, holding ul.p-1.5 product links); its links were never followed.', sel: 'products dropdown' }, { open: openNavMenu, noScroll: true, noReset: true });
  await S('app-nav-menu-item', q('a.text-content-subtle[href="/serverless"], a.text-content-subtle[href*="/compute"], a.text-content-subtle[href*="/inference"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Products menu item', desc: 'A product entry inside the opened dropdown (a.text-content-subtle); measured, never followed.', sel: 'products menu link' }, { open: openNavMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('app-nav-docs', q('header a').filter({ hasText: /^\s*Documentation\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Documentation link (app)', desc: 'The app header Documentation link; measured, never followed.', sel: 'header Documentation' }, { noScroll: true });
  await S('app-btn-login', q('header a, header button').filter({ hasText: /^\s*Log-?in\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Log-in button (app)', desc: 'The Log-in button in the app header; measured, never followed.', sel: 'header Log-in' }, { noScroll: true });
  await S('app-btn-signup', q('header a, header button').filter({ hasText: /^\s*Sign-?up\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Sign-up button (app)', desc: 'The primary Sign-up button in the app header; measured, never followed.', sel: 'header Sign-up' }, { noScroll: true });
  const c = G.catalog;
  await S('search-models', q('input[aria-label="Search models"]').filter({ visible: true }).first(), FIELD, { group: c, title: 'Model search field', desc: 'The "Search models" input over the catalog; focused and typed into then cleared — the catalog only filters locally.', sel: 'input[aria-label="Search models"]' }, { noScroll: true, fillText: 'flux' });
  // The grid tiles are a.page-model-card anchors (~360x350): artwork, a
  // "new" ribbon, the endpoint id, a description. The h1/h2 headings higher
  // on the page are hero-carousel slide titles, not cards.
  await S('model-card', q('a.page-model-card').filter({ visible: true }).first(), ['default', 'hover'], { group: c, title: 'Model card', desc: 'A model tile in the explore grid (a.page-model-card): artwork, endpoint id, publisher and description; measured, never followed.', sel: 'a.page-model-card' });
  // Cards carry no heading elements: the endpoint id is a .truncate text
  // line inside the tile.
  await S('model-card-title', q('a.page-model-card span.truncate, a.page-model-card .truncate').filter({ visible: true }).first(), ['default'], { group: c, title: 'Model card endpoint line', desc: 'The endpoint-id text line inside a card (e.g. blackforestlabs/flux-3-max/text-to-video) — a span.truncate, cards carry no heading elements.', sel: 'a.page-model-card .truncate' });
  await S('card-cta', q('a').filter({ hasText: /^\s*try it now!?\s*$/i }).filter({ visible: true }).first(), B4, { group: c, title: 'Card CTA', desc: 'The "Try it now!" pill on a hero-carousel slide; measured, never followed.', sel: 'Try it now' });
  await S('card-docs-link', q('a').filter({ hasText: /^\s*see docs\s*$/i }).filter({ visible: true }).first(), B4, { group: c, title: 'Card docs link', desc: 'The "See docs" pill on a hero-carousel slide; measured, never followed.', sel: 'See docs' });
  await S('carousel-dot', q('button[aria-label^="Go to slide"]').filter({ visible: true }).first(), B4, { group: c, title: 'Carousel dot', desc: 'A "Go to slide N" dot in the hero carousel — a local pager; measured, never clicked.', sel: 'button[aria-label^="Go to slide"]' }, { noScroll: true });
  // Catalog sections scroll with "Next page" arrow buttons and number-dot
  // pagers ("Go to page N"); each section ships hidden twins, which the box
  // check skips.
  await S('pager-next', q('button[aria-label="Next page"]').filter({ visible: true }), B4, { group: c, title: 'Section pager arrow', desc: 'A "Next page" arrow button scrolling a catalog section (~48x96); a local scroller — measured, never clicked.', sel: 'button[aria-label="Next page"]' });
  await S('pager-dot', q('button[aria-label^="Go to page"]').filter({ visible: true }), B4, { group: c, title: 'Section pager dot', desc: 'A "Go to page N" dot paging a catalog section — a local pager; measured, never clicked.', sel: 'button[aria-label^="Go to page"]' });
  save();
}

async function model() {
  if (!(await newPage('model', { wait: 10000 }))) return;
  await sheetsFor('model');
  await chrome('model');
  const g = G.modelpg;
  await S('mp-back', q('a[href="/models"], a[href="/explore"]').filter({ visible: true }).first(), B4, { group: g, title: 'Back to Gallery link', desc: 'The breadcrumb-style link back to the catalog; measured, never followed.', sel: 'Back to Gallery' }, { noScroll: true });
  await S('mp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Model heading', desc: '"krea/v3/text-to-image" — the model endpoint heading.', sel: 'h1' }, { noScroll: true });
  await S('mp-badge', q('[class*="badge" i]').filter({ hasText: /inference|commercial use|idle/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Model badge', desc: 'A .badge-role-* pill under the heading (Inference / Commercial use / Idle).', sel: '.badge-role-*' }, { noScroll: true });
  await S('mp-tab', q('[role="tab"], a[href*="/models/krea/v3/text-to-image"]').filter({ hasText: /^\s*(Playground|API|Examples)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Model page tab', desc: 'A Playground/API/Examples tab on the model page — an in-page tab link; measured, the active tab was not switched for state capture.', sel: 'model tab' }, { noScroll: true });
  await S('mp-endpoint-btn', q('button[aria-label="Model endpoint"]').filter({ visible: true }).first(), B4, { group: g, title: 'Model endpoint button', desc: 'The endpoint-id chip button; measured, never activated.', sel: 'button[aria-label="Model endpoint"]' }, { noScroll: true });
  await S('mp-copy', q('button[aria-label="Copy"]').filter({ visible: true }).first(), B4, { group: g, title: 'Copy button', desc: 'A clipboard Copy icon button (endpoint / code); measured, never pressed.', sel: 'button[aria-label="Copy"]' }, { noScroll: true });
  await S('mp-agent-btn', q('button').filter({ hasText: /onboard your agent/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Onboard-your-agent button', desc: 'The "Onboard your agent" button that copies a setup prompt; measured, never pressed.', sel: 'Onboard your agent' }, { noScroll: true });
  // "Sandbox Open in Sandbox" renders twice; the first copy is hidden and
  // reads "SandboxOpen in Sandbox", so an exact text match picks the real one.
  await S('mp-sandbox-link', q('a[href*="/sandbox"]').filter({ hasText: /open in sandbox/i }).filter({ visible: true }), B4, { group: g, title: 'Open in Sandbox link', desc: 'The Open-in-Sandbox link on the model page (a 120x32 pill, text "SandboxOpen in Sandbox" — a hidden twin ships beside it); measured, never followed.', sel: 'a[href*="/sandbox"] "Open in Sandbox"' }, { noScroll: true });
  await S('mp-prompt', q('textarea[placeholder*="prompt" i], textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Prompt textarea', desc: 'The playground prompt field ("Write your prompt here..."); focused and typed into then cleared — inference was never run.', sel: 'playground textarea' }, { fillText: 'a lighthouse on a cliff at dusk' });
  await S('mp-param', q('button').filter({ hasText: /^\s*(Square HD|1K|2K)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Parameter option', desc: 'A playground parameter option pill (an aspect/size choice) — a local option button; measured, never toggled.', sel: 'param option pill' });
  await S('mp-param-more', q('button').filter({ hasText: /^\s*More\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'More-params button', desc: 'The "More" disclosure for extra playground parameters — a local disclosure; measured, never opened.', sel: 'More' });
  await S('mp-run', q('a, button').filter({ hasText: /^\s*sign in to run\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in-to-run button', desc: 'The playground run button — it links to login signed out; measured, never activated.', sel: 'Sign in to run' });
  await S('mp-result-tab', q('button').filter({ hasText: /^\s*(Preview|JSON)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Result view toggle', desc: 'The Preview/JSON toggle on the Result pane — a local view switch; measured, never switched.', sel: 'Preview/JSON toggle' });
  await S('mp-download', q('button').filter({ hasText: /^\s*Download\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Download button', desc: 'The result Download button — a licensed download; measured, never pressed.', sel: 'Download' });
  const f = G.footer;
  await S('app-footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'App footer', desc: 'The app page footer: product/learn/social columns, legal and privacy links.', sel: 'footer' });
  save();
}

async function api() {
  if (!(await newPage('api', { wait: 10000 }))) return;
  await sheetsFor('api');
  await chrome('api');
  const g = G.apipg;
  await S('api-tab', q('a[href$="/models/krea/v3/text-to-image/api"]').filter({ hasText: /^\s*API\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'API tab (active)', desc: 'The "API" tab of the model page tab bar, active (aria-selected true); measured, never switched.', sel: 'a[href$="/api"] "API"' }, { noScroll: true });
  await S('api-code', q('pre, code, [class*="code" i]').filter({ hasText: /import|fal_client|subscribe|endpoint_id|queue/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'API code block', desc: 'A code sample on the API tab (client subscribe / queue call).', sel: 'code block' });
  // The code block's own Copy button: the first sample <pre> and the absolutely
  // positioned button inside its `group relative` wrapper (the endpoint-id Copy
  // measured as mp-copy sits in the page header, outside every code block).
  const codeWrap = q('pre').filter({ hasText: /import|fal_client|subscribe|endpoint_id|queue/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"group") and contains(@class,"relative")][1]');
  await S('api-copy', codeWrap.locator('button[aria-label="Copy"]').first(), B4, { group: g, title: 'Copy button (API)', desc: 'The code-block Copy button (top-right of the first code sample); measured, never pressed.', sel: 'code block button[aria-label="Copy"]' });
  await S('api-lang-tab', q('button').filter({ hasText: /javascript \/ node|python|curl/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Language tab', desc: 'A client-language tab on the API samples ("JavaScript / Node.js") — a local view switch; measured, never switched.', sel: 'language tab' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('li-card', q('h1').filter({ hasText: /welcome to fal/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[3]'), ['default'], { group: g, title: 'Login card', desc: 'The OAuth-only login/signup card: fal mark, "Login or sign up", the Continue-with-* buttons and Use SSO; measured at rest, nothing followed.', sel: 'login card (h1 ancestor)' }, { noScroll: true });
  await S('li-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login heading', desc: '"Welcome to fal" over the card.', sel: 'h1' }, { noScroll: true });
  await S('li-oauth-github', q('button, a').filter({ hasText: /continue with github/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue-with-GitHub button', desc: 'A Continue-with-* OAuth button; measured, never followed (it starts the OAuth flow).', sel: 'Continue with GitHub' }, { noScroll: true });
  await S('li-oauth-google', q('button, a').filter({ hasText: /continue with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue-with-Google button', desc: 'The Continue-with-Google OAuth button; measured, never followed.', sel: 'Continue with Google' }, { noScroll: true });
  await S('li-sso', q('button, a').filter({ hasText: /use sso/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Use SSO button', desc: 'The Use-SSO button; measured, never followed.', sel: 'Use SSO' }, { noScroll: true });
  await S('li-support', q('a').filter({ hasText: /contact support/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact-support link', desc: 'The Contact-support link under the card; measured, never followed.', sel: 'Contact support' }, { noScroll: true });
  save();
}

async function docs() {
  if (!(await newPage('docs'))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  // The docs shell is fumadocs: the tab strip is .nav-tabs of a.nav-tabs-item
  // links, the sidebar a fixed nav, the search trigger a
  // button[class*="group/search"], the theme control a three-way
  // "Switch to * theme" button set, code samples .code-group divs. Several
  // elements ship hidden mobile/desktop twins, so every spec picks the first
  // visible match.
  await S('docs-topbar', q('.nav-tabs').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs top bar', desc: 'The docs tab strip (.nav-tabs): Documentation / Examples / Model API Reference / SDK Reference / Inference API / Platform API / Changelog.', sel: '.nav-tabs' }, { noScroll: true });
  await S('docs-tab-item', q('a.nav-tabs-item').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Docs tab item', desc: 'A tab inside the docs tab strip; measured, never followed.', sel: 'a.nav-tabs-item' }, { noScroll: true });
  await S('docs-search', q('button[class*="group/search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Docs search trigger', desc: 'The "Search… Ctrl K" command trigger at the top of the sidebar — a local overlay trigger; measured, never opened.', sel: 'button.group/search' }, { noScroll: true });
  await S('docs-hero-search', q('.fal-hero-search').filter({ visible: true }).first(), B4, { group: g, title: 'Docs hero search', desc: 'The "Search or ask…" field in the docs hero — a local overlay trigger; measured, never opened.', sel: '.fal-hero-search' });
  await S('docs-theme-btn', q('button[aria-label="Switch to system theme"], button[aria-label="Switch to light theme"], button[aria-label="Switch to dark theme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme switcher', desc: 'One segment of the light/system/dark theme control — a local display toggle; measured, never cycled (the page was captured at its light default).', sel: 'button[aria-label*="theme"]' }, { noScroll: true });
  await S('docs-nav-section', q('nav a.group, [class*="sidebar" i] a.group').filter({ hasText: /^\s*(Overview|Quick Start|Why fal\?)\s*$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Docs nav item', desc: 'A sidebar navigation item on the docs tree (a.group); measured, never followed.', sel: 'docs sidebar link' }, { noScroll: true });
  await S('docs-sidebar', q('nav[class*="sidebar" i], nav.fixed').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar', desc: 'The fixed docs sidebar: search, Status/Community/Blog and the grouped nav tree.', sel: 'docs sidebar' }, { noScroll: true });
  // The hero title is h1.fal-hero-title; the page also carries a display:none
  // "Documentation" h1 twin, which the box check skips.
  await S('docs-h1', q('h1.fal-hero-title, .fal-hero-title, .mdx-content h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs heading', desc: '"Build with fal" — the docs hero heading (Focal, h1.fal-hero-title).', sel: 'h1.fal-hero-title' });
  await S('docs-prose', q('p.fal-hero-body, p.fal-hero-subtitle, .mdx-content p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs body text', desc: 'A hero/body paragraph in the docs prose (Public Sans, p.fal-hero-body).', sel: 'p.fal-hero-body' });
  // Section cards are div.card blocks; the anchor inside is display:contents.
  await S('docs-card', q('.columns .card, div.card, [class*="columns" i] [class*="card" i]').filter({ hasText: /model apis|serverless|compute/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Docs section card', desc: 'A section card in the docs .columns grid (Model APIs / Serverless / Compute); measured, its link never followed.', sel: '.columns .card' });
  await S('docs-toc', q('[class*="toc" i], nav').filter({ hasText: /on this page/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'On-this-page TOC', desc: 'The right-hand "On this page" table of contents.', sel: 'docs toc' }, { noScroll: true });
  await S('docs-code', q('.code-group').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs code block', desc: 'A .code-group sample block in the docs (Python/JavaScript/cURL tabs).', sel: '.code-group' });
  await S('docs-code-copy', q('button[aria-label="Copy the contents from the code block"]').filter({ visible: true }).first(), B4, { group: g, title: 'Docs code-copy button', desc: 'The Copy button on a docs code block; measured, never pressed.', sel: 'button[aria-label="Copy the contents from the code block"]' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/explore' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header.dashboard-navigation-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar (header.dashboard-navigation-header): fal mark and the "Open navigation" trigger.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('button[aria-label*="navigation" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-hamburger', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu trigger', desc: 'The "Open navigation" icon button — a local disclosure; the opened state was measured after clicking it.', sel: 'button[aria-label*=navigation]' }, { noScroll: true, allowLink: true });
  // The opened nav is a vaul bottom sheet of a[role="menuitem"] rows; the
  // desktop header ships hidden menuitem twins the box check skips.
  await S('m-nav-item', q('[class*="vaul-drawer-direction" i] a[role="menuitem"], [role="dialog"] a[role="menuitem"], a[role="menuitem"]').filter({ hasText: /^\s*(Pricing|Documentation|Enterprise|Model APIs|Blog)\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav link', desc: 'A menuitem row inside the opened vaul bottom-sheet nav; measured, never followed.', sel: 'mobile nav menuitem' }, { open: openMobileNav, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-search', q('input[aria-label="Search models"], input[placeholder*="search" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile search field', desc: 'The model search field at phone width.', sel: 'mobile search' });
  await S('m-model-card', q('a.page-model-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile model card', desc: 'A model tile (a.page-model-card) in the phone catalog grid.', sel: 'mobile model card' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing and docs pages paint their light themes, the app pages (explore, model, api, login, mobile) paint dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, explore, model, api, login, docs, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on elements that really move (see MOTION_PROBES).
  if (!pages.length || pages.includes('explore') || pages.includes('motion')) await reducedMotion('explore');
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
