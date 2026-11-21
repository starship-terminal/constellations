// Extra public states the first pass missed: signup overlay, phone menu, search focus.
// Nothing is typed or submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'letterboxd', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const browser = await chromium.launch();

async function shot(page, name, vw, vh, dpr, url) {
  await screenshotWithMetadata(page, { path: path.join(RAW, name) }, {
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    sanitizedSourceUrl: url,
  });
  console.log('shot', name);
}

{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto('https://letterboxd.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(1500);
  await page.locator('a[href="/create-account/"]').first().click();
  await page.waitForTimeout(1500);
  const vis = await page.locator('#cboxContent').isVisible().catch(() => false);
  console.log('signup overlay visible', vis);
  await shot(page, 'signup-light-default.png', 1440, 900, 1, 'https://letterboxd.com/create-account/');
  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);
  await page.locator('#search-q').click();
  await page.waitForTimeout(400);
  await shot(page, 'home-light-search-focused.png', 1440, 900, 1, 'https://letterboxd.com/');
  await ctx.close();
}

{
  const ctx = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const page = await ctx.newPage();
  await page.goto('https://letterboxd.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(1800);
  const info = await page.evaluate(() => {
    const els = [...document.querySelectorAll('button, a, .nav-toggle, .mobile-nav-toggle, .js-nav-toggle')];
    return els.filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && r.top < 80;
    }).map((el) => ({
      tag: el.tagName,
      cls: (el.className || '').toString().slice(0, 60),
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 30),
      w: Math.round(el.getBoundingClientRect().width),
    }));
  });
  console.log('phone header', JSON.stringify(info));
  const toggle = page.locator('a.nav-toggle, button.nav-toggle, .js-hide-in-app .mobile-menu, a[href="#nav"]').first();
  let opened = false;
  if (await toggle.count()) {
    await toggle.click().catch(() => {});
    opened = true;
  } else {
    const byLabel = page.getByRole('button', { name: /menu|navigation/i }).first();
    if (await byLabel.count()) {
      await byLabel.click().catch(() => {});
      opened = true;
    }
  }
  await page.waitForTimeout(700);
  console.log('menu opened attempt', opened);
  await shot(page, 'mobile-home-light-menu.png', 390, 844, 2, 'https://letterboxd.com/');
  await ctx.close();
}

await browser.close();
console.log('extra done');
