// Measures rive.app's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing downloads contact newsletter docs marketplace mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// rive.app marketing is a Framer site in one dark theme. Components are found
// by role, aria-label, or visible text. Nothing is sent or signed into.
// Newsletter SIGN UP, GET STARTED, login, Google, and SSO are never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', downloads: '/downloads', contact: '/contact',
  newsletter: '/newsletter', docs: '/docs/getting-started/introduction',
  marketplace: '/marketplace/', login: '/login/',
};
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && BASE + URLS[current] }, meta);
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
  footer: 'Footer', form: 'Forms', docs: 'Docs', mobile: 'Mobile (390 wide)',
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
  if (!(await newPage('home', { wait: 2500 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header, nav').first(), ['default'], { group: g, title: 'Header', desc: 'Fixed bar: logo, PRODUCTS, USE CASES, RESOURCES, PRICING, DOWNLOADS, DOCS, GET STARTED.', sel: 'header or first nav' }, { noScroll: true });
  await S('logo', q('a[href="/"]').first(), ['default'], { group: g, title: 'Logo', sel: 'a[href="/"]' }, { noScroll: true });
  const navBtn = (label) => q('button.rn-top, button').filter({ hasText: new RegExp('^' + label + '$') }).first();
  await S('nav-products', navBtn('PRODUCTS'), ['default', 'hover', 'focus-visible', 'pressed', 'opened'], { group: g, title: 'Products menu button', desc: 'Opens the products mega menu. Escape closes it after the opened shot.', sel: 'button.rn-top PRODUCTS' }, { noScroll: true });
  await page.keyboard.press('Escape');
  await S('nav-link', q('a[href="/pricing"]').first(), B4, { group: g, title: 'Nav link', desc: 'PRICING in the header. Measured, never followed from a submit.', sel: 'a[href="/pricing"]' }, { noScroll: true });
  await S('nav-cta', q('a[href="https://editor.rive.app"]').first(), B4, { group: g, title: 'Get started', desc: 'Header GET STARTED. Measured, never followed (editor host).', sel: 'a[href="https://editor.rive.app"]' }, { noScroll: true });
  await S('hero-title', q('h1').first(), ['default'], { group: G.home, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  await S('page-ground', q('body'), ['default'], { group: G.home, title: 'Page ground', desc: 'The black the marketing pages paint on.', sel: 'body' }, { noScroll: true, crop: false });
  await S('copy-button', q('button').filter({ hasText: /^COPY$/ }).first(), B4, { group: G.home, title: 'Copy button', desc: 'Copies a starter prompt. Does not submit a form.', sel: 'button COPY' }, { noScroll: true });
  await S('demo-segment', q('button[aria-label="Show Dashboard"]'), ['default', 'hover', 'pressed'], { group: G.home, title: 'Demo segment', desc: 'Hero demo switcher. Selecting a segment stays on the page.', sel: 'button[aria-label="Show Dashboard"]' }, { noScroll: true });
  const h2ok = await scrollFind(() => {
    const h = [...document.querySelectorAll('h2')].find((n) => (n.innerText || '').trim().length > 3 && n.getBoundingClientRect().height > 8);
    if (!h) return false;
    h.setAttribute('data-m-h2', '1');
    return true;
  });
  await S('section-title', h2ok ? q('[data-m-h2="1"]') : q('[data-m-h2="__none__"]'), ['default'], { group: G.home, title: 'Section title', sel: 'first visible h2' });
  save();
}


async function pricing() {
  if (!(await newPage('pricing', { wait: 2000 }))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  const monthly = q('p,div,button').filter({ hasText: /^MONTHLY$/ }).first();
  await S('billing-toggle', monthly, ['default', 'hover', 'pressed'], { group: g, title: 'Billing period', desc: 'YEARLY / MONTHLY labels. A click swaps prices in place. Not a form submit.', sel: 'text MONTHLY' });
  const cta = q('a,button').filter({ hasText: /^GET STARTED$/ }).nth(1);
  await S('plan-cta', cta, B4, { group: g, title: 'Plan CTA', desc: 'GET STARTED on a plan. Measured, never followed.', sel: 'GET STARTED' });
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('a,button,div,p')].find((n) => /^GET STARTED$/i.test((n.innerText || '').trim()) && n.getBoundingClientRect().y > 200);
    if (!el) return;
    let card = el;
    for (let n = el, i = 0; n && i < 8; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width >= 180 && r.width <= 520 && r.height >= 180) card = n;
      if (r.width > 700) break;
    }
    card.setAttribute('data-m-plan-card', '1');
  });
  await S('plan-card', q('[data-m-plan-card="1"]'), ['default'], { group: g, title: 'Plan card', sel: 'ancestor of GET STARTED' });
  save();
}

async function downloads() {
  if (!(await newPage('downloads', { wait: 1800 }))) return;
  await S('download-title', q('h1').first(), ['default'], { group: 'Downloads', title: 'Downloads title', sel: 'h1' }, { noScroll: true });
  const link = q('a').filter({ hasText: /mac|windows|linux|download/i }).first();
  await S('download-link', link, B4, { group: 'Downloads', title: 'Download link', desc: 'A platform download link. Measured, never followed.', sel: 'download anchor' });
  save();
}

async function forms() {
  if (!(await newPage('newsletter', { wait: 1500 }))) return;
  const field = q('input[type="email"]').first();
  await S('email-field', field, ['default', 'hover', 'focus-visible', 'focused'], { group: G.form, title: 'Newsletter email field', desc: 'Footer and newsletter email field. Nothing was typed into the committed captures that could be a real address, and the form was not submitted.', sel: 'input[type=email]' });
  await S('signup-button', q('button[type="submit"], button').filter({ hasText: /^SIGN UP$/ }).first(), ['default', 'hover', 'focus-visible'], { group: G.form, title: 'Sign up button', desc: 'Newsletter submit. Not pressed. Pressed state is omitted so the form cannot fire.', sel: 'button SIGN UP' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 2500 }))) return;
  await S('docs-title', q('h1').first(), ['default'], { group: G.docs, title: 'Docs title', sel: 'h1' }, { noScroll: true });
  await S('docs-search', q('input, button').filter({ hasText: /search/i }).first(), ['default'], { group: G.docs, title: 'Docs search', desc: 'Search control. Not submitted.', sel: 'search' }, { noScroll: true });
  await S('docs-nav', q('nav a, aside a').first(), B4, { group: G.docs, title: 'Docs nav link', sel: 'sidebar a' }, { noScroll: true });
  const theme = q('button').filter({ hasText: /theme/i }).first();
  await S('docs-theme', theme, ['default', 'hover', 'opened'], { group: G.docs, title: 'Theme preference', desc: 'Change theme preference. Opened to read the menu. A light theme was not applied as a capture theme.', sel: 'button theme' }, { noScroll: true });
  await page.keyboard.press('Escape');
  save();
}

async function marketplace() {
  if (!(await newPage('marketplace', { wait: 1800 }))) return;
  await S('market-search', q('input[type="text"], input[placeholder*="Search"]').first(), ['default', 'focused'], { group: 'Marketplace', title: 'Marketplace search', desc: 'Search field. Not submitted.', sel: 'search input' }, { noScroll: true });
  save();
}


async function footer() {
  if (!(await newPage('home', { wait: 2000 }))) return;
  const g = G.footer;
  const fl = q('footer a, a').filter({ hasText: /^Careers$/ }).first();
  await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'Careers link' });
  await S('footer-social', q('a[href*="github.com/rive-app"]').first(), B4, { group: g, title: 'Footer social', desc: 'GitHub icon link. Measured, never followed.', sel: 'a[href*=github.com/rive-app]' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 2000 }))) return;
  const g = G.mobile;
  const menuBtn = q('button[aria-label="Open menu"]');
  await S('m-header', q('a[href="/"]').first(), ['default'], { group: g, title: 'Mobile logo', sel: 'home link' }, { noScroll: true });
  if (await menuBtn.count()) {
    await S('m-menu-button', menuBtn, ['default', 'pressed'], { group: g, title: 'Mobile menu button', desc: 'aria-label Open menu. Opens the sheet.', sel: 'button[aria-label="Open menu"]' }, { noScroll: true });
    await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The sheet after its own toggle.', sel: 'Open menu' }, { noScroll: true, cropLoc: q('body') });
  }
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), marketing dark theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, downloads, forms, docs, marketplace, footer, mobile };
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
