// Read every custom property jitter.video declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site ships one light theme. Tokens live on body
// (--bg-color, --primary-color, --primary-color-alt, --secondary-color).
// Component modules declare their own --* names. Sheets are same-origin, so
// the CSSOM can read them.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, closePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(3000);
await closePromo(page);

const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try {
    return { name: s.href ? new URL(s.href).pathname : 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') };
  } catch (e) {
    return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: String(e).slice(0, 80) };
  }
}));

const bodyResolved = await page.evaluate(() => {
  const cs = getComputedStyle(document.body);
  const names = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.style) for (const n of r.style) if (n.startsWith('--')) names.push(n);
        if (r.cssRules) walk(r.cssRules);
      }
    };
    try { walk(rules); } catch { /* skip */ }
  }
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const out = {};
  for (const n of [...new Set(names)]) {
    const v = noUrl(cs.getPropertyValue(n).trim());
    if (v) out[n] = v.slice(0, 200);
  }
  return {
    resolvedOnBody: out,
    fontFamily: cs.fontFamily,
    backgroundColor: cs.backgroundColor,
    color: cs.color,
  };
});
await browser.close();

const probe = await (await launch()).browser;
const probePage = await probe.newPage({ viewport: { width: 1440, height: 900 } });
const result = await probePage.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
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
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : (r.cssText || '').split('{')[0].trim().slice(0, 120);
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
    }
  };
  for (const s of sheets) {
    if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: s.unreadable }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const binOf = (r) => {
  const sel = r.selector || '';
  if (/\\\[--/.test(sel)) return 'utility';
  if (/^(body|html|:root)$/.test(sel)) return 'foundation';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const fontKey = (f) => [f['font-family'], f['font-weight'], f['font-style']].join('|');
const seenFonts = new Set();
const fonts = [];
for (const f of result.fonts) {
  const k = fontKey(f);
  if (seenFonts.has(k)) continue;
  seenFonts.add(k);
  const bare = (font) => font;
  fonts.push(bare({ ...f, src: f.src ? 'url(...)' : f.src }));
}

const out = {
  readAt: '2026-11-18',
  source: 'jitter.video stylesheets read through the CSSOM on the live home page (same-origin modules) and re-parsed in a probe document. One light theme. Foundation tokens are declared on body.',
  sheets: sheets.map(({ name, media, css, unreadable }) => ({ name, media, bytes: (css || '').length, unreadable: unreadable || undefined })),
  counts: {
    rules: result.rules.length,
    fonts: fonts.length,
    fontFacesRaw: result.fonts.length,
    names: { foundation: names('foundation').length, app: names('app').length, utility: names('utility').length },
  },
  errors: result.errors,
  foundation: result.rules.filter((r) => r.bin === 'foundation'),
  app: result.rules.filter((r) => r.bin === 'app'),
  utility: result.rules.filter((r) => r.bin === 'utility'),
  fonts,
  body: bodyResolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${result.rules.length} rules, ${result.fonts.length} fonts, body resolved ${Object.keys(bodyResolved.resolvedOnBody).length}`);
await probe.close();
