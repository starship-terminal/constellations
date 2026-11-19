// Recapture the FAQ page with one accordion row open, and the desktop nav menu.
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, BASE, clearChallenge, closePromo, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'helloklean', 'raw-shots');
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-SG' });
await patch(ctx);
const page = await ctx.newPage();
const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };

await page.goto(BASE + '/en-int/pages/faqs', { waitUntil: 'domcontentloaded', timeout: 90000 });
await clearChallenge(page);
await page.waitForTimeout(4000);
await closePromo(page);
// Close a leftover nav drawer if the previous click left one open.
await page.keyboard.press('Escape');
await page.waitForTimeout(400);
await page.evaluate(() => {
  document.querySelectorAll('[class*="menu"][class*="open"], [class*="drawer"]').forEach((el) => {
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' && el.getBoundingClientRect().width > 200) el.style.setProperty('display', 'none', 'important');
  });
});
const rows = page.locator('button, summary').filter({ hasText: /what is hard water/i });
console.log('faq rows', await rows.count());
if (await rows.count()) {
  await rows.first().click();
  await page.waitForTimeout(800);
}
await screenshotWithMetadata(page, { path: `${RAW}/faq-light-open.png` }, requested);
console.log('faq open shot');

await page.goto(BASE + '/en-int', { waitUntil: 'domcontentloaded', timeout: 90000 });
await clearChallenge(page);
await page.waitForTimeout(3000);
await closePromo(page);
const menu = page.getByRole('button', { name: /open menu|menu/i }).first();
if (await menu.count()) {
  await menu.click();
  await page.waitForTimeout(900);
  await screenshotWithMetadata(page, { path: `${RAW}/home-light-menu.png` }, requested);
  console.log('menu shot');
}
await browser.close();
