// Third pass: click Visit so the menu paints, wait for the store home hero,
// and open the empty cart. No typing, no checkout, no offer claim.
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
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

const browser = await chromium.launch({ channel: 'chrome', headless: false, args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();

try {
  await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2000);
  const visit = page.getByRole('button', { name: 'Visit', exact: true }).first();
  await visit.click();
  await page.waitForTimeout(800);
  const vis = await page.evaluate(() => {
    const el = document.getElementById('visit-nav');
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { visibility: s.visibility, opacity: s.opacity, h: Math.round(r.height), text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 120) };
  });
  log('visit after click', JSON.stringify(vis));
  if (vis && vis.visibility === 'visible' && vis.opacity !== '0') {
    await shot(page, 'home-light-visit-menu', 'https://www.moma.org/');
  } else {
    log('visit menu still hidden, leaving the earlier shot');
  }

  await page.goto('https://store.moma.org/', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2500);
  const close = page.locator('button[aria-label="Close"], button[aria-label="close"]').first();
  if (await close.count()) await close.click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(400);
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(2500);
  const hero = await page.evaluate(() => {
    const imgs = [...document.images].filter((img) => img.getBoundingClientRect().top < 700 && img.getBoundingClientRect().height > 80);
    return { n: imgs.length, complete: imgs.filter((i) => i.complete && i.naturalWidth > 0).length, title: document.title, href: location.pathname };
  });
  log('store hero', JSON.stringify(hero));
  await shot(page, 'store-light-default', 'https://store.moma.org/');

  await page.goto('https://store.moma.org/cart', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2000);
  const close2 = page.locator('button[aria-label="Close"], button[aria-label="close"]').first();
  if (await close2.count()) await close2.click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(600);
  const cart = await page.evaluate(() => ({ title: document.title, path: location.pathname, text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 280) }));
  log('cart', JSON.stringify(cart));
  if (/cart/i.test(cart.path) && !/card number|payment method/i.test(cart.text)) {
    await shot(page, 'store-cart-empty-light-default', 'https://store.moma.org/cart');
  }
} finally {
  await browser.close();
}
