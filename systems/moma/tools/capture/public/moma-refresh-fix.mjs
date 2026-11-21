// Second pass for shots that painted blank on the first headed Chrome launch.
// Waits for images, dismisses the store offer dialog by its close control
// (does not type an email, does not claim the offer), and photographs the
// store, the listing, the empty search, the footer, and the Visit menu.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

function assertNotChallenge(title, text) {
  if (/just a moment|attention required|verify you are human/i.test(`${title}\n${(text || '').slice(0, 300)}`) && !/MoMA/i.test(title)) {
    const e = new Error('STOP: challenge page');
    e.code = 3;
    throw e;
  }
}

async function settle(page) {
  await page.waitForLoadState('networkidle', { timeout: 12000 }).catch(() => {});
  await page.waitForTimeout(1800);
  await page.evaluate(async () => {
    const imgs = [...document.images].slice(0, 12);
    await Promise.all(imgs.map((img) => img.complete ? null : new Promise((r) => { img.onload = img.onerror = r; setTimeout(r, 2500); })));
  });
}

async function dismissStoreOffer(page) {
  const close = page.locator('button[aria-label="Close"], button[aria-label="close"], .klaviyo-close-form, button.needsclick').first();
  if (await close.count()) {
    await close.click({ timeout: 2500 }).catch(() => {});
    await page.waitForTimeout(400);
    return 'clicked close';
  }
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(300);
  return 'escape';
}

async function shot(page, name, source, full = false) {
  const requested = {
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    sanitizedSourceUrl: source,
  };
  await screenshotWithMetadata(page, { path: `${RAW}/${name}.png`, fullPage: full }, requested);
  log('shot', name);
}

const browser = await chromium.launch({ channel: 'chrome', headless: false, args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();

try {
  await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  assertNotChallenge(await page.title(), await page.evaluate(() => document.body.innerText.slice(0, 200)));
  const visit = page.getByRole('button', { name: 'Visit', exact: true }).first();
  await visit.hover();
  await page.waitForTimeout(700);
  const panel = page.locator('#visit-nav');
  await panel.waitFor({ state: 'visible', timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(400);
  const vis = await page.evaluate(() => {
    const el = document.getElementById('visit-nav');
    if (!el) return null;
    const s = getComputedStyle(el);
    return { visibility: s.visibility, opacity: s.opacity, text: (el.innerText || '').slice(0, 80) };
  });
  log('visit panel', JSON.stringify(vis));
  await shot(page, 'home-light-visit-menu', 'https://www.moma.org/');
  await page.mouse.move(8, 700);
  await page.waitForTimeout(200);
  await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(600);
  await shot(page, 'home-light-footer', 'https://www.moma.org/');

  await page.goto('https://store.moma.org/collections/new', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await settle(page);
  assertNotChallenge(await page.title(), await page.evaluate(() => document.body.innerText.slice(0, 200)));
  log('store title', await page.title(), 'href', page.url().split('?')[0]);
  log('dismiss', await dismissStoreOffer(page));
  await page.waitForTimeout(600);
  await page.evaluate(async () => {
    const imgs = [...document.images].filter((img) => img.getBoundingClientRect().top < 900);
    await Promise.all(imgs.map((img) => img.complete ? null : new Promise((r) => { img.onload = img.onerror = r; setTimeout(r, 3000); })));
  });
  await shot(page, 'store-listing-light-default', 'https://store.moma.org/collections/new');
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  log('listing height', H);
  if (H > 1000) await shot(page, 'store-listing-light-full', 'https://store.moma.org/collections/new', true);

  await page.goto('https://store.moma.org/', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await settle(page);
  log('dismiss home', await dismissStoreOffer(page));
  await page.waitForTimeout(500);
  await shot(page, 'store-light-default', 'https://store.moma.org/');

  await page.goto('https://store.moma.org/search?q=zzzznotaproduct999', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await settle(page);
  log('dismiss empty', await dismissStoreOffer(page));
  await page.waitForTimeout(500);
  await shot(page, 'store-search-empty-light-default', 'https://store.moma.org/search?q=zzzznotaproduct999');

  await page.goto('https://store.moma.org/cart', { waitUntil: 'domcontentloaded', timeout: 40000 });
  await settle(page);
  log('cart', await page.title(), page.url().split('?')[0]);
  log('dismiss cart', await dismissStoreOffer(page));
  const cartText = await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 240));
  log('cart text', cartText);
  if (!/checkout|payment|card number/i.test(cartText) || /empty|0 item/i.test(cartText)) {
    await shot(page, 'store-cart-empty-light-default', 'https://store.moma.org/cart');
  }
} catch (e) {
  log('FAILED', e.message);
  if (e.code === 3) process.exitCode = 3;
  else throw e;
} finally {
  await browser.close();
}
