// Shared helpers for the Leonardo.Ai public capture. PRODUCT (adapt).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://leonardo.ai';

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const PKG = path.resolve(HERE, '..', '..', '..');

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'alignItems', 'justifyContent',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'opacity', 'cursor',
];

export async function launch() {
  const browser = await chromium.launch({ headless: true });
  return { browser };
}

export async function contextFor(browser, { mobile = false } = {}) {
  return browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
}

// Cookie overlays are hidden, never answered. A consent click can POST.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const sel = '.cookiefirst-root, [class*="cookiefirst"], [id*="cookiefirst"], [id*="cookie" i], [class*="cookie-banner" i], [class*="consent" i]';
    document.querySelectorAll(sel).forEach((el) => {
      const t = (el.innerText || '').slice(0, 400);
      if (/cookie|consent|privacy/i.test(t) || /cookiefirst/i.test(el.className + ' ' + el.id)) {
        el.style.setProperty('display', 'none', 'important');
      }
    });
  }).catch(() => {});
}

export async function open(page, url, wait = 3500) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(400);
  return res?.status() ?? 0;
}

const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
  : v);

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string'
      ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
      : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = noUrl(cs[p]);
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
    };
  }, PROPS);
}

export { noUrl };
