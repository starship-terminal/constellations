// Shared helpers for the forhims.co.uk public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// The UK marketing site (www.forhims.co.uk) is a distinct page from
// www.hims.com. Headless Chromium loads it. Ketch consent ("About cookies
// on our site", Customise / Accept all) is hidden, never clicked.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.forhims.co.uk';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
  });
}

export async function launchBrowser() {
  return chromium.launch({ headless: true });
}

export async function newContext(browser, { mobile = false, width = 1440, height = 900, dpr = 1 } = {}) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-GB' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-GB' });
  await patch(context);
  return context;
}

// Hide the Ketch consent layer. Never click Customise, Accept all, or any consent POST.
export async function hideConsent(page) {
  await page.addStyleTag({ content: `
    #ketch-consent-banner, [id*="ketch"], [class*="ketch-"],
    iframe[src*="ketch"], iframe[src*="consent"],
    #onetrust-consent-sdk, .osano-cm-window,
    [class*="consent-manager"], [data-testid*="consent"] {
      display: none !important; visibility: hidden !important; pointer-events: none !important;
    }
  ` }).catch(() => {});
  await page.evaluate(() => {
    const hide = (el) => {
      el.style.setProperty('display', 'none', 'important');
      el.style.setProperty('visibility', 'hidden', 'important');
      el.style.setProperty('pointer-events', 'none', 'important');
    };
    for (const el of document.querySelectorAll('[role="dialog"], div, aside, section')) {
      const id = (el.id || '') + ' ' + (el.className || '');
      const t = (el.innerText || '').slice(0, 240);
      if (/ketch/i.test(id) || (/About cookies on our site/i.test(t) && /Accept all|Customise/i.test(t))) hide(el);
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(600);
  await hideConsent(page);
  await page.waitForTimeout(wait);
  await hideConsent(page);
  return true;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing',
  'color', 'textDecorationLine', 'opacity',
];

export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string'
      ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)')
      : v);
    const cs = getComputedStyle(el);
    const out = {};
    for (const p of props) out[p] = noUrl(cs[p]);
    const r = el.getBoundingClientRect();
    out._rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    return out;
  }, PROPS);
}

export async function crop(locator, file, { pad = 8 } = {}) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box ' + file);
  const vp = locator.page().viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 2 || clip.height < 2) throw new Error('clip collapsed ' + file);
  await locator.page().screenshot({ path: file, clip });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGBA')
bg = Image.new('RGB', im.size, (255, 255, 255))
bg.paste(im, mask=im.split()[-1])
q = bg.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
q.save(${JSON.stringify(file)}, optimize=True)
`], { stdio: 'ignore' });
  } catch { /* keep the raw crop if Pillow is missing */ }
}

export const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)')
  : v);
