// Shared helpers for the Kitchen.co public capture.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const PYTHON = process.env.PYTHON || 'python3';
export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://kitchen.co';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..'); // systems/kitchen, from tools/capture
export const RAW = path.join(REF, 'raw');

export const PAGES = {
  home: '/',
  features: '/features',
  pricing: '/pricing',
  buy: '/buy',
  reviews: '/reviews',
  tutorials: '/tutorials',
  integrations: '/integrations',
  'how-it-works': '/how-it-works',
  benefits: '/benefits',
  about: '/about',
  'our-story': '/our-story',
  blog: '/blog',
  'affiliate-program': '/affiliate-program',
  'for-creative-agencies': '/for-creative-agencies',
  'for-accounting-agencies': '/for-accounting-agencies',
  'for-law-firms': '/for-law-firms',
  'for-freelancers': '/for-freelancers',
  login: '/login',
  'login-find': '/login/find',
  'get-started': '/get-started',
  'get-demo': '/get-demo',
  'cookie-policy': '/legal/cookie-policy',
  terms: '/legal/terms',
  privacy: '/legal/privacy',
  dpa: '/legal/dpa',
};

// Hide cookie/consent overlays. Never click a consent control (that POSTs).
export async function hideConsent(page) {
  await page.addStyleTag({
    content: [
      '#cookie-banner, #cookie-consent, .cookie-banner, .cookie-consent, .cookie-notice,',
      '.cc-window, .cc-banner, #onetrust-banner-sdk, #CybotCookiebotDialog,',
      '[class*="cookie-bar"], [id*="cookie-consent"], [aria-label*="cookie" i],',
      '[class*="consent-banner"], .legal-docs-banner, .js-cookie, .cookies',
      '{ display: none !important; visibility: hidden !important; pointer-events: none !important; }',
    ].join(''),
  }).catch(() => {});
  await page.evaluate(() => {
    const words = /cookie|consent|gdpr/i;
    for (const el of document.querySelectorAll('div, aside, section, dialog')) {
      const t = (el.innerText || '').slice(0, 400);
      const r = el.getBoundingClientRect();
      if (words.test(t) && /accept|decline|reject|allow|preferences/i.test(t) && r.height > 40 && r.height < 420 && r.width > 240) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

export async function open(page, url, { wait = 2500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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
    const textNode = [...el.childNodes].find((n) => n.nodeType === 3 && n.textContent.trim());
    let textStyle = null;
    if (textNode) {
      const range = document.createRange();
      range.selectNodeContents(textNode);
      const tcs = getComputedStyle(el);
      textStyle = {
        node: 'text',
        fontFamily: tcs.fontFamily,
        fontSize: tcs.fontSize,
        fontWeight: tcs.fontWeight,
        lineHeight: tcs.lineHeight,
        letterSpacing: tcs.letterSpacing,
        color: tcs.color,
      };
    }
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 4).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
      textStyle,
    };
  }, PROPS);
}

export async function crop(page, locator, name, pad = 8) {
  const { execFileSync } = await import('node:child_process');
  const fs = await import('node:fs');
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box');
  const dpr = page.viewportSize() ? (await page.evaluate(() => window.devicePixelRatio)) : 1;
  const dir = path.join(REF, 'components', 'crops');
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `${name}.png`);
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: box.width + pad * 2,
    height: box.height + pad * 2,
  };
  await page.screenshot({ path: file, clip, scale: 'css' });
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert('RGB')
im.save(${JSON.stringify(file)}, 'PNG', optimize=True)
`], { stdio: 'ignore' });
  } catch { /* quantize later */ }
  return `components/crops/${name}.png`;
}
