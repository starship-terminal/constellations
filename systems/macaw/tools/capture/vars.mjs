// Reads every custom property macawhq.com's stylesheets declare and writes
// raw/css-vars.json. Public Webflow site, one light theme, live CSSOM.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);

const result = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.STYLE_RULE) {
        const props = {};
        for (const name of r.style) {
          if (name.startsWith('--')) props[name] = noUrl(r.style.getPropertyValue(name).trim());
        }
        if (Object.keys(props).length) rules.push({ selector: r.selectorText, context: ctx, file, properties: props });
      } else if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({
          family: (r.style.getPropertyValue('font-family') || '').replace(/['"]/g, ''),
          weight: r.style.getPropertyValue('font-weight'),
          style: r.style.getPropertyValue('font-style'),
          file,
        });
      } else if (r.cssRules) {
        const cond = r.conditionText || r.name || r.media?.mediaText || '';
        walk(r.cssRules, ctx.concat(cond), file);
      }
    }
  };
  for (const sheet of document.styleSheets) {
    let list;
    try { list = sheet.cssRules; } catch { continue; }
    const file = sheet.href ? new URL(sheet.href).pathname.split('/').pop() : 'inline';
    walk(list, [], file);
  }
  const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))].sort();
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:-9999px;top:0';
  document.body.appendChild(probe);
  const resolved = {};
  for (const name of names) {
    const raw = getComputedStyle(document.documentElement).getPropertyValue(name).trim()
      || getComputedStyle(probe).getPropertyValue(name).trim();
    resolved[name] = raw;
  }
  probe.remove();
  const meta = {
    themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.media })),
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
    title: document.title,
  };
  return { rules, fonts, names, resolved, meta };
});

const out = {
  product: 'macaw',
  url: BASE + '/',
  captured: new Date().toISOString().slice(0, 10),
  theme: 'light',
  note: 'Public Webflow marketing site. Custom properties are whatever the published CSS declares. Design colours mostly live on classes, measured in components-computed.json.',
  meta: result.meta,
  names: result.names,
  resolved: result.resolved,
  fonts: result.fonts,
  rules: result.rules,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('vars', result.names.length, 'fonts', result.fonts.length, 'rules', result.rules.length);
await browser.close();
