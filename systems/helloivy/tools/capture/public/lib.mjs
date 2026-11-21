// Shared helpers for the Hello Ivy public capture.
// PRODUCT (adapt): BASE is www.helloivy.co. Consent SDK hosts are aborted.
// Nothing is submitted. Login, signup, Google, and mailto are never clicked.
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
export const BASE = 'https://www.helloivy.co';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing', 'textAlign',
  'color', 'backgroundColor', 'backgroundImage',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRadius',
  'boxShadow', 'opacity', 'textDecoration', 'textTransform',
];

export async function patch(ctx) {
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  await ctx.route('**/*', (route) => {
    const u = route.request().url();
    if (/cookiebot|onetrust|cookielaw|cdn\.cookielaw|consent\.cookiebot|iubenda|cookieyes|trustarc|osano|privacy-mgmt/i.test(u)) {
      return route.abort();
    }
    return route.continue();
  });
}

export async function hideOverlays(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('[id*="cookie" i], [class*="cookie" i], [id*="consent" i], [class*="consent" i]')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

// The header menu icon is a Framer div named Menu, not a button.
export async function openMenu(page) {
  const box = await page.evaluate(() => {
    const el = document.querySelector('[data-framer-name="Menu"]');
    if (!el) return null;
    const r = el.getBoundingClientRect();
    // The icon lines sit in the lower half of the cell.
    return { x: r.x + r.width * 0.5, y: r.y + r.height * 0.62 };
  });
  if (!box) return false;
  await page.mouse.click(box.x, box.y);
  await page.waitForTimeout(700);
  return true;
}

export async function closeMenu(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(300);
  const still = await page.evaluate(() => /01\s*HOME/.test(document.body.innerText) && getComputedStyle(document.documentElement).overflow === 'hidden');
  if (still) {
    await page.mouse.click(page.viewportSize().width - 48, 48);
    await page.waitForTimeout(400);
  }
}

export function quantizePng(src, dest) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(src)}).convert('RGBA')
q = im.convert('P', palette=Image.ADAPTIVE, colors=256)
q.convert('RGBA').save(${JSON.stringify(dest)}, optimize=True)
`], { stdio: 'inherit' });
}
