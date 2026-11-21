// Read custom properties from cal.com's live public stylesheets.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// cal.com is a Next.js marketing site. Linked CSS is captured from network
// responses; inline sheets are read from the CSSOM. Each rule that declares
// a --* property is kept, then resolved on a probe document.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, contextFor, hideBanners } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await contextFor(browser);
const page = await ctx.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(3500);
await hideBanners(page);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const brand = await page.evaluate(() => ({
  themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.getAttribute('media') })),
  maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  colorScheme: getComputedStyle(document.documentElement).colorScheme,
  htmlClass: document.documentElement.className.slice(0, 200),
  fonts: [...document.fonts].slice(0, 20).map((f) => f.family),
}));
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
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        if (o.src) o.src = noUrl(o.src);
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
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
      if (n) rules.push({ file: String(file).slice(0, 180), selector: (r.selectorText || '').slice(0, 200), context: ctx.slice(0, 4), properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, ctx, file);
    }
  };
  for (const [name, text] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(text);
      walk(sheet.cssRules, [], name);
    } catch (e) { errors.push(String(name).slice(0, 120) + ': ' + e.message); }
  }
  return { rules, fonts, errors };
}, sheets);

const names = new Map();
for (const rule of result.rules) {
  for (const [k, v] of Object.entries(rule.properties)) {
    if (!names.has(k)) names.set(k, { name: k, value: v, selector: rule.selector, file: rule.file, context: rule.context });
  }
}
function bin(name) {
  if (name.startsWith('--tw-')) return 'tailwind';
  if (/^--(color|font|text|spacing|radius|shadow|ease|animate|hp-|cal-|background|foreground|border|ring|muted|accent|primary|destructive|card|popover|sidebar)/.test(name)) return 'theme';
  return 'app';
}
const bins = { theme: [], app: [], tailwind: [], utility: [] };
for (const rec of names.values()) bins[bin(rec.name)].push(rec);

const resolved = await page.evaluate(() => {
  const cs = getComputedStyle(document.documentElement);
  const out = {};
  for (let i = 0; i < cs.length; i++) {
    const k = cs[i];
    if (k.startsWith('--')) out[k] = cs.getPropertyValue(k).trim();
  }
  const body = getComputedStyle(document.body);
  return {
    custom: out,
    body: {
      color: body.color, backgroundColor: body.backgroundColor, fontFamily: body.fontFamily,
      fontSize: body.fontSize, lineHeight: body.lineHeight,
    },
  };
});

const out = {
  capturedAt: new Date().toISOString(),
  source: 'https://cal.com/ live stylesheets, signed out, 1440x900',
  brand,
  sheetCount: sheets.length,
  ruleCount: result.rules.length,
  nameCount: names.size,
  errors: result.errors.slice(0, 20),
  fonts: result.fonts.slice(0, 40),
  bins: Object.fromEntries(Object.entries(bins).map(([k, v]) => [k, v.length])),
  theme: bins.theme.sort((a, b) => a.name.localeCompare(b.name)),
  app: bins.app.filter((r) => !r.name.startsWith('--tw-')).sort((a, b) => a.name.localeCompare(b.name)).slice(0, 400),
  computedOnRoot: resolved,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote css-vars.json', 'names', names.size, 'bins', out.bins, 'fonts', result.fonts.length);
console.log('brand', JSON.stringify(brand));
console.log('body', JSON.stringify(resolved.body));
const themeNames = bins.theme.map((t) => t.name + '=' + t.value).slice(0, 40);
console.log(themeNames.join('\n'));
await browser.close();
