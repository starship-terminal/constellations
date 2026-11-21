// Dismiss the store offer dialog by its visible close control, then photograph
// the store home and the empty cart. Does not type an email or claim the offer.
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

async function shot(page, name, source) {
  await screenshotWithMetadata(page, { path: `${RAW}/${name}.png` }, {
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    sanitizedSourceUrl: source,
  });
  log('shot', name);
}

async function dismiss(page) {
  const how = await page.evaluate(() => {
    const dialog = [...document.querySelectorAll('div, aside, section')].find((el) => /Enjoy 10% Off/i.test(el.innerText || '') && el.getBoundingClientRect().width > 200 && el.getBoundingClientRect().width < 900);
    if (!dialog) return 'no dialog';
    const btn = [...dialog.querySelectorAll('button')].find((b) => {
      const label = (b.getAttribute('aria-label') || b.innerText || '').trim();
      return /close|no thanks/i.test(label) || b.querySelector('svg');
    });
    if (btn) { btn.click(); return 'clicked ' + (btn.getAttribute('aria-label') || btn.innerText || 'svg').slice(0, 40); }
    return 'dialog without close';
  });
  log('dismiss', how);
  await page.waitForTimeout(700);
  return how;
}

const browser = await chromium.launch({ channel: 'chrome', headless: false, args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
try {
  await page.goto('https://store.moma.org/', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2500);
  await dismiss(page);
  const still = await page.evaluate(() => /Enjoy 10% Off/i.test(document.body.innerText || ''));
  log('offer still visible', still);
  if (!still) await shot(page, 'store-light-default', 'https://store.moma.org/');
  else log('keeping the dialog shot; store home behind it is recorded in the listing');

  await page.goto('https://store.moma.org/cart', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2000);
  await dismiss(page);
  const cartStill = await page.evaluate(() => /Enjoy 10% Off/i.test(document.body.innerText || ''));
  const text = await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 200));
  log('cart offer', cartStill, text.slice(0, 140));
  if (!cartStill) await shot(page, 'store-cart-empty-light-default', 'https://store.moma.org/cart');
} finally {
  await browser.close();
}
