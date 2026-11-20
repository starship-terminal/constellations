// Shared helpers for the Lummi public signed-out capture.
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
export const BASE = 'https://www.lummi.ai';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// OneTrust cookie banner. Hide it. Never click Accept, Reject, or Save.
const CONSENT = '#onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk, .onetrust-pc-dark-filter, #onetrust-style';

export async function hideConsent(page) {
  await page.addStyleTag({
    content: `${CONSENT}{display:none!important;visibility:hidden!important;pointer-events:none!important}`,
  }).catch(() => {});
  await page.evaluate((sel) => {
    document.querySelectorAll(sel).forEach((el) => el.remove());
  }, CONSENT).catch(() => {});
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const deviceScaleFactor = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor, userAgent: UA, locale: 'en-US' });
  await context.addInitScript((sel) => {
    const hide = () => document.querySelectorAll(sel).forEach((el) => el.remove());
    const start = () => {
      hide();
      new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    };
    if (document.documentElement) start();
    else document.addEventListener('DOMContentLoaded', start);
  }, CONSENT);
  return { browser, context };
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.waitForTimeout(250);
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
    const cls = (n) => [...(n.classList || [])].filter((c) => c && c.length < 48).slice(0, 8);
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
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize };
    }
    const svg = el.tagName.toLowerCase() === 'svg' ? el : el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const scs = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color };
    }
    return out;
  }, PROPS);
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error(`no box for ${name}`);
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 4 || clip.height < 4) throw new Error(`clip too small for ${name}`);
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(200);
}
