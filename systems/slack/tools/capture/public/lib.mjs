// Shared helpers for the slack.com public captures.
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
// The bare root redirects to a locale. Capture the locale the live site chose.
export const BASE = 'https://slack.com/intl/en-sg';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const LAUNCH_OPTS = { headless: true };

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
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Hide the cookie banner. Never click Accept or Reject: those POST consent.
export async function hideConsent(page) {
  await page.evaluate(() => {
    for (const sel of ['#onetrust-banner-sdk', '#onetrust-consent-sdk', '.ot-sdk-container', '#ot-sdk-btn-floating', '.onetrust-pc-dark-filter']) {
      document.querySelectorAll(sel).forEach((el) => el.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  const status = resp ? resp.status() : 0;
  const title = await page.title();
  if (status >= 400 || /not supported|access denied|just a moment/i.test(title)) return false;
  return true;
}

export function styleOf(elStyle) {
  const pick = ['color', 'backgroundColor', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
    'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
    'height', 'width', 'boxShadow', 'outline', 'outlineOffset', 'textDecoration', 'opacity', 'display'];
  const out = {};
  for (const k of pick) out[k] = elStyle[k];
  return out;
}

export async function crop(page, locator, name, pad = 6) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 2 || clip.height < 2) return null;
  await page.screenshot({ path: file, clip });
  try {
    execFileSync(PYTHON, ['-c', 'from PIL import Image; import sys; im=Image.open(sys.argv[1]).convert("RGB"); im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(sys.argv[1])', file]);
  } catch { /* keep the full-colour crop if Pillow is missing */ }
  return path.relative(REF, file);
}
