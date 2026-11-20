// Reads every custom property www.monarch.com declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site is a Next.js build on Vercel. Stylesheets that the CSSOM
// can read are taken from the live page. Cross-origin sheets are fetched and
// re-parsed. Osano consent variables are binned separately from the product
// theme. The public site paints one light theme (cream page, ink text).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const BASE = 'https://www.monarch.com';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const bodies = new Map();
page.on('response', (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  r.text().then((t) => bodies.set(r.url().split('?')[0], t), () => {});
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);

const live = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try {
    return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') };
  } catch {
    return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true };
  }
}));
const htmlClass = await page.evaluate(() => document.documentElement.className);
const colorScheme = await page.evaluate(() => getComputedStyle(document.documentElement).colorScheme);
await page.close();

const sheets = live.map((s) => {
  if (s.css) return s;
  const key = (s.name || '').split('?')[0];
  if (bodies.has(key)) return { ...s, css: bodies.get(key), fetched: true, unreadable: false };
  return s;
});
for (const s of sheets) {
  if (s.css || !/^https?:/.test(s.name || '')) continue;
  try {
    const res = await fetch(s.name);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    s.css = await res.text();
    s.fetched = true;
    delete s.unreadable;
    console.log('fetched', s.name.slice(0, 140), s.css.length);
  } catch (e) {
    s.fetchError = String(e.message || e);
    console.log('fetch failed', s.name, s.fetchError);
  }
}
console.log('sheets', sheets.map((s) => ({ name: (s.name || '').slice(0, 80), bytes: (s.css || '').length, unreadable: !!s.unreadable })));

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
    if (!s.css) { errors.push({ file: s.name, error: s.fetchError || 'unreadable' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_)/.test(n)).sort();
console.log('names to resolve', want.length, 'rules', result.rules.length, 'fonts', result.fonts.length);

const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const cssJoin = sheets.filter((s) => s.css).map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('');
await probe2.setContent('<!doctype html><html><head>' + cssJoin + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
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
  const num = (x) => (String(x).endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
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
    if (!raw) { out[name] = { kind: 'missing' }; continue; }
    const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
    probe.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if ((m = raw.match(/^(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)%\s+(\d+(?:\.\d+)?)%(?:\s*\/\s*([\d.]+%?))?$/))) {
      probe.style.color = `hsl(${m[1]} ${m[2]}% ${m[3]}%)`;
      r.kind = 'color'; r.value = norm(getComputedStyle(probe).color); r.note = 'H S% L% channel';
    } else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|currentcolor)$/i.test(raw)) {
      probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = r.value.unparsed; delete r.value; }
    } else if (!raw.includes('%') && CSS.supports('width', raw)) {
      probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width;
    } else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, want);

const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--osano'))) return 'osano';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tw';
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  return 'token';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'www.monarch.com public homepage stylesheets, CSSOM plus fetched cross-origin sheets, re-parsed in a probe document. One light theme. html class: ' + JSON.stringify(htmlClass) + '. color-scheme: ' + colorScheme,
  sheets: sheets.map(({ name, media, css, fetched }) => ({ name, media, bytes: (css || '').length, ...(fetched ? { fetched: true } : {}) })),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, osano: names('osano').length, tw: names('tw').length, utility: names('utility').length },
  },
  errors: result.errors,
  token: result.rules.filter((r) => r.bin === 'token'),
  osano: result.rules.filter((r) => r.bin === 'osano'),
  tw: result.rules.filter((r) => r.bin === 'tw'),
  utility: result.rules.filter((r) => r.bin === 'utility'),
  fonts: result.fonts.map((f) => ({ ...f, src: f.src ? String(f.src).replace(/url\([^)]{40,}\)/g, 'url(…)') : f.src })),
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', path.join(REF, 'raw', 'css-vars.json'));
console.log('counts', JSON.stringify(out.counts));
const sample = Object.entries(resolved).filter(([, v]) => v.kind === 'color').slice(0, 25);
console.log('color sample', sample.map(([k, v]) => k + '=' + v.value).join('\n'));
await browser.close();
