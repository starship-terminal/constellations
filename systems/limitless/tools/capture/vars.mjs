// Harvest Limitless stylesheets into raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// limitless.ai is a Next.js + Tailwind site. Almost every painted colour is a
// Tailwind utility (text-slate-900, bg-white/75, shadow-button-light), not a
// custom-property token. This script keeps @font-face rules, every --* declaration
// that is not a Tailwind internal, and a palette of literal colours declared in
// the same-origin CSS. Resolution is one pass: the site ships one painted theme.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, APP, HELP, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const browser = await chromium.launch({ headless: true });
const bodies = new Map();
const pages = [BASE + '/', BASE + '/developers', BASE + '/for/voice-recorder', APP + '/', HELP + '/en/'];
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
page.on('response', async (r) => {
  const t = r.request().resourceType();
  if (t !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 }).catch((e) => console.log('skip', url, e.message.split('\n')[0]));
  await page.waitForTimeout(1800);
  await hideConsent(page);
}
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const fontsLoaded = await page.evaluate(() => [...document.fonts].map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status })));
const bodyFont = await page.evaluate(() => getComputedStyle(document.body).fontFamily);
await ctx.close();

const sheets = [...bodies.entries()].concat(inline);
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const probe = await probeCtx.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const colourRe = /#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)/g;
  const colours = {};
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
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : (r.cssText || '').split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      const colourProps = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        else if (/color|shadow|fill|stroke/.test(k)) {
          const v = noUrl(r.style.getPropertyValue(k).trim());
          if (colourRe.test(v)) colourProps[k] = v;
          colourRe.lastIndex = 0;
        }
      }
      if (Object.keys(props).length) rules.push({ file: String(file).slice(0, 80), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(-2), properties: props });
      for (const [k, v] of Object.entries(colourProps)) {
        for (const m of v.matchAll(colourRe)) {
          const lit = m[0].toLowerCase().replace(/\s+/g, ' ');
          (colours[lit] ??= { count: 0, uses: [] }).count++;
          if (colours[lit].uses.length < 4) colours[lit].uses.push({ selector: (r.selectorText || '').slice(0, 100), property: k });
        }
      }
    }
  };
  for (const [name, text] of sheets) {
    if (!text || text.length > 2_500_000) continue;
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 80), error: String(e).slice(0, 120) }); continue; }
    walk(ss.cssRules, [], String(name).split('/').pop());
  }
  return { rules, fonts, errors, colours };
}, sheets);
await browser.close();

const keep = result.rules.filter((r) => Object.keys(r.properties).some((n) => !n.startsWith('--tw-')));
const palette = Object.entries(result.colours)
  .filter(([k]) => k !== '#0000' && k !== '#fff0' && !k.startsWith('rgba(0, 0, 0, 0)') && !k.startsWith('rgba(0,0,0,0)'))
  .sort((a, b) => b[1].count - a[1].count)
  .slice(0, 80);

const out = {
  source: 'limitless.ai public stylesheets, harvested 2026-11-18. One painted theme (light). Tailwind utilities carry most colour; custom properties are mostly --tw-* internals plus --font-greycliff and a few product gradients.',
  pages,
  bodyFont,
  fontsLoaded,
  sheetCount: sheets.length,
  fontFaces: result.fonts.slice(0, 40),
  app: keep.slice(0, 400),
  palette: Object.fromEntries(palette),
  errors: result.errors.slice(0, 12),
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('sheets', sheets.length, 'font-faces', result.fonts.length, 'kept rules', keep.length, 'palette', palette.length, 'errors', result.errors.length);
