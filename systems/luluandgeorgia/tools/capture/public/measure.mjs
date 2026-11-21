// Measures luluandgeorgia.com public components without signing in,
// adding to cart, or submitting a form.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { BASE, launch, hideOverlays, open, styleOf, crop, centre, RAW, clearChallenge } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Written mid-run outside the repo; OUT is replaced only when the whole run finishes, so a page
// that fails part-way never leaves the committed readings missing every later component.
const PARTIAL = path.join(os.tmpdir(), 'luluandgeorgia-components-computed.partial.json');
const out = { _meta: { product: 'Lulu and Georgia', site: BASE, captured: new Date().toISOString().slice(0, 10), route: 'public signed-out' }, components: {}, foundations: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');
page.setDefaultTimeout(8000);

async function go(url) {
  log('open', url);
  // A bot check that never clears stops the run: the challenge page is not the storefront.
  if (!(await open(page, url.startsWith('http') ? url : BASE + url, { wait: 4000 }))) throw new Error(`challenge did not clear on ${url}`);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(300);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, opts = {}) {
  const target = loc.filter({ visible: true }).first();
  const c = (out.components[key] ??= { states: {}, title: opts.title, group: opts.group, selector: opts.sel });
  if (!(await target.count())) {
    c.states[state] = { error: 'missing' };
    log('  ! missing', key, state);
    return;
  }
  try {
    if (opts.scroll !== false) await centre(target);
    // Start every state from rest: pointer away, nothing focused, so a focus reading is not a
    // hover+focus mix left over from the state before it.
    await page.mouse.move(1, 1);
    await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur());
    await page.waitForTimeout(150);
    let undo;
    let via;
    if (state === 'hover') {
      await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true }));
      await page.waitForTimeout(350);
    } else if (state === 'focus') {
      // A keyboard focus, so :focus-visible applies; a failed one is recorded as failed, never as
      // a state that draws no ring.
      await target.evaluate((el) => el.focus());
      await page.keyboard.press('Shift+Tab');
      await page.keyboard.press('Tab');
      await page.waitForTimeout(250);
      const ok = await target.evaluate((el) => document.activeElement === el && el.matches(':focus-visible'));
      via = ok ? 'keyboard focus (Shift+Tab, Tab)' : 'focus failed';
    } else if (state === 'pressed') {
      undo = await forcePseudo(target, ['active', 'hover']);
    }
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, opts.pad ?? 10); } catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    c.states[state] = { ...s, crop: file, ...(via ? { via } : {}) };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.backgroundColor, s.color, s.fontSize);
    if (undo) await undo();
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function readFoundations() {
  out.foundations = await page.evaluate(() => {
    const cs = (el) => el ? getComputedStyle(el) : null;
    const body = cs(document.body);
    const h1 = document.querySelector('h1');
    const nav = [...document.querySelectorAll('header a, nav a')].find((a) => a.getBoundingClientRect().width > 40 && a.getBoundingClientRect().height > 8 && a.getBoundingClientRect().height < 40);
    const promo = document.querySelector('.cf-promobar, [class*="promobar"], [class*="announcement"]');
    const promoLink = document.querySelector('.cf-promobar a, [class*="promobar"] a');
    const search = document.querySelector('input.marqo-header-search__input');
    const atc = [...document.querySelectorAll('button')].find((b) => /add to cart/i.test(b.innerText || ''));
    const heroCta = [...document.querySelectorAll('a,button')].find((a) => /shop bestsellers/i.test(a.innerText || ''));
    const sale = [...document.querySelectorAll('a')].find((a) => (a.innerText || '').trim() === 'SALE' && a.getBoundingClientRect().width > 10);
    const card = document.querySelector('a[href*="/products/"]');
    const price = document.querySelector('[class*="price"]:not(.js-subtotal)');
    const faces = [...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family + ' ' + f.weight);
    const sample = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        fontFamily: s.fontFamily, fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing, color: s.color, backgroundColor: s.backgroundColor,
        borderRadius: s.borderRadius, borderTop: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
        padding: s.padding, height: Math.round(r.height), boxShadow: s.boxShadow.slice(0, 160),
      };
    };
    return {
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      body: sample(document.body),
      htmlBg: getComputedStyle(document.documentElement).backgroundColor,
      h1: sample(h1),
      nav: sample(nav),
      promo: sample(promo),
      promoLink: sample(promoLink),
      search: sample(search),
      heroCta: sample(heroCta),
      sale: sample(sale),
      atc: sample(atc),
      card: sample(card),
      price: sample(price),
      header: sample(document.querySelector('header')),
      faces: [...new Set(faces)].slice(0, 30),
    };
  });
}

// ---- home ----
await go('/');
await readFoundations();
await measure('nav-link', 'default', page.locator('header a, nav a').filter({ hasText: 'FURNITURE' }), { title: 'Category link', group: 'link' });
await measure('nav-link', 'hover', page.locator('header a, nav a').filter({ hasText: 'FURNITURE' }), { title: 'Category link', group: 'link' });
await measure('sale-link', 'default', page.locator('a').filter({ hasText: /^SALE$/ }), { title: 'Sale link', group: 'link' });
await measure('search', 'default', page.locator('input.marqo-header-search__input'), { title: 'Search field', group: 'text field' });
await measure('search', 'focus', page.locator('input.marqo-header-search__input'), { title: 'Search field', group: 'text field' });
await measure('icon-account', 'default', page.locator('button.js-account-toggle'), { title: 'Account icon button', group: 'icon button', pad: 6 });
await measure('icon-cart', 'default', page.locator('a.js-cart-drawer-toggle, a.cart-drawer-toggle').first(), { title: 'Bag icon button', group: 'icon button', pad: 6 });
await measure('hero-cta', 'default', page.getByRole('link', { name: /shop bestsellers/i }), { title: 'Hero button', group: 'button' });
await measure('hero-cta', 'hover', page.getByRole('link', { name: /shop bestsellers/i }), { title: 'Hero button', group: 'button' });
const promo = page.locator('.cf-promobar, [class*="promobar"]').first();
await measure('promo-bar', 'default', promo, { title: 'Announcement bar', group: 'badge', scroll: false });

// Focus only. Do not type a query and do not submit.
const search = page.locator('input.marqo-header-search__input').first();
await search.click();
await page.waitForTimeout(400);

// account drawer (local toggle, not a sign-in)
await page.locator('button.js-account-toggle').first().click();
await page.waitForTimeout(700);
await measure('account-link', 'default', page.getByRole('link', { name: /sign in \/ create account/i }), { title: 'Account drawer link', group: 'link' });
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

// cart drawer, empty, no add
await page.locator('a.js-cart-drawer-toggle, a.cart-drawer-toggle').first().click();
await page.waitForTimeout(700);
await measure('cart-drawer', 'empty', page.locator('[class*="cart-drawer"], [class*="drawer"]').filter({ hasText: /bag|cart/i }).first(), { title: 'Cart drawer', group: 'dialog', pad: 0 });
await page.keyboard.press('Escape');

fs.writeFileSync(PARTIAL, JSON.stringify(out, null, 1) + '\n');

// ---- collection ----
await go('/collections/furniture');
await measure('product-card', 'default', page.locator('a[href*="/products/"]').filter({ has: page.locator('img') }).first(), { title: 'Product card', group: 'card', pad: 4 });
const badge = page.locator('[class*="badge"], [class*="label"]').filter({ hasText: /new|sale|exclusive/i }).first();
await measure('badge', 'default', badge, { title: 'Product badge', group: 'badge', pad: 4 });
const filterBtn = page.getByRole('button', { name: /filter/i }).first();
await measure('filter-btn', 'default', filterBtn, { title: 'Filter button', group: 'button' });
await readFoundations();
out.foundations.collection = await page.evaluate(() => ({
  title: document.title,
  h1: document.querySelector('h1') && getComputedStyle(document.querySelector('h1')).fontFamily,
  h1size: document.querySelector('h1') && getComputedStyle(document.querySelector('h1')).fontSize,
  h1text: document.querySelector('h1') && document.querySelector('h1').innerText.slice(0, 80),
}));

// ---- product ----
await go('/products/sachs-dining-table');
await measure('atc', 'default', page.locator('button.js-add-to-cart, button.button-cta').filter({ hasText: /add to cart/i }).first(), { title: 'Add to cart', group: 'button' });
await measure('atc', 'hover', page.locator('button.js-add-to-cart, button.button-cta').filter({ hasText: /add to cart/i }).first(), { title: 'Add to cart', group: 'button' });
await measure('atc', 'pressed', page.locator('button.js-add-to-cart, button.button-cta').filter({ hasText: /add to cart/i }).first(), { title: 'Add to cart', group: 'button' });
await measure('atc', 'focus', page.locator('button.js-add-to-cart, button.button-cta').filter({ hasText: /add to cart/i }).first(), { title: 'Add to cart', group: 'button' });
await measure('product-title', 'default', page.locator('h1').first(), { title: 'Product title', group: 'type' });
await measure('variant-select', 'default', page.locator('select.product-variants, select.js-select-variants').first(), { title: 'Variant select', group: 'select' });
await measure('qty', 'default', page.locator('input.js-counter-quantity, input[name="quantity"]').first(), { title: 'Quantity field', group: 'text field' });
const wishlist = page.locator('button').filter({ hasText: /wishlist/i }).first();
await measure('wishlist', 'default', wishlist, { title: 'Wishlist icon button', group: 'icon button' });
out.foundations.product = await page.evaluate(() => {
  const price = [...document.querySelectorAll('[class*="price"], .product-price, [data-product-price]')].find((e) => /\$\d/.test(e.innerText || '') && e.getBoundingClientRect().height > 8);
  const s = price ? getComputedStyle(price) : null;
  const qty = document.querySelector('button.js-counter-plus, button.js-counter-minus, [class*="quantity"] button');
  return {
    title: document.title,
    priceText: price ? price.innerText.trim().slice(0, 40) : null,
    price: s && { color: s.color, fontSize: s.fontSize, fontFamily: s.fontFamily, fontWeight: s.fontWeight },
    h1: document.querySelector('h1') && {
      font: getComputedStyle(document.querySelector('h1')).fontFamily,
      size: getComputedStyle(document.querySelector('h1')).fontSize,
      color: getComputedStyle(document.querySelector('h1')).color,
    },
  };
});

// ---- login (do not submit) ----
await go('/account/login');
const email = page.locator('input[type="email"], input#CustomerEmail, input[name="customer[email]"]').first();
const pass = page.locator('input[type="password"]').first();
const submit = page.locator('button').filter({ hasText: /continue with shop/i }).first();
await measure('login-email', 'default', email, { title: 'Login email', group: 'text field' });
await measure('login-email', 'focus', email, { title: 'Login email', group: 'text field' });
// Photograph the email empty. Do not type, submit, or click Continue with shop.
await measure('login-password', 'default', pass, { title: 'Login password', group: 'text field' });
await measure('login-submit', 'default', submit, { title: 'Sign in button', group: 'button' });
await measure('login-submit', 'hover', submit, { title: 'Sign in button', group: 'button' });
// do not click submit
out.foundations.login = await page.evaluate(() => ({
  title: document.title,
  url: location.pathname,
  hasForm: !!document.querySelector('form'),
  text: (document.body.innerText || '').slice(0, 300),
}));

// motion sample from computed transitions on the home CTA
await go('/');
out.foundations.motion = await page.evaluate(() => {
  const els = [...document.querySelectorAll('a, button, header')].slice(0, 40);
  const found = [];
  for (const el of els) {
    const s = getComputedStyle(el);
    if (s.transitionDuration && s.transitionDuration !== '0s' && s.transitionProperty !== 'none') {
      found.push({
        tag: el.tagName,
        text: (el.innerText || '').trim().slice(0, 30),
        property: s.transitionProperty,
        duration: s.transitionDuration,
        timing: s.transitionTimingFunction,
      });
    }
  }
  return found.slice(0, 12);
});

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
fs.rmSync(PARTIAL, { force: true });
log('wrote', OUT);
await browser.close();
