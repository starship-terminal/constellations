// Read custom properties from scale.com's live public pages.
// Scale serves CSS from its own origin (Next.js). Cross-origin sheets are
// collected from network responses and parsed with a constructed CSSStyleSheet.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, open, RAW, BASE } from './public/lib.mjs';

const PAGES = {
  home: '/',
  demo: '/demo',
  docs: '/docs',
  enterprise: '/enterprise',
  blog: '/blog',
};

const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)')
  : v);

const { browser, context } = await launch({ width: 1440, height: 900 });
const decls = new Map();
const faces = new Map();
const resolved = {};
const computed = {};
const fontsLoaded = {};
const themeChecks = {};

for (const [key, pth] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  const pending = [];
  page.on('response', (r) => {
    const type = r.request().resourceType();
    if (type !== 'stylesheet') return;
    pending.push(r.text().then((t) => { bodies.set(r.url().split('?')[0], t); }, () => {}));
  });
  console.log('open', key);
  await open(page, BASE + pth, { wait: 2500 });
  await Promise.race([Promise.all(pending), page.waitForTimeout(8000)]);
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
    try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; }
    catch { return null; }
  }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u.replace(/^https?:\/\/[^/]+/, ''), t]).concat(inline);
  console.log('  sheets', sheets.length, 'bytes', sheets.reduce((n, s) => n + s[1].length, 0));
  const found = await page.evaluate((sheets) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const res = [];
    const ff = [];
    for (const [name, text] of sheets) {
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rules, media) => {
        for (const r of rules) {
          if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; }
          if (r instanceof CSSFontFaceRule) {
            ff.push({
              family: r.style.getPropertyValue('font-family').replace(/["']/g, ''),
              weight: r.style.getPropertyValue('font-weight'),
              style: r.style.getPropertyValue('font-style'),
              src: noUrl(r.style.getPropertyValue('src')).slice(0, 180),
              sheet: name,
            });
            continue;
          }
          if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; }
          if (!r.style) continue;
          for (const n of r.style) {
            if (n.startsWith('--')) res.push({
              sheet: name,
              selector: r.selectorText || '',
              media: media.join(' and ') || null,
              name: n,
              value: noUrl(r.style.getPropertyValue(n).trim()),
            });
          }
        }
      };
      walk(s.cssRules, []);
    }
    return { res, ff };
  }, sheets);
  for (const d of found.res) {
    const k = [d.sheet, d.selector, d.media, d.name].join('|');
    const e = decls.get(k) || { ...d, value: noUrl(d.value), pages: [] };
    if (!e.pages.includes(key)) e.pages.push(key);
    decls.set(k, e);
  }
  for (const f of found.ff) faces.set([f.family, f.weight, f.style, f.src].join('|'), f);

  const rootVars = await page.evaluate(() => {
    const cs = getComputedStyle(document.documentElement);
    const names = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        for (const r of list) {
          if (r.cssRules && !r.style) { try { walk(r.cssRules); } catch {} continue; }
          if (!r.style) continue;
          for (const n of r.style) if (n.startsWith('--') && !names.includes(n)) names.push(n);
        }
      };
      try { walk(rules); } catch {}
    }
    // Also collect names already seen on the element style.
    const out = {};
    for (const n of names) {
      const v = cs.getPropertyValue(n).trim();
      if (v) out[n] = v;
    }
    return out;
  });
  resolved[key] = rootVars;

  computed[key] = await page.evaluate(() => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        selector: sel,
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
        rect: { w: Math.round(r.width), h: Math.round(r.height) },
        color: s.color,
        backgroundColor: s.backgroundColor,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        borderTopWidth: s.borderTopWidth,
        borderTopColor: s.borderTopColor,
        padding: `${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`,
        boxShadow: s.boxShadow,
      };
    };
    return {
      body: pick('body'),
      h1: pick('h1'),
      header: pick('header'),
      primary: pick('a[href="/demo"], a[href="https://scale.com/demo"]'),
      navButton: pick('header button'),
    };
  });

  fontsLoaded[key] = await page.evaluate(() => [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => `${f.family.replace(/"/g, '')} ${f.weight}`))].sort());

  const sample = () => page.evaluate(() => [[80, 40], [200, 200], [720, 450]].map(([x, y]) => {
    let n = document.elementFromPoint(x, y);
    while (n && getComputedStyle(n).backgroundColor === 'rgba(0, 0, 0, 0)') n = n.parentElement;
    return n ? getComputedStyle(n).backgroundColor : '-';
  }));
  const light = await sample();
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.waitForTimeout(600);
  const dark = await sample();
  themeChecks[key] = {
    prefersDarkChangesPage: JSON.stringify(light) !== JSON.stringify(dark),
    samplesLight: light,
    samplesDark: dark,
    themeColor: await page.evaluate(() => document.querySelector('meta[name="theme-color"]')?.content || null),
  };
  await page.close();
}
await browser.close();

fs.mkdirSync(RAW, { recursive: true });
const out = {
  url: BASE,
  read: '2026-11-21',
  pages: PAGES,
  declCount: decls.size,
  decls: [...decls.values()].sort((a, b) => (a.name + a.selector).localeCompare(b.name + b.selector)),
  resolved,
  computed,
  fontFaces: [...faces.values()],
  fontsLoaded,
  themeChecks,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('decls', decls.size, 'fonts', [...faces.values()].map((f) => f.family).filter((v, i, a) => a.indexOf(v) === i));
console.log('theme', JSON.stringify(themeChecks.home));
