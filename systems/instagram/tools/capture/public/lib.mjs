// Shared helpers for the instagram.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// Scope is signed-out: the login wall, the email signup form at rest,
// about.instagram.com, help.instagram.com and a public profile if one loads.
// Cookie and consent layers are hidden, never clicked. Nothing is typed into
// a credential field, submitted, or followed into Facebook login.
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.instagram.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Meta sometimes mounts a cookie dialog. Hide it. Never click Allow or Decline.
export const HIDE_CONSENT =
  '[data-testid="cookie-policy-dialog"],[role="dialog"][aria-label*="cookie" i],[role="dialog"][aria-label*="Cookie" i],#cookie-banner,.cookie-banner{display:none!important;visibility:hidden!important;pointer-events:none!important}';

export async function patch(context) {
  await context.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const scale = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function hideConsent(page) {
  await page.addStyleTag({ content: HIDE_CONSENT }).catch(() => {});
}

export async function open(page, url, { wait = 4000 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(Math.min(wait, 2000));
  await hideConsent(page);
  await page.waitForTimeout(Math.max(0, wait - 2000));
  await hideConsent(page);
}

export async function setDark(page) {
  await page.evaluate(() => {
    document.documentElement.classList.remove('__fb-light-mode', '__ig-light-mode');
    document.documentElement.classList.add('__fb-dark-mode', '__ig-dark-mode');
  });
  await page.waitForTimeout(400);
}
