// Shared helpers for the doctronic.ai public captures.
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
export const BASE = 'https://www.doctronic.ai';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Doctronic uses hashed CSS-module classes. Prefer data-test-id. M() is a
// passthrough so older kit call sites keep compiling.
export const M = (name) => `[data-test-id="${name}"]`;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  return { browser, context };
}

// Hide a consent or cookie overlay. Never click Accept, Reject, or a consent POST.
export async function hideConsent(page) {
  return page.evaluate(() => {
    let n = 0;
    for (const el of document.querySelectorAll('div, section, aside, [role="dialog"]')) {
      const t = (el.innerText || '').slice(0, 600);
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky') && r.height > 40 && r.width > 180
          && /cookie|consent|we value your privacy|accept all/i.test(t)
          && !/log in|sign up|email address/i.test(t)) {
        el.style.setProperty('display', 'none', 'important');
        el.setAttribute('data-capture-hidden', 'consent');
        n++;
      }
    }
    return n;
  });
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
}
