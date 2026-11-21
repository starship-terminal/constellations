// Shared helpers for the ClassPass public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://classpass.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// ClassPass 403s a reused browser after a few navigations. Every page gets a
// fresh browser. Headless Chromium works when the context is not reused.
export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Cookie banner is a consent dialog. Hide it. Never click OK or Cookie Preferences.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const kill = (el) => {
      el.setAttribute('data-cp-hidden-consent', '1');
      el.style.setProperty('display', 'none', 'important');
    };
    for (const el of document.querySelectorAll('[role="dialog"], dialog, [aria-modal="true"], #onetrust-consent-sdk, #onetrust-banner-sdk')) {
      const t = ((el.innerText || '') + (el.id || '') + (el.className || '')).slice(0, 500);
      if (/cookie|onetrust|consent/i.test(t)) kill(el);
    }
    for (const el of document.querySelectorAll('div, section, aside')) {
      if (el.getAttribute('data-cp-hidden-consent')) continue;
      const t = (el.innerText || '').slice(0, 220);
      const r = el.getBoundingClientRect();
      if (/this site uses cookies/i.test(t) && r.height > 40 && r.height < 700) kill(el);
    }
  }).catch(() => {});
}

// Promo strip "Get 14 days free" is a marketing banner, not a consent dialog.
// Leave it unless a caller asks to close it with its own Close control.
export async function closePromo(page) {
  const b = page.getByRole('button', { name: 'Close' }).first();
  if (await b.count() && await b.isVisible().catch(() => false)) {
    const box = await b.boundingBox();
    if (box && box.y < 140) {
      await b.click().catch(() => {});
      await page.waitForTimeout(500);
      return true;
    }
  }
  return false;
}

export async function open(page, url, { wait = 2800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(300);
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
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
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
    const text = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80);
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
  }, PROPS);
}

export async function crop(locator, file) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  await locator.screenshot({ path: file });
}

export function centre(box) {
  return { x: box.x + box.width / 2, y: box.y + box.height / 2 };
}
