// Read Square's declared custom properties from the live public homepage.
// Writes raw/css-vars.json. Nothing is signed into and no form is submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node read-vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, RAW, BASE } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
await open(page, BASE + '/us/en', { wait: 3000 });

const data = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string'
    ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)')
    : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, href) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({
          family: r.style.getPropertyValue('font-family').replace(/["']/g, ''),
          weight: r.style.getPropertyValue('font-weight'),
          style: r.style.getPropertyValue('font-style'),
          href: (href || '').slice(0, 120),
        });
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : r.cssText.split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], href);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) {
        rules.push({
          selector: (r.selectorText || '').slice(0, 180),
          context: ctx.slice(0, 4),
          href: (href || 'inline').slice(0, 140),
          properties: props,
        });
      }
    }
  };
  for (const sheet of document.styleSheets) {
    try { if (sheet.cssRules) walk(sheet.cssRules, [], sheet.href || 'inline'); }
    catch (e) { rules.push({ selector: null, error: String(e).slice(0, 160), href: sheet.href || 'inline' }); }
  }

  const rootStyle = getComputedStyle(document.documentElement);
  const resolved = {};
  const names = new Set();
  for (const rule of rules) {
    if (!rule.properties) continue;
    for (const k of Object.keys(rule.properties)) names.add(k);
  }
  for (const name of names) {
    const v = rootStyle.getPropertyValue(name).trim();
    if (v) resolved[name] = noUrl(v).slice(0, 240);
  }
  return {
    url: location.href.split('?')[0],
    title: document.title,
    colorScheme: rootStyle.colorScheme,
    htmlClass: document.documentElement.className,
    rules,
    fonts,
    resolved,
  };
});

// Dark color mode is declared on :where([data-color-mode="dark"]). Resolve those
// names by setting the attribute on a clone of the live document's custom props
// is not possible without the cascade, so re-read after setting the attribute
// on <html> and record which computed values change. This is a live attribute
// flip on the public page, not an account setting.
await page.evaluate(() => document.documentElement.setAttribute('data-color-mode', 'dark'));
await page.waitForTimeout(400);
const dark = await page.evaluate(() => {
  const s = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  const out = {};
  for (let i = 0; i < s.length; i++) {
    const k = s[i];
    if (k.startsWith('--')) out[k] = s.getPropertyValue(k).trim().slice(0, 240);
  }
  return {
    htmlBg: body.backgroundColor,
    htmlColor: body.color,
    colorScheme: s.colorScheme,
    resolved: out,
  };
});
await page.evaluate(() => document.documentElement.removeAttribute('data-color-mode'));

const changed = [];
for (const [k, v] of Object.entries(dark.resolved)) {
  if (data.resolved[k] && data.resolved[k] !== v) changed.push(k);
}

const out = {
  capturedAt: new Date().toISOString(),
  source: data.url,
  title: data.title,
  htmlClass: data.htmlClass,
  colorScheme: data.colorScheme,
  note: 'Declared custom properties walked from the live CSSOM on the public US English homepage. resolved is getComputedStyle(documentElement) in the default (light) theme. darkChanged lists names whose computed value differs after setting data-color-mode=dark on <html>. Cross-origin sheets that throw are recorded as errors and skipped.',
  fontFamilies: [...new Set(data.fonts.map((f) => f.family))].sort(),
  fonts: data.fonts.filter((f, i, a) => a.findIndex((g) => g.family === f.family && g.weight === f.weight) === i).slice(0, 80),
  ruleCount: data.rules.filter((r) => r.properties).length,
  errors: data.rules.filter((r) => r.error),
  rules: data.rules.filter((r) => r.properties),
  resolved: data.resolved,
  dark: { colorScheme: dark.colorScheme, htmlBg: dark.htmlBg, htmlColor: dark.htmlColor, changed },
  darkResolved: Object.fromEntries(changed.map((k) => [k, dark.resolved[k]])),
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', out.ruleCount, 'resolved', Object.keys(out.resolved).length, 'darkChanged', changed.length, 'fonts', out.fontFamilies);
await browser.close();
