// Shared helpers for the LottieFiles public capture.
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
export const BASE = 'https://lottiefiles.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  // Automation is not hidden: no navigator.webdriver mask (bot check: recorded as a boundary, not bypassed).
  return { browser, context };
}

// Hide the cookie banner. Never click Got It / Accept: that posts consent.
export async function hideConsent(page) {
  await page.addStyleTag({
    content: `
      .simple-cookie-banner, .simple-cookie-banner__accept-btn,
      [class*="cookie-banner"], [id*="cookie-banner"],
      #onetrust-consent-sdk, .cky-consent-container, #CybotCookiebotDialog,
      iframe[src*="accounts.google.com"], iframe[src*="gsi"],
      #credential_picker_container, [id*="credential_picker"] {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
      }
    `,
  }).catch(() => {});
}

export async function open(page, url, { wait = 2800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(400);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'backgroundColor', 'color', 'borderTopColor', 'borderRightColor', 'borderBottomColor', 'borderLeftColor',
  'borderTopWidth', 'borderRightWidth', 'borderBottomWidth', 'borderLeftWidth',
  'borderTopStyle', 'borderRadius', 'boxShadow', 'outline', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing', 'textAlign',
  'textDecoration', 'opacity', 'transform', 'filter',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
];

export async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const c = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    };
    for (const p of props) o[p] = c[p];
    return o;
  }, PROPS);
}

// Element screenshot into components/crops/<name>.png, padded, then stored as 256 colours like every
// other committed image. The element is scrolled into view first and measured once after, so one
// below the fold is cropped where it now sits.
export async function crop(page, loc, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box');
  const vp = page.viewportSize();
  const x = Math.max(0, box.x - pad);
  const y = Math.max(0, box.y - pad);
  const w = Math.min(vp.width - x, box.width + pad * 2);
  const h = Math.min(vp.height - y, box.height + pad * 2);
  if (w < 2 || h < 2) throw new Error('crop clipped off viewport');
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({ path: file, clip: { x, y, width: w, height: h } });
  quantize(file);
  return `components/crops/${name}.png`;
}

export function quantize(file) {
  execFileSync(PYTHON, ['-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file]);
}

export async function centre(loc) {
  await loc.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await loc.page().waitForTimeout(250);
}

export function quantizeNote() {
  return PYTHON;
}
