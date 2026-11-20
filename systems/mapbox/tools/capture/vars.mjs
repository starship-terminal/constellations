// Read Mapbox custom properties from the live public homepage.
// PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(4000);
await hideConsent(page);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const sheets = [...bodies.entries()].concat(inline);
console.log('sheets', sheets.length, 'bytes', sheets.reduce((n, s) => n + s[1].length, 0));

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
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
          : (r.cssText || '').split('{')[0].trim().slice(0, 160);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ file, context: ctx, selector: (r.selectorText || '').slice(0, 240), properties: props });
    }
  };
  for (const [file, css] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(css);
      walk(sheet.cssRules, [], file);
    } catch (e) { errors.push(file + ': ' + String(e).slice(0, 160)); }
  }
  return { rules, fonts, errors };
}, sheets);

// Resolve every custom property on a probe element that has the live computed style.
const resolved = await page.evaluate(() => {
  const root = getComputedStyle(document.documentElement);
  const names = new Set();
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.cssRules && !r.style) walk(r.cssRules);
        if (!r.style) continue;
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k && k.startsWith('--')) names.add(k);
        }
      }
    };
    if (rules) walk(rules);
  }
  const out = {};
  for (const n of names) {
    const v = root.getPropertyValue(n).trim();
    if (v) out[n] = v.slice(0, 400);
  }
  const body = getComputedStyle(document.body);
  const h1 = document.querySelector('h1');
  const a = document.querySelector('a');
  const sample = (el) => el ? {
    color: getComputedStyle(el).color,
    background: getComputedStyle(el).backgroundColor,
    fontFamily: getComputedStyle(el).fontFamily,
    fontSize: getComputedStyle(el).fontSize,
    fontWeight: getComputedStyle(el).fontWeight,
    lineHeight: getComputedStyle(el).lineHeight,
    letterSpacing: getComputedStyle(el).letterSpacing,
  } : null;
  return {
    count: Object.keys(out).length,
    vars: out,
    body: sample(document.body),
    h1: sample(h1),
    link: sample(a),
    pageBg: body.backgroundColor,
  };
});

const theme = [];
const app = [];
const utility = [];
const vendor = [];
for (const r of result.rules) {
  const sel = r.selector || '';
  const names = Object.keys(r.properties);
  if (names.some((n) => n.startsWith('--tw-') || n.startsWith('--_tw'))) continue;
  if (/onetrust|ot-|cookie/i.test(sel) || names.some((n) => /onetrust|^--ot-/.test(n))) { vendor.push(r); continue; }
  if (sel === ':root' || sel === 'html' || sel === 'body' || sel.startsWith(':root') || sel.includes('w-mod')) theme.push(r);
  else if (sel.startsWith('[') || sel.includes('--')) utility.push(r);
  else app.push(r);
}

const out = {
  capturedAt: new Date().toISOString(),
  source: 'https://www.mapbox.com/',
  theme: 'light',
  note: 'Mapbox marketing paints one light theme. No dark class or data-theme switch was found.',
  sheetCount: sheets.length,
  ruleCount: result.rules.length,
  fontCount: result.fonts.length,
  errors: result.errors.slice(0, 20),
  theme,
  app,
  utility,
  vendor,
  fonts: result.fonts.map((f) => ({
    file: f.file,
    family: f['font-family'],
    weight: f['font-weight'],
    style: f['font-style'],
    display: f['font-display'],
    src: f.src ? 'url(…)' : undefined,
  })),
  resolved: { light: resolved },
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2));
console.log('rules', result.rules.length, 'resolved', resolved.count, 'fonts', result.fonts.length, 'errors', result.errors.length);
await browser.close();
