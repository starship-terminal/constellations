// Shared helpers for the Parallel public capture (useparallel.com).
// Adapted from tools/kit/capture/public/lib.mjs. Nothing is submitted.
// A login, signup, LinkedIn, Google or Apple wall stops that branch.
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
export const BASE = 'https://www.useparallel.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

// Hide a cookie or newsletter overlay. Never click Accept, Reject, or Subscribe.
export async function closePromo(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('div,section,aside,[role="dialog"]')) {
      const t = el.innerText || '';
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky')
        && /cookie|we value privacy|accept cookies|newsletter/i.test(t)
        && t.length < 800 && r.height > 40 && r.height < 400) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2200 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await closePromo(page);
  return res;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'textDecorationLine',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'opacity', 'cursor',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { rect: { x: r.x, y: r.y, width: r.width, height: r.height } };
    for (const k of props) o[k] = cs[k];
    return o;
  }, PROPS);
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box');
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  const file = path.join(CROPS, `${name}.png`);
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  const box2 = await locator.boundingBox();
  if (!box2) throw new Error('no box after scroll');
  const clip2 = {
    x: Math.max(0, box2.x - pad),
    y: Math.max(0, box2.y - pad),
    width: Math.min(vp.width - Math.max(0, box2.x - pad), box2.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box2.y - pad), box2.height + pad * 2),
  };
  if (clip2.width < 2 || clip2.height < 2) throw new Error('clip empty');
  await page.screenshot({ path: file, clip: clip2 });
  // Quantize the crop in place so the committed PNG is 256-colour sRGB.
  execFileSync(PYTHON, [path.join(HERE, '..', 'quantize.py'), file, file], { stdio: 'ignore' });
  return `components/crops/${name}.png`;
}
