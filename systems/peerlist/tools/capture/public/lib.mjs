// Peerlist public capture helpers. PRODUCT (adapt): peerlist.io.
// Headed Chromium: a fresh headless hit often stops on Cloudflare "Just a moment...".
// Never type into email, password, phone, username, or newsletter fields.
// Never submit a form. Never click Continue with Google.
import fs from 'node:fs';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://peerlist.io';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const RAW = path.join(REF, 'raw');

export async function launchBrowser() {
  return chromium.launch({
    headless: false,
    args: ['--disable-blink-features=AutomationControlled'],
  });
}

export async function newContext(browser, { mobile = false } = {}) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return context;
}

export async function settle(page, ms = 12000) {
  const start = Date.now();
  while (Date.now() - start < ms) {
    const title = await page.title().catch(() => '');
    if (title && !/just a moment/i.test(title)) return true;
    await page.waitForTimeout(800);
  }
  return false;
}

export async function open(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  const ok = await settle(page);
  await page.waitForTimeout(900);
  return { status: resp ? resp.status() : 0, ok, url: page.url(), title: await page.title() };
}

export function isWall(url) {
  try {
    const path = new URL(url).pathname;
    return /^\/(login|signup|forgot-password)(\/|$)/.test(path);
  } catch {
    return false;
  }
}

export async function dismissAuthDialog(page) {
  const dialog = page.locator('[role="dialog"]').filter({ hasText: /Log in|Create Profile|Continue with Google/ }).first();
  if (await dialog.count() && await dialog.isVisible().catch(() => false)) {
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(300);
    return true;
  }
  return false;
}
