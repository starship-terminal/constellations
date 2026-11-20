// Measures gumroad.com's components on its public pages, in every state that
// can be reached without signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home discover login product checkout mobile. Writes
// raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           the same element after colour-scheme emulation repaints the
//                  page — gumroad.com's own theme mechanism is @media
//                  (prefers-color-scheme:dark); there is no in-page toggle
//                  (setTheme verifies the painted surface; product/checkout
//                  pages pin a light palette, so their dark reads are skipped)
//   opened         a resting state reached by the component's own toggle: the
//                  Discover Filters details, the product Share popover, the
//                  phone's menu
//   focused        a field clicked into — nothing typed
// Nothing is typed, sent, bought or signed into. The only presses are local
// UI toggles the page's own chrome provides; the checkout form is measured as
// found, never filled.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW, PRODUCT_URL, CHECKOUT_URL } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  discover: '/discover',
  login: '/login',
  product: PRODUCT_URL,
  checkout: CHECKOUT_URL,
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
  // The driver is only honest when keyboard focus actually reached the target
  // (or a child of it — wrapper targets like the discover card's article can
  // take no focus of their own, and Tab may land elsewhere). A miss is a
  // failed state, not a reading that falsely shows no visible change.
  const focused = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement)).catch(() => false);
  if (!focused) throw new Error('keyboard focus never reached the target — focus-visible state not measurable');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  const b = await loc.boundingBox();
  if (!b) return null;
  // Force the component's own node: the topmost node at its centre (DOM.getNodeForLocation) is a text span or
  // an svg, whose :active never triggers the component's own :active rule.
  // Clear any marker a failed earlier press left, mark this control, and always unmark it,
  // so a later press can never find a stale marker first and force the wrong control.
  await page.evaluate(() => document.querySelectorAll('[data-m-press]').forEach((el) => el.removeAttribute('data-m-press')));
  let nodeId;
  try {
    await loc.evaluate((el) => el.setAttribute('data-m-press', '1'));
    const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
    ({ nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-press]' }));
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-m-press')).catch(() => {});
  }
  if (!nodeId) return null;
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
  await page.waitForTimeout(400);
  return nodeId;
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'dark' | 'opened:label' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'dark': 'same element after the colour-scheme emulation repainted the page through @media (prefers-color-scheme:dark)' };

// The hero bar gumroad.com puts over its signed-out pages: the wordmark, the
// search combobox, the Log in / Start selling pair and the category nav.
const CHROME = [
  { key: 'nav-bar', group: 'Site chrome', title: 'Header bar',
    desc: 'The hero header over Discover: wordmark, search, the auth buttons and the category nav.',
    sel: 'header.hero, header', find: (p) => p.locator('header.hero, header').first(), states: ['default', 'dark'] },
  { key: 'nav-logo', group: 'Site chrome', title: 'Wordmark link',
    desc: 'The GUMROAD wordmark, uppercased display type, linking home.',
    sel: 'header a (Gumroad)', find: async (p) => await domFind(p, /^\s*gumroad\s*$/i, { sel: 'header a', tag: 'lg', minW: 60 }), states: ['default', 'hover'] },
  { key: 'nav-search', group: 'Site chrome', title: 'Search combobox',
    desc: 'The "Search products" field — a combobox that opens a suggestion menu; "focused" is the field clicked into, nothing typed.',
    sel: 'header input[role="combobox"], header input', find: (p) => p.locator('header input[role="combobox"], header input').filter({ visible: true }).first(), states: ['default', 'focused', 'dark'] },
  { key: 'nav-login', group: 'Site chrome', title: '"Log in" button',
    desc: 'The bordered auth button beside the primary CTA.',
    sel: 'header a (Log in)', find: async (p) => await domFind(p, /^\s*log in\s*$/i, { sel: 'header a, header button', tag: 'li', minW: 40, minH: 20 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-start-selling', group: 'Site chrome', title: '"Start selling" button',
    desc: 'The filled primary auth CTA — primary background, contrast-primary text.',
    sel: 'header a (Start selling)', find: async (p) => await domFind(p, /^\s*start selling\s*$/i, { sel: 'header a, header button', tag: 'ss', minW: 60, minH: 20 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'nav-category', group: 'Site chrome', title: 'Category nav link',
    desc: 'A link in the categories nav ("Design") — underlined text links on the header bar.',
    sel: 'header a[href="/design"]', find: (p) => p.locator('header a[href="/design"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-category-active', group: 'Site chrome', title: 'Category nav link, current',
    desc: '"All" — the current category, painted with the active marker.',
    sel: 'header a[href="/discover"] (All)', find: (p) => p.locator('header a[href="/discover"]').filter({ hasText: /^\s*All\s*$/ }).first(), states: ['default'] },
];

const DISCOVER = [
  { key: 'discover-featured-card', group: 'Discover', title: 'Featured product card',
    desc: 'A large card in the Featured products carousel: cover, title, blurb, creator, rating and the price flag.',
    sel: 'div.override article', find: (p) => p.locator('div.override article').filter({ visible: true }).first(), states: ['default', 'hover', 'dark'] },
  { key: 'discover-pager-arrow', group: 'Discover', title: 'Carousel pager arrow',
    desc: 'The small square arrow button beside the "1 / 8" counter in the Featured header.',
    sel: 'section (Featured) button', find: (p) => p.locator('section').filter({ hasText: /Featured products/ }).locator('button').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'discover-card', group: 'Discover', title: 'Product card (market grid)',
    desc: 'A card in the "On the market" grid: cover block, title, creator, rating row and the price cell in the footer.',
    sel: 'div.grid-cols-2 article', find: (p) => p.locator('div.grid-cols-2 > article, div.grid-cols-2 article').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'dark'] },
  { key: 'discover-card-price', group: 'Discover', title: 'Price flag',
    desc: 'The price cell in a card footer — the accent flag tag ("SGD 47.67").',
    sel: 'article footer (price)', find: async (p) => await domFind(p, /SGD|\$\s*\d/, { sel: 'article footer *', tag: 'pr', minW: 30, minH: 14 }), states: ['default', 'dark'] },
  { key: 'discover-card-rating', group: 'Discover', title: 'Rating stars row',
    desc: 'The star rating in a card footer ("5.0 (6)").',
    sel: 'article footer (rating)', find: async (p) => await domFind(p, /^\s*[\d.]+\s*\(?[\d.,KM]+\)?\s*$/, { sel: 'article footer *', tag: 'rt', minW: 20, minH: 10 }), states: ['default'] },
  { key: 'discover-tab', group: 'Discover', title: 'Market tab',
    desc: 'A tab in the market switcher ("Trending" / "Best Sellers" / "Hot & New") — a bordered pill link.',
    sel: 'a[role="tab"]', find: (p) => p.locator('a[role="tab"]').filter({ hasText: /Best Sellers/ }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'discover-tab-active', group: 'Discover', title: 'Market tab, selected',
    desc: '"Trending" — the selected tab, filled with the inverted colours.',
    sel: 'a[role="tab"][aria-selected="true"]', find: (p) => p.locator('a[role="tab"][aria-selected="true"]').first(), states: ['default', 'dark'] },
  { key: 'discover-filters', group: 'Discover', title: 'Filters disclosure',
    desc: 'The "Filters" details/summary panel — "opened" is its own disclosure press.',
    sel: 'details', find: (p) => p.locator('details').filter({ visible: true }).first(), states: ['default',
      { name: 'opened', via: 'the disclosure\'s own press', fn: async (loc) => { await loc.locator('summary').first().click({ timeout: 4000 }).catch(() => loc.click({ timeout: 4000 }).catch(() => {})); await page.waitForTimeout(700); } }] },
  { key: 'discover-filter-checkbox', group: 'Discover', title: 'Filter checkbox',
    desc: 'A checkbox row inside the open Filters panel (the square box with the tick).',
    sel: 'details[open] input', find: async (p) => {
      const det = p.locator('details').filter({ visible: true }).first();
      if (await det.count() && !(await det.evaluate((d) => d.open).catch(() => false))) { await det.locator('summary').first().click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(700); }
      return p.locator('details[open] input').filter({ visible: true }).first();
    }, states: ['default', 'hover'] },
  { key: 'discover-load-more', group: 'Discover', title: '"Load more" button',
    desc: 'The bordered pagination button under the market grid.',
    sel: 'button (Load more)', find: async (p) => await domFind(p, /^\s*load more\s*$/i, { sel: 'button', tag: 'lm', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'discover-currency-select', group: 'Discover', title: 'Currency select',
    desc: 'The currency picker at the foot of the page ("$ (US Dollars)").',
    sel: 'select', find: (p) => p.locator('select').filter({ visible: true }).last(), states: ['default', 'hover'] },
];

const HOME = [
  { key: 'home-hero', group: 'Home', title: 'Hero section',
    desc: 'The landing hero ("Go from 0 to $1") — display heading over the brand illustration.',
    sel: 'main header, header.grid', find: (p) => p.locator('main header, header.grid').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'home-h1', group: 'Home', title: 'Hero heading',
    desc: 'The display headline in ABC Favorit.',
    sel: 'h1', find: (p) => p.locator('h1').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'home-search', group: 'Home', title: 'Marketplace search field',
    desc: 'The hero\'s "Search marketplace" input with its own search button.',
    sel: 'input#marketplace-search, form input', find: (p) => p.locator('input#marketplace-search, form input[type="search"], form input').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'home-search-button', group: 'Home', title: 'Search button',
    desc: 'The square button attached to the hero search field.',
    sel: 'form button', find: (p) => p.locator('form').filter({ visible: true }).first().locator('button').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'home-subscribe-input', group: 'Home', title: 'Email capture field',
    desc: 'The footer email field of the "subscribe" form.',
    sel: 'form input[type="email"]', find: (p) => p.locator('form input[type="email"], form input').filter({ visible: true }).last(), states: ['default'] },
  { key: 'home-subscribe-form', group: 'Home', title: 'Subscribe form',
    desc: 'The email capture form row at the foot of the landing page — the field plus its arrow submit.',
    sel: 'form.flex.gap-1, form', find: (p) => p.locator('form').filter({ visible: true }).last(), states: ['default', 'dark'] },
];

const LOGIN = [
  { key: 'login-card', group: 'Auth', title: 'Login form card',
    desc: 'The centred card: OAuth buttons, the divider, the email/password fieldset and the submit.',
    sel: 'form', find: (p) => p.locator('form').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'login-oauth', group: 'Auth', title: 'OAuth button',
    desc: 'An identity-provider button ("Apple" / "Google" / "X" / "Stripe") — full-width bordered.',
    sel: 'form button', find: (p) => p.locator('form button').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'login-email', group: 'Auth', title: 'Email input',
    desc: 'The labelled email field — measured, never typed into.',
    sel: 'form input[type="email"]', find: (p) => p.locator('form input[type="email"], form input').filter({ visible: true }).first(), states: ['default', 'focused', 'dark'] },
  { key: 'login-password', group: 'Auth', title: 'Password input',
    desc: 'The password field with its "Show password" eye button.',
    sel: 'form input[type="password"]', find: (p) => p.locator('form input[type="password"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'login-submit', group: 'Auth', title: '"Login" button',
    desc: 'The filled submit — measured and hovered only, never pressed for real.',
    sel: 'form button (Login)', find: async (p) => await domFind(p, /^\s*login\s*$/i, { sel: 'form button', tag: 'ls', minW: 100, minH: 30 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'login-forgot', group: 'Auth', title: '"Forgot your password?" link',
    desc: 'The muted recovery link inside the password fieldset.',
    sel: 'form a (Forgot)', find: async (p) => await domFind(p, /forgot/i, { sel: 'form a', tag: 'fp', minW: 60, minH: 10 }), states: ['default', 'hover'] },
];

const PRODUCT = [
  { key: 'product-header', group: 'Product page', title: 'Product header',
    desc: 'The title block over the buy panel on a <creator>.gumroad.com/l/ page.',
    sel: 'article header', find: (p) => p.locator('article header').filter({ visible: true }).first(), states: ['default'] },
  { key: 'product-tier', group: 'Product page', title: 'Tier option (radio)',
    desc: 'A priced tier card — a radio-style button carrying the price and tier emoji label.',
    sel: '[role="radio"]', find: (p) => p.locator('button[role="radio"], [role="radio"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'product-term-select', group: 'Product page', title: 'Billing term select',
    desc: 'The "Monthly | Yearly" select in the buy controls.',
    sel: 'select', find: (p) => p.locator('select').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'product-buy', group: 'Product page', title: 'Purchase link',
    desc: 'The "Subscribe"/"I want this" link that navigates to gumroad.com/checkout — measured, never followed in this run.',
    sel: 'a (Subscribe|I want this)', find: async (p) => await domFind(p, /^\s*(subscribe|i want this|buy this|add to cart)\s*$/i, { sel: 'a, button', tag: 'by', minW: 80, minH: 30 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'product-wishlist', group: 'Product page', title: '"Add to wishlist" control',
    desc: 'The combobox-shaped wishlist picker beside the purchase link.',
    sel: '[role="combobox"] (wishlist)', find: async (p) => await domFind(p, /wishlist/i, { sel: '[role="combobox"], button, div', tag: 'wl', minW: 100, minH: 30 }), states: ['default', 'hover'] },
  { key: 'product-share', group: 'Product page', title: '"Share" button + popover',
    desc: 'The Share button; "opened" is its own popover state.',
    sel: 'button (Share)', find: async (p) => await domFind(p, /^\s*share\s*$/i, { sel: 'button', tag: 'sh', minW: 60, minH: 30 }), states: ['default', 'hover',
      { name: 'opened', via: 'the button\'s own press, opening the share popover', fn: async (loc) => { await loc.click({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(1200); } }] },
  { key: 'product-ratings', group: 'Product page', title: 'Ratings + reviews',
    desc: 'The ratings column beside the buy panel — the 4.1 summary, the star histogram and the review feed under it.',
    sel: 'article section (Ratings)', find: (p) => p.locator('article section').filter({ has: p.locator('header').filter({ hasText: /ratings/i }) }).filter({ visible: true }).last(), states: ['default'] },
  { key: 'product-review-load', group: 'Product page', title: '"Load more" reviews',
    desc: 'The underlined reviews pagination button.',
    sel: 'button (Load more)', find: async (p) => await domFind(p, /load more/i, { sel: 'button', tag: 'rl', minW: 50, minH: 14 }), states: ['default', 'hover'] },
  { key: 'product-footer', group: 'Product page', title: '"Powered by Gumroad" footer',
    desc: 'The slim footer under the product page — the brand link and currency select.',
    sel: 'footer', find: (p) => p.locator('footer').filter({ visible: true }).first(), states: ['default'] },
];

const CHECKOUT = [
  { key: 'checkout-summary', group: 'Checkout', title: 'Order summary card',
    desc: 'The cart block: item thumbnail with quantity badge, Edit/Remove, the "Give as a gift?" toggle and the totals.',
    sel: 'div#app div.grid.gap-8 > div > div:first-child', find: (p) => p.locator('div#app div.grid.gap-8 > div > div:first-child').filter({ visible: true }).first(), states: ['default'] },
  { key: 'checkout-gift-toggle', group: 'Checkout', title: '"Give as a gift?" switch',
    desc: 'The iOS-style switch — measured, never toggled.',
    sel: '[role="switch"], [role="checkbox"]', find: (p) => p.locator('[role="switch"], [role="checkbox"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'checkout-email', group: 'Checkout', title: 'Email field',
    desc: 'The labelled Email address input — measured as found, never typed into.',
    sel: 'input[type="email"]', find: (p) => p.locator('input[type="email"], input[name*="email" i]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'checkout-name', group: 'Checkout', title: 'Full name field',
    desc: 'The labelled Full name input.',
    sel: 'input[id*="fullName" i]', find: (p) => p.locator('input[id*="fullName" i], input[id*="name" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'checkout-country', group: 'Checkout', title: 'Country select',
    desc: 'The country picker, pre-detected to the visitor\'s region.',
    sel: 'select', find: (p) => p.locator('select').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'checkout-currency', group: 'Checkout', title: 'Currency select',
    desc: 'The "SGD$ (Singapore Dollars) — detected" select in the totals column.',
    sel: 'select (currency)', find: (p) => p.locator('select').filter({ visible: true }).last(), states: ['default'] },
  { key: 'checkout-pay', group: 'Checkout', title: 'Pay button',
    desc: 'The filled pay submit at the foot of the payment column — measured, never pressed.',
    sel: 'button[type="submit"], button (Pay)', find: async (p) => await domFind(p, /pay|subscribe/i, { sel: 'button', tag: 'pa', minW: 100, minH: 30 }), states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-nav-bar', group: 'Site chrome (mobile)', title: 'Mobile header',
    desc: 'The header at 390px: wordmark, search and the menu button.', sel: 'header.hero, header',
    find: (p) => p.locator('header.hero, header').filter({ visible: true }).first(), states: ['default'] },
  { key: 'm-nav-menu-button', group: 'Site chrome (mobile)', title: 'Menu button',
    desc: 'The button that opens the mobile nav panel.',
    sel: 'header button, nav button',
    find: (p) => p.locator('header button').filter({ visible: true }).last(), states: ['default', 'hover'] },
  { key: 'm-discover-card', page: 'discover', group: 'Discover (mobile)', title: 'Product card, phone',
    desc: 'A market-grid card at 390px — the grid collapses to a single column.',
    sel: 'article', find: (p) => p.locator('article').filter({ visible: true }).first(), states: ['default'] },
];

const GROUPS = {
  discover: { page: 'discover', specs: [...CHROME, ...DISCOVER] },
  home: { page: 'home', specs: HOME },
  login: { page: 'login', specs: LOGIN },
  product: { page: 'product', specs: PRODUCT },
  // checkout: a boundary, not a page. CHECKOUT_URL opens a checkout session for a real product (a
  // server-side cart), so it is no longer visited; the committed checkout-* readings were taken past that
  // step (README, What to distrust). CHECKOUT stays as the record of what was measured.
  mobile: { page: 'discover', mobile: true, specs: MOBILE },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); gumroad.com paints light by default and dark under @media (prefers-color-scheme:dark) — the emulation is the theme mechanism, there is no in-page toggle; the product subdomain pins a light palette — `dark` states are measured on the painted dark surface only';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = URLS[g.page].startsWith('http') ? URLS[g.page] : BASE + URLS[g.page];
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 7000 }))) {
    // not reached, or a bot check that never cleared: a boundary, never measured as the product
    log('  ! not reached or bot-checked: recorded as a boundary', key);
    await page.close().catch(() => {});
    continue;
  }
  // Cosmetic only (no blinking caret in crops) — the checkout page's CSP
  // refuses injected styles, so a refusal must not kill the run.
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[URLS[g.page]] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    // Route paths stay paths; absolute URLs go through safeUrl so the checkout
    // page never keeps its product/option query in the record.
    comp.page = URLS[g.page].startsWith('http') ? safeUrl(url) : URLS[g.page];
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        if (st === 'hover') { await hover(loc); viaText = via.hover; }
        else if (st === 'focus-visible') { await kbFocus(loc); viaText = via['focus-visible']; }
        else if (st === 'focused') { await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(loc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await setTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.dark; }
        else if (st && typeof st === 'object' && st.fn) { await st.fn(loc); viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(loc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(loc).catch(() => {});
        const v = await styleOf(loc);
        v.via = viaText;
        v.crop = await crop(page, loc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
        if (darkOn) await setTheme(page, 'light').catch(() => {});
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await setTheme(page, 'light').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
