// Read custom properties from Patreon's public stylesheets and write raw/css-vars.json.
// Cross-origin sheets are kept from the network response and parsed with a constructed CSSStyleSheet.
// Login, signup and form submit are never used.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const PAGES = {
  'home-app': 'https://www.patreon.com/',
  explore: 'https://www.patreon.com/explore',
  pricing: 'https://www.patreon.com/pricing',
  'product-create': 'https://www.patreon.com/product/create',
  creator: 'https://www.patreon.com/cw/GlamorousTrash',
  help: 'https://support.patreon.com/hc/en-us',
};

const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);

function owner(name, selector) {
  if (name.startsWith('--studio-') || name.startsWith('--global-') || /studio/i.test(selector)) return 'studio';
  if (name.startsWith('--zd-') || /zendesk/i.test(selector)) return 'zendesk';
  return 'patreon';
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });

const decls = new Map();
const faces = new Map();
const fontsLoaded = {};
const checks = {};
const resolved = {};
const brand = {};
const sheetsSeen = {};

for (const [key, url] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  const pending = [];
  page.on('response', (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    pending.push(r.text().then((t) => { bodies.set(r.url().split('?')[0], t); }, () => {}));
  });
  console.log('open', key);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await page.waitForTimeout(2500);
  } catch (e) {
    console.log('  FAILED', key, String(e.message || e).split('\n')[0]);
    await page.close();
    continue;
  }
  if (await page.locator('input[type="password"]').count()) {
    console.log('  wall, skipped', page.url());
    await page.close();
    continue;
  }
  await Promise.race([Promise.all(pending), page.waitForTimeout(8000)]);
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
    try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
  }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u.replace(/^https?:\/\/[^/]+/, ''), t]).concat(inline);
  sheetsSeen[key] = sheets.map(([n, t]) => `${n} (${t.length})`);
  const found = await page.evaluate((sheets) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const res = [], ff = [];
    for (const [name, text] of sheets) {
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rules, media) => {
        for (const r of rules) {
          if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; }
          if (r instanceof CSSFontFaceRule) {
            ff.push({ family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), sheet: name });
            continue;
          }
          if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; }
          if (!r.style) continue;
          for (const n of r.style) if (n.startsWith('--')) res.push({ sheet: name.slice(0, 80), selector: (r.selectorText || '').slice(0, 180), media: media.join(' and ') || null, name: n, value: noUrl(r.style.getPropertyValue(n).trim()).slice(0, 300) });
        }
      };
      walk(s.cssRules, []);
    }
    return { res, ff };
  }, sheets);
  for (const d of found.res) {
    const o = owner(d.name, d.selector);
    const k = [o, d.selector, d.media, d.name, d.value].join('|');
    const e = decls.get(k) || { owner: o, selector: d.selector, media: d.media, name: d.name, value: d.value, pages: [] };
    if (!e.pages.includes(key)) e.pages.push(key);
    decls.set(k, e);
  }
  for (const f of found.ff) {
    const k = [f.family, f.weight, f.style].join('|');
    faces.set(k, f);
  }
  fontsLoaded[key] = await page.evaluate(() => [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => `${f.family.replace(/"/g, '')} ${f.weight} ${f.style}`))].sort());
  brand[key] = await page.evaluate(() => ({
    title: document.title,
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
    themeColorDark: document.querySelector('meta[name="theme-color"][media*="dark"]')?.content || null,
    mask: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  }));
  const sample = () => page.evaluate(() => [[80, 80], [720, 200], [200, 700]].map(([x, y]) => {
    let n = document.elementFromPoint(x, y);
    while (n && getComputedStyle(n).backgroundColor === 'rgba(0, 0, 0, 0)') n = n.parentElement;
    return n ? getComputedStyle(n).backgroundColor : '-';
  }));
  const light = await sample();
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.waitForTimeout(800);
  const dark = await sample();
  await page.emulateMedia({ colorScheme: 'light' });
  checks[key] = { prefersDarkChangesPage: JSON.stringify(light) !== JSON.stringify(dark), samplesLight: light, samplesDark: dark, htmlClass: await page.evaluate(() => document.documentElement.className.slice(0, 160)) };
  const rootNames = [...decls.values()].filter((d) => /:root|html/.test(d.selector) && !d.media).map((d) => d.name);
  resolved[key] = await page.evaluate((ns) => {
    const cs = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    return {
      root: Object.fromEntries([...new Set(ns)].sort().slice(0, 400).map((n) => [n, cs.getPropertyValue(n).trim()])),
      body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize },
    };
  }, rootNames.slice(0, 400));
  await page.close();
}
await browser.close();

const all = [...decls.values()].sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
const counts = {};
for (const d of all) counts[d.owner] = (counts[d.owner] || 0) + 1;
const outFile = path.join(RAW, 'css-vars.json');
fs.writeFileSync(outFile, JSON.stringify({
  read: new Date().toISOString().slice(0, 10),
  pages: PAGES,
  counts,
  decls: all,
  resolved,
  fontFaces: [...faces.values()].sort((a, b) => (a.family < b.family ? -1 : 1)),
  fontsLoaded,
  themeChecks: checks,
  brand,
  sheets: sheetsSeen,
}, null, 1) + '\n');
console.log(counts, 'decls', all.length, '->', outFile);
