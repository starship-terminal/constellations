// Reads every custom property factory.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// factory.com is Next.js. CSS ships as same-origin /_next/static/css chunks,
// so the CSSOM can read every rule. The public routes paint light
// (html[data-theme="light"]). The theme layer's default maps
// --color-background to the dark base; [data-theme="light"] inverts it.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
await page.goto('https://factory.com/', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(2500);
const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: (s.href || 'inline-' + i).split('?')[0], media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
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

const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--tw-/.test(n)).sort();

const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await probe2.setContent('<!doctype html><html><head>'
  + sheets.filter((s) => s.css).map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });

const resolveAll = async (theme) => await probe2.evaluate(([names, theme]) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const rootProbe = document.getElementById('probe-root');
  document.documentElement.setAttribute('data-theme', theme);
  document.documentElement.className = '';
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
  const probeEl = document.createElement('div');
  probeEl.style.cssText = 'position:absolute;left:0;top:0';
  box.appendChild(probeEl);
  document.body.appendChild(box);
  const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
  const fromOklab = (L, a, b) => {
    const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
    return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
  };
  const num = (x) => (String(x).endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
  const norm = (c) => {
    let m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    let rgb, a = 1;
    if (m) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v)); a = m[4] === undefined ? 1 : +m[4]; }
    else if ((m = c.match(/^color\(srgb ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^oklab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^oklch\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
    else return { unparsed: c };
    a = Math.round(a * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim() || getComputedStyle(rootProbe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probeEl.removeAttribute('style'); probeEl.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probeEl.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probeEl).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
    } else if (!raw.includes('%') && CSS.supports('width', raw)) {
      probeEl.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probeEl).width;
    } else if (/^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw) || /cubic-bezier/.test(raw)) {
      r.kind = 'easing'; r.value = raw;
    } else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) {
      r.kind = 'fontFamily'; r.value = raw;
    } else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, [want, theme]);

const resolvedLight = await resolveAll('light');
const resolvedDark = await resolveAll('dark');
await browser.close();

const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tw';
  if (names.every((n) => n.startsWith('--sf-') || n.startsWith('--fh-') || n === '--web-demo-sidebar' || n === '--my-var' || n === '--var')) return 'app';
  return 'token';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'factory.com same-origin /_next/static/css chunks, read through the CSSOM on the live home page and re-parsed in a probe. Light is html[data-theme=light], the theme the public routes paint. Dark is the theme-layer default (data-theme=dark on the probe), not a toggle on the marketing pages.',
  sheets: sheets.map(({ name, media, css }) => ({ name, media, bytes: css.length, unreadable: !css })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, tw: names('tw').length, utility: names('utility').length },
  },
  errors: result.errors,
  token: ok.filter((r) => r.bin === 'token'),
  app: ok.filter((r) => r.bin === 'app'),
  tw: ok.filter((r) => r.bin === 'tw'),
  utility: ok.filter((r) => r.bin === 'utility'),
  fonts: result.fonts.map((f) => ({ ...f, src: f.src ? 'url(…)' : f.src, file: (f.file || '').split('?')[0] })),
  resolved: { light: resolvedLight, dark: resolvedDark },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved light ${Object.keys(resolvedLight).length} dark ${Object.keys(resolvedDark).length}`);
console.log(`rules ${ok.length} fonts ${result.fonts.length} token ${out.counts.names.token} app ${out.counts.names.app} tw ${out.counts.names.tw} utility ${out.counts.names.utility}`);
console.log('errors', result.errors);
