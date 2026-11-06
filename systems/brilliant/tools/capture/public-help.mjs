// The public Help Center search, the one free-text search with live results the product shows
// without an account: default, a query with results, and a query with none. Headless, signed out.
//   PLAYWRIGHT=/path/to/playwright/index.mjs OUT=<dir> node tools/capture/public-help.mjs
// Writes full-colour PNGs to OUT (quantize.py turns them into screenshots/app-2026-10/) and prints
// the computed styles of the search field and a result row.
import fs from 'fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = process.env.OUT;
if (!OUT) { console.error('set OUT to a scratch directory outside the repository'); process.exit(2); }
fs.mkdirSync(OUT, { recursive: true });
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const p = await ctx.newPage();
await p.goto('https://brilliant.org/help/', { waitUntil: 'load' });
await p.waitForTimeout(2500);
await p.evaluate(() => document.getElementById('onetrust-consent-sdk')?.remove());
await p.screenshot({ path: `${OUT}/help-light-search-default.png` });
const inp = p.locator('input[type=search]');
const read = () => p.evaluate(() => { const i = document.querySelector('input[type=search]'); const cs = getComputedStyle(i); return { height: cs.height, border: cs.border, radius: cs.borderRadius, bg: cs.backgroundColor, padding: cs.padding, font: cs.font, outline: cs.outline, boxShadow: cs.boxShadow }; });
const rest = await read();
await inp.click(); await inp.fill('slope'); await p.waitForTimeout(2500);
const focused = await read();
await p.screenshot({ path: `${OUT}/help-light-search-results.png` });
await inp.fill('qqzxv'); await p.waitForTimeout(2500);
await p.screenshot({ path: `${OUT}/help-light-search-empty.png` });
const empty = await p.evaluate(() => (document.querySelector('main') || document.body).innerText.slice(0, 300));
console.log(JSON.stringify({ rest, focused, empty }, null, 1));
await b.close();
