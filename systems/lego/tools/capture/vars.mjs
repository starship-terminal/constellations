// Reads every custom property lego.com's stylesheets declare and writes
// raw/css-vars.json. Headless Chromium. Consent is hidden, never answered.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, closePromo, withGate, BASE } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const u = r.url();
  if (r.request().resourceType() !== 'stylesheet' && !/\.css(\?|$)/.test(u)) return;
  try { bodies.set(u.split('?')[0], await r.text()); } catch { /* body gone */ }
});
await page.goto(withGate(BASE + '/en-us/themes/city'), { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(5000);
await closePromo(page);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
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
        const o = { file: file.slice(0, 120) };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : (r.cssText || '').split('{')[0].trim().slice(0, 80);
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
      if (n) rules.push({ file: String(file).slice(0, 120), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(0, 4), properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 80)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 80), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

function bin(name, selector) {
  if (/^--(ot-|onetrust)/.test(name) || /onetrust/i.test(selector || '')) return 'vendor';
  if (name.startsWith('--ds-')) return 'app';
  if (name.startsWith('--sk-') || name.startsWith('--_')) return 'component';
  return 'other';
}

const rules = result.rules.map((r) => ({ ...r, bin: bin(Object.keys(r.properties)[0] || '', r.selector) }));
const want = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => n.startsWith('--ds-') || n.startsWith('--sk-'))
  .sort();

const shell = '<!doctype html><html><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe"></div></body></html>';

async function resolve(theme) {
  const p = await browser.newPage();
  await p.setContent(shell, { waitUntil: 'domcontentloaded' });
  if (theme === 'dark') await p.evaluate(() => document.documentElement.classList.add('dark'));
  const values = await p.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const root = document.documentElement;
    const cs = getComputedStyle(root);
    const out = {};
    for (const n of names) {
      const raw = noUrl(cs.getPropertyValue(n).trim());
      if (!raw) continue;
      root.style.setProperty('--probe', `var(${n})`);
      const painted = noUrl(getComputedStyle(root).getPropertyValue('--probe').trim());
      out[n] = { raw: raw.slice(0, 180), value: (painted || raw).slice(0, 180) };
    }
    return out;
  }, want);
  await p.close();
  return values;
}

const light = await resolve('light');
const dark = await resolve('dark');
const bins = {};
for (const r of rules) bins[r.bin] = (bins[r.bin] || 0) + Object.keys(r.properties).length;

const payload = {
  source: 'lego.com /en-us stylesheets, 2026-11-18, signed out, headless Chromium. Consent hidden, never answered.',
  bins,
  sheetCount: sheets.length,
  fonts: result.fonts.slice(0, 40),
  errors: result.errors.slice(0, 12),
  rules: rules.filter((r) => Object.keys(r.properties).some((k) => k.startsWith('--ds-color-') || k.startsWith('--ds-spacing') || k.startsWith('--ds-layout-spacing') || k.startsWith('--ds-layout-radius') || k.startsWith('--ds-border-radius') || k.startsWith('--ds-shadow') || k.startsWith('--ds-font') || /duration|easing/.test(k))).slice(0, 800),
  resolved: { light, dark },
};
fs.writeFileSync(OUT, JSON.stringify(payload, null, 1) + '\n');
console.log('wrote', OUT, 'vars', Object.keys(light).length, 'rules kept', payload.rules.length, 'bins', bins);
await browser.close();
