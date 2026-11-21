// Shared helpers for the Typeform public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules of its own.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.typeform.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

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
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
  await patch(context);
  return { browser, context };
}

// Hide the OneTrust banner. Never click Accept, Reject, or Cookie settings:
// those controls POST a consent choice.
export async function hideConsent(page) {
  await page.addStyleTag({
    content: `#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter, #onetrust-pc-sdk { display: none !important; visibility: hidden !important; pointer-events: none !important; }`,
  }).catch(() => {});
  await page.evaluate(() => {
    document.documentElement.classList.remove('show-cookie-banner');
    document.body && document.body.style.removeProperty('overflow');
    document.documentElement.style.removeProperty('overflow');
  }).catch(() => {});
}

export async function open(page, url, { wait = 3500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(300);
}

// Webflow dropdowns open on hover (aria-expanded flips true). A click toggles
// them shut again, so this only hovers.
export async function hoverMenu(page, ariaLabel) {
  const t = page.locator(`[aria-label="${ariaLabel}"]`).first();
  if (!(await t.count())) return false;
  const box = await t.boundingBox();
  if (!box) return false;
  await page.mouse.move(box.x + Math.min(24, box.width / 2), box.y + 10);
  await page.waitForTimeout(700);
  return (await t.getAttribute('aria-expanded')) === 'true';
}

export async function dismissAnnouncement(page) {
  const b = page.locator('[aria-label="close announcement banner"]').first();
  if (await b.count() && await b.isVisible().catch(() => false)) {
    await b.click().catch(() => {});
    await page.waitForTimeout(400);
    return true;
  }
  return false;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'gap', 'rowGap', 'columnGap',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'backgroundImage',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRadius',
  'boxShadow', 'outline', 'outlineOffset', 'opacity', 'textDecorationLine',
];

export async function styleOf(page, locator) {
  return locator.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = { tag: el.tagName.toLowerCase(), text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80) };
    for (const p of props) out[p] = cs[p];
    out.rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    return out;
  }, PROPS);
}
