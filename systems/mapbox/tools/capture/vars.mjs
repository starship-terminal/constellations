// Reads every custom property mapbox.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// www.mapbox.com is a Webflow site. Its design tokens are custom properties
// on :root with Webflow's long names (--_colors---blue--blue50, and so on).
// Same-origin sheets are read through the CSSOM. Cross-origin sheets are
// recorded as unreadable and not guessed.
//
// Bins:
//   token    the site's own palette and type scales (--_colors---, --_text-styles---,
//            --_heading-styles---, --_dimensions---, --_color-mode---)
//   app      other custom names the site declares
//   webflow  Webflow internals and OneTrust leftovers
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, closePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);
await closePromo(page);
const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  // Sheet names drop the query and fragment, as the kit does (a ?v= or a signed query is not a name).
  const name = s.href ? s.href.split(/[?#]/)[0] : null;
  try { return { name: name || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch { return { name: name || 'sheet-' + i, media: '', css: '', unreadable: true }; }
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
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await probe2.setContent('<!doctype html><html><head>'
  + sheets.filter((s) => s.css).map((s) => '<style' + (s.media ? ' media="' + s.media.replace(/"/g, '') + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !n.includes('<deleted') && !n.includes('|')).sort();
const resolved = await probe2.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rootProbe = document.getElementById('probe-root');
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
  const probeEl = document.createElement('div');
  box.appendChild(probeEl);
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
    const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
    probeEl.removeAttribute('style');
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)/.test(raw)) {
      probeEl.style.color = raw;
      const painted = getComputedStyle(probeEl).color;
      const n = norm(painted);
      if (n.unparsed) { r.kind = 'other'; r.note = 'colour not converted: ' + painted; }
      else { r.kind = 'color'; r.value = n; }
    } else if (!raw.includes('%') && CSS.supports('width', raw) && /px|rem|em/.test(raw)) {
      probeEl.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probeEl).width;
    } else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, want);
await browser.close();

const TOKEN = /^--_(colors|text-styles|heading-styles|dimensions|color-mode|border)/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.some((n) => TOKEN.test(n))) return 'token';
  if (names.every((n) => /^--(w-|wf-|ot-|hsf-)/.test(n))) return 'webflow';
  return 'app';
};
const ok = result.rules.filter((r) => !Object.keys(r.properties).every((n) => n.includes('<deleted')));
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties).filter((n) => !n.includes('<'))))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "www.mapbox.com Webflow stylesheets, read through the CSSOM on the live home page and re-parsed in a probe document. Cross-origin sheets that the CSSOM could not read are listed under errors and were not guessed.",
  sheets: sheets.map(({ name, media, css, unreadable }) => ({ name, media, bytes: (css || '').length, unreadable: !!unreadable })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, webflow: names('webflow').length },
  },
  errors: result.errors,
  token: ok.filter((r) => r.bin === 'token').map((r) => ({ ...r, properties: Object.fromEntries(Object.entries(r.properties).filter(([k]) => !k.includes('<'))) })),
  app: ok.filter((r) => r.bin === 'app'),
  webflow: ok.filter((r) => r.bin === 'webflow'),
  fonts: result.fonts,
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved: ${Object.keys(resolved).length} names`);
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; token ${out.counts.names.token}, app ${out.counts.names.app}`);
console.log('errors', result.errors.length);
