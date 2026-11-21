// Recapture shots the first pass got wrong. Cookie notice stays hidden.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'digg', 'raw-shots');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const browser = await chromium.launch({ headless: true });

async function hide(page) {
  await page.addStyleTag({ content: 'section.cookie-notice{display:none!important;pointer-events:none!important}' });
}
async function shot(page, name, vw, vh, dpr) {
  await screenshotWithMetadata(page, { path: path.join(RAW, name) }, { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: page.url().split('?')[0] });
  console.log('shot', name, page.url());
}

// Phone light nav + phone dark feed (sheet closed) + phone feed menu
{
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto('https://digg.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1600);
  await hide(page);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  // close sheet if open
  const close = page.getByRole('button', { name: /Close|navigation/i });
  await shot(page, 'mobile-home-light-feed.png', 390, 844, 2);
  await page.getByRole('button', { name: 'Open navigation menu' }).click();
  await page.waitForTimeout(500);
  await shot(page, 'mobile-home-light-nav-open.png', 390, 844, 2);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);
  // theme to dark via sheet, then close sheet
  await page.getByRole('button', { name: 'Open navigation menu' }).click();
  await page.waitForTimeout(300);
  const theme = page.locator('button[aria-label*="Switch theme"]');
  for (let i = 0; i < 4; i++) {
    const cls = await page.evaluate(() => document.documentElement.className);
    if (cls.split(/\s+/).includes('dark')) break;
    await theme.click();
    await page.waitForTimeout(300);
  }
  await page.keyboard.press('Escape');
  await page.waitForTimeout(500);
  // click scrim if sheet still open
  await page.mouse.click(360, 400).catch(() => {});
  await page.waitForTimeout(400);
  const sheetOpen = await page.locator('[role="dialog"]').count();
  console.log('sheet after escape', sheetOpen, await page.evaluate(() => document.documentElement.className.split(' ').slice(-1)[0]));
  if (sheetOpen) {
    await page.keyboard.press('Escape');
    await page.locator('[data-slot="sidebar"] button, button[aria-label*="Close"]').first().click().catch(() => {});
    await page.waitForTimeout(300);
  }
  await shot(page, 'mobile-home-dark-feed.png', 390, 844, 2);
  await ctx.close();
}

// Desktop: hover signup, focus login, comfy display, digg button hover, cookie dialog via footer button (opens preferences, does not accept)
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto('https://digg.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1400);
  await hide(page);
  await page.locator('a[href*="/sign-up"]').filter({ hasText: 'Sign up' }).hover();
  await page.waitForTimeout(200);
  await shot(page, 'home-light-signup-hover.png', 1440, 900, 1);
  await page.locator('a[href*="/login"]').filter({ hasText: 'Log in' }).focus();
  await page.waitForTimeout(150);
  await shot(page, 'home-light-login-focus.png', 1440, 900, 1);
  // switch display to Comfy (a view state, not a form submit)
  await page.locator('button[aria-label^="Feed display"]').click();
  await page.waitForTimeout(300);
  await page.getByRole('option', { name: 'Comfy' }).click();
  await page.waitForTimeout(600);
  await shot(page, 'home-light-comfy.png', 1440, 900, 1);
  await ctx.close();
}

// Cookie preferences dialog: open from footer control. Do not click Accept.
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const page = await ctx.newPage();
  await page.goto('https://digg.com/about', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1200);
  // do not hide; click Cookie preferences if present, else Manage preferences on the notice
  const prefs = page.getByRole('button', { name: 'Cookie preferences' });
  const manage = page.getByRole('button', { name: 'Manage preferences' });
  if (await prefs.count()) {
    await prefs.first().click();
  } else if (await manage.count()) {
    await manage.first().click();
  }
  await page.waitForTimeout(700);
  await shot(page, 'about-light-cookie-preferences.png', 1440, 900, 1);
  const text = await page.evaluate(() => {
    const d = document.querySelector('[role="dialog"]');
    return d ? d.innerText.replace(/\s+/g, ' ').trim().slice(0, 400) : 'no dialog';
  });
  console.log('cookie dialog', text);
  await ctx.close();
}

await browser.close();
