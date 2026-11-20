// Crop IKEA Singapore controls from a live page. Never clicks Add to cart or consent.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
import { execFileSync } from 'node:child_process';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
const PYTHON = process.env.PYTHON || 'python3';

async function save(page, locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) { console.log('miss', name); return; }
  const file = path.join(CROPS, name + '.png');
  const pad = 6;
  await page.screenshot({
    path: file,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 900),
      height: Math.min(box.height + pad * 2, 400),
    },
  });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert('RGB')
im.save(${JSON.stringify(file)}, 'PNG', optimize=True)
`], { stdio: 'ignore' });
  } catch {}
  console.log('crop', name, Math.round(box.width), Math.round(box.height));
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  locale: 'en-SG',
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});
const page = await ctx.newPage();
const hide = async () => page.addStyleTag({ content: '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter{display:none!important}' }).catch(() => {});

await page.goto('https://www.ikea.com/sg/en/p/billy-bookcase-white-00522047/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2800);
await hide();
const add = page.locator('button.pipf-btn--emphasised').first();
await add.scrollIntoViewIfNeeded();
await save(page, add, 'button-primary-default');
await add.hover();
await page.waitForTimeout(200);
await save(page, add, 'button-primary-hover');
await add.focus();
await page.waitForTimeout(150);
await save(page, add, 'button-primary-focus');
const fav = page.locator('button.pipf-favourite-button').first();
await save(page, fav, 'icon-button-default');
const qty = page.locator('input[name="pipf-quantity-stepper-input"]').first();
await save(page, qty, 'quantity-default');
await qty.focus();
await save(page, qty, 'quantity-focus');
const search = page.locator('input[name="q"]').first();
await save(page, search, 'search-default');
await search.focus();
await save(page, search, 'search-focus');
const h1 = page.locator('h1').first();
await save(page, h1, 'product-title-default');
const price = page.locator('[class*="pipcom-price"]').first();
await save(page, price, 'price-default');

await page.goto('https://www.ikea.com/sg/en/search/?q=lamp', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2500);
await hide();
const card = page.locator('a[href*="/sg/en/p/"]').nth(2);
await card.scrollIntoViewIfNeeded().catch(() => {});
await save(page, card, 'product-card-default');
const sort = page.getByRole('button', { name: 'Sort' }).first();
await save(page, sort, 'sort-default');

await page.goto('https://www.ikea.com/sg/en/profile/login/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2200);
await hide();
const field = page.locator('input[type="email"], input[type="text"]').first();
await save(page, field, 'text-field-default');
await field.focus();
await save(page, field, 'text-field-focus');
const heading = page.locator('h1').first();
await save(page, heading, 'login-heading-default');

await page.goto('https://www.ikea.com/sg/en/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2000);
await hide();
const logo = page.getByRole('link', { name: /IKEA logotype/i }).first();
await save(page, logo, 'logo-default');
const products = page.getByRole('link', { name: 'Products', exact: true }).first();
await save(page, products, 'nav-link-default');

await browser.close();
console.log('crops', fs.readdirSync(CROPS).length);
