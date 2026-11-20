// Shared helpers for the Resend public capture.
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
export const BASE = 'https://resend.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  await context.route('**/*', (route) => {
    const u = route.request().url();
    if (/onetrust|cookiebot|cookielaw|consent\.|privacy-mgmt|trustarc/i.test(u)) return route.abort();
    return route.continue();
  });
  return { browser, context };
}

export async function hideOverlays(page) {
  await page.evaluate(() => {
    const sels = ['#onetrust-banner-sdk', '#onetrust-consent-sdk', '[id*="cookie-banner"]', '[class*="cookie-banner"]'];
    for (const s of sels) document.querySelectorAll(s).forEach((el) => { el.style.setProperty('display', 'none', 'important'); });
  }).catch(() => {});
}

const AUTH = /\/(login|signup|sign-up|register)(\/|$|\?)/i;

export function isAuthUrl(url) {
  try {
    const u = new URL(url);
    if (u.hostname === 'accounts.google.com' || u.hostname === 'github.com' || u.hostname.endsWith('.github.com')) return true;
    if (u.hostname.endsWith('resend.com') && AUTH.test(u.pathname)) return true;
    return false;
  } catch { return false; }
}

export async function open(page, url, { wait = 1800 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
  const landed = page.url();
  if (isAuthUrl(landed)) {
    return { status: resp ? resp.status() : null, authWall: true, url: landed.split('?')[0] };
  }
  return { status: resp ? resp.status() : null, authWall: false, url: landed.split('?')[0] };
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'backgroundImage',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRadius',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'boxShadow', 'opacity', 'textDecorationLine',
];

export async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = cs[p];
    const r = el.getBoundingClientRect();
    o._rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    o._tag = el.tagName.toLowerCase();
    o._text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, PROPS);
}

export function quantizePng(src, dest) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(src)}).convert("RGB")
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert("RGB")
im.save(${JSON.stringify(dest)}, "PNG", optimize=True)
`], { stdio: 'pipe' });
}
