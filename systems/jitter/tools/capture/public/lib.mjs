// Shared helpers for the jitter.video public captures.
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
export const BASE = 'https://jitter.video';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CSS-modules classes look like _button_ruopi_1. Match the stable prefix.
export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 20, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide cookie/consent overlays and the Intercom launcher. Never click a
// consent control, and never open the messenger.
export async function closePromo(page) {
  for (let i = 0; i < 3; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      for (const sel of [
        '#intercom-container',
        '.intercom-lightweight-app',
        '.intercom-launcher',
        'iframe[name="intercom-launcher-frame"]',
        '[class*="intercom-lightweight"]',
        '#onetrust-consent-sdk',
        '#onetrust-banner-sdk',
        '[id*="cookie-banner" i]',
        '[class*="cookie-banner" i]',
        '[id*="consent" i]',
      ]) {
        document.querySelectorAll(sel).forEach((el) => {
          el.style.setProperty('display', 'none', 'important');
          n++;
        });
      }
      const hits = [...document.querySelectorAll('div,section,aside,[role="dialog"]')].filter((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /cookie|consent|we value your privacy|privacy preference/i.test(t)
          && t.length < 1600 && r.width > 200 && r.height > 40 && r.height < 700;
      });
      const box = hits.find((x) => !hits.some((o) => o !== x && x.contains(o)));
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      return n;
    }).catch(() => 0);
    if (!hit) return true;
    await page.waitForTimeout(300);
  }
  return true;
}

export async function open(page, url, { wait = 4000, promo = 'close' } = {}) {
  // A failed load or a challenge page that never clears is a boundary,
  // never measured as the product: open() logs BLOCKED, leaves the tab on
  // about:blank and returns false (true once the page loaded), without
  // stopping the rest of the run. Every caller checks the result and skips
  // the page or group, or fails the reading, so a blank tab is never saved
  // as the product (2026-11 audit, finding 20-4; not run since).
  const loaded = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).then(() => true, (e) => { console.log(`BLOCKED ${url}: ${String(e.message).split('\n')[0]}`); return false; });
  if (!loaded || !(await clearChallenge(page))) {
    if (loaded) console.log(`BLOCKED ${url}: the challenge page never cleared`);
    await page.goto('about:blank').catch(() => {});
    return false;
  }
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  return true;
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
    const cls = (n) => [...n.classList].map((c) => String(c)).filter((c) => c && !/^x[0-9a-z]{5,8}$/.test(c));
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
      classes: cls(el).slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    const inner = el.querySelector('.button-inner, [class*="_inner_"]');
    if (inner) {
      const ics = getComputedStyle(inner);
      out.face = {
        backgroundColor: ics.backgroundColor,
        color: ics.color,
        borderRadius: ics.borderRadius,
        boxShadow: ics.boxShadow,
        padding: ics.padding,
        height: ics.height,
        fontSize: ics.fontSize,
        fontWeight: ics.fontWeight,
        fontFamily: ics.fontFamily,
      };
    }
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, borderRadius: p.borderRadius, opacity: p.opacity,
        };
      }
    }
    const paint = [];
    const nodes = [el, ...el.querySelectorAll('*')].slice(0, 80);
    for (const n of nodes) {
      if (paint.length >= 8) break;
      if (n.closest('svg') && n.tagName.toLowerCase() !== 'svg') continue;
      const c = getComputedStyle(n);
      const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
      const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
      const ol = c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor}` : '';
      if (!(bg || sh || ol)) continue;
      const rr = n.getBoundingClientRect();
      paint.push({
        node: n.tagName.toLowerCase() + cls(n).slice(0, 2).map((x) => '.' + x).join(''),
        size: `${rr.width.toFixed(0)}x${rr.height.toFixed(0)}`,
        bg: bg || undefined, shadow: sh || undefined, outline: ol || undefined,
        radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        color: c.color,
      });
    }
    if (paint.length) out.paint = paint;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize };
    }
    return out;
  }, PROPS);
}

const STICKY = 'header, .intercom-lightweight-app, #intercom-container';
export async function crop(page, locator, name, pad = 10) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, sel) => {
    let n = 0;
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      n++;
    });
    return n;
  }, STICKY).catch(() => 0);
  try {
    const box = await locator.boundingBox();
    if (!box) throw new Error(`no box for ${name}`);
    const vp = page.viewportSize();
    const inView = box.y - pad >= 0 && box.y + box.height + pad <= vp.height && box.x >= -1 && box.x + box.width <= vp.width + 1;
    if (inView) {
      const clip = {
        x: Math.max(0, box.x - pad),
        y: Math.max(0, box.y - pad),
        width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
        height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
      };
      await page.screenshot({ path: file, clip });
    } else {
      await locator.screenshot({ path: file });
    }
  } finally {
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.removeAttribute('data-m-hidden'); }));
  }
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(250);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}
