// Shared helpers for the Sonarworks public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.sonarworks.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.route('**/*cookie-script.com/**', (route) => route.abort());
  await context.route('**/*getsitecontrol.com/**', (route) => route.abort());
  return { browser, context };
}

// Hide CookieScript and GetSiteControl. Never click Got it, never submit a form.
export async function hideOverlays(page) {
  await page.addStyleTag({
    content: '#cookiescript_injected_wrapper,#cookiescript_injected,#cookiescript_badge,getsitecontrol-widget{display:none !important; pointer-events:none !important}',
  }).catch(() => {});
  await page.evaluate(() => {
    document.querySelectorAll('#cookiescript_injected_wrapper,#cookiescript_injected,#cookiescript_badge,getsitecontrol-widget').forEach((el) => el.remove());
  }).catch(() => {});
}

export async function open(page, url, { wait = 1800 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
  return resp;
}
