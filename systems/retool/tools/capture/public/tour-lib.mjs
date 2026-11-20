// Shared helpers for the retool.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://retool.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');
export const LAUNCH_OPTS = { headless: true };

export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch(LAUNCH_OPTS);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
  await patch(context);
  return { browser, context };
}

// Hide cookie and newsletter overlays. Never click Accept, Reject, or a form submit.
export async function closePromo(page) {
  await page.evaluate(() => {
    for (const sel of ['[class*="cookie" i]', '[id*="cookie" i]', '[class*="consent" i]', '[id*="onetrust" i]', '#onetrust-banner-sdk']) {
      document.querySelectorAll(sel).forEach((x) => x.style.setProperty('display', 'none', 'important'));
    }
    for (const x of document.querySelectorAll('[role="dialog"], [role="alertdialog"], div, aside')) {
      const t = x.innerText || '';
      const cs = getComputedStyle(x);
      const r = x.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky')
        && /cookie|we value your privacy|newsletter|subscribe/i.test(t)
        && t.length < 1800 && r.width > 180 && r.height > 40) {
        x.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
  return true;
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|access denied|attention required/i.test(s.title)
      || /performing security verification|verify you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 3500 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  const ok = await clearChallenge(page);
  await closePromo(page);
  return ok && res && res.status() < 400;
}

export function quantize(file) {
  execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(${JSON.stringify(file)})
`], { stdio: 'inherit' });
}
