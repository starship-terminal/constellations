// Click each header menu and wait until its panel text is visible, then shoot.
// Does not follow Tickets, Donate, Log in, or Store.
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

const browser = await chromium.launch({ channel: 'chrome', headless: false, args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
try {
  await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1800);
  const menus = [
    ['Exhibitions and events', 'exhibitions-and-events-nav', 'home-light-exhibitions-menu'],
    ['Art and artists', 'art-and-artists-nav', 'home-light-art-menu'],
    ['Search', 'search-nav', 'home-light-search'],
    ['Membership', 'membership-menu', 'home-light-membership-menu'],
  ];
  for (const [name, id, file] of menus) {
    await page.keyboard.press('Escape').catch(() => {});
    await page.mouse.move(8, 700);
    await page.waitForTimeout(200);
    const btn = page.getByRole('button', { name, exact: true }).first();
    await btn.click();
    await page.waitForTimeout(700);
    const vis = await page.evaluate((panelId) => {
      const el = document.getElementById(panelId);
      if (!el) return null;
      const s = getComputedStyle(el);
      return { visibility: s.visibility, opacity: s.opacity, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100) };
    }, id);
    log(name, JSON.stringify(vis));
    if (vis && vis.visibility === 'visible' && Number(vis.opacity) > 0.4 && vis.text.length > 2) {
      await screenshotWithMetadata(page, { path: `${RAW}/${file}.png` }, {
        viewport: { width: 1440, height: 900 },
        deviceScaleFactor: 1,
        sanitizedSourceUrl: 'https://www.moma.org/',
      });
      log('shot', file);
    } else {
      log('skip', file);
    }
  }
} finally {
  await browser.close();
}
