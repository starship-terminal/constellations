// Measures avnier.com's public components in every state reachable without
// adding to cart, logging in, subscribing or signing in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shop pdp cart login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// avnier.com is a Shopify storefront on a Dawn-family theme in one light
// theme, served in French (fr-FR). Selectors key off the theme's stable
// semantic classes (mega-menu__item, card, facets, product-form__submit) and
// text. Headless Chrome is served a 200 (see lib.mjs). Nothing is sent, added
// to cart, joined or subscribed: the only presses are local UI toggles — the
// mobile drawer, PDP variant radios and accordion details. The Axeptio
// consent SDK and the shipping-country popup are hidden before every
// measurement, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', shop: '/collections/tous-les-produits', pdp: '/products/doudoune-symphony', cart: '/cart', login: '/account/login' };
let page, cdp, current, context, run;
let activeCtx; // the context of the current page; closed when the next route opens
const touched = new Set();
const ranPages = new Set();  // pages that actually opened this run
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
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); activeCtx = undefined; return false; }
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
  shell: 'Shell and navigation', hero: 'Home', plp: 'Shop grid', pdp: 'Product page',
  cart: 'Cart', login: 'Login gate', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

const tid = (id) => `[data-testid="${id}"]`;

async function home() {
  if (!(await newPage('home'))) return;
  ranPages.add('home');
  await sheetsFor('home');
  const g = G.shell;
  await S('skip-link', q('a').filter({ hasText: /ignorer|skip/i }).first(), ['default', 'focus-visible'], { group: g, title: 'Skip link', desc: '"IGNORER ET PASSER AU CONTENU" — off-screen until focused.', sel: 'a:has-text("IGNORER")' }, { noScroll: true });
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The white bar: wordmark, SHOP/MARQUE/SECONDE MAIN/ARCHIVE SALE nav, search, CONNEXION and PANIER.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a.header__heading-link'), ['default'], { group: g, title: 'Logo', desc: 'The wordmark link (a hidden drawer copy is filtered out).', sel: 'a.header__heading-link' }, { noScroll: true });
  await S('nav-item', q('header .mega-menu__item-link').filter({ hasText: /SECONDE MAIN/ }), B4, { group: g, title: 'Nav link', desc: 'A top-level nav link (SECONDE MAIN). Measured, never followed.', sel: '.mega-menu__item-link:has-text("SECONDE MAIN")' }, { noScroll: true });
  const shopItem = q('.mega-menu__item').filter({ hasText: /^\s*SHOP\b/ });
  await S('nav-mega', shopItem, ['hover'], { group: g, title: 'SHOP menu item, hover', desc: 'The SHOP item while its mega-menu dropdown is open.', sel: 'mega-menu__item "SHOP"' }, { noScroll: true, noReset: true, open: async () => { await shopItem.hover(); await page.waitForTimeout(1600); } });
  await S('nav-dropdown', q('.mega-menu__dropdown').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu dropdown', desc: 'The open SHOP dropdown panel.', sel: '.mega-menu__dropdown' }, { noScroll: true, noReset: true, open: async () => { await shopItem.hover(); await page.waitForTimeout(1600); } });
  await S('search-toggle', q('header').locator('a[href*="search" i], button, summary').filter({ has: q('svg') }).filter({ visible: true }).first(), B4, { group: g, title: 'Search icon', desc: 'The magnifier that opens the search modal. Measured, never submitted.', sel: 'header search icon' }, { noScroll: true });
  await S('account-link', q('header a').filter({ hasText: /connexion/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'CONNEXION in the header. Measured, never followed.', sel: 'header a:has-text("CONNEXION")' }, { noScroll: true });
  await S('cart-link', q('header a').filter({ hasText: /panier/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Cart link', desc: 'PANIER in the header. Measured, never followed.', sel: 'header a:has-text("PANIER")' }, { noScroll: true });
  for (let y = 0; y < 3000; y += 700) { await page.evaluate((yy) => scrollTo(0, yy), y); await page.waitForTimeout(220); }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(800);
  const h = G.hero;
  await S('hero', q('[class*="banner" i], [class*="hero" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero', desc: 'The collection announcement block under the header.', sel: '[class*="banner"]' });
  await S('hero-cta', q('a, button').filter({ hasText: /découvrir|decouvrir|shop|voir/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The first call-to-action on the home page. Measured, never followed.', sel: ':has-text("DÉCOUVRIR")' });
  save();
}

async function shop() {
  if (!(await newPage('shop', { wait: 8000 }))) return;
  ranPages.add('shop');
  const g = G.plp;
  await S('plp-title', q('[class*="product-count" i], [id*="ProductCount" i], .facets__heading, h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Collection count', desc: 'The "100 PRODUITS" count / collection heading.', sel: '.product-count, .facets__heading' }, { noScroll: true });
  await S('facet', q('details.facets__disclosure').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Facet filter', desc: 'A PRIX/COULEUR/TAILLE filter disclosure; opened by its own summary.', sel: 'details.facets__disclosure' });
  await S('facet-checkbox', q('details[open].facets__disclosure input[type="checkbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Facet checkbox', desc: 'A checkbox row inside the open COULEUR facet.', sel: 'details[open].facets__disclosure input[type=checkbox]' }, { open: async () => { await page.evaluate(() => { const d = [...document.querySelectorAll('details.facets__disclosure')].find((x) => /COULEUR/i.test(x.innerText || '') && x.offsetParent); if (d) d.open = true; }); await page.waitForTimeout(800); } });
  await S('sort-select', q('select[name="sort_by"], #SortBy').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Sort select', desc: 'The "Recommandés" sort dropdown.', sel: 'select[name="sort_by"]' });
  const card = q('a[href*="/products/"]').filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"card") or self::li][1]');
  await S('product-card', card, ['default', 'hover'], { group: g, title: 'Product card', desc: 'A grid card: image, name, price.', sel: 'card ancestor of a[href*="/products/"]' });
  await S('card-name', q('a[href*="/products/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Card link', desc: 'The product name/link inside a card.', sel: 'a[href*="/products/"]' });
  await S('card-price', q('[class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card price', sel: '.price' });
  save();
}

async function pdp() {
  if (!(await newPage('pdp', { wait: 8000 }))) return;
  ranPages.add('pdp');
  const href = URLS.pdp;
  await closePromo(page);
  await page.waitForSelector('product-form, .product-form__submit, button[name="add"]', { timeout: 15000 }).catch(() => {});
  const g = G.pdp;
  out.components.pdp_url ??= { page: 'pdp', title: 'PDP URL', states: {} };
  out.components.pdp_url.states.default = { text: href, via: 'fixed public sample /products/doudoune-symphony' };
  touched.add('pdp_url');
  await S('pdp-title', q('[class*="product" i] h1, .product__title, h1').filter({ hasText: /\S/ }), ['default'], { group: g, title: 'Product title', sel: '.product__title, product h1' }, { noScroll: true });
  await S('pdp-price', q('[class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product price', sel: '.price' }, { noScroll: true });
  await S('variant-radio', q('input[type="radio"] + label'), ['default', 'hover'], { group: g, title: 'Variant option', desc: 'A TAILLE size chip — the visible label of a visually hidden radio input.', sel: 'input[type=radio] + label' });
  await S('qty-input', q('quantity-input input, input[name="quantity"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Quantity field', sel: 'input[name="quantity"]' });
  await S('add-to-cart', q('button[name="add"], .product-form__submit').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Add to cart', desc: 'The AJOUTER AU PANIER buy button; measured in every state except a real press.', sel: '.product-form__submit' });
  await S('accordion', q('main details summary, product-info details summary').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'PDP accordion', desc: 'A disclosure row (Description / Livraison…) — none on the captured product.', sel: 'main details summary' });
  save();
}

async function cart() {
  // The /cart URL 404s on avnier.com — the cart is the side-cart drawer,
  // opened by clicking the header's PANIER link (JS intercepts the /cart
  // href). The 404 page is recorded as cart-page, then the drawer itself is
  // measured from the home page.
  if (!(await newPage('cart'))) return;
  ranPages.add('cart');
  const g = G.cart;
  out.components['cart-page'] ??= { page: 'cart', title: '/cart is a 404', states: {} };
  out.components['cart-page'].states.default = {
    text: (await page.evaluate(() => document.title)) + ' — /cart answers 404 "Page non trouvée" for everyone; the cart opens as the side-cart drawer (PANIER intercepts the link).',
    via: 'direct GET /cart',
  };
  touched.add('cart-page');
  await S('cart-title', q('main h1, main h2, [class*="cart" i] [class*="title" i], h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: '/cart 404 title', desc: 'The 404 page /cart serves — the cart is the drawer, measured next.', sel: 'h1' }, { noScroll: true });
  await open(page, BASE + '/', { wait: 7000 });
  if (await blocked()) { log('  BLOCKED cart drawer'); return; }
  await closePromo(page);
  const cartLink = q('header a').filter({ hasText: /panier/i }).filter({ visible: true }).first();
  if (await cartLink.count()) {
    await cartLink.click().catch(() => {});
    await page.waitForTimeout(2500);
  }
  await S('cart-drawer', q('.side-cart__wrapper, [class*="side-cart" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart drawer', desc: 'The side-cart opened by PANIER — "MON PANIER - 0 ARTICLE" empty.', sel: '.side-cart__wrapper' }, { noScroll: true });
  await S('cart-empty', q('[class*="cart-empty" i], .side-cart__cart-empty').filter({ visible: true }).first(), ['default'], { group: g, title: 'Empty cart', desc: 'LE PANIER EST VIDE in the drawer.', sel: '.side-cart__cart-empty' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login'))) return;
  ranPages.add('login');
  const g = G.login;
  await S('login-title', q('main h1, main h2, #customer_login h1').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Login title', sel: 'main h1' }, { noScroll: true });
  await S('email-input', q('input[type="email"], input[name*="email" i], #CustomerEmail').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The login email field. Nothing was typed. Nothing was submitted.', sel: 'input[type=email]' });
  await S('password-input', q('input[type="password"]').first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'Focused only; nothing typed.', sel: 'input[type="password"]' });
  await S('login-button', q('button[type="submit"], input[type="submit"], button').filter({ hasText: /connexion|connecter|login|sign in/i }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Login button', desc: 'The submit; measured except a real press — the form was never submitted.', sel: 'button[type="submit"]' });
  save();
}

async function footer() {
  if (!page || page.isClosed()) {
    if (!(await newPage('home'))) return;
  ranPages.add('home');
  } else {
    current = 'home';
    await open(page, BASE + URLS.home, {});
    if (await blocked()) { log('  BLOCKED footer'); return; }
    await closePromo(page);
    ranPages.add('home');
  }
  const g = G.footer;
  // The theme's footer is .footer-bottom__* divs (no <footer> element); its
  // links lazy-load, so scroll it into view first.
  await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(1800);
  const fl = q('footer a, .footer a, [class*="footer" i] a').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  if (await fl.count()) {
    await S('footer', q('.footer-bottom, footer, .footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', sel: '.footer-bottom' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: '.footer a' });
    const nl = q('footer input[type="email"], .footer input[type="email"], [class*="footer" i] input[name*="email" i]').first();
    if (await nl.count()) await S('newsletter-input', nl, ['default', 'focused'], { group: g, title: 'Newsletter field', desc: 'Focused only; never subscribed.', sel: 'footer input[type="email"]' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  ranPages.add('home');
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuSum = q('header details summary, .header__icon--menu, [class*="drawer" i] summary').filter({ visible: true }).first();
  await S('m-menu-button', menuSum, B4, { group: g, title: 'Mobile menu button', sel: 'header details summary' }, { noScroll: true });
  const drawer = q('details.menu-drawer-container, .menu-drawer, menu-drawer, [id*="menu-drawer" i]');
  await S('m-menu-open', menuSum, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The menu summary after its own toggle; the crop is the open drawer.', sel: 'header details summary' }, { noScroll: true, cropLoc: drawer });
  const mLink = q('.toggle-item__header, [class*="menu-drawer" i] a.toggle-item__header').filter({ hasText: /\w{3,}/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', desc: 'A row inside the opened drawer.', sel: '.toggle-item__header' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-feature-tile', q('[class*="card" i] a, [class*="banner" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile content tile', desc: 'A content tile under the hero.', sel: '.card a' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, shop, pdp, cart, login };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Only a page that actually opened may lose its untouched components; a
    // blocked or thrown route keeps its earlier readings instead of erasing
    // them with an incomplete write.
    if (!touched.has(key) && !pages.length && ranPages.has(c.page)) { delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
