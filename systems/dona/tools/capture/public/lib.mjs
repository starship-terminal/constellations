// Shared helpers for the Dona public capture.
// PLAYWRIGHT points at a Playwright install's index.mjs.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://dona.ai';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  return { browser, context };
}

// Hide the cookie bar. Never click Accept: that writes localStorage consent.
export async function hideConsent(page) {
  await page.evaluate(() => {
    for (const n of document.querySelectorAll('[class*="Cookie"]')) {
      n.style.setProperty('display', 'none', 'important');
    }
  });
}

export async function waitReady(page) {
  await page.waitForFunction(() => {
    const pre = document.querySelector('.preload');
    if (!pre) return true;
    return getComputedStyle(pre).display === 'none' || pre.getBoundingClientRect().width < 2;
  }, { timeout: 12000 }).catch(() => {});
  await page.waitForTimeout(400);
}

export async function open(page, url, { wait = 400 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await waitReady(page);
  await page.waitForTimeout(wait);
  await hideConsent(page);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'boxShadow', 'outline', 'outlineOffset', 'opacity', 'textDecoration',
];

export async function styleOf(page, locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  return handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = { box: { x: r.x, y: r.y, w: r.width, h: r.height } };
    for (const p of props) out[p] = s[p];
    return out;
  }, PROPS);
}
