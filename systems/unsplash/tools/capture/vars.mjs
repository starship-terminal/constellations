// Read custom properties and computed foundation colours from unsplash.com.
// Headed Chromium: headless stops on the Anubis check.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, open } from './public/lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');

const PAGES = {
  home: BASE + '/',
  plus: BASE + '/plus',
  about: BASE + '/about',
  login: BASE + '/login',
  developers: BASE + '/developers',
};

const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  locale: 'en-US',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });

const decls = [];
const faces = [];
const computed = {};
const sheetsSeen = {};

for (const [key, url] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    const rt = r.request().resourceType();
    if (rt !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
  });
  console.log('open', key, url);
  await open(page, url, { wait: 2000 });
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
    try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
  }).filter(Boolean));
  const sheets = [...bodies.entries(), ...inline];
  sheetsSeen[key] = sheets.map(([n, t]) => `${n} (${(t || '').length})`);
  const found = await page.evaluate((sheets) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]{40,}\)/g, 'url(…)') : v);
    const res = [];
    const ff = [];
    for (const [name, text] of sheets) {
      if (!text) continue;
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rules, media) => {
        for (const r of rules) {
          if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; }
          if (r.style) {
            for (const prop of r.style) {
              if (prop.startsWith('--')) res.push({ name: prop, value: noUrl(r.style.getPropertyValue(prop).trim()), selector: r.selectorText, media: media.join(' and ') || null, sheet: name });
            }
          }
          if (r instanceof CSSFontFaceRule) {
            ff.push({ family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), sheet: name });
          }
          if (r.cssRules && !(r instanceof CSSMediaRule)) walk(r.cssRules, media);
        }
      };
      walk(s.cssRules, []);
    }
    return { res, ff };
  }, sheets);
  for (const d of found.res) decls.push({ ...d, page: key });
  for (const f of found.ff) faces.push({ ...f, page: key });

  computed[key] = await page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const cs = getComputedStyle(el);
      return {
        tag: el.tagName.toLowerCase(),
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        color: cs.color,
        backgroundColor: cs.backgroundColor,
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        borderRadius: cs.borderRadius,
        borderTopColor: cs.borderTopColor,
        boxShadow: cs.boxShadow,
      };
    };
    const body = getComputedStyle(document.body);
    const rootVars = {};
    const csRoot = getComputedStyle(document.documentElement);
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (rs) => {
        for (const r of rs) {
          if (r.style) for (const n of r.style) if (n.startsWith('--') && !(n in rootVars)) rootVars[n] = csRoot.getPropertyValue(n).trim();
          if (r.cssRules) walk(r.cssRules);
        }
      };
      walk(rules);
    }
    const roles = {
      body: { color: body.color, backgroundColor: body.backgroundColor, fontFamily: body.fontFamily, fontSize: body.fontSize, lineHeight: body.lineHeight },
      h1: pick(document.querySelector('h1')),
      h2: pick(document.querySelector('h2')),
      link: pick(document.querySelector('header a, a')),
      button: pick([...document.querySelectorAll('a, button')].find((el) => /submit an image|get unsplash\+|upgrade|log in/i.test(el.innerText || '') && el.getBoundingClientRect().width > 40)),
      search: pick(document.querySelector('input[name="searchKeyword"]')),
    };
    return {
      colorScheme: csRoot.colorScheme,
      dataTheme: document.documentElement.getAttribute('data-theme'),
      className: document.documentElement.className.slice(0, 160),
      rootVars,
      roles,
      fonts: [...document.fonts].slice(0, 20).map((f) => ({ family: f.family, weight: f.weight, status: f.status })),
      viewport: { innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio },
    };
  });
  console.log('  vars', Object.keys(computed[key].rootVars).length, 'font', computed[key].roles.body.fontFamily);
  await page.close();
}

const byName = {};
for (const d of decls) {
  if (!byName[d.name]) byName[d.name] = d;
}
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify({
  read: new Date().toISOString().slice(0, 10),
  source: 'https://unsplash.com headed Chromium, public pages, light only',
  sheetsSeen,
  declCount: decls.length,
  uniqueNames: Object.keys(byName).length,
  decls: Object.values(byName),
  faces,
  computed,
}, null, 1) + '\n');
console.log('wrote', OUT, 'unique', Object.keys(byName).length);
await browser.close();
