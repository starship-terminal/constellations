// Reads every custom property soundtrap.com's stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site is same-origin for its own CSS. OneTrust sheets are vendor.
// One public theme: html has no data-theme. Values resolve at 1440 x 900.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, closePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);
await closePromo(page);

const result = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const skipped = [];
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
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.cssText.split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 160), context: ctx, properties: props });
    }
  };
  [...document.styleSheets].forEach((ss, i) => {
    const file = ss.href ? ss.href.split('/').pop().split('?')[0] || ss.href : `inline-${i}`;
    try { walk(ss.cssRules, [], file); } catch { skipped.push(file); }
  });
  const rootVars = {};
  const cs = getComputedStyle(document.documentElement);
  for (const r of rules) for (const name of Object.keys(r.properties)) {
    if (rootVars[name]) continue;
    const raw = cs.getPropertyValue(name).trim();
    if (raw) rootVars[name] = noUrl(raw).slice(0, 300);
  }
  return {
    rules, fonts, skipped, rootVars,
    theme: {
      className: document.documentElement.className,
      dataTheme: document.documentElement.getAttribute('data-theme'),
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
    },
    fontFacesComputed: [...document.fonts].slice(0, 40).map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status })),
  };
});
await browser.close();

const VENDOR = /^--(ot|onetrust|cky)-/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => VENDOR.test(n)) || /onetrust/i.test(r.file)) return 'vendor';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'live CSSOM on www.soundtrap.com/musicmakers, signed out, 1440x900, one public theme',
  themeProbe: result.theme,
  sheetsSkippedCrossOrigin: result.skipped,
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { app: names('app').length, vendor: names('vendor').length, tailwind: names('tailwind').length },
  },
  app: result.rules.filter((r) => r.bin === 'app'),
  vendor: result.rules.filter((r) => r.bin === 'vendor').slice(0, 40),
  fonts: result.fonts,
  fontFacesComputed: result.fontFacesComputed,
  rootVars: result.rootVars,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${result.rules.length} rules, ${result.fonts.length} faces; app ${out.counts.names.app} vendor ${out.counts.names.vendor}; rootVars ${Object.keys(result.rootVars).length}; skipped ${result.skipped.length}`);
console.log('theme', JSON.stringify(result.theme));
console.log('fonts', JSON.stringify(result.fontFacesComputed.slice(0, 12)));
console.log('root sample', Object.keys(result.rootVars).slice(0, 30).join(', '));
