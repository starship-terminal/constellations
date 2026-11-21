// Measure IKEA public components. No form submit, no login, no store or country change.
// PLAYWRIGHT=... node tools/capture/public/measure.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, hideConsent, openPublic, BASE, PKG } from './lib.mjs';

const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PROPS = [
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderRadius',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'width', 'boxShadow', 'outline', 'textTransform',
];

async function readStyle(loc) {
  return loc.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = s[p];
    const r = el.getBoundingClientRect();
    o._box = { x: r.x, y: r.y, w: r.width, h: r.height };
    return o;
  }, PROPS);
}

async function crop(page, loc, file) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return false;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 400),
  };
  await page.screenshot({ path: file, clip });
  return true;
}

async function states(page, key, loc) {
  const out = {};
  const el = loc.first();
  if (!(await el.count())) return out;
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  out.default = await readStyle(el);
  await crop(page, el, path.join(CROPS, `${key}-default.png`));
  await el.hover().catch(() => {});
  await page.waitForTimeout(350);
  out.hover = await readStyle(el);
  await crop(page, el, path.join(CROPS, `${key}-hover.png`));
  await el.focus().catch(() => {});
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  await page.waitForTimeout(250);
  out['focus-visible'] = await readStyle(el);
  await crop(page, el, path.join(CROPS, `${key}-focus-visible.png`));
  return out;
}

const browserPack = await launch({ width: 1440, height: 900 });
const page = await browserPack.context.newPage();
const components = {};
try {
  await openPublic(page, BASE + '/sg/en/', { wait: 2500 });
  await hideConsent(page);
  await page.evaluate(() => {
    document.querySelectorAll('#onetrust-consent-sdk, .onetrust-pc-dark-filter, [class*="cookie"]').forEach((n) => n.remove());
  });
  const specs = {
    'nav-link': page.locator('a.hnf-menu__entrypoint').filter({ hasText: 'Products' }).first(),
    'search-field': page.locator('#ikea-search-input'),
    'header-icon': page.locator('a.hnf-btn[href*="/cart/"]').first(),
    'login-link': page.locator('a.hnf-btn[href*="/profile/"]').first(),
    'category-card': page.locator('a[href*="/cat/storage-organisation"]').first(),
    'primary-cta': page.locator('a.pub__btn, a[class*="pub__btn"]').filter({ hasText: 'Explore the Christmas shop' }).first(),
  };
  for (const [key, loc] of Object.entries(specs)) {
    try {
      components[key] = { page: 'home', url: BASE + '/sg/en/', states: await states(page, key, loc) };
      console.log('measured', key, Object.keys(components[key].states));
    } catch (e) {
      console.log('miss', key, e.message.split('\n')[0]);
      components[key] = { page: 'home', error: e.message.split('\n')[0], states: {} };
    }
  }
  await page.goto(BASE + '/sg/en/cat/sofas-armchairs-700640/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  await hideConsent(page);
  const plp = {
    'filter-button': page.getByRole('button', { name: /Filter/i }).first(),
    'product-card': page.locator('a[href*="/p/"]').first(),
    'sort-control': page.getByRole('button', { name: /Sort/i }).first(),
  };
  for (const [key, loc] of Object.entries(plp)) {
    try {
      if (!(await loc.count())) { components[key] = { page: 'plp', missing: true, states: {} }; continue; }
      components[key] = { page: 'plp', url: page.url(), states: await states(page, key, loc) };
      console.log('measured', key);
    } catch (e) {
      components[key] = { page: 'plp', error: e.message.split('\n')[0], states: {} };
    }
  }
  await page.goto(BASE + '/sg/en/p/vinterfint-artificial-christmas-tree-in-outdoor-green-60636381/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  await hideConsent(page);
  const add = page.locator('button').filter({ hasText: /^Add to cart$/ }).first();
  if (await add.count()) {
    components['add-to-bag'] = { page: 'pdp', url: page.url(), states: await states(page, 'add-to-bag', add) };
    console.log('measured add-to-bag');
  } else {
    components['add-to-bag'] = { page: 'pdp', missing: true, states: {} };
  }
  const price = page.locator('[class*="price__integer"], [class*="pip-price"]').first();
  if (await price.count()) {
    components.price = { page: 'pdp', states: { default: await readStyle(price) } };
    await crop(page, price, path.join(CROPS, 'price-default.png'));
  }
} finally {
  await browserPack.browser.close();
}

const out = {
  _meta: {
    product: 'IKEA Singapore',
    captured: '2026-11-21',
    source: 'computed styles on www.ikea.com/sg/en public pages, signed out',
    theme: 'light',
    widths: [1440],
  },
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote', Object.keys(components).length);
