// Dumps every custom property Expedia's pages declare, by stylesheet, selector and
// media condition, sorted into who owns it, plus the font faces, the fonts that
// loaded, and the dark-theme checks.
//
//   PLAYWRIGHT=<path to playwright index.mjs> PAGES=<dir of archived pages> \
//     node tools/capture/vars.mjs     (writes raw/css-vars.json)
//
// www.expedia.com is PerimeterX-walled (HTTP 429 "Bot or Not?"), so the DOM is a
// Wayback server-rendered copy served locally (see public/lib.mjs); the styles
// are the site's OWN files fetched live from *.travel-assets.com plus the theme
// palette block Expedia inlines into its SSR <style>. Link sheets are read from
// response bodies (the CSSOM refuses cross-origin sheets), inline sheets via the
// CSSOM. Owners:
//   palette   the inlined theme palettes: --light_1__*, --dark_1__*,
//             --marketing_3__* and friends (one --theme__role pair per var)
//   egds      the Expedia Group Design System semantic layer: --egds-*, rebound
//             per theme by [data-theme-light=<name>]/[data-theme-dark=<name>]
//   uitk      UITK component internals (--uitk-*)
//   legacy    the older __-joined component vars (--button__*, --link__*,
//             --font_face__*, --field__*...) that are not theme palettes
//   other     anything else a sheet declares
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { servePages, open, launch, RAW } from './public/lib.mjs';

const PAGESDIR = process.env.PAGES || path.join(os.homedir(), '.design-systems', 'expedia', 'pages');
const THEMES = ['light-1', 'dark-1', 'dark-2', 'marketing-3', 'bright-1'];
const clean = (s) => String(s)
  .replace(/(https?:\/\/[^\s"')?]+)\?[^\s"')]*/g, '$1')
  .replace(/url\(\s*["']?data:[^)]{80,}\)/g, 'url(data:…)');

function owner(name, selector, sheet) {
  if (name.startsWith('--egds-')) return 'egds';
  if (name.startsWith('--uitk-')) return 'uitk';
  // a theme palette name: --<theme words>__<role>, theme words drawn from the
  // data-theme-* bindings (light_1, dark_1, marketing_3, global_loyalty_*, ...)
  const m = name.match(/^--([a-z0-9_]+)__([a-z0-9_]+)$/);
  if (m && !/__.*__/.test(name) && /^(light|dark|bright|marketing|ai|romie|global)_/.test(m[1])) return 'palette';
  if (name.includes('__')) return 'legacy';
  if (/travel-assets\.com/.test(sheet) || sheet.startsWith('inline')) return 'app';
  return 'other';
}

const decls = new Map();
const faces = new Map();
const fontsLoaded = {};
const checks = {};
const resolved = {};
const sheetsSeen = {};

const { srv, port } = await servePages(PAGESDIR);
const base = `http://127.0.0.1:${port}`;
const PAGES = { home: `${base}/pages/home.html`, search: `${base}/pages/search.html` };

const { browser, context } = await launch();
for (const [key, url] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  console.log('open', key, url);
  // scripts blocked: the SSR markup paints with the live sheets; hydration is
  // irrelevant to what the stylesheets declare.
  await open(page, url, { wait: 6000 });
  // inline sheets read via CSSOM; link sheets via the responses above
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u, t]).concat(inline);
  sheetsSeen[key] = sheets.map(([n, t]) => `${n} (${t.length} bytes)`);
  const found = await page.evaluate((sheets) => {
    // A custom property can hold a url() with a signed or per-account query: record it as url(…).
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    // The masked src of two faces can match (same family, weight and style, different files), so each face also keeps a hash of its src with the queries cut, only to tell them apart.
    const srcId = (v) => { let h = 5381; for (const ch of v.replace(/\?[^"')\s]*/g, '')) h = ((h << 5) + h + ch.charCodeAt(0)) | 0; return (h >>> 0).toString(36); };
    const res = [], ff = [];
    for (const [name, text] of sheets) {
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rules, media) => {
        for (const r of rules) {
          if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; }
          if (typeof CSSScopeRule !== 'undefined' && r instanceof CSSScopeRule) { walk(r.cssRules, [...media, `@scope (${r.start})`]); continue; }
          if (typeof CSSLayerBlockRule !== 'undefined' && r instanceof CSSLayerBlockRule) { walk(r.cssRules, [...media, `@layer ${r.name}`]); continue; }
          if (r instanceof CSSFontFaceRule) { ff.push({ family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), src: noUrl(r.style.getPropertyValue('src')), sid: srcId(r.style.getPropertyValue('src')), sheet: name }); continue; }
          if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; }
          if (!r.style) continue;
          for (const n of r.style) if (n.startsWith('--')) res.push({ sheet: name, selector: (r.selectorText || '').replace(/__[A-Za-z0-9_-]{5,6}\b/g, '').slice(0, 200), media: media.join(' and ') || null, name: n, value: noUrl(r.style.getPropertyValue(n).trim()) });
        }
      };
      walk(s.cssRules, []);
    }
    return { res, ff };
  }, sheets);
  for (const d of found.res) {
    const sheet = d.sheet.startsWith('inline-') ? 'inline' : d.sheet;
    const o = owner(d.name, d.selector, sheet);
    const k = [o, sheet, d.selector, d.media, d.name].join('|');
    const e = decls.get(k) || { owner: o, sheet, selector: d.selector, media: d.media, name: d.name, value: clean(d.value), pages: [] };
    if (!e.pages.includes(key)) e.pages.push(key);
    decls.set(k, e);
  }
  for (const f of found.ff) {
    const k = [f.family, f.weight, f.style, f.sid, clean(f.src).replace(/data:[^)]*/, 'data:…').slice(0, 300)].join('|');
    const { sid, ...face } = f;
    faces.set(k, { ...face, src: clean(f.src).replace(/url\("?data:[^)]*\)/g, 'url(data:…)').slice(0, 300), sheet: f.sheet.startsWith('inline-') ? 'inline' : f.sheet });
  }
  fontsLoaded[key] = await page.evaluate(() => [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => `${f.family.replace(/"/g, '')} ${f.weight} ${f.style}`))].sort());
  // dark theme: does anything set a theme attribute, and does the page change under prefers-color-scheme: dark?
  const sample = () => page.evaluate(() => [[100, 100], [700, 300], [720, 850], [1300, 450], [300, 600]].map(([x, y]) => {
    let n = document.elementFromPoint(x, y); const t = n; while (n && getComputedStyle(n).backgroundColor === 'rgba(0, 0, 0, 0)') n = n.parentElement;
    return (n ? getComputedStyle(n).backgroundColor : '-') + ' / ' + (t ? getComputedStyle(t).color : '-');
  }));
  const light = await sample();
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.waitForTimeout(1200);
  const dark = await sample();
  await page.emulateMedia({ colorScheme: 'light' });
  checks[key] = {
    body: await page.evaluate(() => [...document.body.attributes].map((a) => `${a.name}=${a.value}`)),
    themeAttributes: await page.evaluate(() => [...document.querySelectorAll('[data-theme],[data-theme-light],[data-theme-dark],[data-color-scheme],[data-mode]')].slice(0, 20).map((e) => `${e.tagName.toLowerCase()} ${['data-theme', 'data-theme-light', 'data-theme-dark', 'data-color-scheme', 'data-mode'].filter((a) => e.hasAttribute(a)).map((a) => `${a}=${e.getAttribute(a)}`).join(' ')}`)),
    prefersDarkChangesPage: JSON.stringify(light) !== JSON.stringify(dark),
    samplesLight: light, samplesDark: dark,
  };
  // Resolve every declared name under each theme the pages reference. The page
  // themes by element attribute — body carries data-theme-light="light-1", a
  // marketing band data-theme-light="marketing-3" — so each pass plants a probe
  // inside a div carrying that attribute, which is exactly how the bindings
  // ([data-theme-light=<name>] descends) apply on the real page.
  {
    const names = [...new Set([...decls.values()].map((d) => d.name))].sort();
    for (const theme of THEMES) {
      const out = await page.evaluate(([ns, theme]) => {
        const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
        const host = document.createElement('div');
        host.setAttribute('data-theme-light', theme);
        host.setAttribute('data-theme-dark', theme);
        host.setAttribute('type-style-theme', 'standard'); // the page's own type theme binding
        host.style.cssText = 'position:absolute;left:-9999px;top:0;width:10px;height:10px;visibility:hidden';
        document.body.appendChild(host);
        const cs = getComputedStyle(host);
        const out = Object.fromEntries(ns.map((n) => [n, noUrl(cs.getPropertyValue(n).trim())]).filter(([, v]) => v !== ''));
        host.remove();
        return out;
      }, [names, theme]);
      // later pages can carry sheets the first did not (vendor.css is only on
      // the results page): merge, first resolution wins
      resolved[theme] = { ...out, ...resolved[theme] };
      resolved[theme] = Object.fromEntries(Object.entries(resolved[theme]).sort());
    }
    // the painted context too: the values the page's own body resolves
    const paintedNow = await page.evaluate((ns) => {
      const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
      const cs = getComputedStyle(document.body);
      return Object.fromEntries(ns.map((n) => [n, noUrl(cs.getPropertyValue(n).trim())]).filter(([, v]) => v !== ''));
    }, names);
    resolved['painted'] = { ...paintedNow, ...(resolved['painted'] || {}) };
    console.log('resolved:', Object.fromEntries(Object.entries(resolved).map(([k, v]) => [k, Object.keys(v).length])));
  }
  await page.close();
}
await browser.close();
srv.close();

const sortKey = (d) => [d.owner, d.selector, d.media || '', d.name].join('|');
const all = [...decls.values()].sort((a, b) => (sortKey(a) < sortKey(b) ? -1 : 1));
const count = {};
for (const d of all) count[d.owner] = (count[d.owner] || 0) + 1;
const outFile = path.join(RAW, 'css-vars.json');
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(outFile, JSON.stringify({
  url: { product: 'https://www.expedia.com (PerimeterX 429; archived SSR + live travel-assets.com CSS)' }, read: new Date().toLocaleDateString('en-CA'), pages: { home: 'wayback 20260207171241 https://www.expedia.com/', search: 'wayback 20261030191926 https://www.expedia.com/Hotel-Search' }, counts: count,
  decls: all, resolved, fontFaces: [...faces.values()].sort((a, b) => (a.family + a.weight < b.family + b.weight ? -1 : 1)),
  fontsLoaded, themeChecks: checks, sheets: sheetsSeen,
}, null, 1) + '\n');
console.log(count, '->', outFile);
