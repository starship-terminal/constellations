// Reads every custom property overflow.io's public stylesheets declare and
// writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site serves /dist/prod/css/public-site-*.min.css. Same-origin
// sheets are readable through the CSSOM. Cross-origin sheets are fetched and
// re-parsed. Overflow paints one light theme; the probe set is named light.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, hideCookies } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await hideCookies(page);

const sheets = await page.evaluate(async () => {
  const out = [];
  for (const s of [...document.styleSheets]) {
    let css = '';
    let unreadable = false;
    try { css = [...s.cssRules].map((r) => r.cssText).join('\n'); }
    catch { unreadable = true; }
    if (unreadable && s.href) {
      try {
        const r = await fetch(s.href);
        css = await r.text();
        unreadable = false;
      } catch { /* leave unreadable */ }
    }
    out.push({ name: s.href || 'inline-' + out.length, media: s.media.mediaText || '', css, unreadable });
  }
  return out;
});
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
    if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: 'unreadable' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await probe2.setContent('<!doctype html><html><head>'
  + sheets.filter((s) => s.css).map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !/^--(tw-|_)/.test(n)).sort();
const resolved = await probe2.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rootProbe = document.getElementById('probe-root');
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
  const probe = document.createElement('div');
  box.appendChild(probe);
  document.body.appendChild(box);
  const norm = (c) => {
    const m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return { unparsed: c };
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : Math.round(+m[4] * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(rootProbe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probe.removeAttribute('style');
    if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probe.style.color = raw;
      r.kind = 'color';
      r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = r.value.unparsed; delete r.value; }
    } else if (CSS.supports('width', raw) && !raw.includes('%')) {
      probe.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probe).width;
    } else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, want);
await browser.close();

const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--bs-'))) return 'bootstrap';
  return 'app';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "overflow.io public stylesheets, read through the CSSOM (and fetch when a sheet was cross-origin) on https://overflow.io/ and re-parsed in a probe document. One light theme.",
  sheets: sheets.map(({ name, media, css }) => ({ name, media, bytes: (css || '').length })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { app: names('app').length, bootstrap: names('bootstrap').length },
  },
  errors: result.errors,
  app: ok.filter((r) => r.bin === 'app'),
  bootstrap: ok.filter((r) => r.bin === 'bootstrap'),
  fonts: result.fonts.map((f) => ({ ...f, src: f.src ? 'url(…)' : undefined })),
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces, ${Object.keys(resolved).length} resolved names`);
console.log('sheets', out.sheets.map((s) => `${s.bytes} ${s.name}`).join('\n'));
