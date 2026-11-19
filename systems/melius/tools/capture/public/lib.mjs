// Shared helpers for the Melius public capture (www.melius.com + the
// signed-out app.melius.com login and signup cards + docs.melius.com).
// Adapted from the kit's public route. Run with PLAYWRIGHT pointing at a
// Playwright install (index.mjs).
//
// Nothing here signs in, submits a form, starts a checkout, or clicks a
// consent control. Billing, Google OAuth, and the newsletter are never
// followed. The login and signup pages are opened by URL and left
// unsubmitted.
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

export const BASE = 'https://www.melius.com';
export const APP = 'https://app.melius.com';
export const DOCS = 'https://docs.melius.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// c15t consent banner, if it mounts. Hide it. Never click Accept or Reject.
const CONSENT = '[class*="c15t"], [id*="c15t"], [data-consent], #onetrust-consent-sdk, #onetrust-banner-sdk, .cky-consent-container';

export async function hideConsent(page) {
  await page.addStyleTag({
    content: `${CONSENT}{display:none!important;visibility:hidden!important;pointer-events:none!important}
      body, html { overflow: auto !important; }`,
  }).catch(() => {});
}

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr } = {}) {
  const browser = await chromium.launch({ headless: true });
  const scale = dpr ?? (mobile ? 2 : 2);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: scale, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 6, step = 1200 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /verify you are human|checking your browser|performing security verification|cf-challenge/i.test(s.body);
    if (challenging) {
      if (i === tries - 1) return false;
      await page.waitForTimeout(step);
      continue;
    }
    if (s.body.length > 20 || /melius/i.test(s.title)) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 1800 } = {}) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  const ok = await clearChallenge(page);
  if (!ok) {
    const title = await page.title().catch(() => '');
    throw new Error(`Cloudflare or empty page at ${url} (title: ${title}). Stopping this launch.`);
  }
  for (let i = 0; i < 16; i++) {
    const ready = await page.evaluate(() => {
      const h = document.querySelector('h1, h2, form, input');
      const r = h && h.getBoundingClientRect();
      return !!(r && r.height > 8 && (document.body.innerText || '').length > 30);
    }).catch(() => false);
    if (ready) break;
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(Math.min(wait, 600));
  await hideConsent(page);
  await page.evaluate(() => {
    const stop = (obj) => { try { obj && obj.stop && obj.stop(); } catch { /* Lenis optional */ } };
    stop(window.lenis);
    stop(window.__lenis);
    document.documentElement.classList.add('lenis-stopped');
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
  }).catch(() => {});
  return res;
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
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 8).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    let tEl = el;
    for (let i = 0; i < 4; i++) {
      const kids = [...tEl.children].filter((k) => (k.innerText || '').trim());
      if (kids.length !== 1) break;
      tEl = kids[0];
    }
    if (tEl !== el && (tEl.innerText || '').trim()) {
      out.textStyle = pick(getComputedStyle(tEl));
      out.textTag = tEl.tagName.toLowerCase();
    }
    const before = getComputedStyle(el, '::before');
    const after = getComputedStyle(el, '::after');
    const pseudo = (cs) => ({
      width: cs.width, height: cs.height, position: cs.position,
      backgroundColor: noUrl(cs.backgroundColor),
      backgroundImage: noUrl(cs.backgroundImage),
      borderRadius: cs.borderRadius, boxShadow: noUrl(cs.boxShadow),
      content: cs.content,
    });
    if (before.content && before.content !== 'none') out['::before'] = pseudo(before);
    if (after.content && after.content !== 'none') out['::after'] = pseudo(after);
    return out;
  }, PROPS);
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box) throw new Error(`no box for ${name}`);
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

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(220);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}
