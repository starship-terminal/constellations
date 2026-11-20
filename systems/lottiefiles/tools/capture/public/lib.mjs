// Shared helpers for the lottiefiles.com public captures.
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
export const BASE = 'https://lottiefiles.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const LAUNCH_OPTS = { headless: true };

// Tailwind utility classes. Selectors in measure.mjs use roles and text, not hashed modules.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ mobile = false } = {}) {
  const browser = await chromium.launch(LAUNCH_OPTS);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Hide the cookie banner. Never click Got It (that would accept cookies).
export async function hideConsent(page) {
  await page.addStyleTag({
    content: [
      '[class*="cookie" i], [id*="cookie" i], [class*="consent" i]',
      '{ visibility: hidden !important; }',
    ].join(''),
  }).catch(() => {});
  await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('div, section, aside')];
    for (const el of nodes) {
      const t = (el.innerText || '');
      if (t.length > 40 && t.length < 400 && /we use cookies/i.test(t) && /got it/i.test(t)) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  return res && res.status();
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'outline', 'textDecorationLine', 'opacity',
];
