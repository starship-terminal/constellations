// Shared helpers for the literal.club public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
//
// literal.club sits behind Cloudflare. A bot check is a boundary: when a
// challenge page ("Verify you are human", "Just a moment") is still showing
// after clearChallenge's wait, open() throws and the page is not measured or
// shot. Nothing here solves, clicks, hides or works around a challenge.
// The scripts attach over CDP (CDP=http://127.0.0.1:9339) to a Chrome the
// operator starts with a throwaway profile, for example
//   chrome --remote-debugging-port=9339 --user-data-dir="$(mktemp -d)"
// and never the operator's own profile. Every page opens in a fresh browser
// context, so no cookie or sign-in of that Chrome is used. Consent overlays
// are hidden, never answered. Nothing is signed into or submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://literal.club';
export const CDP = process.env.CDP || 'http://127.0.0.1:9339';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CSS modules: Button_focus__7rs32. Match the stable prefix.
export const M = (name) => `[class*="${name}"]`;

export async function launchBrowser() {
  return chromium.connectOverCDP(CDP);
}

// A page in a fresh context of the CDP browser: never the default context,
// which holds whatever profile that Chrome was started with. Closing the
// page closes its context.
export async function newPage({ browser, width = 1440, height = 900, colorScheme = 'light' }) {
  const context = await browser.newContext({ viewport: { width, height }, colorScheme });
  const page = await context.newPage();
  page.on('close', () => { context.close().catch(() => {}); });
  const bundle = { width, height, colorScheme };
  await page.setViewportSize({ width: bundle.width, height: bundle.height });
  if (bundle.colorScheme === 'dark') await page.emulateMedia({ colorScheme: 'dark' });
  else await page.emulateMedia({ colorScheme: 'light' });
  return page;
}

// Hide a consent layer if one mounts. Never click Accept, Reject, or a consent POST.
export async function hideConsent(page) {
  await page.addStyleTag({ content: `
    #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
    .osano-cm-window, #transcend-consent-manager,
    [id*="cookie-banner"], [class*="cookie-banner"], [class*="CookieBanner"],
    iframe[src*="consent"] {
      display: none !important; visibility: hidden !important; pointer-events: none !important;
    }
  ` }).catch(() => {});
  await page.evaluate(() => {
    const hide = (el) => el.style.setProperty('display', 'none', 'important');
    for (const el of document.querySelectorAll('div, aside, section, dialog')) {
      const t = (el.innerText || '').slice(0, 280);
      const r = el.getBoundingClientRect();
      if (/cookie|consent|we use personal data|accept all cookies/i.test(t)
        && r.width > 140 && r.height > 40 && r.height < 520 && r.top > 400) hide(el);
    }
  }).catch(() => {});
}

export async function clearChallenge(page, { tries = 16, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: ((document.body && document.body.innerText) || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /verify you are human|verifying you are human|performing security verification|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40 && !/just a moment/i.test(s.title)) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 1400 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  const ok = await clearChallenge(page);
  // bot check: recorded as a boundary, not bypassed.
  if (!ok) throw new Error(`bot check still showing on ${new URL(url).pathname}: recorded as a boundary, not bypassed`);
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
    if (el.placeholder) out.placeholder = { color: cs.color, opacity: cs.opacity };
    return out;
  }, PROPS);
}

export async function crop(locator, file, { pad = 8 } = {}) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const dpr = await locator.evaluate(() => window.devicePixelRatio || 1);
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: box.width + pad * 2,
    height: box.height + pad * 2,
  };
  await locator.page().screenshot({ path: file, clip, type: 'png' });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert('RGB')
im.save(${JSON.stringify(file)}, 'PNG', optimize=True)
`], { stdio: 'ignore' });
  } catch { /* keep the full-colour crop if Pillow is missing */ }
  return { ...clip, dpr };
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(200);
}

export function scratchDir() {
  return path.join(os.homedir(), '.design-systems', 'literal');
}
