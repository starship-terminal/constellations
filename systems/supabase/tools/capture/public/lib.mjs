// Shared helpers for the Supabase public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

export const HERE = path.dirname(fileURLToPath(import.meta.url));

export function launchBrowser() {
  return chromium.launch({ headless: true });
}

export function desktopContext(browser) {
  return browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
    colorScheme: 'dark',
  });
}

export function mobileContext(browser) {
  return browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
    colorScheme: 'dark',
  });
}

// Hide consent overlays. Never click a consent button.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const sels = [
      '#onetrust-banner-sdk', '#onetrust-consent-sdk', '.onetrust-pc-dark-filter',
      '#ot-sdk-btn-floating', '.ot-sdk-container',
      '[class*="osano"]', '[id*="cookie-banner"]', '[id*="cookieBanner"]',
    ];
    for (const s of sels) {
      document.querySelectorAll(s).forEach((el) => {
        el.style.setProperty('display', 'none', 'important');
        el.setAttribute('data-capture-hidden', 'consent');
      });
    }
  }).catch(() => {});
}

const WALL = /supabase\.com\/dashboard|accounts\.google\.com|github\.com\/login|appleid\.apple\.com|login\.microsoftonline\.com/i;

export function isWall(url) {
  return WALL.test(url);
}

export async function openPublic(page, url, { wait = 1800 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  return { status: resp ? resp.status() : 0, url: page.url(), wall: isWall(page.url()) };
}
