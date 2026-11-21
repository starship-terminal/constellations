// Shared helpers for the MasterClass public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.masterclass.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

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

export async function hidePromo(page) {
  const close = page.getByRole('button', { name: 'Close banner' });
  if (await close.count()) {
    await close.first().click({ timeout: 2000 }).catch(() => {});
    await page.waitForTimeout(400);
  }
}

export async function open(page, url, { wait = 2800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  await page.waitForTimeout(wait);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'outlineWidth', 'outlineColor', 'outlineStyle', 'outlineOffset',
  'opacity', 'textDecorationLine',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const c = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = c[k];
    const r = el.getBoundingClientRect();
    o._rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    const vars = {};
    for (const name of ['--mc-color-primary-default', '--mc-color-bg-page-default', '--mc-color-text-light', '--mc-color-brand', '--mc-color-focus']) {
      const v = c.getPropertyValue(name);
      if (v) vars[name] = v.trim();
    }
    o._vars = vars;
    return o;
  }, PROPS);
}
