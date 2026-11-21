// Shared helpers for the forhims.co.uk public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.forhims.co.uk';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Styled-components hashes change between deploys. Match the stable prefix
// (buttonstyles__Frame, global-navigationstyles__NavButton) and never the hash.
export const M = (prefix) => `[class*="${prefix}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  // Ketch consent SDK. Aborting it keeps the banner from mounting. No Accept
  // or Customise button is clicked, and no consent record is posted.
  await context.route(/ketchcdn\.com|cdn\.ketchjs\.com|global\.ketchcdn\.com/, (r) => r.abort());
}

export async function hideConsent(page) {
  await page.evaluate(() => {
    document.querySelectorAll('[class*="ketch"], [id*="ketch"], #lanyard_root').forEach((n) => n.remove());
  }).catch(() => {});
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-GB' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-GB' });
  await patch(context);
  return { browser, context };
}

export function scratchDir() {
  const dir = process.env.RAW || path.join(os.homedir(), '.design-systems', 'forhims', 'raw-shots');
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

// A login, signup or assessment URL. The capture stops that branch.
export function isWall(url) {
  return /app\.forhims\.co\.uk|\/customer\/login|\/login|\/sign-?up|\/flow\//i.test(url || '');
}
