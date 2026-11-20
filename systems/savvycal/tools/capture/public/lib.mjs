// Shared helpers for the SavvyCal public captures.
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
export const BASE = 'https://savvycal.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// savvycal.com paints one light marketing theme (body.bg-brand-oatmeal).
// Tailwind utilities carry the brand colours. The only custom property on
// marketing pages is --nav-height. Selectors key off roles and visible text.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function closePromo() {
  return false;
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
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
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const cls = [...el.classList].slice(0, 6);
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: cls.join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    const paint = [];
    const nodes = [el, ...el.querySelectorAll('*')].slice(0, 80);
    for (const n of nodes) {
      if (paint.length >= 8) break;
      const c = getComputedStyle(n);
      const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
      const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
      if (!bg && !sh) continue;
      const rr = n.getBoundingClientRect();
      paint.push({
        node: n.tagName.toLowerCase() + [...n.classList].slice(0, 2).map((x) => '.' + x).join(''),
        size: `${rr.width.toFixed(1)}x${rr.height.toFixed(1)}`,
        bg: bg || undefined,
        shadow: sh || undefined,
        radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        color: c.color,
      });
    }
    if (paint.length) out.paint = paint;
    return out;
  }, PROPS);
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box');
  const file = path.join(CROPS, `${name}.png`);
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box2 = await locator.boundingBox();
  if (!box2) throw new Error('no box after scroll');
  await locator.screenshot({ path: file });
  return `components/crops/${name}.png`;
}

export function centre(box) {
  return { x: box.x + box.width / 2, y: box.y + box.height / 2 };
}

export function quantizeNote() {
  return PYTHON;
}
