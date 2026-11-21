// Shared helpers for the ROVR public capture.
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
export const BASE = 'https://www.rovr.live';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

// ROVR paints no cookie banner. Do not click consent, and do not fill auth fields.
export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'backgroundImage',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'opacity', 'textDecoration', 'outline', 'outlineOffset',
  'cursor', 'transition',
];

export async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = {};
    for (const p of props) o[p] = cs[p];
    o.rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    o.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, PROPS);
}

export async function crop(page, loc, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box');
  const vp = page.viewportSize();
  const x = Math.max(0, box.x - pad);
  const y = Math.max(0, box.y - pad);
  const w = Math.min(vp.width - x, box.width + pad * 2);
  const h = Math.min(vp.height - y, box.height + pad * 2);
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({ path: file, clip: { x, y, width: w, height: h } });
  return `components/crops/${name}.png`;
}

export function centre(box) {
  return { x: box.x + box.width / 2, y: box.y + box.height / 2 };
}
