// Read every custom property column.com declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// column.com paints one light theme. Custom properties live in inline stylesheets
// the CSSOM can read. Each name is resolved in a probe document that carries those
// sheets. Docs (docs.column.com) are a separate surface and are not mixed in.
//
// Bins:
//   token    palette and role names: --color-*, --rgb-*, --text-*, --bg-*, --btn-*,
//            --blog-*, declared on :root or a palette/theme class
//   app      other names the site's own rules declare
//   utility  a one-off [--x:value] arbitrary-property class
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' });
const page = await context.newPage();
await page.goto('https://column.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch { return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true }; }
}));
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
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: 'cross-origin to the CSSOM' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await probe2.setContent('<!doctype html><html><head>'
  + sheets.filter((s) => s.css).map((s) => '<style' + (s.media ? ' media="' + s.media.replace(/"/g, '') + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="color-palette--primary"><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_)/.test(n)).sort();
const resolved = await probe2.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rootProbe = document.getElementById('probe-root');
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0';
  box.appendChild(probe);
  document.body.appendChild(box);
  const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
  const fromOklab = (L, a, b) => {
    const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
    return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
  };
  const num = (x) => (x.endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
  const norm = (c) => {
    let m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    let rgb, a = 1;
    if (m) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v)); a = m[4] === undefined ? 1 : +m[4]; }
    else if ((m = c.match(/^color\(srgb ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
    else return { unparsed: c };
    a = Math.round(a * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim() || getComputedStyle(rootProbe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
    } else if (!raw.includes('%') && CSS.supports('width', raw) && !raw.includes('var(')) {
      probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width;
    } else if (CSS.supports('transition-duration', raw) && !raw.includes('var(')) {
      probe.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(probe).transitionDuration;
    } else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, want);
await browser.close();

const TOKEN = /^--(color|rgb|text|bg|btn|blog|font|space|radius|shadow|ring)-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.some((n) => TOKEN.test(n)) && /^(:root|html|body|\.color-palette|\.blog-theme)/.test(r.selector || '')) return 'token';
  if (names.every((n) => TOKEN.test(n))) return 'token';
  return 'app';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "column.com inline stylesheets, read through the CSSOM on the live signed-out home page and re-parsed in a probe document. One light theme. Docs are a separate surface.",
  sheets: sheets.map(({ name, media, css }) => ({ name, media, bytes: css.length })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, utility: names('utility').length },
  },
  errors: result.errors,
  token: ok.filter((r) => r.bin === 'token'),
  app: ok.filter((r) => r.bin === 'app'),
  utility: ok.filter((r) => r.bin === 'utility'),
  fonts: result.fonts.map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], display: f['font-display'] })),
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved: ${Object.keys(resolved).length} names`);
console.log(`rules ${ok.length} fonts ${result.fonts.length} token ${out.counts.names.token} app ${out.counts.names.app}`);
