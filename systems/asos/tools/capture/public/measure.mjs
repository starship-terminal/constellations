// Measures asos.com's public components in every state reachable without
// adding to bag, joining, subscribing or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home women plp pdp bag saved account mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// asos.com is a React storefront in one light theme, geo-served (Singapore,
// ROW store, SGD prices). Classes are CSS-module hashes, so selectors key off
// roles, aria-labels, stable class stems ([class*="productTile"]) and text.
// Akamai 403s headless Chromium/Chrome, so every page opens in HEADED Chrome
// (channel 'chrome', headless false — see lib.mjs). Nothing is sent, added to
// bag, joined or subscribed: the only presses are local UI toggles — the
// mobile menu, a PDP size select and accordion rows. The OneTrust consent SDK
// is hidden before every measurement, never answered. "ADD TO BAG" and the
// sign-in "CONTINUE" are measured in all states except a real press.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { pageRunner, exitStatus } from './run-pages.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', women: '/women/', plp: '/women/new-in/new-in-clothing/cat/?cid=2623', pdp: '/women/new-in/new-in-clothing/cat/?cid=2623', bag: '/bag', saved: '/saved-lists/', account: 'https://my.asos.com/my-account' };
let page, cdp, current, context, run;
let activeCtx; // the context of the current page; closed when the next route opens
const touched = new Set();
const blockedPages = new Set(); // pages a bot check stopped; their old readings are kept
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /access denied|performing security verification|verifying you are human|just a moment|edgesuite\.net/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  // Close the previous route's context first: leaving every context and page
  // running until the whole pass ends keeps each route's scripts, images and
  // timers alive while later routes are measured.
  if (activeCtx) { await activeCtx.close().catch(() => {}); activeCtx = undefined; }
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-GB' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-GB' });
  activeCtx = ctx;
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const target = URLS[key];
  await open(page, /^https?:/.test(target) ? target : BASE + target, { wait });
  if (await blocked()) { log('  BLOCKED', key); blockedPages.add(key); await page.close(); await ctx.close(); activeCtx = undefined; return false; }
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

// comp() merges the spec's meta into the entry and marks it touched. The
// page/run/url provenance is only written once the target is found, so a
// re-run whose selector misses keeps the earlier evidence's own page, run and
// url instead of stamping a new date on stale readings (FIELD-NOTES).
function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, meta);
  // the page that owns the entry, even when its element is missing: stale-entry
  // cleanup (pageDone) needs it; found() restamps page/run/url on a real reading
  c.page ??= current;
  touched.add(key);
  c.states ??= {};
  return c;
}

function found(c) {
  delete c.missing;
  delete c.recaptureMissed;
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current]) ? URLS[current] : BASE + URLS[current] });
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
  // meta is the entry's description only; an option placed here (fillText, cropLoc,
  // noToggle...) would be silently ignored, so refuse it
  for (const k of Object.keys(meta)) if (!['group', 'title', 'desc', 'sel'].includes(k)) throw new Error(`S(${key}): '${k}' is an option; pass it in opts`);
  const c = comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0,80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    log('  ! missing', key);
    c.missing = true;
    c.recaptureMissed = run;
    c.states = {}; // stale states from an earlier run are not current evidence
    return;
  }
  found(c);
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
        // a state that did not receive keyboard focus is not a captured focus
        if (via === 'focus failed') throw new Error('keyboard focus did not land on the element');
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
      } else if (st === 'picked') {
        const sel = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await sel.selectOption({ index: 1 }).catch(() => {});
        await page.waitForTimeout(500);
        undo = async () => { await sel.selectOption({ index: 0 }).catch(() => {}); };
        via = 'selectOption index 1, then restored to index 0; nothing submitted';
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (menu, accordion, swatch). Refuses a submit button and any
// control whose text names a purchase/action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|continue)$/i;
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

const G = {
  shell: 'Shell and navigation', hero: 'Home', hub: 'Hub pages', plp: 'Shop grid', pdp: 'Product page',
  bag: 'Bag', saved: 'Saved lists', account: 'Account gate', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

const tid = (id) => `[data-testid="${id}"]`;

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('app-strip', q(tid('download-app')).first(), ['default'], { group: g, title: 'App strip', desc: 'The dark link at the very top right of the page, above the header.', sel: tid('download-app') }, { noScroll: true });
  await S('help-link', q(tid('help')).first(), B4, { group: g, title: 'Help link', desc: '"Help & FAQs" in the top bar.', sel: tid('help') }, { noScroll: true });
  await S('country-link', q(tid('country-selector-btn')).first(), B4, { group: g, title: 'Country selector', desc: '"You\'re in Singapore Change" — a flag button in the top bar; opens the country picker, never pressed.', sel: tid('country-selector-btn') }, { noScroll: true });
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The black bar: white wordmark, WOMEN/MEN tabs, search field, account, saved and bag icons.', sel: 'header' }, { noScroll: true });
  await S('logo', q(tid('asoslogo')).first(), ['default'], { group: g, title: 'Logo', sel: tid('asoslogo') }, { noScroll: true });
  await S('nav-tab', q(tid('women-floor')).first(), B4, { group: g, title: 'Gender tab', desc: 'WOMEN/MEN — the audience switch in the header.', sel: tid('women-floor') }, { noScroll: true });
  // The category nav row (primarynav-button ×22) stays display:none on the
  // home page; it is measured in plp() where the row is visible.
  await S('search-input', q(tid('search-input')).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The header search input; focused only, nothing typed.', sel: tid('search-input') }, { noScroll: true });
  await S('search-button', q(tid('search-button-inline')).first(), B4, { group: g, title: 'Search button', desc: 'The magnifier at the end of the search field. Measured, never pressed.', sel: tid('search-button-inline') }, { noScroll: true });
  await S('account-icon', q(tid('myAccountIcon')).first(), B4, { group: g, title: 'Account icon', desc: 'Opens the My Account dropdown (Sign In / Join); measured, never opened.', sel: tid('myAccountIcon') }, { noScroll: true });
  await S('saved-icon', q(tid('savedItemsIcon')).first(), B4, { group: g, title: 'Saved-lists icon', desc: 'The heart. Measured, never followed.', sel: tid('savedItemsIcon') }, { noScroll: true });
  await S('bag-icon', q(tid('miniBagIcon')).first(), B4, { group: g, title: 'Bag icon', desc: '"Bag 0 items". Measured, never followed.', sel: tid('miniBagIcon') }, { noScroll: true });
  const strip = await domFind(page, /new here\?/i, { sel: 'div,section,aside', tag: 'promo', leaf: true, minW: 300 });
  await S('promo-strip', strip, ['default'], { group: g, title: 'Promo strip', desc: 'The dark panel under the header carrying the new-customer offer and WOMEN/MEN toggle buttons.', sel: 'leaf container:has-text("New here?")' }, { noScroll: true });
  await S('promo-tab', strip.locator('a, button').filter({ hasText: /^MEN$/i }).first(), B4, { group: g, title: 'Promo strip tab', desc: 'The bordered WOMEN/MEN buttons inside the promo strip.', sel: 'inside promo strip: a/button "MEN"' }, { noScroll: true });

  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  const h = G.hero;
  await S('hero-cta', q('a, button').filter({ hasText: /^shop womens$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The filled hero button ("SHOP WOMENS"). Measured, never followed.', sel: 'a:has-text("SHOP WOMENS")' });
  await S('hero-cta-alt', q('a, button').filter({ hasText: /^shop mens$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA, alternate', sel: 'a:has-text("SHOP MENS")' });
  await S('grid-tile', q('a.feature__link').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Content tile', desc: 'A dark marketing tile lower on the home page ("NEW HERE?"…).', sel: 'a.feature__link' });
  save();
}

async function women() {
  if (!(await newPage('women'))) return;
  const g = G.hub;
  // The hub h1 is a 1px screen-reader label; the visible "title" is the
  // promo banner and the section heads below it.
  const banner = await domFind(page, /up to \d+% off|single'?s day/i, { sel: 'section,div', tag: 'banner', leaf: true, minW: 300 });
  await S('hub-banner', banner, ['default'], { group: g, title: 'Hub promo banner', desc: 'The dark "SINGLES\' DAY — UP TO 40% OFF" banner under the header.', sel: 'leaf container:has-text("UP TO 40% OFF")' }, { noScroll: true });
  await S('hub-title', q('h2').filter({ hasText: /the latest drops/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Hub section title', desc: '"The latest drops" — the hub\'s visible section heading (the h1 is screen-reader only).', sel: 'h2:has-text("The latest drops")' });
  await S('hub-tile', q('a.hero__link').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Hub hero tile', desc: 'The "THE PARTY EDIT / SHOP NOW" campaign tile.', sel: 'a.hero__link' });
  // Scoped to the section carrying the "The latest drops" heading: a bare
  // `main a:has(h2)` climbs out of the rail and lands on the promo banner.
  const railHead = q('h2').filter({ hasText: /the latest drops/i }).filter({ visible: true }).first();
  const rail = railHead.locator('xpath=ancestor::*[(self::section or self::div) and .//a[.//img]][1]');
  await S('hub-card', rail.locator('a').filter({ has: q('img') }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Hub rail card', desc: 'A card in the "latest drops" rail.', sel: 'section:has(h2 "The latest drops") a:has(img)' });
  save();
}

async function plp() {
  if (!(await newPage('plp', { wait: 9000 }))) return;
  const g = G.plp;
  await S('breadcrumb', q('nav[aria-label*="breadcrumb" i], [class*="breadcrumb" i]').first(), ['default'], { group: g, title: 'Breadcrumb', desc: 'Home / Women / New In / New In: Clothing.', sel: 'breadcrumb nav' }, { noScroll: true });
  // The category nav row is visible here (it is display:none on home).
  const gnav = G.shell;
  await S('nav-item', q(tid('primarynav-button')).filter({ visible: true }).first(), B4, { group: gnav, title: 'Category button', desc: 'A button in the category nav row (New in, Clothing, Dresses…); each opens a flyout.', sel: tid('primarynav-button') }, { cropLoc: q(tid('primarynav-button')).filter({ visible: true }).first(), noScroll: true });
  const newin = q(tid('primarynav-button')).filter({ visible: true }).first();
  await S('nav-mega', newin, ['opened'], { group: gnav, title: 'Category flyout, open', desc: 'The nav button while its flyout is open.', sel: tid('primarynav-button') + ':hover' }, { cropLoc: newin, noScroll: true, noReset: true, noToggle: true, open: async () => { await newin.hover(); await page.waitForTimeout(1600); } });
  await S('nav-flyout', q(tid('secondarynav-flyout')).filter({ visible: true }).first(), ['default'], { group: gnav, title: 'Category flyout panel', desc: 'The open mega-menu panel itself, while the button is hovered.', sel: tid('secondarynav-flyout') }, { cropLoc: q(tid('secondarynav-flyout')).filter({ visible: true }).first(), noScroll: true, noReset: true, open: async () => { await newin.hover(); await page.waitForTimeout(1600); } });
  // Only states that keep the pointer on the nav button: the flyout closes
  // as soon as focus moves, so focus/press states on its links do not exist.
  await S('flyout-link', q(tid('secondarynav-flyout')).filter({ visible: true }).first().locator(tid('text-link')).filter({ visible: true }).first(), ['default', 'hover'], { group: gnav, title: 'Flyout link', desc: 'A link inside the open mega-menu ("View all", "New In: Today"…). Measured, never followed.', sel: tid('secondarynav-flyout') + ' ' + tid('text-link') }, { cropLoc: q(tid('secondarynav-flyout')).filter({ visible: true }).first().locator(tid('text-link')).filter({ visible: true }).first(), noScroll: true, noReset: true, open: async () => { await newin.hover(); await page.waitForTimeout(1600); } });
  await page.mouse.move(700, 500); await page.waitForTimeout(500);
  await S('plp-title', q('h1').first(), ['default'], { group: g, title: 'Collection title', desc: '"New In Clothing for Women" in Futura bold.', sel: 'h1' }, { noScroll: true });
  await S('cat-pill', q('a, button').filter({ hasText: /new in: today/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category pill', desc: 'A chip in the sub-category carousel ("New in: Today"…).', sel: ':has-text("New in: Today")' }, { noScroll: true });
  await S('sort-button', q(tid('sort-button')).first(), B4, { group: g, title: 'Sort control', desc: 'The grid sort trigger. Measured, never opened.', sel: tid('sort-button') });
  await S('filter-button', q(tid('filter-button-desktop')).first(), B4, { group: g, title: 'Filter button', desc: 'Opens the filter panel; measured, never opened.', sel: tid('filter-button-desktop') });
  await S('styles-count', q('p, span, div').filter({ hasText: /styles found$/i }).last(), ['default'], { group: g, title: 'Styles count', desc: '"2,697 styles found".', sel: ':has-text("styles found")' });
  const card = q('[class*="productTile"]').filter({ visible: true }).first();
  await S('product-tile', card, ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A grid card: image, save heart, name, price, MORE COLOURS / SELLING FAST badges.', sel: '[class*="productTile"]' });
  await S('save-heart', card.locator('button[aria-label*="save" i]').first(), B4, { group: g, title: 'Save heart', desc: 'The heart on a product tile; a local save toggle, never pressed.', sel: 'tile button[aria-label*="Save"]' });
  await S('tile-name', card.locator('a[href*="/prd/"]').first(), B4, { group: g, title: 'Product link', desc: 'The whole-card link inside the tile: image, name and price.', sel: 'a.productLink' });
  await S('tile-price', card.locator('[class*="price" i], p, span').filter({ hasText: /SGD\$|\$\d/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Tile price', desc: 'SGD pricing on the geo-served surface.', sel: ':has-text("SGD$")' });
  // The label itself, not the first span/div/p whose text merely contains it
  // (that is the tile's whole name-and-price block).
  await S('tile-badge', card.getByText(/^\s*(selling fast|more colours)\s*$/i).filter({ visible: true }).first(), ['default'], { group: g, title: 'Tile badge', desc: 'SELLING FAST or MORE COLOURS — the small status text under a tile.', sel: ':has-text("SELLING FAST")' });
  await S('load-more', q(tid('loadMoreProducts') + ', [data-auto-id="loadMoreProducts"]').filter({ visible: true }).first(), B4, { group: g, title: 'Load more', desc: 'The grid pagination button. Measured, never pressed.', sel: '[data-auto-id="loadMoreProducts"]' });
  save();
}

async function pdp() {
  if (!(await newPage('pdp', { wait: 9000 }))) return;
  // Walk to the first product the shop grid offers.
  const href = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a[href*="/prd/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
    return a ? a.getAttribute('href') : null;
  });
  if (href) {
    await page.goto(href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await page.waitForTimeout(9000);
    await closePromo(page);
    await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  }
  const g = G.pdp;
  out.components.pdp_url ??= { page: 'pdp', title: 'PDP URL', states: {} };
  out.components.pdp_url.states.default = { text: href || 'none found', via: 'first product link on /women/new-in/new-in-clothing/cat/?cid=2623' };
  touched.add('pdp_url');
  await S('pdp-title', q('h1').first(), ['default'], { group: g, title: 'Product title', sel: 'h1' }, { noScroll: true });
  await S('pdp-price', q(tid('product-price')).first(), ['default'], { group: g, title: 'Product price', sel: tid('product-price') }, { noScroll: true });
  await S('rating', q(tid('rating-button')).first(), ['default'], { group: g, title: 'Star rating', desc: 'The 3.8 (30) review stars under the price.', sel: tid('rating-button') }, { noScroll: true });
  await S('promo-banner', q(tid('promo-message-box')).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The light-blue strip "Get 20% off! With code: WOW" between price and colour.', sel: tid('promo-message-box') });
  await S('colour-label', q(tid('productColour')).first(), ['default'], { group: g, title: 'Colour label', sel: tid('productColour') });
  await S('fit-link', q(tid('fitAssistantLink')).first(), B4, { group: g, title: 'Fit Assistant link', desc: '"Find your Fit Assistant size" beside SIZE:. Measured, never pressed.', sel: tid('fitAssistantLink') });
  await S('size-select', q('select').filter({ visible: true }).first(), ['default', 'focused', 'picked'], { group: g, title: 'Size select', desc: 'The native "Please select" dropdown; a size was picked then restored, never submitted.', sel: 'select' });
  await S('add-to-bag', q(tid('add-button')).first(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Add to bag', desc: 'The green buy button; measured in every state except a real press.', sel: tid('add-button') });
  await S('save-button', q(tid('saveForLater')).filter({ visible: true }).first(), B4, { group: g, title: 'Save for later', desc: 'The heart button beside Add to bag; a local save toggle, never pressed.', sel: tid('saveForLater') });
  await S('delivery-link', q(tid('deliveryAndReturns__termsLink')).first(), B4, { group: g, title: 'Delivery link', sel: tid('deliveryAndReturns__termsLink') });
  const acc = q(tid('product-description-section')).locator('button, [aria-expanded]').filter({ visible: true }).first();
  await S('pdp-accordion', acc, B4, { group: g, title: 'PDP accordion', desc: 'A disclosure row (Size & Fit / Product Details / Brand).', sel: tid('product-description-section') + ' button' });
  await S('pdp-accordion-open', acc, ['opened'], { group: g, title: 'PDP accordion, open', sel: 'accordion button' });
  await S('gallery-chevron', q(tid('imageGalleryChevrons')).locator('button').first(), B4, { group: g, title: 'Gallery chevron', desc: 'The prev/next control on the product gallery. Measured, never pressed.', sel: tid('imageGalleryChevrons') + ' button' });
  await S('reviews-cta', q(tid('reviewsViewAll')).filter({ visible: true }).first(), B4, { group: g, title: 'Reviews CTA', desc: '"VIEW ALL REVIEWS" — measured, never pressed.', sel: tid('reviewsViewAll') });
  save();
}

async function bag() {
  if (!(await newPage('bag'))) return;
  const g = G.bag;
  await S('bag-title', q('h1, h2').filter({ hasText: /bag/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Bag title', desc: '"MY BAG".', sel: 'h1' }, { noScroll: true });
  await S('bag-empty', q('main').first(), ['default'], { group: g, title: 'Bag body', desc: 'The signed-out bag with nothing in it.', sel: 'main' }, { noScroll: true });
  await S('bag-cta', q('a, button').filter({ hasText: /continue shopping|shop now|start shopping|sign in|shop women|shop men/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Bag CTA', desc: 'Measured, never followed.', sel: 'a:has-text("Shop")' });
  save();
}

async function saved() {
  if (!(await newPage('saved'))) return;
  const g = G.saved;
  await S('saved-title', q('h1, h2').filter({ hasText: /saved|boards/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Saved title', sel: 'h1' }, { noScroll: true });
  await S('saved-empty', q('main').first(), ['default'], { group: g, title: 'Saved body', desc: 'Saved items is signed-out empty.', sel: 'main' }, { noScroll: true });
  await S('saved-cta', q('a, button').filter({ hasText: /sign in|continue|shop/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Saved CTA', desc: 'Measured, never followed.', sel: 'a:has-text("Sign in")' });
  save();
}

async function account() {
  if (!(await newPage('account'))) return;
  const g = G.account;
  // my.asos.com/account/login: "Hi friend!" — email, CONTINUE, socials.
  await S('login-title', q('h1, h2').filter({ hasText: /hi friend|sign in|welcome/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login title', desc: '"Hi friend!"', sel: 'h1' }, { noScroll: true });
  await S('email-input', q('input[name*="email" i], input[type="email"], input[type="text"]').first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'Text was typed and deleted; the form was never submitted.', sel: 'input[name="email"]' });
  await S('continue-button', q('button, input[type="submit"]').filter({ hasText: /continue/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Continue button', desc: 'The submit; measured except a real press — the form was never submitted.', sel: 'button:has-text("CONTINUE")' });
  await S('social-button', q('button, a').filter({ hasText: /google|facebook|apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Social sign-in button', desc: 'Measured, never pressed.', sel: 'button:has-text("GOOGLE")' });
  save();
}

async function footer() {
  // The footer lives on the home page, but a full run ends on my.asos.com —
  // open home first so the readings are the home footer the page/run/url claim.
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); blockedPages.add('home'); return; }
    await closePromo(page);
  }
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q(tid('social-link')).first(), B4, { group: g, title: 'Footer social icon', sel: tid('social-link') });
    const nl = q('footer input[type="email"], footer input[name*="email" i], input[placeholder*="email" i]').first();
    if (await nl.count()) await S('newsletter-input', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; never subscribed.', sel: 'footer input[type="email"]' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q(tid('burger-menu-button')).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: tid('burger-menu-button') }, { noScroll: true });
  // The button is measured, but the crop is the opened side panel: the
  // data-testid="sidepanel" portal's fixed 320x844 child (the drawer itself is
  // a hashed-class div, so the testid portal is the stable handle). A miss
  // records no crop.
  const drawer = q(tid('sidepanel')).locator('> div').filter({ visible: true }).first();
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the crop is the open drawer, not the button.', sel: tid('burger-menu-button') }, { noScroll: true, cropLoc: drawer });
  const mLink = q(tid('menu-item')).filter({ visible: true }).nth(1);
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A category row inside the opened side panel (NEW IN, CLOTHING…).', sel: tid('menu-item') }, { noScroll: true });
  await S('m-floor-tab', q(tid('women-floor')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile floor tab', desc: 'The WOMEN tab at the top of the open side panel.', sel: tid('women-floor') }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-search-icon', q(tid('searchIcon')).first(), B4, { group: g, title: 'Mobile search icon', desc: 'The magnifier that opens the search overlay (there is no inline field on mobile).', sel: tid('searchIcon') }, { noScroll: true });
  await S('m-feature-tile', q('a.feature__link').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile content tile', desc: 'A dark marketing tile under the hero.', sel: 'a.feature__link' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, women, plp, pdp, bag, saved, account, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
// A page counts as finished only when its runner returns without throwing and
// no bot check stopped it. Pruning touches only finished pages: a page that
// threw keeps its unreached components and states instead of losing them.
// A page that throws is recorded as broken and the run goes on; the exit
// status at the end is nonzero when any page threw (run-pages.mjs).
const { finished, broken, runPage } = pageRunner(() => current, log);
const pageDone = (c) => finished.has(c.page) && !broken.has(c.page) && !blockedPages.has(c.page);
try {
  for (const k of order) { if (k !== 'mobile') await runPage(plan[k]); }
  if (!pages.length || pages.includes('home')) await runPage(footer);
  if (!pages.length || pages.includes('mobile')) await runPage(plan.mobile);
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key)) { if (!pages.length && pageDone(c)) delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want && pageDone(c)) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log(broken.size ? 'incomplete ->' : 'done ->', OUT);
process.exitCode = exitStatus(broken);
