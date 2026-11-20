// Shared helpers for the kraken.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// Scope is signed-out marketing and the sign-in / sign-up boundary.
// OneTrust is hidden, never answered. Nothing is typed into a credential
// field, submitted, or followed into OAuth.
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
export const BASE = 'https://www.kraken.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const HIDE_CONSENT =
  '#onetrust-consent-sdk,#onetrust-banner-sdk,#onetrust-pc-sdk,.onetrust-pc-dark-filter,#ot-sdk-btn-floating,.ot-floating-button,[id^="onetrust"]{display:none!important;visibility:hidden!important;pointer-events:none!important}';

export async function patch(context) {
  await context.addInitScript(() => {
    // navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const scale = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

// Hide the OneTrust layer. Never click Accept, Reject, or Manage.
export async function hideConsent(page) {
  await page.addStyleTag({ content: HIDE_CONSENT }).catch(() => {});
  await page.evaluate(() => {
    for (const sel of ['#onetrust-consent-sdk', '#onetrust-banner-sdk', '#onetrust-pc-sdk', '.onetrust-pc-dark-filter', '#ot-sdk-btn-floating']) {
      for (const el of document.querySelectorAll(sel)) {
        el.style.setProperty('display', 'none', 'important');
        el.style.setProperty('pointer-events', 'none', 'important');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 4000 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(Math.min(wait, 2500));
  await hideConsent(page);
  await clearAutofill(page);
  await page.waitForTimeout(Math.max(0, wait - 2500));
  await hideConsent(page);
  await clearAutofill(page);
}

// Browser autofill can paint an email into a public field. Clear it.
// Never type a replacement and never submit.
export async function clearAutofill(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('input, textarea')) {
      const v = el.value || '';
      if (/@/.test(v) || /satoshi/i.test(v)) {
        el.value = '';
        el.setAttribute('value', '');
        el.dispatchEvent(new Event('input', { bubbles: true }));
      }
    }
  }).catch(() => {});
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
    const cls = [...el.classList].slice(0, 6).join(' ');
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: cls.slice(0, 180),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
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
        node: n.tagName.toLowerCase(),
        size: `${rr.width.toFixed(0)}x${rr.height.toFixed(0)}`,
        bg: bg || undefined,
        shadow: sh ? sh.slice(0, 120) : undefined,
        radius: c.borderRadius,
        color: c.color,
      });
    }
    if (paint.length) out.paint = paint;
    return out;
  }, PROPS);
}

const STICKY = 'header, [class*="sticky"], #onetrust-consent-sdk';
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  await hideConsent(page);
  const box = await locator.boundingBox();
  if (!box || box.width < 1 || box.height < 1) throw new Error(`no box for ${name}`);
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

export function quantize(file) {
  const script = path.resolve(HERE, '..', 'quantize.py');
  execFileSync(PYTHON, [script, file, file], { stdio: 'ignore' });
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(280);
}

export async function mark(page, js) {
  const ok = await page.evaluate(js);
  return ok;
}
