// Reads every custom property cohere.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// cohere.com is a Next.js/Tailwind build: its styles arrive as a
// same-origin CSS bundle plus inline <style> rules, so the CSSOM can read
// most rules. Every rule declaring a --* property is kept with its
// selector and enclosing @media/@layer context, and @font-face rules are
// kept too.
//
// The site paints one light theme. Each name is resolved in a probe document
// that carries the real stylesheets, computed the way the browser computes
// it: colours come back as sRGB hex, lengths as px at 1440 x 900.
//
// Bins:
//   token     namespaced design-token names (--cp-*, --token-*) if any
//   app       other custom names the site's own rules declare
//   framework third-party internals (styled-components, vendor prefixes)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(6000);
// sheets read via CSSOM (the Webflow bundle arrives same-origin; external
// sheets are read the same way when the CSSOM allows)
const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch { return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true }; }
}));
await page.close();

// The Webflow bundle and Google Fonts sit on their CDNs — same-origin to the
// user but cross-origin to the CSSOM. They are static public stylesheets, so
// their text is fetched directly and parsed through the same path.
import https from 'node:https';
const fetchText = (url) => new Promise((resolve, reject) => {
  https.get(url, { headers: { 'user-agent': 'Mozilla/5.0' } }, (res) => {
    if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location)
      return resolve(fetchText(new URL(res.headers.location, url).href));
    if (res.statusCode !== 200) return reject(new Error('HTTP ' + res.statusCode));
    let body = ''; res.on('data', (d) => (body += d)); res.on('end', () => resolve(body));
  }).on('error', reject);
});
for (const s of sheets) {
  if (s.unreadable && /^https?:/.test(s.name)) {
    try { s.css = await fetchText(s.name); s.fetched = true; delete s.unreadable; }
    catch (e) { s.fetchError = String(e); }
  }
}

// ---- harvest: every rule with --* declarations ----
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
      // cohere's named palette ships as Tailwind config utility classes
      // (.bg-volcanic-500 { background-color: rgb(...) }) — no :root theme
      // layer exists, so the declared token layer is these literal
      // declarations. Keep their paint/type declarations in a utilities bin.
      const sel = r.selectorText || '';
      let lit = null;
      if (/^\.(bg|text|border|fill|stroke|rounded|font|leading|tracking|w|h|max-w|min-w|z|shadow|ring|ease|duration|text-web3|outline|gap)-[a-zA-Z0-9_\[\]\/.%()#-]+/.test(sel) && sel.indexOf(':') === sel.lastIndexOf(':')) {
        lit = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k && !k.startsWith('--') && /^(color|background-color|border-color|border-top-color|border-right-color|border-bottom-color|border-left-color|fill|stroke|font-size|line-height|font-family|font-weight|letter-spacing|text-transform|border-radius|border-(top|bottom)-(left|right)-radius|box-shadow|width|height|max-width|min-width|z-index|transition-timing-function|transition-duration|outline-color|caret-color|text-decoration-color|gap|row-gap|column-gap)$/.test(k)) {
            lit[k] = noUrl(r.style.getPropertyValue(k).trim());
          }
        }
        if (!Object.keys(lit).length) lit = null;
      }
      if (n || lit) rules.push({ file, selector: r.selectorText, context: ctx, properties: props, literal: lit || undefined });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    const name = s.name.split(/[?#]/)[0];  // rules cite the sheet by path only
    if (!s.css) { if (s.unreadable) errors.push({ file: name, error: 'cross-origin to the CSSOM' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

// ---- resolve each name the way the browser does, on a probe carrying the sheets
const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await probe2.setContent('<!doctype html><html><head>'
  + sheets.filter((s) => s.css).map((s) => '<style' + (s.media ? ' media="' + s.media + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
const want = [...new Set(result.rules.filter((r) => !r.error).flatMap((r) => Object.keys(r.properties)))]
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
    else if ((m = c.match(/^oklab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^oklch\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
    else return { unparsed: c };
    a = Math.round(a * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(rootProbe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
    } else if (!raw.includes('%') && CSS.supports('width', raw)) { probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
    else if (CSS.supports('box-shadow', raw)) { probe.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(probe).boxShadow; }
    else if (CSS.supports('transition-duration', raw)) { probe.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(probe).transitionDuration; }
    else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
    else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
    else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, want);
await browser.close();

const FRAMEWORK = /^--(sc-|framer|border|grid|section|stack|variant|ticker|cursor|overlay|scroll|breakpoint|blending|mask|filters?|transform|layout|styles)-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.some((n) => n.startsWith('--token-'))) return 'token';
  if (names.every((n) => FRAMEWORK.test(n))) return 'framework';
  return 'app';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'cohere.com\'s inline <style> rules and its CDN stylesheets (cross-origin to the CSSOM, fetched directly as public static files), read through the CSSOM on the live home page and re-parsed in a probe document',
  sheets: sheets.map(({ name, media, css }) => ({ name: name.split(/[?#]/)[0], media, bytes: css.length })),  // path only: no deploy id or font query
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, framework: names('framework').length, utility: names('utility').length },
    bySelector,
  },
  errors: result.errors,
  token: ok.filter((r) => r.bin === 'token'),
  app: ok.filter((r) => r.bin === 'app'),
  framework: ok.filter((r) => r.bin === 'framework'),
  utility: ok.filter((r) => r.bin === 'utility'),
  fonts: result.fonts,
  resolved: { light: resolved },
  utilities: ok.filter((r) => r.literal).map((r) => ({ selector: r.selector, file: r.file, literal: r.literal })),
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved: ${Object.keys(resolved).length} names`);
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names token ${out.counts.names.token}, app ${out.counts.names.app}, framework ${out.counts.names.framework}, utility ${out.counts.names.utility}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 160)}`);
