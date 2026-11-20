// Shared helpers for the rivian.com public captures.
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
export const BASE = 'https://rivian.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US' });
  return { browser, context };
}

// Reject optional cookies when the Ketch control is in the document. If the
// button is clipped (it often is), hide the banner shell so it does not cover
// the page. Hiding is the fallback FIELD-NOTES records for a consent POST.
export async function dismissConsent(page) {
  // Ketch mounts #ketch-banner a few seconds after load, in the light DOM.
  // Wait for Reject All, click only that button, then hide the shell if the
  // dialog is still covering the page. Never click Accept or Confirm.
  const loc = page.locator('#ketch-banner-button-secondary');
  let clicked = 'absent';
  try {
    await loc.waitFor({ state: 'attached', timeout: 8000 });
    await loc.click({ timeout: 4000 });
    clicked = 'reject-all';
    await page.waitForTimeout(800);
  } catch {
    clicked = 'absent';
  }
  const still = await loc.count().catch(() => 0);
  let hidden = 0;
  if (still) {
    hidden = await page.evaluate(() => {
      const root = document.querySelector('#lanyard_root');
      if (root) { root.style.setProperty('display', 'none', 'important'); return 1; }
      return 0;
    }).catch(() => 0);
  }
  return { clicked, hidden, still };
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await dismissConsent(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'backgroundColor', 'color', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight',
  'letterSpacing', 'textTransform', 'textDecoration', 'opacity', 'outline', 'outlineOffset',
];

export async function styleOf(loc) {
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = cs[p];
    const r = el.getBoundingClientRect();
    o._box = { x: r.x, y: r.y, w: r.width, h: r.height };
    return o;
  }, PROPS);
}

export async function crop(page, loc, file) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 2 || clip.height < 2) return null;
  await page.screenshot({ path: file, clip });
  return clip;
}

export function quantizeDir(dir) {
  const q = path.resolve(HERE, '..', 'quantize.py');
  execFileSync(PYTHON, [q, dir], { stdio: 'inherit' });
}
