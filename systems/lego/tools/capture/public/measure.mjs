// Measures LEGO shop components on public pages. Never signs in, never adds
// to bag, never submits search or the footer email field.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, closePromo, styleOf, crop, centre, RAW, BASE } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const components = {};

async function record(name, state, locator) {
  const n = await locator.count().catch(() => 0);
  if (!n) { log('  miss', name, state); return; }
  const loc = locator.first();
  if (!(await loc.isVisible().catch(() => false))) { log('  hidden', name, state); return; }
  await centre(loc);
  const style = await styleOf(loc).catch((e) => ({ error: String(e.message).slice(0, 160) }));
  let cropPath = null;
  try { cropPath = await crop(page, loc, `${name}-${state}`); } catch (e) { log('  crop fail', name, state, String(e.message).slice(0, 120)); }
  components[name] ??= {};
  components[name][state] = { style, crop: cropPath, page: page.url().split('?')[0] };
  log('  ok', name, state, style && style.style && style.style.backgroundColor);
}

async function hover(name, locator) {
  const loc = locator.first();
  if (!(await loc.count()) || !(await loc.isVisible().catch(() => false))) return;
  await centre(loc);
  await loc.hover({ timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(350);
  await record(name, 'hover', loc);
}

async function focusVis(name, locator) {
  const loc = locator.first();
  if (!(await loc.count())) return;
  await loc.focus().catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await loc.focus().catch(() => {});
  await page.waitForTimeout(200);
  await record(name, 'focus-visible', loc);
}

async function pressed(name, locator) {
  const loc = locator.first();
  if (!(await loc.count())) return;
  const handle = await loc.elementHandle();
  if (!handle) return;
  const node = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => null);
  try {
    await loc.evaluate((el) => el.setAttribute('data-m-press', '1'));
    const doc = await cdp.send('DOM.getDocument');
    const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-m-press="1"]' });
    if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['hover', 'active'] });
    await page.waitForTimeout(120);
    await record(name, 'pressed', page.locator('[data-m-press="1"]'));
    if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
  } catch (e) {
    log('  press fail', name, String(e.message).slice(0, 100));
  }
  await page.evaluate(() => document.querySelectorAll('[data-m-press]').forEach((n) => n.removeAttribute('data-m-press'))).catch(() => {});
  void node;
}

async function states(name, locator, { press = true, focus = false } = {}) {
  await record(name, 'default', locator);
  await hover(name, locator);
  if (focus) await focusVis(name, locator);
  if (press) await pressed(name, locator);
}

// Home
await open(page, '/en-us', { wait: 4000 });
await states('nav-shop', page.locator('header button').filter({ hasText: /^Shop$/ }), { focus: true });
await states('search-field', page.locator('[data-test="quick-search-input-input-field"]'), { press: false, focus: true });
await states('account-button', page.locator('[data-test="account"]'), { focus: true });
await states('wishlist-button', page.locator('[data-test="wishlist"]'), { focus: true });
await states('bag-link', page.getByRole('link', { name: /bag/i }), { focus: true });
await states('logo', page.locator('a[aria-label="Home"], header a[href="/en-us"]').first(), { press: false });
const banner = page.locator('[data-test="sitewide-banner-cta"], [class*="sitewide__banner"]').first();
await record('promo-banner', 'default', banner);

// Open Shop mega menu (a disclosure, not a navigation away)
await page.locator('header button').filter({ hasText: /^Shop$/ }).first().click({ timeout: 4000 }).catch(() => {});
await page.waitForTimeout(600);
await record('mega-menu', 'open', page.locator('[class*="level-two"], [class*="mega"], nav').filter({ hasText: /Themes/ }).first());
await page.keyboard.press('Escape').catch(() => {});

// Theme listing
await open(page, '/en-us/themes/city', { wait: 4000 });
await record('page-heading', 'default', page.locator('h1').first());
await states('filter-button', page.locator('[data-test="action-filter-button"]'), { focus: true });
await states('sort-button', page.locator('[data-test="action-sort-button"]'), { focus: true });
await states('product-card', page.locator('[data-test="product-leaf"]').first(), { press: false });
await states('product-title', page.locator('[data-test="product-leaf-title"]').first(), { press: false });
await states('product-price', page.locator('[data-test="product-leaf-price"]').first(), { press: false });
await states('add-to-bag', page.locator('[data-test="add-to-cart-skroll-cta"]').first(), { focus: true });
await states('wishlist-icon', page.locator('[data-test="wishlist-skroll-icon-button"]').first(), { focus: true });
await record('badge', 'default', page.locator('[data-test="product-leaf-badge"]').first());

// Open filter panel (a disclosure)
await page.locator('[data-test="action-filter-button"]').first().click({ timeout: 4000 }).catch(() => {});
await page.waitForTimeout(700);
await record('filter-panel', 'open', page.locator('[role="dialog"], [class*="filter"]').filter({ hasText: /Age|Price|Theme/ }).first());
await page.keyboard.press('Escape').catch(() => {});

// Product
await open(page, '/en-us/product/dump-truck-front-end-loader-60494', { wait: 4500 });
await record('pdp-title', 'default', page.locator('h1').first());
await record('pdp-price', 'default', page.locator('[data-test="product-price-display-price"]').first());
await states('pdp-add', page.locator('[data-test="add-to-cart-skroll-cta"]').first(), { focus: true });
await states('quantity', page.locator('[data-test="product-overview-quantity"]'), { press: false, focus: true });
await record('accordion', 'default', page.locator('[data-test="accordion-summary"]').first());
await page.locator('[data-test="accordion-summary"]').first().click({ timeout: 3000 }).catch(() => {});
await page.waitForTimeout(400);
await record('accordion', 'open', page.locator('[data-test="accordion"]').first());

// Help
await open(page, '/en-us/service', { wait: 3500 });
await record('help-heading', 'default', page.locator('h1').first());
const helpSearch = page.locator('input[type="search"], input[placeholder*="Search" i], input[aria-label*="Search" i]').last();
await states('help-search', helpSearch, { press: false, focus: true });

// Search results (query in the URL, field not submitted by us beyond the public URL)
await open(page, '/en-us/search?q=city', { wait: 3500 });
await record('search-heading', 'default', page.locator('h1').first());
await record('search-result', 'default', page.locator('[data-test="product-leaf"]').first());

// Type into search then clear. Enter is never pressed.
await open(page, '/en-us', { wait: 3000 });
const field = page.locator('[data-test="quick-search-input-input-field"]');
await field.click({ timeout: 3000 }).catch(() => {});
await field.fill('city').catch(() => {});
await page.waitForTimeout(400);
await record('search-field', 'filled', field);
await field.fill('').catch(() => {});

const payload = {
  _meta: {
    product: 'LEGO',
    source: 'https://www.lego.com/en-us',
    captured: '2026-11-18',
    route: 'public-web',
    viewport: { width: 1440, height: 900, dpr: 1 },
    note: 'Signed out. Consent hidden, never clicked. Add to Bag measured, never pressed. Search text typed and cleared; Enter never pressed.',
  },
  components,
};
fs.writeFileSync(OUT, JSON.stringify(payload, null, 1) + '\n');
log('wrote', OUT, 'components', Object.keys(components).length);
await browser.close();
