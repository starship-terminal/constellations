// Harvest Instacart's IDS custom properties from the live homepage.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Writes raw/css-vars.json. Instacart paints one light theme: --ids-* colour,
// space, radius and opacity tokens plus three easing functions are declared
// on :root. --ids-typography-name is empty on :root and set per emotion class.
// Nothing is signed into. Overlays are hidden, never clicked.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, hideOverlays, BASE } from './public/lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = path.resolve(HERE, '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideOverlays(page);

const data = await page.evaluate(async () => {
  // The page runs apart from this module, so the masking helper is defined here.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const sheets = [...document.styleSheets];
  const declared = {};
  const fonts = [];
  let rules = 0;
  let blocked = 0;
  const walk = (list) => {
    for (const rule of list) {
      rules++;
      if (rule.type === CSSRule.FONT_FACE_RULE) {
        const o = {
          family: rule.style.getPropertyValue('font-family').replace(/['"]/g, ''),
          weight: rule.style.getPropertyValue('font-weight'),
          style: rule.style.getPropertyValue('font-style'),
          src: noUrl(rule.style.getPropertyValue('src') || '').slice(0, 180),
        };
        fonts.push(o);
      }
      if (rule.style) {
        for (let i = 0; i < rule.style.length; i++) {
          const name = rule.style[i];
          if (name.startsWith('--')) declared[name] = noUrl(rule.style.getPropertyValue(name).trim());
        }
      }
      if (rule.cssRules) {
        try { walk(rule.cssRules); } catch { blocked++; }
      }
    }
  };
  for (const sheet of sheets) {
    try { walk(sheet.cssRules); } catch { blocked++; }
  }
  const cs = getComputedStyle(document.documentElement);
  const resolved = {};
  for (const name of Object.keys(declared)) resolved[name] = noUrl(cs.getPropertyValue(name).trim());
  const body = getComputedStyle(document.body);
  return {
    declared,
    resolved,
    fonts,
    rules,
    blocked,
    sheetCount: sheets.length,
    body: {
      fontFamily: body.fontFamily,
      fontSize: body.fontSize,
      fontWeight: body.fontWeight,
      lineHeight: body.lineHeight,
      color: body.color,
      backgroundColor: body.backgroundColor,
    },
    htmlClass: document.documentElement.className,
    bodyClass: document.body.className,
    colorScheme: cs.colorScheme,
  };
});

const out = {
  source: 'https://www.instacart.com/',
  capturedAt: new Date().toISOString(),
  theme: 'light',
  note: 'Instacart IDS. One light theme. --ids-* declared on :root. Typography name is per emotion class, empty on :root.',
  sheetCount: data.sheetCount,
  ruleCount: data.rules,
  blockedSheets: data.blocked,
  htmlClass: data.htmlClass,
  bodyClass: data.bodyClass,
  colorScheme: data.colorScheme,
  body: data.body,
  fonts: data.fonts,
  declared: { light: data.declared },
  resolved: { light: data.resolved },
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('vars', Object.keys(data.declared).length, 'fonts', data.fonts.length, 'rules', data.rules, 'blocked', data.blocked);
await browser.close();
