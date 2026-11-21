// Shared helpers for the Trip.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// Headless Chromium is redirected to verify.trip.com (an icon-order captcha).
// Installed Chrome (channel: 'chrome', headless) loads the public site.
// www.trip.com geo-redirects to sg.trip.com/?locale=en-sg from this network.
// The language suggestion is a dialog (.online-language-match). It is hidden,
// never clicked, so no language preference is submitted.
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

export const BASE = 'https://sg.trip.com';
export const ENTRY = 'https://www.trip.com/';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const AUTH_RE = /signin|signup|\/login|register|account\/signin|passport\/|oauth|accounts\.google|appleid|auth\.trip/i;
export const CAPTCHA_RE = /verify\.trip\.com|verification test/i;

export function isAuth(url) {
  return AUTH_RE.test(url || '');
}
export function isCaptcha(url, title = '') {
  return CAPTCHA_RE.test(url || '') || /verification/i.test(title || '');
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-SG', timezoneId: 'Asia/Singapore' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-SG', timezoneId: 'Asia/Singapore' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Hide the language suggestion. Never click it (that would pick a language).
export async function hideLanguage(page) {
  await page.evaluate(() => {
    document.querySelectorAll('.online-language-match').forEach((n) => {
      n.style.setProperty('display', 'none', 'important');
    });
  }).catch(() => {});
}

export async function open(page, url, { wait = 4500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideLanguage(page);
  const title = await page.title().catch(() => '');
  const finalUrl = page.url();
  return {
    status: resp && resp.status(),
    url: finalUrl,
    title,
    auth: isAuth(finalUrl),
    captcha: isCaptcha(finalUrl, title),
  };
}
