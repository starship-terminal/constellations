// Shared helpers for the luluandgeorgia.com public captures.
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
export const BASE = 'https://www.luluandgeorgia.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Shopify storefront. Header chrome uses semantic classes (js-site-logo,
// js-account-toggle, marqo-header-search, button-cta). Search is Marqo.
// Consent is a DataGrail banner (.dg-consent-banner). Selectors key off
// those classes and roles, never account text.
export const M = (name) => `.${name}`;

const CONSENT = /datagrail|dg-consent|cookielaw\.org|onetrust\.com|cookiepro\.com|privacy-mgmt|transcend-cdn|cdn\.transcend\.io|consent\.cookielaw/;

export async function patch(context) {
  // Automation is not hidden: no navigator.webdriver mask (bot check: recorded as a boundary, not bypassed).
  await context.route(CONSENT, (r) => r.abort());
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr = 1 } = {}) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
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

// DataGrail consent banner (.dg-consent-banner) plus Klaviyo newsletter
// embeds. REMOVE-ONLY: hiding never accepts, rejects, or POSTs a consent
// record, and never submits the newsletter form.
export async function hideOverlays(page) {
  await page.addStyleTag({
    content: `
      .dg-consent-banner, #dg-consent-banner, [class*="dg-consent"],
      .klaviyo-form, .needsclick, [class*="kl-private"],
      iframe[title*="cookie" i], iframe[id*="consent" i],
      #swym-consent-popup, .swym-consent-popup,
      #gladlyChat_container, [class*="gladly"], [id*="gladly"],
      iframe[title*="chat" i], [class*="gorgias"], #gorgias-chat-container {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
      }
      body { overflow: auto !important; }
    `,
  }).catch(() => {});
  await page.evaluate(() => {
    for (const sel of ['.dg-consent-banner', '[class*="dg-consent"]', '.klaviyo-form', '.needsclick', '#swym-consent-popup']) {
      document.querySelectorAll(sel).forEach((n) => n.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

export async function closePromo(page) {
  await hideOverlays(page);
  return true;
}

export async function styleOf(locator) {
  return locator.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const pick = (names) => Object.fromEntries(names.map((n) => [n, cs[n]]));
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      textTransform: cs.textTransform,
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      borderTopWidth: cs.borderTopWidth,
      borderTopStyle: cs.borderTopStyle,
      borderTopColor: cs.borderTopColor,
      borderRadius: cs.borderRadius,
      padding: cs.padding,
      boxShadow: cs.boxShadow,
      outline: cs.outline,
      outlineOffset: cs.outlineOffset,
      opacity: cs.opacity,
      textDecoration: cs.textDecorationLine,
      ...pick([]),
    };
  });
}

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await locator.evaluate((el) => {
    const r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  });
  if (box.width < 2 || box.height < 2) throw new Error('crop has no box: ' + name);
  const dpr = await page.evaluate(() => window.devicePixelRatio || 1);
  const vw = page.viewportSize().width;
  const vh = page.viewportSize().height;
  const x = Math.max(0, box.x - pad);
  const y = Math.max(0, box.y - pad);
  const width = Math.min(vw - x, box.width + pad * 2);
  const height = Math.min(vh - y, box.height + pad * 2);
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({ path: file, clip: { x, y, width, height } });
  // Stored as 256 colours like every other committed image.
  execFileSync(PYTHON, ['-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file]);
  return `components/crops/${name}.png`;
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(250);
}

// Returns false when a bot check never cleared, so the caller does not measure the challenge page.
export async function open(page, url, { wait = 3500 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) return false;
  await page.waitForTimeout(wait);
  await hideOverlays(page);
  await page.waitForTimeout(400);
  return true;
}
