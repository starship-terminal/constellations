// Read custom properties and font faces from live public pages.
// RevenueCat's marketing CSS is same-origin enough for the CSSOM on the live page.
// Cross-origin sheets that throw are skipped and named in the output.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, hideConsent, RAW } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(RAW, 'css-vars.json');
fs.mkdirSync(RAW, { recursive: true });

const PAGES = ['/', '/pricing', '/feature/paywalls', '/docs', '/blog', '/why-revenuecat'];

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await ctx.newPage();

const all = { capturedAt: new Date().toISOString().slice(0, 10), pages: {}, resolved: {}, fontFaces: [], themeChecks: {}, sheets: [] };

for (const pth of PAGES) {
  const url = BASE + pth;
  console.log('vars', url);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1800);
  await hideConsent(page);
  const reading = await page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
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
            : (r.constructor && r.constructor.name === 'CSSLayerBlockRule') ? '@layer ' + (r.name || '')
            : r.cssText.split('{')[0].trim().slice(0, 120);
          walk(r.cssRules, [...ctx, head], file);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) rules.push({ context: ctx, selector: r.selectorText, properties: props, file });
      }
    };
    for (const sheet of [...document.styleSheets]) {
      let href = '';
      try { href = sheet.href || 'inline'; } catch { href = 'opaque'; }
      try {
        walk(sheet.cssRules, [], href);
      } catch (e) {
        skipped.push({ href, error: String(e).slice(0, 160) });
      }
    }
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = new Set();
    for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
    const resolved = {};
    for (const k of names) {
      try {
        const v = root.getPropertyValue(k).trim();
        if (v) resolved[k] = noUrl(v);
      } catch {}
    }
    return {
      rules, fonts, skipped,
      root: {
        background: body.backgroundColor,
        color: body.color,
        fontFamily: body.fontFamily,
        fontSize: body.fontSize,
        lineHeight: body.lineHeight,
        colorScheme: root.colorScheme,
      },
      htmlClass: document.documentElement.className.slice(0, 240),
    };
  });
  all.pages[pth] = {
    root: reading.root,
    htmlClass: reading.htmlClass,
    ruleCount: reading.rules.length,
    skipped: reading.skipped,
  };
  all.sheets.push(...reading.skipped.map((s) => ({ page: pth, ...s })));
  if (!all.rules) all.rules = [];
  if (!all.resolved) all.resolved = {};
  if (!all.fontFaces) all.fontFaces = [];
  if (pth === '/') {
    all.rules = reading.rules;
    all.fontFaces = reading.fonts;
    all.resolved = reading.resolved || {};
  } else {
    for (const rule of reading.rules) {
      for (const [k, v] of Object.entries(rule.properties)) {
        if (!all.resolved[k]) all.resolved[k] = v;
      }
    }
  }
  console.log(' ', reading.rules.length, 'rules', Object.keys(reading.resolved || {}).length, 'resolved', reading.skipped.length, 'skipped');
}

// theme probe: prefers-color-scheme dark does not restyle the marketing page
const dark = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  colorScheme: 'dark',
  locale: 'en-US',
});
const dp = await dark.newPage();
await dp.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 40000 });
await dp.waitForTimeout(1200);
all.themeChecks.marketingPrefersDark = await dp.evaluate(() => ({
  bodyBg: getComputedStyle(document.body).backgroundColor,
  bodyColor: getComputedStyle(document.body).color,
  scheme: getComputedStyle(document.documentElement).colorScheme,
}));
await dark.close();

fs.writeFileSync(OUT, JSON.stringify(all, null, 2));
console.log('wrote', OUT, 'rules', (all.rules || []).length, 'resolved', Object.keys(all.resolved).length);
await browser.close();
