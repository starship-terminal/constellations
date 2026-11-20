// Harvest Mangomint stylesheets into raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site is CSS modules. Most painted colour is a literal in those
// modules, not a custom property. The app host and the booking host declare
// their own --* layers. This script keeps every --* declaration, @font-face
// rules, and a count of hex literals in same-origin CSS.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, APP, BOOK, hidePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const browser = await chromium.launch({ headless: true });
const bodies = new Map();
const pages = [BASE + '/', BASE + '/pricing/', APP + '/login', BOOK];
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
page.on('response', async (r) => {
  const t = r.request().resourceType();
  if (t !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 }).catch((e) => console.log('skip', url, e.message.split('\n')[0]));
  await page.waitForTimeout(1600);
  await hidePromo(page);
}
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const fontsLoaded = await page.evaluate(() => [...document.fonts].map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status })));
await ctx.close();

const sheets = [...bodies.entries()].concat(inline);
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const probe = await probeCtx.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const colours = {};
  const colourRe = /#[0-9a-fA-F]{3,8}\b/g;
  const style = document.createElement('style');
  document.head.appendChild(style);
  const sheet = style.sheet;
  for (const [file, css] of sheets) {
    const text = String(css).slice(0, 2_000_000);
    for (const m of text.matchAll(colourRe)) {
      const h = m[0].toLowerCase();
      if (h.length === 4 || h.length === 7 || h.length === 9) colours[h] = (colours[h] || 0) + 1;
    }
    try {
      sheet.insertRule(`@media all { ${text.includes('{') ? '' : ''} }`, 0);
    } catch { /* parse via CSSStyleSheet below */ }
    const blob = new CSSStyleSheet();
    try { blob.replaceSync(text); } catch { continue; }
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file: String(file).slice(0, 80) };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : (r.cssText || '').split('{')[0].trim().slice(0, 80);
          walk(r.cssRules, [...ctx, head]);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) rules.push({ file: String(file).slice(0, 90), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(-2), properties: props });
      }
    };
    walk(blob.cssRules, []);
  }
  return { rules, fonts, colours };
}, sheets);

const ranked = Object.entries(result.colours).sort((a, b) => b[1] - a[1]).slice(0, 60);
const out = {
  product: 'Mangomint',
  captured: new Date().toLocaleDateString('en-CA'),
  pages,
  fontsLoaded,
  rules: result.rules,
  fonts: result.fonts.slice(0, 40),
  colourCounts: Object.fromEntries(ranked),
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('rules', result.rules.length, 'fonts', result.fonts.length, 'colours', ranked.length);
await browser.close();
