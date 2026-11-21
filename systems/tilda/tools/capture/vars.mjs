// Reads custom properties and @font-face rules from tilda.cc stylesheets.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// Tilda's public pages are Tilda block pages. Most colour and type is inline
// on elements, not a --* token layer. This file records whatever --* names
// the stylesheets declare, plus font-face rules. Cross-origin sheets are
// fetched and re-parsed.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);

const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try {
    return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') };
  } catch {
    return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true };
  }
}));

for (const s of sheets) {
  if (!s.unreadable || !/^https?:/.test(s.name)) continue;
  try {
    const res = await fetch(s.name);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    s.css = await res.text();
    s.fetched = true;
    delete s.unreadable;
    console.log('fetched', s.name.slice(0, 100), s.css.length);
  } catch (e) {
    console.log('unreadable', s.name.slice(0, 100), e.message);
  }
}

const parsed = await page.evaluate((sheets) => {
  const fonts = [];
  const props = [];
  const errors = [];
  for (const s of sheets) {
    if (!s.css) continue;
    let sheet;
    try {
      sheet = new CSSStyleSheet();
      sheet.replaceSync(s.css);
    } catch (e) {
      errors.push(s.name + ': ' + e.message);
      continue;
    }
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file: s.name };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim().slice(0, 180);
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const cond = r.conditionText || r.name || '';
          walk(r.cssRules, ctx.concat(r.constructor.name + (cond ? ' ' + cond : '')));
          continue;
        }
        if (!r.style) continue;
        const names = [];
        for (let i = 0; i < r.style.length; i++) {
          const p = r.style[i];
          if (p.startsWith('--')) names.push([p, r.style.getPropertyValue(p).trim().slice(0, 200)]);
        }
        if (names.length) props.push({ file: s.name, selector: r.selectorText || '', context: ctx, properties: Object.fromEntries(names) });
      }
    };
    walk(sheet.cssRules, s.media ? ['@media ' + s.media] : []);
  }
  return { fonts, props, errors };
}, sheets);

await browser.close();

const names = new Set();
for (const r of parsed.props) for (const k of Object.keys(r.properties)) names.add(k);

const out = {
  read: '2026-11-21',
  url: BASE + '/',
  sheetCount: sheets.length,
  customPropertyCount: names.size,
  customProperties: [...names].sort(),
  fonts: parsed.fonts.map((f) => ({
    family: f['font-family'],
    weight: f['font-weight'],
    style: f['font-style'],
    display: f['font-display'],
    file: (f.file || '').split('?')[0].slice(0, 120),
  })),
  rules: parsed.props.slice(0, 400),
  errors: parsed.errors.slice(0, 20),
  resolved: { light: {}, dark: {} },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('vars', names.size, 'fonts', parsed.fonts.length, 'rules', parsed.props.length);
