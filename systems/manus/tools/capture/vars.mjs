// Read every custom property Manus's stylesheets declare and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs [dir of .css files]
//
// Manus (manus.im/app, Next.js with Tailwind 3) serves its CSS as hashed chunks from
// files.manuscdn.com, cross-origin to the app, so the page's CSSOM refuses to read them and a
// snapshot keeps them as <link> tags. The chunk list below is what the signed-in app page
// loaded on 2026-10-17 (document.styleSheets; the 2026-10-04 capture's list was different); pass a directory of downloaded copies to read
// those instead of fetching. Each file is parsed by a headless Chromium (constructed
// CSSStyleSheet), and every rule that declares a custom property is kept with its selector,
// enclosing media/supports/layer, and the file it came from. @font-face rules are kept too.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const BASE = 'https://files.manuscdn.com/webapp/_next/static/chunks/';
const CHUNKS = ['103b_7yr04gh1', '40pg-gaizz3oq', '20ltafw1wb84f', '0l0v22wndw5xb', '1bc8iqysa6nev', '08_8tcflrgsla',
  '0mlvxo4ytv-6f', '0p0dbh3-6xn1t', '06xv5_avbc1xh', '0456am4tjt1gw', '3o5taco3mrcp2', '2-5arczle5b7o', '0qsju0u24gcvr',
  '1gu7e9ofl-qhh', '2zhca6bc4lzot', '0shl_3bp9nxh9', '2o41ojcla7cf9', '2xcvan87951zy'];

const dir = process.argv[2];
const sheets = [];
for (const c of CHUNKS) {
  const name = c + '.css';
  let css;
  if (dir) css = fs.readFileSync(path.join(dir, name), 'utf8');
  else {
    // The chunk names are pinned to one deploy and rotate; a 404 body parsed as CSS would overwrite
    // raw/css-vars.json with sheets that hold no rules.
    const res = await fetch(BASE + name);
    if (!res.ok) { console.error(`${name}: HTTP ${res.status}; the chunk list is stale, update CHUNKS or pass a dir of saved sheets`); process.exit(1); }
    css = await res.text();
  }
  sheets.push({ name, bytes: css.length, css });
}

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const b = await chromium.launch();
const p = await b.newPage();
await p.setContent('<!doctype html><html><head></head><body></body></html>');
const result = await p.evaluate((sheets) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && r.cssRules.length !== undefined && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.constructor.name === 'CSSContainerRule' ? '@container ' + r.conditionText
          : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
    }
  };
  for (const s of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { rules.push({ file: s.name, error: String(e) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts };
}, sheets);
await b.close();

// Group the semantic sets: the :root block and the .dark block of the theme sheet are Manus's
// own two palettes; the --ui-* block is its type and density scale.
const own = (r) => r.selector === ':root' || r.selector === '.dark' || r.selector === 'html' || r.selector === ':root, :host';
const summary = {};
for (const r of result.rules) {
  if (r.error) continue;
  const key = (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  summary[key] = (summary[key] || 0) + Object.keys(r.properties).length;
}
const out = {
  readAt: new Date().toISOString(),
  source: dir ? 'local copies of the chunks' : BASE,
  sheets: sheets.map(({ name, bytes }) => ({ name, bytes })),
  counts: { rules: result.rules.filter((r) => !r.error).length, fonts: result.fonts.length, bySelector: summary },
  rootAndDark: result.rules.filter(own),
  rules: result.rules,
  fonts: result.fonts,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${out.counts.rules} rules with custom properties, ${out.counts.fonts} font faces`);
for (const [k, v] of Object.entries(summary).sort((a, b2) => b2[1] - a[1]).slice(0, 12)) console.log(`  ${v}\t${k}`);
