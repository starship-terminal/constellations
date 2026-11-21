// Read custom properties and @font-face rules from savvycal.com's live CSS.
// Marketing pages declare almost no custom properties (only --nav-height).
// Brand colours live in Tailwind utilities, so this file records the
// stylesheet harvest and the font faces, not a token layer that is not there.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(here, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const sheets = [];
page.on('response', async (res) => {
  const ct = res.headers()['content-type'] || '';
  const url = res.url();
  if (!/css|font/.test(ct) && !url.includes('.css')) return;
  if (sheets.length > 12) return;
  try {
    const body = await res.text();
    if (body && body.includes('{')) sheets.push({ url: url.split('?')[0].slice(0, 180), bytes: body.length, css: body.slice(0, 400000) });
  } catch { /* cross-origin body unavailable */ }
});
await page.goto(BASE + '/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1500);

const live = await page.evaluate(() => {
  const vars = [];
  const fonts = [];
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = {};
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim().slice(0, 180);
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) { walk(r.cssRules, ctx); continue; }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim();
      }
      if (Object.keys(props).length) vars.push({ selector: r.selectorText, props, ctx });
    }
  };
  for (const s of document.styleSheets) {
    let rules;
    try { rules = s.cssRules; } catch { continue; }
    if (rules) walk(rules, []);
  }
  const root = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  return {
    vars,
    fonts: fonts.slice(0, 40),
    fontCount: fonts.length,
    bodyBg: body.backgroundColor,
    bodyColor: body.color,
    bodyFont: body.fontFamily,
    navHeight: root.getPropertyValue('--nav-height'),
  };
});

const brand = await page.evaluate(() => {
  const want = ['bg-brand-oatmeal', 'bg-brand-sand', 'bg-brand-orange', 'bg-brand-neon-green', 'text-brand-orange', 'text-olive-950'];
  const found = {};
  const all = [...document.querySelectorAll('[class]')];
  for (const name of want) {
    const el = all.find((n) => [...n.classList].some((c) => c === name || c.endsWith(name) || c.includes(name)));
    if (!el) { found[name] = null; continue; }
    const cs = getComputedStyle(el);
    found[name] = { bg: cs.backgroundColor, color: cs.color, tag: el.tagName };
  }
  // Probe Tailwind classes by reading a painted element that uses them.
  const probes = {};
  for (const el of all) {
    for (const c of el.classList) {
      if (/^bg-brand-/.test(c) || /^text-brand-/.test(c) || /^text-olive-/.test(c) || /^bg-olive-/.test(c) || /^ring-brand-/.test(c)) {
        if (probes[c]) continue;
        const cs = getComputedStyle(el);
        probes[c] = { bg: cs.backgroundColor, color: cs.color };
      }
    }
  }
  return { found, probes };
});

const out = {
  product: 'savvycal',
  captured: '2026-11-21',
  source: 'https://savvycal.com/ live CSSOM plus stylesheet responses',
  note: 'Marketing pages declare --nav-height only. Brand colours are Tailwind utilities, recorded from computed styles of elements that carry those classes. Unread values stay Not captured.',
  resolved: { light: {}, dark: {} },
  customProperties: live.vars,
  fonts: live.fonts,
  fontCount: live.fontCount,
  body: { backgroundColor: live.bodyBg, color: live.bodyColor, fontFamily: live.bodyFont, navHeight: live.navHeight },
  brandClasses: brand,
  stylesheets: sheets.map((s) => ({ url: s.url, bytes: s.bytes })),
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('vars', live.vars.length, 'fonts', live.fontCount, 'probes', Object.keys(brand.probes).length, 'sheets', sheets.length);
await browser.close();
