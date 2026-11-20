// Shared helpers for the MasterClass public capture.
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
export const BASE = 'https://www.masterclass.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CSS-module classes are `<file>_<name>__<hash>`. Stable prefix match.
export const M = (name) => `[class*="${name}"]`;

const CONSENT_CSS = `
#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
#onetrust-pc-sdk, .ot-sdk-container, [id*="onetrust"],
iframe[title*="consent" i], [class*="cookie-banner"], [id*="cookie-banner"] {
  display: none !important; visibility: hidden !important; pointer-events: none !important;
}`;

export async function hideConsent(page) {
  await page.addStyleTag({ content: CONSENT_CSS }).catch(() => {});
  await page.evaluate(() => {
    for (const sel of ['#onetrust-consent-sdk', '#onetrust-banner-sdk', '.onetrust-pc-dark-filter']) {
      document.querySelectorAll(sel).forEach((el) => el.remove());
    }
  }).catch(() => {});
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  // Automation is not hidden (no webdriver mask): a bot check is recorded as a boundary, not bypassed.
  return { browser, context };
}

// Whether the page is a bot check (Cloudflare and the like) rather than the product. Automation is
// not hidden, so a rerun can meet one; it is recorded as a boundary and nothing from it is saved.
export async function blockedByChallenge(page) {
  const s = await page.evaluate(() => ({ title: document.title, body: (document.body && document.body.innerText || '').slice(0, 400) }))
    .catch(() => ({ title: '', body: '' }));
  return /just a moment|attention required|verify you are human/i.test(s.title)
    || /performing security verification|verify you are human|checking your browser|press ?& ?hold|you have been blocked/i.test(s.body);
}

export async function open(page, url, { wait = 4000 } = {}) {
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
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'cursor', 'opacity', 'overflow', 'zIndex',
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
    const textEl = el.querySelector('h1, h2, h3, p, span, a, button') || el;
    const ts = getComputedStyle(textEl);
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
      textStyle: { fontFamily: ts.fontFamily, fontSize: ts.fontSize, fontWeight: ts.fontWeight, lineHeight: ts.lineHeight, color: ts.color, letterSpacing: ts.letterSpacing },
      viewport: { innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio },
    };
  }, PROPS);
}

export async function crop(locator, file) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return false;
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await locator.screenshot({ path: file }).catch(async () => {
    const b = await locator.boundingBox();
    if (!b) return;
    await locator.page().screenshot({ path: file, clip: { x: Math.max(0, b.x), y: Math.max(0, b.y), width: Math.min(b.width, 1400), height: Math.min(b.height, 900) } });
  });
  return true;
}

export function quantize(file) {
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGBA')
bg = Image.new('RGB', im.size, (13, 13, 14))
bg.paste(im, mask=im.split()[-1])
bg.quantize(colors=256, method=2).save(${JSON.stringify(file)})
`], { stdio: 'ignore' });
  } catch { /* leave the full-colour crop */ }
}
