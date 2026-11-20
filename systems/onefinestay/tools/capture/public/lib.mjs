// Shared helpers for the onefinestay.com public captures.
// PRODUCT (adapt): onefinestay.com, signed out, one light theme.
import { createRequire } from 'node:module';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const pwPath = process.env.PLAYWRIGHT;
if (!pwPath) {
  console.error('set PLAYWRIGHT to a playwright index.mjs');
  process.exit(2);
}
const require = createRequire(pathToFileURL(path.resolve(pwPath)).href);
const pw = require(pwPath);
export const chromium = pw.chromium;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.onefinestay.com';

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({
    headless: true,
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

export async function isChallenge(page) {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText || '').slice(0, 500);
    return /performing security verification|verify you are human|just a moment/i.test(t)
      || document.title === 'Just a moment...';
  }).catch(() => true);
}
