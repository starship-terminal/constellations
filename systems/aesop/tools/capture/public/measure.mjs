// Measures aesop.com's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shopall skincare pdp search cart signup stores login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// aesop.com is Salesforce B2C Commerce (Sites-aesop-us-Site): server-rendered
// pages with descriptive BEM class names (l-header__, c-product-tile,
// c-sliding-panel, c-navigation__). Nothing is sent, bought or signed into:
// the only presses are local UI toggles (the Search disclosure, the Email
// sign up modal, the My cart drawer, the All filters panel, the burger menu,
// PDP accordions). Submit controls are measured through CDP-forced
// pseudo-classes only. The OneTrust consent SDK is aborted at request level.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { pageState, recordBlocked } from './gate.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  shopall: '/shop-all/',
  skincare: '/skin-care/',
  pdp: '/shop-all/',                // the catalogue; the product page is its first tile, opened in the same context
  search: '/',
  cart: '/',
  signup: '/',
  stores: '/stores',
  login: '/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show',
};
let page, cdp, current, context, contextMobile, run;
const touched = new Set();

// A bot check is a boundary (gate.mjs). Each page is loaded once in its run's
// context. A page that shows a challenge, an error or no content, at load or
// after the settle wait, is recorded in _meta.blocked and skipped: it is never
// reloaded, retried or opened again in a fresh context, and never measured.
// Earlier readings in the file are kept as they are.
function block(key, url, reason) {
  log('  BLOCKED', key, reason);
  recordBlocked(out, key, url, reason, run);
  save();
  return false;
}

// Loads `url` once into the current page and checks it is still the product
// after the settle wait.
async function load(key, url, { wait, promo }) {
  let r = await open(page, url, { wait, promo });
  if (r.ok && (await pageState(page)) !== 'ok') r = { ok: false, reason: 'page turned into a challenge or an error after loading' };
  if (!r.ok) return block(key, url, r.reason);
  if (out._meta.blocked) delete out._meta.blocked[key];
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return true;
}

// The product URL (…/<SKU>.html) of the first product tile on the catalogue
// page the current page shows.
async function firstProductUrl() {
  return page.evaluate(() => {
    const a = [...document.querySelectorAll('a[href$=".html"]')].find((n) => /\/[A-Z]+\d[A-Z0-9]*\.html/i.test(n.getAttribute('href') || ''));
    return a ? a.href : null;
  }).catch(() => null);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000, url } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  // Desktop and mobile runs share page keys (home): a block is recorded per view.
  return load(mobile && !key.startsWith('mobile-') ? `mobile-${key}` : key, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
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

// Clicks a UI toggle (menu, search, filter). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|add to bag|add to cart|register|continue|google|accept|reject|customize|sign me up)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
    let s;
    try {
      s = await styleOf(loc);
    } catch (e) {
      // A state change can briefly unmount/remount the node; retry once
      // against the re-queried element.
      await page.waitForTimeout(1500);
      s = await styleOf(target.filter({ visible: true }).first());
    }
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
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
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
  save(); // the host runs a fleet of captures: persist each component so a crash loses at most one
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'name@example.com';

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
  shell: 'Shell and navigation', home: 'Home', plp: 'Catalogue page (PLP)',
  pdp: 'Product page (PDP)', overlay: 'Panels and overlays',
  login: 'Sign in', stores: 'Stores', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function shell() {
  const g = G.shell;
  await S('header', q('header.l-header'), ['default'], { group: g, title: 'Header', desc: 'The two-tier top bar every page shares: a thin utility row (Stores, Customer service left; Email sign up, Account, My cart right), the centred Aēsop wordmark, the Search disclosure and the main navigation row. Transparent over the hero, solid elsewhere.', sel: 'header.l-header' }, { noScroll: true });
  await S('logo', q('a.c-logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The centred "Aēsop." wordmark linking home.', sel: 'a.c-logo' }, { noScroll: true });
  await S('topnav-link', q('a.c-storeslink').filter({ visible: true }).first(), B4, { group: g, title: 'Utility link', desc: 'A utility-nav entry on the left of the top row (Stores); Customer service sits beside it.', sel: 'a.c-storeslink' }, { noScroll: true });
  await S('topnav-button', q('button.l-header__top-nav-link').filter({ visible: true }).first(), B4, { group: g, title: 'Utility button', desc: 'The Customer service utility button.', sel: 'button.l-header__top-nav-link' }, { noScroll: true });
  await S('signup-link', q('button.c-signup-link').filter({ visible: true }).first(), B4, { group: g, title: 'Email sign up button', desc: 'The Email sign up trigger; opens the newsletter modal (a local toggle).', sel: 'button.c-signup-link' }, { noScroll: true });
  await S('account-link', q('.l-header__top-nav-item.m-account, .c-user__link').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Account entry', desc: 'The Account slot in the utility row; its link lazy-loads once the header hydrates.', sel: '.l-header__top-nav-item.m-account' }, { noScroll: true });
  await S('cart-button', q('button.c-minicart-icon__link').filter({ visible: true }).first(), B4, { group: g, title: 'My cart button', desc: 'The My cart trigger with its item count ("0 product in cart" empty); opens the right-hand cart drawer.', sel: 'button.c-minicart-icon__link' }, { noScroll: true });
  await S('nav-link', q('a.c-navigation__link.m-level-1').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A main-nav entry (Gifts, Shop all, New & Notable, Skin Care, Hand & Body, Fragrance, Home, Hair, Travel, Library, Experience).', sel: 'a.c-navigation__link.m-level-1' }, { noScroll: true });
  await S('search-button', q('button.l-header__search-button[data-js-header-search-cta-large], button.l-header__search-button').last(), B4, { group: g, title: 'Search button', desc: 'The "Search…" trigger opening the search disclosure under the nav.', sel: 'button.l-header__search-button' }, { noScroll: true });
}

async function footerRun() {
  const g = G.footer;
  await S('footer', q('footer, .l-footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The page foot: the newsletter block, help and service link columns, social and region links, and the "Online Preferences" OneTrust trigger.', sel: 'footer' });
  await S('footer-col-title', await domFind(page, /^(help|support|contact|about|company|services|orders?|legal)$/i, { sel: 'footer *, .l-footer *', tag: 'fc', minH: 14 }), ['default'], { group: g, title: 'Footer column title', desc: 'A footer column heading.', sel: 'footer column title' });
  await S('footer-link', q('footer a, .l-footer a').filter({ hasText: /contact us|faqs|shipping|returns|track your order/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link (Contact us, FAQs, Shipping, Returns, Track your order).', sel: 'footer a' });
  await S('footer-prefs-link', q('a.optanon-show-settings, #OTCookieConsentFooter').filter({ visible: true }).first(), B4, { group: g, title: 'Online Preferences link', desc: 'The OneTrust "Online Preferences" cookie-settings trigger in the footer. Measured, never pressed.', sel: 'a.optanon-show-settings' });
  await S('newsletter-field', q('footer input[type="email"], .l-footer input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Newsletter field', desc: 'The footer email field, if the region serves one: typed and deleted, never submitted.', sel: 'footer input[type=email]' });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell();
  const h = G.home;
  // The hero is a full-bleed campaign band with a photo or video and a
  // bordered "Discover" CTA card over it.
  const hero = await page.evaluate(() => {
    // The band under the header: the first painted region inside
    // .experience-main that is hero-sized (300-1400px), not the region itself.
    const els = [...document.querySelectorAll('.experience-main > *, main [class*="spotlight" i], main [class*="hero" i], main section, main > *')];
    const el = els.filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.top < 300 && r.height >= 300 && r.height <= 1400 && n.getBoundingClientRect().width > 800 && (n.querySelector('img, picture, video') || cs.backgroundImage !== 'none');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'hero'); return true;
  });
  await S('hero', hero ? q('[data-m-mark="hero"]') : page.locator('__none__'), ['default'], { group: h, title: 'Hero', desc: 'The full-bleed campaign band under the transparent header: photography or film, an overlaid eyebrow line, a headline and a bordered CTA card.', sel: 'first main band' });
  const cta = await page.evaluate(() => {
    const h = document.querySelector('[data-m-mark="hero"]');
    const a = h && [...h.querySelectorAll('a, button')].filter((n) => { const r = n.getBoundingClientRect(); return r.width > 60 && r.height > 24; })[0];
    if (!a) return false; a.setAttribute('data-m-mark', 'hc'); return true;
  });
  await S('hero-cta', cta ? q('[data-m-mark="hc"]') : page.locator('__none__'), B4, { group: h, title: 'Hero CTA', desc: 'A bordered call-to-action card inside the hero (Discover).', sel: 'hero cta' });
  await footerRun();
  await page.close();
}

async function shopall() {
  if (!(await newPage('shopall'))) { await page.close(); return; }
  await sheetsFor('shopall');
  const g = G.plp;
  await S('plp-title', q('h1.c-refinements__category-name, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Catalogue title', desc: 'The "Shop all" heading over the results grid, beside the product count.', sel: 'h1.c-refinements__category-name' }, { noScroll: true });
  await S('filter-toggle', q('button.c-refinements-toggler').filter({ visible: true }).first(), B4, { group: g, title: 'All filters button', desc: 'The "All filters" toggle opening the refinement panel.', sel: 'button.c-refinements-toggler' }, { noScroll: true });
  const opened = await domClick(page, /all filters/i, 'button.c-refinements-toggler');
  await page.waitForTimeout(1600);
  const panel = await page.evaluate(() => {
    // The rail holds the "Filter by" heading and the RESET ALL / APPLY foot.
    const el = [...document.querySelectorAll('aside, [class*="refinement" i], [class*="panel" i], [role="dialog"], [class*="filter" i], div')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.width > 240 && r.width < 700 && r.height > 300 && cs.visibility !== 'hidden' && cs.display !== 'none' && /filter by|reset all/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'fp'); return true;
  });
  await S('filter-panel', panel ? q('[data-m-mark="fp"]') : q('__none__'), ['default'], { group: g, title: 'Refinement rail', desc: 'The left-hand "Filter by" rail the All filters toggle opens: Price and attribute groups (Skin type, Skin concern, Form, Ingredients, Aroma) as accordion rows, RESET ALL and APPLY at the foot.', sel: 'refinement rail' });
  await S('filter-group', q('[data-m-mark="fp"] [class*="accordion" i] > *, [data-m-mark="fp"] button, [data-m-mark="fp"] [data-js-accordion-control]').filter({ hasText: /price|skin|form|ingredients|aroma|filter/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter group row', desc: 'A refinement group header row inside the rail (Price, Skin type, Skin concern, Form, Ingredients, Aroma).', sel: 'filter group' });
  await S('filter-apply', await domFind(page, /^apply$/i, { sel: '[data-m-mark="fp"] button, [data-m-mark="fp"] a', tag: 'fa', minH: 20 }), B4, { group: g, title: 'Apply button', desc: 'The black APPLY button at the rail’s foot. Measured, never pressed.', sel: 'filter apply' });
  await S('sort-select', q('.c-sorting.c-select, [class*="sort" i] select, select').filter({ visible: true }).first(), B4, { group: g, title: 'Sort select', desc: 'The "Sort: Featured" dropdown beside the product count.', sel: '.c-sorting select' });
  await page.keyboard.press('Escape').catch(() => {});
  await page.evaluate(() => { for (const n of document.querySelectorAll('[class*="m-opened"], [class*="m-active"]')) { if (!n.closest('.c-product-grid')) n.classList.remove('m-opened', 'm-active'); } }).catch(() => {});
  await page.waitForTimeout(600);
  const card = q('.c-product-tile__wrapper, .c-product-tile').filter({ visible: true }).first();
  await S('product-card', card, ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A product cell in the grid: a "New addition" tag when present, the product photograph, the name and the price.', sel: '.c-product-tile' });
  await S('product-card-name', q('.c-product-tile__name, [class*="tile__name" i], .c-product-tile a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product tile name', desc: 'The product name under the tile photograph.', sel: '.c-product-tile__name' });
  await S('product-card-price', q('.c-product-tile .c-product-price__value, .c-product-tile [class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product tile price', desc: 'The price under the name.', sel: '.c-product-price__value' });
  await S('tile-badge', await domFind(page, /new addition|new|limited/i, { sel: '.c-product-tile *, [class*="badge" i], [class*="tag" i], [class*="flag" i]', tag: 'tb', minH: 10 }), ['default'], { group: g, title: 'Tile badge', desc: 'The "New addition" tag over a tile photograph.', sel: 'tile badge' });
  await footerRun();
  await page.close();
}

async function skincare() {
  if (!(await newPage('skincare'))) { await page.close(); return; }
  const g = G.plp;
  const ct = await page.evaluate(() => {
    // The landing's own h1, scoped to page content: a page-wide
    // `h1, [class*="title" i]` match caught the header nav's item title
    // ("Gifts") instead — anything inside header/nav is rejected.
    const el = [...document.querySelectorAll('main h1, [role="main"] h1, .experience-main h1, h1')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.width > 40 && r.height > 10 && cs.visibility !== 'hidden' && !n.closest('header, nav, .l-header, [class*="navigation" i]');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'ct'); return true;
  });
  await S('category-title', ct ? q('[data-m-mark="ct"]') : page.locator('__none__'), ['default'], { group: g, title: 'Category title', desc: 'The Skin Care landing title.', sel: 'main h1' }, { noScroll: true });
  await S('category-quicklink', q('.c-quicklinks__link').filter({ visible: true }).first(), B4, { group: g, title: 'Category quicklink', desc: 'A quicklink pill on the category landing (Category, Skin type, Skin concern).', sel: '.c-quicklinks__link' });
  await S('category-product', q('.c-product-tile, [class*="product-tile" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Category product tile', desc: 'A product tile on the Skin Care landing.', sel: '.c-product-tile' });
  await page.close();
}

async function search() {
  if (!(await newPage('search'))) { await page.close(); return; }
  const g = G.overlay;
  const btn = page.locator('button.l-header__search-button[data-js-header-search-cta-large], button.l-header__search-button').last();
  await btn.click({ timeout: 6000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(1600);
  const panel = await page.evaluate(() => {
    let el = document.getElementById('headerSimpleSearch');
    if (!el) {
      const f = [...document.querySelectorAll('input.c-simple-search, input.c-simple-search__field, input[name="q"], input[type="search"]')].find((x) => x.getBoundingClientRect().width > 0);
      let n = f && f.parentElement;
      while (n && n !== document.body) {
        const r = n.getBoundingClientRect();
        if (r.width > 600 && r.height > 39) { el = n; break; }
        n = n.parentElement;
      }
    }
    if (!el) return false; el.setAttribute('data-m-mark', 'sp'); return true;
  });
  await S('search-panel', panel ? q('[data-m-mark="sp"]') : q('__none__'), ['default'], { group: g, title: 'Search disclosure', desc: 'The "I\'m looking for…" band the Search button reveals under the nav, with a Close button.', sel: '#headerSimpleSearch' }, { noScroll: true });
  await S('search-field', q('#headerSimpleSearch input, input.c-simple-search__field, input[name="q"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Search field', desc: 'The search text field; typed and deleted, never submitted.', sel: 'input.c-simple-search__field' });
  await S('search-close', await domFind(page, /close/i, { sel: 'button, a', tag: 'sc', minH: 14 }), B4, { group: g, title: 'Search close button', desc: 'The Close button ending the search disclosure.', sel: 'search close' });
  await page.close();
}

async function cart() {
  if (!(await newPage('cart'))) { await page.close(); return; }
  const g = G.overlay;
  const btn = page.locator('button.c-minicart-icon__link').filter({ visible: true }).first();
  await btn.click({ timeout: 6000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(1800);
  await S('cart-panel', q('.c-sliding-panel.m-right, .c-minicart').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart drawer', desc: 'The right-hand sliding panel the My cart button opens; shows the empty-cart state when nothing was added. Its body logs a JSON parse warning in headless Chromium.', sel: '.c-sliding-panel.m-right' }, { noScroll: true });
  await S('cart-close', q('button.c-content-panel__close, button[aria-label*="close" i], .c-sliding-panel button, .c-minicart button').filter({ visible: true }).first(), B4, { group: g, title: 'Cart close button', desc: 'The close control at the drawer\u2019s head.', sel: 'cart close' }, { noScroll: true });
  await page.close();
}

async function signup() {
  if (!(await newPage('signup'))) { await page.close(); return; }
  const g = G.overlay;
  const btn = page.locator('button.c-signup-link').filter({ visible: true }).first();
  await btn.click({ timeout: 6000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(2500);
  await page.waitForTimeout(1500);
  const dlg = await page.evaluate(() => {
    // The remote Newsletter-SignUp fragment may not render in headless; the
    // mounted shell (a centred panel with a close control) is measured either
    // way, and the empty-body case is the honest record.
    const el = [...document.querySelectorAll('[role="dialog"], [class*="modal" i], [class*="dialog" i], [class*="popup" i], [class*="lightbox" i]')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.width > 300 && r.height > 200 && cs.visibility !== 'hidden' && cs.display !== 'none' && r.left > 100;
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'sd'); return true;
  });
  await S('signup-dialog', dlg ? q('[data-m-mark="sd"]') : q('__none__'), ['default'], { group: g, title: 'Email sign up dialog', desc: 'The newsletter modal the Email sign up button mounts (a remote Demandware content fragment).', sel: 'signup modal' });
  await S('signup-field', q('[data-m-mark="sd"] input[type="email"], [data-m-mark="sd"] input.c-text-field__input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Sign up email field', desc: 'The email field inside the dialog; typed and deleted, never submitted.', sel: 'signup email input' });
  await S('signup-checkbox', q('[data-m-mark="sd"] .c-check-field, [data-m-mark="sd"] input[type="checkbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign up checkbox', desc: 'A consent checkbox row in the dialog.', sel: 'signup checkbox' });
  await S('signup-submit', q('[data-m-mark="sd"] button[type="submit"], [data-m-mark="sd"] button').filter({ hasText: /sign up|submit|join/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The dialog\u2019s submit button. Measured and state-forced, never pressed: pressing it subscribes an address.', sel: 'signup submit' });
  await page.close();
}

// The product page is reached the way a visitor reaches it: from the
// catalogue, in the same context, so it is that context's second document.
// Turnstile challenges a second document load; a challenge there is recorded
// as blocked like any other page, never got past with a fresh context.
async function toProductPage(key) {
  const url = await firstProductUrl();
  if (!url) return block(key, BASE + '/shop-all/', 'no product tile link found');
  out._meta.pdpUrl = url;
  URLS[key] = url;   // the product URL, so component records name it
  return load(key, url, { wait: 8000, promo: 'close' });
}

async function pdp() {
  if (!(await newPage('pdp', { url: BASE + '/shop-all/' })) || !(await toProductPage('pdp'))) { await page.close(); return; }
  const g = G.pdp;
  await S('breadcrumbs', q('[class*="breadcrumb" i], nav[aria-label*="bread" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Breadcrumbs', desc: 'The breadcrumb line over the PDP.', sel: 'breadcrumbs' }, { noScroll: true });
  await S('breadcrumb-link', q('[class*="breadcrumb" i] a, nav[aria-label*="bread" i] a').filter({ visible: true }).first(), B4, { group: g, title: 'Breadcrumb link', desc: 'A crumb link; the last crumb is the product name.', sel: 'breadcrumb a' }, { noScroll: true });
  await S('pdp-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The product name heading the purchase column.', sel: 'pdp h1' });
  await S('pdp-price', q('[class*="price" i] .c-product-price__value, .c-product-price, [class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product price', desc: 'The price beside or under the title.', sel: 'pdp price' });
  await S('pdp-subtitle', await domFind(page, /cleanser|balm|serum|moisturiser|parfum|drops|wash|cream|oil|kit/i, { sel: '[class*="subtitle" i], [class*="short" i], p, span, div', tag: 'ps', minH: 14 }), ['default'], { group: g, title: 'Product descriptor', desc: 'The short descriptor line under the product name.', sel: 'pdp descriptor' });
  await S('add-to-cart', q('[class*="add-to-cart" i], button[class*="cart" i], [data-component*="addtocart" i] button, form[class*="product" i] button, button').filter({ hasText: /add to (cart|bag|basket)|loading|out of stock|unavailable/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Add to cart button', desc: 'The primary purchase bar, caught mid-hydration as "Loading …" before its label resolves. Measured and state-forced, never pressed: pressing it adds the item.', sel: 'add to cart button' });
  await S('variant-box', await domFind(page, /^kit\b|select a size|^size$/i, { sel: '[class*="variant" i], [class*="attribute" i], [class*="option" i], button, fieldset, legend, label, span, div', tag: 'vb', minH: 20, minW: 150, up: '[class*="variant" i], [class*="option" i], [class*="attribute" i], fieldset, div[class]' }), B4, { group: g, title: 'Variant box', desc: 'The variant/size selector above the purchase bar (the bordered "Kit $600.00" box on a kit).', sel: 'variant box' });
  await S('qty-select', q('select, input[type="number"], [class*="quantity" i] select, [class*="quantity" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Quantity control', desc: 'The quantity selector beside Add to cart, when the product offers one.', sel: 'quantity' });
  await S('pdp-image', q('[class*="gallery" i], [class*="image" i] picture, [class*="carousel" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product gallery', desc: 'The product photograph column.', sel: 'pdp gallery' });
  // The PDP's information accordion (.c-accordion) carries h-hide-for-large:
  // it renders only at phone widths, so the desktop record is an honest miss
  // and the real measurement happens in mobile() below.
  await S('accordion', page.locator('__none__'), B4, { group: g, title: 'Accordion row', desc: 'An expandable information row on the PDP (Description). Desktop never paints it — the block carries h-hide-for-large — so it is measured on the mobile PDP instead; this desktop record stays an honest miss.', sel: '.c-accordion__title' });
  await S('info-row', await domFind(page, /complimentary|free (shipping|delivery)|returns|samples/i, { sel: 'p, li, div, span', tag: 'ir', minH: 14 }), ['default'], { group: g, title: 'Service line', desc: 'A service message near the purchase bar (complimentary shipping, samples).', sel: 'pdp service line' });
  await footerRun();
  await page.close();
}

async function stores() {
  if (!(await newPage('stores'))) { await page.close(); return; }
  const g = G.stores;
  await S('stores-title', await domFind(page, /find a store/i, { sel: 'h1, h2, [class*="title" i]', tag: 'st', minH: 20 }), ['default'], { group: g, title: 'Stores title', desc: '"Find a store" — the locator heading.', sel: 'stores h1' }, { noScroll: true });
  await S('store-search', q('input.c-text-field__input[type="text"], input.c-text-field__input:not([type]), input[type="search"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Store search field', desc: 'The "Address, city, postal code…" locator field (a floating-label text field): typed and deleted, never submitted.', sel: 'store search' }, { noScroll: true });
  await S('store-geolocate', await domFind(page, /geolocate me/i, { sel: 'button, a', tag: 'sg', minH: 14 }), B4, { group: g, title: 'Geolocate button', desc: 'The "Geolocate me" option under the search field.', sel: 'geolocate' }, { noScroll: true });
  await S('store-filters', q('select, [class*="filter" i] select, button').filter({ hasText: /filters/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Store filters', desc: 'The Filters select beside the search field.', sel: 'store filters' }, { noScroll: true });
  await S('map-toggle', await domFind(page, /map|satellite/i, { sel: 'button, [role="button"], [class*="toggle" i]', tag: 'mt', minH: 20 }), B4, { group: g, title: 'Map/Satellite toggle', desc: 'The Map/Satellite segmented toggle over the map.', sel: 'map toggle' }, { noScroll: true });
  const nores = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[role="dialog"], [class*="modal" i], [class*="dialog" i], [class*="popup" i], [class*="toast" i]')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.width > 200 && r.width < 800 && r.height > 100 && r.height < 600 && cs.visibility !== 'hidden' && cs.display !== 'none' && /no result|sorry|no stores/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'nr'); return true;
  });
  await S('no-result-dialog', nores ? q('[data-m-mark="nr"]') : page.locator('__none__'), ['default'], { group: g, title: 'No-result dialog', desc: 'The "No result found / Sorry no stores found" dialog the locator raises for a region with no boutiques; carries an OK dismiss button.', sel: 'no result dialog' });
  await S('see-all-link', await domFind(page, /see all locations/i, { sel: 'a, button', tag: 'sa', minH: 14 }), B4, { group: g, title: 'See all locations link', desc: 'The "See all locations" link beside the map.', sel: 'see all locations' });
  await footerRun();
  await page.close();
}

async function login() {
  if (!(await newPage('login', { wait: 12000 }))) { await page.close(); return; }
  const g = G.login;
  await S('login-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign in title', desc: 'The sign-in page heading.', sel: 'login h1' });
  await S('login-email', q('input[type="email"], input[name*="mail" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The sign-in email field: typed and deleted, never submitted.', sel: 'login email input' });
  await S('login-password', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password field: focused only, never filled or submitted.', sel: 'login password input' });
  await S('login-submit', q('button[type="submit"], input[type="submit"], button, a[class*="button" i]').filter({ hasText: /sign in|log in|submit|continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in button', desc: 'The sign-in submit. Measured, never pressed.', sel: 'login submit' });
  await S('login-register', q('a').filter({ hasText: /create|register|new customer/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Register link', desc: 'The create-account link beside the form.', sel: 'register link' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await S('m-header', q('header.l-header'), ['default'], { group: g, title: 'Mobile header', desc: 'The bar at 390: the burger button, the wordmark, search and cart.', sel: 'header' }, { noScroll: true });
  await S('m-menu-button', q('button.c-hamburger__button').filter({ visible: true }).first(), B4, { group: g, title: 'Burger button', desc: 'The menu trigger; opens the navigation drawer.', sel: 'button.c-hamburger__button' }, { noScroll: true });
  const btn = page.locator('button.c-hamburger__button').filter({ visible: true }).first();
  await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(1600);
  const drawer = await page.evaluate(() => {
    const el = [...document.querySelectorAll('[class*="navigation" i], nav, aside, [class*="panel" i], [class*="drawer" i]')].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 200 && r.height > 300 && /Gifts|Shop all|Skin Care/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'md'); return true;
  });
  await S('m-menu-drawer', drawer ? q('[data-m-mark="md"]') : page.locator('__none__'), ['default'], { group: g, title: 'Mobile menu drawer', desc: 'The navigation accordion the burger button opens.', sel: 'mobile drawer' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="md"] button.c-navigation__button.m-level-1, [data-m-mark="md"] .c-navigation__button').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A level-1 accordion row inside the drawer (Gifts, New & Notable, Skin Care…).', sel: 'm nav item' }, { noScroll: true });
  await page.close();
  // The PDP's information accordion carries h-hide-for-large — it only paints
  // at phone widths — so it is measured here, on the product page at 390.
  if ((await newPage('mobile-pdp', { mobile: true, url: BASE + '/shop-all/' })) && (await toProductPage('mobile-pdp'))) {
    await S('accordion', q('.c-accordion__title, [data-js-accordion-control]').filter({ visible: true }).first(), ['default'], { group: G.pdp, title: 'Accordion row', desc: 'An expandable information row on the PDP (Description). The block carries h-hide-for-large — desktop never paints it — so this is measured on the mobile PDP at 390.', sel: '.c-accordion__title' });
  }
  await page.close();
}

run = new Date().toISOString();
const which = process.argv.slice(2).flatMap((a) => a.split(',')).filter(Boolean);
const ALL = { home, shopall, skincare, pdp, search, cart, signup, stores, login, mobile };
let browser;
({ browser, context } = await launch());
for (const [k, fn] of Object.entries(ALL)) {
  if (which.length && !which.includes(k)) continue;
  for (let attempt = 0; attempt < 3; attempt++) {
    try { await fn(); break; } catch (e) {
      log('RUN FAILED', k, e.message);
      // A renderer crash ("Target page/context/browser has been closed") is
      // retried with a fresh browser; anything else fails the page once.
      if (!/closed|crash|Terminated|target/i.test(e.message) || attempt === 2) break;
      try { await browser.close(); } catch {}
      ({ browser, context } = await launch());
      log('  relaunched browser, retrying', k);
    }
  }
  save();
}
save();
console.log('components:', Object.keys(out.components).length);
await browser.close();
