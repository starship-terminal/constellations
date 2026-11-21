// Shared helpers for the Unsplash public capture.
// Headless Chromium is stopped by unsplash.com's Anubis check
// (/.within.website, HTTP 401). Headed Chromium clears it. Launch headed.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const PYTHON = process.env.PYTHON || 'python3';
export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://unsplash.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (sel) => sel;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

export async function waitPastChallenge(page, ms = 90000) {
  const start = Date.now();
  while (Date.now() - start < ms) {
    const url = page.url();
    const title = await page.title().catch(() => '');
    if (url.includes('unsplash.com') && !url.includes('.within.website') && !/Checking your browser/i.test(title)) {
      await page.waitForTimeout(1200);
      return true;
    }
    await page.waitForTimeout(1500);
  }
  return false;
}

// Hide OneTrust. Never click Allow all / Reject (FIELD-NOTES: consent can POST).
export async function hideConsent(page) {
  await page.addStyleTag({
    content: `
      #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
      [id*="onetrust"], [class*="ot-sdk"], iframe[title*="preference" i] {
        display: none !important; visibility: hidden !important; pointer-events: none !important;
      }
    `,
  }).catch(() => {});
}

export async function open(page, url, { wait = 1500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  const ok = await waitPastChallenge(page);
  if (!ok) throw new Error('Anubis challenge did not clear: ' + page.url());
  await hideConsent(page);
  await page.waitForTimeout(wait);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'textDecorationLine', 'opacity', 'cursor',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))[^)]*\)/g, 'url(…)') : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = noUrl(cs[p]);
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
    };
  }, PROPS);
}
