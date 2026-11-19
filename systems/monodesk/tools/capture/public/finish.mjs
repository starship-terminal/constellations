// Icons, header bar, secondary CTA fill, motion sample, favicon.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const ICONS = path.join(PKG, 'icons');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(ICONS, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});
const page = await context.newPage();

await page.goto('https://www.monodesk.com/', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1200);

const header = await page.evaluateHandle(() => {
  const all = [...document.querySelectorAll('header, header *')];
  let best = null;
  for (const el of all) {
    const r = el.getBoundingClientRect();
    const bg = getComputedStyle(el).backgroundColor;
    if (r.width > 1000 && r.height > 48 && r.height < 100 && bg.startsWith('rgb') && bg !== 'rgba(0, 0, 0, 0)') {
      if (!best || r.height < best.getBoundingClientRect().height) best = el;
    }
  }
  return best;
});
const hel = header.asElement();
if (hel) {
  const s = await hel.evaluate((n) => {
    const cs = getComputedStyle(n);
    const r = n.getBoundingClientRect();
    return { bg: cs.backgroundColor, radius: cs.borderRadius, h: Math.round(r.height), w: Math.round(r.width), shadow: cs.boxShadow, pad: cs.padding };
  });
  console.log('header', s);
  const b = await hel.boundingBox();
  await page.screenshot({ path: path.join(CROPS, 'site-header-bar.png'), clip: { x: Math.max(0, b.x - 8), y: Math.max(0, b.y - 8), width: b.width + 16, height: b.height + 16 } });
  fs.writeFileSync(path.join(RAW, 'header.json'), JSON.stringify(s, null, 2));
}

const ghost = await page.evaluateHandle(() => {
  const links = [...document.querySelectorAll('a')].filter((a) => /^Log in/.test((a.innerText || '').trim()));
  for (const a of links) {
    const r = a.getBoundingClientRect();
    if (r.width < 80 || r.height < 28 || r.top > 700) continue;
    const nodes = [a, ...a.querySelectorAll('*')];
    for (const n of nodes) {
      const bg = getComputedStyle(n).backgroundColor;
      const b = n.getBoundingClientRect();
      if (bg !== 'rgba(0, 0, 0, 0)' && b.width > 60 && b.height > 24) return n;
    }
  }
  return null;
});
const gel = ghost.asElement();
if (gel) {
  const s = await gel.evaluate((n) => {
    const cs = getComputedStyle(n);
    return { bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, pad: cs.padding, fs: cs.fontSize };
  });
  console.log('ghost', s);
  await gel.hover();
  await page.waitForTimeout(250);
  const s2 = await gel.evaluate((n) => {
    const cs = getComputedStyle(n);
    return { bg: cs.backgroundColor, color: cs.color };
  });
  console.log('ghost hover', s2);
  const b = await gel.boundingBox();
  await page.screenshot({ path: path.join(CROPS, 'cta-secondary-hover.png'), clip: { x: b.x - 8, y: b.y - 8, width: b.width + 16, height: b.height + 16 } });
  fs.writeFileSync(path.join(RAW, 'ghost.json'), JSON.stringify({ rest: s, hover: s2 }, null, 2));
}

// inline SVGs
const svgs = await page.evaluate(() => {
  const seen = new Map();
  for (const svg of document.querySelectorAll('svg')) {
    const r = svg.getBoundingClientRect();
    if (r.width < 8 || r.width > 80 || r.height < 8) continue;
    const html = svg.outerHTML;
    if (html.length > 8000 || html.length < 40) continue;
    const label = (svg.getAttribute('aria-label') || svg.closest('a,button')?.innerText || svg.closest('a')?.getAttribute('href') || 'icon').trim().slice(0, 40);
    const key = html.replace(/\s+/g, ' ');
    if (!seen.has(key)) seen.set(key, { label, html, w: Math.round(r.width), h: Math.round(r.height) });
    if (seen.size > 40) break;
  }
  return [...seen.values()];
});
console.log('svgs', svgs.length);
const index = ['role\tfile\tseen'];
svgs.forEach((s, i) => {
  const slug = (s.label || 'icon').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || 'icon';
  const file = `${String(i + 1).padStart(2, '0')}-${slug}.svg`;
  fs.writeFileSync(path.join(ICONS, file), s.html.includes('xmlns') ? s.html : s.html.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"'));
  index.push(`${s.label.replace(/\t/g, ' ')}\t${file}\thome`);
});
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), index.join('\n') + '\n');

// favicon
const iconHref = await page.evaluate(() => {
  const links = [...document.querySelectorAll('link[rel*="icon"]')].map((l) => l.href);
  return links;
});
console.log('icons', iconHref);
fs.writeFileSync(path.join(RAW, 'icon-links.json'), JSON.stringify(iconHref, null, 2));

// motion sample: transitions on home
const motion = await page.evaluate(() => {
  const hits = [];
  const nodes = [...document.querySelectorAll('a, button, header, header *')].slice(0, 400);
  for (const el of nodes) {
    const cs = getComputedStyle(el);
    const tp = cs.transitionProperty;
    const td = cs.transitionDuration;
    if (tp && tp !== 'all' && tp !== 'none' && td && td !== '0s') {
      hits.push({ tag: el.tagName, text: (el.innerText || '').trim().slice(0, 24), tp, td, tf: cs.transitionTimingFunction, delay: cs.transitionDelay });
    } else if (td && td !== '0s' && tp === 'all') {
      hits.push({ tag: el.tagName, text: (el.innerText || '').trim().slice(0, 24), tp, td, tf: cs.transitionTimingFunction });
    }
    if (hits.length > 25) break;
  }
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  return { reduced, hits: hits.slice(0, 20), sheets: [...document.styleSheets].map((s) => s.href).filter(Boolean) };
});
fs.writeFileSync(path.join(RAW, 'motion-sample.json'), JSON.stringify(motion, null, 2));
console.log('motion hits', motion.hits.length, motion.hits.slice(0, 4));

await browser.close();
console.log('done');
