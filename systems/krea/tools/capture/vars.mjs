// Reads the custom properties krea.ai's public stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// krea.ai serves two public stylesheet families signed out, kept apart:
//
//   app        www.krea.ai /, /pricing, /enterprise, /login, /blog, /image —
//              a Tailwind v4 token layer on :root,:host. Colour ramps
//              (--color-*-50..950), semantic roles (--color-primary-*,
//              --color-action, --color-canvas), type (--font-sans,
//              --font-mono, --text-*), radius and spacing. The painted theme
//              is the `dark` class on <html> (body is dark:bg-primary-950).
//              Resolved once with html.dark and once with html.light so the
//              dark: utilities that the class switches can be compared.
//   docs       /docs — a light documentation shell (html.light). Its own
//              sheets are harvested and resolved separately so docs colours
//              do not leak into the app token set.
//
// Styles arrive as linked CSS bundles plus inline <style> blocks. Only the
// sheets a document actually applies are kept: each document's
// document.styleSheets list, in cascade order, is the source of truth (a
// bundle the page merely prefetched, or one a neighbouring surface uses, is
// not applied and never enters the harvest). Linked bodies come from the
// network responses (or a direct fetch when the response was missed), inline
// <style> blocks through the CSSOM, then everything is re-parsed in a probe
// page with a constructed CSSStyleSheet — the same parse the browser does.
// A surface's variables are resolved from its primary document alone, so one
// page's styles never leak into another page's resolution; extra documents
// of a surface are harvested for evidence only, under their own file names.
// Every rule declaring a
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
  { name: 'app', url: BASE + '/', colorScheme: 'dark', extra: [
    { key: 'pricing', url: BASE + '/pricing' },
    { key: 'enterprise', url: BASE + '/enterprise' },
    { key: 'blog', url: BASE + '/blog' },
    { key: 'login', url: BASE + '/login' },
  ] },
  { name: 'docs', url: BASE + '/docs', colorScheme: 'light' },
];
// The sheets one loaded document applies, in cascade order: linked sheets by
// href (bodies from the recorded responses, fetched directly when missed),
// inline sheets through the CSSOM. Disabled sheets and sheets whose media
// query does not match are not applied and are skipped.
async function appliedSheets(p, context, seen, prefix) {
  const list = await p.evaluate(() => [...document.styleSheets].map((s, i) => {
    const media = s.media && s.media.mediaText;
    if (s.disabled || (media && media !== 'all' && !matchMedia(media).matches)) return null;
    if (s.href) return { href: s.href };
    try { return { name: 'inline-' + i, css: [...s.cssRules].map((r) => r.cssText).join('\n') }; } catch { return null; }
  }).filter(Boolean));
  const bodies = new Map();
  for (const sheet of list) {
    if (sheet.css !== undefined) { bodies.set(prefix + sheet.name, sheet.css); continue; }
    const key = sheet.href.split('?')[0];
    let text = seen.get(key);
    if (text === undefined) text = await context.request.get(sheet.href).then((r) => r.text()).catch(() => undefined);
    if (text !== undefined) bodies.set(key, text);
  }
  return bodies;
}
// name -> { primary: Map<sheetName, cssText> (the resolution document),
//           extras: Map<sheetName, cssText> (other documents, evidence only) }
const perSurface = new Map();
for (const surface of SURFACES) {
  let loaded = null;
  for (let tries = 0; tries < 6 && !loaded; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: surface.colorScheme });
    await patch(context);
    const p = await context.newPage();
    const seen = new Map(); // every stylesheet response this context saw, by URL; used as a body cache only
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { seen.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(surface.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(6000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const primary = await appliedSheets(p, context, seen, '');
      // Other documents of the surface (pricing, enterprise, blog, login share the app bundle) are
      // read on their own load: their applied sheets are kept apart from the primary document's.
      const extras = new Map();
      for (const extra of surface.extra || []) {
        await p.goto(extra.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        await p.waitForTimeout(4000);
        for (const [n, t] of await appliedSheets(p, context, seen, extra.key + ':')) {
          if (!primary.has(n) && !extras.has(n)) extras.set(n, t);
        }
      }
      loaded = { primary, extras };
      await context.close().catch(() => {});
      break;
    }
    console.log(`${surface.name}: challenge page, fresh context (try ${tries + 1})`);
    await context.close();
  }
  if (!loaded) { console.log(`${surface.name}: blocked by the edge on every try`); continue; }
  perSurface.set(surface.name, loaded);
  console.log(`${surface.name}: ${loaded.primary.size} applied sheets` + (loaded.extras.size ? ` + ${loaded.extras.size} from other documents` : ''));
}
if (!perSurface.size) { console.log('no surface loaded; css-vars.json not written'); await browser.close(); process.exit(2); }

// ---- harvest: every rule with --* declarations, per surface ----
const probe = await browser.newPage({ viewport: { width: 1440, height: 900 } });   // the size every vw/vh note names
const allRules = [];
const allFonts = [];
const allErrors = [];
for (const [surface, { primary, extras }] of perSurface) {
  const sheets = [...primary.entries(), ...extras.entries()];
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
  for (const r of result.rules) { r.surface = surface; r.primary = primary.has(r.file); allRules.push(r); }
  for (const f of result.fonts) { f.surface = surface; allFonts.push(f); }
  allErrors.push(...result.errors);
}

// ---- resolution: probe document per surface, with the real sheets ----
// The app paints with html.dark (a dark class, not a media query). Docs
// paints html.light. Every pass resolves the vars on
// document.documentElement at 1440 x 900. The light pass on the app sheets
// records what the same declarations compute without the dark class; it is
// not evidence that the product ships a public light theme.
const shell = (sheets, cls) => '<!doctype html><html' + (cls ? ' class="' + cls + '"' : '') + '><head>'
  + [...sheets.values()].map((css) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const PASSES = [
  { pass: 'appDark', surface: 'app', cls: 'dark' },
  { pass: 'appLight', surface: 'app', cls: 'light' },
  { pass: 'docsLight', surface: 'docs', cls: 'light' },
];
const resolved = {};
for (const { pass, surface, cls } of PASSES) {
  const loaded = perSurface.get(surface);
  if (!loaded) continue;
  const bodies = loaded.primary;
  // Only the primary document's own sheets decide the resolution.
  const rules = allRules.filter((r) => r.surface === surface && r.primary);
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
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
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
      } else if (/^-?(\d*\.)?\d+em$/.test(raw)) {
        // A font-relative length (--tracking-wide: .025em) is kept as declared: resolving it through the probe's
        // width would freeze it into pixels at the probe's own font size, and the exported letter spacing would
        // stop following the text it is applied to.
        r.kind = 'dimension'; r.value = raw; r.note = 'font-relative, kept as declared';
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
for (const [surface, { primary, extras }] of perSurface) {
  for (const [n, t] of primary) allSheets.push(`${surface}: ${n} (${t.length} bytes)`);
  for (const [n, t] of extras) allSheets.push(`${surface} (other document): ${n} (${t.length} bytes)`);
}
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheets each document applied (document.styleSheets, in cascade order) during live signed-out loads of www.krea.ai on 2026-11-18 (/ for the app shell, with /pricing, /enterprise, /blog and /login harvested for evidence under their own file names; /docs for the documentation shell — linked CSS bundles plus inline <style> blocks, re-parsed with CSSStyleSheet); resolved in probes carrying each surface\'s primary-document sheets — the app once with html.dark (the painted theme) and once with html.light (a comparison, not a shipped public theme), docs once with html.light — at 1440 x 900.',
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
