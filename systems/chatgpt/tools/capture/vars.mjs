// Read every custom property ChatGPT's stylesheets declare and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/vars.mjs
//
// chatgpt.com serves its CSS from its own origin, so snapshot.js read every sheet through the CSSOM
// and inlined it as a <style> block in each page copy. This script collects those blocks from every
// copy in SNAPS, keeps one of each (by the sha1 of its text), and parses each in a headless Chromium
// with a constructed CSSStyleSheet. Every rule that declares a custom property is kept with its
// selector, its enclosing @media/@supports/@layer/@container chain and the sheet it came from;
// @font-face rules are kept too, with a data: URL cut to its media type. Sheets are named
// `s-<first 10 hex of the sha1>`.
//
// Since the 2026-10 redesign the palette is declared on `:where(:root), :where([data-theme])` and
// `.chatgpt-theme[data-theme="light"|"dark"]`, mostly as var() chains and color-mix() into the
// primitive ramps (`--gray-*`, `--blue-*`, ...). So the value each root-level name takes is read
// from a real page copy, on <html>, in dark (as captured) and light (every data-theme="dark" set to
// light, as render.mjs does), and resolved by the browser: a colour through a probe element's
// `color` and a canvas (so color-mix(), oklab() and relative colours become one sRGB value), a
// length through a probe's `width`, a shadow through `box-shadow`.
//
// It also records what the custom properties cannot: every rule under prefers-reduced-motion or
// [data-reduced-motion] (what changes when motion is reduced), every z-index the rules declare,
// every grid-template-columns, and, from the page copies' class lists, how many elements use each
// Tailwind spacing, radius and border-width utility, per page.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const SNAPS = process.env.SNAPS ? path.resolve(process.env.SNAPS) : null;
if (!SNAPS) { console.error('SNAPS=<dir of page copies> is required'); process.exit(2); }

const files = fs.readdirSync(SNAPS).filter((n) => n.endsWith('.html')).sort();
const sheets = new Map();
const classUse = {};
const UTIL = /^(?:[a-z0-9@:[\]-]+:)?(-?(?:p|px|py|pt|pb|pl|pr|ps|pe|m|mx|my|mt|mb|ml|mr|ms|me|gap|gap-x|gap-y|space-x|space-y)-(?:\d+(?:\.\d+)?|px)|rounded(?:-(?:[trblse]{1,2}-)?(?:none|xs|sm|md|lg|xl|2xl|3xl|4xl|full|\[[^\]]+\]))?|border(?:-[trblxyse])?(?:-(?:0|2|4|8|\[[^\]]*px\]))?)$/;
for (const f of files) {
  const html = fs.readFileSync(path.join(SNAPS, f), 'utf8');
  const label = f.replace(/\.html$/, '');
  for (const m of html.matchAll(/<style([^>]*)>([\s\S]*?)<\/style>/g)) {
    const css = m[2].replace(/<\\\/style/gi, '</style');
    const id = 's-' + crypto.createHash('sha1').update(css).digest('hex').slice(0, 10);
    const media = (m[1].match(/media="([^"]*)"/) || [])[1] || '';
    if (!sheets.has(id)) sheets.set(id, { name: id, firstIn: label, media, bytes: css.length, css, pages: [] });
    const s = sheets.get(id);
    if (!s.pages.includes(label)) s.pages.push(label);
  }
  // Class lists of the page body only (the <style> blocks are cut first).
  const body = html.replace(/<style[\s\S]*?<\/style>/g, '');
  const per = {};
  for (const m of body.matchAll(/\sclass="([^"]*)"/g)) {
    for (const c of m[1].split(/\s+/)) {
      const u = c.match(UTIL);
      if (u) per[u[1]] = (per[u[1]] || 0) + 1;
    }
  }
  for (const [k, n] of Object.entries(per)) { (classUse[k] ||= { elements: 0, pages: 0 }); classUse[k].elements += n; classUse[k].pages += 1; }
}

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const b = await chromium.launch();
const p = await b.newPage();
await p.setContent('<!doctype html><html><head></head><body></body></html>');
const result = await p.evaluate((list) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const motion = [];
  const zIndex = [];
  const grid = [];
  const walk = (rs, ctx, file) => {
    for (const r of rs) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) {
          let v = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          v = v.replace(/url\("?data:([^;,]+)[^)]*\)/g, 'url(data:$1,…)');
          o[r.style[i]] = v;
        }
        fonts.push(o);
        continue;
      }
      if (r.type === CSSRule.KEYFRAMES_RULE) continue;
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.constructor.name === 'CSSContainerRule' ? '@container ' + r.conditionText
          : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const outer = [...ctx].reverse().find((c) => c.startsWith('& '));
      const selector = r.selectorText ?? (outer ? outer.slice(2) : ':scope');
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector, context: ctx, properties: props });
      const all = {};
      for (let i = 0; i < r.style.length; i++) all[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
      if (ctx.some((c) => /prefers-reduced-motion/.test(c)) || /data-reduced-motion/.test(selector)) motion.push({ file, selector: selector.slice(0, 240), context: ctx, properties: all });
      if (all['z-index'] !== undefined) zIndex.push({ selector: selector.slice(0, 160), value: all['z-index'] });
      if (all['grid-template-columns'] !== undefined) grid.push({ selector: selector.slice(0, 160), value: all['grid-template-columns'] });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, '& ' + r.selectorText], file);
    }
  };
  const errors = [];
  for (const s of list) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e) }); continue; }
    walk(ss.cssRules, s.media ? ['@media ' + s.media] : [], s.name);
  }
  return { rules, fonts, motion, zIndex, grid, errors };
}, [...sheets.values()].map(({ name, css, media }) => ({ name, css, media })));

// The names a root-level selector declares. Rules scoped to the extension and Electron windows
// (data-codex-window-type="extension"|"electron") declare names too; the cascade decides, and the
// copies were taken in the browser window, so the computed reading is the browser window's value.
const ROOTISH = /(^|[\s(,])(:root|:host|html|\[data-theme|\.chatgpt-theme|:where\(:root|:where\(\[data-theme)/;
const rootNames = [...new Set(result.rules.filter((r) => ROOTISH.test(r.selector)).flatMap((r) => Object.keys(r.properties)))].sort();

const ctx = await b.newContext();
await ctx.route('**/*', (route) => (route.request().url().startsWith('file:') ? route.continue() : route.abort()));
const page = await ctx.newPage();
const probe = fs.existsSync(path.join(SNAPS, 'home-dark.html')) ? 'home-dark' : files[0].replace(/\.html$/, '');
await page.goto(`file://${SNAPS}/${probe}.html`, { waitUntil: 'domcontentloaded', timeout: 60000 });
const computed = await page.evaluate((names) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const h = document.documentElement;
  const host = document.createElement('div');
  host.style.cssText = 'position:absolute;left:-9999px;top:0;color:rgb(1, 2, 3);';
  const el = document.createElement('div');
  host.appendChild(el);
  document.body.appendChild(host);
  const cv = document.createElement('canvas').getContext('2d');
  const toSrgb = (c) => { cv.fillStyle = '#010203'; cv.fillStyle = c; return cv.fillStyle; };
  const COLORISH = /^(#|rgba?\(|hsla?\(|color-mix\(|color\(|oklab\(|oklch\(|lab\(|lch\(|hwb\(|light-dark\(|transparent$|currentcolor$|white$|black$)/i;
  const LENGTHISH = /^-?[\d.]+(px|rem|em)$|^calc\(|^clamp\(|^min\(|^max\(/;
  const read = () => {
    const cs = getComputedStyle(h);
    const raw = {}, resolved = {};
    for (const n of names) {
      const v = noUrl(cs.getPropertyValue(n).trim());
      if (!v) continue;
      raw[n] = v;
      if (COLORISH.test(v)) {
        el.style.color = '';
        el.style.setProperty('color', `var(${n})`);
        const c = getComputedStyle(el).color;
        if (c !== 'rgb(1, 2, 3)' || /^#010203|rgb\(1, 2, 3\)/.test(v)) { resolved[n] = { kind: 'color', value: toSrgb(c) }; continue; }
      }
      if (LENGTHISH.test(v)) {
        el.style.width = '7.77px';
        el.style.setProperty('width', `var(${n})`);
        const w = getComputedStyle(el).width;
        if (w !== '7.77px' && /px$/.test(w)) { resolved[n] = { kind: 'dimension', value: w }; continue; }
      }
      if (/\dpx/.test(v) && /(#|rgb|color|oklab)/.test(v)) {
        el.style.boxShadow = '';
        el.style.setProperty('box-shadow', `var(${n})`);
        const s = getComputedStyle(el).boxShadow;
        if (s && s !== 'none') { resolved[n] = { kind: 'shadow', value: s.replace(/(oklab|lab|color)\([^)]*\)/g, (m) => toSrgb(m)) }; continue; }
      }
    }
    return { raw, resolved };
  };
  const captured = { theme: h.getAttribute('data-theme'), classes: h.className, windowType: h.getAttribute('data-codex-window-type'), reducedMotion: h.getAttribute('data-reduced-motion') };
  const dark = read();
  const darkEls = [...document.querySelectorAll('[data-theme="dark"]')];
  darkEls.forEach((n) => n.setAttribute('data-theme', 'light'));
  h.style.colorScheme = 'light';
  const light = read();
  return { captured, nestedThemeScopes: darkEls.length - 1, dark, light };
}, rootNames);
computed.page = probe;
await b.close();

const z = {};
for (const r of result.zIndex) { (z[r.value] ||= { rules: 0, selectors: [] }); z[r.value].rules++; if (z[r.value].selectors.length < 6) z[r.value].selectors.push(r.selector); }
const g = {};
for (const r of result.grid) { (g[r.value] ||= { rules: 0, selectors: [] }); g[r.value].rules++; if (g[r.value].selectors.length < 4) g[r.value].selectors.push(r.selector); }
const sortObj = (o, f) => Object.fromEntries(Object.entries(o).sort(f));
const out = {
  // The day the copies were taken (the oldest copy's local date), so a rebuild writes the same bytes.
  readAt: (() => { const t = new Date(Math.min(...files.map((n) => fs.statSync(path.join(SNAPS, n)).mtimeMs))); return `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, '0')}-${String(t.getDate()).padStart(2, '0')}`; })(),
  source: 'the <style> blocks snapshot.js inlined into each page copy from chatgpt.com\'s same-origin stylesheets, deduplicated by sha1',
  pages: files.map((n) => n.replace(/\.html$/, '')),
  sheets: [...sheets.values()].map(({ name, firstIn, media, bytes, pages }) => ({ name, firstIn, media: media || undefined, bytes, pages: pages.length })),
  counts: { rules: result.rules.length, rootNames: rootNames.length, fonts: result.fonts.length, reducedMotionRules: result.motion.length, zIndexRules: result.zIndex.length, gridRules: result.grid.length },
  errors: result.errors,
  computed,
  reducedMotion: result.motion,
  zIndex: sortObj(z, (a, c) => c[1].rules - a[1].rules || (a[0] < c[0] ? -1 : 1)),
  gridColumns: sortObj(g, (a, c) => c[1].rules - a[1].rules || (a[0] < c[0] ? -1 : 1)),
  classUse: sortObj(classUse, (a, c) => c[1].elements - a[1].elements || (a[0] < c[0] ? -1 : 1)),
  fonts: result.fonts,
  rules: result.rules,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${sheets.size} sheets, ${out.counts.rules} rules with custom properties, ${rootNames.length} root names, ${Object.keys(computed.dark.resolved).length} resolved in dark, ${out.counts.reducedMotionRules} reduced-motion rules, ${out.counts.zIndexRules} z-index rules, ${Object.keys(classUse).length} utilities counted`);
