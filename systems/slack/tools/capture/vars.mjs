// Reads custom properties slack.com declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Stylesheet bodies are taken from network responses plus inline sheets,
// then re-parsed with CSSStyleSheet. Resolution runs on a probe that carries
// those sheets, once plain and once with a .dark class. The public site
// painted light on every captured route; a dark class that changes nothing
// is recorded as unbound.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);
await hideConsent(page);
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
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        if (o.src) o.src = noUrl(o.src);
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.constructor.name === 'CSSContainerRule' ? '@container ' + r.conditionText
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shell = (themeClass) => '<!doctype html><html class="' + themeClass + '"><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const pass of ['light', 'dark']) {
  await probe.setContent(shell(pass === 'dark' ? 'dark' : ''), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
    const p = document.createElement('div');
    box.appendChild(p);
    document.body.appendChild(box);
    const out = {};
    for (const name of names) {
      const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      p.removeAttribute('style');
      if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|currentcolor)$/i.test(raw)) {
        p.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(p).color;
      } else if (!raw.includes('%') && CSS.supports('width', raw) && /px|rem|em/.test(raw)) {
        p.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(p).width;
      } else r.kind = 'other';
      out[name] = r;
    }
    box.remove();
    return out;
  }, want);
}
await browser.close();

const VENDOR = /onetrust|ot-|osano|qualtrics|drift|intercom/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (r.context.some((c) => c === '@layer theme') || names.some((n) => /^--(color|font|space|radius|shadow|text)/.test(n))) return 'theme';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'stylesheet bodies fetched during a live load of https://slack.com/intl/en-sg/ in headless Chromium, plus inline style blocks, re-parsed with CSSStyleSheet. Resolved on a probe carrying those sheets, plain and with a .dark class, at 1440 x 900. The public pages painted light; the dark pass is a probe, not a painted theme.',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, tailwind: names('tailwind').length },
  },
  errors: result.errors,
  theme: result.rules.filter((r) => r.bin === 'theme'),
  app: result.rules.filter((r) => r.bin === 'app'),
  vendor: result.rules.filter((r) => r.bin === 'vendor'),
  tailwind: result.rules.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts.map((f) => ({ file: f.file, family: f['font-family'], weight: f['font-weight'], style: f['font-style'] })),
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${result.rules.length} rules, ${result.fonts.length} font faces`);
console.log('names', out.counts.names);
console.log('resolved light', Object.keys(resolved.light).length, 'dark', Object.keys(resolved.dark).length);
console.log('errors', result.errors.length);
