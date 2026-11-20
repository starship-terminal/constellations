// Shared helpers for the MonoDesk public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.monodesk.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/monodesk
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export function isWall(url) {
  try {
    const u = new URL(url);
    if (u.hostname === 'app.monodesk.com') return true;
    return /\/(login|signin|sign-up|signup|register|create)(\/|$)/i.test(u.pathname);
  } catch {
    return false;
  }
}

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

// Cookie and newsletter overlays are hidden, never clicked (FIELD-NOTES: a
// consent button can POST). The phone "email me the link" prompt is a form;
// its dismiss control is a local hide, not a POST, so it may be pressed.
export async function hideOverlays(page) {
  await page.evaluate(() => {
    const nodes = document.querySelectorAll('[class*="cookie" i], [id*="cookie" i], [class*="consent" i], [id*="consent" i], #onetrust-banner-sdk');
    for (const el of nodes) {
      const t = (el.innerText || '').slice(0, 240).toLowerCase();
      if (/cookie|consent|privacy preference/.test(t)) el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

export async function dismissDesktopPrompt(page) {
  const b = page.locator('button.desktop-link__dismiss');
  if (await b.count() && await b.first().isVisible().catch(() => false)) {
    await b.first().click({ timeout: 2000 }).catch(() => {});
    await page.waitForTimeout(300);
  }
}

export async function open(page, url, { wait = 1800 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  if (isWall(page.url())) throw new Error('login wall: ' + page.url());
  await hideOverlays(page);
  return res;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textAlign', 'color',
  'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'outlineStyle', 'outlineWidth', 'outlineColor', 'outlineOffset',
  'opacity', 'textDecorationLine',
];

export async function styleOf(el) {
  return el.evaluate((node, props) => {
    const s = getComputedStyle(node);
    const out = {};
    for (const p of props) out[p] = s[p];
    const r = node.getBoundingClientRect();
    out._box = { x: r.x, y: r.y, width: r.width, height: r.height };
    return out;
  }, PROPS);
}
