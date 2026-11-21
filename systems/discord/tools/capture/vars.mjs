// Read Discord's custom properties from the live marketing stylesheets and
// write raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// discord.com ships two layers. The marketing site (Webflow, discord-2022)
// declares brand names on :root (--blurple, --not-quite-black, breakpoints).
// The app token sheet (styles.css) declares :root, .theme-light, .theme-dark,
// .theme-darker, .theme-midnight and .visual-refresh. Marketing pages do not
// bind .theme-dark. Resolved values are computed on a probe element inside
// each theme class, so a dark value is declared evidence, not a painted
// marketing page, unless the login wall also resolves it.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(5000);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const brand = await page.evaluate(() => ({
  themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.getAttribute('media') })),
  mask: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  manifest: document.querySelector('link[rel="manifest"]')?.href || null,
  bodyFont: getComputedStyle(document.body).fontFamily,
  bodyBg: getComputedStyle(document.body).backgroundColor,
  bodyColor: getComputedStyle(document.body).color,
  h1: (() => {
    const h = document.querySelector('h1');
    if (!h) return null;
    const cs = getComputedStyle(h);
    return { fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight, lineHeight: cs.lineHeight, letterSpacing: cs.letterSpacing, color: cs.color, textTransform: cs.textTransform };
  })(),
}));
const sheets = [...bodies.entries()].concat(inline);
await page.close();

const probe = await browser.newPage();
const harvested = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file: file.slice(-60) };
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (['font-family', 'font-weight', 'font-style', 'font-display'].includes(k)) o[k] = r.style.getPropertyValue(k).trim();
        }
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : (r.cssText || '').split('{')[0].trim().slice(0, 100);
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
      if (n) rules.push({ file: file.slice(-70), selector: (r.selectorText || '').slice(0, 180), context: ctx.slice(0, 4), properties: props });
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name.slice(-70), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

// Resolve a focused set of names on probe elements, one per theme class.
const KEEP = /^(--(blurple|brand|black|white|not-quite-black|greyple|off-white|dark-not-black|text-link|status-|background-|text-|border-|font-|header-|interactive-|control-|button|primary-|red|green|yellow|focus-|channels-|scrollbar-|spacing|space-|radius|shadow|size-|breakpoint|mobile-nav|always-white|dark-charcoal|button-hover|dark-button-hover))/;
const names = [...new Set(harvested.rules.flatMap((r) => Object.keys(r.properties || {})))]
  .filter((n) => KEEP.test(n) && !n.endsWith('-hsl') && !n.includes('gradient'))
  .sort();

const themes = {
  light: '',
  'theme-light': 'theme-light',
  'theme-dark': 'theme-dark',
  'theme-darker': 'theme-darker',
  'visual-refresh': 'visual-refresh theme-dark',
};
const resolved = {};
for (const [label, cls] of Object.entries(themes)) {
  const html = '<!doctype html><html class="' + cls + '"><head>'
    + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body class="' + cls + '"><div id="probe" class="' + cls + '"></div></body></html>';
  const p2 = await browser.newPage();
  await p2.setContent(html, { waitUntil: 'domcontentloaded' });
  resolved[label] = await p2.evaluate((want) => {
    const el = document.getElementById('probe');
    const cs = getComputedStyle(el);
    const out = {};
    for (const n of want) {
      const v = cs.getPropertyValue(n).trim();
      if (v) out[n] = v.slice(0, 200);
    }
    return out;
  }, names);
  await p2.close();
  console.log('resolved', label, Object.keys(resolved[label]).length);
}

const out = {
  capturedAt: new Date().toISOString(),
  source: 'https://discord.com/ stylesheets, probe document',
  brand,
  sheetCount: sheets.length,
  ruleCount: harvested.rules.length,
  errors: harvested.errors,
  fonts: harvested.fonts.filter((f, i, a) => a.findIndex((x) => x['font-family'] === f['font-family'] && x['font-weight'] === f['font-weight']) === i).slice(0, 80),
  nameCount: names.length,
  names,
  // Keep declaration rules only for kept names, to stay reviewable.
  rules: harvested.rules.map((r) => {
    const properties = {};
    for (const [k, v] of Object.entries(r.properties || {})) if (names.includes(k)) properties[k] = v;
    return Object.keys(properties).length ? { ...r, properties } : null;
  }).filter(Boolean),
  resolved,
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote', path.join(REF, 'raw', 'css-vars.json'), 'names', names.length, 'rules', out.rules.length);
await browser.close();
