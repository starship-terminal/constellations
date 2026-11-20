// Shared helpers for the onmarathon.com public captures (adapted from the kit's
// Gauth copy, which came from Coursera). Run with PLAYWRIGHT pointing at a
// Playwright install (index.mjs) when this directory has no node_modules.
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
export const BASE = 'https://onmarathon.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/onmarathon, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Tailwind utility classes. Selectors key off roles, landmarks and text.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
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

// Hide (never click) any fixed cookie or newsletter overlay. The archive
// banner is page content and stays. REMOVE-ONLY: hiding never accepts or rejects.
export async function closePromo(page) {
  for (let i = 0; i < 3; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /cookie|we value privacy|newsletter|subscribe to/i.test(t)
          && t.length < 1600 && r.width > 200 && r.height > 60 && +cs.zIndex > 5;
      });
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      return n;
    }).catch(() => 0);
    if (!hit) return false;
    await page.waitForTimeout(400);
  }
  return true;
}

export async function open(page, url, { wait = 2500, promo = 'close' } = {}) {
  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  await clearChallenge(page);
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
];

export async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = cs[k];
    const r = el.getBoundingClientRect();
    o._box = { x: r.x, y: r.y, width: r.width, height: r.height };
    o._text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, PROPS);
}

export async function crop(page, loc, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await loc.evaluate((el) => {
    const r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  });
  if (!box || box.width < 2 || box.height < 2) throw new Error('empty box ' + name);
  const dpr = page.viewportSize() ? (await page.evaluate(() => window.__captureDPR || window.devicePixelRatio)) : 1;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: box.width + pad * 2,
    height: box.height + pad * 2,
  };
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  try {
    execFileSync(PYTHON, ['-c',
      'from PIL import Image; p=Image.open(%r); p.convert("RGB").quantize(256).save(%r)' % (file, file)],
      { stdio: 'ignore' });
  } catch { /* keep the raw crop if Pillow is missing */ }
  return { file: 'components/crops/' + name + '.png', box, dpr };
}
