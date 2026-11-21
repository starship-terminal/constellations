// Shared helpers for the Zellerfeld captures (adapted from the public kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.zellerfeld.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// Hide the cookie banner. Never click Accept or Decline (those POST consent).
export async function hideCookies(page) {
  await page.evaluate(() => {
    document.querySelectorAll('[data-cookie-banner]').forEach((n) => n.remove());
    // Overlay scrollbars paint an orange stripe into the viewport shot on
    // mobile. Hide them; the page still scrolls for full-page tiles.
    const id = 'zf-capture-scrollbar';
    if (!document.getElementById(id)) {
      const s = document.createElement('style');
      s.id = id;
      s.textContent = 'html{scrollbar-width:none}::-webkit-scrollbar{width:0;height:0}';
      document.documentElement.appendChild(s);
    }
  }).catch(() => {});
}

// Close the Perfect Fit Guarantee notice. Close does not submit a form.
export async function dismissNotice(page) {
  const dlg = page.locator('[role="dialog"]').filter({ hasText: 'Perfect Fit Guarantee' }).first();
  if (!(await dlg.count())) return false;
  const close = dlg.getByRole('button', { name: 'Close' }).first();
  if (await close.count()) await close.click({ timeout: 4000 }).catch(() => {});
  else await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  return true;
}

export async function launchBrowser() {
  return chromium.launch({
    channel: 'chrome',
    headless: false,
    args: ['--disable-blink-features=AutomationControlled'],
  });
}
