// Shared helpers for the Missive public capture (missiveapp.com marketing
// and the signed-out mail.missiveapp.com auth screens). Adapted from the
// kit's public route. Run with PLAYWRIGHT pointing at a Playwright install.
//
// Nothing here signs in, submits a form, books a demo, or starts checkout.
// Book a demo leaves the site for Calendly and is never followed. Cookie
// banners, when present, are hidden, never clicked.
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

export const BASE = 'https://missiveapp.com';
export const MAIL = 'https://mail.missiveapp.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');

const CONSENT = '#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter, .cky-consent-container, .cky-modal, .cky-overlay, [id*="cookie-banner"], [class*="cookie-banner"], [class*="cookie-consent"]';

export async function hideConsent(page) {
  // Hide only. Never click "I understand", Accept, or a vendor toggle.
  await page.addStyleTag({
    content: `${CONSENT}{display:none!important;visibility:hidden!important;pointer-events:none!important}`,
  }).catch(() => {});
  await page.evaluate(() => {
    const hits = [...document.querySelectorAll('div, section, aside')].filter((el) => {
      const t = (el.innerText || '').trim();
      return t.startsWith('Your Privacy Choices') && t.length < 900;
    });
    const hit = hits.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
    if (!hit) return;
    let el = hit;
    for (let i = 0; i < 6 && el.parentElement && el.parentElement !== document.body; i++) {
      const r = el.getBoundingClientRect();
      if (r.height > 80 && r.width > 200) break;
      el = el.parentElement;
    }
    el.style.setProperty('display', 'none', 'important');
    const veil = el.previousElementSibling;
    if (veil && veil.getBoundingClientRect && veil.getBoundingClientRect().height > 200) {
      veil.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, dpr, colorScheme = 'light' } = {}) {
  const browser = await chromium.launch({ headless: true });
  const scale = dpr ?? (mobile ? 2 : 1);
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: scale, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme }
    : { viewport: { width, height }, deviceScaleFactor: scale, userAgent: UA, locale: 'en-US', colorScheme, reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 6, step = 1200 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /verify you are human|checking your browser|performing security verification|attention required/i.test(s.body)
      || /cf-challenge|challenge-platform/i.test(s.body);
    if (!challenging && (s.body.length > 40 || /missive/i.test(s.title))) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

export async function open(page, url, { wait = 1800 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  const ok = await clearChallenge(page);
  if (!ok) {
    const title = await page.title().catch(() => '');
    throw new Error(`Cloudflare or challenge blocked ${url} (title: ${title}). Stop this launch.`);
  }
  for (let i = 0; i < 12; i++) {
    const ready = await page.evaluate(() => (document.body?.innerText || '').length > 40).catch(() => false);
    if (ready) break;
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(wait);
  await hideConsent(page);
  await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {});
  return resp;
}
