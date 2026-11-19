// Collect inline SVGs from Make public pages into icons/.
import crypto from 'crypto';
import fs from 'fs';
import { chromium, UA, BASE, hideConsent } from './public/lib.mjs';

const OUT = new URL('../../icons/', import.meta.url).pathname;
fs.mkdirSync(OUT, { recursive: true });

function collect() {
  const hex = (c) => {
    const m = String(c).match(/rgba?\(([^)]+)\)/);
    if (!m) return c;
    const [r, g, b] = m[1].split(',').map((x) => Math.round(parseFloat(x)));
    return '#' + [r, g, b].map((v) => v.toString(16).padStart(2, '0')).join('');
  };
  const rgb = (c) => {
    const m = String(c).match(/rgba?\(([^)]+)\)/);
    return m ? m[1].split(',').slice(0, 3).map((x) => Math.round(parseFloat(x))).join(',') : c;
  };
  return [...document.querySelectorAll('svg')].filter((s) => {
    if (s.closest('#onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk')) return false;
    const r = s.getBoundingClientRect();
    return r.width >= 8 && r.width <= 64 && r.height >= 8 && r.height <= 64 && getComputedStyle(s).visibility !== 'hidden';
  }).slice(0, 36).map((s) => {
    const col = rgb(getComputedStyle(s).color);
    const c = s.cloneNode(true);
    c.querySelectorAll('path,circle,rect,line,polyline,polygon').forEach((e, i) => {
      const src = s.querySelectorAll('path,circle,rect,line,polyline,polygon')[i];
      if (!src) return;
      const cs = getComputedStyle(src);
      if (cs.fill && cs.fill !== 'none' && !cs.fill.startsWith('url')) e.setAttribute('fill', rgb(cs.fill) === col ? 'currentColor' : hex(cs.fill));
      if (cs.stroke && cs.stroke !== 'none') e.setAttribute('stroke', rgb(cs.stroke) === col ? 'currentColor' : hex(cs.stroke));
    });
    c.removeAttribute('class');
    const label = (s.closest('a,button')?.innerText || s.closest('a,button')?.getAttribute('aria-label') || s.getAttribute('aria-label') || 'icon').trim().replace(/\s+/g, ' ').slice(0, 40);
    return { markup: c.outerHTML, label, w: Math.round(s.getBoundingClientRect().width) };
  });
}

const pages = [BASE + '/', BASE + '/templates', BASE + '/pricing', BASE + '/login'];
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const seen = new Map();
const page = await ctx.newPage();
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 }).catch(() => {});
  await page.waitForTimeout(1500);
  await hideConsent(page);
  const icons = await page.evaluate(collect);
  for (const icon of icons) {
    const hash = crypto.createHash('sha1').update(icon.markup).digest('hex').slice(0, 8);
    const slug = icon.label.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 28) || 'icon';
    const name = `${slug}-${hash}.svg`;
    if (seen.has(hash)) continue;
    seen.set(hash, { name, label: icon.label, w: icon.w, page: url });
    fs.writeFileSync(OUT + name, icon.markup);
  }
  console.log(url, icons.length, 'visible, unique', seen.size);
}
await browser.close();
const rows = ['file\tlabel\tpx\tpage'];
for (const v of seen.values()) rows.push(`${v.name}\t${v.label}\t${v.w}\t${v.page}`);
fs.writeFileSync(OUT + 'INDEX.tsv', rows.join('\n') + '\n');
console.log('wrote', seen.size, 'icons');
