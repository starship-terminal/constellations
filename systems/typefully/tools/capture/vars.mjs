// Read Typefully custom properties from a live public page and write raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Typefully is a Next.js marketing site. Styles arrive as linked CSS plus inline
// blocks. Linked bodies are taken from network responses. Names are resolved on
// a probe document, once plain and once with a dark class. The live site has no
// theme toggle; the dark pass is a reconstruction and is labelled as such.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US', colorScheme: 'light' });
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
const res = await page.goto('https://typefully.com/pricing', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(2500);
console.log('pricing', res && res.status(), 'sheets', bodies.size);
const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean));
const rootVars = await page.evaluate(() => {
  const cs = getComputedStyle(document.documentElement);
  const out = {};
  for (let i = 0; i < cs.length; i++) {
    const k = cs[i];
    if (k.startsWith('--')) out[k] = cs.getPropertyValue(k).trim();
  }
  return { count: Object.keys(out).length, sample: Object.fromEntries(Object.entries(out).slice(0, 40)), bg: getComputedStyle(document.body).backgroundColor, font: getComputedStyle(document.body).fontFamily };
});
console.log('computed root vars', rootVars.count, 'bg', rootVars.bg, 'font', rootVars.font);
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'root-computed.json'), JSON.stringify(rootVars, null, 1) + '\n');

const sheets = [...bodies.entries()].concat(inline);
await page.close();

const probe = await browser.newPage();
const parsed = await probe.evaluate((sheets) => {
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
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors, sheetBytes: sheets.map(([n, t]) => [n, t.length]) };
}, sheets);
console.log('rules', parsed.rules.length, 'fonts', parsed.fonts.length, 'errors', parsed.errors.length);

const want = [...new Set(parsed.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !n.startsWith('--tw-')).sort();
const shell = (cls) => '<!doctype html><html class="' + cls + '"><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe"></div></body></html>';
const resolved = {};
for (const pass of ['light', 'dark']) {
  await probe.setContent(shell(pass === 'dark' ? 'dark' : ''), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const box = document.createElement('div');
    const p = document.createElement('div');
    box.appendChild(p);
    box.style.cssText = 'position:absolute;visibility:hidden';
    document.body.appendChild(box);
    const out = {};
    for (const name of names) {
      const raw = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      p.removeAttribute('style');
      if (CSS.supports('color', raw)) {
        p.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(p).color;
      } else if (CSS.supports('width', raw) && !raw.includes('%')) {
        p.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(p).width;
      } else r.kind = 'other';
      out[name] = r;
    }
    return out;
  }, want);
  console.log(pass, Object.keys(resolved[pass]).length);
}
await browser.close();

const THEME = /^--(typ-|color-|font-|radius-|shadow-|spacing)/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c.includes('@layer properties') || c.includes('@layer theme'))) return 'tailwind';
  if (names.some((n) => n.startsWith('--typ-'))) return 'app';
  if (names.every((n) => THEME.test(n))) return 'theme';
  return 'app';
};
for (const r of parsed.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(parsed.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'stylesheet bodies from a live https://typefully.com/pricing load (network responses plus inline style blocks), re-parsed with CSSStyleSheet. Resolved on a probe at 1440x900, plain and with a dark class. The dark class is a reconstruction: the public site has no theme toggle.',
  sheets: parsed.sheetBytes,
  counts: { rules: parsed.rules.length, fonts: parsed.fonts.length, app: names('app').length, theme: names('theme').length, tailwind: names('tailwind').length },
  errors: parsed.errors,
  app: parsed.rules.filter((r) => r.bin === 'app').slice(0, 400),
  theme: parsed.rules.filter((r) => r.bin === 'theme').slice(0, 200),
  fonts: parsed.fonts.map((f) => ({ ...f, src: f.src ? String(f.src).replace(/url\([^)]+\)/g, 'url(…)') : f.src })),
  resolved,
  appNames: names('app').filter((n) => n.startsWith('--typ-')).slice(0, 200),
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote css-vars.json', out.counts);
console.log('typ names', out.appNames.slice(0, 40).join(', '));
