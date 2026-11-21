// Measures nothing.tech public controls. Does not submit forms or open login.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const RAW = path.join(REF, 'raw');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PROPS = ['fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform', 'color', 'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderRadius', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width', 'boxShadow', 'outlineWidth', 'outlineColor', 'outlineOffset'];

async function dismiss(page) {
  await page.evaluate(() => document.querySelectorAll('#didomi-host, .didomi-popup-backdrop, [class*="didomi-popup"]').forEach((n) => n.remove()));
  const stay = page.getByRole('button', { name: /stay on/i });
  if (await stay.count().catch(() => 0)) {
    await stay.first().click({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(300);
    await page.evaluate(() => document.querySelectorAll('#didomi-host, .didomi-popup-backdrop').forEach((n) => n.remove()));
  }
}

async function read(page, handle) {
  return handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of props) o[p] = s[p];
    return o;
  }, PROPS);
}

async function crop(page, handle, name) {
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  return file;
}

async function states(page, handle, id) {
  const out = {};
  out.default = await read(page, handle);
  await crop(page, handle, id + '-default');
  await handle.hover({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(200);
  out.hover = await read(page, handle);
  await crop(page, handle, id + '-hover');
  await handle.focus().catch(() => {});
  await page.waitForTimeout(150);
  out['focus-visible'] = await read(page, handle);
  await crop(page, handle, id + '-focus-visible');
  await page.evaluate((el) => el.blur(), await handle.elementHandle()).catch(() => {});
  return out;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-GB' });
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await context.newPage();
const components = {};

async function go(url) {
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1200);
  await dismiss(page);
  if (/account\.nothing\.tech/i.test(page.url())) return false;
  return true;
}

await go('/');
const promo = page.locator('header a').filter({ hasText: /black friday/i }).first();
if (await promo.count()) components['promo-bar'] = { page: '/', states: await states(page, promo, 'promo-bar') };
const shop = page.getByRole('link', { name: /shop now/i }).first();
if (await shop.count()) components['hero-cta'] = { page: '/', states: await states(page, shop, 'hero-cta') };
const audio = page.locator('header nav a').filter({ hasText: /^audio$/i }).first();
if (await audio.count()) components['nav-link'] = { page: '/', states: await states(page, audio, 'nav-link') };
const cart = page.locator('button[aria-label*="Cart"]').first();
if (await cart.count()) components['cart-button'] = { page: '/', states: await states(page, cart, 'cart-button') };

// open audio menu without navigating
await page.evaluate(() => {
  const a = [...document.querySelectorAll('header nav a')].find((el) => /audio/i.test((el.innerText || '').trim()));
  if (!a) return;
  a.addEventListener('click', (e) => e.preventDefault(), { capture: true });
  a.click();
});
await page.waitForTimeout(700);
await dismiss(page);
const menuLink = page.locator('a[href="/collections/headphones"]').filter({ hasText: /headphones/i }).first();
if (await menuLink.count() && (await menuLink.boundingBox())?.y < 700) {
  components['menu-link'] = { page: '/', states: await states(page, menuLink, 'menu-link') };
}
await page.screenshot({ path: path.join(osShot(), 'menu-audio-measure.png') }).catch(() => {});

await go('/products/headphone-1-pro');
const add = page.getByRole('button', { name: /add to (bag|cart)/i }).first();
if (await add.count()) components['add-to-bag'] = { page: '/products/headphone-1-pro', states: await states(page, add, 'add-to-bag') };
const price = page.locator('main').getByText(/£\d/).first();
if (await price.count()) {
  components['price'] = { page: '/products/headphone-1-pro', states: { default: await read(page, price) } };
  await crop(page, price, 'price-default');
}

await go('/pages/contact-support');
const field = page.locator('input:visible, textarea:visible').first();
if (await field.count()) components['text-field'] = { page: '/pages/contact-support', states: await states(page, field, 'text-field') };

await go('/');
await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight || 4000));
await page.waitForTimeout(400);
const footerLink = page.locator('footer a').filter({ hasText: /^about$/i }).first();
if (await footerLink.count()) components['footer-link'] = { page: '/', states: await states(page, footerLink, 'footer-link') };

const out = {
  _meta: { read: '2026-11-21', viewport: '1440 x 900', tool: 'tools/capture/public/measure.mjs', url: BASE },
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('components', Object.keys(components).join(', '));
await browser.close();

function osShot() {
  return path.join(process.env.HOME, '.design-systems', 'nothing', 'raw-shots');
}
