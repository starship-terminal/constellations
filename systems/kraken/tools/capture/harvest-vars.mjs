// Read Kraken's declared design tokens from the live public pages.
// Writes raw/css-vars.json. OneTrust is hidden, never clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest-vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, hideConsent, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const PAGES = [
  { key: 'light', url: 'https://www.kraken.com/' },
  { key: 'dark', url: 'https://www.kraken.com/pro' },
  { key: 'signup', url: 'https://www.kraken.com/sign-up' },
];

const browser = await chromium.launch({ headless: true });
const out = {
  product: 'kraken',
  captured: '2026-11-18',
  note: 'Declared custom properties harvested from the CSSOM of public kraken.com pages. resolved.<theme> is getComputedStyle on the body theme element. url() values are stripped.',
  pages: {},
  fonts: [],
  resolved: {},
  themes: {},
};

for (const spec of PAGES) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  console.log('harvest', spec.key, spec.url);
  await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(3500);
  await hideConsent(page);
  const data = await page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/gi, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = {};
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim()).slice(0, 180);
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.selectorText) {
          const head = r.conditionText ? '@media ' + String(r.conditionText).slice(0, 80) : (r.cssText || '').split('{')[0].trim().slice(0, 80);
          walk(r.cssRules, [...ctx, head].slice(0, 4));
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (!k.startsWith('--')) continue;
          if (k.startsWith('--tw-')) continue;
          props[k] = noUrl(r.style.getPropertyValue(k).trim()).slice(0, 180);
        }
        if (Object.keys(props).length) {
          rules.push({
            selector: (r.selectorText || '').slice(0, 160),
            context: ctx.slice(0, 3),
            properties: props,
          });
        }
      }
    };
    for (const sheet of document.styleSheets) {
      try { if (sheet.cssRules) walk(sheet.cssRules, []); } catch { /* cross-origin */ }
    }
    const themeEl = document.body;
    const cs = getComputedStyle(themeEl);
    const names = new Set();
    for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
    const resolved = {};
    for (const name of names) {
      const v = cs.getPropertyValue(name);
      if (v && v.trim()) resolved[name] = noUrl(v.trim()).slice(0, 180);
    }
    return {
      title: document.title.slice(0, 120),
      url: location.href.split('?')[0],
      theme: document.body.getAttribute('data-theme'),
      bodyClass: String(document.body.className).slice(0, 180),
      ruleCount: rules.length,
      nameCount: names.size,
      resolvedCount: Object.keys(resolved).length,
      rules,
      fonts,
      resolved,
    };
  });
  out.pages[spec.key] = {
    url: data.url,
    title: data.title,
    theme: data.theme,
    bodyClass: data.bodyClass,
    ruleCount: data.ruleCount,
    nameCount: data.nameCount,
    resolvedCount: data.resolvedCount,
  };
  out.resolved[spec.key] = data.resolved;
  out.themes[spec.key] = { rules: data.rules };
  if (spec.key === 'light') out.fonts = data.fonts;
  console.log(' ', data.theme, 'rules', data.ruleCount, 'resolved', data.resolvedCount);
  await ctx.close();
}

fs.writeFileSync(OUT, JSON.stringify(out));
console.log('wrote', OUT, 'bytes', fs.statSync(OUT).size);
await browser.close();
