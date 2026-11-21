// Shared helpers for the ripple.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';
export { PYTHON };

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://ripple.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  await context.route('**/*wistia*', (route) => route.abort());
  await context.route('**/*.mp4', (route) => route.abort());
  await context.route('**/*doubleclick*', (route) => route.abort());
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Hide the cookie banner. Never click Accept, Deny, or Save Preferences:
// those controls POST a consent choice. Hiding leaves essential-only as the
// unset state and does not submit a form.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const hide = (el) => { if (el) el.style.setProperty('display', 'none', 'important'); };
    for (const el of document.querySelectorAll('[role="dialog"], div, section, aside')) {
      const t = el.innerText || '';
      if (t.includes('Deny Non-Essential Cookies') || t.includes('Accept All Cookies') || /cookie consent/i.test(el.getAttribute('aria-label') || '')) {
        hide(el);
      }
    }
    document.documentElement.style.removeProperty('overflow');
    document.body && document.body.style.removeProperty('overflow');
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(300);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'alignItems', 'justifyContent',
  'backgroundColor', 'color', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'textTransform', 'opacity', 'outline', 'outlineOffset',
];
