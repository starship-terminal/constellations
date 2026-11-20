// Read Sharewillow's declared custom properties from the live public homepage.
// The marketing site ships one light theme. Hero colours are a dark section
// inside that theme, not a second theme toggle.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const css = [];
page.on('response', async (r) => {
  const ct = r.headers()['content-type'] || '';
  if (ct.includes('text/css') || r.url().includes('.css')) {
    try { css.push({ url: r.url().split('?')[0], text: await r.text() }); } catch { /* ignore */ }
  }
});
await page.goto('https://www.sharewillow.com/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(2000);

const parsed = await page.evaluate((sheets) => {
  const noUrl = (v) => v.replace(/url\([^)]*\)/gi, 'url(…)');
  const rules = [];
  const fonts = [];
  function walk(list, ctx, file) {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        if (o.src) o.src = noUrl(o.src);
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.cssText.split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText || '', props, ctx, file });
    }
  }
  const style = document.createElement('style');
  style.textContent = sheets.map((s) => s.text).join('\n');
  document.head.appendChild(style);
  walk(style.sheet.cssRules, [], 'network');
  const resolved = {};
  const cs = getComputedStyle(document.documentElement);
  for (const rule of rules) {
    for (const name of Object.keys(rule.props)) {
      resolved[name] = { raw: rule.props[name], value: cs.getPropertyValue(name).trim() || rule.props[name] };
    }
  }
  return { rules, fonts, resolved };
}, css.map((s) => ({ url: s.url, text: s.text })));

const brand = {};
const utility = {};
for (const [name, rec] of Object.entries(parsed.resolved)) {
  const brandish = /^--color-(bg|surface|border|ink|accent|hero|lemon|ivory|paper|espresso|lime|peach|sky|rose)/.test(name)
    || name.startsWith('--font-') || name.startsWith('--radius-') || name.startsWith('--ease-')
    || name === '--spacing' || name.startsWith('--leading-') || name.startsWith('--tracking-')
    || name.startsWith('--font-weight');
  (brandish ? brand : utility)[name] = rec;
}

const out = {
  product: 'sharewillow',
  captured: '2026-11-21',
  url: 'https://www.sharewillow.com/',
  theme: 'light only; no data-theme toggle. --color-hero-* paints a dark section inside the light page.',
  stylesheetCount: css.length,
  stylesheets: css.map((s) => s.url),
  fontFaces: parsed.fonts.filter((f) => /Matter|Mackinac/i.test(JSON.stringify(f))).slice(0, 24),
  resolved: { light: brand },
  utilityCount: Object.keys(utility).length,
  ruleCount: parsed.rules.length,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('brand vars', Object.keys(brand).length, 'utility', Object.keys(utility).length, 'fonts', parsed.fonts.length);
await browser.close();
