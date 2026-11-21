// Shared helpers for the Nothing public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://nothing.tech';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Nothing's classes are Tailwind utilities, not hashed modules. M() is a
// substring match kept so the kit's callers still work.
export const M = (name) => `[class*="${name}"]`;

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-GB' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-GB' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// Hide the Didomi consent wall and the store-region suggestion. Never click
// Agree, Disagree, Learn More, or a region switch. Removing the host is the
// only way the nav becomes clickable; clicking those buttons would record a
// consent choice.
export async function closePromo(page) {
  await page.evaluate(() => {
    document.querySelectorAll('#didomi-host, #didomi-popup, .didomi-popup-backdrop, .didomi-notice-popup, [class*="didomi-popup"]').forEach((n) => n.remove());
    for (const el of [...document.querySelectorAll('div, aside, section, dialog')]) {
      const t = (el.innerText || '').slice(0, 160);
      if (!/LOOKS LIKE YOU/i.test(t)) continue;
      const r = el.getBoundingClientRect();
      if (r.height > 30 && r.height < 640) el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
  return true;
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await closePromo(page);
  await page.waitForTimeout(300);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'opacity', 'outlineWidth', 'outlineColor', 'outlineOffset',
  'textDecorationLine',
];

export function patch(page) {
  return page;
}
