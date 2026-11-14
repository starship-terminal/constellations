// Dumps every custom property Gauth's pages declare, by stylesheet, selector and
// media condition, sorted into who owns it, plus the font faces, the fonts that
// loaded, and the dark-theme checks.
//
//   PLAYWRIGHT=<path to playwright index.mjs> node vars.mjs     (writes raw/css-vars.json)
//
// Gauth's own CSS sits on a CDN, so the CSSOM refuses to read it cross-origin. The
// script keeps every stylesheet response body and parses it in the page with a
// constructed CSSStyleSheet, which reads it exactly as the browser does. Owners:
//   gauth    Gauth's own variables (--lesson-*, --ugc-lesson-*, --pc-side-menu-*, --md-*, ...)
//   antd     Ant Design's CSS-variable theme (--ant-*), written by its CSS-in-JS
//   tux      TikTok's TUX theme (:root, [data-theme="light"] / [data-theme="dark"], .twv-container)
//   astryx   Astryx, the design system the science lesson canvas is built in (astryx-* classes, StyleX
//            `.x…, :root` variable rules, the "stone" theme in @scope ([data-astryx-theme="stone"]))
//   antd-mobile, swiper, katex   third-party defaults
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, RAW, drain } from './lib.mjs';

const PAGES = {
  home: '/', academy: '/course/science', unit: '/course/math/algebra-1?unit=real-numbers-and-sets',
  'lesson-science': '/course/science/how-things-work-1/learn?entry_source=start&from=science',
  'lesson-math': '/course/math/algebra-1/fundamentals-of-set-theory/learn?entry_source=start&return_to=course_detail',
  'lesson-history': '/course/history/crossing-the-ocean-wall/learn?entry_source=start&from=history',
  atlas: '/atlas', news: '/news',
};
const clean = (s) => String(s)
  .replace(/(https?:\/\/[^\s"')?]+)\?[^\s"')]*/g, '$1')
  .replace(/url\(\s*["']?data:[^)]{80,}\)/g, 'url(data:…)');

function owner(name, selector, media) {
  if (name.startsWith('--ant-')) return 'antd';
  if (/data-astryx-theme/.test(media || '') || /^\.x[0-9a-z]{5,8}, :root$/.test(selector) || /astryx/.test(selector) || name.startsWith('--color-data-')) return 'astryx';
  if (name.startsWith('--adm-')) return 'antd-mobile';
  if (name.startsWith('--swiper')) return 'swiper';
  if (name.startsWith('--katex')) return 'katex';
  if (/data-theme|twv-container|tux-/.test(selector) || name.startsWith('--tux-')) return 'tux';
  return 'gauth';
}

const decls = new Map();
const faces = new Map();
const fontsLoaded = {};
const checks = {};
const resolved = {};
const sheetsSeen = {};

const { browser, context } = await launch();
for (const [key, p] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  // Each body is read asynchronously; the reads, late ones included, are awaited after the page opens
  // (settled() below, bounded by drain()), so a sheet still in flight is not silently left out.
  const pending = [];
  page.on('response', (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    pending.push(r.text().then((t) => { bodies.set(r.url().split('?')[0], t); }, () => { /* body gone */ }));
  });
  const settled = async () => {
    if (!(await drain(pending))) console.log('  ! some stylesheet bodies did not finish within 15s');
    const hrefs = await page.evaluate(() => [...document.styleSheets].map((s) => s.href).filter(Boolean));
    return [...new Set(hrefs.map((h) => h.split('?')[0]).filter((h) => !bodies.has(h)))];
  };
  console.log('open', key);
  await open(page, BASE + p, { wait: 7000 });
  const unread = await settled();
  if (unread.length) console.log('  ! stylesheets the page loaded but whose body was not read:', unread.join(', '));
  // inline sheets (CSS-in-JS) are readable through the CSSOM directly
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u.replace(/^https?:\/\/[^/]+/, '').replace(/^.*\/static\/css\//, 'css/'), t]).concat(inline);
  sheetsSeen[key] = sheets.map(([n, t]) => `${n} (${t.length} bytes)`).concat(unread.map((u) => `${u} (body not read)`));
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
          if (r instanceof CSSFontFaceRule) { ff.push({ family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), src: noUrl(r.style.getPropertyValue('src')), sid: srcId(r.style.getPropertyValue('src')), sheet: name }); continue; }
          if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; }
          if (!r.style) continue;
          for (const n of r.style) if (n.startsWith('--')) res.push({ sheet: name, selector: (r.selectorText || '').replace(/__[A-Za-z0-9_-]{5,6}\b/g, ''), media: media.join(' and ') || null, name: n, value: noUrl(r.style.getPropertyValue(n).trim()) });
        }
      };
      walk(s.cssRules, []);
    }
    return { res, ff };
  }, sheets);
  for (const d of found.res) {
    const sheet = d.sheet.startsWith('inline-') ? 'inline' : d.sheet;
    const o = owner(d.name, d.selector, d.media);
    const k = [o, sheet, d.selector, d.media, d.name].join('|');
    const e = decls.get(k) || { owner: o, sheet, selector: d.selector, media: d.media, name: d.name, value: clean(d.value), pages: [] };
    if (!e.pages.includes(key)) e.pages.push(key);
    decls.set(k, e);
  }
  for (const f of found.ff) {
    if (/^KaTeX_/.test(f.family)) { faces.set('KaTeX', { family: 'KaTeX_* (20 faces)', weight: '400 700', style: 'normal italic', src: 'KaTeX fonts', sheet: f.sheet }); continue; }
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
    themeAttributes: await page.evaluate(() => [...document.querySelectorAll('[data-theme],[data-lesson-style],[data-color-scheme]')].map((e) => `${e.tagName.toLowerCase()}.${String(e.className).split(' ')[0].replace(/__[\w-]{5,6}$/, '')} ${['data-theme', 'data-lesson-style', 'data-color-scheme'].filter((a) => e.hasAttribute(a)).map((a) => `${a}=${e.getAttribute(a)}`).join(' ')}`)),
    prefersDarkChangesPage: JSON.stringify(light) !== JSON.stringify(dark),
    samplesLight: light, samplesDark: dark,
  };
  // the value each Gauth root variable resolves to on this page, at four widths
  const names = [...decls.values()].filter((d) => d.owner === 'gauth' && /^(:root|html:root|:root, html:root|:root, \[data-lesson-style="light"\])$/.test(d.selector) && !d.media).map((d) => d.name);
  if (key === 'academy' || key === 'lesson-math') {
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
fs.writeFileSync(outFile, JSON.stringify({
  url: BASE, read: new Date().toLocaleDateString('en-CA'), pages: PAGES, counts: count,
  decls: all, resolved, fontFaces: [...faces.values()].sort((a, b) => (a.family + a.weight < b.family + b.weight ? -1 : 1)),
  fontsLoaded, themeChecks: checks, sheets: sheetsSeen,
}, null, 1) + '\n');
console.log(count, '->', outFile);
