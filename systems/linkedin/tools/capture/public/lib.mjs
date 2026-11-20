// Shared helpers for the LinkedIn public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.linkedin.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const WALL = /\/login\/?$|\/signup|\/authwall|\/checkpoint\/|\/uas\/login|join linkedin|sign in with apple|agree & join/i;

export async function launch(opts = {}) {
  const browser = await chromium.launch({ headless: true });
  return { browser, ...(await contextFor(browser, opts)) };
}

export async function contextFor(browser, { mobile = false, width = 1440, height = 900 } = {}) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: 'light' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: 'light' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { context };
}

export function isWall(url, text = '') {
  return WALL.test(url) || WALL.test(text.slice(0, 400));
}

export async function open(page, url, { wait = 2500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  const finalUrl = page.url();
  const head = await page.evaluate(() => (document.body?.innerText || '').slice(0, 400)).catch(() => '');
  return { status: resp && resp.status(), url: finalUrl, wall: isWall(finalUrl, head), title: await page.title().catch(() => '') };
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textAlign',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'opacity', 'outlineStyle', 'outlineWidth', 'outlineColor', 'outlineOffset',
];

export function styleOf(cs) {
  const out = {};
  for (const k of PROPS) out[k] = cs[k];
  return out;
}
