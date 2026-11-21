// Read custom properties from ia.net/writer's public stylesheet and resolve
// them on the live light page. Writes raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// ia.net serves one sheet, /assets/css/main.css. The marketing pages paint
// one light theme. There is no theme switch and no dark attribute.

const ADAPTED_FOR = 'ia-writer';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE } from './public/lib.mjs';

const OUT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', 'raw');

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' });
const page = await ctx.newPage();
let css = '';
page.on('response', async (r) => {
  if (/\.css($|\?)/.test(r.url()) && r.url().includes('ia.net')) {
    try { css += '\n' + await r.text(); } catch { /* ignore */ }
  }
});
await page.goto(BASE + '/writer', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(2500);

const declared = {};
for (const m of css.matchAll(/(--[\w-]+)\s*:\s*([^;}]+);/g)) declared[m[1]] = m[2].trim();
const names = Object.keys(declared).sort();

const probe = await page.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/g, 'url(…)') : v);
  const cs = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  const resolved = {};
  for (const n of names) resolved[n] = noUrl(cs.getPropertyValue(n).trim());
  const theme = document.querySelector('meta[name="theme-color"]')?.content || null;
  const mask = document.querySelector('link[rel="mask-icon"]');
  return {
    attrs: {
      colorScheme: cs.colorScheme,
      htmlClass: document.documentElement.className,
      dataTheme: document.documentElement.getAttribute('data-theme'),
    },
    brand: {
      themeColor: theme,
      maskIconColor: mask?.getAttribute('color') || null,
      bodyBackground: body.backgroundColor,
      bodyColor: body.color,
      bodyFont: body.fontFamily,
    },
    resolved,
  };
}, names);

const faces = [...css.matchAll(/@font-face\s*\{[^}]*font-family:\s*([^;}]+)[^}]*\}/g)].map((m) => m[1].trim()).slice(0, 20);

fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, 'css-vars.json'), JSON.stringify({
  source: 'https://ia.net/assets/css/main.css',
  declaredCount: names.length,
  fontFaces: faces,
  ...probe,
  resolved: { light: probe.resolved },
}, null, 2) + '\n');
console.log('declared', names.length, 'font-faces', faces.length);
await browser.close();
