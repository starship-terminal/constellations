// Shared helpers for the RevenueCat public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.revenuecat.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false, scheme = 'light' } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: scheme }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: scheme });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Hide the iubenda banner. Never click Accept, Reject or Customize.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const css = `#iubenda-cs-banner, .iubenda-cs-container, .iubenda-cs-default, [id^="iubenda-cs"], #iubenda-iframe { display: none !important; visibility: hidden !important; }`;
    let tag = document.getElementById('rc-hide-consent');
    if (!tag) {
      tag = document.createElement('style');
      tag.id = 'rc-hide-consent';
      document.documentElement.appendChild(tag);
    }
    tag.textContent = css;
  }).catch(() => {});
}

export async function open(page, url, { wait = 2200 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(200);
  return resp;
}

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
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style: pick(cs),
    };
  }, PROPS);
}

export { fs, path, PYTHON };
