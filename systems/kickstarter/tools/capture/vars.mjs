// Harvest kickstarter.com custom properties.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// a.kickstarter.com stylesheets are cross-origin, so the live CSSOM cannot
// read them. The script downloads the atomic sheet through the page (Playwright
// response body, which is not CORS-blocked) and parses it in a constructed
// CSSStyleSheet adopted into the document, then reads computed values on
// documentElement. Consent is hidden, never clicked. Headed Chrome: Cloudflare
// challenges headless Chromium.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launchBrowser, newContext, open } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });
const CACHE = path.join(os.homedir(), '.design-systems', 'kickstarter', 'css');
fs.mkdirSync(CACHE, { recursive: true });

const browser = await launchBrowser();
const context = await newContext(browser, { dpr: 1 });
const saved = [];
context.on('response', async (res) => {
  try {
    const u = res.url();
    if (!/a\.kickstarter\.com\/assets\/packages\/.*\.css/.test(u)) return;
    if (res.status() !== 200) return;
    const body = await res.body();
    if (body.length < 1000) return;
    const name = u.split('/').pop().split('?')[0];
    const file = path.join(CACHE, name);
    if (!fs.existsSync(file) || fs.statSync(file).size < body.length) fs.writeFileSync(file, body);
    saved.push({ url: u.split('?')[0], file, bytes: body.length });
  } catch { /* body already consumed */ }
});
const page = await context.newPage();
await open(page, BASE + '/', { wait: 2000 });

// Prefer the freshly saved atomic sheet; fall back to the probe cache.
let cssFile = saved.sort((a, b) => b.bytes - a.bytes)[0]?.file;
if (!cssFile) {
  const probe = path.join(os.homedir(), '.design-systems', 'kickstarter', 'probe', 'css');
  const hit = fs.existsSync(probe) && fs.readdirSync(probe).find((n) => n.includes('atomic'));
  if (hit) cssFile = path.join(probe, hit);
}
if (!cssFile) { console.error('no atomic css captured'); process.exit(1); }
const css = fs.readFileSync(cssFile, 'utf8').replace(/^\/\* https?:\/\/[^\n]*\n/, '');
console.log('parsing', cssFile, 'bytes', css.length);

const live = await page.evaluate(async (cssText) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const sheet = new CSSStyleSheet();
  await sheet.replace(cssText);
  document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];
  const decls = [];
  const fonts = [];
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = {};
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : (r.cssText || '').split('{')[0].trim().slice(0, 140);
        walk(r.cssRules, [...ctx, head].slice(0, 4));
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (!Object.keys(props).length) continue;
      const keep = Object.keys(props).some((k) => k.startsWith('--kds-') || k.startsWith('--bttn') || k.startsWith('--focus-ring') || k.startsWith('--creator-nav'));
      if (keep) decls.push({ selector: (r.selectorText || '').slice(0, 180), context: ctx, props });
    }
  };
  walk(sheet.cssRules, []);
  const cs = getComputedStyle(document.documentElement);
  const names = new Set();
  for (const d of decls) for (const k of Object.keys(d.props)) names.add(k);
  const resolved = {};
  for (const name of names) {
    const v = noUrl(cs.getPropertyValue(name).trim());
    if (v) resolved[name] = v;
  }
  const reduceRules = [];
  const walkReduce = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.MEDIA_RULE && /prefers-reduced-motion/.test(r.media.mediaText)) {
        reduceRules.push({ media: r.media.mediaText, rules: r.cssRules.length, sample: (r.cssText || '').slice(0, 240) });
      }
      if (r.cssRules) walkReduce(r.cssRules, ctx);
    }
  };
  walkReduce(sheet.cssRules, []);
  return {
    declCount: decls.length,
    decls,
    fonts: fonts.slice(0, 40),
    resolved,
    reduceRules: reduceRules.slice(0, 30),
    fontBody: getComputedStyle(document.body).fontFamily,
    brand: cs.getPropertyValue('--kds-color-brand').trim(),
  };
}, css);

const binOf = (name) => name.startsWith('--kds-') ? 'kds' : name.startsWith('--_') ? 'utility' : 'app';
const bins = { kds: 0, app: 0, utility: 0 };
for (const name of Object.keys(live.resolved)) bins[binOf(name)]++;

const out = {
  product: 'kickstarter',
  read: new Date().toLocaleDateString('en-CA'),
  source: 'atomic stylesheet downloaded through headed Chrome from a.kickstarter.com, parsed in a constructed CSSStyleSheet and resolved on documentElement at https://www.kickstarter.com/',
  cssFile: path.basename(cssFile),
  fontBody: live.fontBody,
  brandResolved: live.brand,
  fonts: live.fonts,
  bins,
  declarations: live.decls,
  reduceRules: live.reduceRules,
  resolved: { light: live.resolved },
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, 'resolved', Object.keys(live.resolved).length, 'kds', bins.kds, 'decls', live.declCount, 'brand', live.brand, 'fonts', live.fonts.length, 'reduce', live.reduceRules.length);
await browser.close();
