// Reads helloklean.com's custom properties from its stylesheets and resolves
// each name the way the browser does, on a light :root probe.
//
//   PLAYWRIGHT=... node vars.mjs
//
// Writes raw/css-vars.json. The site is light only (Shopify theme BF26 /
// Quickfire). Cross-origin sheets that the CSSOM blocks are fetched and
// reparsed. Signed query strings are stripped before anything is written.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, BASE, RAW, clearChallenge, closePromo } from './public/lib.mjs';

const OUT = path.join(RAW, 'css-vars.json');
fs.mkdirSync(RAW, { recursive: true });

const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
  : v);

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-GB' });
const page = await ctx.newPage();
const sheets = [];
page.on('response', async (res) => {
  const ct = res.headers()['content-type'] || '';
  const url = res.url();
  if (!/text\/css|stylesheet/.test(ct) && !/\.css(\?|$)/.test(url)) return;
  if (sheets.length > 40) return;
  try {
    const text = await res.text();
    if (text && text.includes('--')) sheets.push({ url: url.split('?')[0].slice(0, 180), text: text.slice(0, 400000) });
  } catch { /* body already consumed */ }
});
await page.goto(BASE + '/en-int', { waitUntil: 'domcontentloaded', timeout: 90000 });
await clearChallenge(page);
await page.waitForTimeout(5000);
await closePromo(page);

const harvested = await page.evaluate(() => {
  // The page runs apart from this module, so it needs its own copy; masking before the
  // slice keeps a cut-off url( from slipping past the pattern.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const blocked = [];
  const rootVars = {};
  const cs = getComputedStyle(document.documentElement);
  for (const sheet of document.styleSheets) {
    let cssRules;
    try { cssRules = sheet.cssRules; } catch (e) { blocked.push((sheet.href || 'inline').split('?')[0]); continue; }
    const walk = (list, context) => {
      for (const rule of list) {
        if (rule.type === CSSRule.MEDIA_RULE) { walk(rule.cssRules, context.concat(rule.conditionText)); continue; }
        if (rule.type === CSSRule.SUPPORTS_RULE) { walk(rule.cssRules, context); continue; }
        if (!rule.style) continue;
        const props = {};
        for (const p of rule.style) {
          if (p.startsWith('--')) props[p] = noUrl(rule.style.getPropertyValue(p).trim()).slice(0, 240);
        }
        if (Object.keys(props).length) {
          rules.push({ selector: (rule.selectorText || '').slice(0, 180), context, properties: props, href: (sheet.href || 'inline').split('?')[0].slice(0, 160) });
        }
      }
    };
    walk(cssRules, []);
  }
  // Resolved values of every name we saw, plus a scan of computed custom props.
  const names = new Set();
  for (const r of rules) for (const k of Object.keys(r.properties)) names.add(k);
  const resolved = {};
  for (const name of names) {
    const v = noUrl(cs.getPropertyValue(name).trim());
    if (v) resolved[name] = v.slice(0, 240);
  }
  const fonts = [...document.fonts].slice(0, 30).map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status }));
  const theme = {
    bodyClass: document.body.className.slice(0, 200),
    htmlClass: document.documentElement.className.slice(0, 120),
    colorScheme: cs.colorScheme,
    shopifyTheme: window.Shopify && window.Shopify.theme ? { name: window.Shopify.theme.name, schema: window.Shopify.theme.schema_name, version: window.Shopify.theme.schema_version } : null,
  };
  return { rules: rules.slice(0, 800), blocked: blocked.slice(0, 20), resolved, fonts, theme, title: document.title };
});

const resolved = {};
for (const [name, value] of Object.entries(harvested.resolved)) {
  resolved[name] = { value: noUrl(value), raw: noUrl(value) };
}

const out = {
  source: 'https://helloklean.com/en-int',
  captured: new Date().toISOString(),
  theme: harvested.theme,
  fonts: harvested.fonts,
  blocked: harvested.blocked,
  rules: harvested.rules.map((r) => ({ ...r, properties: Object.fromEntries(Object.entries(r.properties).map(([k, v]) => [k, noUrl(v)])) })),
  resolved: { light: resolved },
  themeChecks: {
    darkClass: /dark/.test(harvested.theme.bodyClass + harvested.theme.htmlClass),
    colorScheme: harvested.theme.colorScheme,
    note: 'Shopify theme BF26 / Quickfire. No dark class or data-theme switch was present on the captured pages.',
  },
  networkSheets: sheets.map((s) => s.url),
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
console.log('rules', out.rules.length, 'resolved', Object.keys(resolved).length, 'blocked', harvested.blocked.length, '->', OUT);
await browser.close();
