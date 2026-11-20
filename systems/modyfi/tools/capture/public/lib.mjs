// Shared helpers for the Modyfi public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// BOUNDARY: on 2026-11-19 every live modyfi.com and www.modyfi.com route
// returned Webflow's own 404 ("Page not found"), and app.modyfi.com did not
// resolve (ERR_NAME_NOT_RESOLVED). Modyfi shut down on 2025-06-13 after the
// Figma acquisition. The capture therefore renders the product's own pages
// from the Internet Archive: each route is
// https://web.archive.org/web/<timestamp>/<original url>. Wayback chrome is
// hidden, never answered. Nothing is signed into, paid for, or submitted.
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
export const BASE = 'https://web.archive.org/web/';
export const SITE = 'https://www.modyfi.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Relume / Webflow class names are stable (rl_navbar2_button, button-7).
export const M = (name) => `[class*="${name}"]`;

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
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /performing security verification|verify you are human|this url is in the wayback machine but is not archived|wayback machine doesn't have that page archived|page not found/i.test(s.body + ' ' + s.title);
    if (!challenging && s.body.length > 40 && /modyfi/i.test(s.title + s.body)) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide Wayback chrome only. Never click a consent or signup control.
export async function closePromo(page) {
  await page.evaluate(() => {
    document.querySelectorAll('#wm-ipp-base, #wm-ipp-print, #wm-ipp, [id^="wm-ipp"], .wb-autocomplete-suggestions, #donato, #playback, #sparkles-md, iframe[src*="archive.org"]').forEach((x) => {
      x.style.setProperty('display', 'none', 'important');
    });
    document.documentElement.style.removeProperty('margin-top');
    document.body && document.body.style.removeProperty('margin-top');
  }).catch(() => {});
  return true;
}

export async function open(page, url, { wait = 5000 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await closePromo(page);
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'rowGap', 'columnGap',
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'opacity',
];

export function readBox(el) {
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const out = { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80) };
  for (const k of ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle', 'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'opacity', 'textTransform']) {
    out[k] = s[k];
  }
  out.width = Math.round(r.width) + 'px';
  out.height = Math.round(r.height) + 'px';
  return out;
}

export { fs, path, execFileSync, PYTHON };
