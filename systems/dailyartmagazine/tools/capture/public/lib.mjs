// Shared helpers for the DailyArt Magazine public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// The magazine is a public WordPress site (theme idvetmp-child). Nothing is
// signed into, no newsletter or contact field is filled, and Shop / Courses
// (external stores) are recorded as links and never opened.
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.dailyartmagazine.com';

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
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Hide ad and promo overlays. Never click a consent or subscribe control.
export async function closePromo(page) {
  await page.evaluate(() => {
    const hide = (el) => { el.style.setProperty('display', 'none', 'important'); };
    for (const el of document.querySelectorAll(
      '.fs-close-button, [class*="freestar"], [id*="freestar"], iframe[title*="ad" i], .announcer, [class*="announcer"]'
    )) hide(el);
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await closePromo(page);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'backgroundColor', 'color', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'textTransform', 'textDecorationLine', 'opacity', 'outline',
];

export function styleOf(el, props = PROPS) {
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const out = { rect: { x: r.x, y: r.y, w: r.width, h: r.height } };
  for (const p of props) out[p] = cs[p];
  return out;
}
