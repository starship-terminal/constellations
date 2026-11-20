// Shared helpers for the lego.com public captures (adapted from the kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// lego.com (Official LEGO Shop US, /en-us) is a Skroll storefront. It paints
// one light theme. Consent is a first-party modal (data-test cookie-accept-all
// / cookie-necessary-button). Hide it. Never click Accept, Reject, or Save.
// Age-gate URLs already carry ?age-gate=grown_up from the shop's own redirect;
// the grown-up CTA is not clicked. Nothing is signed into, added to the bag,
// or checked out.
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
export const BASE = 'https://www.lego.com';
export const LOCALE = '/en-us';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // automation is not hidden: navigator.webdriver is left as the browser reports it.
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr ?? 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr ?? 1, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|access denied|are you a robot/i.test(s.title)
      || /performing security verification|verify you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide consent, age-gate and promo overlays. Never click a consent control.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      const sel = [
        '[class*="consent-modal"]',
        '[class*="consent"]',
        '[id*="consent"]',
        '[class*="onetrust"]',
        '[id*="onetrust"]',
        '[data-test="cookie-accept-all"]',
        '[data-test="cookie-necessary-button"]',
        '[data-test="age-gate-grown-up-cta"]',
        '[class*="AgeGate"]',
        '[class*="age-gate"]',
        'dialog',
      ].join(',');
      document.querySelectorAll(sel).forEach((el) => {
        const root = el.closest('dialog, [role="dialog"], [class*="consent-modal"], [class*="age-gate"], [class*="AgeGate"]') || el;
        root.remove();
        n++;
      });
      document.querySelectorAll('[role="dialog"], dialog, [class*="modal"]').forEach((el) => {
        const t = (el.innerText || '').slice(0, 500);
        if (/privacy preferences|cookie|age gate|play zone|are you a grown|start playing/i.test(t)) { el.remove(); n++; }
      });
      document.body && document.body.style.setProperty('overflow', 'auto', 'important');
      document.documentElement && document.documentElement.style.setProperty('overflow', 'auto', 'important');
      return n;
    }).catch(() => 0);
    if (!hit) { await page.waitForTimeout(400); continue; }
    await page.waitForTimeout(300);
  }
  return true;
}

export function withGate(url) {
  if (/age-gate=/.test(url)) return url;
  return url + (url.includes('?') ? '&' : '?') + 'age-gate=grown_up';
}

export async function open(page, url, { wait = 4000 } = {}) {
  await page.goto(withGate(url.startsWith('http') ? url : BASE + url), { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(Math.min(wait, 1500));
  await closePromo(page);
  await page.waitForTimeout(Math.max(0, wait - 1500));
  if (!(await clearChallenge(page))) throw new Error('challenge: ' + url);
  await closePromo(page);
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
    const cls = (n) => [...n.classList].slice(0, 4);
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
      test: el.getAttribute('data-test') || '',
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    return out;
  }, PROPS);
}

const STICKY = 'header, [class*="header"], [data-test="sitewide-banner"], [class*="sitewide"]';
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, sel) => {
    let n = 0;
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      const cs = getComputedStyle(s);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      n++;
    });
    return n;
  }, STICKY).catch(() => 0);
  try {
    const box = await locator.boundingBox();
    if (!box || box.width < 2 || box.height < 2) throw new Error(`no box for ${name}`);
    const vp = page.viewportSize();
    const clip = {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
      height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
    };
    if (clip.width < 2 || clip.height < 2) throw new Error(`clip too small for ${name}`);
    await page.screenshot({ path: file, clip, animations: 'disabled' });
  } finally {
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.removeAttribute('data-m-hidden'); })).catch(() => {});
  }
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(280);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}
