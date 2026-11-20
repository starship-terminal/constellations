// Shared helpers for the Lemon Squeezy public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// Two public hosts, both signed out:
//   www.lemonsqueezy.com   Webflow marketing (Client-First). :root declares
//                          the --purple-* / --yellow-* / --grey-* ramps.
//   docs.lemonsqueezy.com  Mintlify docs (Tailwind, one light theme).
//   auth.lemonsqueezy.com  the sign-in card and the closed-signup SMP page.
// Merchant dashboard is closed to new store signups. Get started, OAuth,
// bank and payout KYC are not followed.
// Consent overlays are hidden, never answered.
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
export const BASE = 'https://www.lemonsqueezy.com';
export const DOCS = 'https://docs.lemonsqueezy.com';
export const AUTH = 'https://auth.lemonsqueezy.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Webflow class names are stable (Client-First). Pass a class fragment.
export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const scale = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: scale, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

// Hide consent and cookie overlays. Never click a consent control.
export async function hideConsent(page) {
  await page.evaluate(() => {
    const sel = [
      '#onetrust-banner-sdk', '#onetrust-consent-sdk', '#CybotCookiebotDialog',
      '.cc-window', '[id*="cookie" i]', '[class*="cookie" i]',
      '[id*="consent" i]', '[class*="consent" i]',
      '[aria-label*="cookie" i]', '[aria-label*="consent" i]',
    ].join(',');
    document.querySelectorAll(sel).forEach((el) => {
      const t = ((el.innerText || '') + ' ' + (el.id || '') + ' ' + (el.className || '')).toLowerCase();
      if (!/cookie|consent|privacy preference|gdpr/.test(t) && !/onetrust|cookiebot|cc-window/.test((el.id || '') + (el.className || ''))) return;
      el.style.setProperty('display', 'none', 'important');
      el.setAttribute('data-ls-hidden', 'consent');
    });
  }).catch(() => {});
}

export async function open(page, url, { wait = 1800 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
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
    const cls = (n) => [...(n.classList || [])].filter((c) => c && c.length < 48).slice(0, 5);
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
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow,
          borderTopWidth: p.borderTopWidth, borderRadius: p.borderRadius, opacity: p.opacity, transition: p.transition,
        };
      }
    }
    const svg = el.tagName.toLowerCase() === 'svg' ? el : el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const scs = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color };
    }
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.tagName === 'SELECT') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize };
    }
    return out;
  }, PROPS);
}

const STICKY = '.banner, .nav_component, header, [class*="sticky"]';

export async function crop(page, locator, name, pad = 10) {
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
  quantize(file);
  return path.relative(REF, file);
}

function quantize(file) {
  const script = path.resolve(HERE, '..', 'quantize.py');
  execFileSync(PYTHON, [script, file], { stdio: 'ignore' });
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(280);
}

export { STICKY };
