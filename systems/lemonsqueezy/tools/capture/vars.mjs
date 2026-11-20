// Reads every custom property Lemon Squeezy declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing stylesheet is cross-origin, so the CSSOM walk cannot see it.
// This script records stylesheet responses and parses the :root custom
// properties from the text. docs.lemonsqueezy.com is same-origin enough for
// a CSSOM walk of its own names (Tailwind internals are dropped).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, BASE, DOCS, AUTH, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
const cssBodies = [];
page.on('response', async (res) => {
  const url = res.url();
  const ct = res.headers()['content-type'] || '';
  if (!(ct.includes('text/css') || url.includes('/css/'))) return;
  try { cssBodies.push({ url, body: await res.text() }); } catch { /* gone */ }
});

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
await hideConsent(page);
const inline = await page.evaluate(() => [...document.querySelectorAll('style')].map((s) => s.textContent).join('\n'));
const fontFaces = await page.evaluate(() => {
  const faces = [];
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  for (const sheet of [...document.styleSheets]) {
    let rules;
    try { rules = [...sheet.cssRules]; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const src = noUrl(r.style.getPropertyValue('src') || '');
          faces.push({
            family: (r.style.getPropertyValue('font-family') || '').replace(/["']/g, ''),
            weight: r.style.getPropertyValue('font-weight') || '400',
            style: r.style.getPropertyValue('font-style') || 'normal',
            display: r.style.getPropertyValue('font-display') || '',
            format: (src.match(/format\("?([a-z0-9-]+)"?\)/i) || [])[1] || '',
            host: 'marketing',
          });
        }
        if (r.cssRules) try { walk([...r.cssRules]); } catch { /* skip */ }
      }
    };
    walk(rules);
  }
  return faces;
});

const css = cssBodies.map((s) => s.body).join('\n') + '\n' + inline;
// Same guard as the in-page readers: never record a url() target (it can be a signed asset URL).
// It runs on the whole block before the declarations are split, so a ';' inside a url() cannot
// cut the url short and leave its query behind.
const noUrl = (v) => v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)');
const rootBlocks = [...css.matchAll(/:root\s*\{([^}]+)\}/g)].map((m) => noUrl(m[1]));
const declared = {};
for (const block of rootBlocks) {
  for (const m of block.matchAll(/(--[a-zA-Z0-9_-]+)\s*:\s*([^;]+)/g)) {
    declared[m[1]] = m[2].trim();
  }
}

await page.goto(DOCS + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1800);
const docs = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const keep = {};
  for (const sheet of [...document.styleSheets]) {
    let rules;
    try { rules = [...sheet.cssRules]; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.style && r.selectorText && /:root|html/.test(r.selectorText) && !r.selectorText.includes('*')) {
          for (const n of r.style) {
            if (n.startsWith('--') && !n.startsWith('--tw-')) keep[n] = noUrl(r.style.getPropertyValue(n).trim());
          }
        }
        if (r.cssRules) try { walk([...r.cssRules]); } catch { /* skip */ }
      }
    };
    walk(rules);
  }
  return { title: document.title, vars: keep };
});

const out = {
  captured: new Date().toLocaleDateString('en-CA'),
  source: 'www.lemonsqueezy.com shared Webflow stylesheet :root plus the inline :root block; docs.lemonsqueezy.com non-Tailwind :root names',
  stylesheet: cssBodies.map((s) => s.url.split('/').pop()),
  marketing: { declared, rootBlocks: rootBlocks.length },
  docs: docs.vars,
  fonts: fontFaces.filter((f) => f.family && f.family !== 'webflow-icons'),
  resolved: { light: declared },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('declared', Object.keys(declared).length, 'docs', Object.keys(docs.vars).length, 'fonts', out.fonts.length);
await browser.close();
