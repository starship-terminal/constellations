// Reads every custom property factory.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// factory.com's Next.js marketing site declares a Tailwind-v4-style token
// layer in its served CSS bundles (~290 KB app.css plus small chunks, read
// from network responses, plus inline <style> blocks through the CSSOM):
// dark-first primitives (--dark-base-primary/secondary, --light-base-*,
// --neutral-100..1000, --surface-page/raised/sunken, --accent-100..300, the
// oklch colour scales --color-red-*/--orange-*/--amber-*/--emerald-*/
// --sky-*/--blue-*/--violet-*/--zinc-*), semantic roles
// (--color-background/--color-foreground/--color-base-100..1000/
// --color-accent-*/--color-surface-raised/--color-light/dark-base-*) remapped
// per [data-theme], the --text-* ramp with --line-height companions,
// --tracking-*/--leading-*/--font-weight-*, --font-geist-sans/
// --font-geist-mono/--font-japanese/--font-pixel, --radius-*, --container-*,
// --content-gutter/--content-column, --breakpoint-3xl, --blur-*, --ease-*,
// --default-transition-*, --spacing, plus component-level layers: --cli-*
// terminal palette, --factory-* brand vars, --sf-*/--fh-* effect vars,
// --shiki-* code highlighting and --hsf-* HubSpot form skin vars.
// <html data-theme="light"> ships on every marketing page; dark is the :root
// default, painted in scoped sections and selectable on docs.factory.com's
// theme toggle.
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets,
// once with data-theme="light" and once with data-theme="dark", computed the
// way the browser computes it: colours come back as sRGB hex, lengths as px
// at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared —
//             the --color-* roles and scales, the primitive scales
//             (--neutral-*, --accent-*, --surface-*, --dark-base-*,
//             --light-base-*), --text-*, --font-*, --spacing*, --radius-*,
//             --container-*, --content-*, --breakpoint-*, --shadow-*,
//             --ease-*, --animate-*, --blur-*, --tracking-*, --leading-*,
//             --weight-*, --default-*, --cli-*, --factory-*, --sf-*, --fh-*,
//             --sg-*, --shiki-*, --hsf-*, --reader-*, --web-demo-* ...
//   app       any other custom property the site's own sheets declare
//   vendor    embedded widget/framework vars (cookie banners, embeds)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
// An edge-block page (www's Cloudflare 403 shape) can greet a fresh client:
// retry on a fresh context until the real document (with its sheets)
// arrives, then harvest.
const bodies = new Map();
let page = null, inline = [];
for (let tries = 0; tries < 6 && !page; tries++) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(6000);
  if (await clearChallenge(p, { tries: 3, step: 1500 })) {
    page = p;
    inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
    break;
  }
  console.log('challenge page, fresh context (try ' + (tries + 1) + ')');
  await context.close();
}
if (!page) { console.log('blocked by the edge on every try; css-vars.json not written'); await browser.close(); process.exit(2); }
// inline sheets read via CSSOM; link sheets via the captured bodies
const sheets = [...bodies.entries()].concat(inline);
await page.close();

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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

// ---- resolution: probe document with the real sheets, light and dark ----
// factory.com's root palette is dark; [data-theme="light"] remaps the semantic
// layer. Setting data-theme="dark" selects the root defaults plus the dark
// color-scheme/shiki rules — the same state docs.factory.com's theme toggle
// produces.
// next/font scopes the font-name variables to generated .__variable_* classes
// that the real page carries on <body>; the probe copies those class names
// onto its own <body> so --font-geist-sans/--font-geist-mono resolve.
const probeClasses = [...new Set(result.rules
  .filter((r) => Object.keys(r.properties).some((k) => k.startsWith('--font-')))
  .flatMap((r) => (r.selector || '').match(/\.[\w-]+/g) || [])
  .map((s) => s.slice(1)))].join(' ');
const shell = (dark) => '<!doctype html><html' + (dark ? ' data-theme="dark"' : ' data-theme="light"') + '><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + `</head><body class="${probeClasses}"><div id="probe-root"></div></body></html>`;
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const pass of ['dark', 'light']) {
  await probe.setContent(shell(pass === 'dark'), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
    const p = document.createElement('div');
    box.appendChild(p);
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
      else if ((m = c.match(/^lab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) {
        // CIELAB D50 -> sRGB
        const fy = (num(m[1]) + 16) / 116, fx = fy + (+m[2]) / 500, fz = fy - (+m[3]) / 200;
        const eps = 216 / 24389, kap = 24389 / 27;
        const f = (t) => (t ** 3 > eps ? t ** 3 : (116 * t - 16) / kap);
        const X = 0.96422 * f(fx), Y = f(fy), Z = 0.82521 * f(fz);
        const r = 3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z, g = -0.9787684 * X + 1.9161415 * Y + 0.033454 * Z, bl = 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z;
        rgb = [r, g, bl].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255)); a = m[4] === undefined ? 1 : num(m[4]);
      }
      else return { unparsed: c };
      a = Math.round(a * 1000) / 1000;
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
    };
    const out = {};
    // Resolved on <body>: the page carries the font-name variables on
    // generated .__variable_* classes there, and :root/[data-theme] values
    // inherit down to it.
    for (const name of names) {
      const raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      p.removeAttribute('style');
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
      else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
        p.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(p).color);
        if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
      } else if (!raw.includes('%') && CSS.supports('width', raw)) {
        p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width;
        if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900';
        // max-content/min-content/fit-content/auto resolve to 0px on an empty
        // probe: keep the keyword instead of publishing a bogus length.
        if (r.value === '0px' && !/^[.\d]/.test(raw)) { r.value = raw; r.note = 'sizing keyword, not a fixed length'; }
      }
      else if (CSS.supports('box-shadow', raw)) { p.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(p).boxShadow; }
      else if (CSS.supports('transition-duration', raw)) { p.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(p).transitionDuration; }
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

const THEME = /^--(color|font|text|spacing|radius|breakpoint|container|content|grid|shadow|inset-shadow|drop-shadow|ease|animate|blur|perspective|aspect|leading|tracking|weight|font-weight|default|sizing|flex|z|opacity|background|divider|border|elevation|icon|surface|neutral|accent|dark-base|light-base|cli|factory|sf|fh|sg|shiki|hsf|reader|web-demo|dither|width|height|min-|max-|overflow|line|ink|destination)-?/;
const SKIN = /$^/; // factory declares no alternate theme skins
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|radix-|reka-|bits-|kb-accordion|hubspot/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (SKIN.test(r.selector || '') || r.context.some((c) => SKIN.test(c))) return 'skins';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n) || n.startsWith('--toast-'))) return 'vendor';
  if (r.context.some((c) => c === '@layer theme') || names.every((n) => THEME.test(n) || VENDOR.test(n))) return 'theme';
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
  source: 'the stylesheet bodies read during a live signed-out load of factory.com / (linked Next.js CSS bundles from network responses plus any inline <style> blocks via the CSSOM, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets with data-theme="light" and with data-theme="dark" (the state docs.factory.com\'s theme toggle produces; marketing pages always ship data-theme="light"), at 1440 x 900',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, skins: names('skins').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  skins: ok.filter((r) => r.bin === 'skins'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, skins ${out.counts.names.skins}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
