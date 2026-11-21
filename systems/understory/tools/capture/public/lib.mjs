// Shared helpers for the understory.io public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://understory.io';

export const HERE = path.dirname(new URL(import.meta.url).pathname);

// understory.io marketing pages are Webflow. Dropdowns are .w-dropdown,
// tabs are .w-tab-link, the phone drawer is .w-nav-button. Selectors key
// off those classes and visible labels, never account text.
export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  // Cookie Information banner (#coiOverlay) covers the page and intercepts
  // clicks. Hide only. Never click Accept or Decline (those POST consent).
  await context.route(/cookieinformation\.com|cookieinfo\.net/, (r) => r.abort());
}

export async function hideConsent(page) {
  await page.evaluate(() => {
    for (const sel of ['#coiOverlay', '#cookie-information-template-wrapper', '#Coi-Renew']) {
      document.querySelectorAll(sel).forEach((n) => n.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function settle(page) {
  await page.waitForTimeout(1800);
  const title = await page.title();
  const body = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 240));
  const blocked = /just a moment/i.test(title) || /verify you are human|checking your browser/i.test(body);
  return { title, blocked, url: page.url() };
}
