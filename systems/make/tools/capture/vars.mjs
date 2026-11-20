// Harvest Make custom properties into raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Marketing pages (/, /pricing, /product) are Webflow. They declare a large
// --_theme---* / --_typography---* / --_default---swatch--* set on :root.
// /templates and /integrations declare --palette-brand-* and --palette-orchid-*.
// Signed URLs in computed values are replaced with url(…).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const pages = [BASE + '/', BASE + '/pricing', BASE + '/templates', BASE + '/login'];
const perPage = {};
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 }).catch((e) => console.log('skip', url, e.message.split('\n')[0]));
  await page.waitForTimeout(1600);
  await hideConsent(page);
  perPage[url] = await page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const root = getComputedStyle(document.documentElement);
    const declared = {};
    const interesting = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      if (!rules) continue;
      const walk = (list) => {
        for (const rule of list) {
          if (rule.cssRules && !rule.style) { walk(rule.cssRules); continue; }
          if (!rule.style) continue;
          if (rule.selectorText !== ':root' && rule.selectorText !== 'html') continue;
          for (let i = 0; i < rule.style.length; i++) {
            const name = rule.style[i];
            if (!name.startsWith('--')) continue;
            if (!declared[name]) declared[name] = noUrl(rule.style.getPropertyValue(name).trim()).slice(0, 180);
            if (interesting.length < 80 && /theme|swatch|palette|typography|radius|spacing|font/.test(name)) interesting.push(name);
          }
        }
      };
      walk(rules);
    }
    const resolved = {};
    for (const name of Object.keys(declared)) {
      if (!/theme|swatch|palette|typography|radius|spacing|font|button/.test(name)) continue;
      const v = noUrl(root.getPropertyValue(name).trim());
      if (v) resolved[name] = v.slice(0, 160);
    }
    const h1 = document.querySelector('h1');
    const cta = [...document.querySelectorAll('a')].find((a) => /try it free|get started free|sign in/i.test(a.innerText || ''));
    return {
      title: document.title,
      final: location.href,
      font: getComputedStyle(document.body).fontFamily,
      h1: h1 && {
        font: getComputedStyle(h1).fontFamily,
        size: getComputedStyle(h1).fontSize,
        weight: getComputedStyle(h1).fontWeight,
        color: getComputedStyle(h1).color,
        tracking: getComputedStyle(h1).letterSpacing,
        line: getComputedStyle(h1).lineHeight,
      },
      cta: cta && {
        text: (cta.innerText || '').replace(/\s+/g, ' ').slice(0, 40),
        bg: getComputedStyle(cta).backgroundColor,
        color: getComputedStyle(cta).color,
        radius: getComputedStyle(cta).borderRadius,
        size: getComputedStyle(cta).fontSize,
        weight: getComputedStyle(cta).fontWeight,
        pad: getComputedStyle(cta).padding,
      },
      declaredCount: Object.keys(declared).length,
      declared,
      resolved,
    };
  });
  console.log(url, perPage[url].title, 'vars', perPage[url].declaredCount);
}
const fonts = await page.evaluate(() => [...document.fonts].slice(0, 40).map((f) => ({ family: f.family, weight: f.weight, status: f.status })));
await browser.close();
const out = { captured: new Date().toLocaleDateString('en-CA'), product: 'Make', pages: perPage, fonts };
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote raw/css-vars.json');
