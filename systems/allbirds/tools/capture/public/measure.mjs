// Measures Allbirds' components on its public pages, in every state that can
// be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: geo home collection product cartdrawer search account mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open           a resting state reached by a UI toggle (accordion, drawer, menu)
//   anything else  a resting state reached by the page itself
// Nothing is sent, bought or signed into: the only presses are the geo dialog's
// US choice, the MEN mega-menu button, a size chip, the header cart button and
// accordions. Add to Cart is measured at rest and never pressed: it writes a
// cart on the store's server (state change: recorded as a boundary).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  collection: '/collections/mens',
  product: '/products/mens-tree-runner-nz-medium-grey',
  search: '/search',
  account: '/account/login',
  help: '/pages/help',
};

let page, cdp, current, context, contextMobile, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  if (!contextMobile) {
    const b = context.browser();
    contextMobile = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  }
  const ctx = mobile ? contextMobile : context;
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait, promo });
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
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

// Clicks a UI toggle (accordion, menu, drawer). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|start free trial|upgrade|open)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'runner size 8.5';

// Transitions and animations declared in every readable sheet, by selector.
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

// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', collection: 'Collection grid', product: 'Product page',
  overlay: 'Dialogs and overlays', cart: 'Cart drawer', form: 'Forms', mobile: 'Mobile (390 wide)',
};

// The geofencing dialog, kept open on purpose (promo: 'keep').
async function geo() {
  await newPage('home', { promo: 'keep', wait: 10000 });
  const dlg = q('[id*="geofencing"] [role="dialog"], [id*="geofencing"] [class*="modal" i], [id*="geofencing"] > div > div').filter({ visible: true }).last();
  const has = await page.locator('[id*="geofencing"]').filter({ visible: true }).count();
  if (!has) { log('  geo dialog did not mount; skipping'); await page.close(); return; }
  const g = G.overlay;
  const box = page.locator('[id*="geofencing"]').filter({ visible: true }).first();
  await S('geo-dialog', box, ['default'], { group: g, title: 'Region dialog', desc: 'The Shopify geofencing prompt every first visit opens with: a centred white card asking "Where are we shipping to?" over a bg-black/50 overlay, with US and SG flag buttons and a round close.', sel: '[id*="geofencing"]' }, { noScroll: true });
  await S('geo-title', box.locator('h1, h2, [class*="title" i], :has-text("Where are we shipping")').filter({ visible: true }).first(), ['default'], { group: g, title: 'Region dialog title', sel: '[id*="geofencing"] heading' }, { noScroll: true });
  const us = box.locator('button:has-text("US")').filter({ visible: true }).first();
  await S('geo-choice', us, ['default', 'hover'], { group: g, title: 'Region choice button', desc: 'A flag card for the shipping region. The US one was clicked to dismiss; the SG one was never pressed.', sel: '[id*="geofencing"] button' }, { noScroll: true });
  await S('geo-close', box.locator('button:has-text("Close"), [class*="close" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Region dialog close', sel: '[id*="geofencing"] close' }, { noScroll: true });
  out._meta.geoBackdrop = await page.evaluate(() => {
    const res = [];
    for (const n of document.querySelectorAll('[id*="geofencing"] *')) {
      const c = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width > 1200 && c.backgroundColor !== 'rgba(0, 0, 0, 0)') res.push({ node: n.tagName.toLowerCase() + '.' + String(n.className).slice(0, 60), bg: c.backgroundColor, backdrop: c.backdropFilter });
    }
    return res;
  });
  await killGeo(page);
  await page.close();
}

async function home() {
  await newPage('home');
  await sheetsFor('home');
  const g = G.shell;
  const bar = q('.swiper').filter({ hasText: /shipping|demand|orders/i }).filter({ visible: true }).first();
  await S('promo-bar', bar, ['default'], { group: g, title: 'Announcement bar', desc: 'The rotating strip above the header ("Free ground shipping on orders over $100", shipping-delay notices): black fill, centred xs copy, prev/next chevrons at the ends (a Swiper carousel).', sel: '.swiper top bar' }, { noScroll: true });
  await S('promo-bar-next', bar.locator('.swiper-next-button, button').filter({ visible: true }).last(), ['default', 'hover'], { group: g, title: 'Announcement bar arrow', sel: '.swiper-next-button' }, { noScroll: true });
  await page.waitForSelector('a[href*="shop-all"], button:has-text("MEN")', { state: 'attached', timeout: 20000 }).catch(() => {});
  const men = await domFind(page, /^MEN$/, { tag: 'men' });
  const header = await domFind(page, /^MEN$/, { tag: 'hdr', up: '[class*="rounded"]' });
  await S('header', header, ['default'], { group: g, title: 'Header', desc: 'The sticky rounded bar: wordmark centre-left, text links NEW ARRIVALS and SHOP ALL, the MEN and WOMEN mega-menu buttons, a Search link and the cart button with its count badge.', sel: 'nav pill bar' }, { noScroll: true });
  await S('nav-link', q('a[href*="shop-all"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A text nav item: xs, medium, tracking-wider, uppercase.', sel: 'nav a' }, { noScroll: true });
  await S('nav-menu-button', men, ['default', 'hover', 'pressed'], { group: g, title: 'Mega-menu button', desc: 'MEN/WOMEN open the mega-menu flyout on hover; measured, also hovered once for the flyout crop.', sel: 'nav button' }, { noScroll: true });
  await S('mega-menu', q('div:has(> a[href*="/collections/mens-"]), [class*="dropdown" i], [class*="submenu" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu flyout', desc: 'The panel under MEN: category links and colour/material rows of circular swatches.', sel: 'mega menu flyout' }, { noScroll: true, open: async () => { await men.hover().catch(() => {}); await page.waitForTimeout(1500); } });
  await S('cart-button', q('button[aria-label*="cart" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart button', desc: 'The bag icon with the count badge on top; opens the cart drawer.', sel: 'nav cart button' }, { noScroll: true });
  await S('search-link', q('a[href*="/search"]').filter({ visible: true }).first(), B4, { group: g, title: 'Search link', desc: 'The magnifier nav item; navigates to /search.', sel: 'nav a[href*=search]' }, { noScroll: true });

  const h = G.home;
  await S('hero', q('h1').filter({ visible: true }).first().locator('xpath=ancestor::*[self::section or contains(@class,"rounded")][1]'), ['default'], { group: h, title: 'Hero', desc: 'The first band: a rounded-corner photo card carrying the "Wildly Comfortable. Super Natural." headline and the two pill CTAs.', sel: 'hero container' }, { noScroll: true });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: 'The home hero headline: it renders in Geograph (24px/32px, 0.6px tracking), not the brand serif.', sel: 'h1' }, { noScroll: true });
  await S('cta-primary', q('a.btn.btn-primary').filter({ visible: true }).first(), B4, { group: h, title: 'Primary button', desc: '.btn.btn-primary: the white pill CTA ("SHOP MEN"), xs medium uppercase tracking-wider.', sel: 'a.btn.btn-primary' }, { noScroll: true });
  await S('cta-outline-white', q('a.btn.btn-outline-white').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Outline button', desc: '.btn.btn-outline-white: the bordered pill used on category cards.', sel: 'a.btn.btn-outline-white' }, { noScroll: true });
  await S('section-title', q('h2.font-serif').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'Marketing section headline in the brand serif, fluid 30-40px.', sel: 'h2.font-serif' });
  await S('carousel-nav', q('.swiper-prev-button, .swiper-next-button').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Carousel arrow', desc: 'A 24-40px round icon button at the edge of a product/media carousel.', sel: '.swiper-prev-button' });
  const f = G.form;
  const email = q('footer input[type="email"], footer input[name*="email" i]').filter({ visible: true }).first();
  await S('email-input', email, ['default', 'focused', 'filled'], { group: f, title: 'Email field', desc: 'The footer subscribe field. Text was typed and deleted; never submitted.', sel: 'footer input[type=email]' }, { fillText: 'name@example.com' });
  await S('signup-button', q('button[type="submit"]').filter({ hasText: /sign up/i }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: f, title: 'Sign Up button', desc: '.btn.btn-outline on the subscribe row. Measured, never submitted.', sel: 'footer button[type=submit]' });
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The black footer: subscribe row, HELP/SHOP/COMPANY link columns, legal links, the OneTrust "Do Not Sell" settings button.', sel: 'footer' });
  await page.close();
}

async function collection() {
  await newPage('collection');
  await sheetsFor('collection');
  const g = G.collection;
  await S('collection-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Collection title', desc: 'The collection page heading.', sel: 'h1' });
  await S('filter-button', page.getByRole('button', { name: /filter/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter button', desc: 'Opens the filter/sort sheet; labelled with the product count. The sheet itself is the filter-sheet component.', sel: 'button filter' });
  if (!(await domClick(page, /filter/i))) log('  filter button not found this load');
  await page.waitForTimeout(1500);
  const sheet = await domFind(page, /filter|size|price|colour|color/i, { sel: '.z-takeover, [role="dialog"], [class*="fixed"]', tag: 'fsh', leaf: false, minW: 200, minH: 200 });
  await S('filter-sheet', sheet, ['open'], { group: g, title: 'Filter sheet', desc: 'The panel the Filter button opens: size/price/colour groups with checkboxes.', sel: 'filter sheet' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  const card = q('a[href*="/products/"].flex.h-full.flex-col, a[href*="/products/"][class*="flex-col"]').filter({ visible: true }).first();
  await S('product-card', card, ['default', 'hover'], { group: g, title: 'Product card', desc: 'A grid card: rounded-2xl photo, name, colour name, price; hover swaps in the second photo (opacity fade on a z-[1] image).', sel: 'a[href*=/products/] card' });
  await S('card-image', q('a[href*="/products/"] img').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card photo', sel: 'card img' });
  await S('more-colors', q('a[href*="/products/"]').filter({ hasText: /\+\d+/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'More colours link', desc: 'The "+6" under a card: xs medium underline, points at the product page.', sel: 'card +N link' });
  await page.close();
}

async function product() {
  await newPage('product', { wait: 8000 });
  // the buy box hydrates late (geo resolution re-renders it); give it a window
  await page.waitForSelector('button.btn-size', { state: 'attached', timeout: 20000 }).catch(() => {});
  await killGeo(page);
  await sheetsFor('product');
  const g = G.product;
  await S('pdp-title', q('h1.font-serif').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: '"Men\'s Tree Runner NZ" in the brand serif.', sel: 'h1.font-serif' });
  await S('pdp-price', q('main *:not(:has(*)):has-text("$")').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', sel: 'pdp $ leaf' });
  const sw = q('.swatch-group').filter({ visible: true }).first();
  await S('swatch-group', sw, ['default'], { group: g, title: 'Swatch group', desc: 'The colour picker: rows of circular swatches (uppercase group labels like "JERSEY", "STRIPE").', sel: '.swatch-group' });
  await S('swatch', sw.locator('button, a, [role="radio"], [class*="swatch" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Swatch', desc: 'One colour circle; the selected one carries a ring.', sel: 'swatch' });
  // Exact labels: /SIZES/ matched both tabs and the same WOMEN'S tab was read twice.
  await S('size-tab-active', await domFind(page, /^MEN'S SIZES$/i, { tag: 'tab0' }), ['default'], { group: g, title: 'Size tab, active', desc: 'The underlined "MEN\'S SIZES" tab of the men/women size-grid switch.', sel: 'size tab' });
  await S('size-tab', await domFind(page, /^WOMEN'S SIZES$/i, { tag: 'tab1' }), ['default', 'hover'], { group: g, title: 'Size tab', desc: 'The inactive tab: light-charcoal, transparent border.', sel: 'size tab' });
  const chipOn = q('button.btn-size:not(.disabled)').filter({ visible: true }).first();
  await S('size-button', chipOn, ['default', 'hover', 'pressed'], { group: g, title: 'Size button', desc: '.btn-size: the bordered size chip, measured before any chip is picked (no selected state was read).', sel: 'button.btn-size' });
  await S('size-button-disabled', q('button.btn-size.disabled').filter({ visible: true }).first(), ['default'], { group: g, title: 'Size button, sold out', desc: '.btn-size.disabled: the struck-through greyed chip.', sel: 'button.btn-size.disabled' });
  await S('fit-guide', q('button, a').filter({ hasText: /fit guide/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Fit Guide link', desc: 'The underlined text button under the size grid.', sel: 'fit guide' });
  // pick a size so the ATC button mounts, then measure it
  await chipOn.click().catch(() => chipOn.evaluate((el) => el.click())).catch(() => {});
  await page.waitForTimeout(800);
  const atc = q('button:has-text("ADD TO CART"), button:has-text("Add to Cart"), button:has-text("ADD TO BAG")').filter({ visible: true }).first();
  await S('atc-button', atc, B4, { group: g, title: 'Add to Cart button', desc: '.btn.btn-secondary: the full-width black pill under the buy box ("ADD TO CART - $100"). Mounted once a size is picked; measured at rest, never pressed.', sel: 'btn-secondary ATC' });
  const acc = q('button[aria-expanded]').filter({ hasText: /WHY WE LOVE THIS/ }).filter({ visible: true }).first();
  // open last: nothing collapses the row, so a state after it would be read on the expanded row
  await S('accordion', acc, ['default', 'hover', 'open'], { group: g, title: 'Accordion row', desc: 'A PDP details row (WHY WE LOVE THIS, MATERIALS & SUSTAINABILITY, CARE INSTRUCTIONS): full-width, py-6, plus/minus on the right.', sel: 'button[aria-expanded]' }, { before: { open: async (loc) => { if ((await loc.getAttribute('aria-expanded')) === 'false') { await toggle(loc); await page.waitForTimeout(600); } return 'accordion opened'; } } });
  await S('tooltip-pill', await domFind(page, /./, { sel: 'button.inline-flex.cursor-pointer', tag: 'pill', minW: 100 }), ['default', 'hover'], { group: g, title: 'Tooltip pill', desc: 'The black pill over the gallery (e.g. "Tree-based upper for lightweight comfort") that opens a material tooltip.', sel: 'tooltip pill' });
  // cart drawer via ATC (DOM-side click: the buy box re-renders, so a locator
  // resolved earlier can be detached); falls back to the header cart button.
  // killGeo only: the cart drawer itself matches closePromo's dialog patterns.
  await killGeo(page);
  // the closed drawer sits translated off-canvas, so check on-screen position
  const drOpen = () => page.evaluate(() => {
    const d = [...document.querySelectorAll('.z-takeover')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 300 && r.height > 300 && r.left < innerWidth - 100 && /CART/.test(n.innerText || '');
    });
    return !!d;
  }).catch(() => false);
  for (let attempt = 0; attempt < 4; attempt++) {
    if (await drOpen()) break;
    // ATC stays disabled until an in-stock size is picked; the grid hydrates
    // late, so wait for an enabled chip and fall back to any size.
    await page.waitForSelector('button.btn-size:not(.disabled)', { state: 'attached', timeout: 10000 }).catch(() => {});
    const picked = await domClick(page, /^8\.5$/, 'button.btn-size:not(.disabled)') || await domClick(page, /^\d+(\.\d+)?$/, 'button.btn-size:not(.disabled)');
    await page.waitForTimeout(1200);
    // the header cart button opens the (empty) drawer; Add to Cart is never pressed
    const hit = await domClick(page, /^0$|view cart/i, 'button');
    if (!hit) log('  cart open attempt', attempt, 'no target', picked ? '' : '(size pick also missed)');
    await page.waitForTimeout(3000);
  }
  if (!(await drOpen().catch(() => false))) {
    const zs = await page.locator('.z-takeover').all();
    for (const z of zs) log('   z-takeover:', (await z.evaluate((n) => n.getBoundingClientRect().width + 'x' + n.getBoundingClientRect().height + ' ' + (n.innerText || '').slice(0, 40)).catch(() => '?')).trim());
  }
  const c = G.cart;
  const dr = await domFind(page, /CART/, { sel: '.z-takeover', tag: 'cdr', leaf: false, minW: 300, minH: 300 });
  await S('cart-drawer', dr, ['open'], { group: c, title: 'Cart drawer', desc: 'The right-hand .z-takeover drawer opened from the header cart button, with an empty cart: the CART heading and whatever the empty state shows. Add to Cart is never pressed, so no item rows, subtotal or checkout buttons.', sel: '.z-takeover cart' }, { noScroll: true });
  await S('cart-qty', await domFind(page, /^[+−-]$/, { sel: '.z-takeover button', tag: 'qty' }), ['default'], { group: c, title: 'Quantity stepper', desc: 'The +/- stepper on a cart row.', sel: 'qty button' }, { noScroll: true });
  await S('cart-upsell-card', await domFind(page, /Add\+/, { sel: '.z-takeover a, .z-takeover button', tag: 'ups', up: 'li, [class*="card" i], [class*="upsell" i], [class*="item" i]' }), ['default'], { group: c, title: 'Upsell card', desc: 'RECOMMENDED FOR YOU carousel cards with a size select and an "Add+" link.', sel: '.cart-upsells' }, { noScroll: true });
  // the checkout bar may sit outside the .z-takeover scroll root or inside a
  // shadow root (Playwright locators pierce shadow DOM; querySelectorAll does
  // not); the "Checkout+" pill is the wide one.
  await page.waitForTimeout(1500);
  await S('checkout-button', q('a, button, [role="button"], [class*="checkout" i]').filter({ hasText: /^checkout/i }).filter({ visible: true }).last(), ['default'], { group: c, title: 'Checkout button', desc: 'The black "Checkout+ | $104.98" pill in the cart drawer footer. Rendered by Shopify\'s checkout surface (shadow DOM / iframe): visible in the drawer crop but not introspectable from the page DOM, so no computed style was recorded. Never pressed.', sel: 'checkout button' }, { noScroll: true });
  await S('express-button', q('iframe, [class*="express" i], [class*="wallet" i], [class*="payment" i], [class*="additional-checkout" i], [class*="dynamic-checkout" i]').filter({ visible: true }).last(), ['default'], { group: c, title: 'Express pay buttons', desc: 'The Amazon Pay / G Pay / PayPal / Shop Pay wallet row under checkout. Shopify-hosted (iframes/shadow): visible in the drawer crop, not introspectable from the page DOM, so no computed style was recorded.', sel: 'express row' }, { noScroll: true });
  await page.close();
}

async function search() {
  await newPage('search');
  const f = G.form;
  const input = q('input[type="search"], input[name="q"], main input[type="text"], [class*="search" i] input').filter({ visible: true }).first();
  await S('search-input', input, ['default', 'focused', 'filled'], { group: f, title: 'Search field', desc: 'The /search page field. Text was typed and deleted; never submitted.', sel: 'search input' }, { fillText: 'wool runner' });
  await S('search-submit', q('button[type="submit"], button[aria-label*="search" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: f, title: 'Search submit', desc: 'Measured, never pressed.', sel: 'search submit' });
  await page.close();
}

async function account() {
  await newPage('account');
  const f = G.form;
  await S('login-input', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: f, title: 'Login email field', desc: 'The account sign-in field on the public login page. Text was typed and deleted; never submitted.', sel: 'input[type=email]' }, { fillText: 'name@example.com' });
  await S('login-submit', q('main button[type="submit"], button:has-text("Submit"), button:has-text("Continue")').filter({ visible: true }).last(), ['default', 'hover'], { group: f, title: 'Sign-in button', desc: 'Measured, never pressed; signing in was out of scope. The account page is Shopify-hosted (Shop account UI).', sel: 'login submit' });
  await page.close();
}

async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  await S('m-header', q('.shopify-section-group-header-group > div.relative, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The rounded pill bar: hamburger, wordmark, search and bag icons.', sel: 'mobile header' }, { noScroll: true });
  const ham = q('button[aria-label*="menu" i], button.header-mobile-menu, .header-mobile-menu button').filter({ visible: true }).first();
  await S('m-hamburger', ham, ['default', 'pressed'], { group: g, title: 'Hamburger button', desc: 'Opens the mobile menu drawer.', sel: 'mobile menu button' }, { noScroll: true });
  await S('m-menu-drawer', q('.header-mobile-menu').filter({ visible: true }).first(), ['open'], { group: g, title: 'Mobile menu drawer', desc: 'The sheet the hamburger opens: NEW ARRIVALS / SHOP ALL text rows, MEN and WOMEN with chevrons, and a footer of category links.', sel: '.header-mobile-menu' }, { noScroll: true, open: async () => { if (await ham.count()) { await toggle(ham); await page.waitForTimeout(1500); } } });
  await S('m-ai-chip', q('button, [role="button"]').filter({ hasText: /shop with ai|shop best sellers/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop with AI chip', desc: 'The floating pill bottom-right: spark icon, label, close X. Never opened.', sel: 'ai chip' }, { noScroll: true });
  await page.close();
}

const RUNNERS = { geo, home, collection, product, search, account, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'allbirds.com (Shopify)';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter((s) => s && s !== 'all');
({ context } = await launch());
for (const [k, fn] of Object.entries(RUNNERS)) {
  if (wanted.length && !wanted.includes(k)) continue;
  try { await fn(); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  save();
}
// mark components from this run whose selectors matched nothing; a component
// with recorded states (from an earlier merged run) is covered, not missing
for (const [k, c] of Object.entries(out.components)) {
  if (!touched.has(k)) continue;
  if (Object.keys(c.states || {}).length) delete c.missing;
  else c.missing = true;
}
save();
log('done ->', OUT);
await context.browser().close();
