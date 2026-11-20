// Shared helpers for the Marathon public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
// PRODUCT (adapt): onmarathon.com, November 2026. The product is an archive.
// Sign-in, register and checkout redirect to / and were never submitted.
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { safeUrl } from '../safe-url.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://onmarathon.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const PKG = path.resolve(HERE, '..', '..', '..');
export const RAW = path.join(PKG, 'raw');
export const CROPS = path.join(PKG, 'components', 'crops');

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex',
];

export async function launch({ mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Hide a consent overlay if one appears. Never click it (FIELD-NOTES: a consent
// button can POST). The 2026-11-18 public pages showed none.
export async function hideConsent(page) {
  return page.evaluate(() => {
    const hits = [];
    for (const el of document.querySelectorAll('div, section, aside, dialog, iframe, [role="dialog"]')) {
      const id = (el.id || '') + ' ' + (typeof el.className === 'string' ? el.className : '');
      const t = (el.innerText || '').slice(0, 180);
      if (!/cookie|consent|gdpr|onetrust|cookiebot|osano|didomi/i.test(id + ' ' + t)) continue;
      const r = el.getBoundingClientRect();
      if (r.width < 200 || r.height < 40 || r.height > 700) continue;
      el.style.setProperty('display', 'none', 'important');
      hits.push((el.id || el.tagName) + ' ' + t.replace(/\s+/g, ' ').slice(0, 60));
    }
    return hits;
  });
}

export async function open(page, url, { wait = 2500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  const hidden = await hideConsent(page);
  return { status: resp ? resp.status() : 0, final: safeUrl(page.url()), hidden };
}

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = noUrl(cs[p]);
    const vars = {};
    for (const name of ['--background', '--foreground', '--primary', '--primary-foreground', '--primary-hover', '--primary-text', '--muted', '--muted-foreground', '--card', '--border', '--ring', '--destructive', '--radius', '--secondary', '--secondary-foreground']) {
      const v = cs.getPropertyValue(name).trim();
      if (v) vars[name] = v;
    }
    return {
      tag: el.tagName.toLowerCase(),
      classes: String(el.className || '').slice(0, 160),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
      vars,
    };
  }, PROPS);
}
