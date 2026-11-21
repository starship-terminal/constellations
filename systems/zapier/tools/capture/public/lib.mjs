// Shared helpers for the zapier.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
// PRODUCT: Zapier. Public marketing site only. Never type, submit, or click an identity provider.
const ADAPTED_FOR = 'zapier';

import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://zapier.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Marketing classes are stable prefixes (zapier-marketing-ui-*), not hashed modules.
export const M = (name) => `[class*="${name}"]`;

export const WALL = /\/(app\/login|sign-up|signup|register|google-sso|oauth|sso|auth)\b/i;

export function stripUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.toString();
  } catch {
    return String(url).split('?')[0].split('#')[0];
  }
}

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function blocked(page) {
  const s = await page.evaluate(() => ({
    title: document.title,
    body: ((document.body && document.body.innerText) || '').slice(0, 500),
  })).catch(() => ({ title: '', body: '' }));
  return /just a moment|attention required|verify you are human|checking your browser|you have been blocked|access denied|performing security verification/i.test(s.title + '\n' + s.body);
}

// Hide a consent or promo overlay. Never click Accept or Reject.
export async function hideOverlays(page) {
  await page.evaluate(() => {
    const sel = [
      '#onetrust-banner-sdk',
      '[id*="onetrust" i]',
      '[class*="onetrust" i]',
      '[id*="cookie" i]',
      '[class*="cookie" i]',
      '[class*="consent" i]',
      '[id*="termly" i]',
      'iframe[title*="privacy" i]',
      '[aria-label*="cookie" i]',
      'iframe[src*="accounts.google.com"]',
      'iframe[src*="gsi"]',
      '#credential_picker_container',
      '[id*="credential_picker" i]',
    ].join(',');
    document.querySelectorAll(sel).forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
    });
    // Google One Tap paints a "Sign in with Google" sheet without a click.
    // Hide it. Never click Continue on it.
    for (const el of document.querySelectorAll('div, iframe, section')) {
      const t = (el.innerText || '').slice(0, 180);
      if (/Sign in to Zapier with Google/i.test(t) && el.getBoundingClientRect().height > 40 && el.getBoundingClientRect().height < 420) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2800 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
  return res;
}
