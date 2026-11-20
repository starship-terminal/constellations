// Shared helpers for the Pryzm public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// PRODUCT (adapt): https://pryzm.design is a public Next.js app. The marketing
// shell and the studio apps are both reachable signed out. Sign-in, checkout,
// Google, newsletter and profile forms are never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://pryzm.design';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Pryzm's classes are Tailwind utilities and hashed font modules, so specs
// match by role and visible text. M() stays a pass-through for the kit shape.
export const M = (sel) => sel;

export function isWall(url) {
  return /\/signin|\/login|accounts\.google|oauth|polar\.sh|\/api\/checkout/i.test(url);
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: 'dark' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

// No cookie banner was present on 2026-11-21. Never click a consent POST.
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
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'backgroundColor', 'backgroundImage', 'borderTopColor', 'borderTopWidth',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius',
  'boxShadow', 'opacity', 'outline', 'outlineOffset', 'textDecorationLine',
];
