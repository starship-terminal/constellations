// Shared helpers for the Epidemic Sound public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.epidemicsound.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

// Hide the cookie dialog. Never click Accept, Change cookie settings, or
// any consent control. The banner is #es-cookie-banner.
export async function hideCookies(context) {
  await context.addInitScript(() => {
    const kill = () => {
      const n = document.getElementById('es-cookie-banner');
      if (n) n.style.setProperty('display', 'none', 'important');
    };
    const start = () => {
      kill();
      new MutationObserver(kill).observe(document.documentElement, { childList: true, subtree: true });
    };
    if (document.documentElement) start();
    else document.addEventListener('DOMContentLoaded', start);
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await hideCookies(context);
  return { browser, context };
}

export async function open(page, url, { wait = 1600 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await page.evaluate(() => {
    const n = document.getElementById('es-cookie-banner');
    if (n) n.style.setProperty('display', 'none', 'important');
  });
}
