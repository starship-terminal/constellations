// Shared helpers for the Weights & Biases public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

export const SITE = 'https://wandb.ai/site';
export const APP = 'https://wandb.ai/';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');

// Origin and path only. Query strings can carry next= redirects into a login wall.
export function originPath(u) {
  try {
    const x = new URL(u);
    return x.origin + x.pathname;
  } catch {
    return null;
  }
}

export function isAuthWall(url, body) {
  const u = String(url || '');
  const b = String(body || '').slice(0, 800);
  if (/id\.coreweave\.com|accounts\.google\.com|github\.com\/login|login\.microsoftonline/i.test(u)) return true;
  if (/\/login|\/signup|\/sign-up|\/sign-in/i.test(u)) return true;
  if (/sign in to|log in to continue|create your account|continue with google|continue with github/i.test(b) && /password|email/i.test(b)) return true;
  return false;
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  return { browser, context };
}

export async function hideOverlays(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('div, section, aside, [role="dialog"]')) {
      const t = (el.innerText || '').slice(0, 400);
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky')
        && r.width > 200 && r.height > 80
        && /cookie|we value your privacy|consent|accept all/i.test(t)) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}
