// Shared helpers for the The Org public captures.
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
export const BASE = 'https://theorg.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// theorg.com is a styled-components site. Class hashes change between deploys,
// so specs select by role and visible text, never by class.
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
      body: (document.body && document.body.innerText || '').slice(0, 500),
      path: location.pathname,
    })).catch(() => ({ title: '', body: '', path: '' }));
    const challenging = /just a moment|checking your browser|verify to continue/i.test(s.title + ' ' + s.body)
      || /performing security verification|verify you are human|verifying you are human|confirm you are a person/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide a cookie or promo overlay. Never click Accept or Reject.
export async function closePromo(page) {
  await page.evaluate(() => {
    document.querySelectorAll('#onetrust-banner-sdk, [id*="onetrust" i], [class*="cookie" i], [id*="cookie" i], [class*="consent" i]').forEach((x) => {
      const t = (x.innerText || '').slice(0, 400);
      if (/cookie|consent|privacy/i.test(t) || /onetrust|cookie|consent/i.test(x.id || '')) {
        x.style.setProperty('display', 'none', 'important');
      }
    });
  }).catch(() => {});
  return true;
}

// True when the document shows an email, a phone number, or a street address.
// Callers must not screenshot that page.
export async function hasPrivateContact(page) {
  return page.evaluate(() => {
    const t = document.body ? document.body.innerText : '';
    const email = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(t);
    const phone = /\+\d[\d\s().-]{7,}\d/.test(t);
    const street = /\b\d{1,5}\s+[A-Za-z0-9.'-]+\s+(Street|St\.|Avenue|Ave\.|Road|Rd\.|Boulevard|Blvd\.|Drive|Dr\.|Lane|Ln\.)\b/i.test(t);
    return email || phone || street;
  }).catch(() => true);
}

export async function isAuthWall(page) {
  return page.evaluate(() => {
    const path = location.pathname;
    if (/^\/(login|signup|forgot-password|sign-up|register)/.test(path)) return true;
    const inputs = [...document.querySelectorAll('input')].map((i) => (i.getAttribute('type') || '') + ':' + (i.getAttribute('name') || ''));
    return inputs.some((n) => /password/.test(n));
  }).catch(() => true);
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  const ok = await clearChallenge(page, { tries: 4, step: 800 });
  await page.waitForTimeout(wait);
  await closePromo(page);
  return ok;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'rowGap', 'columnGap',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'textDecorationLine', 'textTransform',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'opacity', 'cursor',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = noUrl(cs[p]);
    const out = {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style,
    };
    let tEl = el;
    for (let i = 0; i < 4; i++) {
      const kids = [...tEl.children].filter((k) => (k.innerText || '').trim());
      if (!kids.length) break;
      tEl = kids[kids.length - 1];
    }
    if (tEl !== el) {
      const tcs = getComputedStyle(tEl);
      out.textStyle = {
        color: tcs.color, fontFamily: tcs.fontFamily, fontSize: tcs.fontSize,
        fontWeight: tcs.fontWeight, lineHeight: tcs.lineHeight, letterSpacing: tcs.letterSpacing,
      };
    }
    return out;
  }, PROPS);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box) throw new Error(`no box for ${name}`);
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 2 || clip.height < 2) throw new Error(`clip too small for ${name}`);
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(250);
}
