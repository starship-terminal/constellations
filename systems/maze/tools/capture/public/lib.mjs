// Shared helpers for the Maze public capture (maze.co + auth.maze.co + a
// published sample report on app.maze.co). Adapted from the kit's public
// route. Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// Nothing here signs in, submits a form, starts a study, or clicks a consent
// control. OneTrust and the survey promo are hidden, never answered.
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

export const BASE = 'https://maze.co';
export const AUTH = 'https://auth.maze.co';
export const APP = 'https://app.maze.co';
// Maze's own published sample report. It loads signed out. It is a report,
// not a study to take. Its URL is a share link, and a share link that grants
// access is masked like a signed URL (owner's rule, 2026-11-21), so it is not
// committed: set MAZE_REPORT_URL to the report's link before a capture.
// measure.mjs and vars.mjs stop without it; public.mjs skips the report pages.
export const REPORT = process.env.MAZE_REPORT_URL || null;
// Every file a capture writes goes through maskReport, so the link used to
// navigate is never saved: the committed placeholder takes its place.
export const REPORT_PLACEHOLDER = 'https://app.maze.co/report/[share-link]';
export function maskReport(text) {
  return REPORT ? String(text).split(REPORT).join(REPORT_PLACEHOLDER) : String(text);
}
export function requireReport() {
  if (!REPORT) throw new Error('MAZE_REPORT_URL is not set: the sample report link is not committed (a share link is masked like a signed URL)');
  return REPORT;
}

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CookieYes on maze.co (.cky-*), OneTrust on auth.maze.co. Hide both.
// Never click Accept All, Customize, or Save My Preferences.
const CONSENT = '.cky-consent-container, .cky-modal, .cky-overlay, #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter, #ot-sdk-btn-floating';

export async function hideConsent(page) {
  await page.addStyleTag({
    content: `${CONSENT}, .cky-consent-container, .cky-modal, .cky-overlay, #onetrust-consent-sdk{display:none!important;visibility:hidden!important;pointer-events:none!important}
      body, html { overflow: auto !important; }`,
  }).catch(() => {});
  await page.evaluate((sel) => {
    document.querySelectorAll(sel).forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
      el.setAttribute('aria-hidden', 'true');
    });
    // Survey promo ("Help shape Maze's Future of Research Report 2027").
    // Hide the whole bar, including its close control. Never click it:
    // Take the survey starts a study.
    const hits = [...document.querySelectorAll('div, aside, section, a, p, span')].filter((x) => /future of research report 2027|what does market research look like today/i.test(x.innerText || '') && (x.innerText || '').length < 180);
    const hit = hits.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
    if (hit) {
      let el = hit;
      for (let i = 0; i < 5 && el.parentElement && el.parentElement !== document.body; i++) {
        const r = el.parentElement.getBoundingClientRect();
        const text = (el.parentElement.innerText || '');
        if (r.height > 20 && r.height < 80 && r.width > 280 && text.length < 220) el = el.parentElement;
        else break;
      }
      el.style.setProperty('display', 'none', 'important');
    }
  }, CONSENT).catch(() => {});
}

export async function patch(context) {
  // webdriver mask only. Do not inject a style or observer before hydration:
  // maze.co's React tree stays blank (error 421) if the document mutates first.
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
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

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 300),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /verify you are human|checking your browser|performing security verification/i.test(s.body);
    if (!challenging && (s.body.length > 20 || /maze/i.test(s.title))) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  // A bot check that never clears is not the product: fail the page instead of measuring it.
  if (!(await clearChallenge(page))) throw new Error('challenge did not clear: ' + url);
  // Wait for paint before hiding consent. An init-script style tag blanks
  // maze.co's React tree (minified error 421).
  for (let i = 0; i < 16; i++) {
    const ready = await page.evaluate(() => {
      const h = document.querySelector('h1, h2, form');
      const r = h && h.getBoundingClientRect();
      const header = document.querySelector('header');
      const hr = header && header.getBoundingClientRect();
      const painted = !!(r && r.height > 16 && (document.body.innerText || '').length > 40);
      const bar = !header || (hr && hr.height > 40 && hr.y < 200);
      return painted && bar;
    }).catch(() => false);
    if (ready) break;
    await page.waitForTimeout(500);
  }
  await page.waitForTimeout(Math.min(wait, 800));
  await hideConsent(page);
  await page.evaluate(() => {
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
  }).catch(() => {});
  // Reports paint "Loading..." then the slides. Wait that out, bounded.
  if (/app\.maze\.co\/report/.test(url)) {
    for (let i = 0; i < 10; i++) {
      const body = await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 80)).catch(() => '');
      if (body && !/^Loading/i.test(body) && body.length > 40) break;
      await page.waitForTimeout(1500);
    }
    await hideConsent(page);
  }
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
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    // Marketing CTAs are an <a> wrapping a <button> that paints the text.
    // Auth links paint text on the anchor. Record the deepest text child.
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
  await locator.page().waitForTimeout(280);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}
