// Read custom properties from Runway's live public stylesheets (network responses + inline styles).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Writes raw/css-vars.json. Cross-origin sheets are taken from the network, not the CSSOM.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const URLS = [
  'https://runway.com/',
  'https://runway.com/pricing',
  'https://runway.com/product',
  'https://dev.runwayml.com/',
  'https://docs.dev.runwayml.com/',
];

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const sheets = new Map();

page.on('response', async (res) => {
  try {
    const ct = res.headers()['content-type'] || '';
    const url = res.url();
    if (!/text\/css|stylesheet/i.test(ct) && !/\.css(\?|$)/.test(url)) return;
    if (sheets.has(url)) return;
    const css = await res.text();
    if (css && css.includes('--')) sheets.set(url, css);
  } catch { /* body unavailable */ }
});

for (const url of URLS) {
  console.log('open', url);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch((e) => console.log('  fail', e.message.split('\n')[0]));
  await page.waitForTimeout(2500);
  const inline = await page.evaluate(() => [...document.querySelectorAll('style')].map((s) => s.textContent || '').filter((t) => t.includes('--')));
  inline.forEach((css, i) => sheets.set(url + '#inline-' + i, css));
}
await browser.close();
console.log('sheets', sheets.size);

const parsePage = await chromium.launch({ headless: true }).then(async (b) => {
  const p = await (await b.newContext()).newPage();
  await p.setContent('<!doctype html><html><head></head><body></body></html>');
  return { browser: b, page: p };
});

const parsed = await parsePage.page.evaluate((list) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const decls = [];
  const fonts = [];
  for (const item of list) {
    let sheet;
    try { sheet = new CSSStyleSheet(); sheet.replaceSync(item.css); } catch { continue; }
    const walk = (rules, ctx) => {
      for (const r of rules) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file: item.name };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const head = r.cssText.split('{')[0].trim().slice(0, 180);
          walk(r.cssRules, [...ctx, head]);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) decls.push({ selector: r.selectorText, context: ctx, props, file: item.name });
      }
    };
    walk(sheet.cssRules, []);
  }
  return { decls, fonts };
}, [...sheets.entries()].map(([name, css]) => ({ name: name.slice(0, 180), css: css.slice(0, 1_500_000) })));

await parsePage.browser.close();

function bin(name, selector) {
  if (name.startsWith('--tw-') || name.startsWith('--radix-')) return 'vendor';
  if (/tailwind|@layer theme|@layer properties/.test(selector || '')) return 'vendor';
  return 'app';
}

const byName = {};
for (const d of parsed.decls) {
  for (const [name, value] of Object.entries(d.props)) {
    const b = bin(name, (d.context || []).join(' ') + ' ' + (d.selector || ''));
    byName[name] ??= [];
    byName[name].push({ value, selector: d.selector, context: d.context, file: d.file, bin: b });
  }
}

const resolved = { light: {}, dark: {} };
for (const [name, occ] of Object.entries(byName)) {
  const root = occ.find((o) => /:root|html/.test(o.selector || '')) || occ[0];
  resolved.light[name] = { value: root.value, raw: root.value, selector: root.selector, bin: root.bin };
  resolved.dark[name] = { value: root.value, raw: root.value, selector: root.selector, bin: root.bin, note: 'no public dark theme; same as light' };
}

const out = {
  product: 'Runway',
  captured: '2026-11-21',
  source: 'live public stylesheets on runway.com, dev.runwayml.com, docs.dev.runwayml.com',
  theme: 'light only on the public marketing site',
  sheetCount: sheets.size,
  declarationCount: parsed.decls.length,
  fonts: parsed.fonts.slice(0, 40),
  names: Object.keys(byName).sort(),
  resolved,
  occurrences: byName,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('names', out.names.length, 'decls', parsed.decls.length, 'fonts', parsed.fonts.length);
console.log(out.names.filter((n) => !n.startsWith('--tw-')).slice(0, 80).join('\n'));
