// Reads custom properties and a few authored rules from Macaw's live public CSS.
// Writes raw/css-vars.json. Does not sign in or submit anything.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, hideOverlays } from './public/lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
await page.goto(BASE + '/', { waitUntil: 'load', timeout: 90000 });
await hideOverlays(page);
const data = await page.evaluate(() => {
  const names = [];
  const rules = [];
  const fonts = [];
  const walk = (rs, href) => {
    for (const r of rs) {
      if (r.type === CSSRule.FONT_FACE_RULE) fonts.push((r.cssText || '').slice(0, 240));
      if (r.style) {
        for (const n of r.style) if (n.startsWith('--') && !names.includes(n)) names.push(n);
        const interesting = /button|navbar|form-input|pricing|faq|heading/i.test(r.selectorText || '');
        if (interesting && rules.length < 40) rules.push({ sel: (r.selectorText || '').slice(0, 160), href: href || 'inline', css: (r.cssText || '').slice(0, 280) });
      }
      if (r.cssRules) walk([...r.cssRules], href);
    }
  };
  const sheets = [];
  for (const sheet of document.styleSheets) {
    let ruleset;
    try { ruleset = [...sheet.cssRules]; } catch (e) { sheets.push({ href: sheet.href, error: String(e).slice(0, 80) }); continue; }
    sheets.push({ href: sheet.href, rules: ruleset.length });
    walk(ruleset, sheet.href);
  }
  const root = getComputedStyle(document.documentElement);
  const computed = {};
  for (const n of names) {
    const v = root.getPropertyValue(n).trim();
    if (v) computed[n] = v.slice(0, 200);
  }
  return {
    title: document.title,
    url: location.href,
    sheets,
    names,
    computed,
    sampleRules: rules,
    fonts: fonts.slice(0, 12),
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
  };
});
data.readAt = new Date().toISOString();
data.source = 'https://macawhq.com/ live CSSOM, signed out, 1440x900. Webflow stylesheet on cdn.prod.website-files.com plus inline rules.';
fs.writeFileSync(OUT, JSON.stringify(data, null, 2) + '\n');
console.log('names', data.names.length, 'sheets', data.sheets.length, '->', OUT);
await browser.close();
