// Measures farfetch.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home plp-women plp-men set-women pdp mhome mplp mpdp.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// farfetch.com denies every automated request (Akamai 403 on the host, 429 on
// both farfetch-contents.com CDNs), so the DOM evidence is Wayback Machine SSR
// snapshots served locally by lib.mjs's servePages, painted by their archived
// Emotion CSS with all scripts stripped. farfetch paints one light theme.
// Components carry stable data-component / data-testid hooks, so specs select
// by those, by role, aria-label or structure. Because no script runs, opens and
// toggles that hydration owns (size selector listbox, menus, accordion
// animation) cannot paint: those states are recorded as gaps, not faked. Hover
// is a real pointer hover, focus-visible a real keyboard focus, pressed is
// forced with DevTools CSS.forcePseudoState so no link or button ever fired,
// filled is text typed into a field and deleted again — never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, servePages, launch, open, closePromo, patch, domFind, styleOf, crop, centre, RAW, SCRATCH, PAGES, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
let page, cdp, current, srv, port, browser, run, liveCtx;
const touched = new Set();
const listed = new Map();
const failedPages = new Set();
const URLS = Object.fromEntries(Object.entries(PAGES).map(([k, v]) => [k, v.url]));

// Mobile passes reuse a desktop page file; name the map instead of stripping an
// "m" (that turned mplp into "plp", which has no page file).
const PAGE_OF = { mplp: 'plp-women', mpdp: 'pdp', mhome: 'home' };

async function newPage(key, { mobile = false, wait = 7000 } = {}) {
  current = PAGE_OF[key] || key;
  if (!PAGES[current]) throw new Error(`no page file for ${key}`);
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = browser;
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(9000);
  log('open', key, mobile ? '(mobile)' : '');
  await page.goto(`http://127.0.0.1:${port}/pages/${current}.html`, { waitUntil: 'load', timeout: 120000 }).catch(() => {});
  await page.waitForFunction(() => document.fonts && document.fonts.status === 'loaded', undefined, { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(wait);
  await closePromo(page);
  const body = await page.evaluate(() => (document.body && document.body.innerText || '').length).catch(() => 0);
  if (body < 200) { log('  EMPTY', key); failedPages.add(key); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars.
async function chrome(key) {
  if (KEYS) return; // a targeted run leaves the recorded chrome map as it was
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// KEYS=hero-module,type-title limits a run to those components, so a targeted
// re-measure leaves every other reading and crop untouched.
const KEYS = process.env.KEYS ? new Set(process.env.KEYS.split(',')) : null;

async function S(key, target, list, meta = {}, opts = {}) {
  if (KEYS && !KEYS.has(key)) return;
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    if (opts.dropPrior) {
      out.components[key].states = {};
      out.components[key].missing = true;
      delete out.components[key].recaptureMissed;
    } else if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
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
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

const G = {
  shell: 'Header and site chrome', plp: 'Product listing page', set: 'New-in edit page',
  pdp: 'Product detail page', home: 'Home (department chooser)', type: 'Type specimens',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// ---------------------------------------------------------------- header

async function header() {
  const g = G.shell;
  await S('header', q('header, [data-component="TopBar"], [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The full top chrome: the TopBar (department links, locale flag, account, wishlist, bag) over the NavBar row (wordmark, category links, search field).', sel: 'first header/TopBar' }, { noScroll: true });
  await S('topbar-dept', q('a[data-testid^="header-department"], [data-testid="departments"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Department link', desc: 'A TopBar department link ("Womenswear" / "Menswear" / "Kidswear"); measured, never followed.', sel: 'header-department-* a' }, { noScroll: true });
  await S('topbar-locale', q('button[aria-label*="Language and region" i], [data-component="FlagIcon"]').filter({ visible: true }).first(), B4, { group: g, title: 'Locale control', desc: 'The "Language and region" flag IconButtonGhostDark in the TopBar; measured, never toggled (its picker needs hydration).', sel: 'button[aria-label*=Language and region]' }, { noScroll: true });
  await S('topbar-account', q('[data-testid="userlogin"], a[aria-label*="account" i], a[aria-label*="sign" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Account icon', desc: 'The account/sign-in icon button in the TopBar; measured, never followed.', sel: 'userlogin' }, { noScroll: true });
  await S('topbar-wishlist', q('a[data-testid="wishlist"], [data-testid="wishlist"]').filter({ visible: true }).first(), B4, { group: g, title: 'Wishlist icon', desc: 'The heart icon link to /wishlist (gated); measured, never followed.', sel: 'a[data-testid=wishlist]' }, { noScroll: true });
  await S('topbar-bag', q('a[data-testid="bag"], [data-testid="bag"]').filter({ visible: true }).first(), B4, { group: g, title: 'Bag icon', desc: 'The shopping-bag icon link to checkout (gated); measured, never followed.', sel: 'a[data-testid=bag]' }, { noScroll: true });
  await S('logo', q('[data-testid="ff-logo-global"], [data-component="TopBarBrandArea"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Wordmark', desc: 'The FARFETCH wordmark lockup linking home; measured, never followed.', sel: 'ff-logo-global' }, { noScroll: true });
  await S('nav-link', q('[data-component="NavBarItemLink"], [data-testid="navigation-area-desktop"] a').filter({ hasText: /Clothing/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category link', desc: 'A NavBar category link ("Clothing"); measured, never followed.', sel: 'NavBarItemLink Clothing' }, { noScroll: true });
  await S('nav-sale', q('[data-component="NavBarItemLink"], [data-testid="navigation-area-desktop"] a, [data-component="NavBarList"] a').filter({ hasText: /^\s*Sale\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sale link', desc: 'The red "Sale" link in the NavBar — the one nav item painted in pos-sales red.', sel: 'NavBarItemLink Sale' }, { noScroll: true });
  await S('search-field', q('[data-testid="search-input"], [data-component="SearchInputContainer"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The header "What are you looking for?" search input; focused and typed into then cleared — never submitted.', sel: 'search-input' }, { noScroll: true, fillText: 'trench coat' });
  await S('search-submit', q('[data-component="SearchInputSubmitButton"], button[aria-label*="search" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Search icon button', desc: 'The search-icon submit inside the header field; measured, never pressed.', sel: 'SearchInputSubmitButton' }, { noScroll: true });
}

// ---------------------------------------------------------------- footer

async function footer() {
  const f = G.footer;
  const foot = q('[data-testid="footerDesktop"], [data-component="FooterDesktop"], footer').filter({ visible: true }).last();
  await S('footer', foot, ['default'], { group: f, title: 'Footer', desc: 'The site footer: link columns, newsletter sign-up, socials, locale/legal line.', sel: 'footerDesktop' });
  await S('footer-link', foot.locator('a').filter({ hasText: /Contact us|Terms|Privacy|About|Help/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer column link; measured, never followed.', sel: 'footer a' });
  await S('footer-heading', foot.locator('[data-component="FooterSectionTitle"]').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer column heading', desc: 'A footer column heading (small caps label).', sel: 'FooterSectionTitle' });
  await S('news-field', q('[data-testid="newsletter-form"] input, input[data-testid="email"], input[type="email"]').filter({ visible: true }).first(), FIELD, { group: f, title: 'Newsletter field', desc: 'The footer "Get updates by Email" field; focused and typed into then cleared — never submitted.', sel: 'newsletter email input' }, { fillText: 'name@example.com' });
  await S('news-submit', q('[data-testid="newsletter-submit-button"], [data-testid="newsletter-form"] button').filter({ visible: true }).first(), B4, { group: f, title: 'Sign Up button', desc: 'The "Sign Up" newsletter button; measured, never pressed.', sel: 'newsletter-submit-button' });
  await S('footer-social', foot.locator('a:has(svg), [data-component="FooterSocialsGrouping"] a').filter({ visible: true }).first(), B4, { group: f, title: 'Social icon link', desc: 'A social icon link in the footer; measured, never followed.', sel: 'FooterSocialsGrouping a' });
}

// ---------------------------------------------------------------- listing (plp-women, plp-men, set-women)

async function listing(key) {
  const g1 = key === 'set-women' ? G.set : G.plp;
  await header();
  // The classic listing chrome (breadcrumb, h1, filters, pagination) is SSR
  // only on the sets page; the modular PLPs render it after hydration, so
  // those specs record as missing there — an honest hydration gap.
  await S('breadcrumb', q('nav[aria-label*="breadcrumb" i], [data-component="BreadcrumbsNavigation"], [data-component="Breadcrumbs"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Breadcrumbs', desc: 'The category breadcrumb trail (Home > Women > …).', sel: 'BreadcrumbsNavigation' });
  await S('page-title', q('h1, [data-component="DisplayLarge"], [data-component="Display"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Page heading', desc: 'The listing h1 (PageTitleHeading on the classic listing) or the hero module DisplayLarge title on the modular pages.', sel: 'first h1/DisplayLarge' });
  await S('page-desc', q('[data-component="PageTitleDescription"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Page description', desc: 'The collapsible SEO body copy under the page heading.', sel: 'PageTitleDescription' });
  // The campaign hero only exists on the modular PLPs. The edit page has no
  // hero-container; its ProductShowcase blocks are recommendation rails, so
  // those must never fill the hero keys.
  const hero = q('[data-testid="hero-container"]');
  if (key !== 'set-women') {
    await S('hero-module', hero.filter({ visible: true }).first(), ['default'], { group: g1, title: 'Hero module', desc: 'The content-module hero on the listing front: campaign image, Display title, dek and a "Shop Now" secondary button.', sel: 'hero-container' });
    await S('hero-cta', hero.locator('a, button').filter({ hasText: /^\s*Shop Now\s*$/i }).filter({ visible: true }).first(), B4, { group: g1, title: 'Hero CTA', desc: 'The "Shop Now" secondary button inside the hero module (white surface, dark stroke); measured, never followed.', sel: 'hero-container a "Shop Now"' });
  }
  await S('filter-button', q('[data-testid="filter-button"]').filter({ visible: true }).first(), B4, { group: g1, title: 'All Filters button', desc: 'The "All Filters" button in the listing toolbar; measured, never toggled (its panel needs hydration).', sel: 'filter-button' });
  await S('quick-filter', q('[data-testid="quick-filters-scroller"] button, [data-testid="quick-filters-scroller"] a, [data-selector="catalog-quick-filters-skeleton"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Quick filter scroller', desc: 'The quick-filter chip scroller under the toolbar — the chips are lazy-rendered, so the SSR copy only paints their skeleton bar.', sel: 'quick-filters-scroller > *' });
  const card = q('[data-testid="product-card"], [data-testid="productCard"], [data-component="ProductCard"]').filter({ visible: true }).first();
  await S('product-card', card, ['default', 'hover'], { group: g1, title: 'Product card', desc: 'A listing product card: image, wishlist heart, brand name, description, price.', sel: 'product-card' });
  await S('card-brand', card.locator('[data-testid="product-card-label-primary"], [data-component="ProductCardBrandName"], [data-testid="product-card-label"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g1, title: 'Card brand', desc: 'The brand-name line on a product card.', sel: 'ProductCardBrandName' });
  await S('card-desc', card.locator('[data-component="ProductCardDescription"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Card description', desc: 'The product description line under the brand.', sel: 'ProductCardDescription' });
  await S('card-price', card.locator('[data-testid="product-card-price"], [data-component="PriceBrief"], [data-component="PriceFinal"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Card price', desc: 'The price block on a product card.', sel: 'product-card-price' });
  await S('card-wishlist', card.locator('[data-testid="addToWishlist"], [data-component="WishlistButtonControlled"], button[aria-label*="wishlist" i]').filter({ visible: true }).first(), B4, { group: g1, title: 'Card wishlist heart', desc: 'The heart icon button floating on the card image (aria-pressed toggle); measured, never toggled — adding to a wishlist needs an account.', sel: 'addToWishlist' });
  await S('card-sizes', card.locator('[data-component="ProductCardSizes"], [data-component="ProductCardSizesAvailable"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Card size hint', desc: 'The size-availability hint under a card ("XS S M L" style).', sel: 'ProductCardSizes' });
  await S('sale-price', q('[data-component="PriceSaleDiscount"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Sale price mark', desc: 'The "-40%" discount footnote on a sale card — content-primary-enabled-sale red (its sibling PriceOriginal strikes through).', sel: 'PriceSaleDiscount' });
  await S('sale-original', q('[data-component="PriceOriginal"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Original price', desc: 'The struck-through pre-sale price beside the discount mark on a sale card (grey, line-through).', sel: 'PriceOriginal' });
  await S('pagination', q('[data-component="Pagination"]').filter({ visible: true }).last(), ['default'], { group: g1, title: 'Pagination', desc: 'The pagination control under the grid ("1 of 3" + next arrow).', sel: 'Pagination' });
  await S('pagination-next', q('[data-component="PaginationNextActionButton"], [data-component="Pagination"] a').filter({ visible: true }).last(), B4, { group: g1, title: 'Pagination next', desc: 'The next-page arrow in the pagination control; measured, never followed.', sel: 'PaginationNextActionButton' });
  await S('carousel-arrow', q('[data-testid="showcase-carousel-arrow-next"], [data-component="CarouselArrowSmall"]').filter({ visible: true }).first(), B4, { group: g1, title: 'Carousel arrow', desc: 'A showcase carousel next-arrow (small ghost-dark icon button); measured, never pressed.', sel: 'CarouselArrowSmall' });
  await S('brands-module', q('[data-testid="premium-brands"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Brands module', desc: '"Brands of the moment" — the premium-brand tile module on the modular listing.', sel: 'premium-brands' });
  await S('editorial-card', q('[data-testid="editorial-post"], [data-component="EditorialPost"]').filter({ visible: true }).first(), ['default'], { group: g1, title: 'Editorial card', desc: 'A fashion-feed editorial card on the listing tail.', sel: 'editorial-post' });
  await footer();
  save();
}

// ---------------------------------------------------------------- pdp

async function pdp() {
  await header();
  const g = G.pdp;
  await S('pdp-breadcrumb', q('nav[aria-label*="breadcrumb" i], [data-component="BreadcrumbsNavigation"], [data-component="Breadcrumbs"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Breadcrumbs', desc: 'The PDP breadcrumb trail (Women > Dolce & Gabbana > Shoes > …).', sel: 'BreadcrumbsNavigation' }, { noScroll: true });
  // The product photo column has no stable hook, and the CarouselStandard/SnapSliderWrapper hooks
  // belong to the related-products loading rail below it. Mark the innermost wide block that holds
  // several images, sits left of the buy box and starts near the top of the page.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="pdp-gallery"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const buy = document.querySelector('[data-testid="variant-selector"]');
    const left = buy ? buy.getBoundingClientRect().left : Infinity;
    const hits = [...document.querySelectorAll('div')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width >= 400 && r.right <= left + 1 && r.top + scrollY < 400 && el.querySelectorAll('img').length >= 2
        && !el.closest('[data-testid*="skeleton" i]');
    });
    const inner = hits.filter((el) => !hits.some((o) => o !== el && el.contains(o)))[0];
    if (inner) inner.setAttribute('data-m-mark', 'pdp-gallery');
  });
  await S('pdp-gallery', q('[data-m-mark="pdp-gallery"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Image gallery', desc: 'The PDP product-photo column (the stacked product shots left of the buy box; its arrow controls need hydration).', sel: 'innermost multi-image block left of the buy box' }, { noScroll: true, dropPrior: true });
  await S('pdp-arrow', q('[data-component="CarouselArrowSmall"], button[aria-label*="next" i], button[aria-label*="previous" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Gallery arrow', desc: 'A gallery next/previous arrow; measured, never pressed.', sel: 'CarouselArrowSmall' }, { noScroll: true });
  await S('pdp-brand', q('[data-component="LinkGhostDark"], [data-component="Kicker"]').filter({ visible: true }).first(), B4, { group: g, title: 'Brand link', desc: 'The "Dolce & Gabbana" ghost-dark brand link over the PDP title; measured, never followed.', sel: 'LinkGhostDark' }, { noScroll: true });
  await S('pdp-title', q('[data-testid="product-short-description"], h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The product description heading ("logo-embossed cut-out slides").', sel: 'product-short-description' }, { noScroll: true });
  await S('pdp-price', q('[data-component="PriceCallout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price callout', desc: 'The "$345" price callout above the size selector.', sel: 'PriceCallout' }, { noScroll: true });
  // The variant selector in the archived copy holds only the size combobox: no colour/variant tabs are
  // SSR-rendered, so this records a gap (an unrestricted TabsContainer match read the size selector).
  await S('variant-tabs', q('[data-testid="variant-selector"] [role="tablist"], [data-testid="variant-selector"] [role="tab"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Variant tabs', desc: 'Colour/variant tabs in the variant selector. The archived PDP renders only the size combobox there, so none exist to measure.', sel: 'variant-selector [role=tab]' }, { noScroll: true, dropPrior: true });
  await S('size-selector', q('[data-testid="ScaledSizeSelector"], [data-component="SizeSelectorControlled"], [role="combobox"]').filter({ visible: true }).first(), B4, { group: g, title: 'Size selector', desc: 'The "Select size" combobox (44px outlined field, chevron). Its listbox is hydration-rendered, so no opened state exists in the static copy.', sel: 'ScaledSizeSelector' }, { noScroll: true });
  await S('add-to-bag', q('[data-testid="addToBag"], [data-component="AddToBag"], button[aria-label="Add To Bag"]').filter({ visible: true }).first(), B4, { group: g, title: 'Add To Bag', desc: 'The primary "Add To Bag" button — actions-primary dark surface; measured, never pressed.', sel: 'addToBag' }, { noScroll: true });
  await S('pdp-wishlist', q('[data-component="WishlistIconsContainer"], button[aria-pressed]').filter({ visible: true }).first(), B4, { group: g, title: 'PDP wishlist', desc: 'The "Wishlist" secondary action beside Add To Bag (aria-pressed toggle); measured, never toggled.', sel: 'WishlistIconsContainer' }, { noScroll: true });
  await S('pdp-accordion', q('[data-testid="product-information-accordion"], [data-component="Accordion"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Info accordion', desc: '"The Details / Composition / FARFETCH ID" accordion under the buy box.', sel: 'product-information-accordion' });
  await S('accordion-item', q('[data-component="AccordionItem"], [data-testid="product-information-accordion"] section').filter({ visible: true }).first(), ['default'], { group: g, title: 'Accordion section', desc: 'One accordion section (SSR ships the first panel expanded).', sel: 'AccordionItem' });
  await S('accordion-button', q('[data-component="AccordionButton"]').filter({ visible: true }).first(), B4, { group: g, title: 'Accordion toggle', desc: 'An accordion section toggle; measured, never toggled (panels need hydration).', sel: 'AccordionButton' });
  await S('skeleton-card', q('[data-component="ProductCardSkeleton"], [data-component="ProductCardImageSkeleton"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card skeleton', desc: 'A product-card loading skeleton in the related-products showcase (the showcase grid ships skeletonised in SSR).', sel: 'ProductCardSkeleton' });
  await S('skeleton-showcase', q('[data-testid="showcase-skeleton"], [data-testid="showcase-carousel-skeleton"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Showcase skeleton', desc: 'A related-products showcase in its SSR loading state.', sel: 'showcase-skeleton' });
  await footer();
  save();
}

// ---------------------------------------------------------------- home

async function home() {
  await header();
  const g = G.home;
  await S('dept-heading', q('[data-component="Title"], h2').filter({ hasText: /^Choose a department$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Chooser heading', desc: '"Choose a department" — the Title heading over the three department tiles.', sel: 'Title Choose a department' });
  await S('dept-tile', q('a').filter({ has: q('[data-component="Display"]').filter({ hasText: /^WOMENSWEAR$/ }) }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Department tile', desc: 'A department chooser tile — full-bleed image with the department Display name overlaid; measured, never followed.', sel: 'a:has(Display WOMENSWEAR)' });
  // On the archived home every editorial-post article is a department or category card (the three
  // chooser tiles, then the NEW IN / CLOTHING / ... columns); no fashion-feed card is painted.
  await S('dept-kicker', q('[data-component="Kicker"]').filter({ hasText: /^Clothing$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Category kicker', desc: 'The Kicker heading ("Clothing") over a category card in a department column; the card around it is the link, the heading itself is not interactive.', sel: 'Kicker Clothing' }, { dropPrior: true });
  await S('home-category-card', q('article[data-testid="editorial-post"]').filter({ has: q('[data-component="Kicker"]') }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Category card', desc: 'A department-column category card (image with a Kicker label, e.g. NEW IN); measured, never followed.', sel: 'editorial-post with Kicker' });
  await S('home-editorial', q('[data-testid="editorial-post"]').filter({ hasNot: q('[data-component="Kicker"], [data-component="Display"]') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Editorial card', desc: 'A fashion-feed editorial card on the home tail. The archived home paints only department and category cards, so no feed card exists to measure (the listing pages carry the editorial-card component).', sel: 'editorial-post without Kicker or Display' }, { dropPrior: true });
  await footer();
  save();
}

// ---------------------------------------------------------------- type specimens (from the set page, which paints most roles)

async function types() {
  const g = G.type;
  await S('type-display', q('[data-component="DisplayLarge"], [data-component="Display"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Display', desc: 'A --typography-display / display-large specimen.', sel: 'Display/DisplayLarge' });
  await S('type-title', q('[data-component="Title"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Title', desc: 'A --typography-title specimen.', sel: 'Title' });
  await S('type-kicker', q('[data-component="Kicker"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Kicker', desc: 'The uppercase --typography-kicker over a heading.', sel: 'Kicker' });
  await S('type-body', q('[data-component="Body"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body', desc: 'A --typography-body specimen.', sel: 'Body' });
  await S('type-footnote', q('[data-component="Footnote"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footnote', desc: 'The --typography-footnote micro-label.', sel: 'Footnote' });
  await S('type-label', q('[data-component="LabelPrimarySmall"], [data-component="LabelPrimary"], [data-component="FieldLabel"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Label', desc: 'A small label style (LabelPrimarySmall).', sel: 'LabelPrimarySmall' });
  await S('type-editorial', q('[data-component="Editorial"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Editorial', desc: 'The Nimbus Roman D --typography-editorial serif.', sel: 'Editorial' });
  save();
}

// ---------------------------------------------------------------- mobile

async function mobile(key) {
  const g = G.mobile;
  await S('m-header', q('header, [data-component="TopBar"], [data-component="NavBar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The top chrome at 390: department links, wordmark, locale/account/wishlist/bag icons (the SSR markup paints the desktop chrome responsively; the hamburger needs hydration).', sel: 'first header/TopBar' }, { noScroll: true });
  await S('m-dept-menu', q('[data-testid="departments"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile department menu', desc: 'The "departments" DropdownMenuSelectorUncontrolled in the TopBar — visible only below 60em; measured, never toggled.', sel: 'departments dropdown' }, { noScroll: true });
  await S('m-search', q('[data-testid="search-input"], [data-component="SearchInputContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile search field', desc: 'The search input at phone width.', sel: 'search-input' }, { noScroll: true });
  await S('m-logo', q('[data-testid="ff-logo-global"], [data-component="TopBarBrandArea"] a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile wordmark', desc: 'The FARFETCH wordmark at phone width.', sel: 'ff-logo-global' }, { noScroll: true });
  if (key === 'plp-women' || key === 'set-women') {
    const card = q('[data-testid="product-card"], [data-testid="productCard"], [data-component="ProductCard"]').filter({ visible: true }).first();
    await S('m-product-card', card, ['default'], { group: g, title: 'Mobile product card', desc: 'A listing product card at phone width.', sel: 'product-card' });
    await S('m-filter', q('[data-testid="filter-button"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile filter button', desc: 'The All Filters control at phone width (plp modular page renders it post-hydration).', sel: 'filter-button' });
  }
  if (key === 'pdp') {
    await S('m-add-to-bag', q('[data-testid="addToBag"], [data-component="AddToBag"], button[aria-label="Add To Bag"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile Add To Bag', desc: 'The primary buy button at phone width.', sel: 'addToBag' });
    await S('m-size-selector', q('[data-testid="ScaledSizeSelector"], [data-component="SizeSelectorControlled"], [role="combobox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile size selector', desc: 'The "Select size" combobox at phone width.', sel: 'ScaledSizeSelector' });
  }
  if (key === 'home') {
    await S('m-dept-tile', q('a').filter({ has: q('[data-component="Display"]').filter({ hasText: /^WOMENSWEAR$/ }) }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile department tile', desc: 'A department chooser tile at phone width.', sel: 'a:has(Display WOMENSWEAR)' });
  }
  save();
}

// ---------------------------------------------------------------------------

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
({ srv, port } = await servePages(`${SCRATCH}/pages`, `${SCRATCH}/assets`));
browser = await chromium.launch();
const only = (process.argv[2] || '').split(',').filter(Boolean);
const want = (k) => !only.length || only.includes(k);
try {
  if (want('plp-women') && await newPage('plp-women', { wait: 9000 })) { await chrome('plp-women'); await listing('plp-women'); }
  if (want('set-women') && await newPage('set-women', { wait: 9000 })) { await chrome('set-women'); await listing('set-women'); }
  if (want('plp-men') && await newPage('plp-men', { wait: 9000 })) { await chrome('plp-men'); await listing('plp-men'); }
  if (want('pdp') && await newPage('pdp', { wait: 9000 })) { await chrome('pdp'); await pdp(); }
  if (want('home') && await newPage('home', { wait: 9000 })) { await chrome('home'); await home(); }
  if (want('types')) { if (await newPage('plp-women', { wait: 6000 })) await types(); }
  if (want('mplp') && await newPage('mplp', { mobile: true })) await mobile('plp-women');
  if (want('mpdp') && await newPage('mpdp', { mobile: true })) await mobile('pdp');
  if (want('mhome') && await newPage('mhome', { mobile: true })) await mobile('home');
} finally {
  save();
  await browser.close();
  srv.close();
}
log('done ->', OUT);
