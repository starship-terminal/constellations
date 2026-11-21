// Read maze.co custom properties from the live public homepage and write
// raw/css-vars.json. One light theme. No dark class is applied.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, hideConsent } from './lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA });
await page.goto(BASE + '/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(2000);
await hideConsent(page);

const data = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const declared = [];
  const fonts = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = [...sheet.cssRules]; } catch { continue; }
    const href = sheet.href || 'inline';
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family').replace(/['"]/g, ''),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
            src: noUrl(r.style.getPropertyValue('src')).slice(0, 180),
            file: href,
          });
          continue;
        }
        if (r.cssRules && !r.style) {
          walk([...r.cssRules], ctx);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (!k.startsWith('--') || k.startsWith('--tw-')) continue;
          props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) declared.push({ selector: (r.selectorText || '').slice(0, 180), props, file: href });
      }
    };
    walk(rules, '');
  }
  const root = getComputedStyle(document.documentElement);
  const resolved = {};
  const seen = new Set();
  for (const row of declared) for (const name of Object.keys(row.props)) seen.add(name);
  for (const name of seen) {
    resolved[name] = { raw: declared.find((d) => d.props[name])?.props[name] || '', value: root.getPropertyValue(name).trim() };
  }
  return { declaredCount: declared.length, fonts, resolved };
});

const out = {
  product: 'maze',
  capturedAt: new Date().toISOString(),
  url: 'https://maze.co/',
  theme: 'light',
  note: 'Read from the live public homepage CSSOM. No dark theme switch exists on the captured pages. Tailwind --tw-* internals are omitted. url() values are stripped.',
  fonts: data.fonts.filter((f) => f.family && !f.src.startsWith('url(…)')).slice(0, 40),
  resolved: { light: data.resolved },
  declarations: data.declaredCount,
};
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
console.log('vars', Object.keys(data.resolved).length, 'fonts', out.fonts.length, '->', OUT);
await browser.close();
