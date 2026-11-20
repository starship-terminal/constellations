// Shared helpers for the kickstarter.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// kickstarter.com sits behind Cloudflare. Headless Chromium is challenged on
// every route except the home page; headed Google Chrome (channel: 'chrome')
// clears the managed challenge. Consent is a Transcend dialog ("We use
// personal data…", Confirm / Accept all). It is hidden, never clicked.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.kickstarter.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launchBrowser() {
  return chromium.launch({
    headless: false,
    channel: 'chrome',
  });
}

export async function newContext(browser, { mobile = false, width = 1440, height = 900, dpr = 1 } = {}) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return context;
}

// Hide the consent layer. Never click Confirm, Accept all, or any consent POST.
export async function hideConsent(page) {
  await page.addStyleTag({ content: `
    #transcend-consent-manager, [id*="transcend"], iframe[src*="transcend"],
    iframe[src*="consent"], iframe[src*="challenges.cloudflare"],
    #onetrust-consent-sdk, .osano-cm-window,
    [class*="consent-manager"], [data-testid*="consent"],
    [class*="statuspage"], [id*="statuspage"], [class*="sp-status"],
    iframe[src*="statuspage"] {
      display: none !important; visibility: hidden !important; pointer-events: none !important;
    }
  ` }).catch(() => {});
  await page.evaluate(() => {
    const hide = (el) => el.style.setProperty('display', 'none', 'important');
    for (const el of document.querySelectorAll('div, aside, section, dialog')) {
      const t = (el.innerText || '').slice(0, 320);
      const r = el.getBoundingClientRect();
      if (/We use personal data|Accept all|Essential purposes|Sale of personal information/i.test(t)
        && r.width > 140 && r.width < 560 && r.height > 70 && r.height < 700) hide(el);
    }
    for (const f of document.querySelectorAll('iframe')) {
      const r = f.getBoundingClientRect();
      const src = f.getAttribute('src') || '';
      if (/transcend|consent|privacy|cloudflare|statuspage/i.test(src) || (r.width > 160 && r.height > 50 && r.height < 520 && r.left < 500)) hide(f);
    }

  }).catch(() => {});
}

export async function clearChallenge(page, { tries = 10, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: ((document.body && document.body.innerText) || '').slice(0, 500),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required|performing security/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser|you have been blocked|unable to access/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(800);
  const ok = await clearChallenge(page);
  await hideConsent(page);
  await page.waitForTimeout(wait);
  await hideConsent(page);
  return ok;
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
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage),
          borderRadius: p.borderRadius, boxShadow: noUrl(p.boxShadow),
        };
      }
    }
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) {
      if (!n.textContent.trim()) continue;
      const pcs = getComputedStyle(n.parentElement);
      out.textStyle = {
        node: n.parentElement.tagName.toLowerCase(),
        fontFamily: pcs.fontFamily, fontSize: pcs.fontSize, fontWeight: pcs.fontWeight,
        lineHeight: pcs.lineHeight, letterSpacing: pcs.letterSpacing, color: pcs.color,
      };
      break;
    }
    const svg = el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const sc = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(1), h: +sr.height.toFixed(1), color: sc.color, fill: sc.fill };
    }
    if (el.placeholder) {
      out.placeholder = { color: cs.color, opacity: cs.opacity };
    }
    return out;
  }, PROPS);
}

export async function crop(locator, file, { pad = 8 } = {}) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: box.width + pad * 2,
    height: box.height + pad * 2,
  };
  await locator.page().screenshot({ path: file, clip });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert('RGB')
im.save(${JSON.stringify(file)}, 'PNG', optimize=True)
`], { stdio: 'ignore' });
  } catch { /* quantize is a second pass; the PNG still stands */ }
  return file;
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(250);
}
