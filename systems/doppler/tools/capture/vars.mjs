// Reads every custom property doppler.com's stylesheets declare and writes
// raw/css-vars.json; also harvests the named Tailwind utility classes
// (the site's real token layer) into raw/utility-classes.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// doppler.com is a Next.js marketing site over Tailwind v3. Its custom
// properties are few — --font-doppler-repro(-mono), --font-inter,
// --global-ease, --global-transition, --spacing-1, --anchor-gap — because the
// design layer lives in named utility classes instead: a custom palette
// (warm-black, basalt, charcoal, warm-white, silver, aluminum, brand-orange /
// carmine, purple, light-purple, lilac, flourescent-green, flourescent-red,
// the black<N> warm-white translucencies, subtle-*, glow-stroke-*), a named
// type ramp (.text-h1Mobile/.text-h2Mobile/.text-h3/.text-h4/.text-p1-3/
// .text-label/.text-small/.text-navLink/.text-code), named shadows
// (shadow-medium-dark, shadow-people) and 1/8/16px border utilities. The
// linked /_next/static/css/*.css bundles are same-origin; bodies are read
// from the network responses, inline <style> blocks through the CSSOM, then
// re-parsed in the page with a constructed CSSStyleSheet — the same parse the
// browser does. Every rule declaring a --* property is kept with its selector
// and enclosing @media/@layer context; @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets
// (one pass: the site paints a single dark theme on :root), computed the way
// the browser computes it: colours come back as sRGB hex, lengths as px at
// 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared
//   app       any other custom property the site's own sheets declare
//   vendor    embedded widget vars (Marketo forms, consent, chat)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
// An edge-block page can greet a fresh client: retry on a fresh context until
// the real document (with its sheets) arrives, then harvest. Two routes are
// visited so late-loading bundles land too: the marketing home ('/') and the
// demo-request page ('/demo'), each with its own context.
const bodies = new Map();
const inlines = [];
for (const route of ['/', '/demo']) {
  let got = false;
  for (let tries = 0; tries < 6 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(6000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inl = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + location.pathname.replace(/\//g, '') + '-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      inlines.push(...inl);
      got = true;
      await context.close();
      break;
    }
    console.log(route, 'challenge page, fresh context (try ' + (tries + 1) + ')');
    await context.close();
  }
  if (!got) console.log(route, 'blocked by the edge on every try; its sheets are missing');
}
if (!bodies.size && !inlines.length) { console.log('no stylesheets harvested; css-vars.json not written'); await browser.close(); process.exit(2); }
// inline sheets read via CSSOM; link sheets via the captured bodies
const sheets = [...bodies.entries()].concat(inlines);

// ---- harvest: every rule with --* declarations ----
// The probe resolves vw/vh/dvh and @media at the 1440 x 900 the notes below claim; a bare
// browser.newPage() would give Playwright's 1280 x 720 default (finding 19-1).
const probe = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const utils = [];
  // The utility-class harvest: one-class selectors (Tailwind's named custom
  // palette, type ramp, shadows and radii live here, not in custom
  // properties). Responsive/hover variants are recorded under the same name
  // with their context. Arbitrary-value classes ([#fff] etc.) are kept too —
  // they are painted values, flagged by their bracketed selector.
  const KEEP_PROP = /^(color|background-color|border-color|border.*-color|fill|stroke|caret-color|outline-color|text-decoration-color|--tw-gradient-from|--tw-gradient-to|--tw-gradient-stops|font-family|font-size|font-weight|line-height|letter-spacing|text-transform|border-radius|border.*-radius|box-shadow|--tw-shadow|border-width|border.*-width|text-decoration|opacity|transition.*|animation.*)$/;
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
      // Utility harvest: rules whose selector is a list of plain classes
      // (.a, .a:hover, .b) — record the class list and the kept props.
      const sel = r.selectorText || '';
      const simple = sel.trim() && sel.split(',').every((s) => /^\s*\.[-_a-zA-Z0-9\\[\]().%#\/:]+(:[a-z-]+(\([^)]*\))?)?\s*$/.test(s.trim()));
      if (simple) {
        const up = {};
        let un = 0;
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (KEEP_PROP.test(k)) { up[k] = noUrl(r.style.getPropertyValue(k).trim()); un++; }
        }
        // A shorthand holding var() serialises as empty longhands; fall back
        // to the shorthand itself so .border-aluminum keeps its colour.
        const shorthand = (long, short) => {
          if (long.every((k) => up[k] === '')) { const v = noUrl(r.style.getPropertyValue(short).trim()); if (v) { for (const k of long) delete up[k]; up[short] = v; } }
        };
        shorthand(['border-top-color', 'border-right-color', 'border-bottom-color', 'border-left-color'], 'border-color');
        shorthand(['border-top-width', 'border-right-width', 'border-bottom-width', 'border-left-width'], 'border-width');
        shorthand(['border-top-style', 'border-right-style', 'border-bottom-style', 'border-left-style'], 'border-style');
        shorthand(['border-top-left-radius', 'border-top-right-radius', 'border-bottom-right-radius', 'border-bottom-left-radius'], 'border-radius');
        if (Object.keys(up).length) utils.push({ file, selector: sel.slice(0, 220), context: ctx, properties: up });
      }
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors, utils };
}, sheets);

// ---- resolution: probe document with the real sheets ----
// One pass: doppler.com declares no theme mechanism (no data-theme, no .dark
// class, no prefers-color-scheme block that re-binds roles) — the whole
// surface paints the same dark theme from :root.
const shell = (attrs) => '<!doctype html><html ' + attrs + '><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
const PASSES = [
  ['dark', ''],
];
for (const [pass, attrs] of PASSES) {
  await probe.setContent(shell(attrs), { waitUntil: 'load' });
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
      else if ((m = c.match(/^rgb\(([\d.]+) ([\d.]+) ([\d.]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => +v); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^color\(srgb ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklch\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^hsla?\(([\d.]+)deg?,\s*([\d.]+)%,\s*([\d.]+)%(?:,\s*([\d.]+))?\)$/))) {
        const h = +m[1] / 360, s = +m[2] / 100, l = +m[3] / 100;
        const q = l < 0.5 ? l * (1 + s) : l + s - l * s, pp = 2 * l - q;
        const hue = (t) => { if (t < 0) t += 1; if (t > 1) t -= 1; if (t < 1 / 6) return pp + (q - pp) * 6 * t; if (t < 1 / 2) return q; if (t < 2 / 3) return pp + (q - pp) * (2 / 3 - t) * 6; return pp; };
        rgb = [hue(h + 1 / 3), hue(h), hue(h - 1 / 3)].map((v) => Math.round(v * 255)); a = m[4] === undefined ? 1 : +m[4];
      }
      else return { unparsed: c };
      a = Math.round(a * 1000) / 1000;
      return a === 1 ? '#' + rgb.map((v) => Math.round(v).toString(16).padStart(2, '0')).join('') : `rgba(${rgb.map(Math.round).join(', ')}, ${a})`;
    };
    const out = {};
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
      } else if (!raw.includes('%') && CSS.supports('width', raw)) { p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
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

const THEME = /^--(color|font|text|spacing|radius|breakpoint|container|shadow|inset-shadow|drop-shadow|ease|animate|blur|perspective|aspect|leading|tracking|weight|default|sizing|grid|flex|z|opacity|global|anchor|vh)-?/;
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|stripe|mkto|marketo|hs-|hubspot|drift|intercom|onetrust|ketch|termly|osano|data-org-theme/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (r.context.some((c) => c === '@layer theme') || names.every((n) => THEME.test(n))) return 'theme';
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
  source: 'the stylesheet bodies read during live loads of the marketing home and the demo-request page on doppler.com (the linked /_next/static/css/*.css bundles from network responses plus inline <style> blocks, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets on :root (the site paints one dark theme) at 1440 x 900',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    utilityRules: result.utils.length,
    names: { theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');

// The utility-class harvest: doppler.com's real token layer. Dedupe by
// selector + context so the same class seen in two sheets records once.
const seen = new Set();
const utils = [];
for (const u of result.utils) {
  const k = u.selector + ' | ' + u.context.join(' ');
  if (seen.has(k)) continue;
  seen.add(k);
  utils.push(u);
}
fs.writeFileSync(path.join(REF, 'raw', 'utility-classes.json'), JSON.stringify({
  readAt: out.readAt,
  source: 'the same harvested stylesheet bodies as css-vars.json: every rule whose selector is a plain class list (.bg-brand-orange, .text-h3, .rounded-16, .shadow-medium-dark, hover/focus/responsive variants) with its colour, type, radius, shadow, border and motion declarations',
  classes: utils,
}, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`utility-classes.json: ${utils.length} class rules`);
console.log(`resolved: dark ${Object.keys(resolved.dark).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
