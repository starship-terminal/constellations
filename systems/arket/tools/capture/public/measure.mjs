// Measures arket.com's public components in every state reachable without
// buying, sending, submitting or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: dialogs home clothing service account mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// arket.com is a Next.js + Tailwind v4 storefront in one light theme, run in
// headed real Chrome (Akamai blocks headless Chromium with "Access Denied"
// and blocks every /en-ww/product/<slug>-<id>/ URL — the PDP is a boundary,
// so product values come from the listing cards). Components are found by
// role and stable text: the classes are Tailwind utilities. Nothing is
// bought, sent, submitted or signed into: the only presses are local UI
// toggles — the header search and cart drawers, the mobile menu, the PLP
// filter and a card colour swatch. The cookie-consent popup and the
// "Please confirm your location" dialog are measured as they arrive, then
// hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
// Akamai answers /en-ww/ itself with "Access Denied" for this client (every
// other route passes), so the shell, dialogs and footer are measured on the
// /en-ww/women/ landing, which carries the same chrome.
const URLS = { home: '/en-ww/women/', clothing: '/en-ww/women/clothing/', service: '/en-ww/customer-service/', account: '/en-ww/account/' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
const reached = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close' } = {}) {
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
  if (!(await open(page, BASE + URLS[key], { wait, promo }))) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  reached.add(mobile ? '@' + key : key);
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
  // Found again: a retry's fresh readings replace the earlier miss record, so
  // the token builder stops rejecting them.
  delete out.components[key].recaptureMissed;
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
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        await toggle(loc, { allowLink: true });
        await page.waitForTimeout(500);
        via = 'own toggle, pressed once; a local UI state, never submitted';
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

// Clicks a UI toggle (drawer, accordion, menu). Refuses a submit button and
// any control whose text names a purchase, consent or location answer this
// kit must never take.
const NEVER = /^(accept all|only required cookies|continue to|stay in|send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|shop now|read more)$/i;
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
  dialogs: 'Consent and location dialogs', shell: 'Shell and navigation', home: 'Home',
  plp: 'Listing page', service: 'Customer service', account: 'Account gate',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// The two auto-mounted overlays, measured as the page arrives, before
// closePromo hides them. Nothing inside either is ever pressed.
async function dialogs() {
  if (!(await newPage('home', { wait: 9000, promo: 'keep' }))) return;
  const g = G.dialogs;
  const consent = q('.cookie-consent-popup').first();
  await S('consent-card', consent, ['default'], { group: g, title: 'Cookie consent card', desc: '"Before you start shopping": the consent card measured as it arrives, never answered.', sel: '.cookie-consent-popup' });
  await S('consent-accept', consent.locator('button').filter({ hasText: /Accept all/ }).first(), B4, { group: g, title: 'Accept all button', desc: 'The consent primary. Measured, never pressed.', sel: '.cookie-consent-popup button' });
  await S('consent-required', consent.locator('button').filter({ hasText: /Only required cookies/ }).first(), B4, { group: g, title: 'Only required cookies button', desc: 'The consent secondary. Measured, never pressed.', sel: '.cookie-consent-popup button' });
  await S('consent-settings-link', consent.locator('button, a').filter({ hasText: /settings/i }).first(), B4, { group: g, title: 'Cookie settings link', desc: 'The text link to the settings panel. Measured, never pressed.', sel: 'consent settings link' });
  const loc = q('dialog').filter({ hasText: /confirm your location/ }).first();
  await S('location-dialog', loc, ['default'], { group: g, title: 'Location dialog', desc: '"Please confirm your location", the auto-mounted <dialog>. Measured, never answered.', sel: 'dialog:has-text("confirm your location")' });
  await S('location-search', loc.locator('input').first(), ['default', 'focused'], { group: g, title: 'Country search field', desc: 'The "Search country" input; focused only, nothing typed.', sel: 'location dialog input' });
  await S('location-continue', loc.locator('button, a').filter({ hasText: /Continue to/ }).first(), B4, { group: g, title: 'Continue to country button', desc: 'The black confirm action. Measured, never pressed.', sel: 'Continue to <country>' });
  await S('location-stay', loc.locator('button, a').filter({ hasText: /Stay in/ }).first(), B4, { group: g, title: 'Stay in country button', desc: 'The outlined alternative. Measured, never pressed.', sel: 'Stay in <country>' });
  await S('location-row', loc.locator('button, a, li').filter({ hasText: /^Australia/ }).first(), ['default', 'hover'], { group: g, title: 'Country row', desc: 'A country/currency row in the list. Measured, never pressed.', sel: 'country row' });
  save();
}

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('locale-notice', await domFind(page, /Location and language/, { sel: 'div, section', tag: 'ln', minW: 200, minH: 20 }), ['default'], { group: g, title: 'Locale notice bar', desc: 'The top "Location and language: <country>/<lang>" strip with Change and Close.', sel: 'locale notice strip' }, { noScroll: true });
  await S('promo-strip', await domFind(page, /Everyday beauty|gift shop/i, { sel: 'section, a', tag: 'ps', minW: 200, minH: 20, leaf: false }), ['default'], { group: g, title: 'Promo strip', desc: 'The thin promo line under the notice bar.', sel: 'promo strip section' }, { noScroll: true });
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The sticky z-header bar: wordmark, search field, account, wishlist, cart.', sel: 'header' }, { noScroll: true });
  await S('logo', q('a').filter({ hasText: /^ARKET$/ }).first(), ['default'], { group: g, title: 'Logo', sel: 'a:has-text("ARKET")' }, { noScroll: true });
  await S('nav-item', q('button').filter({ hasText: /^Women$/ }).first(), B4, { group: g, title: 'Nav item', desc: 'A top-level shop category button; opens the nav drawer at that section.', sel: 'nav button "Women"' }, { noScroll: true });
  await S('search-field', q('header input, input[placeholder*="earch" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The header search input; focused only, nothing typed or sent.', sel: 'header input' }, { noScroll: true });
  await S('account-button', q('button').filter({ hasText: /^My account$/ }).first(), B4, { group: g, title: 'Account button', desc: 'The account icon button. Measured, never followed.', sel: 'button:has-text("My account")' }, { noScroll: true });
  await S('wishlist-link', q('a[aria-label*="wishlist" i], a:has-text("Wishlist")').filter({ visible: true }).first(), B4, { group: g, title: 'Wishlist link', desc: 'The wishlist icon link. Measured, never followed.', sel: 'a:has-text("Wishlist")' }, { noScroll: true });
  await S('cart-button', q('button[aria-label*="cart" i], button:has-text("Cart")').filter({ visible: true }).first(), B4, { group: g, title: 'Cart button', desc: 'The bag icon button; opens the cart drawer.', sel: 'button:has-text("Cart")' }, { noScroll: true });
  await S('locale-button', q('button:has-text("| EN"), button[aria-label*="language" i], button[aria-label*="region" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Locale button', desc: 'The "AR | EN" region/language button. Measured, never pressed.', sel: 'locale button' }, { noScroll: true });
  await S('cafe-link', q('a').filter({ hasText: /ARKET CAFÉ/ }).first(), B4, { group: g, title: 'ARKET CAFÉ link', desc: 'The café utility link. Measured, never followed.', sel: 'a:has-text("ARKET CAFÉ")' }, { noScroll: true });
  await S('service-link', q('a').filter({ hasText: /^Customer service$/ }).first(), B4, { group: g, title: 'Customer service link', sel: 'a:has-text("Customer service")' }, { noScroll: true });

  // The bag drawer, opened by its own icon; the signed-out bag is empty.
  const cartBtn = q('button[aria-label*="cart" i], button:has-text("Cart")').filter({ visible: true }).first();
  await S('cart-drawer', q('dialog').filter({ visible: true }).last(), ['default'], { group: g, title: 'Cart drawer, empty', desc: 'The bag drawer after its own icon press; the signed-out bag is empty.', sel: 'dialog' }, { noScroll: true, open: async () => { await cartBtn.click().catch(() => cartBtn.evaluate((el) => el.click())); await page.waitForTimeout(1600); } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(700);

  const h = G.home;
  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  await S('hero-title', q('main h1, main h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', sel: 'first main h1/h2' });
  const tile = q('main a').filter({ has: q('img') }).filter({ visible: true }).first();
  await S('tile-card', tile, ['default', 'hover'], { group: h, title: 'Campaign tile', desc: 'A hero/editorial image tile link (the whole tile is the link).', sel: 'main a:has(img)' });
  await S('tile-label', q('main a h2, main a h3, main a p').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Tile label', desc: 'The text on a campaign tile.', sel: 'inside campaign tile' });
  await S('section-title', q('h2, h3').filter({ hasText: /Discover more|Editorial/ }).first(), ['default'], { group: h, title: 'Section heading', sel: 'h2/h3' });
  save();
}

async function clothing() {
  if (!(await newPage('clothing', { wait: 9000 }))) return;
  const g = G.plp;
  await S('plp-title', q('h1').first(), ['default'], { group: g, title: 'Category title', desc: '"Women\'s clothes" h1.', sel: 'h1' }, { noScroll: true });
  // the breadcrumb itself: a bare nav/ol match caught the main category nav
  await S('breadcrumb', q('nav[aria-label*="breadcrumb" i], [class*="breadcrumb" i]').filter({ hasText: /Women.*Clothing|Clothing.*Women/s }).first(), ['default'], { group: g, title: 'Breadcrumb', desc: 'The ARKET / Women / Clothing trail.', sel: 'breadcrumb' }, { noScroll: true });
  await S('read-more', q('button').filter({ hasText: /^Read more/ }).first(), B4, { group: g, title: 'Read more button', desc: 'The category intro expander; a local toggle, measured closed.', sel: 'button:has-text("Read more")' }, { noScroll: true });
  await S('filter-button', q('button').filter({ hasText: /^Filter$/ }).first(), B4, { group: g, title: 'Filter button', desc: 'Opens the filter panel. Measured, never applied.', sel: 'button:has-text("Filter")' });
  const filterBtn = q('button').filter({ hasText: /^Filter$/ }).filter({ visible: true }).first();
  await S('filter-panel', q('dialog, aside, [role="dialog"]').filter({ visible: true }).last(), ['default'], { group: g, title: 'Filter panel, open', desc: 'The filter sheet after the Filter button\'s own press; nothing inside was applied.', sel: 'filter dialog' }, { open: async () => { await filterBtn.scrollIntoViewIfNeeded(); await filterBtn.click().catch(() => filterBtn.evaluate((el) => el.click())); await page.waitForTimeout(1500); } });
  await S('filter-option', q('dialog, [role="dialog"], aside').last().locator('li, label, button, a, [role="checkbox"]').filter({ hasText: /\w{2,}/ }).filter({ visible: true }).nth(2), B4, { group: g, title: 'Filter option', desc: 'A filter facet row inside the open panel; measured, never selected.', sel: 'filter facet' });
  await page.keyboard.press('Escape'); await page.waitForTimeout(700);
  await S('sort-button', q('button').filter({ hasText: /^Sort by$/ }).first(), B4, { group: g, title: 'Sort button', desc: 'The sort control. Measured, never opened.', sel: 'button:has-text("Sort by")' });
  await S('view-button', q('button').filter({ hasText: /^View$/ }).first(), B4, { group: g, title: 'View button', desc: 'The grid-density control. Measured, never pressed.', sel: 'button:has-text("View")' });
  const card = q('a.block.text-center, a[class*="text-center"]').filter({ hasText: /\$\s*\d/ }).first();
  await S('product-card', card, ['default', 'hover'], { group: g, title: 'Product card', desc: 'A listing card: image, name, price, "+N" colours.', sel: 'a.text-center product card' });
  await S('card-badge', q('a').filter({ hasText: /^New$/ }).first(), ['default'], { group: g, title: 'New badge', desc: 'The "New" tag on a card image.', sel: 'badge a' });
  await S('product-name', card, ['default'], { group: g, title: 'Product name', desc: 'The card text block: name, price, colour count.', sel: 'card text block' }, { cropLoc: card });
  await S('price', await domFind(page, /\$\s*\d/, { sel: 'a span, a div, span', tag: 'price', minW: 8 }), ['default'], { group: g, title: 'Price', desc: 'The "$ 349" price text inside a card.', sel: 'card price text' });
  await S('more-colors', await domFind(page, /^\+\d+$/, { sel: 'span, div, a', tag: 'mc', minW: 8 }), ['default'], { group: g, title: 'More colours chip', desc: 'The "+2" colour count.', sel: '"+N" chip' });
  // The card quick-add and carousel controls live in the image overlay and
  // only appear while the card is hovered: measure them under a real hover
  // of the card's image link, labelled as that state.
  // The overlay only shows while the <article> card cell is :hover'd; a
  // real pointer move does not trigger it (the reveal watches a deeper
  // child), so the card is held in :hover with CDP like every other
  // pseudo state here.
  const cardCell = q('article').filter({ has: q('button[aria-label*="add to bag" i]') }).first();
  let cardUndo;
  const hoverCard = async () => { await cardCell.scrollIntoViewIfNeeded().catch(() => {}); cardUndo = await forcePseudo(cardCell, ['hover']); await page.waitForTimeout(300); return 'CDP forcePseudoState :hover on the card cell'; };
  const releaseCard = async () => { if (cardUndo) await cardUndo().catch(() => {}); cardUndo = null; };
  await S('card-add-bag', q('button[aria-label*="add to bag" i], button:has-text("Add to bag")').first(), ['default', 'hover'], { group: g, title: 'Quick add-to-bag', desc: 'The card\'s quick-add control, shown only while the card image is hovered. Measured, never pressed.', sel: 'button:has-text("Add to bag")' }, { open: hoverCard, after: { default: releaseCard, hover: releaseCard } });
  await S('card-wishlist', q('button[aria-label*="wishlist" i], button:has-text("Add to wishlist")').first(), ['default', 'hover'], { group: g, title: 'Card wishlist button', desc: 'The heart quick-toggle, shown on card hover. Measured, never pressed.', sel: 'button:has-text("Add to wishlist")' }, { open: hoverCard, after: { default: releaseCard, hover: releaseCard } });
  await S('card-img-prev', q('button[aria-label*="previous image" i], button:has-text("Previous image")').first(), ['default', 'hover'], { group: g, title: 'Card image previous', desc: 'The card image carousel arrow, shown on card hover.', sel: 'button:has-text("Previous image")' }, { open: hoverCard, after: { default: releaseCard, hover: releaseCard } });
  await S('card-img-next', q('button[aria-label*="next image" i], button:has-text("Next image")').first(), ['default', 'hover'], { group: g, title: 'Card image next', desc: 'The card image carousel arrow, shown on card hover.', sel: 'button:has-text("Next image")' }, { open: hoverCard, after: { default: releaseCard, hover: releaseCard } });
  save();
}

async function service() {
  if (!(await newPage('service'))) return;
  const g = G.service;
  await S('service-title', q('main h1, main h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Service title', sel: 'main h1/h2' }, { noScroll: true });
  const acc = q('main button[aria-expanded], main summary, main details summary').filter({ hasText: /\w{5,}/ }).filter({ visible: true }).first();
  await S('service-accordion', acc, B4, { group: g, title: 'Service accordion', desc: 'A help-topic disclosure row.', sel: 'main disclosure' });
  await S('service-accordion-open', acc, ['opened'], { group: g, title: 'Service accordion, open', desc: 'The same row after its own toggle.', sel: 'main disclosure' }, { cropLoc: acc.locator('xpath=ancestor::*[self::details or self::section or self::div][1]') });
  // its own key: 'service-link' is the home page's Customer service link
  await S('service-page-link', q('main a').filter({ hasText: /\w{4,}/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Service link', sel: 'main a' });
  save();
}

async function account() {
  if (!(await newPage('account'))) return;
  const g = G.account;
  await S('gate-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Gate title', desc: 'The Login/Signup gate heading.', sel: 'h1/h2' });
  await S('gate-field', q('input[type="email"], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The sign-in email input; focused only, nothing typed or sent.', sel: 'account input' });
  // the gate's own Continue: the first labelled button was "with Google"
  await S('gate-continue', q('button').filter({ hasText: /^\s*continue\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The gate\'s primary action. Measured, never pressed — no sign-in was attempted.', sel: 'account button' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep the account page
  // and mislabel an account-footer reading as home's.
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const foot = q('footer').first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: 'footer' });
  await S('footer-heading', q('footer h2, footer h3').first(), ['default'], { group: g, title: 'Footer heading', sel: 'footer h2' });
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
  }
  const nl = q('footer input').filter({ visible: true }).first();
  if (await nl.count()) await S('newsletter-field', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; nothing was typed or submitted.', sel: 'footer input' });
  const social = q('footer a[href*="instagram"], footer a[href*="facebook"], footer a[aria-label*="Instagram" i]').filter({ visible: true }).first();
  if (await social.count()) await S('footer-social', social, B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('button[aria-label="menu" i], button:has-text("menu")').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'button[aria-label="menu"]' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The bar after its own toggle; the crop is the opened drawer that holds the links and actions.', sel: 'button[aria-label="menu"]' }, { cropLoc: q('dialog').filter({ visible: true }).last(), pad: 0 });
  const mLink = q('a, button').filter({ hasText: /^Women$/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'Read inside the open menu.', sel: 'drawer nav item' }, { noScroll: true });
  const mSearch = q('header input, button[aria-label*="search" i], header button').filter({ visible: true }).first();
  await S('m-search', mSearch, B4, { group: g, title: 'Mobile search', desc: 'The mobile search affordance, header or drawer.', sel: 'mobile search' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { dialogs, home, clothing, service, account, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home') || pages.includes('dialogs')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune entries this run never touched only when their page was actually
    // reached: a blocked page must not erase the readings saved under it.
    const src = c.group === G.mobile ? '@' + c.page : c.page;
    if (!touched.has(key) && !pages.length && reached.has(src)) { delete out.components[key]; continue; }
    if (!Object.keys(c.states || {}).length && !c.missing && touched.has(key)) delete out.components[key];
  }
  save();
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
