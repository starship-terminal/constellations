// Collect inline SVGs from Limitless public pages into icons/.
import crypto from 'crypto';
import fs from 'fs';
import { chromium, UA, BASE, APP, HELP, hideConsent } from './public/lib.mjs';
import { replaceSet } from './replace-set.mjs';

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
    if (s.closest('#enzuzo-modal, .ez-consent, #ez-cookie-notification')) return false;
    const r = s.getBoundingClientRect();
    return r.width >= 8 && r.width <= 80 && r.height >= 8 && r.height <= 80 && getComputedStyle(s).visibility !== 'hidden';
  }).slice(0, 40).map((s) => {
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

const pages = [BASE + '/', BASE + '/developers', BASE + '/for/voice-recorder', APP + '/signin', HELP + '/en/'];
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const seen = new Map();
const failed = [];
for (const url of pages) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch((e) => { failed.push(`${url}: ${String(e.message).split('\n')[0]}`); return null; });
  if (!res || res.status() >= 400) { if (res) failed.push(`${url}: HTTP ${res.status()}`); continue; }
  await page.waitForTimeout(1600);
  await hideConsent(page);
  const icons = await page.evaluate(collect);
  for (const ic of icons) {
    const hash = crypto.createHash('sha1').update(ic.markup).digest('hex').slice(0, 8);
    const rec = seen.get(hash) || { markup: ic.markup, label: ic.label, w: ic.w, pages: [] };
    if (!rec.pages.includes(url)) rec.pages.push(url);
    if (rec.label === 'icon' && ic.label !== 'icon') rec.label = ic.label;
    seen.set(hash, rec);
  }
  console.log(url, icons.length);
}
await browser.close();
// Replace icons/ only after a complete run: a page that failed to load leaves
// the committed icons and INDEX.tsv as they were.
if (failed.length) {
  console.error('not written, pages failed:\n  ' + failed.join('\n  '));
  process.exit(1);
}
const rows = ['file\trole\tpages'];
const files = new Map();
let i = 0;
for (const [hash, rec] of seen) {
  const slug = (rec.label || 'icon').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || 'icon';
  const name = `${slug}-${hash}.svg`;
  files.set(name, rec.markup);
  rows.push(`${name}\t${rec.label}\t${rec.pages.length}`);
  i++;
}
// Written to a scratch folder first; icons/ changes only once every file is written.
replaceSet(OUT, files, rows.join('\n') + '\n');
console.log('icons', i);
