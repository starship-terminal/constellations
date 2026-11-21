// Shared helpers for the Starbucks public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.starbucks.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'opacity',
];

// TrustArc cookie banner. Abort the vendor and hide the overlay. Never click
// Agree or Change cookie settings: those post a consent record.
export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  await context.route(/truste\.com|onetrust\.com|cookielaw\.org|consent\.trustarc|privacy-mgmt\.com|accdab\.net/, (r) => r.abort());
}

export async function hideCookies(page) {
  await page.evaluate(() => {
    const hide = (n) => n.style.setProperty('display', 'none', 'important');
    document.querySelectorAll('#truste-consent-track, #truste-consent-content, .truste_overlay, .truste_box_overlay, #consent_blackbar, [id*="truste"]').forEach(hide);
    for (const el of document.querySelectorAll('div, section, aside')) {
      const t = (el.innerText || '').slice(0, 120);
      const r = el.getBoundingClientRect();
      if (/this site uses cookies/i.test(t) && r.height > 40 && r.height < 700 && r.width > 200) hide(el);
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideCookies(page);
  await page.evaluate(() => scrollTo(0, 0)).catch(() => {});
  await page.waitForTimeout(300);
}
