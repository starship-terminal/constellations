// Read every custom property TokenTracker's stylesheet declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir holding bundle.html> node tools/capture/vars.mjs
//
// The dashboard ships one Vite CSS bundle (/assets/*.css on the local server). It was fetched with
// curl and wrapped in SNAPS/bundle.html as a <style> block, then parsed headless (constructed
// CSSStyleSheet). Every rule declaring a custom property is kept with its selector and context.
//
// Bins:
//   oai        the design tokens: --oai-* and --brand-* (styles.css :root and :root.dark)
//   app        product names: --tt-* (period track, cloud page, card radius) and --lv3-* (leaderboard)
//   utility    a one-off `[--x:value]` arbitrary-property utility class
//   tailwind   Tailwind v3 internals (--tw-*)
//
// Most rendered colours do NOT come from these names: components use Tailwind classes whose
// oai-gray-* values are plain hex in tailwind.config.cjs. Those are read as computed styles by
// public/measure.mjs, which is the evidence of record for colours.
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const SNAPS = process.env.SNAPS;
if (!SNAPS) { console.error('SNAPS=<dir of page copies> is required'); process.exit(2); }

const blocks = new Map();
for (const f of fs.readdirSync(SNAPS).filter((n) => n.endsWith('.html')).sort()) {
  const html = fs.readFileSync(path.join(SNAPS, f), 'utf8');
  for (const m of html.matchAll(/<style([^>]*)>([\s\S]*?)<\/style>/g)) {
    const css = m[2].replace(/<\\\/style/gi, '</style');
    const media = (m[1].match(/media="([^"]*)"/) || [])[1] || '';
    const key = crypto.createHash('sha1').update(media + css).digest('hex').slice(0, 10);
    const b = blocks.get(key) || { name: 'block-' + key, media, bytes: css.length, css, copies: [] };
    b.copies.push(f.replace(/\.html$/, ''));
    blocks.set(key, b);
  }
}
const sheets = [...blocks.values()].sort((a, b) => b.bytes - a.bytes || a.name.localeCompare(b.name));

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent('<!doctype html><html><head></head><body></body></html>');
const result = await page.evaluate((sheets) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
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
          : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith("--")) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      // A nested style rule (CSS nesting) keeps its own children.
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    const ss = new CSSStyleSheet({ media: s.media || undefined });
    try { ss.replaceSync(s.css); } catch (e) { rules.push({ file: s.name, error: String(e) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts };
}, sheets.map(({ name, media, css }) => ({ name, media, css })));

// ---------------------------------------------------------------- resolution
//
// Each name is also resolved the way the browser resolves it: a probe document carries the bundle
// on <html> (light) and <html class="dark"> (dark), every name is read on a probe under <body>, and
// colours come back as sRGB, lengths as px. Viewport 1440 x 900.
const page2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const shell = (mode) => '<!doctype html><html class="' + (mode === 'dark' ? 'dark' : '') + '" lang="en-US"><head>'
  + sheets.map((s) => '<style' + (s.media ? ' media="' + s.media + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div><div><div id="probe-sidebar"></div></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.error && !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const [pass, mode] of [['light', 'light'], ['dark', 'dark']]) {
  await page2.setContent(shell(mode), { waitUntil: 'load' });
  resolved[pass] = await page2.evaluate((names) => {
    // A custom property can hold a url() with a signed or per-account query: record it as url(…).
    // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const rootProbe = document.getElementById('probe-root');
    const sideProbe = document.getElementById('probe-sidebar');
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
      const el = name.startsWith('--df-') ? sideProbe : rootProbe;
      const raw = noUrl(getComputedStyle(el).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      const hsl = /^-?[\d.]+(deg)? [\d.]+% [\d.]+%$/.test(raw);
      const asColor = hsl ? `hsl(${raw})` : raw;
      probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0';
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
      else if (CSS.supports('color', asColor) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
        probe.style.color = asColor; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color); if (hsl) r.hslTriplet = true;
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
}
await browser.close();


const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || "")) return "utility";
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties' || c === '@layer theme')) return 'tailwind';
  if (names.some((n) => /^--(oai|brand)-/.test(n))) return 'oai';
  return 'app';
};
const ok = result.rules.filter((r) => !r.error);
for (const r of ok) r.bin = binOf(r);

const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "TokenTracker v1.4.3's dashboard CSS bundle, fetched from the local server at http://127.0.0.1:7680/assets/ (one Vite bundle)",
  sheets: sheets.map(({ name, media, bytes }) => ({ name, media, bytes })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { oai: names('oai').length, app: names('app').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.rules.filter((r) => r.error),
  oai: ok.filter((r) => r.bin === 'oai'),
  app: ok.filter((r) => r.bin === 'app'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}`);
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names oai ${out.counts.names.oai}, app ${out.counts.names.app}, tailwind ${out.counts.names.tailwind}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 160)}`);
