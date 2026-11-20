// Shared helpers for the Buy Me a Coffee public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://buymeacoffee.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Hide a cookie or promo overlay if one mounts. Never click Accept.
export async function hideOverlays(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('.cky-consent-container, .cky-modal, #ckyBanner, [class*="cky-notice"]')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2200 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
}
