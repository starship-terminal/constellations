// Stocktwits public capture helpers.
// PLAYWRIGHT points at a Playwright install's index.mjs.
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://stocktwits.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CSS modules: `<file>_<name>__<hash>`. Match the stable part.
export const M = (name) => `[class*="${name}__"]`;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({
    headless: true,
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// OneTrust "We Care About Your Privacy". Hide it. Never click I Accept or Reject All.
export async function hideConsent(page) {
  await page.evaluate(() => {
    for (const sel of ['#onetrust-consent-sdk', '#onetrust-banner-sdk', '#onetrust-pc-sdk', '.onetrust-pc-dark-filter']) {
      document.querySelectorAll(sel).forEach((el) => el.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export function isWall(url) {
  try {
    const pathName = new URL(url).pathname;
    return pathName === '/signin' || pathName.startsWith('/signin/')
      || pathName === '/signup' || pathName.startsWith('/signup/')
      || pathName === '/reset-password';
  } catch {
    return false;
  }
}

import fs from 'node:fs';
import { execFileSync } from 'node:child_process';

const PYTHON = process.env.PYTHON || 'python3';

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'textDecorationLine', 'opacity', 'zIndex',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    const text = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 4).join(' '),
      text,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
    };
  }, PROPS);
}

export async function crop(page, locator, name, pad = 6) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box) throw new Error('no box for ' + name);
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 2 || clip.height < 2) throw new Error('clip too small for ' + name);
  await page.screenshot({ path: file, clip });
  execFileSync(PYTHON, ['-c', 'import sys; from PIL import Image; f=sys.argv[1]; im=Image.open(f).convert("RGB"); im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
  return path.relative(REF, file);
}

export async function open(page, url, { wait = 2800 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  const title = await page.title();
  const challenged = /just a moment|security verification|attention required/i.test(title);
  return { status: resp && resp.status(), url: page.url(), title, challenged };
}
