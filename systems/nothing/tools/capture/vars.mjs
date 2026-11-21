// Reads every custom property nothing.tech's stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// Sheets are collected from network responses plus inline style blocks, then
// re-parsed in a probe document. Names are resolved once on :root and once
// with a dark class. If the site never binds dark, both resolutions match
// and the package records a single light theme.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, chromium } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-GB' });
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const t = r.request().resourceType();
  if (t !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await page.evaluate(() => document.querySelectorAll('#didomi-host, .didomi-popup-backdrop').forEach((n) => n.remove()));
const stay = page.getByRole('button', { name: /stay on/i });
if (await stay.count()) await stay.first().click({ timeout: 4000 }).catch(() => {});
await page.waitForTimeout(800);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const sheets = [...bodies.entries()].concat(inline);
console.log('sheets', sheets.length, 'bytes', sheets.reduce((n, s) => n + s[1].length, 0));

const probe = await context.newPage();
const result = await probe.evaluate(async (sheets) => {
  const noUrl = (v) => String(v).replace(/url\((?!\s*['"]?data:)[^)]*\)/gi, 'url(…)');
  const rules = [];
  const fonts = [];
  const errors = [];
  function walk(list, ctx, file) {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const next = r.conditionText ? ctx.concat(r.cssText.slice(0, r.cssText.indexOf('{')).trim()) : ctx;
        try { walk(r.cssRules, next, file); } catch (e) { errors.push(String(e)); }
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const name = r.style[i];
        if (name.startsWith('--')) props[name] = noUrl(r.style.getPropertyValue(name).trim());
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText, context: ctx, properties: props, file });
    }
  }
  for (const [file, css] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      await sheet.replace(css);
      walk(sheet.cssRules, [], file);
    } catch (e) { errors.push(file + ': ' + e.message); }
  }
  const host = document.createElement('div');
  document.body.appendChild(host);
  const adopted = [];
  for (const [, css] of sheets) {
    try { const s = new CSSStyleSheet(); await s.replace(css); adopted.push(s); } catch { /* skip */ }
  }
  document.adoptedStyleSheets = adopted;
  function resolve(dark) {
    host.className = dark ? 'dark' : '';
    if (dark) document.documentElement.classList.add('dark');
    else document.documentElement.classList.remove('dark');
    const cs = getComputedStyle(host);
    const out = {};
    const names = new Set();
    for (const r of rules) for (const n of Object.keys(r.properties)) names.add(n);
    for (const n of names) {
      host.style.setProperty(n, '');
      const v = cs.getPropertyValue(n).trim();
      out[n] = { raw: rules.find((r) => r.properties[n])?.properties[n] || '', value: v || null };
    }
    return out;
  }
  return { rules, fonts, errors, resolved: { light: resolve(false), dark: resolve(true) } };
}, sheets);

function bin(name, selector) {
  if (name.startsWith('--tw-') || (selector || '').includes('tailwind')) return 'tailwind';
  if (/^--(color|font|text|spacing|radius|shadow|ease|animate)/.test(name)) return 'theme';
  if (/didomi|onetrust/.test(name)) return 'vendor';
  if ((selector || '').startsWith('[') && (selector || '').includes(name)) return 'utility';
  return 'app';
}
const bins = { theme: [], app: [], vendor: [], utility: [], tailwind: [] };
for (const r of result.rules) {
  const names = Object.keys(r.properties);
  const b = bin(names[0], r.selector);
  bins[b].push(r);
}
const out = {
  read: '2026-11-21',
  url: BASE + '/',
  sheetCount: sheets.length,
  errors: result.errors.slice(0, 20),
  fonts: result.fonts.map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
  counts: Object.fromEntries(Object.entries(bins).map(([k, v]) => [k, v.length])),
  theme: bins.theme,
  app: bins.app.slice(0, 400),
  resolved: result.resolved,
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, 'rules', result.rules.length, 'fonts', result.fonts.length, 'errors', result.errors.length);
await browser.close();
