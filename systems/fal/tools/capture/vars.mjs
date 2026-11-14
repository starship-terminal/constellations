// Reads the custom properties fal.ai's public stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// fal.ai serves three surfaces signed out, each with its own sheet set and
// token layer, so the harvest runs three signed-out loads and keeps the
// surfaces apart:
//
//   marketing  fal.ai /, /pricing, /serverless — a Webflow build. Webflow's
//              --brand-colors--* / --background-color--* / --text-color--*
//              aliases plus the page's own variables on :root; a single
//              theme. Focal Web / Focal Text / Hal Timezone faces.
//   app        /explore, /models/*, /login — the Next.js app. A Tailwind v4
//              token layer (~450 names on :root,:host): the colour scales,
//              --primary-/--secondary-/--error-/--info-/--success-/
//              --warning-* scales held as raw `H S% L%` triplets, the
//              --surface-*/--content-*/--stroke-*/--overlay-*/--shadow-*
//              semantic roles, --accent-* families, --product-banner-*,
//              the --font-*/--text-* type layer, --radius-*, --spacing,
//              --ease-*, --breakpoint-*, --container-*. The theme is a class
//              on <html>: `light` or `dark`, resolved per class.
//   docs       /docs/* — the fumadocs documentation. Its own var layer
//              (--primary/-light/-dark as RGB triplets, --gray-*, the
//              --font-family-*-custom and --font-inter/--font-paper-mono
//              faces, --background-light/-dark), themed by a `light`|`dark`
//              class on <html> (data-theme-preference decides which).
//
// Styles arrive as linked CSS bundles plus inline <style> blocks. External
// bodies are read from the network responses, inline <style> blocks through
// the CSSOM, then re-parsed in a probe page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its surface, selector and enclosing
// @media/@layer context, and @font-face rules are kept too. Each surface's
// variables are then resolved in a probe document carrying that surface's
// real sheets — app and docs once per theme class — the way the browser
// computes it.
//
// Bins:
//   theme     design-token-looking names wherever they are declared
//   app       any other custom property the surface's own sheets declare
//   vendor    embedded widget/consent vars (dg-consent, recaptcha)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties, @utility
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
// Each surface is loaded once signed out; its response bodies and inline
// sheets are collected under that surface's name. A challenge page (a
// Cloudflare "just a moment") can greet a fresh client: retry the surface on
// a fresh context until the real document arrives.
const SURFACES = [
  { name: 'marketing', url: BASE + '/', colorScheme: 'light', extra: [BASE + '/pricing'] },
  { name: 'app', url: BASE + '/models/krea/v3/text-to-image', colorScheme: 'dark' },
  { name: 'docs', url: BASE + '/docs/documentation', colorScheme: 'light' },
];
const perSurface = new Map(); // name -> Map<sheetName, cssText>
for (const surface of SURFACES) {
  const bodies = new Map();
  let page = null;
  for (let tries = 0; tries < 6 && !page; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: surface.colorScheme });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(surface.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(6000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      // Pricing shares the marketing sheets and adds its own page styles.
      for (const extra of surface.extra || []) {
        await p.goto(extra, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        await p.waitForTimeout(4000);
      }
      page = p;
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      for (const [n, t] of inline) bodies.set(n, t);
      await context.close().catch(() => {});
      break;
    }
    console.log(`${surface.name}: challenge page, fresh context (try ${tries + 1})`);
    await context.close();
  }
  if (!page) { console.log(`${surface.name}: blocked by the edge on every try`); continue; }
  perSurface.set(surface.name, bodies);
  console.log(`${surface.name}: ${bodies.size} sheets`);
}
if (!perSurface.size) { console.log('no surface loaded; css-vars.json not written'); await browser.close(); process.exit(2); }

// ---- harvest: every rule with --* declarations, per surface ----
const probe = await browser.newPage();
const allRules = [];
const allFonts = [];
const allErrors = [];
for (const [surface, bodies] of perSurface) {
  const sheets = [...bodies.entries()];
  const result = await probe.evaluate((sheets) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const errors = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
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
  for (const r of result.rules) { r.surface = surface; allRules.push(r); }
  for (const f of result.fonts) { f.surface = surface; allFonts.push(f); }
  allErrors.push(...result.errors);
}

// ---- resolution: probe document per surface, with the real sheets ----
// App and docs scope their themes on an <html> class (`light`|`dark`);
// marketing is a single-theme :root. Every pass resolves the vars on
// document.documentElement (and falls back to body when a surface scopes
// lower), at 1440 x 900.
const shell = (sheets, cls) => '<!doctype html><html' + (cls ? ' class="' + cls + '"' : '') + '><head>'
  + [...sheets.values()].map((css) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const PASSES = [
  { pass: 'marketing', surface: 'marketing', cls: '' },
  { pass: 'appLight', surface: 'app', cls: 'light' },
  { pass: 'appDark', surface: 'app', cls: 'dark' },
  { pass: 'docsLight', surface: 'docs', cls: 'light' },
  { pass: 'docsDark', surface: 'docs', cls: 'dark' },
];
const resolved = {};
for (const { pass, surface, cls } of PASSES) {
  const bodies = perSurface.get(surface);
  if (!bodies) continue;
  const rules = allRules.filter((r) => r.surface === surface);
  const want = [...new Set(rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
    .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
  await probe.setContent(shell(bodies, cls), { waitUntil: 'load' });
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
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')) : `rgba(${rgb.join(', ')}, ${a})`;
    };
    const out = {};
    const host = document.documentElement;
    for (const name of names) {
      // The theme class lives on <html>, so the variables resolve on the root.
      let raw = noUrl(getComputedStyle(host).getPropertyValue(name).trim());
      if (!raw) raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
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

const THEME = /^--(surface|content|stroke|overlay|shadow|accent|primary|secondary|error|info|success|warning|product-banner|font|text|radius|spacing|ease|animate|animation|default|breakpoint|container|color-|red|orange|amber|yellow|lime|green|teal|cyan|sky|blue|indigo|violet|purple|pink|rose|gray|zinc|neutral|black|white|brand|background|tooltip|mask|blur|scrollbar|borders|grid|full|half|start|end|trim|window|actions|button|divider|icon|border|elevation|default-border|nav|header|sidebar|input|code|card|popover|dialog|docs|prose|leading|tracking|weight|inset-shadow|drop-shadow|perspective|aspect|sizing|flex|z|opacity|chart|kbd)-?/;
const VENDOR = /dg-consent|onetrust|ot-sdk|cookie|recaptcha|grecaptcha|intercom|stripe|sonner|--toast-|\.s-mode|\.s-theme|data-org-theme|--s-|inkeep|algolia|docsearch/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties' || /^@utility/.test(c))) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n) || n.startsWith('--toast-'))) return 'vendor';
  if (r.context.some((c) => c === '@layer theme' || c === '@layer base') || names.every((n) => THEME.test(n) || VENDOR.test(n))) return 'theme';
  return 'app';
};
const ok = allRules;
for (const r of ok) r.bin = binOf(r);
const bySelector = {};
for (const r of ok) {
  const key = `[${r.surface}:${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const allSheets = [];
for (const [surface, bodies] of perSurface) for (const [n, t] of bodies) allSheets.push(`${surface}: ${n} (${t.length} bytes)`);
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during live signed-out loads of fal.ai (/ and /pricing for the Webflow marketing surface, /models/krea/v3/text-to-image for the Next.js app surface, /docs/documentation for the fumadocs docs surface — linked CSS bundles from network responses plus inline <style> blocks, re-parsed with CSSStyleSheet); resolved in probes carrying each surface\'s real sheets — the app and docs once per theme class on <html> (light/dark), marketing once — at 1440 x 900.',
  sheets: allSheets,
  counts: {
    rules: ok.length,
    fonts: allFonts.length,
    names: { theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: allErrors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: allFonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${allFonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: ${Object.entries(resolved).map(([k, v]) => `${k} ${Object.keys(v).length}`).join(', ')}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 150)}`);
