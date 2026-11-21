// Crops visible public controls. Does not submit forms or follow login.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, locale: 'en-US' });
const page = await ctx.newPage();
const log = (...a) => console.log(...a);

async function shot(name, locator) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) {
    log('miss', name);
    return false;
  }
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip });
  log('crop', name, Math.round(box.width), Math.round(box.height));
  return true;
}

await page.goto('https://www.shopify.com/?country=us&lang=en', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);

const start = page.locator('a[href*="admin.shopify.com/signup"]').filter({ hasText: 'Start for free' }).nth(1);
await shot('button-primary-default', start);
await start.hover();
await page.waitForTimeout(350);
await shot('button-primary-hover', start);
await page.mouse.move(2, 2);

const login = page.locator('header a[href*="/login"]').first();
await shot('link-login-default', login);
await login.hover();
await page.waitForTimeout(250);
await shot('link-login-hover', login);

const pricing = page.locator('header a[href="/pricing"]').first();
await shot('nav-link-default', pricing);
await pricing.hover();
await page.waitForTimeout(250);
await shot('nav-link-hover', pricing);

const logo = page.locator('header a[href="/"]').first();
await shot('logo-default', logo);

const why = page.locator('label[for="bk-nav-Why Shopify"]').first();
const box = await why.boundingBox();
await page.mouse.move(box.x + 30, box.y + 24);
await page.waitForTimeout(700);
await page.screenshot({ path: path.join(CROPS, 'menu-open.png'), clip: { x: 0, y: 0, width: 1440, height: 360 } });
const item = page.locator('a[href="/start"]').filter({ hasText: 'Get started fast' }).first();
await shot('menu-link-default', item);
await item.hover();
await page.waitForTimeout(250);
await shot('menu-link-hover', item);
await page.mouse.move(8, 860);
await page.waitForTimeout(300);

const region = page.locator('button[aria-controls="language-selector-popover"]').first();
await region.scrollIntoViewIfNeeded();
await shot('region-button-default', region);
await region.click();
await page.waitForTimeout(600);
const dlg = page.locator('#language-selector-popover');
const dbox = await dlg.boundingBox();
if (dbox) {
  await page.screenshot({
    path: path.join(CROPS, 'dialog-open.png'),
    clip: { x: Math.max(0, dbox.x), y: Math.max(0, dbox.y), width: Math.min(dbox.width, 900), height: Math.min(dbox.height, 640) },
  });
  log('crop dialog');
}
const close = dlg.getByRole('button', { name: /close/i }).first();
if (await close.count()) await shot('icon-button-default', close);
await page.keyboard.press('Escape');

await page.goto('https://www.shopify.com/pricing?country=us&lang=en', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
const sw = page.getByRole('switch').first();
await sw.scrollIntoViewIfNeeded();
await shot('switch-default', sw);
await sw.click();
await page.waitForTimeout(400);
await shot('switch-selected', sw);

const summary = page.locator('summary').first();
await summary.scrollIntoViewIfNeeded();
await shot('accordion-default', summary);
await summary.click();
await page.waitForTimeout(400);
await shot('accordion-open', summary);

log('done', fs.readdirSync(CROPS).length);
await browser.close();
