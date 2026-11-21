// Shared helpers for the nomadgoods.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

// Root redirects to /sg/. Capture the storefront the site itself opens.
export const BASE = 'https://nomadgoods.com';
export const STORE = '/sg';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Shopify Hydrogen storefront. Class names are hashed, so selectors use
// roles, aria-labels and hrefs, not class hashes.
export const M = (name) => `[aria-label="${name}"], [class*="${name}"]`;

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Cookie banner is Pandectes (.cc-window). Hide it. Never click Accept,
// Decline, Preferences or Manage Cookies: those can POST a consent record.
export async function hideCookies(page) {
  await page.addStyleTag({
    content: '.cc-window, .pd-cookie-banner-window, .pd-cp-cookies-details, #cookieconsent\\:desc { display: none !important; visibility: hidden !important; }',
  }).catch(() => {});
}

// Klaviyo "Sign Up to Save Even More" mounts on load. Close with the X.
// Never type an email and never press Sign Up.
export async function closeSignup(page) {
  const x = page.locator('button.klaviyo-close-form, button[aria-label="Close dialog"]').first();
  if (await x.count()) {
    await x.click({ timeout: 4000, force: true }).catch(() => {});
    await page.waitForTimeout(400);
  }
}

export function isWall(url) {
  const u = String(url || '').toLowerCase();
  // /sg/login and /account/login are public 404s on this host, not a
  // login form. The account wall is the account.nomadgoods.com host.
  if (/nomadgoods\.com\/(sg\/)?(account\/)?login\/?(\?|$)/.test(u)) return false;
  return u.includes('account.nomadgoods.com')
    || u.includes('shopify.com/authentication')
    || u.includes('accounts.shopify');
}

export async function open(page, url, { wait = 2500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  if (isWall(page.url())) {
    throw new Error('wall: ' + page.url());
  }
  await hideCookies(page);
  await closeSignup(page);
  await hideCookies(page);
  return resp;
}
