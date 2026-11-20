// Measures clearful.com's public components in every state reachable without
// signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing library signin mobile (the footer group also runs on
// home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is built
// by build-measurements.mjs.
//
// clearful.com is a Webflow build in one LIGHT theme (white page, Manrope):
// stable Webflow classes (navbar1_, pricing27_, footer1_, w-tab-*) are
// selected directly. The /library route is a Tailwind stack in Mulish —
// a sibling surface measured on its own selectors. app.clearful.com is a
// FLUTTER WEB app: it paints the sign-in card on a canvas, so its controls
// are measured through Flutter's flt-semantics overlay (mounted only after
// the "Enable accessibility" toggle — a local, read-only switch) which
// exposes real bounding rects; canvas-painted styles are not readable via
// CSSOM and are documented as such. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the Webflow tab links and the
// mobile menu. Log In / Start-a-journal / Get-started / app-store links are
// measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', library: '/library', signin: 'https://app.clearful.com/#/sign-in' };
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    // The Flutter sign-in paints on a canvas: body.innerText stays empty even
    // on a good load, so an flt-glass-pane/flutter-view counts as rendered.
    if (document.querySelector('flt-glass-pane, flutter-view')) return false;
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  // The Flutter sign-in lays out on physical pixels: under a dsf-2 context it
  // halves the card, so that route is captured at dsf 1 where a desktop user
  // sees the same 400x56 buttons.
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && new URL(URLS[current], BASE).href }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
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
  library: 'Guided-journals library (Tailwind surface)',
  signin: 'App sign-in (Flutter boundary)',
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

// Clicks the nav "Resources"-style dropdown trigger (a local nav toggle;
// opens the link menu, never navigates). The triggers are BUTTONs sharing
// navigationLink's class, so the first one is marked for the menu read.
async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The 72px top bar: wordmark left, Guided-Journals link, Log In and the
  // blue Start-a-journal pill right. No dropdowns on this nav.
  await S('header', q('[class*="navbar1_component"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The 1440x72 top nav (Webflow w-nav): logo, Guided Journals link, Log In and the blue Start-a-journal pill.', sel: '.navbar1_component' }, { noScroll: true });
  await S('logo', q('a.navbar1_logo-link, img.navbar1_logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Clearful logo anchor (150x30).', sel: '.navbar1_logo-link' }, { noScroll: true });
  await S('nav-item', q('a.navbar1_link').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Guided Journals" nav link (16px/600 ink); links to /library, never followed.', sel: 'a.navbar1_link' }, { noScroll: true });
  await S('nav-signin', q('a').filter({ hasText: /^Log In$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The "Log In" nav action linking to app.clearful.com/#/sign-in; measured never followed.', sel: 'nav a: Log In' }, { noScroll: true });
  await S('nav-cta', q('a.button.is-small').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The 999px blue "Start a journal — it\'s free" pill in the nav (225x50, #1953ff); the anchor points at #, measured never pressed.', sel: 'a.button.is-small' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Be a more thoughtful, resilient, and happier you with daily journaling" — the 72px/700 Literatatt display headline.', sel: 'h1' }, { noScroll: true });
  await S('cta', q('a.button.is-large').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The 999px blue "Start journaling for free" pill under the hero (289x82, 20px/600); measured never pressed.', sel: 'a.button.is-large' }, { noScroll: true });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'The first 60px/700 section heading ("We\'re Clearful, the award-winning, modern jour…", navy #001452).', sel: 'first h2' });
  // The big feature cards (layout409) — white panels on the light ground.
  await S('feature-card', q('[class*="layout409_card"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature card', desc: 'A 1280x720 feature card (layout409): copy column + app screenshot.', sel: '.layout409_card' });
  // The cadence tabs (Weekly..Yearly) — a Webflow w-tabs widget; the current
  // tab carries w--current. Its links are local pane switches.
  await S('tab-link', q('a.timeline14_tab-link').filter({ visible: true }).first(), B4, { group: h, title: 'Cadence tab', desc: 'A cadence tab (Weekly/Monthly/Quarterly/Bi-Yearly/Yearly) in the timeline14 w-tabs widget; the held tab carries w--current, tabs switch panes locally.', sel: 'a.timeline14_tab-link' });
  // The brand-light band: the #d6e0ff section behind the big CTA.
  await S('section-accent', q('section[class*="background-color-brand-light"], [class*="background-color-brand-light"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Brand-light band', desc: 'The #d6e0ff brand-light section fill (background-color-brand-light) — the site\'s one tinted band.', sel: '.background-color-brand-light' });
  await S('app-badge', q('img[alt*="App Store"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Store badge', desc: 'The App Store badge artwork (153x80); the anchor links to apps.apple.com, never followed.', sel: 'img[alt*=App Store]' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element\'s painted fill — the white ground (html itself is transparent).', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1, h2').filter({ hasText: /pricing/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Pricing Plans" — the 60px/700 heading over the Free/Premium comparison table.', sel: 'h2 Pricing Plans' }, { noScroll: true });
  // The Monthly/Yearly w-tab-menu: held tab carries w--current.
  await S('billing-tab', q('a.pricing27_tab-link.w--current').filter({ visible: true }).first(), B4, { group: g, title: 'Billing tab', desc: 'The Monthly/Yearly billing tab (w-tab-menu, 108x40); the held period carries w--current. A local pane switch, measured never flipped.', sel: 'a.pricing27_tab-link.w--current' });
  await S('plan-column', q('[class*="pricing27_top-row-content"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan column', desc: 'A plan column top (347x247): price, cadence and the Get-started button.', sel: '.pricing27_top-row-content' });
  await S('plan-price', q('[class*="pricing27_top-row-price"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The "$0/mo"/"$9.99/mo" price line (56px/700).', sel: '.pricing27_top-row-price' });
  await S('plan-cta', q('a.is-pricing27-button').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The blue "Get started" pill under each price (347x58, #1953ff); never pressed.', sel: 'a.is-pricing27-button' });
  await S('feature-row', q('[class*="pricing27_row"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row', desc: 'A feature row in the Free/Premium comparison table (1280x56 on the #f7f7f7 alternate band).', sel: '.pricing27_row' });
  save();
}

async function library() {
  if (!(await newPage('library'))) return;
  const g = G.library;
  // /library is a Tailwind stack in Mulish — a sibling surface to the Webflow
  // marketing pages (gray-900 ink #111827, white cards on a light ground).
  await S('library-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library title', desc: '"Guided Journaling Library" — 60px/800 Mulish in Tailwind gray-900 (#111827); /library is a Tailwind sibling stack, not the Webflow marketing sheet.', sel: 'h1' }, { noScroll: true });
  await S('prompt-card', q('a.flex').filter({ hasText: /journal/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Journal card', desc: 'A guided-journal link card (white, 395x160, radius 16, Tailwind utilities); links into the library, never followed.', sel: 'a.flex h-40 card' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 20000, dsf: 1 }))) return;
  const g = G.signin;
  // app.clearful.com is a Flutter web app: the sign-in card paints on a
  // canvas, so the DOM carries no measurable controls until Flutter mounts
  // its semantics overlay — a documented assistive layer toggled locally by
  // the "Enable accessibility" placeholder (read-only; nothing is sent).
  await page.waitForTimeout(9000);
  await page.evaluate(() => document.querySelector('flt-semantics-placeholder') && document.querySelector('flt-semantics-placeholder').click()).catch(() => {});
  await page.waitForTimeout(2500);
  await S('signin-image', q('flt-semantics[role="img"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Welcome illustration', desc: 'The "Welcome Back Image" artwork on the sign-in card (264x176) — read through Flutter\'s flt-semantics overlay; the card paints on canvas so only geometry/roles are DOM-readable.', sel: 'flt-semantics[role=img]' }, { noScroll: true });
  await S('signin-button', q('flt-semantics[role="button"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in button', desc: 'A "Continue with email/Apple/Google" button on the sign-in card (400x56); canvas-painted, measured via the semantics overlay — never pressed.', sel: 'flt-semantics[role=button]' }, { noScroll: true });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document
  // that is actually open.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, [role="contentinfo"], .footer1_component');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The #f7f7f7 footer band (1440x535): resource links, store badges, social icons and the legal subfooter.', sel: 'footer.footer1_component' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a.footer1_link').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a.footer1_link' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] a[href*="instagram" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon link (Instagram).', sel: 'footer a[href*=instagram]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the Webflow nav collapses to the bar plus a w-nav-button
  // hamburger; the menu opens on the button's own press.
  await S('m-header', q('[class*="navbar1_component"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390x64 mobile nav bar: logo + hamburger.', sel: '.navbar1_component at 390' }, { noScroll: true });
  await S('m-menu-button', q('[class*="navbar1_menu-button"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The 40x48 hamburger (w-nav-button, the menu-icon1 lines); its own press opens the nav menu.', sel: '.navbar1_menu-button' }, { noScroll: true });
  const menuBtn = q('[class*="navbar1_menu-button"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.evaluate((el) => el.click()); await page.waitForTimeout(1200); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  await S('m-menu-open', q('nav.w-nav-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The nav menu after the hamburger press (Webflow w-nav-menu).', sel: 'nav.w-nav-menu after toggle press' }, { noScroll: true });
  await S('m-menu-link', q('nav.w-nav-menu a').filter({ visible: true, hasText: /\w{3,}/ }).first(), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open mobile menu.', sel: 'first link inside the open w-nav-menu' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (library is a Tailwind sibling surface; sign-in is a Flutter canvas)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, library, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
