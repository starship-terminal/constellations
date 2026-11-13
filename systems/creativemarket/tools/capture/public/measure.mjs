// Measures creativemarket.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home category product search membership signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// creativemarket.com is a Rails/Vue storefront behind Cloudflare (Turnstile
// greets some routes — newPage waits it out on a fresh context per route, and
// a still-blocked route keeps its earlier readings). The CSS is Sass-compiled
// literals plus a component-scoped var layer (--btn-*, --default-*). The page
// paints one theme (<html data-theme="legacy">). Specs select by class
// fragment, role, aria-label or text. The /sign-in form is measured but Log In
// is never pressed; Add to cart, Buy now, checkout and downloads are never
// used. The only presses are local UI toggles: the mobile menu, the category
// filter accordion and FAQ-style toggles.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', category: '/fonts', product: '/SilverStag/7290900-Silver-Garden-Nostalgic-Font-Duo', search: '/search?q=font', membership: '/membership', signin: '/sign-in' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  // Cloudflare Turnstile can greet a route: wait it out, then one retry on a
  // fresh context before recording the route as blocked this run.
  let ok = false;
  for (let tries = 0; tries < 2 && !ok; tries++) {
    await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
    ok = !(await blocked());
    if (!ok && tries === 0) { log('  challenge, one reload', key); }
  }
  if (!ok) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
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
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|buy now|buy font|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
}

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
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the opened mobile nav overlay: the smallest visible ancestor that
// holds the category links and the Join / Log in actions.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div, nav, section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.height > innerHeight * 0.4 && r.width > innerWidth * 0.5
        && /FONTS|TEMPLATES|GRAPHICS/i.test(t) && t.length < 4000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks a product card: the first product link (/<shop>/<id>-<slug>, skipping
// the masthead promo anchor) walked up to its .product-card container — the
// real card boundary this storefront uses.
async function markProductCard(scope = 'body') {
  await page.evaluate((sc) => {
    const links = [...document.querySelectorAll(sc + ' a[href]')].filter((a) => {
      const h = a.getAttribute('href') || '';
      return /\/[^/]+\/\d{5,}-/.test(h) && !a.closest('.masthead-sale');
    });
    const a = links[0];
    if (!a) return;
    // .product-card wins over the nearer .product-thumbnail: the card also holds
    // the hover-mounted add-to-cart button in its inner container.
    const card = a.closest('.product-card, [class*="product-card"]') || a.closest('.product-thumbnail, [class*="thumbnail"], li') || a;
    card.setAttribute('data-m-mark', 'prodcard');
  }, scope);
}

// Marks the membership plan card: the smallest card-height ancestor whose text
// names a price and a billing word.
async function markPlanCard() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('main div, main section, main article, body div, body section')].filter((el) => {
      const t = (el.innerText || '').trim();
      const r = el.getBoundingClientRect();
      return /\$\d+|month|year|credit/i.test(t) && r.height > 250 && r.height < 900 && r.width > 200 && r.width < 560 && t.length < 2000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'plancard');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', category: 'Category', product: 'Product',
  search: 'Search', membership: 'Membership', signin: 'Sign-in', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('site-header', q('.site-header, .site-header-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar: All Categories dropdown, the 585px search field, Join | Log in, the amber Save 25% button and the cart icon.', sel: '.site-header' }, { noScroll: true });
  await S('logo', q('.site-header a[href="/"], header a[href="/"], a[class*="logo"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Creative Market logo anchor.', sel: 'logo anchor' }, { noScroll: true });
  await S('nav-search', q('form.search-field.site-header-search, form.site-header-search').filter({ visible: true }).first(), B4, { group: g, title: 'Nav search field', desc: 'The 585x44 header search (All Categories dropdown + field); never submitted.', sel: 'form.search-field' }, { noScroll: true });
  await S('join-link', q('a.user-link__link').filter({ hasText: /^\s*Join\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Join link', desc: 'The "Join" user link; measured, never followed.', sel: 'a.user-link__link' }, { noScroll: true });
  await S('save25-button', q('a.ui-button--accent, a.ui-button').filter({ hasText: /Save 25%/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Save 25% button', desc: 'The amber "Save 25%" ui-button--accent (92x32); measured, never followed.', sel: 'a.ui-button--accent' }, { noScroll: true });
  await S('cart-icon', q('.user-link__cart-icon, .badge-wrapper--cart, a[href*="cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart icon', desc: 'The header cart icon with its count badge.', sel: 'cart icon' }, { noScroll: true });
  await S('nav-link', q('.lower-nav a, .desktop-nav-wrapper a, nav a').filter({ hasText: /^\s*(FONTS|TEMPLATES|SALE|INSPIRATION|ENTERPRISE)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category nav link', desc: 'A lower-nav category item (FONTS/TEMPLATES/...); measured, never followed.', sel: '.lower-nav a' }, { noScroll: true });
  const h = G.home;
  await S('search-strip-heading', q('h2.homepage-smart-search-strip__heading, h2').filter({ hasText: /search fonts|new way to search/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Try a new way to search fonts" — the painted headline under the hidden h1.', sel: 'smart-search heading' });
  await S('row-title', q('h2.homepage-row-title').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A homepage row heading ("Popular Fonts").', sel: 'h2.homepage-row-title' });
  await lazyLoad();
  await markProductCard();
  await S('product-card', q('[data-m-mark="prodcard"]').filter({ visible: true }).first(), B4, { group: h, title: 'Product card', desc: 'A product card in a home row (artwork, name, shop, teal price pill); measured, never followed.', sel: '.product-card' });
  // The card's Add To Cart button only mounts/paints on card hover.
  await S('add-to-cart-btn', q('[data-m-mark="prodcard"] button.product-card-add-to-cart, button.product-card-add-to-cart').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card add-to-cart', desc: 'A product card\'s sp-button add-to-cart (paints on card hover); measured only — pressing it would change the cart.', sel: 'product-card-add-to-cart' },
    { open: async () => { const c = q('[data-m-mark="prodcard"]').first(); await c.scrollIntoViewIfNeeded().catch(() => {}); await c.hover().catch(() => {}); await page.waitForTimeout(700); }, noReset: true });
  await S('newsletter-field', q('input.email-sign-up-banner__email-input, input[type="email"]').filter({ visible: true }).first(), ['default', 'focus-visible', 'filled'], { group: h, title: 'Newsletter field', desc: 'The email banner input (368x31); filled with a placeholder, never submitted.', sel: 'email banner input' });
}

async function category() {
  if (!(await newPage('category'))) return;
  await sheetsFor('category');
  await chrome('category');
  const g = G.category;
  await S('category-h1', q('h1.category-page-header__title, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category headline', desc: '"Fonts" — the category page title.', sel: 'category h1' }, { noScroll: true });
  await S('filter-btn', q('button.open-filter-btn').filter({ visible: true }).first(), B4, { group: g, title: 'Filter button', desc: 'The "Browse by Category" filter disclosure; toggled locally.', sel: 'button.open-filter-btn' }, { noScroll: true });
  await S('filter-group', q('.filter-groups-container > *, .filter-groups-container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter groups', desc: 'The Classification/Style/Aesthetic filter column.', sel: '.filter-groups-container' });
  await lazyLoad();
  await markProductCard();
  await S('category-card', q('[data-m-mark="prodcard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Category product card', desc: 'A product thumbnail card in the category grid (image, name, shop); measured, never followed.', sel: 'product-thumbnail card' });
}

async function product() {
  if (!(await newPage('product'))) return;
  await sheetsFor('product');
  await chrome('product');
  const g = G.product;
  await S('product-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: '"Silver Garden - Nostalgic Font Duo" (h1.sp-h4).', sel: 'h1' });
  await S('shop-byline', q('.shop-info-details, [class*="shop-info"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop byline', desc: '"SilverStag Type Foundry | Featured" — the author row.', sel: '.shop-info-details' });
  await S('buy-box-price', q('.buy-box-price, .price-container').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', desc: 'The buy-box price ($79).', sel: '.buy-box-price' });
  await S('license-row', q('.checkbox-row, .checkbox-row-price').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'License row', desc: 'A license option row in the buy box (label + $79.00 price).', sel: '.checkbox-row' });
  await S('add-cart', q('button.btn--primary').filter({ hasText: /^\s*Add to cart\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Add to cart', desc: 'The primary buy-box button (450x45); measured only — never pressed.', sel: 'btn--primary Add to cart' });
  await S('buy-now', q('button.buy-box-actions__buy-now, button.btn--secondary').filter({ hasText: /^\s*Buy now\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Buy now', desc: 'The secondary buy-box button (450x40); measured only — never pressed.', sel: 'buy-box Buy now' });
  await S('enterprise-cta', q('button.buy-box-enterprise-cta').filter({ visible: true }).first(), B4, { group: g, title: 'Enterprise CTA', desc: '"Enterprise or Custom License / Contact sales" row (450x52).', sel: 'buy-box-enterprise-cta' });
  await S('follow-btn', q('button').filter({ hasText: /^\s*FOLLOW\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Follow button', desc: 'The shop FOLLOW button; measured, never pressed.', sel: 'FOLLOW button' });
  await lazyLoad();
  await S('specs', q('section.product-specs-section').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product Specs', desc: 'The Product Specs block: File Size, Vector, Web Font, creation date.', sel: 'section.product-specs-section' });
  await S('accordion-row', q('summary').filter({ hasText: /^\s*(Reviews|Comments|FAQs?)\s*$/i }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Accordion row', desc: 'A details/summary accordion row (Reviews/Comments/FAQs); opened state toggled locally, closed again.', sel: 'summary' }, { after: { opened: async (loc) => { try { await toggle(loc); } catch {} } } });
  await S('search-chip', q('a.sp-pill, .suggested-searches__pill-wrapper a').filter({ visible: true }).first(), B4, { group: g, title: 'Suggested-search chip', desc: 'A Suggested Searches pill (Serif, Script, Nostalgic...); measured, never followed.', sel: 'a.sp-pill' });
  await S('shop-card', q('.meet-the-shop__profile').filter({ visible: true }).first(), ['default'], { group: g, title: 'Meet the shop', desc: 'The shop profile card: avatar, name, bio, FOLLOW/MESSAGE, stats (joined, sales, rating).', sel: '.meet-the-shop' });
  await markProductCard();
  await S('related-card', q('[data-m-mark="prodcard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Related product card', desc: 'A card in "More from this shop"/"Similar Fonts"; measured, never followed. The rails rendered empty on this capture — recorded as a miss if absent.', sel: 'related card' });
}

async function search() {
  if (!(await newPage('search'))) return;
  await chrome('search');
  const g = G.search;
  await S('search-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search heading', desc: 'The results heading for ?q=font.', sel: 'results h1' }, { noScroll: true });
  await lazyLoad();
  await markProductCard();
  await S('result-card', q('[data-m-mark="prodcard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Result card', desc: 'A results-grid card; measured, never followed.', sel: 'result card' });
}

async function membership() {
  if (!(await newPage('membership'))) return;
  await chrome('membership');
  const g = G.membership;
  await S('membership-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Membership headline', desc: 'The membership page heading.', sel: 'membership h1' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Plan card', desc: 'A membership plan card (name, price, benefits, CTA); measured, never purchased.', sel: 'plan card' });
}

async function signin() {
  if (!(await newPage('signin'))) return;
  await chrome('signin');
  const g = G.signin;
  await S('signin-h1', q('h1, h2').filter({ hasText: /Welcome back/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in headline', desc: '"Welcome back to the world\'s marketplace for design".', sel: 'sign-in heading' }, { noScroll: true });
  await S('username-field', q('input[name="username"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focus-visible', 'filled'], { group: g, title: 'Username field', desc: 'The username text field; filled with a placeholder, never submitted.', sel: 'input[name=username]' });
  await S('password-field', q('input[type="password"], input[name="password"]').filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Password field', desc: 'The password field; never filled, never submitted.', sel: 'input[type=password]' });
  await S('login-btn', q('button, [type="submit"], a').filter({ hasText: /^\s*Log In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log In button', desc: 'The sign-in submit; measured only — pressing it would post credentials.', sel: 'Log In button' });
  await S('sso-btn', q('button, a').filter({ hasText: /Log In Using Google|Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO', desc: '"Log In Using Google"; measured, OAuth never followed.', sel: 'Google SSO button' });
}

async function footer() {
  if (!(await newPage('home'))) return;
  await chrome('home-footer');
  const g = G.footer;
  const ft = q('.c-site-footer__main, footer.c-site-footer').filter({ visible: true }).first();
  await ft.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', ft, ['default'], { group: g, title: 'Footer', desc: 'The footer: the logo/about column plus the five link sections (c-site-footer__main, 1376x322).', sel: '.c-site-footer__main' }, { noScroll: true });
  await S('footer-link', q('.c-site-footer__nav a, .c-site-footer__section a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link; measured, never followed.', sel: 'footer nav a' }, { noScroll: true });
  await S('social-icon', q('.c-site-footer__socials a, footer a[href*="instagram"], footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="youtube"], footer a[href*="facebook"], footer a[href*="pinterest"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social icon in the about column.', sel: 'footer socials a' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('.site-header, .site-header-wrapper, header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('button[data-testid="hamburger-menu-trigger"], button[aria-label*="menu" i], button[aria-label*="nav" i], [class*="hamburger"] button').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The header menu button that opens the nav overlay.', sel: 'header menu button' }, { noScroll: true });
  if (await menu.count()) {
    try {
      await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click()));
      await page.waitForTimeout(1600);
      await markMobileMenu();
    } catch (e) { log('  ! menu open failed', String(e.message).slice(0, 80)); }
  }
  await S('m-menu-open', q('[data-m-mark="mmenu"], .mobile-menu.mobile-nav__mobile-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened nav overlay (.mobile-menu).', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, .mobile-menu a, .mobile-menu button').filter({ hasText: /^\s*(FONTS|TEMPLATES|GRAPHICS|Join|Log in|SALE)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu row', desc: 'A row inside the opened nav overlay.', sel: 'mobile menu row' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.evaluate(() => document.querySelector('.mobile-menu-header__button--close-btn')?.dispatchEvent(new MouseEvent('click', { bubbles: true }))).catch(() => {});
  await page.waitForTimeout(600);
  await page.evaluate(() => { const c = [...document.querySelectorAll('h1,h2')].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 100 && r.height > 10; }); if (c[0]) c[0].setAttribute('data-m-mark', 'mhead'); });
  await S('m-heading', q('[data-m-mark="mhead"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile heading', sel: 'painted heading at 390' });
  await S('m-search', q('form.mobile-search-bar, form.search-field').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile search', desc: 'The mobile search bar; never submitted.', sel: 'mobile search-field' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); creativemarket.com paints a single "legacy" theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, category, product, search, membership, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // link), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.lower-nav a, .site-header a');
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
