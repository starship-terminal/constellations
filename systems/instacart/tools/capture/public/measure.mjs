// Measure Instacart public components and crop them at 2x.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and components/crops/{name}-{state}.png.
// Selectors are roles and visible text. Emotion classes are hashes and are
// not used. Login Continue is never clicked. Consent is never clicked.
// Add-to-cart is measured, never clicked.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, hideOverlays, open, styleOf, BASE } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const readings = [];

async function crop(locator, name) {
  const count = await locator.count().catch(() => 0);
  if (!count) {
    readings.push({ name, missing: true, reason: 'not found' });
    console.log('miss', name);
    return;
  }
  const box = await locator.boundingBox({ timeout: 8000 }).catch(() => null);
  if (!box || box.width < 2 || box.height < 2) {
    readings.push({ name, missing: true, box });
    console.log('miss', name, 'no box');
    return;
  }
  const file = path.join(CROPS, `${name}.png`);
  await locator.screenshot({ path: file, animations: 'disabled' }).catch(async () => {
    const page = locator.page();
    await page.screenshot({
      path: file,
      animations: 'disabled',
      clip: {
        x: Math.max(0, box.x - 4),
        y: Math.max(0, box.y - 4),
        width: Math.min(box.width + 8, 1400),
        height: Math.min(box.height + 8, 800),
      },
    });
  });
  const style = await styleOf(locator).catch(() => null);
  readings.push({ name, box, style, file: `components/crops/${name}.png` });
  console.log('crop', name, Math.round(box.w || box.width), Math.round(box.h || box.height));
}

async function states(locator, name) {
  await crop(locator, `${name}-default`);
  await locator.hover().catch(() => {});
  await locator.page().waitForTimeout(180);
  await crop(locator, `${name}-hover`);
  await locator.focus().catch(() => {});
  await locator.page().waitForTimeout(120);
  await crop(locator, `${name}-focus`);
}

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
const page = await context.newPage();

await open(page, BASE + '/');
const headerLogin = page.getByRole('link', { name: /^Log in$/ }).or(page.getByRole('button', { name: /^Log in$/ })).first();
const headerSignup = page.getByRole('link', { name: /Sign up|Get the app/ }).or(page.getByRole('button', { name: /Sign up/ })).first();
const search = page.getByPlaceholder(/Search products/i).or(page.getByRole('combobox')).first();
await states(headerSignup, 'button-primary');
await states(headerLogin, 'button-secondary');
await crop(search, 'search-default');
await search.click().catch(() => {});
await page.waitForTimeout(400);
await crop(search, 'search-focused');
const chip = page.getByRole('button', { name: 'EBT' }).or(page.getByRole('tab', { name: 'EBT' })).first();
await states(chip, 'chip');
const store = page.getByRole('link', { name: /Safeway/i }).first();
await crop(store, 'store-card-default');
await store.hover().catch(() => {});
await page.waitForTimeout(180);
await crop(store, 'store-card-hover');

await open(page, BASE + '/login');
const email = page.getByPlaceholder('Enter your email address');
const cont = page.getByRole('button', { name: 'Continue' });
await crop(page.locator('form').first(), 'login-card-default');
await states(email, 'text-field');
await states(cont, 'button-continue');
await crop(page.getByRole('button', { name: 'Google' }), 'button-social-google');
await crop(page.getByRole('button', { name: 'Phone' }), 'button-social-phone');

await open(page, BASE + '/grocery-delivery');
const zip = page.getByPlaceholder(/ZIP/i).first();
const shop = page.getByRole('button', { name: 'Shop' });
await crop(zip, 'zip-field-default');
await states(shop, 'button-shop');

await open(page, BASE + '/store/s?k=milk');
const add = page.getByRole('button', { name: /^Add$/ }).first();
await states(add, 'button-add');
const badge = page.getByText('Best seller').first();
await crop(badge, 'badge-bestseller');
const price = page.getByText(/^\$/).first();
await crop(price, 'price-default');

await open(page, BASE + '/help');
const row = page.getByRole('link', { name: /Adding a payment method/i }).or(page.getByText('Adding a payment method')).first();
await crop(row, 'list-row-default');
const connect = page.getByRole('button', { name: /Connect with Instacart/i }).first();
await crop(connect, 'button-help-default');

await open(page, BASE + '/business');
const create = page.getByRole('link', { name: /Create free business account/i }).or(page.getByRole('button', { name: /Create free business account/i })).first();
await states(create, 'button-business');

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  source: 'live DOM, public signed-out, 1440x900 at 2x crops',
  readings,
}, null, 2) + '\n');
console.log('readings', readings.length, 'missing', readings.filter((r) => r.missing).length);
await browser.close();
