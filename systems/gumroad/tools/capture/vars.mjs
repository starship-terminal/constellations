// Reads every custom property gumroad.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// gumroad.com (and the <creator>.gumroad.com product pages) serve one Vite
// bundle, assets.gumroad.com/vite/assets/entrypoints/design-*.css —
// CROSS-ORIGIN, invisible to the CSSOM, so bodies are read from network
// responses. The declared layer is a Tailwind v4 @theme plus a hand-written
// semantic layer:
//   --pink --purple --green --orange --red --yellow --gray --dark-gray
//                                   the flat brand palette
//   --accent --primary --color --filled --black --success --warning
//   --danger --info --neutral-* --indicator --accent-with-text
//                                   semantic roles as `R G B` channel
//                                   triplets consumed as rgb(var(--x)),
//                                   with --contrast-* foreground partners
//   --color-*                       the same roles wrapped rgb(var(--x)/a)
//                                   plus the Tailwind palette (oklch)
//   --body-bg --active-bg --border-alpha --border-width --border-radius-1..3
//   --box-shadow-1/2                the hard offset shadows
//   --spacer-1..8 --spacing --form-element-height --main-stack-width
//   --dynamic-grid --spacing-product-page --grid-cols-sidebar --breakpoint-*
//   --font-family 'ABC Favorit' --font-sans/-mono --text-xs..9xl
//   --font-weight-* --tracking-* --leading-*
//   --radius-xs..3xl --radius --ease-* --animate-* --default-transition-*
//   --transition-duration --button-hover-offset --big-icon-size
//   --z-index-* --disabled-opacity --logo --loading-spinner
//   --product-cover-placeholder --container-* --aspect-video
// Theme is @media (prefers-color-scheme:dark): a second :root block swaps the
// triplets (--body-bg #242423, --color/--filled, --border-alpha .35) and the
// markup carries dark:* utilities. There is no in-page toggle.
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets,
// once under colour-scheme light and once under dark (the emulation is the
// product's own theme mechanism), computed the way the browser computes it:
// channel triplets come back as sRGB hex, lengths as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared
//   darkscope the @media (prefers-color-scheme:dark) re-point rules
//   app       any other custom property the site's own sheets declare
//   vendor    embedded widget vars (checkout/payments/players)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, PRODUCT_URL, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
const bodies = new Map();
const inline = [];
let bodyClass = '', htmlClass = '';
// The marketing pages and a product subdomain page share the one design-*.css
// bundle; both routes are loaded so per-surface inline styles and any extra
// sheet are harvested too.
for (const route of ['/', '/discover', PRODUCT_URL]) {
  let page = null;
  for (let tries = 0; tries < 4 && !page; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    const url = route.startsWith('http') ? route : BASE + route;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(9000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) page = p;
    else { console.log('challenge page, fresh context (try ' + (tries + 1) + ')'); await context.close(); }
  }
  if (!page) { console.log(route, 'blocked by the edge on every try; skipping'); continue; }
  inline.push(...(await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean))).map(([n, css]) => [route + ' ' + n, css]));
  if (!bodyClass) [bodyClass, htmlClass] = await page.evaluate(() => [document.body.className, document.documentElement.className]);
  await page.context().close();
}
if (!bodies.size && !inline.length) { console.log('no stylesheets captured; css-vars.json not written'); await browser.close(); process.exit(2); }
const sheets = [...bodies.entries()].concat(inline);

// ---- harvest: every rule with --* declarations ----
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
await patch(probeCtx);
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

// ---- resolution: probe document with the real sheets, both colour schemes ----
// The semantic names hold channel triplets ("255 144 232") consumed as
// rgb(var(--x)), or var() chains ("var(--accent)", "var(--color)/var(--border-alpha)").
// Reading getPropertyValue alone would publish the channels; instead each
// name is applied to a real typed property on a probe element inside the
// themed root, so the browser resolves the chain the way a component does:
//   colour    p.style.color = raw, then 'rgb('+raw+')' for triplets and
//             channel+var mixes
//   length    p.style.width = raw (a font-relative em keeps its note)
//   shadow    p.style.boxShadow = raw
//   duration  p.style.transitionDuration = raw
//   easing    a timing-function keyword or cubic-bezier() string
//   font      CSS.supports('font-family', raw)
// The probe carries the real page's own body/html classes, and the dark pass
// runs under the colour-scheme emulation — the media the dark :root block
// answers — never a class the product does not set.
const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
// The product subdomain pins its own light palette: its inline <style>
// declares an unlayered `:root` that beats the bundle's layered dark rules,
// so a product page never darkens. Resolving the merged sheets would invent
// a document that exists nowhere — each profile resolves only the sheets a
// real page of that kind carries.
const mainSheets = sheets.filter(([n]) => !n.startsWith(PRODUCT_URL));
const productSheets = sheets.filter(([n]) => !n.startsWith('/') || n.startsWith(PRODUCT_URL));
const shell = (profile) => '<!doctype html><html class="' + escAttr(htmlClass) + '"><head>'
  + profile.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="' + escAttr(bodyClass) + '"><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-|radix-|cmdk-)/.test(n)).sort();
const resolved = {};
for (const [key, profile] of [['light', mainSheets], ['dark', mainSheets], ['product-light', productSheets], ['product-dark', productSheets]]) {
  // gumroad.com's theme is @media (prefers-color-scheme:*), so the pass is
  // the emulated colour scheme — the same media the live page answers.
  const pass = key.endsWith('dark') ? 'dark' : 'light';
  await probe.emulateMedia({ colorScheme: pass });
  await probe.setContent(shell(profile), { waitUntil: 'load' });
  resolved[key] = await probe.evaluate((names) => {
    const readEl = document.getElementById('probe-root');
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:0;top:0;width:4000px;height:1000px;visibility:hidden';
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
      else if ((m = c.match(/^oklab\(([-\d.e]+%?|none) ([-\d.e]+|none) ([-\d.e]+|none)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]) || 0, m[2] === 'none' ? 0 : +m[2], m[3] === 'none' ? 0 : +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklch\(([-\d.e]+%?|none) ([-\d.e]+|none) ([-\d.e]+|none)(?: \/ ([\d.]+%?))?\)$/))) { const h = (m[3] === 'none' ? 0 : +m[3]) * Math.PI / 180, C = m[2] === 'none' ? 0 : +m[2]; rgb = fromOklab(num(m[1]) || 0, C * Math.cos(h), C * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^lab\(([-\d.e]+%?) ([-\d.e]+) ([-\d.e]+)(?: \/ ([\d.]+%?))?\)$/))) {
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
    // `R G B` channels, or the same with a var() inside ("var(--color)/var(--border-alpha)"):
    // the site's own semantic names are consumed as rgb(<channels>), so each
    // raw value is tried plain and rgb()-wrapped. A sentinel colour tells a
    // rejected assignment from an accepted one (element.style ignores invalid
    // values, leaving the sentinel in place).
    const CHANNELS = /var\(--[\w-]+\)|^[-\d.]+%?\s+[-\d.]+%?\s+[-\d.]+%?\s*(?:\/\s*[-\d.]+%?)?$/;
    const colourOf = (raw) => {
      // A var() or channel-triplet raw resolves a usable colour only inside
      // rgb(...); tried first so `color: var(--accent)` (which would compute
      // to the channels and fail as a colour) cannot win.
      for (const t of (CHANNELS.test(raw) ? [`rgb(${raw})`, raw] : [raw, `rgb(${raw})`])) {
        p.style.color = 'rgb(1, 2, 3)';
        p.style.color = t;
        if (p.style.color !== 'rgb(1, 2, 3)' && p.style.color !== '') return norm(getComputedStyle(p).color);
      }
      return null;
    };
    const out = {};
    for (const name of names) {
      const raw = noUrl(getComputedStyle(readEl).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      p.removeAttribute('style');
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
      else {
        const col = (CSS.supports('color', raw) || raw.includes('var(') || CHANNELS.test(raw)) ? colourOf(raw) : null;
        if (col && typeof col === 'string') { r.kind = 'color'; r.value = col; }
        else if (col && typeof col === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + col.unparsed; }
        else if (!raw.includes('%') && CSS.supports('width', raw)) {
          if (/(em|ex|ch|cap|ic|lh|rlh)$/.test(raw) && !/rem$/.test(raw)) {
            r.kind = 'other'; r.note = 'font-relative length; resolves per element';
          } else {
            p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width;
            if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900';
            if (r.value === '0px' && !/^[.\d]/.test(raw)) { r.value = raw; r.note = 'sizing keyword, not a fixed length'; }
          }
        }
        else if (CSS.supports('box-shadow', raw) || (CHANNELS.test(raw.trim().split(/\s+/).slice(-3).join(' ')) && CSS.supports('box-shadow', raw.replace(/(-?[\d.]+%?\s+[\d.]+%?\s+[\d.]+%?\s*(?:\/\s*[\d.]+%?)?)\s*$/, 'rgb($1)')))) {
          const wrapped = CSS.supports('box-shadow', raw) ? raw : raw.replace(/(-?[\d.]+%?\s+[\d.]+%?\s+[\d.]+%?\s*(?:\/\s*[\d.]+%?)?)\s*$/, 'rgb($1)');
          p.style.boxShadow = wrapped; r.kind = 'shadow'; r.value = getComputedStyle(p).boxShadow;
          if (wrapped !== raw) r.note = 'channel-triplet colour wrapped rgb() the way the site consumes it';
        }
        else if (CSS.supports('transition-duration', raw)) { p.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(p).transitionDuration; }
        else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
        else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
        else r.kind = 'other';
      }
      out[name] = r;
    }
    box.remove();
    return out;
  }, want);
}
await browser.close();

const THEME = /^--(color|neutral|white|black|bg|fg|foreground|background|primary|secondary|accent|muted|card|popover|input|ring|border|sidebar|chart|destructive|success|warning|alert|on-alert|info|danger|font|text|radius|spacing|tracking|leading|ease|default-|animate|container|breakpoint|drop-shadow|blur|aspect|cursor|content|skeleton|theme|btn|shadow|spread|gap|max-w|z|pink|purple|green|orange|red|yellow|gray|filled|contrast|body|active|spacer|form|main|dynamic|indicator|disabled|logo|loading|product|button|big|grid|transition|transform|ease|motion)-?/;
const SKIN = /@media \(prefers-color-scheme:\s*dark\)/;
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|vimeo|sanity|statsig|hubspot|--hub|ahrefs|googletagmanager|gtm/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (SKIN.test(r.selector || '') || r.context.some((c) => SKIN.test(c))) return 'darkscope';
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
  source: 'the stylesheet bodies read during live signed-out loads of gumroad.com / and /discover and ichigo.gumroad.com/l/ichigo-reader (the cross-origin assets.gumroad.com design-*.css Vite bundle plus inline <style> blocks, from network responses, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets under emulated colour-scheme light and again dark — the media the @media (prefers-color-scheme:dark) :root block answers — each name applied to a real typed property so the `R G B` channel triplets and var() chains resolve the way a component consumes them, at 1440 x 900. light/dark resolve the gumroad.com document; product-light/product-dark resolve the product-page document, whose inline :root pins a light palette over the shared bundle',

  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, darkscope: names('darkscope').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  darkscope: ok.filter((r) => r.bin === 'darkscope'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, darkscope ${out.counts.names.darkscope}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}, product-light ${Object.keys(resolved['product-light'] || {}).length}, product-dark ${Object.keys(resolved['product-dark'] || {}).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
