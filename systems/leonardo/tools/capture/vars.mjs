// Reads every custom property Leonardo.Ai's public stylesheets declare and
// writes raw/css-vars.json. Three signed-out surfaces:
//   marketing  leonardo.ai — Tailwind v4 layer (--color-*, --background,
//              --foreground, --accent, --radius, --font-*)
//   app        app.leonardo.ai — the signed-out shell (--accent-brand,
//              --background, --border-*, --sidebar-*, --primary-brand)
//   docs       docs.leonardo.ai — ReadMe (--project-color-*, --recipe-button-*)
// The product ships one dark theme on each surface. Resolution runs plain,
// data-theme=light and data-theme=dark; light and dark match when no theme
// attribute exists.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, DOCS, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch({ colorScheme: 'dark' });
const SURFACES = [
  { name: 'marketing', url: BASE + '/' },
  { name: 'app', url: APP + '/' },
  { name: 'docs', url: DOCS + '/docs/getting-started' },
];
const bodies = new Map();
const inline = [];
for (const surface of SURFACES) {
  let got = false;
  for (let tries = 0; tries < 4 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      const rt = r.request().resourceType();
      if (rt !== 'stylesheet' && !/text\/css/.test(r.headers()['content-type'] || '')) return;
      try { bodies.set(surface.name + ' ' + r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(surface.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (await clearChallenge(p, { tries: 8, step: 1500 })) {
      await p.waitForTimeout(2500);
      const blocks = await p.evaluate((name) => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return [name + ' inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean), surface.name);
      inline.push(...blocks);
      console.log(surface.name, 'sheets', bodies.size, 'inline', blocks.length);
      got = true;
    } else console.log(surface.name, 'challenge try', tries + 1);
    await context.close();
  }
  if (!got) console.log(surface.name, 'blocked; continuing with other surfaces');
}
const sheets = [...bodies.entries()].concat(inline);
if (!sheets.length) { console.log('no sheets harvested'); await browser.close(); process.exit(2); }

// ---- harvest: every rule with --* declarations ----
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const probe = await probeCtx.newPage();
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

// ---- resolution: one probe document per host, then light and dark ----
// Marketing, the app and the docs all declare names such as --font-weight-bold
// and --radius. Loading every sheet into one page lets the last host win, so
// each host is resolved in its own document and the readings stay separate.
const HOSTS = ['marketing', 'app', 'docs'];
const hostOf = (file) => HOSTS.find((h) => file.startsWith(h + ' ')) || 'other';
const sheetsByHost = Object.fromEntries(HOSTS.map((h) => [h, sheets.filter(([n]) => hostOf(n) === h)]));
const shell = (hostSheets, attr, cls) => '<!doctype html><html' + (attr ? ' ' + attr : '') + '><head>'
  + hostSheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-wrap"' + (cls ? ' class="' + cls + '"' : '') + '><div id="probe-root"></div></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
const resolvedByHost = {};
// dji.com scopes its semantic layer to section classes, not a root
// attribute: `:root .light-theme` and `:root .dark-theme` re-declare
// --primary/--bg/--border/… (section wrappers opt into dark or light
// paint — the dark hero sections are themed, not baked). The plain and
// data-theme passes resolve the unscoped layer (identical — no theme
// attribute ships); the theme passes compute inside a wrapper carrying
// the product's own class. Each pass runs once per host so a shared name
// keeps the value that host declared.
const PASSES = {
  plain: ['', ''],
  light: ['data-theme="light"', ''],
  dark: ['data-theme="dark"', ''],
  colorModeLight: ['data-color-mode="light"', ''],
  colorModeDark: ['data-color-mode="dark"', ''],
  htmlDark: ['class="dark"', ''],
};
for (const host of HOSTS) resolvedByHost[host] = {};
for (const [pass, [attr, cls]] of Object.entries(PASSES)) {
  resolved[pass] = {};
  for (const host of HOSTS) {
    if (!sheetsByHost[host].length) continue;
    await probe.setContent(shell(sheetsByHost[host], attr, cls), { waitUntil: 'load' });
    // Each host's reading goes into its own object. Writing it to
    // resolved[pass] made the last host (docs) the merge target, so the
    // product-first merge below kept docs values for shared names.
    const got = await probe.evaluate((names) => {
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
    const holder = document.documentElement;
    for (const name of names) {
      const raw = noUrl(getComputedStyle(holder).getPropertyValue(name).trim());
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
        // font-relative units (em/rem) resolve against the probe's font size
        // and stop scaling with the element's own font — keep them as declared.
        if (/(em|rem)$/.test(raw)) { r.value = raw; r.note = 'font-relative length, kept as declared'; }
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
    resolvedByHost[host][pass] = got;
  }
  // Publish one flat pass for readers that still look up a name once.
  // A name only one host declares keeps that reading. A name several
  // hosts declare keeps the product host (app, then marketing): docs
  // ReadMe names such as --font-weight-bold must not overwrite it.
  // resolvedByHost keeps every host, so a later rebuild can pick explicitly.
  for (const host of ['app', 'marketing', 'docs']) {
    for (const [name, reading] of Object.entries(resolvedByHost[host][pass] || {})) {
      if (!(name in resolved[pass])) resolved[pass][name] = { ...reading, host };
    }
  }
}
await probeCtx.close().catch(() => {});
await browser.close();

const THEME = /^--(color|semantics|grey|ember|peach|vivid|pastel|extended|overlay|switch|selection|dds|safe-area|icon|surface|gradient|theme|spacing|space|radius|shadow|font|icon|z|breakpoint|size|duration|ease|motion|weight|leading|tracking|line-height|grid|full-screen|common|dji|atom|header|footer|nav|text|button|border|input|scale|chart|status|toast|overlay2|amber|black|blue|brown|crimson|cyan|emerald|fuchsia|gold|grass|gray|green|indigo|lime|neutral|orange|pink|plum|purple|red|rose|ruby|sand|sky|slate|stone|teal|tomato|violet|white|yellow|zinc|blurple|greyple|brand|illo|font|display|text|fg|background|bg|foreground|card|popover|primary|secondary|muted|accent|destructive|border|input|ring|chart|sidebar|avatar|surface|elevation|shadow|duration|error|info|warning|success|toast|overlay|size|grid|tag|note|z|radius|spacing|ease|breakpoint|leading|tracking|weight|opacity|app|badge|button|control|status|chat|channel|embed|guild|header|icon|interactive|mention|message|modal|notice|premium|scrim|search|spine|spoiler|switch|theme|user|voice|activity|nitro|expressive|feedback|focus|mod|refresh|mobile|dark|always|off|dim|vivid|spring|mint|ekko|pinc|navy|application|custom|safe|semantic|global|new|legacy|deprecated|unsafe|ansi|channels|channeltextarea|checkbox|checkpoint|chip|collectibles|content|context|creator|datepicker|experimental|form|gradient|guildbar|hexagon|home|hypesquad|inlinenotice|keyword|logo|lol|menu|motion|navigator|not|num|page|panel|platform|polls|profile|progressbar|quest|radio|reaction|redesign|role|scrollbar|section|select|slider|space|standard|steam|tabs|textbox|thread|togglebutton|transparent)-?/;
const SKIN = /^\.(crazy|stealth|premium|high-contrast|barbie|nineties|legacy)\b/;
const VENDOR = /video-js|vjs-|stripe|sonner|geist|osano-cm|--s-|--chakra-|gdpr|__nextjs|clerk|radix|hcaptcha|--w-\w+-ix|webflow|w-mod/i;
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
  source: 'stylesheet bodies from signed-out loads of leonardo.ai/, app.leonardo.ai/ and docs.leonardo.ai/docs/getting-started on 2026-11-18 (linked CSS from network responses plus inline style blocks, re-parsed with CSSStyleSheet); resolved in a probe carrying those sheets, plain and data-theme=light|dark on html, at 1440 x 900. Each public surface ships one dark theme.',
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
  resolvedByHost,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, skins ${out.counts.names.skins}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: ${Object.keys(resolved).map((k) => k + ' ' + Object.keys(resolved[k]).length).join(', ')}`);
console.log(`resolvedByHost: ${HOSTS.map((h) => h + ' ' + Object.keys(resolvedByHost[h].plain || {}).length).join(', ')}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
