// Reads every custom property webflow.com declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// Stylesheet bodies come from network responses plus inline CSSOM. Each name
// is resolved on a probe document once without u-mode-dark and once with it.
// PRODUCT (adapt): bins are theme (Webflow's own --colors--*, --_color---*,
// --_typography---*, --_components---*), vendor, utility, tailwind.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, chromium, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const t = r.request().resourceType();
  if (t !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const brand = await page.evaluate(() => ({
  themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
  themeColorDark: document.querySelector('meta[name="theme-color"][media*="dark"]')?.content || null,
  maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  manifest: document.querySelector('link[rel="manifest"]')?.href || null,
}));
const sheets = [...bodies.entries()].concat(inline);
await page.close();

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
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : r.cssText.split('{')[0].trim().slice(0, 180);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (!k.startsWith('--')) continue;
        props[k] = noUrl(r.style.getPropertyValue(k).trim());
        n++;
      }
      if (n) rules.push({ file, selector: r.selectorText || '', context: ctx, properties: props });
    }
  };
  for (const [file, css] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(css);
      walk(sheet.cssRules, [], file);
    } catch (e) { errors.push({ file, error: String(e).slice(0, 180) }); }
  }
  return { rules, fonts, errors };
}, sheets);

function bin(rule) {
  const names = Object.keys(rule.properties).join(' ');
  if (/--tw-/.test(names) || (rule.context || []).some((c) => /@layer (properties|theme)/.test(c))) return 'tailwind';
  if (/onetrust|cookiebot|intellimize|qualified|intercom|stripe/i.test(rule.file || '') || /onetrust|cookiebot/i.test(rule.selector || '')) return 'vendor';
  if (/--colors--|__color---|--_color---|--_typography---|--_components---|--_spacing|wf-/.test(names) || /:root|html|body/.test(rule.selector || '')) return 'theme';
  if (/^\[--/.test(rule.selector || '')) return 'utility';
  return 'app';
}
const bins = { theme: [], app: [], vendor: [], utility: [], tailwind: [] };
for (const r of result.rules) bins[bin(r)].push(r);

async function resolve(dark) {
  const p = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await p.setContent('<!doctype html><html class="' + (dark ? 'u-mode-dark' : '') + '"><head></head><body></body></html>');
  await p.evaluate(async (sheets) => {
    for (const [, css] of sheets) {
      const s = new CSSStyleSheet();
      try { s.replaceSync(css); document.adoptedStyleSheets = [...document.adoptedStyleSheets, s]; } catch { /* skip broken */ }
    }
  }, sheets);
  const names = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].sort();
  const resolved = await p.evaluate((names) => {
    const el = document.createElement('div');
    document.body.appendChild(el);
    const cs = getComputedStyle(el);
    const root = getComputedStyle(document.documentElement);
    const out = {};
    for (const n of names) {
      const v = (root.getPropertyValue(n) || cs.getPropertyValue(n) || '').trim();
      if (v) out[n] = { value: v.slice(0, 240), raw: v.slice(0, 240) };
    }
    out.__paint = {
      bg: getComputedStyle(document.body).backgroundColor,
      color: getComputedStyle(document.body).color,
      scheme: getComputedStyle(document.documentElement).colorScheme,
    };
    return out;
  }, names);
  await p.close();
  return resolved;
}

const light = await resolve(false);
const dark = await resolve(true);
const out = {
  capturedAt: new Date().toISOString(),
  url: BASE + '/',
  brand,
  stylesheetCount: sheets.length,
  errors: result.errors,
  fonts: result.fonts.slice(0, 40),
  theme: bins.theme,
  app: bins.app,
  vendor: bins.vendor,
  utility: bins.utility,
  tailwind: bins.tailwind,
  counts: Object.fromEntries(Object.entries(bins).map(([k, v]) => [k, v.length])),
  resolved: { light, dark },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', out.counts, 'resolved', Object.keys(light).length, Object.keys(dark).length);
await browser.close();
