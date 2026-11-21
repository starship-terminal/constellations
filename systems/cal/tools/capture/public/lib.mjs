// Shared helpers for the Cal.com public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const PYTHON = process.env.PYTHON || 'python3';
export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://cal.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const AUTH_RE = /app\.cal\.com|\/auth\/|\/signup|\/login|accounts\.google|login\.microsoftonline|github\.com\/login|appleid\.apple|saml/i;

export async function launch() {
  const browser = await chromium.launch({ headless: true });
  return { browser };
}

export async function contextFor(browser, { mobile = false } = {}) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await ctx.route('**/*', (route) => {
    const u = route.request().url();
    if (/onetrust|cookiebot|cookielaw|consent\.cookie|privacy-mgmt|trustarc|osano|iubenda|cdn\.cookielaw|geolocation\.onetrust/i.test(u)) {
      return route.abort();
    }
    return route.continue();
  });
  return ctx;
}

export async function hideBanners(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('#onetrust-banner-sdk, #onetrust-consent-sdk, .cky-consent-container, [id*="cookie-banner"], [class*="cookie-banner"]')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

export function isAuth(url) {
  return AUTH_RE.test(url || '');
}
