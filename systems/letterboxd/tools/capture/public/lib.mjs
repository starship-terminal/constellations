// Shared helpers for the Letterboxd public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
const ADAPTED_FOR = 'letterboxd';

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { quantizeCrop } from '../crop.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://letterboxd.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

export const FILM = BASE + '/film/the-hunger-games-sunrise-on-the-reaping/';
export const LIST = BASE + '/official/list/letterboxds-top-500-films/';

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await context.route('**/*', (route) => {
    const u = route.request().url();
    if (/doubleclick|googlesyndication|google-analytics|adservice|adnxs|taboola|outbrain|scorecardresearch|facebook\.net|hotjar|clarity\.ms/i.test(u)) {
      return route.abort();
    }
    return route.continue();
  });
  return { browser, context };
}

// Letterboxd's public pages do not open a consent dialog on first paint.
// A hidden consent list item exists in the footer. Never click it.
export async function closePromo() {
  return false;
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
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

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const noEmail = (v) => (typeof v === 'string' ? v.replace(/[\w.+%-]+@[\w-]+(?:\.[\w-]+)+/g, '<email>') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const text = noEmail((el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80));
    return {
      tag: el.tagName.toLowerCase(),
      className: (el.className || '').toString().slice(0, 120),
      text,
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      style: pick(cs),
    };
  }, PROPS);
}

export async function crop(locator, file) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 4;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 900),
    height: Math.min(box.height + pad * 2, 500),
  };
  const raw = file.replace(/\.png$/, '.raw.png');
  await locator.page().screenshot({ path: raw, clip });
  await quantizeCrop(raw, file, PYTHON);
  try { fs.unlinkSync(raw); } catch {}
  return file;
}

export async function centre(locator) {
  const box = await locator.boundingBox();
  if (!box) return;
  await locator.page().mouse.move(box.x + box.width / 2, box.y + Math.min(box.height / 2, 20));
}
