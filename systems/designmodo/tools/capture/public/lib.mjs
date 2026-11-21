// Shared helpers for the designmodo.com public signed-out captures.
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
export const BASE = 'https://designmodo.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// designmodo.com is a WordPress theme (designmodo) with descriptive classes
// (.menu-link, .button, .dropdown). M() is a class selector.
export const M = (name) => `.${name}`;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Cookie settings panel is first-party. Hide it. Never click Accept, Reject,
// Save choices, or Only necessary (those would record a consent choice).
export async function hideConsent(page) {
  await page.addInitScript(() => {
    const kill = () => {
      // Match the widget only. body.dm-cookie-consent-open contains the same
      // substring, and hiding body paints a blank page.
      for (const sel of [
        '.dm-cookie-consent__banner', '.dm-cookie-consent__settings',
        '.dm-cookie-consent__panel', '#cookie-law-info-bar',
      ]) {
        document.querySelectorAll(sel).forEach((n) => {
          if (n === document.body || n === document.documentElement) return;
          n.style.setProperty('display', 'none', 'important');
        });
      }
      document.body && document.body.classList.remove('dm-cookie-consent-open');
    };
    let n = 0;
    const t = setInterval(() => { kill(); if (++n > 20) clearInterval(t); }, 400);
    document.addEventListener('DOMContentLoaded', kill);
  }).catch(() => {});
  await page.evaluate(() => {
    document.querySelectorAll('.dm-cookie-consent__banner, .dm-cookie-consent__settings, .dm-cookie-consent__panel').forEach((n) => {
      if (n === document.body || n === document.documentElement) return;
      n.style.setProperty('display', 'none', 'important');
    });
    document.body && document.body.classList.remove('dm-cookie-consent-open');
  }).catch(() => {});
}

export async function closePromo(page) {
  await hideConsent(page);
  return true;
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  // The marketing theme paints after load. A shot taken on the first frame
  // is a white viewport even though the DOM already has text.
  await page.waitForFunction(() => {
    const h = document.documentElement.scrollHeight;
    const text = (document.body && document.body.innerText) || '';
    return h > 400 && text.trim().length > 80;
  }, { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(600);
}

export { PYTHON };
