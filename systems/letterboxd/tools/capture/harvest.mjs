// Live harvest of letterboxd.com custom properties, computed roles, and nav.
// Writes raw/css-vars.json and raw/harvest.json. Nothing is typed or submitted.
const ADAPTED_FOR = 'letterboxd';

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const sheets = [];
page.on('response', async (res) => {
  const ct = res.headers()['content-type'] || '';
  const url = res.url();
  if (!/text\/css|stylesheet/i.test(ct) && !url.endsWith('.css')) return;
  try {
    const body = await res.text();
    if (body && body.length > 40) sheets.push({ url: url.split('?')[0].slice(0, 180), bytes: body.length, css: body });
  } catch {}
});

await page.goto('https://letterboxd.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);

const live = await page.evaluate(() => {
  const noUrl = (v) => String(v).replace(/url\((?!\s*['"]?(?:data:|#))[^)]*\)/gi, 'url(…)');
  const declared = [];
  const fonts = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = [...sheet.cssRules]; } catch { continue; }
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = {};
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const kind = r.constructor.name.replace('CSS', '').replace('Rule', '');
          const extra = r.conditionText ? `@${kind.toLowerCase()} ${r.conditionText}` : (r.name ? `@${kind.toLowerCase()} ${r.name}` : '');
          walk([...r.cssRules], extra ? ctx.concat(extra) : ctx);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const n = r.style[i];
          if (n.startsWith('--')) props[n] = noUrl(r.style.getPropertyValue(n).trim());
        }
        if (Object.keys(props).length) declared.push({ selector: r.selectorText, context: ctx, properties: props });
      }
    };
    walk(rules, []);
  }
  const root = getComputedStyle(document.documentElement);
  const names = new Set(declared.flatMap((d) => Object.keys(d.properties)));
  const resolved = {};
  for (const n of names) {
    const v = root.getPropertyValue(n).trim();
    if (v) resolved[n] = noUrl(v);
  }
  const pick = (sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      sel,
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      w: Math.round(r.width),
      h: Math.round(r.height),
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      textTransform: cs.textTransform,
      borderRadius: cs.borderRadius,
      padding: cs.padding,
      borderTop: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
      boxShadow: cs.boxShadow,
    };
  };
  const body = getComputedStyle(document.body);
  const roles = {
    body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize, lineHeight: body.lineHeight },
    logo: pick('a.logo'),
    navlink: pick('a.navlink'),
    search: pick('#search-q'),
    searchSubmit: pick('#search input[type=submit]'),
    footer: pick('#page-footer'),
    h1: pick('h1'),
    h2: pick('h2'),
    cta: pick('a[href="/create-account/"]'),
  };
  return {
    title: document.title,
    lang: document.documentElement.lang,
    innerWidth: innerWidth,
    innerHeight: innerHeight,
    dpr: devicePixelRatio,
    themeColor: document.querySelector('meta[name=theme-color]')?.content || null,
    declared,
    fonts,
    resolved,
    roles,
  };
});

const cssPath = path.join(RAW, 'css-vars.json');
const out = {
  source: 'live signed-out load of https://letterboxd.com/ at 1440 x 900. Custom properties read from the CSSOM. The site paints one dark field. No theme switch was found in the header or footer.',
  product: ADAPTED_FOR,
  capturedAt: new Date().toISOString(),
  viewport: { width: live.innerWidth, height: live.innerHeight, dpr: live.dpr },
  themeColor: live.themeColor,
  counts: {
    rules: live.declared.length,
    names: Object.keys(live.resolved).length,
    fonts: live.fonts.length,
    stylesheetsFetched: sheets.length,
  },
  resolved: { light: live.resolved, dark: {} },
  rules: live.declared,
  fonts: live.fonts,
};
fs.writeFileSync(cssPath, JSON.stringify(out, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'harvest.json'), JSON.stringify({ roles: live.roles, title: live.title, lang: live.lang, themeColor: live.themeColor }, null, 1) + '\n');
console.log('rules', live.declared.length, 'names', Object.keys(live.resolved).length, 'fonts', live.fonts.length, 'sheets', sheets.length);
console.log('body', JSON.stringify(live.roles.body));
console.log('nav', JSON.stringify(live.roles.navlink));
await browser.close();
