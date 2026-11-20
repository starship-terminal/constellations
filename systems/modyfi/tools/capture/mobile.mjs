// Mobile-only pass. Desktop readings already exist. 390x844 at 1x.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const SHOTS = path.join(os.homedir(), '.design-systems', 'modyfi', 'raw-shots');
fs.mkdirSync(SHOTS, { recursive: true });
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PAGES = {
  home: '20250219221151/https://www.modyfi.com/',
  about: '20241210063443/https://www.modyfi.com/about',
  modifiers: '20250416105018/https://www.modyfi.com/modifiers',
};
const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 1,
  isMobile: true,
  hasTouch: true,
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
});
const page = await context.newPage();
for (const [key, spec] of Object.entries(PAGES)) {
  console.log('mobile', key);
  await page.goto('https://web.archive.org/web/' + spec, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(3000);
  await page.evaluate(() => {
    document.querySelectorAll('#wm-ipp-base, #wm-ipp, [id^="wm-ipp"]').forEach((x) => x.style.setProperty('display', 'none', 'important'));
  });
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 };
  const file = path.join(SHOTS, `mobile-${key}-dark-default.png`);
  await screenshotWithMetadata(page, { path: file }, requested);
  console.log('  shot', key, await page.evaluate(() => [innerWidth, innerHeight, devicePixelRatio].join('x')));
}
await browser.close();
