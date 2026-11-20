// Probe a list of krea routes: status, final URL, title, gate signals. No clicks.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const routes = (process.argv[2] || '').split(',').filter(Boolean);
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US',
});
// navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
const page = await context.newPage();
const out = [];
for (const route of routes) {
  const url = route.startsWith('http') ? route : 'https://www.krea.ai' + route;
  const row = { route };
  try {
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 40000 });
    await page.waitForTimeout(2500);
    row.status = res?.status() ?? null;
    row.final = page.url();
    const info = await page.evaluate(() => {
      const t = (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 280);
      const html = document.documentElement;
      return {
        title: document.title,
        htmlClass: html.className,
        h1: [...document.querySelectorAll('h1,h2')].slice(0, 4).map((h) => h.innerText.trim().slice(0, 80)),
        text: t,
        loginish: /sign in|log in|create account|continue with/i.test(t.slice(0, 400)),
      };
    });
    Object.assign(row, info);
  } catch (e) {
    row.error = String(e).split('\n')[0];
  }
  out.push(row);
  console.log([row.status, row.final, row.title, (row.h1 || []).join(' | '), (row.text || row.error || '').slice(0, 140)].join(' :: '));
}
const dest = path.join(os.homedir(), '.design-systems', 'krea', 'routes.json');
fs.writeFileSync(dest, JSON.stringify(out, null, 1));
await browser.close();
