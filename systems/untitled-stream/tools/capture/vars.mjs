// Reads every custom property untitled.stream's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// untitled.stream is a Vite build serving app-*.css same-origin, so the live
// page's CSSOM is readable: every rule declaring a --* property is kept with
// its selector and enclosing @media/@supports/@layer context, and @font-face
// rules are kept too. Each name is then resolved on the live page (document
// root and a hidden probe under <body>), classified and computed the way the
// browser computes it: colours come back as sRGB hex, lengths as px at
// 1440 x 900.
//
// Bins (Tailwind site):
//   theme    the design tokens: --color-*, --font-*, --text-*, --spacing-*,
//            --radius-*, --breakpoint-*, --shadow-*, --ease-*, --animate-* ...
//   utility  a one-off `[--x:value]` arbitrary-property utility class
//   app      any other name the theme's own rules declare
//   tailwind Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, clearChallenge } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT_FILE = path.join(REF, 'raw', 'css-vars.json');

const { browser, context } = await launch();
const page = await context.newPage();
// The Cloudflare waiting room and the Remix error boundary are both known
// outcomes for this site — the same checks the measure runner makes. A
// blocked page must not replace the saved readings, so bail out instead.
let ok = false;
for (let attempt = 0; attempt < 3 && !ok; attempt++) {
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (!(await clearChallenge(page))) break;
  await page.waitForTimeout(6000);
  const err = await page.evaluate(() => /something went wrong/i.test((document.body && document.body.innerText) || '')).catch(() => true);
  ok = !err;
}
if (!ok) {
  await browser.close();
  console.error('blocked: the Cloudflare waiting room or the Remix error boundary is up — keeping the existing raw/css-vars.json');
  process.exit(1);
}

// ---- harvest: every rule with --* declarations, live CSSOM ----
const result = await page.evaluate(() => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const skipped = [];
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
          : r.cssText.split('{')[0].trim().slice(0, 120);
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 160), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  [...document.styleSheets].forEach((ss, i) => {
    const file = ss.href ? ss.href.split('/').pop().split('?')[0] || ss.href : `inline-${i}`;
    try { walk(ss.cssRules, [], file); } catch { skipped.push(file); }
  });
  return { rules, fonts, skipped };
});

// ---- resolution: read each name on the live root and a body probe ----
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = await page.evaluate((names) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
  document.body.appendChild(probe);
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
    const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim())
      || noUrl(getComputedStyle(probe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
    }
    else if (!raw.includes('%') && CSS.supports('width', raw)) { probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
    else if (CSS.supports('box-shadow', raw)) { probe.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(probe).boxShadow; }
    else if (CSS.supports('transition-duration', raw)) { probe.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(probe).transitionDuration; }
    else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
    else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
    else r.kind = 'other';
    out[name] = r;
  }
  probe.remove();
  return out;
}, want);
await browser.close();

// Verify the page delivered its token layer before replacing the saved
// readings: an error page's or an empty CSSOM yields none of them.
const REQUIRED = ['--color-primary-label', '--color-primary-background', '--body-size', '--super-title-size'];
const missingRequired = REQUIRED.filter((n) => !resolved[n]);
if (!result.rules.length || missingRequired.length) {
  console.error(`refusing to write: ${result.rules.length} rules harvested, missing ${missingRequired.join(', ') || 'none'} — keeping the existing raw/css-vars.json`);
  process.exit(1);
}

const THEME = /^--(color|font|text|spacing|radius|breakpoint|container|shadow|inset-shadow|drop-shadow|ease|animate|blur|perspective|aspect|leading|tracking|weight|default)-?/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties' || c === '@layer theme')) return 'tailwind';
  if (names.every((n) => THEME.test(n))) return 'theme';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const bySelector = {};
for (const r of result.rules) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'the live CSSOM on untitled.stream (app-*.css is same-origin, readable); one theme, resolved at 1440 x 900',
  sheetsSkippedCrossOrigin: result.skipped,
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  theme: result.rules.filter((r) => r.bin === 'theme'),
  app: result.rules.filter((r) => r.bin === 'app'),
  utility: result.rules.filter((r) => r.bin === 'utility'),
  tailwind: result.rules.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(OUT_FILE, JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${result.rules.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}; resolved ${Object.keys(resolved).length}; skipped ${result.skipped.length} cross-origin sheets`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 20)) console.log(`  ${v}\t${k.slice(0, 150)}`);
