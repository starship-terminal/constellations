// One-shot homepage map for the public Meta shop. Writes a JSON tree
// outside the repo. Does not click identity providers, submit forms, or
// type credentials.
import fs from 'node:fs';
import { chromium } from './lib.mjs';

const OUT = process.env.MAP_OUT || '/tmp/meta-ai-home-map.json';
const URLS = (process.env.MAP_URLS || 'https://www.meta.com/').split(',');

function abs(href) {
  try { return new URL(href, 'https://www.meta.com/').href; } catch { return href; }
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});
const page = await context.newPage();
const reports = [];

for (const url of URLS) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch((e) => ({ status: () => 0, url: () => url, err: String(e) }));
  await page.waitForTimeout(4000);
  const data = await page.evaluate(() => {
    const textOf = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '').replace(/\s+/g, ' ').trim().slice(0, 140);
    const nav = [...document.querySelectorAll('header a, header button, nav a, nav button, [role="banner"] a, [role="banner"] button')].map((el) => ({
      tag: el.tagName,
      role: el.getAttribute('role'),
      text: textOf(el),
      href: el.href || null,
      aria: el.getAttribute('aria-label'),
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls'),
      haspopup: el.getAttribute('aria-haspopup'),
    }));
    const dialogs = [...document.querySelectorAll('[role="dialog"], dialog, [aria-modal="true"]')].map((el) => ({
      role: el.getAttribute('role') || el.tagName,
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400),
      buttons: [...el.querySelectorAll('button, a')].slice(0, 20).map((b) => ({
        tag: b.tagName,
        text: (b.innerText || b.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        href: b.href || null,
      })),
    }));
    const buttons = [...document.querySelectorAll('button')].slice(0, 40).map((el) => ({
      text: textOf(el),
      aria: el.getAttribute('aria-label'),
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls'),
    }));
    return {
      title: document.title,
      href: location.href,
      htmlClass: document.documentElement.className,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      dialogs,
      headerCount: nav.length,
      nav: nav.slice(0, 80),
      buttons,
    };
  });
  reports.push({
    requested: url,
    status: typeof res.status === 'function' ? res.status() : null,
    finalUrl: page.url(),
    ...data,
  });
  console.log(url, '->', page.url(), data.title, 'nav', data.nav.length, 'dialogs', data.dialogs.length);
}

fs.writeFileSync(OUT, JSON.stringify(reports, null, 2));
await browser.close();
console.log('wrote', OUT);
