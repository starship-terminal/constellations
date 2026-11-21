// Shared helpers for the Overflow public captures. Adapted from the kit's
// Gauth copy. Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
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
export const BASE = 'https://overflow.io';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Overflow's public site is a Bootstrap marketing site. Classes are stable
// (btn, navbar-toggler, accordion__opener). M() is a pass-through so the kit
// callers still compile.
export const M = (name) => name;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// The cookie bar asks to accept cookies. Hide it. Never click Required only
// or Allow all: those buttons POST a consent choice.
export async function hideCookies(page) {
  await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('#cookies-alert, .cookies-alert, div, section, aside')];
    for (const n of nodes) {
      const t = (n.innerText || '').slice(0, 400);
      const id = n.id || '';
      if (id === 'cookies-alert' || (/we use cookies/i.test(t) && /required only/i.test(t) && n.getBoundingClientRect().height < 500 && n.getBoundingClientRect().height > 0)) {
        n.style.setProperty('display', 'none', 'important');
        n.setAttribute('data-capture-hidden', 'cookies');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideCookies(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cls = (n) => [...n.classList].slice(0, 4);
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: cls(el).join(' '),
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
      if (rr.width < 2 || rr.height < 2) continue;
      paint.push({
        node: n.tagName.toLowerCase() + cls(n).slice(0, 2).map((x) => '.' + x).join(''),
        size: `${rr.width.toFixed(1)}x${rr.height.toFixed(1)}`,
        bg: bg || undefined,
        shadow: sh || undefined,
        radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        color: c.color,
        fontSize: c.fontSize,
        fontWeight: c.fontWeight,
      });
    }
    if (paint.length) out.paint = paint;
    return out;
  }, PROPS);
}

export async function crop(page, locator, name, pad = 10) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 2 || clip.height < 2) return null;
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box2 = await locator.boundingBox();
  if (!box2) return null;
  const clip2 = {
    x: Math.max(0, box2.x - pad),
    y: Math.max(0, box2.y - pad),
    width: Math.min(vp.width - Math.max(0, box2.x - pad), box2.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box2.y - pad), box2.height + pad * 2),
  };
  await page.screenshot({ path: file, clip: clip2 });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert('RGB')
im.save(${JSON.stringify(file)}, 'PNG')
`], { stdio: 'ignore' });
  } catch { /* keep the full-colour crop if Pillow is missing */ }
  return file;
}
