// Screenshots of calendly.com's public pages. Cookie banner is hidden, never clicked.
// Identity providers are not opened. Forms are not submitted. Nothing is typed.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(PKG, 'raw', 'full');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return context;
}

async function hideCookies(page) {
  await page.addStyleTag({ content: '#onetrust-consent-sdk,#onetrust-banner-sdk{display:none!important}' }).catch(() => {});
}

async function shot(page, name, requested, sourceUrl) {
  const sanitizedSourceUrl = sourceUrl ? sourceUrl.split('?')[0] : null;
  await screenshotWithMetadata(page, { path: path.join(RAW, name + '.png') }, { ...requested, sanitizedSourceUrl });
  console.log('shot', name);
}

const desktop = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const mobile = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };

const pages = [
  ['home', 'https://calendly.com/'],
  ['pricing', 'https://calendly.com/pricing'],
  ['scheduling', 'https://calendly.com/scheduling'],
  ['integrations', 'https://calendly.com/integration'],
  ['customers', 'https://calendly.com/customers'],
  ['blog', 'https://calendly.com/blog'],
  ['about', 'https://calendly.com/about'],
  ['help', 'https://calendly.com/help'],
  ['contact', 'https://calendly.com/contact-us'],
  ['login', 'https://calendly.com/login'],
  ['signup', 'https://calendly.com/signup'],
  ['app-signup', 'https://calendly.com/app/signup'],
  ['app-login', 'https://calendly.com/app/login'],
  ['booking', 'https://calendly.com/calendly'],
  ['booking-event', 'https://calendly.com/calendly/ts?back=1'],
];

const ctx = await contextFor(false);
for (const [name, url] of pages) {
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await page.waitForTimeout(2200);
    await hideCookies(page);
    await shot(page, name + '-light-default', desktop, url);
    if (['home', 'pricing', 'login', 'signup'].includes(name)) {
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      if (h > 0 && h < 8000) await shot(page, name + '-light-full', { ...desktop, fullPage: true }, url);
      else console.log('skip full', name, h);
    }
  } catch (e) {
    console.log('FAIL', name, String(e.message).split('\n')[0]);
  }
  await page.close();
}

// Header menu overlay.
{
  const page = await ctx.newPage();
  await page.goto('https://calendly.com/', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1800);
  await hideCookies(page);
  await page.locator('#site-header nav').getByRole('button', { name: 'Product', exact: true }).first().hover();
  await page.waitForTimeout(600);
  await shot(page, 'home-light-product-menu', desktop, 'https://calendly.com/');
  await page.keyboard.press('Escape');
  await page.mouse.move(700, 860);
  await page.waitForTimeout(300);
  await page.locator('#site-header nav').getByRole('button', { name: 'Solutions', exact: true }).first().hover();
  await page.waitForTimeout(500);
  await shot(page, 'home-light-solutions-menu', desktop, 'https://calendly.com/');
  await page.close();
}

// Pricing billing toggle if one exists. Do not start a checkout.
{
  const page = await ctx.newPage();
  await page.goto('https://calendly.com/pricing', { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1800);
  await hideCookies(page);
  const toggle = page.getByRole('button', { name: /annual|yearly|monthly|billed/i }).first();
  if (await toggle.count()) {
    await toggle.click().catch(() => {});
    await page.waitForTimeout(500);
    await shot(page, 'pricing-light-billing', desktop, 'https://calendly.com/pricing');
  } else {
    console.log('no billing toggle');
  }
  const faq = page.locator('button[aria-expanded="false"]').filter({ hasText: /.+/ }).first();
  if (await faq.count()) {
    await faq.click().catch(() => {});
    await page.waitForTimeout(400);
    await shot(page, 'pricing-light-faq', desktop, 'https://calendly.com/pricing');
  }
  await page.close();
}
await ctx.close();

const mctx = await contextFor(true);
for (const [name, url] of [['home', 'https://calendly.com/'], ['pricing', 'https://calendly.com/pricing'], ['login', 'https://calendly.com/login']]) {
  const page = await mctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await page.waitForTimeout(2000);
    await hideCookies(page);
    await shot(page, 'mobile-' + name + '-light-default', mobile, url);
    if (name === 'home') {
      const menu = page.getByRole('button', { name: 'Open menu' }).first();
      if (await menu.count()) {
        await menu.click();
        await page.waitForTimeout(600);
        await shot(page, 'mobile-home-light-menu', mobile, url);
      }
    }
  } catch (e) {
    console.log('FAIL mobile', name, String(e.message).split('\n')[0]);
  }
  await page.close();
}
await browser.close();
console.log('done');
