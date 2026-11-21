// Read every custom property getfernand.com declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site paints one light theme. Brand colours are --black, --blue,
// --grey* and status hues on :root. WordPress theme.json also injects
// --wp--preset--* names; those are binned separately and are not the product palette.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);

const harvested = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : (r.cssText || '').split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
    }
  };
  for (const s of [...document.styleSheets]) {
    let ruleset;
    try { ruleset = s.cssRules; } catch (e) { errors.push({ file: s.href || 'inline', error: String(e) }); continue; }
    walk(ruleset, [], s.href || 'inline');
  }
  const root = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))];
  const resolved = {};
  for (const n of names) resolved[n] = root.getPropertyValue(n).trim();
  const theme = {
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
    bodyBg: body.backgroundColor,
    bodyColor: body.color,
    bodyFont: body.fontFamily,
    h1: (() => {
      const h = document.querySelector('h1');
      if (!h) return null;
      const c = getComputedStyle(h);
      return { fontFamily: c.fontFamily, fontSize: c.fontSize, fontWeight: c.fontWeight, lineHeight: c.lineHeight, color: c.color, letterSpacing: c.letterSpacing };
    })(),
  };
  return { rules, fonts, errors, resolved, theme };
});

function bin(name) {
  if (name.startsWith('--wp--')) return 'wordpress';
  if (name.startsWith('--')) return 'app';
  return 'other';
}
const bins = { app: [], wordpress: [] };
for (const r of harvested.rules) {
  const grouped = {};
  for (const [k, v] of Object.entries(r.properties)) {
    const b = bin(k);
    (grouped[b] ||= {})[k] = v;
  }
  for (const [b, properties] of Object.entries(grouped)) bins[b].push({ ...r, properties });
}

const out = {
  source: BASE + '/',
  capturedAt: new Date().toISOString(),
  theme: harvested.theme,
  resolved: { light: Object.fromEntries(Object.entries(harvested.resolved).filter(([k]) => !k.startsWith('--wp--')).map(([k, v]) => [k, { value: v }])) },
  app: bins.app,
  wordpress: bins.wordpress.map((r) => ({ selector: r.selector, names: Object.keys(r.properties) })),
  fonts: harvested.fonts.map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
  errors: harvested.errors,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('vars', Object.keys(harvested.resolved).length, 'fonts', harvested.fonts.length, 'errors', harvested.errors.length);
await browser.close();
