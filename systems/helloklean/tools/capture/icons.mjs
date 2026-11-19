// Collects inline SVG icons from Hello Klean's public pages.
//   PLAYWRIGHT=... node icons.mjs
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { chromium, UA, BASE, REF, clearChallenge, closePromo, patch } from './public/lib.mjs';

const DIR = path.join(REF, 'icons');
fs.mkdirSync(DIR, { recursive: true });

const PAGES = ['/en-int', '/en-int/collections/filters', '/en-int/products/hello-klean-skin-filter', '/en-int/pages/faqs'];

function clean(svg) {
  return svg
    .replace(/\s(?:href|xlink:href)="[^"]*"/g, '')
    .replace(/\s(?:data-[a-z-]+)="[^"]*"/g, '')
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-GB' });
await patch(ctx);
const page = await ctx.newPage();
const seen = new Map();
for (const urlPath of PAGES) {
  await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (!(await clearChallenge(page))) continue;
  await page.waitForTimeout(2500);
  await closePromo(page);
  const icons = await page.evaluate(() => {
    return [...document.querySelectorAll('header svg, nav svg, footer svg, button svg, a svg')].slice(0, 80).map((svg) => {
      const host = svg.closest('button, a') || svg.parentElement;
      const label = (host && (host.getAttribute('aria-label') || host.innerText) || '').trim().replace(/\s+/g, ' ').slice(0, 40);
      const r = svg.getBoundingClientRect();
      return { label, w: Math.round(r.width), h: Math.round(r.height), html: svg.outerHTML.slice(0, 4000) };
    }).filter((i) => i.w > 8 && i.w < 80 && i.h > 8 && i.h < 80);
  });
  for (const icon of icons) {
    const html = clean(icon.html);
    const hash = crypto.createHash('sha1').update(html).digest('hex').slice(0, 10);
    if (!seen.has(hash)) seen.set(hash, { ...icon, html, hash, pages: [urlPath] });
    else seen.get(hash).pages.push(urlPath);
  }
  console.log(urlPath, icons.length);
}
const rows = ['file\trole\tlabel\tsize\tpages'];
let i = 0;
for (const icon of seen.values()) {
  i++;
  const role = (icon.label || 'icon').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || 'icon';
  const file = `${String(i).padStart(2, '0')}-${role}.svg`;
  fs.writeFileSync(path.join(DIR, file), icon.html + '\n');
  rows.push(`${file}\t${role}\t${icon.label.replace(/\t/g, ' ')}\t${icon.w}x${icon.h}\t${[...new Set(icon.pages)].join(',')}`);
}
fs.writeFileSync(path.join(DIR, 'INDEX.tsv'), rows.join('\n') + '\n');
console.log('wrote', i, 'icons');
await browser.close();
