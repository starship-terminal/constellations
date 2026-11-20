// Measures aloyoga.com's public components in every state reachable without
// adding to bag, joining, subscribing or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home plp pdp cart account mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// aloyoga.com is Shopify + Builder.io in one light theme; components are
// found by the semantic classes (main-nav__item, image-grid__card, SwatchUI),
// roles and stable text. Nothing is sent, added to bag, joined or subscribed:
// the only presses are local UI toggles — the mobile menu and a PDP colour
// swatch. The Osano consent dialog is hidden before every measurement, never
// answered. "Add to bag", "Sign in" and "Join" buttons are measured in all
// states except a real press.
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
const URLS = { home: '/', plp: '/collections/womens-shop-all', pdp: '/collections/womens-shop-all', cart: '/cart', account: '/account' };
let page, cdp, current, context, run;
const touched = new Set();
const blockedPages = new Set(); // pages a bot check stopped; their old readings are kept
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
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
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); blockedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] });
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order)$/i;
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
  shell: 'Shell and navigation', hero: 'Home', plp: 'Shop grid', pdp: 'Product page',
  cart: 'Cart', account: 'Account gate', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('promo-strip', q('a').filter({ hasText: /^JOIN TO SHOP$/ }).first(), ['default'], { group: g, title: 'Promo strip', desc: 'The thin bar above the header linking the current offer.', sel: 'a:has-text("JOIN TO SHOP")' }, { noScroll: true });
  await S('header', q('header, .main-navbar, nav.main-nav').first(), ['default'], { group: g, title: 'Header', desc: 'The white bar: wordmark, WOMEN/MEN/SHOES nav, search, account, bag.', sel: 'header' }, { noScroll: true });
  await S('logo', q('a[href*="/en-sg"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', sel: 'home link' }, { noScroll: true });
  await S('nav-item', q('a.main-nav__item').filter({ hasText: /WOMEN/i }), B4, { group: g, title: 'Nav item', desc: 'A top-level shop category; hover opens the mega-menu.', sel: 'a.main-nav__item' }, { noScroll: true });
  const women = q('a.main-nav__item').filter({ hasText: /WOMEN/i }).first();
  await S('nav-mega', women, ['opened'], { group: g, title: 'Mega-menu, open', desc: 'The nav item while its flyout is open; the panel shows in the crop.', sel: 'a.main-nav__item:hover' }, { noScroll: true, noReset: true, noToggle: true, open: async () => { await women.hover(); await page.waitForTimeout(1600); } });
  await page.mouse.move(700, 400); await page.waitForTimeout(500);
  await S('search-icon', q('#main-navbar-search-icon, a.main-navbar__icon--search'), B4, { group: g, title: 'Search icon', sel: '#main-navbar-search-icon' }, { noScroll: true });
  await S('account-icon', q('button.account-icon, .account-icon'), B4, { group: g, title: 'Account icon', sel: '.account-icon' }, { noScroll: true });
  await S('bag-icon', q('a.main-navbar__icon--bag, a[aria-label*="Cart" i]'), B4, { group: g, title: 'Bag icon', sel: '.main-navbar__icon--bag' }, { noScroll: true });
  await S('search-input', q('#search-keyboard-up'), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The header search input; focused only, nothing typed.', sel: '#search-keyboard-up' }, { noScroll: true });

  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  const h = G.hero;
  await S('hero-button', q('.hero-button, a.hero-button').first(), B4, { group: h, title: 'Hero button', desc: 'The filled hero CTA ("JOIN NOW"). Measured, never followed.', sel: '.hero-button' });
  await S('grid-card', q('a.image-grid__card').first(), ['default', 'hover'], { group: h, title: 'Category tile', desc: 'A shop-category image tile (NEW ARRIVALS, PANTS, ...).', sel: 'a.image-grid__card' });
  await S('grid-card-label', q('a.image-grid__card').first().locator('h2,h3,div').filter({ hasText: /\w{2,}/ }).last(), ['default'], { group: h, title: 'Tile label', sel: 'inside image-grid__card' });
  await S('carousel-cta', q('a.carousel-header__cta').first(), B4, { group: h, title: 'Carousel CTA link', desc: '"Shop Now" over a product carousel.', sel: 'a.carousel-header__cta' });
  await S('color-tile', q('a.builder-block').filter({ hasText: /FROSTED|ESPRESSO|NAVY|BLACK|IVORY|Shop/ }).first(), ['default', 'hover'], { group: h, title: 'Colour-story tile', desc: 'A Builder.io colourway block.', sel: 'a.builder-block' });
  await S('to-top', q('#toTop, a[id="toTop"], [id*="top" i][class*="top" i]').filter({ visible: true }), B4, { group: h, title: 'Back-to-top button', desc: 'The floating round return-to-top control.', sel: '#toTop' });
  save();
}

async function plp() {
  if (!(await newPage('plp'))) return;
  const g = G.plp;
  await S('plp-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Collection title', sel: 'h1' }, { noScroll: true });
  const sort = q('button, select, [role="button"], a').filter({ hasText: /sort|filter/i }).filter({ visible: true }).first();
  await S('sort-button', sort, B4, { group: g, title: 'Sort control', desc: 'The grid sort/filter trigger. Measured, never opened.', sel: 'button:has-text("Sort")' });
  const card = q('.PlpTile, [class*="PlpTile" i]').filter({ visible: true }).first();
  await S('product-tile', card, ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A grid card: image, name, price, colour swatches, member-price link.', sel: 'card containing .swatch' });
  await S('swatch', q('button.SwatchUI.swatch, button.swatch').filter({ visible: true }).first(), B4, { group: g, title: 'Colour swatch', desc: 'A product colour dot; a local selection toggle.', sel: 'button.swatch' });
  await S('swatch-selected', q('button.SwatchUI.swatch.active, button.swatch.active').first(), ['default'], { group: g, title: 'Swatch, selected', sel: 'button.swatch.active' });
  await S('product-name', q('a').filter({ hasText: /Legging|Bra|Trouser|Hoodie|Tee|Pant/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Product name link', sel: 'product name a' });
  await S('member-link', q('a').filter({ hasText: /^Join Now$/ }).first(), B4, { group: g, title: 'Member-price link', desc: '"Join Now" — the membership hook. Measured, never followed.', sel: 'a:has-text("Join Now")' });
  await S('more-colors', q('a.more-colors-icon, .more-colors-icon').first(), B4, { group: g, title: 'More colours chip', sel: '.more-colors-icon' });
  save();
}

async function pdp() {
  if (!(await newPage('pdp'))) return;
  // Walk to the first product the shop grid offers.
  const href = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a[href*="/products/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
    return a ? a.getAttribute('href') : null;
  });
  if (href) {
    await page.goto(new URL(href, 'https://www.aloyoga.com').toString(), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await page.waitForTimeout(8000);
    await closePromo(page);
    await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  }
  const g = G.pdp;
  out.components.pdp_url ??= { page: 'pdp', title: 'PDP URL', states: {} };
  out.components.pdp_url.states.default = { text: href || 'none found', via: 'first product link on /collections/womens-shop-all' };
  touched.add('pdp_url');
  await S('pdp-title', q('h1').first(), ['default'], { group: g, title: 'Product title', sel: 'h1' }, { noScroll: true });
  await S('pdp-price', q('[class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product price', sel: '[class*="price"]' }, { noScroll: true });
  await S('pdp-swatch', q('label.option-Color, [class*="option-Color" i], label[class*="swatch" i]').filter({ visible: true }).first(), B4, { group: g, title: 'PDP swatch', sel: 'button.swatch' });
  // Pin the swatch before its toggle: once clicked it gains .active, and a live
  // :not(.active) locator would re-resolve to the next unpicked swatch.
  await q('label.option-Color:not(.active), [class*="option-Color" i]:not(.active)').filter({ visible: true }).first()
    .evaluate((el) => el.setAttribute('data-m-pick', 'swatch'), null, { timeout: 5000 }).catch(() => {});
  await S('pdp-swatch-picked', q('[data-m-pick="swatch"]'), ['opened'], { group: g, title: 'PDP swatch, picked', desc: 'A colour swatch after its own toggle; never an add-to-bag.', sel: 'button.swatch' });
  const size = q('button.button-size-selector__button:not(.out-of-stock)').filter({ visible: true }).first();
  await S('size-button', size, B4, { group: g, title: 'Size button', sel: 'size option button' });
  const add = q('button.product__buy--button, button').filter({ hasText: /add to bag/i }).filter({ visible: true }).first();
  await S('add-to-bag', add, ['default', 'hover', 'focus-visible'], { group: g, title: 'Add to bag', desc: 'The purchase action; measured in every state except a real press.', sel: 'button:has-text("Add to bag")' });
  await S('size-oos', q('button.button-size-selector__button.out-of-stock, button.notify-me').filter({ visible: true }).first(), ['default'], { group: g, title: 'Size button, out of stock', desc: 'The sold-out size state (a "notify me" affordance). Never pressed.', sel: 'button.out-of-stock' });
  await S('wishlist-button', q('button.button-ghost').filter({ hasText: /wishlist/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Wishlist button', desc: 'The ghost sibling of Add to bag. Measured, never pressed.', sel: 'button.button-ghost' });
  await S('size-guide', q('a, button, span').filter({ hasText: /size guide|size chart/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Size-guide link', sel: 'a:has-text("Size guide")' });
  const acc = q('details summary, button[aria-expanded]').filter({ visible: true }).first();
  await S('pdp-accordion', acc, B4, { group: g, title: 'PDP accordion', desc: 'Details/shipping disclosure row.', sel: 'button[aria-expanded]' });
  await S('pdp-accordion-open', acc, ['opened'], { group: g, title: 'PDP accordion, open', sel: 'button[aria-expanded]' });
  save();
}

async function cart() {
  if (!(await newPage('cart'))) return;
  const g = G.cart;
  await S('cart-empty', q('main, .main-content, #MainContent').first(), ['default'], { group: g, title: 'Empty cart', desc: 'The signed-out bag with nothing in it.', sel: 'main' }, { noScroll: true });
  await S('cart-continue', q('a, button').filter({ hasText: /continue shopping|start shopping|shop now/i }).first(), B4, { group: g, title: 'Continue shopping', desc: 'Measured, never followed.', sel: 'a:has-text("Continue")' });
  save();
}

async function account() {
  if (!(await newPage('account'))) return;
  const g = G.account;
  // Scope to the login form: a page-wide heading match caught the footer's
  // "Customer Service" heading, and a loose submit match caught "JOIN NOW".
  const loginForm = q('form').filter({ has: q('input[type="email"], input[name*="email" i]') });
  // Shopify hydrates the account sections after first paint; wait the form in.
  await page.waitForSelector('form h1, form h2, form legend, form [class*="title" i], form [class*="heading" i]', { timeout: 5000 }).catch(() => {});
  await S('login-title', loginForm.locator('h1, h2, h3, legend, [class*="title" i], [class*="heading" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login title', sel: 'login form heading' }, { noScroll: true });
  const email = q('input[type="email"], input[name*="email" i]').first();
  await S('email-input', email, ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'Text was typed and deleted; the form was never submitted.', sel: 'input[type="email"]' });
  await S('password-input', q('input[type="password"]'), ['default', 'focused'], { group: g, title: 'Password field', desc: 'Focused only; nothing was typed.', sel: 'input[type="password"]' });
  // Prefer the control labelled Sign in; a bare submit still beats any
  // unrelated button the old page-wide match caught ("JOIN NOW").
  const loginBtn = loginForm.locator('input[type="submit"], button[type="submit"], button').filter({ hasText: /sign ?in|log ?in|continue/i }).first();
  const loginBtnAny = loginForm.locator('input[type="submit"], button[type="submit"]').filter({ visible: true }).first();
  await S('signin-button', (await loginBtn.count()) ? loginBtn : loginBtnAny, ['default', 'hover', 'focus-visible'], { group: g, title: 'Sign in button', desc: 'The submit; measured except a real press — the form was never submitted.', sel: 'login form submit' });
  await S('forgot-link', q('a').filter({ hasText: /forgot|recover/i }).first(), B4, { group: g, title: 'Forgot-password link', sel: 'a:has-text("Forgot")' });
  await S('create-account', q('a, button').filter({ hasText: /create account|sign up/i }).first(), B4, { group: g, title: 'Create-account link', desc: 'Measured, never followed.', sel: 'a:has-text("Create")' });
  save();
}

async function footer() {
  // The footer lives on the home page, but a full run ends on /account — open
  // home first so the readings are the home footer the page/run/url claim.
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); blockedPages.add('home'); return; }
    await closePromo(page);
  }
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[aria-label], footer a[href*="instagram" i], footer a[href*="tiktok" i]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer a[aria-label]' });
    const nl = q('footer input[type="email"], footer input[name*="email" i], input[placeholder*="email" i]').first();
    if (await nl.count()) await S('newsletter-input', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; never subscribed.', sel: 'footer input[type="email"]' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header, .main-navbar').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('button[aria-label*="menu" i], .hamburger, [class*="hamburger" i], header button:has(svg)').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'header button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the open drawer shows in the crop.', sel: 'header button' }, { noScroll: true });
  // A row inside the drawer m-menu-open left open — a page-wide text match
  // caught the "JOIN TO SHOP" promo instead.
  const mLink = q('[data-state="open"] a, [class*="drawer" i] a, [class*="menu-drawer" i] a, [class*="menu" i][class*="open" i] a').filter({ hasText: /women|men|new arrivals|shop/i }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A row inside the opened menu drawer.', sel: 'open menu a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero-button', q('.hero-button, a.hero-button').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero button', sel: '.hero-button' });
  await S('m-product-tile', q('div, article, li').filter({ has: q('button.swatch, .more-colors-icon') }).first(), ['default'], { group: g, title: 'Mobile product tile', sel: 'grid card' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, plp, pdp, cart, account, mobile };
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
