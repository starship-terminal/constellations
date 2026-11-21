// Read MonoDesk custom properties from the live public homepage.
// PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, BASE } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const outDir = path.join(REF, 'raw');
fs.mkdirSync(outDir, { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);

const harvested = await page.evaluate(() => {
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.conditionText ? '@media ' + (r.media?.mediaText || r.conditionText) : (r.name ? '@layer ' + r.name : r.constructor.name);
        walk(r.cssRules, ctx.concat(head), file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const name = r.style[i];
        if (name.startsWith('--')) props[name] = r.style.getPropertyValue(name).trim();
      }
      if (Object.keys(props).length) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
    }
  };
  for (const sheet of document.styleSheets) {
    const file = sheet.href || 'inline';
    try { walk(sheet.cssRules, [], file); }
    catch (e) { errors.push({ file, error: String(e) }); }
  }
  const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))];
  const cs = getComputedStyle(document.documentElement);
  const resolved = {};
  for (const n of names) resolved[n] = cs.getPropertyValue(n).trim();
  const brand = {
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
    maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
    manifest: document.querySelector('link[rel="manifest"]')?.href || null,
  };
  return {
    url: location.href,
    title: document.title,
    capturedAt: new Date().toISOString(),
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
    bodyFont: getComputedStyle(document.body).fontFamily,
    rules, fonts, errors, resolved, brand,
  };
});
await browser.close();
fs.writeFileSync(path.join(outDir, 'css-vars.json'), JSON.stringify(harvested, null, 2) + '\n');
console.log('rules', harvested.rules.length, 'names', Object.keys(harvested.resolved).length, 'fonts', harvested.fonts.length, 'errors', harvested.errors.length);
