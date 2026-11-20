// Measures LEGO shop components on public pages. Never signs in, never adds
// to bag, never submits search or the footer email field.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, closePromo, styleOf, crop, centre, RAW, BASE } from './lib.mjs';
import { datePrior } from '../merge-dates.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

// Start from the committed readings: a run that fails part-way, or is blocked
// before it reads anything, keeps every component and state it did not reach.
// _meta.captured is this run's date; every state carries its own `read` date, so
// a reading kept after a timed-out visit keeps the date it was taken (merge-dates.mjs).
const prior = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : null;
const RUN = new Date().toLocaleDateString('en-CA');
const components = datePrior((prior && prior.components) || {}, prior && prior._meta && prior._meta.captured);
const failedPages = [];

// Written after every page, so a later failure keeps what was already read.
function save() {
  const payload = {
    _meta: {
      product: 'LEGO',
      source: 'https://www.lego.com/en-us',
      captured: RUN, // the local date of the latest run; per-state dates are under <component>.<state>.read
      failedPages: failedPages.length ? failedPages : undefined,
      route: 'public-web',
      viewport: { width: 1440, height: 900, dpr: 1 },
      note: 'Signed out. Consent hidden, never clicked. Add to Bag measured, never pressed. Search text typed and cleared; Enter never pressed.',
    },
    components,
  };
  fs.writeFileSync(OUT, JSON.stringify(payload, null, 1) + '\n');
}

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
  const old = components[name][state];
  if (style && style.error && old && old.style && !old.style.error) {
    components[name][state] = { ...old, recaptureError: style.error, recaptureRun: RUN }; // keep the prior reading and its date
  } else {
    components[name][state] = { style, crop: cropPath, page: page.url().split('?')[0], read: RUN };
  }
  log('  ok', name, state, style && style.style && style.style.backgroundColor);
}

// Before every state: pointer to the top-right corner and focus dropped, so a
// focus-visible reading carries no hover and a pressed reading no focus ring
// (the kit's S() does the same).
async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.mouse.move(1440 - 2, 2).catch(() => {});
  await page.waitForTimeout(150);
}

async function hover(name, locator) {
  const loc = locator.first();
  if (!(await loc.count()) || !(await loc.isVisible().catch(() => false))) return;
  await reset();
  await centre(loc);
  await loc.hover({ timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(350);
  await record(name, 'hover', loc);
}

async function focusVis(name, locator) {
  const loc = locator.first();
  if (!(await loc.count())) return;
  await reset();
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
  await reset();
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
}

async function states(name, locator, { press = true, focus = false } = {}) {
  // One failing state is logged and skipped; it never loses the rest of the run.
  const step = async (label, fn) => { try { await fn(); } catch (e) { log('  fail', name, label, String(e.message).slice(0, 120)); } };
  await reset();
  await step('default', () => record(name, 'default', locator));
  await step('hover', () => hover(name, locator));
  if (focus) await step('focus-visible', () => focusVis(name, locator));
  if (press) await step('pressed', () => pressed(name, locator));
}

// Each page block runs on its own: a failure is logged, the components read so
// far are saved, and the next page still runs.
async function section(label, fn) {
  try { await fn(); } catch (e) { failedPages.push(label); log('page fail', label, String(e.message).slice(0, 160)); }
  save();
}

// Home
await section('home', async () => {
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
});

// Theme listing
await section('listing', async () => {
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
});

// Product
await section('product', async () => {
  await open(page, '/en-us/product/dump-truck-front-end-loader-60494', { wait: 4500 });
  await record('pdp-title', 'default', page.locator('h1').first());
  await record('pdp-price', 'default', page.locator('[data-test="product-price-display-price"]').first());
  await states('pdp-add', page.locator('[data-test="add-to-cart-skroll-cta"]').first(), { focus: true });
  await states('quantity', page.locator('[data-test="product-overview-quantity"]'), { press: false, focus: true });
  await record('accordion', 'default', page.locator('[data-test="accordion-summary"]').first());
  await page.locator('[data-test="accordion-summary"]').first().click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(400);
  await record('accordion', 'open', page.locator('[data-test="accordion"]').first());
});

// Help
await section('help', async () => {
  await open(page, '/en-us/service', { wait: 3500 });
  await record('help-heading', 'default', page.locator('h1').first());
  const helpSearch = page.locator('input[type="search"], input[placeholder*="Search" i], input[aria-label*="Search" i]').last();
  await states('help-search', helpSearch, { press: false, focus: true });
});

// Search results (query in the URL, field not submitted by us beyond the public URL)
await section('search', async () => {
  await open(page, '/en-us/search?q=city', { wait: 3500 });
  await record('search-heading', 'default', page.locator('h1').first());
  await record('search-result', 'default', page.locator('[data-test="product-leaf"]').first());
});

// Type into search then clear. Enter is never pressed.
await section('search-typed', async () => {
  await open(page, '/en-us', { wait: 3000 });
  const field = page.locator('[data-test="quick-search-input-input-field"]');
  await field.click({ timeout: 3000 }).catch(() => {});
  await field.fill('city').catch(() => {});
  await page.waitForTimeout(400);
  await record('search-field', 'filled', field);
  await field.fill('').catch(() => {});
});

log('wrote', OUT, 'components', Object.keys(components).length);
await browser.close();
if (failedPages.length) {
  console.error('pages that failed (their earlier readings were kept):', failedPages.join(', '));
  process.exitCode = 1;
}
