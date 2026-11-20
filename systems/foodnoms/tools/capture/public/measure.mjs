// Measures foodnoms.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home plus help news press family-plan vs-mfp help-article
// help-mcp news-article terms open-signup dark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// foodnoms.com is a Framer-published marketing site: the product is an iOS app
// sold through the App Store, so there is no web sign-in anywhere. The site
// paints light and a real (prefers-color-scheme: dark) theme — the `dark`
// page emulates the scheme in the browser context, which is the same code
// path a visitor's dark OS takes (authored dark media rules, not a
// reconstruction). Components carry stable data-framer-name labels, so specs
// select by those names, role, aria-label or text. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the help "Search"
// trigger and the "About Foodnoms" accordion header, and the mobile "Open
// navigation menu" button. The newsletter field is focused and typed into
// then cleared, never submitted; every Download/App-Store and mailto link is
// measured, never followed.
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
  home: '/', plus: '/plus', help: '/help', news: '/news', press: '/press',
  'family-plan': '/family-plan', 'vs-mfp': '/vs/myfitnesspal',
  'help-article': '/help/barcode-scanning', 'help-mcp': '/help/mcp',
  'news-article': '/news/foodnoms-2',
  terms: '/terms', 'open-signup': '/open/settings/sign-up',
  dark: '/', mobile: '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge or a failure gated this run: components last measured on
// them keep their earlier readings instead of being pruned below (a blocked
// pass must never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, colorScheme = 'light' } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', colorScheme === 'dark' ? '(dark)' : '');
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|book|start for free|book a demo)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
  shell: 'App shell and navigation', home: 'Home', plus: 'Pricing (Foodnoms+)',
  help: 'Help center', news: 'News', press: 'Press', article: 'Article pages',
  legal: 'Legal', open: 'Open-in-app interstitial',
  dark: 'Dark theme (emulated prefers-color-scheme)',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the help-center Framer search modal: the "Search" control mounts
// __framer-search-modal-container with the real input. A local UI toggle;
// nothing typed into it is submitted.
async function openSearch() {
  const ok = () => page.locator('.__framer-search-modal-container input, input[placeholder="Search..."]').filter({ visible: true }).count().then((n) => n > 0);
  if (await ok()) return 'the Framer search modal was already open';
  const t = page.locator('[data-framer-name="Variant 1"]').filter({ hasText: /^\s*Search\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return 'no search trigger';
  for (let i = 0; i < 3; i++) {
    await t.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
    await page.waitForTimeout(400);
    const bb = await t.boundingBox();
    if (bb) await page.mouse.click(bb.x + bb.width / 2, bb.y + bb.height / 2);
    if (await ok()) return 'clicked "Search" to open the Framer search modal';
    await page.waitForTimeout(700);
  }
  return 'clicked "Search"; the modal did not report open';
}

// Opens the first help accordion: the [data-framer-name="Header"] row inside a
// "Closed" section toggles the Framer component to its "Open" variant. A local
// UI toggle; idempotent — skips when a section is already open.
async function openFirstAccordion() {
  const already = await page.locator('[data-framer-name="Open"]').filter({ visible: true }).count();
  if (already) return 'an accordion section was already open';
  const h = page.locator('[data-framer-name="Closed"] [data-framer-name="Header"]').filter({ visible: true }).first();
  if (!(await h.count())) return 'no accordion header';
  await h.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
  await page.waitForTimeout(400);
  await h.click({ timeout: 4000 }).catch(() => h.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  const ok = await page.locator('[data-framer-name="Open"]').filter({ visible: true }).count();
  return ok ? 'clicked the "About Foodnoms" accordion header (Closed -> Open)' : 'clicked the accordion header; it did not report open';
}

// Opens the phone nav overlay: the "Open navigation menu" button. A local UI
// toggle; its links are never followed.
async function openMobileMenu() {
  const ok = () => page.waitForFunction(() => {
    const links = [...document.querySelectorAll('a')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.height > 20 && /^(News|Foodnoms\+|Help)$/.test((el.innerText || '').trim()) && getComputedStyle(el).visibility !== 'hidden' && el.closest('[data-framer-name]');
    });
    // The overlay renders its own nav links inside a fixed layer.
    return links.some((el) => { let n = el; while (n) { const cs = getComputedStyle(n); if (cs.position === 'fixed') return true; n = n.parentElement; } return false; });
  }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await ok()) return 'the nav overlay was already open';
  const b = page.locator('button[aria-label="Open navigation menu"]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.evaluate((el) => el.scrollIntoView({ block: 'nearest', behavior: 'instant' }));
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok()) return 'clicked "Open navigation menu" to open the nav overlay';
    await page.waitForTimeout(500);
  }
  return 'clicked "Open navigation menu"; the overlay did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-bar', q('[data-framer-name="Desktop"]').filter({ has: page.locator('a[aria-label="Foodnoms home"]') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header row', desc: 'The top bar: app icon + Foodnoms name, News/Foodnoms+/Help links and the "Get the App" primary pill.', sel: '[data-framer-name="Desktop"] (header)' }, { noScroll: true });
  await S('nav-logo', q('a[aria-label="Foodnoms home"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Foodnoms app-icon + wordmark in the header; links home.', sel: 'a[aria-label="Foodnoms home"]' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: /^\s*News\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header link (News / Foodnoms+ / Help); measured, never followed.', sel: 'header nav a' }, { noScroll: true });
  await S('nav-cta', q('a[data-framer-name="Primary"]').filter({ hasText: /Get the App/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-the-App pill', desc: 'The orange "Get the App ↗" primary pill in the header; an App-Store link, measured never followed.', sel: 'a[data-framer-name="Primary"] "Get the App"' }, { noScroll: true });
  const h = G.home;
  await S('hero-ticker', q('[data-framer-name="Hero"] [data-framer-name="Title"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline ticker', desc: 'The rotating benefit headline ("Track Nutrition", "Lose Weight", "Eat Healthy", …). The semantic h1 is visually hidden; this Title container is the painted display text.', sel: '[data-framer-name="Hero"] [data-framer-name="Title"]' }, { noScroll: true });
  await S('hero-lede', q('[data-framer-name="Hero"] [data-framer-name="Paragraph"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: '"A simple, clear nutrition tracker for building healthier habits." — the intro paragraph under the ticker.', sel: 'hero [data-framer-name="Paragraph"]' }, { noScroll: true });
  await S('hero-icon-btn', q('a[data-framer-name="Button"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero icon button', desc: 'The circular icon button beside the hero headline (a Framer "Button" component with an inline svg).', sel: 'a[data-framer-name="Button"]' }, { allowLink: true });
  await S('goal-pill', q('[data-framer-name="Weight"], [data-framer-name="Healthy"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Goal pill', desc: 'A nutrition-goal chip in the benefits marquee (Weight, Healthy, Sugars, Water, Sodium, Muscle, Alcohol, Caffeine).', sel: '[data-framer-name="Weight"]' });
  await S('featured-title', q('[data-framer-name="Hero"] [data-framer-name="Trailing"] [data-framer-name="Title"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'As-Featured-By label', desc: 'The "As Featured By" caption over the press-logo strip.', sel: 'hero Trailing Title' });
  await S('featured-logo', q('[aria-label^="Featured in"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Press logo', desc: 'One outlet logo in the "As Featured By" strip (MacStories, iMore, 9to5Mac, PopSugar, Good Housekeeping, Prevention).', sel: '[aria-label^="Featured in"]' });
  await S('feature-card', q('[data-framer-name="Features"] > [data-framer-name="Container"], [data-framer-name="Features"] [data-framer-name="Container"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A feature section card ("Effortlessly Scan Food"): h3 title, paragraph and a product screenshot.', sel: 'Features > Container' });
  await S('feature-title', q('[data-framer-name="Features"] h3').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature heading', desc: 'The h3 inside a feature card ("Effortlessly Scan Food").', sel: 'Features h3' });
  await S('value-card', q('[data-framer-name="Values"] [data-framer-name="Container"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Value card', desc: 'A values card ("Privacy First", "Your Data, Your Control", "No Ads, Ever"): glyph, h4 title and paragraph.', sel: 'Values > Container' });
  await S('value-icon', q('[data-framer-name="Values"] [data-framer-name="Symbol"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Value glyph', desc: 'The svg glyph on a values card.', sel: 'Values Symbol svg' });
  await S('reviews-h2', q('[data-framer-name="Reviews"] [data-framer-name="Title"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Reviews heading', desc: '"Trusted By Thousands of Users" — the reviews section h2.', sel: 'Reviews Title' });
  await S('review-card', q('[data-framer-name="Reviews"] li').filter({ visible: true }).first(), ['default'], { group: h, title: 'Review card', desc: 'An App-Store review card in the scrolling marquee (quote, handle, star row).', sel: 'Reviews li' });
  await S('review-stars', q('[data-framer-name="Reviews"] [data-framer-name="Stars"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Star rating', desc: 'The five-star row on a review card.', sel: 'Reviews Stars' });
  await S('cta-h2', q('[data-framer-name="CTA"] h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'CTA heading', desc: '"Start Tracking Macros for Free" — the closing call-to-action block.', sel: 'CTA h2' });
  await S('cta-secondary', q('a[data-framer-name="Secondary"]').filter({ hasText: /Download/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The "Download the App ↗" secondary pill inside the closing CTA; an App-Store link, measured never followed.', sel: 'a[data-framer-name="Secondary"] "Download"' });
  const f = G.footer;
  await S('footer', q('[data-framer-name="Footer"]').filter({ visible: true }).last(), ['default'], { group: f, title: 'Footer', desc: 'The site footer: logo, Explore / Comparisons / Company / Social link columns and the legal row.', sel: '[data-framer-name="Footer"]' });
  await S('footer-col', q('[data-framer-name="Explore"] [data-framer-name="Header"], [data-framer-name="Comparisons"] [data-framer-name="Header"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer column label', desc: 'A link-column heading in the footer ("Explore").', sel: 'footer Explore Header' });
  await S('footer-link', q('[data-framer-name="Explore"] [data-framer-name="Item"] a').filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer link ("Download ↗" under Explore); measured, never followed.', sel: 'footer Explore Item a' });
  await S('footer-legal', q('[data-framer-name="Copyright"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Copyright line', desc: 'The "(C) 2026. Algebraic Labs, LLC." line beside the Terms/Privacy links.', sel: 'footer Copyright' });
  save();
}

async function plus() {
  if (!(await newPage('plus'))) return;
  await sheetsFor('plus');
  await chrome('plus');
  const g = G.plus;
  await S('plus-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Level Up Your Nutrition Tracking" — the Foodnoms+ page headline.', sel: 'h1 on /plus' }, { noScroll: true });
  await S('plus-tag', q('[data-framer-name="Tag"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tag chip', desc: 'The "Find pricing info for your region in the app." note chip under the headline.', sel: '[data-framer-name="Tag"]' });
  await S('plus-cta', q('a[data-framer-name="Primary"]').filter({ hasText: /Try Foodnoms/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Try-for-free CTA', desc: 'The "Try Foodnoms for Free ↗" primary pill; an App-Store link, measured never followed.', sel: 'a[data-framer-name="Primary"] "Try Foodnoms"' });
  await S('plus-cta-secondary', q('a[data-framer-name="Secondary"]').filter({ hasText: /Download/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Secondary download pill', desc: 'The "Download the App ↗" secondary pill on /plus; measured never followed.', sel: 'a[data-framer-name="Secondary"] on /plus' });
  await S('pricing-table', q('[data-framer-name="Table"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison table', desc: 'The Free vs Foodnoms+ feature-comparison table — a Framer component of Row/Header/Title/Paragraph/Divider/Symbol cells, not a <table> element.', sel: '[data-framer-name="Table"]' });
  await S('pricing-head', q('[data-framer-name="Table"] [data-framer-name="Header"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table header cell', desc: 'A column header cell in the comparison table ("Features" / "Free" / "Foodnoms+").', sel: 'Table Header' });
  await S('pricing-row', q('[data-framer-name="Table"] [data-framer-name="Row"]').filter({ hasText: /Nutrient Tracking/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Table row', desc: 'A feature row ("Nutrient Tracking") with its Free and Foodnoms+ cells.', sel: 'Table Row' });
  await S('pricing-cell', q('[data-framer-name="Table"] [data-framer-name="Paragraph"]').filter({ hasText: /Calories & Macros/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Table cell text', desc: 'A feature cell value ("Calories & Macros" under Free).', sel: 'Table Paragraph' });
  await S('pricing-check', q('[data-framer-name="Table"] [data-framer-name="Symbol"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table check glyph', desc: 'The check-mark svg used for included features in the comparison table.', sel: 'Table Symbol svg' });
  await S('pricing-divider', q('[data-framer-name="Table"] [data-framer-name="Divider"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Table divider', desc: 'The hairline divider between comparison rows.', sel: 'Table Divider' }, { crop: false });
  save();
}

async function help() {
  if (!(await newPage('help'))) return;
  await sheetsFor('help');
  await chrome('help');
  const g = G.help;
  await S('help-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Help headline', desc: '"Help Center".', sel: 'h1 on /help' }, { noScroll: true });
  await S('help-search', q('[data-framer-name="Variant 1"]').filter({ hasText: /^\s*Search\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Search trigger', desc: 'The "Search" control on the help landing — a Framer component that opens the search modal when clicked (a local UI toggle).', sel: '[data-framer-name="Variant 1"] "Search"' });
  await S('help-search-modal', q('.__framer-search-modal-container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search modal', desc: 'The Framer search overlay opened by the Search trigger.', sel: '.__framer-search-modal-container' }, { open: openSearch, noScroll: true });
  await S('help-search-input', q('.__framer-search-modal-container input, input[placeholder="Search..."]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The real input inside the Framer search modal; focused and typed into then cleared — never submitted.', sel: 'search modal input' }, { open: openSearch, fillText: 'barcode' });
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(700);
  await S('help-accordion', q('[data-framer-name="Closed"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Accordion section (closed)', desc: 'A collapsed topic group ("About Foodnoms"): header row with title and rotating + chevron; the question links sit inside.', sel: '[data-framer-name="Closed"]' });
  await S('help-accordion-open', q('[data-framer-name="Open"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Accordion section (open)', desc: 'The same topic group expanded — measured after clicking its own Header (a local UI toggle; Closed -> Open).', sel: '[data-framer-name="Open"]' }, { open: openFirstAccordion });
  await S('help-accordion-header', q('[data-framer-name="Open"] [data-framer-name="Header"], [data-framer-name="Closed"] [data-framer-name="Header"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Accordion header', desc: 'The clickable header row of a topic group (tabindex=0, data-highlight): title + chevron.', sel: 'accordion Header' });
  await S('help-accordion-link', q('[data-framer-name="Open"] a, [data-framer-name="Closed"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Accordion question link', desc: 'A question link inside an open accordion ("What is Foodnoms?"); measured, never followed.', sel: 'accordion a' }, { open: openFirstAccordion, allowLink: true });
  await S('help-contact', q('[data-framer-name="Contact"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact block', desc: 'The "Contact Us" block under the accordion sections.', sel: '[data-framer-name="Contact"]' });
  await S('help-contact-cta', q('a[data-framer-name="Primary"]').filter({ hasText: /@|Email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Contact CTA', desc: 'The mailto CTA in the Contact block (support@foodnoms.com, a published contact address); measured, never activated.', sel: 'Contact Primary mailto' });
  save();
}

async function news() {
  if (!(await newPage('news'))) return;
  await sheetsFor('news');
  await chrome('news');
  const g = G.news;
  await S('news-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'News headline', desc: '"News & Updates".', sel: 'h1 on /news' }, { noScroll: true });
  await S('news-card', q('a[href*="/news/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Article card', desc: 'A news article card (CMS image, title, date) linking to a /news/* article; measured, never followed.', sel: 'a[href*="/news/"]' }, { allowLink: true });
  await S('news-date', q('[data-framer-name="Date"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card date', desc: 'The publish-date label on a news card.', sel: '[data-framer-name="Date"]' });
  await S('nl-h2', q('[data-framer-name="Newsletter"] h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Newsletter heading', desc: '"Become a Foodnoms Insider" — the newsletter block heading.', sel: 'Newsletter h2' });
  await S('nl-email', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Newsletter email field', desc: 'The pill-shaped email field in the newsletter block; focused and typed into then cleared — never submitted.', sel: 'input[type="email"]' }, { fillText: 'name@example.com' });
  await S('nl-submit', q('input[type="submit"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Newsletter submit', desc: 'The subscribe submit control; hovered and focused only — never pressed (it posts the form).', sel: 'input[type="submit"]' });
  save();
}

async function press() {
  if (!(await newPage('press'))) return;
  await sheetsFor('press');
  await chrome('press');
  const g = G.press;
  await S('press-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Press headline', desc: '"Press Hub".', sel: 'h1 on /press' }, { noScroll: true });
  await S('press-tag', q('[data-framer-name="Tag"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section tag', desc: 'A tag label on the press page sections.', sel: '[data-framer-name="Tag"]' });
  await S('press-details', q('[data-framer-name="Details"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'App details block', desc: 'The "App Details" fact block on the press hub.', sel: '[data-framer-name="Details"]' });
  await S('press-asset', q('a').filter({ hasText: /^\s*Download Screenshots\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Asset download link', desc: 'The "Download Screenshots" asset link (a framerusercontent .zip); measured, never downloaded.', sel: 'press "Download Screenshots"' }, { allowLink: true });
  await S('press-contact-cta', q('a[data-framer-name="Secondary"]').filter({ hasText: /Email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Press contact CTA', desc: 'The "Email Ryan />" secondary pill (a published press-contact mailto); measured, never activated.', sel: 'press Secondary mailto' });
  save();
}

async function familyPlan() {
  if (!(await newPage('family-plan'))) return;
  await sheetsFor('family-plan');
  await chrome('family-plan');
  const g = G.article;
  await S('fp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: '"A calorie tracker with a family plan" — the /family-plan article headline.', sel: 'h1 on /family-plan' }, { noScroll: true });
  await S('fp-intro', q('[data-framer-name="Intro Body"], [data-framer-name="Intro"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Intro paragraph', desc: 'The article intro block under the headline.', sel: '[data-framer-name="Intro Body"]' });
  await S('fp-faq', q('[data-framer-name="FAQ"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ block', desc: 'The "Frequently asked questions" block — static question + Answer rows, not an accordion.', sel: '[data-framer-name="FAQ"]' });
  await S('fp-faq-answer', q('[data-framer-name="Answer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'An answer paragraph inside the FAQ block.', sel: '[data-framer-name="Answer"]' });
  save();
}

async function vsMfp() {
  if (!(await newPage('vs-mfp'))) return;
  await sheetsFor('vs-mfp');
  await chrome('vs-mfp');
  const g = G.article;
  await S('vs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison headline', desc: 'The /vs/myfitnesspal article headline.', sel: 'h1 on /vs/myfitnesspal' }, { noScroll: true });
  await S('vs-body', q('[data-framer-name="Article"] p, article p').filter({ hasText: /.{60,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph in the comparison article.', sel: 'Article p' });
  await S('vs-table', q('table').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison table', desc: 'The "Quick Comparison" feature table inside the article body.', sel: 'article table' });
  await S('vs-faq-h2', q('h2').filter({ hasText: /Frequently Asked Questions/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ heading', desc: 'The "Frequently Asked Questions" h2 in the article.', sel: 'article h2 FAQ' });
  save();
}

async function helpArticle() {
  if (!(await newPage('help-article'))) return;
  await sheetsFor('help-article');
  await chrome('help-article');
  const g = G.article;
  await S('ha-back', q('[data-framer-name="Article"] a[data-framer-name="Secondary"]').filter({ hasText: /Back/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: 'The "← Back" pill at the top of a help article (links to /help); measured, never followed.', sel: 'article Secondary "← Back"' }, { allowLink: true, noScroll: true });
  await S('ha-tag', q('[data-framer-name="Article"] [data-framer-name="Tag"], [data-framer-name="Tag"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article tag', desc: 'The category tag chip on a help article.', sel: 'article Tag' }, { noScroll: true });
  await S('ha-h1', q('[data-framer-name="Article"] h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: '"How do I scan barcodes?" — a help article title.', sel: 'article h1' }, { noScroll: true });
  await S('ha-body', q('[data-framer-name="Article"] p').filter({ hasText: /.{60,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph inside the help article.', sel: 'article p' });
  await S('ha-h2', q('[data-framer-name="Article"] h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article section heading', desc: 'A section heading inside the article ("Scanning a Barcode").', sel: 'article h2' });
  save();
}

// The barcode-scanning article's only anchor is its Back pill — the prose
// carries no inline link — so the inline-link reading comes from /help/mcp,
// which has real links inside its paragraphs.
async function helpMcp() {
  if (!(await newPage('help-mcp'))) return;
  const g = G.article;
  await S('ha-link', q('[data-framer-name="Article"] p a').filter({ hasText: /\S{3,}/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'A link inside a help article\'s prose (the /help/mcp article; the barcode article has none); measured, never followed.', sel: 'article p a' }, { allowLink: true });
  save();
}

async function newsArticle() {
  if (!(await newPage('news-article'))) return;
  await sheetsFor('news-article');
  await chrome('news-article');
  const g = G.article;
  await S('na-date', q('[data-framer-name="Date"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article date', desc: 'The publish-date label above the article title.', sel: '[data-framer-name="Date"]' }, { noScroll: true });
  await S('na-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: '"FoodNoms 2: Feature Overview" — a news article title.', sel: 'article h1' }, { noScroll: true });
  await S('na-toc', q('h2, h3, [data-framer-name="Title"]').filter({ hasText: /^\s*Table of Contents\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Table of contents label', desc: 'The "Table of Contents" heading beside the anchor list.', sel: 'TOC heading' });
  await S('na-inline-link', q('a').filter({ hasText: /^\s*HidrateSpark\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'An inline link inside the article prose ("HidrateSpark"); measured, never followed.', sel: 'article a "HidrateSpark"' }, { allowLink: true });
  await S('na-h2', q('article h2, [data-framer-name="Article"] h2, h2').filter({ hasText: /Design Changes/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article section heading', desc: 'A section heading inside the news article.', sel: 'article h2' });
  await S('na-body', q('p').filter({ hasText: /.{80,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph in the news article.', sel: 'article p' });
  save();
}

async function terms() {
  if (!(await newPage('terms'))) return;
  await sheetsFor('terms');
  await chrome('terms');
  const g = G.legal;
  await S('terms-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Terms headline', desc: '"Terms of Use".', sel: 'h1 on /terms' }, { noScroll: true });
  await S('terms-item', q('[data-framer-name="Legal Item"] h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal section heading', desc: 'A numbered section heading inside the legal body ("1. Agreement to these Terms" style; the single Legal Item component holds the whole document).', sel: 'Legal Item h3' });
  save();
}

async function openSignup() {
  if (!(await newPage('open-signup'))) return;
  await sheetsFor('open-signup');
  await chrome('open-signup');
  const g = G.open;
  await S('os-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Interstitial headline', desc: '"Open in Foodnoms" — the deep-link interstitial shown when an app link is opened on the web.', sel: 'h1 on /open/settings/sign-up' }, { noScroll: true });
  await S('os-primary', q('a[data-framer-name="Secondary"]').filter({ hasText: /Open in Foodnoms/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Interstitial action', desc: 'The "Open in Foodnoms" pill on the interstitial — the page\'s own action (a deep link back into the app); measured, never followed.', sel: 'interstitial Secondary "Open in Foodnoms"' }, { allowLink: true });
  save();
}

// A small dark pass: the same key components re-read under emulated
// prefers-color-scheme dark — the site's own media rule repaints them, so
// these are the values a dark-system visitor actually gets.
async function darkp() {
  if (!(await newPage('dark', { colorScheme: 'dark' }))) return;
  const g = G.dark;
  const themed = await page.evaluate(() => ({ scheme: matchMedia('(prefers-color-scheme: dark)').matches, bodyBg: getComputedStyle(document.body).backgroundColor, bodyColor: getComputedStyle(document.body).color }));
  out._meta.darkProbe = themed;
  if (!themed.scheme) log('  ! dark media did not take; readings may be light');
  await S('d-body', q('main, [data-framer-name="Desktop"], body > div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page canvas (dark)', desc: 'The top-level frame under the dark media rule.', sel: 'page root (dark)' }, { noScroll: true, crop: false });
  await S('d-nav-cta', q('a[data-framer-name="Primary"]').filter({ hasText: /Get the App/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Get-the-App pill (dark)', desc: 'The header primary pill under the dark media rule.', sel: 'nav Primary (dark)' }, { noScroll: true });
  await S('d-nav-link', q('a').filter({ hasText: /^\s*News\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav link (dark)', desc: 'A header link under the dark media rule.', sel: 'nav a (dark)' }, { noScroll: true });
  await S('d-hero-lede', q('[data-framer-name="Hero"] [data-framer-name="Paragraph"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero lede (dark)', desc: 'The hero paragraph under the dark media rule.', sel: 'hero Paragraph (dark)' });
  await S('d-feature-card', q('[data-framer-name="Features"] [data-framer-name="Container"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature card (dark)', desc: 'A feature card under the dark media rule.', sel: 'Features Container (dark)' });
  await S('d-value-card', q('[data-framer-name="Values"] [data-framer-name="Container"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Value card (dark)', desc: 'A values card under the dark media rule.', sel: 'Values Container (dark)' });
  await S('d-review-card', q('[data-framer-name="Reviews"] li').filter({ visible: true }).first(), ['default'], { group: g, title: 'Review card (dark)', desc: 'A review card under the dark media rule.', sel: 'Reviews li (dark)' });
  await S('d-footer', q('[data-framer-name="Footer"]').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer (dark)', desc: 'The footer under the dark media rule.', sel: 'Footer (dark)' });
  await S('d-footer-link', q('[data-framer-name="Explore"] [data-framer-name="Item"] a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer link (dark)', desc: 'A footer link under the dark media rule.', sel: 'footer a (dark)' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('[data-framer-name="Leading"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone top bar: app icon, Foodnoms name and the hamburger.', sel: 'mobile Leading (header)' }, { noScroll: true });
  await S('m-hamburger', q('button[aria-label="Open navigation menu"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hamburger', desc: 'The "Open navigation menu" button that opens the phone nav overlay (its aria-label flips to "Close navigation menu" once open; the opened overlay is evidenced by the mobile-home-light-drawer screenshot).', sel: 'button[aria-label="Open navigation menu"]' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-ticker', q('[data-framer-name="Hero"] [data-framer-name="Title"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero ticker', desc: 'The rotating headline at 390 wide.', sel: 'mobile hero Title' });
  await S('m-hero-cta', q('a[data-framer-name="Primary"]').filter({ hasText: /Download|Get the App/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The primary App-Store pill on the phone layout; measured never followed.', sel: 'mobile Primary' });
  await S('m-feature-card', q('[data-framer-name="Features"] [data-framer-name="Container"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile feature card', desc: 'A feature card at 390 wide.', sel: 'mobile Features Container' });
  await S('m-review-card', q('[data-framer-name="Reviews"] li').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile review card', desc: 'A review card at 390 wide.', sel: 'mobile Reviews li' });
  await S('m-footer-link', q('[data-framer-name="Footer"] [data-framer-name="Item"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile footer link', desc: 'A footer link at 390 wide; measured, never followed.', sel: 'mobile footer a' }, { allowLink: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844; dark group 1440 x 900 under emulated prefers-color-scheme: dark)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, plus, help, news, press, 'family-plan': familyPlan, 'vs-mfp': vsMfp, 'help-article': helpArticle, 'help-mcp': helpMcp, 'news-article': newsArticle, terms, 'open-signup': openSignup, dark: darkp, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'dark') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('dark')) { await plan.dark(); finishedPages.add('dark'); }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a nav link's
  // colour transition), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a');
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
