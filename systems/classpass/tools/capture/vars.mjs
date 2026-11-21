// Reads every custom property classpass.com's stylesheets declare and writes
// raw/css-vars.json. Live CSSOM on the public home page, light theme only.
// Cross-origin sheets that the CSSOM cannot read are listed under skipped.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(3000);
await hideConsent(page);

const result = await page.evaluate(() => {
  const rules = [];
  const fonts = [];
  const skipped = [];
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.constructor.name === 'CSSContainerRule' ? '@container ' + r.conditionText
          : r.cssText.split('{')[0].trim().slice(0, 120);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 160), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  [...document.styleSheets].forEach((ss, i) => {
    const file = ss.href ? ss.href.split('/').pop().split('?')[0] || ss.href : `inline-${i}`;
    try { walk(ss.cssRules, [], file); } catch { skipped.push(file); }
  });
  const root = getComputedStyle(document.documentElement);
  const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))].sort();
  const resolved = {};
  for (const n of names) resolved[n] = root.getPropertyValue(n).trim();
  return {
    rules, fonts, skipped, resolved, names,
    colorScheme: root.colorScheme,
    fontFamily: root.fontFamily,
    background: root.backgroundColor,
    color: root.color,
    hrefs: [...document.styleSheets].map((ss) => ss.href || 'inline'),
  };
});

const out = {
  product: 'ClassPass',
  url: 'https://classpass.com/',
  captured: new Date().toISOString(),
  theme: 'light',
  note: 'Public marketing site. No dark theme switch was found on the captured pages.',
  colorScheme: result.colorScheme,
  rootFontFamily: result.fontFamily,
  rootBackground: result.background,
  rootColor: result.color,
  stylesheetHrefs: result.hrefs,
  skipped: result.skipped,
  fonts: result.fonts,
  ruleCount: result.rules.length,
  nameCount: result.names.length,
  rules: result.rules,
  resolved: result.resolved,
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('rules', result.rules.length, 'names', result.names.length, 'fonts', result.fonts.length, 'skipped', result.skipped.length);
console.log('root', result.fontFamily, result.background, result.color, result.colorScheme);
console.log('sample', result.names.slice(0, 30).join(', '));
await browser.close();
