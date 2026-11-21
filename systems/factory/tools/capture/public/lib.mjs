// Shared helpers for the factory.com public captures. Run with PLAYWRIGHT
// pointing at a Playwright install (index.mjs) when this directory has no
// node_modules.
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://factory.com';
export const APP = 'https://app.factory.ai';
export const DOCS = 'https://docs.factory.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// factory.com is a Next.js marketing site. factory.ai redirects here.
// The public routes paint light (html[data-theme="light"]). A dark set is
// declared as the theme-layer default and inverted on [data-theme="light"].
// docs.factory.com has an explicit light/dark/system switch.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
  await context.route(/iubenda|cookielaw|onetrust|cookiebot|privacy-mgmt/i, (r) => r.abort());
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide a consent overlay. Never click Accept or Reject.
export async function closePromo(page) {
  await page.evaluate(() => {
    for (const x of document.querySelectorAll('div,section,aside,[role="dialog"]')) {
      const t = (x.innerText || '').slice(0, 500);
      const r = x.getBoundingClientRect();
      if (/cookie|consent/i.test(t) && /accept|reject|agree/i.test(t) && r.height > 40 && r.height < 700) {
        x.style.setProperty('display', 'none', 'important');
        x.setAttribute('data-hidden-consent', '1');
      }
    }
  }).catch(() => {});
}

export { PYTHON };
