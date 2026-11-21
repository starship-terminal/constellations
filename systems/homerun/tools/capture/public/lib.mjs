// Shared helpers for the Homerun public captures (Webflow marketing site).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// PRODUCT (adapt): homerun.co. Public marketing only. Never submit a form,
// never type into login, signup, newsletter, contact, partner or booking fields,
// never click Google, Apple or Microsoft.
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
export const BASE = 'https://www.homerun.co';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const deviceScaleFactor = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

export async function hideOverlays(page) {
  await page.evaluate(() => {
    for (const sel of ['#intercom-container', '.intercom-lightweight-app', '.intercom-namespace', '[class*="intercom"]', '#onetrust-banner-sdk', '.cky-consent-container']) {
      document.querySelectorAll(sel).forEach((el) => { el.style.setProperty('display', 'none', 'important'); });
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideOverlays(page);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'boxShadow', 'outline', 'textDecorationLine',
];

export function styleOf(el) {
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const o = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
  for (const p of ['display', 'position', 'boxSizing', 'width', 'height', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform', 'color', 'backgroundColor', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle', 'boxShadow', 'outline', 'textDecorationLine', 'gap']) {
    o[p] = s[p];
  }
  return o;
}

export async function crop(page, locator, file) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return false;
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box2 = await locator.boundingBox();
  if (!box2) return false;
  await page.screenshot({ path: file, clip: { x: Math.max(0, box2.x), y: Math.max(0, box2.y), width: Math.min(box2.width, 1400), height: Math.min(box2.height, 900) } });
  return true;
}

export function quantize(file) {
  const script = `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGBA')
q = im.convert('P', palette=Image.ADAPTIVE, colors=256).convert('RGBA')
# keep alpha from original
q.putalpha(im.getchannel('A'))
q.save(${JSON.stringify(file)}, 'PNG')
`;
  execFileSync(PYTHON, ['-c', script]);
}
