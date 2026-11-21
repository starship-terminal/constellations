// Measures acnestudios.com's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home woman pdp search menu filter login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// acnestudios.com is Salesforce B2C Commerce: server-rendered pages with
// descriptive class names (header__, product-tile__, pdp__, variations__,
// action--primary). Nothing is sent, bought or signed into: the only presses
// are local UI toggles (the SEARCH panel, the WOMAN mega-menu, the FILTER
// rail) and a PDP size swatch's selection state, reached by forcePseudoState
// or the page's own toggle. The OneTrust banner is hidden remove-only.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/sg/en/home',
  woman: '/sg/en/woman/new-arrivals/',
  pdp: '/sg/en/woman/new-arrivals/',   // resolved to the first product at runtime
  search: '/sg/en/home',
  menu: '/sg/en/home',
  filter: '/sg/en/woman/new-arrivals/',
  login: '/sg/en/account',
  about: '/sg/en/about/about.html',
};
let page, cdp, current, context, contextMobile, run;
const touched = new Set();

// A bot interstitial or an error page renders a minimal body: detect it so a
// blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|page cannot be found/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
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
  for (let attempt = 0; attempt < 3; attempt++) {
    await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    if (!(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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

// Clicks a UI toggle (menu, search, filter). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|add to bag|add to cart|register|continue|google|accept|reject|customize)$/i;
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
      // A state change can briefly unmount/remount the node (the site swaps
      // data-component-state); retry once against the re-queried element.
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
const FILL = 'sample';

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
  shell: 'Shell and navigation', home: 'Home', plp: 'Category page (PLP)',
  pdp: 'Product page (PDP)', overlay: 'Panels and overlays',
  login: 'Sign in', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function shell(page_key = 'home') {
  const g = G.shell;
  await S('header', q('header.skip-link-target'), ['default'], { group: g, title: 'Header', desc: 'The fixed top bar: left the section triggers (WOMAN MAN BAGS SCARVES GIFTS on desktop, a Menu button on narrow), centre the Acne Studios wordmark, right SEARCH HELP ACCOUNT and the BAG count, in a two-zone black-on-white layout with hairline rules.', sel: 'header.skip-link-target' }, { noScroll: true });
  await S('nav-item', q('header button.link--main-nav[aria-label="Woman"]'), B4, { group: g, title: 'Nav item', desc: 'A section trigger (WOMAN MAN BAGS SCARVES GIFTS): all-caps micro type, opens the section mega-menu on press. Measured, the menu was opened once for its panel.', sel: 'header button.link--main-nav "WOMAN"' }, { noScroll: true });
  await S('logo', q('header .logo, header [class*="logo" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The centred Acne Studios logotype image (215px), an img that links home.', sel: 'header .logo' }, { noScroll: true });
  await S('search-button', q('header .header__search-button'), B4, { group: g, title: 'Search button', desc: 'The SEARCH trigger opening the right-side search panel.', sel: '.header__search-button' }, { noScroll: true });
  await S('help-button', q('header button.link--main-nav[aria-label="Help"]'), B4, { group: g, title: 'Help button', desc: 'The HELP trigger in the header.', sel: 'header HELP button' }, { noScroll: true });
  await S('account-link', q('header a.link--main-nav[aria-label="Account"]'), B4, { group: g, title: 'Account link', desc: 'The ACCOUNT entry, an <a> to the sign-in page. Hovered and focused, never followed.', sel: 'header a[href*="account"]' }, { noScroll: true });
  await S('bag-button', q('header button.link--main-nav[aria-label="Bag"]'), B4, { group: g, title: 'Bag button', desc: 'The BAG item-count button (shows "00" empty); opens the shopping-bag drawer.', sel: 'header bag button' }, { noScroll: true });
}

async function footerRun() {
  const g = G.footer;
  await S('footer', q('footer.skip-link-target'), ['default'], { group: g, title: 'Footer', desc: 'The page foot: newsletter signup, contact methods (Live chat / Call / Email), four link columns, social icons, the "SHIPPING TO SINGAPORE (ENGLISH)" region selector and a cookie-settings link.', sel: 'footer.skip-link-target' });
  await S('newsletter-label', await domFind(page, /^newsletter$/i, { sel: 'div, h2, h3, p, span, label', tag: 'nl', minH: 14 }), ['default'], { group: g, title: 'Newsletter heading', desc: 'The NEWSLETTER block opening the footer, with the email field under it.', sel: 'footer newsletter block' });
  await S('newsletter-field', q('footer input[type="email"], footer input[name*="mail" i], input.search-field').first(), ['default', 'focused', 'filled'], { group: g, title: 'Newsletter email field', desc: 'The EMAIL text field in the footer: typed and deleted, never submitted.', sel: 'footer input[type=email]' });
  await S('footer-col-title', await domFind(page, /^(HELP|CLIENT SERVICES|COMPANY|CONTACT US)$/, { sel: 'footer *', tag: 'fc', minH: 14 }), ['default'], { group: g, title: 'Footer column title', desc: 'A column heading (HELP, CLIENT SERVICES, COMPANY, CONTACT US) in micro caps.', sel: 'footer column title' });
  await S('footer-link', q('footer a').filter({ hasText: /contact us|faqs|find a store|order status/i }).first(), B4, { group: g, title: 'Footer link', desc: 'A blue footer link (Contact us, FAQs, Find a store).', sel: 'footer a' });
  await S('social-link', q('footer a').filter({ hasText: /^\s*(IG|FB|TW|YT|PT|WB)\s*$/ }).first(), B4, { group: g, title: 'Social link', desc: 'A two-letter social link (IG FB TW YT PT WB).', sel: 'footer social link' });
  await S('geo-selector', await domFind(page, /SHIPPING TO/i, { sel: 'footer a, footer button, footer div', tag: 'geo', minH: 14 }), B4, { group: g, title: 'Region selector', desc: '"SHIPPING TO SINGAPORE (ENGLISH)": the geo prompt serving the SG storefront. Hovered and focused only.', sel: 'footer shipping selector' });
}

async function home() {
  if (!(await newPage('home'))) { await page.close(); return; }
  await sheetsFor('home');
  await shell();
  const h = G.home;
  // The hero is a full-bleed black band with a campaign photo and the
  // wordmark set over it; gift-guide bars sit at its foot.
  const hero = await page.evaluate(() => {
    const el = [...document.querySelectorAll('main section, main div, [class*="hero" i], [class*="banner" i], [class*="experience"]')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.top < 100 && r.height > 500 && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || n.querySelector('img, picture, video'));
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'hero'); return true;
  });
  await S('hero', hero ? q('[data-m-mark="hero"]') : q('main > *').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero', desc: 'The full-bleed campaign band: black ground, a seasonal photo, the white Acne Studios wordmark set over it, a GIFT GUIDE eyebrow top-left and WOMEN\u2019S/MEN\u2019S GIFT GUIDE bars at the foot.', sel: 'first main band' });
  // The hero wordmark is the big centred alt-text image over the campaign
  // photo — h1 is a 1px screen-reader clip and text matches reach the page root
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('img[alt="Acne Studios"]')].find((n) => n.getBoundingClientRect().width > 500);
    if (el) el.setAttribute('data-m-mark', 'hw');
  });
  await S('hero-wordmark', q('[data-m-mark="hw"]').first(), ['default'], { group: h, title: 'Hero wordmark', desc: 'The giant white "Acne Studios" image headline set over the FW26 campaign photo.', sel: 'hero wordmark image' });
  await S('gift-link', await domFind(page, /gift guide/i, { sel: '.as-cell.tile__pos--top, [class*="tile" i] .as-cell, a', tag: 'gg', minH: 20 }), B4, { group: h, title: 'Gift guide bar', desc: 'A hero-foot link bar (WOMEN\u2019S GIFT GUIDE / MEN\u2019S GIFT GUIDE).', sel: 'gift guide link' });
  await footerRun();
  await page.close();
}

async function woman() {
  if (!(await newPage('woman'))) { await page.close(); return; }
  await sheetsFor('woman');
  const g = G.plp;
  await S('subnav-link', q('main a, nav a').filter({ hasText: /new arrivals|gifts for her|winter dressing/i }).first(), B4, { group: g, title: 'Subnav link', desc: 'The under-header section links on a category page (New Arrivals, Gifts for Her, Winter Dressing, Seasonal Denim, Scarf Personalisation): underlined micro caps.', sel: 'plp subnav a' }, { noScroll: true });
  await S('plp-title', await domFind(page, /women.?s new arrivals/i, { sel: 'h1, h2, [class*="title" i]', tag: 'pt', minH: 14 }), ['default'], { group: g, title: 'Category title', desc: '"WOMEN\u2019S NEW ARRIVALS" with the item count under it.', sel: 'plp title' });
  await S('filter-toggle', q('button.filter__toggle').first(), B4, { group: g, title: 'Filter button', desc: 'The FILTER button opening the FILTER & SORTING rail: a header-style button in the toolbar.', sel: 'button.filter__toggle' }, { noScroll: true });
  const card = q('.tile.product-tile').filter({ visible: true }).first();
  await S('product-card', card, ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A product cell: a 4-span tile with the product photo(s), the name in caps and the monospace price under it. Hover swaps the photo.', sel: '.tile.product-tile' });
  await S('product-card-name', q('.product-tile__name').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product tile name', desc: 'The product name under the tile photo, caps micro type.', sel: '.product-tile__name' });
  await S('product-card-price', q('.product-tile__price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product tile price', desc: 'The monospace price under the name (S$4,500).', sel: '.product-tile__price' });
  await S('load-more', q('button.action--primary').filter({ hasText: /load more/i }).first(), B4, { group: g, title: 'Load more button', desc: 'The black "LOAD MORE" button under the grid: a full-caps black pill the width of its cell.', sel: '.action--primary.action--color-black' });
  await footerRun();
  await page.close();
}

async function filter() {
  if (!(await newPage('filter'))) { await page.close(); return; }
  const g = G.overlay;
  const opened = await domClick(page, /filter/i, 'button.filter__toggle');
  if (!opened) { log('  filter panel did not open'); }
  await page.waitForTimeout(1400);
  const rail = await page.evaluate(() => {
    const el = [...document.querySelectorAll('aside, [class*="filter" i], [role="dialog"]')].filter((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      return r.width > 300 && r.height > 400 && (cs.position === 'fixed' || cs.position === 'absolute') && /SORT BY|TYPE OF PRODUCT/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'rail'); return true;
  });
  await S('filter-rail', rail ? q('[data-m-mark="rail"]') : q('aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter rail', desc: 'The FILTER & SORTING drawer on the right: SORT BY radios (Newest, Price High/Low, Popularity) and TYPE OF PRODUCT radios, a bordered row for the picked option, the black SHOW N ITEMS apply button at the foot.', sel: 'filter rail' }, { noScroll: true });
  await S('sort-option', await domFind(page, /price \(high to low\)|newest/i, { sel: 'label, [class*="option" i], [class*="radio" i], div, span', tag: 'so', minH: 20 }), B4, { group: g, title: 'Sort option', desc: 'A radio row in the filter rail; the picked sort gains a hairline box.', sel: 'sort option' });
  await S('show-items', await domFind(page, /show \d+ items/i, { sel: 'button, a', tag: 'si', minH: 30 }), B4, { group: g, title: 'Show items button', desc: 'The black "SHOW N ITEMS" apply button at the rail\u2019s foot. Measured, never pressed.', sel: 'show items button' });
  await S('filter-close', await domFind(page, /close/i, { sel: 'button, a', tag: 'fx', minH: 14 }), B4, { group: g, title: 'Rail close button', desc: 'The X CLOSE at the rail\u2019s head.', sel: 'rail close' });
  await page.close();
}

async function search() {
  if (!(await newPage('search'))) { await page.close(); return; }
  const g = G.overlay;
  const opened = await domClick(page, /search/i, 'button.header__search-button');
  if (!opened) { log('  search panel did not open'); }
  await page.waitForTimeout(1400);
  const panel = await page.evaluate(() => {
    const el = [...document.querySelectorAll('nav.drawer, aside, [role="dialog"], [class*="search" i]')].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 250 && r.width < 800 && r.height > 300 && n.querySelector('input[type="search"], input.search-field');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'sp'); return true;
  });
  await S('search-panel', panel ? q('[data-m-mark="sp"]') : q('nav.drawer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search panel', desc: 'The right-side SEARCH drawer: a SEARCH HERE field, SUGGESTIONS links in blue caps and SUGGESTED PRODUCTS thumbnails.', sel: 'nav.drawer search panel' }, { noScroll: true });
  await S('search-field', q('[data-m-mark="sp"] input[type="search"], input[type="search"]').first(), ['default', 'focused', 'filled'], { group: g, title: 'Search field', desc: 'The SEARCH HERE text field; typed and deleted, never submitted.', sel: 'input[type=search]' });
  await S('search-suggestion', await domFind(page, /Outerwear|Knitwear|Bags|Scarves|Jeans/, { sel: 'a, button', tag: 'ss', minH: 14 }), B4, { group: g, title: 'Search suggestion', desc: 'A suggestion link in the panel (Outerwear, Knitwear, Bags, Scarves, Jeans), blue caps.', sel: 'suggestion link' });
  await page.close();
}

async function menu() {
  if (!(await newPage('menu'))) { await page.close(); return; }
  const g = G.overlay;
  const opened = await domClick(page, /^woman$/i, 'header button.link--main-nav');
  if (!opened) { log('  mega-menu did not open'); }
  await page.waitForTimeout(1400);
  const panel = await page.evaluate(() => {
    const el = [...document.querySelectorAll('nav, aside, [class*="menu" i], [class*="dropdown" i], [role="dialog"]')].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 400 && r.height > 300 && /NEW ARRIVALS|CLOTHING/i.test(n.innerText || '');
    })[0];
    if (!el) return false; el.setAttribute('data-m-mark', 'mm'); return true;
  });
  await S('menu-panel', panel ? q('[data-m-mark="mm"]') : q('nav').filter({ visible: true }).last(), ['default'], { group: g, title: 'Section menu', desc: 'The WOMAN mega-menu: columns of category links under the header.', sel: 'mega menu' }, { noScroll: true });
  await S('menu-link', q('[data-m-mark="mm"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A category link inside the mega-menu.', sel: 'menu a' });
  await page.close();
}

async function pdp() {
  if (!(await newPage('pdp'))) { await page.close(); return; }
  // Reach the PDP the way a visitor does: first product tile on the category.
  const card = page.locator('a[href*=".html"]').filter({ visible: true }).first();
  await card.click({ timeout: 8000 }).catch(() => card.evaluate((el) => el.click()));
  await page.waitForTimeout(6000);
  await killGeo(page);
  const g = G.pdp;
  await S('breadcrumbs', q('nav.breadcrumbs').first(), ['default'], { group: g, title: 'Breadcrumbs', desc: 'The breadcrumb line over the PDP (Clothing / Outerwear / product name), sticky at the page top.', sel: 'nav.breadcrumbs' }, { noScroll: true });
  await S('breadcrumb-link', q('nav.breadcrumbs a').filter({ visible: true }).first(), B4, { group: g, title: 'Breadcrumb link', desc: 'A crumb link (Clothing, Outerwear); the last crumb is the product name.', sel: 'nav.breadcrumbs a' }, { noScroll: true });
  await S('pdp-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The product name in caps, right column head.', sel: 'pdp h1' });
  await S('pdp-price', q('.pdp__price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product price', desc: 'The monospace price (S$4,500) beside the title.', sel: '.pdp__price' });
  await S('pdp-color', await domFind(page, /dark brown|black|blue|beige/i, { sel: '[class*="color" i], .pdp__info *, div, span, p', tag: 'pc', minH: 10 }), ['default'], { group: g, title: 'Colour name', desc: 'The colourway under the title (Dark brown).', sel: 'pdp colour' });
  await S('fit-predictor', q('button.fp-element').filter({ visible: true }).first(), B4, { group: g, title: 'Fit Predictor button', desc: 'The "Fit Predictor - Calculate your size" link-button beside the size grid.', sel: 'button.fp-element' });
  await S('size-guide-link', await domFind(page, /size guide/i, { sel: 'button, a', tag: 'sg2', minH: 10 }), B4, { group: g, title: 'Size guide link', desc: 'The Size guide trigger opening the size drawer.', sel: 'size guide button' });
  const cell = q('button.variations__grid-item').filter({ visible: true }).nth(2);
  await S('size-cell', cell, B4, { group: g, title: 'Size cell', desc: 'A size button in the variations grid (32\u201342): a bordered cell, caps numeral; the picked size gains a heavy black edge.', sel: 'button.variations__grid-item' });
  // Pick a size through the page's own toggle — a local selection, like the
  // search/menu toggles; nothing is added or sent. Then measure the picked cell.
  // The grid only responds to a real pointer click (a synthetic el.click() is ignored).
  await cell.click({ timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(900);
  const picked = await page.evaluate(() => {
    const els = [...document.querySelectorAll('button.variations__grid-item')];
    const el = els.find((n) => n.getAttribute('aria-pressed') === 'true' || n.getAttribute('aria-selected') === 'true')
      || els.find((n) => /selected|active|picked/i.test(n.className || ''))
      || els.find((n) => getComputedStyle(n).borderTopWidth > '1px' || getComputedStyle(n).borderColor === 'rgb(0, 0, 0)');
    if (!el) return false; el.setAttribute('data-m-mark', 'sz'); return true;
  });
  await S('size-cell-selected', picked ? q('[data-m-mark="sz"]') : q('button.variations__grid-item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Size cell, picked', desc: 'The selected size cell, pressed through the page\u2019s own toggle.', sel: 'size cell selected' });
  // The button's own hover handler retitles it "PLEASE SELECT SIZE" until a
  // size is picked, so the text filter has to allow both labels.
  await S('add-to-bag', q('button.action--primary.action--color-blue').filter({ hasText: /add to bag|please select size/i }).first(), B4, { group: g, title: 'Add to bag button', desc: 'The electric-blue ADD TO BAG bar; hovered it retitles to "PLEASE SELECT SIZE" until a size is picked. Measured and state-forced, never pressed: pressing it adds the item.', sel: '.action--primary.action--color-blue' });
  await S('wishlist-button', q('button.action--primary.action--color-white').filter({ visible: true }).first(), B4, { group: g, title: 'Wishlist button', desc: 'The white heart button beside ADD TO BAG, blue heart outline. Measured, never pressed.', sel: '.action--primary.action--color-white' });
  await S('info-row', await domFind(page, /free delivery|complimentary giftwrapping|pick up in store/i, { sel: 'button, a, [class*="accordion" i], [class*="row" i]', tag: 'ir', minH: 30, leaf: false }), ['default', 'hover'], { group: g, title: 'Info row', desc: 'An expandable service row (FREE DELIVERY & EASY RETURNS, COMPLIMENTARY GIFTWRAPPING, PICK UP IN STORE): caps label with a hairline rule and a chevron.', sel: 'pdp info row' });
  await S('description', q('.experience-description').filter({ visible: true }).first(), ['default'], { group: g, title: 'Description block', desc: 'The product story and bullet spec list under the info rows.', sel: '.experience-description' });
  await S('show-more', await domFind(page, /show more/i, { sel: 'button, a', tag: 'sm', minH: 10 }), B4, { group: g, title: 'Show more link', desc: 'The "+ SHOW MORE" spec expander.', sel: 'show more' });
  await footerRun();
  await page.close();
}

async function login() {
  if (!(await newPage('login'))) { await page.close(); return; }
  const g = G.login;
  await S('login-title', await domFind(page, /sign in or register/i, { sel: 'h1, h2, [class*="title" i]', tag: 'lt', minH: 20 }), ['default'], { group: g, title: 'Sign in title', desc: '"Sign in or register" — the gate for the account area.', sel: 'login h1' });
  await S('login-benefit', await domFind(page, /priority access|eligible to exclusive|track your orders/i, { sel: 'li, p, div, span', tag: 'lb', minH: 14 }), ['default'], { group: g, title: 'Benefit row', desc: 'A member-benefit line (Priority access to new collections\u2026) with an en-dash bullet.', sel: 'benefit row' });
  await S('login-email', q('input[type="email"], input[name*="mail" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The grey EMAIL field: typed and deleted, never submitted.', sel: 'login email input' });
  await S('login-continue', await domFind(page, /^continue$/i, { sel: 'button, [role="button"]', tag: 'lc', minH: 30 }), B4, { group: g, title: 'Continue button', desc: 'The black CONTINUE bar. Measured, never pressed.', sel: 'login continue' });
  await S('login-google', await domFind(page, /^google$/i, { sel: 'button, a, [role="button"]', tag: 'lg', minH: 30 }), B4, { group: g, title: 'Google button', desc: 'The white-bordered GOOGLE oauth row. Measured, never pressed.', sel: 'login google' });
  await S('change-location', await domFind(page, /change location/i, { sel: 'a, button', tag: 'cl', minH: 10 }), B4, { group: g, title: 'Change location link', desc: 'The change-location line under the title. The place name is not recorded.', sel: 'change location' });
  await page.close();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await page.close(); return; }
  const g = G.mobile;
  await S('m-header', q('header.skip-link-target'), ['default'], { group: g, title: 'Mobile header', desc: 'The bar at 390: a Menu button, the wordmark and the bag count only.', sel: 'header' }, { noScroll: true });
  await S('m-menu-button', q('header button.header__icon-button').filter({ hasText: /menu/i }).first(), B4, { group: g, title: 'Mobile menu button', desc: 'The Menu trigger; opens the drawer.', sel: 'm menu button' }, { noScroll: true });
  // The Menu trigger is icon-only (aria-label, no text); the drawer is a
  // .navigation-state-container overlay, not a nav/aside element
  await page.locator('header button[aria-label="Menu" i]').first().click().catch(() => {});
  await page.waitForTimeout(1200);
  const drawer = await page.evaluate(() => {
    const el = document.querySelector('.navigation-state-container')
      || [...document.querySelectorAll('[class*="nav" i]')].find((n) => {
        const r = n.getBoundingClientRect();
        return r.width > 200 && r.height > 300 && /WOMAN|MAN/i.test(n.innerText || '');
      });
    if (!el) return false; el.setAttribute('data-m-mark', 'md'); return true;
  });
  await S('m-menu-drawer', drawer ? q('[data-m-mark="md"]') : page.locator('__none__'), ['default'], { group: g, title: 'Mobile menu drawer', desc: 'The navigation drawer the Menu button opens.', sel: 'mobile drawer' }, { noScroll: true });
  await S('m-hero', q('main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile main', desc: 'The mobile page canvas under the header.', sel: 'main' }, { noScroll: true, open: async () => { await page.keyboard.press('Escape'); await page.evaluate(() => { document.querySelectorAll('[data-m-mark="md"]').forEach((n) => { n.style.display = 'none'; }); }); await page.waitForTimeout(500); } });
  await page.close();
}

run = new Date().toISOString();
const which = process.argv.slice(2).flatMap((a) => a.split(',')).filter(Boolean);
const ALL = { home, woman, pdp, search, menu, filter, login, mobile };
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
