// Measures drinkdouze.com's public components in every state reachable
// without signing in, adding to the cart or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shop product trio faq story login cart search mobile (the footer
// runs with home).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// drinkdouze.com is a French Shopify storefront (an Impact-family theme plus
// douze-custom.css) that paints light only, so specs select by the theme's
// custom elements (product-item, store-header, cart-count), its BEM classes
// and visible text. The quick-add form is visibility:hidden until its card is
// hovered, so every quick-add state is read with the card hovered. The only
// presses are local UI toggles: the 24-Canettes pack-size swatch (a radio,
// nothing added) and the mobile menu. Add-to-cart, quick-add, Se connecter and
// the cart actions are measured, never pressed. The Klaviyo popup and any
// consent overlay are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', shop: '/collections/all', product: '/products/orange-sanguine-piment', trio: '/products/trio-douze', faq: '/pages/page-faq', story: '/pages/notre-histoire', login: '/account/login', cart: '/cart', search: '/search?q=douze' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'fr-FR' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'fr-FR' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'fr-FR', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home sections',
  shop: 'Shop', product: 'Product page', content: 'Content pages',
  auth: 'Account and cart', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('announcement-bar', q('announcement-bar, [class*="announcement-bar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Announcement bar', desc: 'The top strip ("Livraison gratuite en France métropolitaine à partir de 50€"), sable on the page edge.', sel: 'announcement-bar' }, { noScroll: true });
  await S('header', q('store-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky transparent header: nav links left, the DOUZE wordmark centre, links + newsletter/account/cart icons right.', sel: 'store-header' }, { noScroll: true });
  await S('logo', q('.header__logo-link, a[aria-label*="Homepage" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The DOUZE wordmark SVG anchor.', sel: '.header__logo-link' }, { noScroll: true });
  await S('nav-link', q('a.header__linklist-link').filter({ hasText: /Notre Histoire/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header nav link (animated-underline style).', sel: 'a.header__linklist-link "Notre Histoire"' }, { noScroll: true });
  await S('nav-shop', q('.header__linklist-item.has-dropdown a, a.header__linklist-link').filter({ hasText: /^\s*Shop\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Shop nav link', desc: 'The Shop link, marked has-dropdown; its panel content is not in the signed-out DOM on hover.', sel: '.header__linklist-item.has-dropdown a' }, { noScroll: true });
  // The newsletter envelope toggle (button[aria-controls=newsletter-popup]) is
  // display:none at desktop widths — the drawer cannot be opened signed out,
  // so there is nothing to measure; the gap is documented in the README.
  await S('account-icon', q('a[aria-label="Connexion" i], a[href="/account/login"]').filter({ visible: true }).first(), B4, { group: g, title: 'Account icon link', desc: 'The person icon linking to /account/login; measured, never followed.', sel: 'a[aria-label="Connexion"]' }, { noScroll: true });
  await S('cart-icon', q('a[aria-controls="mini-cart"], a[aria-label="Panier" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart icon', desc: 'The bag icon with the floating cart-count bubble; toggles the mini-cart drawer.', sel: 'a[aria-controls="mini-cart"]' }, { noScroll: true });
  await S('cart-count', q('cart-count, [class*="cart-count" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart count bubble', desc: 'The numeric bubble on the bag icon (0 signed out).', sel: 'cart-count' }, { noScroll: true });
  const h = G.hero;
  await S('hero-title', q('.image-hero__heading.heading, .image-overlay h1, [class*="hero" i] .heading').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: "The boxed hero's Boogy display heading (60-72px, italic accent on the flavour name), sable text over the photo.", sel: '.image-hero__heading' });
  await S('hero-cta', q('.image-hero__button .button, [class*="hero" i] a.button').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "SHOP" button over the hero media: dusk fill, white label, square 0px corners.', sel: '.image-hero__button .button' });
  await S('marquee', q('.moving-banner').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Moving banner', desc: 'The scrolling claim strip ("Sans sucre ajouté · Faible en calories · …") between sections.', sel: '.moving-banner' });
  await S('marquee-item', q('.moving-banner [class*="item" i], .moving-banner span, .moving-banner p').filter({ hasText: /SANS|INGRÉDIENTS|CALORIES/i }).filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Moving banner item', desc: 'One claim inside the scrolling strip, divided by 9px dots.', sel: '.moving-banner item' });
  await S('section-h2', q('h2.heading, .section__header .heading, .heading.h2').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Section heading', desc: 'A Boogy section heading inside a boxed section.', sel: 'h2.heading' });
  await S('product-item', q('product-item').filter({ visible: true }).first(), B4, { group: G.home, title: 'Product card', desc: 'A product-item card in the featured row: packshot, flavour title, price button; hover swaps to the second image.', sel: 'product-item' });
  const hoverCard = async () => { const c0 = q('product-item').filter({ visible: true }).first(); if (await c0.count()) { await c0.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(700); return 'hovered the first product-item to reveal its quick-form'; } };
  await S('product-price', q('product-item .product-item__btn-price').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Product price', desc: 'The price inside the card\'s quick-add button — the form reveals on card hover.', sel: '.product-item__btn-price (hover-revealed)' }, { noReset: true, open: hoverCard });
  await S('testimonial', q('.testimonials-2 [class*="testimonial" i], [class*="testimonial" i] blockquote, [class*="quote" i]').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Testimonial', desc: 'A customer quote in the "Douze & vous" section.', sel: '.testimonials-2 testimonial' });
  save();
}

async function shop() {
  if (!(await newPage('shop', { wait: 9000 }))) return;
  await sheetsFor('shop');
  await chrome('shop');
  const g = G.shop;
  await S('shop-title', q('.image-overlay__text-container, .image-hero__container, [class*="image-hero" i] section').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop banner', desc: 'The collection page\'s image-hero band — the page leads with media; the heading node is a wordmark image with no live text.', sel: '.image-overlay__text-container' }, { noScroll: true });
  await S('product-card', q('product-item').filter({ visible: true }).first(), B4, { group: g, title: 'Product card', desc: 'A product-item in the /collections/all grid; its per-flavour --button-background-color rebinds the button fill (#f26554 for Orange Sanguine & Piment).', sel: 'product-item' });
  await S('product-card-title', q('product-item .product-item__title-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product card wordmark', desc: 'The flavour title on a grid card is a wordmark image (no live text), over a pack-line paragraph.', sel: '.product-item__title-wrapper' });
  await S('product-card-pack', q('product-item .product-item__info-wrapper .h5, product-item .h5').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card pack line', desc: 'The "6 canettes 25cl" pack description under the wordmark, h5 style.', sel: '.product-item__info-wrapper .h5' });
  const hoverCard2 = async () => { const c0 = q('product-item').filter({ visible: true }).first(); if (await c0.count()) { await c0.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(700); return 'hovered the card to reveal the quick-add form'; } };
  await S('quick-add', q('product-item .product-item__add-to-cart-btn, product-item .product-item__quick-form .button').filter({ visible: true }).first(), B4, { group: g, title: 'Quick-add button', desc: "The card's Ajouter-au-panier — visibility:hidden until the card is hovered, so every state is read with the card hovered; the press posts to /cart/add so it is measured, never pressed.", sel: '.product-item__add-to-cart-btn' }, { noReset: true, open: hoverCard2, before: Object.fromEntries(B4.map((s) => [s, hoverCard2])) });
  await S('product-card-price', q('product-item .product-item__btn-price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Quick-add price', desc: "The price span inside the quick-add button.", sel: '.product-item__btn-price' }, { noReset: true, open: hoverCard2 });
  await S('sort-control', q('select, [class*="filter" i], [class*="sort" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Sort control', desc: 'A sort/filter control on the collection grid, if one paints.', sel: 'shop select' });
  await S('pagination', q('[class*="pagination" i], nav[aria-label*="pagination" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pagination', desc: "The grid's pagination, if the catalogue is long enough to need one.", sel: 'pagination' });
  save();
}

async function product() {
  if (!(await newPage('product', { wait: 10000 }))) return;
  await sheetsFor('product');
  await chrome('product');
  const g = G.product;
  await S('pdp-media', q('.product__media, [class*="gallery" i], product-gallery').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product media', desc: 'The packshot gallery left of the buy box.', sel: '.product__media' }, { noScroll: true });
  await S('pdp-title', q('.product-item__title-wrapper, product-info .heading, [class*="product-info" i] [class*="title" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The 60px Boogy flavour title in the buy box.', sel: '.product-item__title-wrapper' });
  await S('pdp-price', q('[data-product-price-list] .price, .price-list .price, [class*="price" i]').filter({ hasText: /\d+([.,]\d+)?\s*€/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', desc: 'The selling price figure (21.00€ for a 6-pack).', sel: '[data-product-price-list] .price' });
  await S('variant-swatch', q('label.block-swatch__item').filter({ hasText: /6\s*CANETTES/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Pack-size swatch (checked)', desc: 'The checked "6 Canettes" block-swatch radio label.', sel: 'label.block-swatch__item "6 CANETTES"' });
  await S('variant-swatch-2', q('label.block-swatch__item').filter({ hasText: /12\s*CANETTES/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Pack-size swatch', desc: 'An unchecked block-swatch option (12 Canettes), read at rest, on hover, on keyboard focus and forced pressed; the selected look is the separate swatch-selected entry. Never added to the cart.', sel: 'label.block-swatch__item "12 CANETTES"' });
  // add-to-cart first: the swatch-selected click below picks the 24-pack and is not undone, so
  // a later read would show that pack's price, not the default one named in the desc.
  await S('add-to-cart', q('.product-form__add-button, button[data-product-add-to-cart-button]').filter({ visible: true }).first(), B4, { group: g, title: 'Add to cart button', desc: 'The "Ajouter au panier — 21€" submit; measured, never pressed — a press posts to /cart/add.', sel: '.product-form__add-button' });
  await S('swatch-selected', q('label.block-swatch__item').filter({ hasText: /24\s*CANETTES/i }).filter({ visible: true }).first(), ['selected'], { group: g, title: 'Swatch, newly selected', desc: 'The 24-Canettes swatch in its selected state, reached by the swatch\'s own click.', sel: 'selected block-swatch' }, { before: { selected: async () => { const v = q('label.block-swatch__item').filter({ hasText: /24\s*CANETTES/i }).filter({ visible: true }).first(); if (await v.count()) { await v.click({ timeout: 4000 }).catch(() => v.evaluate((el) => el.click())); await page.waitForTimeout(1200); return 'clicked the 24-CANETTES swatch (local radio, nothing added)'; } } } });
  await S('reassurance', q('.product-info__reassurance-item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Reassurance line', desc: 'A trust line under the buy button ("livraison à J+2…"), dusk text with a flavour-coloured divider.', sel: '.product-info__reassurance-item' });
  await S('reviews-tab', q('.kl_reviews__list__tabs button, .kl_reviews [role="tab"], .kl_reviews__list__tabs').filter({ visible: true }).first(), B4, { group: g, title: 'Reviews tab', desc: "A Klaviyo-reviews tab (\"Avis\" / \"Écrire un avis\") — a vendor widget painted in the theme's chrome.", sel: '.kl_reviews__list__tabs' });
  await S('sort-select', q('select').filter({ visible: true }).first(), B4, { group: g, title: 'Review sort select', desc: 'The Klaviyo reviews sort <select> — the one native select that paints signed out.', sel: 'select#kl_reviews__sort_by_reviews' });
  save();
}

async function trio() {
  if (!(await newPage('trio', { wait: 10000 }))) return;
  const g = G.product;
  await S('trio-title', q('.product-item__title-wrapper, [class*="product-info" i] [class*="title" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Bundle title', desc: 'The Trio Douze buy-box title.', sel: 'trio .product-item__title-wrapper' });
  await S('subscription-radio', q('label').filter({ hasText: /ACHAT UNIQUE|ABONNEMENT/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Purchase-option radio', desc: 'The one-off vs. subscription radio in the buy box (it renders after the pack-size is settled, seen in the variant shot); never toggled past the default.', sel: 'label "ACHAT UNIQUE"' });
  save();
}

async function faq() {
  if (!(await newPage('faq', { wait: 8000 }))) return;
  const g = G.content;
  await S('faq-title', q('h1, .heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The "Page FAQ" heading — the page is a stub with no accordion painted signed out.', sel: 'faq .heading' });
  await S('accordion', q('details, [class*="accordion" i], [class*="collapsible" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Accordion', desc: 'A disclosure row, where one paints (none on the FAQ stub).', sel: 'details' });
  save();
}

async function story() {
  if (!(await newPage('story', { wait: 8000 }))) return;
  const g = G.content;
  await S('story-h1', q('h1, .heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Story title', desc: 'The Notre-histoire page heading.', sel: 'story .heading' });
  await S('story-lede', q('.rte p, main p:not(announcement-bar p):not(header p):not(footer p)').filter({ hasText: /\S+\s+\S+\s+\S+\s+\S+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Story paragraph', desc: 'A body paragraph in the story page, Robin Regular.', sel: 'story .rte p' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  const g = G.auth;
  const card = await markPainted('.customer-form-card, form#customer_login', 'm-login', { minW: 250, minH: 200 });
  // markPainted returns a never-matching locator on a miss, not null
  await S('login-card', (await card.count()) ? card : q('.customer-form-card, main form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The centred customer-login card; never filled or submitted.', sel: '.customer-form-card' });
  await S('email-field', q('input[name="customer[email]"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The E-mail input with its floating label; sample text was typed and deleted, nothing sent.', sel: 'input[name="customer[email]"]' });
  await S('password-field', q('input[name="customer[password]"], input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The Mot-de-passe input; focused only, never filled.', sel: 'input[name="customer[password]"]' });
  await S('login-button', q('form button[type="submit"], form .button').filter({ hasText: /connecter|log ?in/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login button', desc: 'The Se-connecter submit; measured, never pressed (a press would submit).', sel: 'form button "Se connecter"' });
  await S('recover-link', q('form button[type="button"], .customer-form-card button, main button').filter({ hasText: /oubli|forgot|recover|récup/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Recover toggle', desc: 'The "Mot de passe oublié ?" button, which swaps the card to the recover form in place; measured at rest, on hover, on keyboard focus and forced pressed, never clicked, so the swap is not captured.', sel: 'button "Mot de passe oublié"' });
  await S('register-link', q('a[href*="register" i], main a').filter({ hasText: /inscrire|register/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Register link', desc: 'The "S\'inscrire" link to /account/register.', sel: 'a[href*="register"]' });
  save();
}

async function cart() {
  if (!(await newPage('cart', { wait: 9000 }))) return;
  const g = G.auth;
  await S('cart-empty', q('.empty-state').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart, empty', desc: 'The "Votre panier est vide" empty state — the only cart surface reachable without adding an item.', sel: '.empty-state' });
  await S('cart-cta', q('.empty-state .button, .empty-state a').filter({ hasText: /Explorer|products|boutique/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Empty-cart CTA', desc: 'The "Explorer nos produits" action in the empty state.', sel: '.empty-state .button' });
  save();
}

async function search() {
  if (!(await newPage('search', { wait: 9000 }))) return;
  const g = G.content;
  await S('search-title', q('h1, .heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search title', desc: 'The search results heading for ?q=douze.', sel: 'search .heading' }, { noScroll: true });
  await S('search-field', q('input[type="search"], input[name="q"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: "The search page's input, prefilled with \"douze\"; never re-submitted.", sel: 'input[name="q"]' });
  await S('search-result', q('product-item, [class*="search-result" i], .product-list product-item').filter({ visible: true }).first(), B4, { group: g, title: 'Search result card', desc: 'A product result in the search grid.', sel: 'search product-item' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(2000);
  await closePromo(page);
  await S('footer', q('footer.footer, footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The boxed footer section over its photo background: nav columns, the "La News Douze" Klaviyo signup and the locale selector.', sel: 'footer.footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer nav link.', sel: 'footer a' }, { noScroll: true });
  await S('newsletter-field', q('.klaviyo-form input[type="email"], .klaviyo-form input, footer input, .footer input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Newsletter field', desc: "The email input inside the footer's Klaviyo embed; focused only, never filled or submitted.", sel: '.klaviyo-form input[type=email]' }, { noScroll: true });
  await S('newsletter-button', q('.klaviyo-form button, footer .klaviyo-form [type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Newsletter button', desc: 'The signup submit inside the Klaviyo embed; measured, never pressed.', sel: '.klaviyo-form button' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram" i], footer a[href*="tiktok" i], footer a[href*="facebook" i], [class*="social" i] a, footer .footer a:has(svg)').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon link', desc: 'A social link, where the footer paints one (none in the captured DOM).', sel: 'footer social a' }, { noScroll: true });
  await S('locale-button', q('footer button, .footer button').filter({ hasText: /français|english|locale/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Locale button', desc: 'The FRANÇAIS locale selector in the footer.', sel: 'footer locale button' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('store-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The compact header at 390: hamburger, wordmark, cart.', sel: 'store-header at 390' }, { noScroll: true });
  const menu = q('button[aria-controls="mobile-menu-drawer"]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The hamburger toggle for the mobile-navigation drawer.', sel: 'button[aria-controls="mobile-menu-drawer"]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1800); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('mobile-navigation, [id="mobile-menu-drawer"], .drawer--from-left').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The from-left navigation drawer opened by its own toggle.', sel: 'mobile-navigation' }, { noScroll: true });
  await S('m-nav-item', q('mobile-navigation a, mobile-navigation button, [id="mobile-menu-drawer"] a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened navigation drawer.', sel: 'mobile-navigation a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero-title', q('.image-hero__heading.heading, [class*="image-hero" i] h1, [class*="image-hero" i] h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', desc: 'The Boogy hero heading at 390 (the hidden-tablet-and-up variant).', sel: '.image-hero__heading at 390' });
  await S('m-hero-cta', q('.image-hero__button .button, [class*="hero" i] a.button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero CTA', desc: 'The SHOP button at 390.', sel: '.image-hero__button at 390' });
  await S('m-product-card', q('product-item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile product card', desc: 'A product-item in the featured row at 390.', sel: 'product-item at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints light — the boxed sections sit on a sable page field';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, shop, product, trio, faq, story, login, cart, search, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on the element that animates (the scrolling banner's
  // inner track — the wrapper .moving-banner itself never animates, so reading
  // it cannot show a reduced-motion delta).
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.moving-banner__inner');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
