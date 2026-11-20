// Dumps every custom property Airbnb's pages declare, by stylesheet, selector and
// media condition, sorted into who owns it, plus the font faces, the fonts that
// loaded, and the dark-theme checks.
//
//   PLAYWRIGHT=<path to playwright index.mjs> node vars.mjs     (writes raw/css-vars.json)
//
// airbnb.com serves its CSS from a0.muscache.com and inline <style> blocks; the
// link-served sheets read via CSSOM where allowed and through response bodies
// otherwise, parsed in the page with a constructed CSSStyleSheet, which reads
// them exactly as the browser does. Owners:
//   airbnb   airbnb.com/airbnb.com.sg sheets and inline styles: the site's own
//            variables (--overlay-*, --ebk-* and friends; the atm_* atomic CSS
//            puts almost every value inline on the rule instead)
//   amplify  the --amplify-* scale AWS Amplify widgets bring (a third-party
//            system the site embeds, kept apart so its palette is not mistaken
//            for Airbnb's)
//   other    anything a third-party sheet declares
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, RAW, firstRoomHref } from './public/lib.mjs';

const PAGES = {
  home: BASE + '/',
  search: BASE + '/s/Tokyo--Japan/homes',
  room: 'ROOM', // resolved to the first /rooms/<id> on the results page at runtime
  help: BASE + '/help',
  host: BASE + '/host/homes',
};
const clean = (s) => String(s)
  .replace(/(https?:\/\/[^\s"')?]+)\?[^\s"')]*/g, '$1')
  .replace(/url\(\s*["']?data:[^)]{80,}\)/g, 'url(data:…)');

function owner(name, selector, sheet) {
  if (name.startsWith('--amplify-') || /amplify|aws|amazonaws/.test(sheet)) return 'amplify';
  if (/airbnb|muscache/.test(sheet) || sheet.startsWith('inline')) return 'airbnb';
  return 'other';
}

const decls = new Map();
const faces = new Map();
const fontsLoaded = {};
const checks = {};
const resolved = {};
const sheetsSeen = {};

const { browser, context } = await launch();
const roomHref = await (async () => {
  const p = await context.newPage();
  await open(p, BASE + '/s/Tokyo--Japan/homes', { wait: 8000 });
  const h = await firstRoomHref(p);
  await p.close();
  return h;
})().catch(() => null);
for (const [key, url] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  const target = url === 'ROOM' ? (roomHref ? BASE + roomHref : null) : url;
  if (!target) { console.log('skip', key, '(no /rooms/ link found)'); await page.close(); continue; }
  console.log('open', key, target);
  await open(page, target, { wait: 9000 });
  // inline sheets read via CSSOM; link sheets via the responses above
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u, t]).concat(inline);
  sheetsSeen[key] = sheets.map(([n, t]) => `${n} (${t.length} bytes)`);
  const found = await page.evaluate((sheets) => {
    // A custom property can hold a url() with a signed or per-account query: record it as url(…).
    // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
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
    html: await page.evaluate(() => [...document.documentElement.attributes].map((a) => `${a.name}=${a.value}`)),
    themeAttributes: await page.evaluate(() => [...document.querySelectorAll('[data-theme],[data-color-scheme],[data-mode]')].slice(0, 20).map((e) => `${e.tagName.toLowerCase()} ${['data-theme', 'data-color-scheme', 'data-mode'].filter((a) => e.hasAttribute(a)).map((a) => `${a}=${e.getAttribute(a)}`).join(' ')}`)),
    prefersDarkChangesPage: JSON.stringify(light) !== JSON.stringify(dark),
    samplesLight: light, samplesDark: dark,
  };
  // the value each root variable resolves to on this page, at four widths
  const names = [...decls.values()].filter((d) => d.owner === 'airbnb' && /^(:root|html|html:root|:root, html|body)$/.test(d.selector) && !d.media).map((d) => d.name);
  if (names.length && key === 'home') {
    resolved[key] = {};
    for (const w of [390, 768, 1024, 1440]) {
      await page.setViewportSize({ width: w, height: 900 });
      await page.waitForTimeout(400);
      resolved[key][w] = await page.evaluate((ns) => { const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v); const cs = getComputedStyle(document.documentElement); return Object.fromEntries([...new Set(ns)].sort().map((n) => [n, noUrl(cs.getPropertyValue(n).trim())])); }, names);
    }
    await page.setViewportSize({ width: 1440, height: 900 });
  }
  await page.close();
}
await browser.close();

const sortKey = (d) => [d.owner, d.selector, d.media || '', d.name].join('|');
const all = [...decls.values()].sort((a, b) => (sortKey(a) < sortKey(b) ? -1 : 1));
const count = {};
for (const d of all) count[d.owner] = (count[d.owner] || 0) + 1;
const outFile = path.join(RAW, 'css-vars.json');
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(outFile, JSON.stringify({
  url: { product: BASE }, read: new Date().toLocaleDateString('en-CA'), pages: PAGES, counts: count,
  decls: all, resolved, fontFaces: [...faces.values()].sort((a, b) => (a.family + a.weight < b.family + b.weight ? -1 : 1)),
  fontsLoaded, themeChecks: checks, sheets: sheetsSeen,
}, null, 1) + '\n');
console.log(count, '->', outFile);
