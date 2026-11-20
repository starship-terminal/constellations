// Harvest resolved custom properties from forhims.co.uk into raw/css-vars.json.
// PLAYWRIGHT=... node harvest-vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, RAW, hideConsent, launchBrowser, newContext, open } from './lib.mjs';

const OUT = path.join(RAW, 'css-vars.json');
fs.mkdirSync(RAW, { recursive: true });

const browser = await launchBrowser();
const ctx = await newContext(browser, { width: 1440, height: 900, dpr: 1 });
const page = await ctx.newPage();
await open(page, BASE + '/', { wait: 2000 });
await hideConsent(page);

const data = await page.evaluate(() => {
  // A url() can carry a signed asset URL: record it as url(…), as the kit and the sibling forks do.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const names = new Set();
  const declared = [];
  const walk = (list, context) => {
    if (!list) return;
    for (const r of list) {
      if (r.type === CSSRule.STYLE_RULE && r.style) {
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const n = r.style[i];
          if (n.startsWith('--')) {
            names.add(n);
            props[n] = noUrl(r.style.getPropertyValue(n).trim());
          }
        }
        if (Object.keys(props).length) declared.push({ selector: r.selectorText, context, properties: props });
      }
      if (r.cssRules) {
        const media = r.conditionText || r.media?.mediaText || '';
        walk(r.cssRules, media ? [...context, media] : context);
      }
    }
  };
  let sheets = 0, blocked = 0;
  for (const sheet of document.styleSheets) {
    sheets++;
    try { walk(sheet.cssRules, []); } catch { blocked++; }
  }
  const cs = getComputedStyle(document.documentElement);
  const resolved = {};
  for (const n of names) {
    const v = cs.getPropertyValue(n).trim();
    if (v) resolved[n] = noUrl(v);
  }
  const fonts = [];
  for (const f of document.fonts) fonts.push({ family: f.family, weight: String(f.weight), style: f.style, status: f.status });
  return {
    url: location.href.split('?')[0],
    htmlClass: document.documentElement.className,
    sheets, blocked,
    viewport: { innerWidth, innerHeight, dpr: devicePixelRatio },
    fonts,
    resolved,
    declaredCount: declared.length,
    declared: declared.slice(0, 80),
  };
});

const payload = {
  product: 'hims',
  host: 'www.forhims.co.uk',
  captured: new Date().toISOString(),
  theme: 'light',
  note: 'UK marketing site paints one light theme (html.brand-hims.variant-care-sans). No dark theme switch was found. Ketch consent was hidden, never clicked.',
  url: data.url,
  htmlClass: data.htmlClass,
  sheets: data.sheets,
  blocked: data.blocked,
  viewport: data.viewport,
  fonts: data.fonts,
  resolved: { light: data.resolved },
  declaredCount: data.declaredCount,
  declaredSample: data.declared,
};
fs.writeFileSync(OUT, JSON.stringify(payload, null, 2));
console.log('wrote', OUT, 'props', Object.keys(data.resolved).length, 'sheets', data.sheets, 'blocked', data.blocked);
await browser.close();
