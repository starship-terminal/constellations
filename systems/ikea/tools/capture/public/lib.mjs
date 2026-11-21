// IKEA Singapore public capture helpers. PRODUCT (adapt): BASE, locale, cookie hide.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.ikea.com';

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const PKG = path.resolve(HERE, '..', '..', '..');

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch({
    headless: true,
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-SG' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-SG' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  // Cookie and survey hosts. Blocking the request keeps the banner from mounting.
  // Never click Accept, Reject, or Cookie settings.
  await context.route('**/*onetrust*', (route) => route.abort());
  await context.route('**/*cookielaw*', (route) => route.abort());
  await context.route('**/*cookieconsent*', (route) => route.abort());
  await context.route('**/*qualtrics*', (route) => route.abort());
  await context.route('**/*medallia*', (route) => route.abort());
  await context.route('**/*kampyle*', (route) => route.abort());
  await context.route('**/*ketchcdn*', (route) => route.abort());
  await context.route('**/feedback.ikea.com/**', (route) => route.abort());
  return { browser, context };
}

// Hide the cookie sheet. Never click Accept, Reject, or Cookie settings (those POST a preference).
export async function hideConsent(page) {
  await page.addStyleTag({
    content: `
      #onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk,
      .onetrust-pc-dark-filter, .ot-sdk-container, #ot-sdk-btn-floating,
      [id^="onetrust"], [class*="onetrust"], [class*="ot-sdk"],
      [class*="cookie-banner"], [id*="cookie-banner"],
      [class*="feedback"], [id*="feedback"], [class*="survey"],
      iframe[title*="feedback" i], iframe[src*="qualtrics"], iframe[src*="medallia"] {
        display: none !important; visibility: hidden !important;
        pointer-events: none !important; opacity: 0 !important;
      }
    `,
  }).catch(() => {});
  // The Singapore cookie card is a custom element with a shadow root
  // (section.banner.panel). Hide the host. Do not click its buttons.
  await page.evaluate(() => {
    const hideHost = (el) => {
      el.style.setProperty('display', 'none', 'important');
      el.style.setProperty('visibility', 'hidden', 'important');
      const host = el.getRootNode && el.getRootNode().host;
      if (host && host.style) {
        host.style.setProperty('display', 'none', 'important');
        host.style.setProperty('visibility', 'hidden', 'important');
      }
    };
    const visit = (root) => {
      root.querySelectorAll('section.banner, .banner.panel, ccm-button').forEach(hideHost);
      root.querySelectorAll('*').forEach((el) => { if (el.shadowRoot) visit(el.shadowRoot); });
    };
    visit(document);
  }).catch(() => {});
  await page.evaluate(() => {
    const kill = (sel) => document.querySelectorAll(sel).forEach((n) => n.remove());
    kill('#onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk, .onetrust-pc-dark-filter');
    kill('[class*="onetrust"], [id^="onetrust"]');
    // Store name in the header is a preference, not a design token. Mask the label only.
    document.querySelectorAll('button, a').forEach((el) => {
      const label = el.getAttribute('aria-label') || '';
      if (/store/i.test(label) && el.querySelector('span, div')) {
        el.querySelectorAll('span').forEach((s) => {
          if (s.textContent && s.textContent.trim() && !/select store/i.test(s.textContent)) s.textContent = 'Store';
        });
      }
    });
  }).catch(() => {});
}

export function isLoginWall(url) {
  return /\/profile\/(login|signup|register)/.test(url) || /\/profile\/?$/.test(new URL(url).pathname);
}

export async function openPublic(page, url, { wait = 2500 } = {}) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  await page.waitForTimeout(wait);
  await hideConsent(page);
  return { status: resp && resp.status(), url: page.url() };
}
