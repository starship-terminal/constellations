// Read custom properties, font faces, and a few computed roles from live public pages.
// Writes raw/css-vars.json. Does not type, submit, or follow a login wall.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(here, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const sheets = [];
page.on('response', async (res) => {
  const url = res.url();
  const ct = res.headers()['content-type'] || '';
  if (!/text\/css|stylesheet/.test(ct) && !url.includes('.css')) return;
  if (res.status() !== 200) return;
  try {
    const css = await res.text();
    if (css && css.length > 40) sheets.push({ url: url.split('?')[0].slice(0, 180), bytes: css.length, css });
  } catch { /* cross-origin body unavailable */ }
});

await page.goto('https://ifttt.ai/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(2500);

const live = await page.evaluate(async () => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)') : v);
  const vars = {};
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.cssRules && !r.style) {
        const head = r.cssText.split('{')[0].trim().slice(0, 160);
        try { walk(r.cssRules, [...ctx, head]); } catch { /* cross-origin sheet */ }
        continue;
      }
      if (!r.style) continue;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (!k.startsWith('--')) continue;
        const raw = r.style.getPropertyValue(k).trim();
        (vars[k] ||= []).push({ selector: (r.selectorText || '').slice(0, 180), context: ctx.slice(-3), raw: noUrl(raw).slice(0, 240) });
      }
    }
  };
  const fonts = [];
  for (const sheet of document.styleSheets) {
    let href = '';
    try { href = sheet.href || 'inline'; } catch { href = 'cross-origin'; }
    try { walk(sheet.cssRules, [href.slice(0, 120)]); } catch { /* inaccessible */ }
    try {
      for (const r of sheet.cssRules) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family'),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
            display: r.style.getPropertyValue('font-display'),
            src: noUrl(r.style.getPropertyValue('src')).slice(0, 180),
          });
        }
      }
    } catch { /* inaccessible */ }
  }
  const root = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  const names = [...root].filter((n) => n.startsWith('--'));
  const computed = {};
  for (const n of names) computed[n] = root.getPropertyValue(n).trim().slice(0, 200);
  const sample = (sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const s = getComputedStyle(el);
    return {
      sel,
      color: s.color,
      backgroundColor: s.backgroundColor,
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      borderRadius: s.borderRadius,
      padding: s.padding,
    };
  };
  return {
    title: document.title,
    url: location.href,
    varDeclCount: Object.keys(vars).length,
    vars,
    fonts: fonts.slice(0, 40),
    rootComputed: computed,
    body: {
      color: body.color,
      backgroundColor: body.backgroundColor,
      fontFamily: body.fontFamily,
      fontSize: body.fontSize,
      lineHeight: body.lineHeight,
    },
    samples: {
      h1: sample('h1'),
      link: sample('header a'),
      button: sample('button.button-primary, a.button-primary, .button-primary'),
    },
  };
});

await browser.close();

const out = {
  capturedAt: new Date().toISOString(),
  page: { url: live.url, title: live.title },
  stylesheetCount: sheets.length,
  stylesheetBytes: sheets.reduce((n, s) => n + s.bytes, 0),
  stylesheets: sheets.map((s) => ({ url: s.url, bytes: s.bytes })),
  declared: live.vars,
  rootComputed: live.rootComputed,
  fonts: live.fonts,
  body: live.body,
  samples: live.samples,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2));
console.log('stylesheets', sheets.length, 'bytes', out.stylesheetBytes);
console.log('declared vars', live.varDeclCount);
console.log('root computed', Object.keys(live.rootComputed).length);
console.log('fonts', live.fonts.length);
console.log('body', JSON.stringify(live.body));
console.log('samples', JSON.stringify(live.samples));
const names = Object.keys(live.vars).slice(0, 40);
console.log('var names', names.join(', '));
