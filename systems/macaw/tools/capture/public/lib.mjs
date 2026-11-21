// Shared helpers for the macawhq.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://macawhq.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// macawhq.com is a Webflow marketing site. Classes are authored names
// (navbar_link, button, pricing-toggle-button, form-input), not hashed.
export const M = (name) => `.${name}`;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: width === 1440 ? 1 : 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// No cookie banner was present on 2026-11-21. This only hides a fixed
// consent or newsletter overlay if one mounts. It never clicks Accept,
// Reject, or a submit control.
export async function closePromo(page) {
  await page.evaluate(() => {
    for (const sel of ['#onetrust-banner-sdk', '#onetrust-consent-sdk', '.onetrust-pc-dark-filter']) {
      document.querySelectorAll(sel).forEach((n) => n.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await clearChallenge(page);
  await page.waitForTimeout(wait);
  await closePromo(page);
}

export function isAuthHost(url) {
  try { return new URL(url).hostname === 'app.macawhq.com'; } catch { return false; }
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'rowGap', 'columnGap',
  'borderTopWidth', 'borderRightWidth', 'borderBottomWidth', 'borderLeftWidth',
  'borderTopStyle', 'borderTopColor', 'borderRadius',
  'backgroundColor', 'color',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'boxShadow', 'opacity', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
];

export async function styleOf(page, locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  const box = await handle.boundingBox();
  const style = await page.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const out = {};
    for (const p of props) out[p] = cs[p];
    out.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return out;
  }, handle, PROPS);
  await handle.dispose();
  return { box, style };
}
