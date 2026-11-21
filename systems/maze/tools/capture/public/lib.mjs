// Shared helpers for the maze.co public captures. Run with PLAYWRIGHT pointing
// at a Playwright install (index.mjs) when this directory has no node_modules.
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://maze.co';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// maze.co is a Gatsby marketing site in one light theme. The CookieYes banner
// is hidden, never accepted. Login (auth.maze.co) and signup are not opened.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function hideConsent(page) {
  await page.evaluate(() => {
    for (const sel of ['.cky-consent-container', '#cookieyes-banner', '.cky-overlay', '.cky-modal', '#ckyPreferenceCenter']) {
      document.querySelectorAll(sel).forEach((el) => el.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(wait);
  return res ? res.status() : 0;
}

export function isWall(url) {
  try {
    const u = new URL(url);
    return u.hostname === 'auth.maze.co' || /\/login|\/signup/.test(u.pathname);
  } catch {
    return false;
  }
}
