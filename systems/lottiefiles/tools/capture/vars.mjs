// Reads custom properties from lottiefiles.com and writes raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Stylesheet bodies are taken from network responses and inline sheets, then
// re-parsed with CSSStyleSheet. The public site paints one light theme.
// A `.dark` pass is recorded so a later reader can see that nothing binds it.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const liveRoot = await page.evaluate(() => {
  const cs = getComputedStyle(document.documentElement);
  const names = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = [...sheet.cssRules]; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.style) for (let i = 0; i < r.style.length; i++) if (r.style[i].startsWith('--')) names.push(r.style[i]);
        if (r.cssRules) walk([...r.cssRules]);
      }
    };
    walk(rules);
  }
  const unique = [...new Set(names)].sort();
  const values = {};
  for (const n of unique) {
    const v = cs.getPropertyValue(n).trim();
    if (v) values[n] = v.slice(0, 300);
  }
  return {
    colorScheme: cs.colorScheme,
    background: getComputedStyle(document.body).backgroundColor,
    font: getComputedStyle(document.body).fontFamily,
    values,
  };
});
const sheets = [...bodies.entries()].concat(inline);
await page.close();

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
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
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : (r.cssText || '').split('{')[0].trim().slice(0, 120);
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
      if (n) rules.push({ file: String(file).slice(0, 180), selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 180), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shell = (themeClass) => '<!doctype html><html class="' + themeClass + '"><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !n.startsWith('--tw-')).sort();
const resolved = {};
for (const pass of ['light', 'dark']) {
  await probe.setContent(shell(pass === 'dark' ? 'dark' : ''), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const cs = getComputedStyle(document.documentElement);
    const out = {};
    for (const name of names) {
      const raw = cs.getPropertyValue(name).trim();
      if (raw) out[name] = { raw: raw.slice(0, 300), value: raw.slice(0, 300) };
    }
    return out;
  }, want);
}
await browser.close();

const names = (pred) => [...new Set(result.rules.filter(pred).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'stylesheet bodies fetched during a live / load on lottiefiles.com, plus inline style blocks, re-parsed with CSSStyleSheet. Resolved on a probe document, plain and with a .dark class (unbound on the public site), at 1440x900. liveRoot is getComputedStyle on the real homepage.',
  liveRoot,
  sheets: sheets.map(([n, t]) => `${String(n).slice(0, 160)} (${t.length} bytes)`),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: want.length,
  },
  errors: result.errors,
  fonts: result.fonts.slice(0, 40),
  theme: result.rules.filter((r) => /:root|html|body/.test(r.selector || '')).slice(0, 80),
  resolved,
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', result.rules.length, 'fonts', result.fonts.length, 'live', Object.keys(liveRoot.values).length, 'errors', result.errors.length);
