// Collect inline SVGs from Loom public pages into icons/.
import crypto from 'crypto';
import fs from 'fs';
import { chromium, UA, BASE, hideConsent } from './public/lib.mjs';
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
    if (s.closest('#onetrust-consent-sdk, #onetrust-banner-sdk')) return false;
    const r = s.getBoundingClientRect();
    return r.width >= 10 && r.width <= 64 && r.height >= 10 && r.height <= 64 && getComputedStyle(s).visibility !== 'hidden';
  }).slice(0, 30).map((s) => {
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

const pages = [BASE + '/', BASE + '/pricing', BASE + '/login', BASE + '/share/136d5353b9fd4b82b0f4410c24200fec'];
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const index = ['file\tlabel\tpx\tpage'];
const seen = new Set();
const files = new Map();
const failed = [];
for (const url of pages) {
  try {
    // goto resolves on a 404 or 503 page: an error status counts as a failed page too.
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    if (!res || !res.ok()) throw new Error('HTTP ' + (res ? res.status() : 'no response'));
  } catch (e) {
    failed.push(new URL(url).pathname);
    console.error('page failed', url, String(e.message).slice(0, 120));
    continue;
  }
  await page.waitForTimeout(1800);
  await hideConsent(page);
  if (url.endsWith('/')) {
    await page.locator('header button, nav button').filter({ hasText: /^Apps$/ }).first().hover().catch(() => {});
    await page.waitForTimeout(400);
  }
  const icons = await page.evaluate(collect);
  for (const icon of icons) {
    const hash = crypto.createHash('sha1').update(icon.markup).digest('hex').slice(0, 8);
    const slug = (icon.label || 'icon').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 28) || 'icon';
    const name = `${slug}-${hash}.svg`;
    if (seen.has(name)) continue;
    seen.add(name);
    files.set(name, icon.markup);
    index.push(`${name}\t${icon.label}\t${icon.w}\t${new URL(url).pathname}`);
  }
  console.log(url, icons.length);
}
await browser.close();
// The old set is replaced only after a complete collection (the kit's guard), so a run
// that loses a page cannot leave icons/ emptied or out of step with INDEX.tsv.
if (failed.length || !seen.size) {
  console.error(`not replacing icons/: ${failed.length ? 'failed pages: ' + failed.join(', ') : 'no icons collected'}`);
  process.exit(1);
}
// Written to a scratch folder first; icons/ changes only once every file is written.
replaceSet(OUT, files, index.join('\n') + '\n');
console.log('icons', seen.size);
