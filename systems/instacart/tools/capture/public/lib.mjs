// Shared helpers for the Instacart public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.instacart.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Instacart's consumer CSS is emotion: classes are `e-<hash>`. Nothing in the
// class name is stable, so selectors are roles, aria labels and visible text.
export const M = (name) => `[class*="${name}"]`;

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  // Automation is not hidden: no AutomationControlled flag, no webdriver mask.
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  return { browser, context };
}

// Consent, location and promo overlays are hidden. Never click a consent
// control: some of them POST. A "Find stores near you" dialog is a location
// prompt, not a consent POST, but it is still dismissed by hiding so a shot
// is not a dialog over the page.
export async function hideOverlays(page) {
  await page.evaluate(() => {
    const hide = (el) => { if (el) el.style.setProperty('display', 'none', 'important'); };
    for (const el of document.querySelectorAll(
      '#onetrust-banner-sdk, #onetrust-consent-sdk, .onetrust-pc-dark-filter, [id*="consent"], [class*="cookie-banner"], [class*="CookieBanner"]'
    )) hide(el);
    for (const el of document.querySelectorAll('[role="dialog"]')) {
      const t = (el.innerText || '').slice(0, 400);
      if (/cookie|consent|privacy information|your privacy|find stores near you|choose address|get \$0 delivery fee/i.test(t)) hide(el);
    }
    for (const el of document.querySelectorAll('[class*="overlay"], [class*="backdrop"]')) {
      const t = (el.innerText || '').slice(0, 200);
      if (/cookie|consent|privacy/i.test(t)) hide(el);
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 3500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
  await page.waitForTimeout(300);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
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
    const text = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80);
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 3).join(' '),
      text,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
  }, PROPS);
}
