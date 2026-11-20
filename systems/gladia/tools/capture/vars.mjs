// Reads every custom property gladia.io's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// www.gladia.io's marketing site is a static server-rendered site whose CSS
// arrives as linked /assets/*.css bundles (a shared sheet plus per-page
// sheets such as library-*.css) and inline <style> blocks — the homepage
// declares its whole token layer in an inline :root block, and
// /css/homepage-deferred.css loads below the fold. The declared layer:
// --color-neutral-0..1000, --color-purple/blue/green/red/yellow/orange/pink
// ramps, --color-purple/--color-blue/etc. hue defaults, --color-white, the
// --alpha-white/black-* translucents, --space-* (4px steps 0-48 plus
// --space-page-x/--space-section-y/--space-card-gap/--hero-*/--cta-*),
// --radius-0..6/--radius-full, --shadow-none/sm/md/lg/xl, --font-sans
// ('Suisse Intl')/--font-mono ('Geist Mono'), --font-size-10..80,
// --font-weight-*, --line-height-*, --letter-spacing-*, --text-body-*,
// --duration-0..480, --ease-*, --label-*, --badge-*, the semantic
// --text-primary/-secondary/-tertiary/-disabled/-inverse/-link/-brand/
// -success/-warning/-error, --bg-primary/-secondary/-tertiary/-inverse/
// -elevated/-sunken/-glass/-glass-light/-brand, --border-* roles,
// --filter-icon-*, --max-w-*, --gradient-*, --nb-*/--nav-bar-*/--hero-offset-*
// and the benchmark --surf-*/--bar-* names. :root's semantic roles are dark:
// --bg-primary is black, --text-primary white. A .light-mode scope
// re-points the 21 semantic roles (painted on /library) and .section--white
// re-points 7 of them for white sections inside dark pages; an emulated
// prefers-color-scheme pass changes nothing on :root.
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets,
// once at prefers-color-scheme light and once dark, computed the way the
// browser computes it: colours come back as sRGB hex, lengths as px at
// 1440 x 900. A third probe resolves the same names under a .light-mode
// ancestor and a fourth under .section--white — the scopes the site ships
// for its light page and white sections.
//
// Bins:
//   theme     design-token-looking names wherever they are declared —
//             the --color-*/--alpha-*/--space-*/--radius-*/--shadow-*/
//             --font-*/--line-height-*/--letter-spacing-*/--text-*/
//             --bg-*/--border-*/--duration-*/--ease-*/--label-*/--badge-*/
//             --filter-*/--max-w-*/--gradient-*/--nb-*/--nav-*/--hero-*/
//             --cta-*/--surf-*/--bar-* names
//   app       any other custom property the site's own sheets declare
//             (component-scoped vars: --mega-*, --glass-*, --liquid, --x/--y)
//   vendor    embedded widget vars (analytics, consent, HubSpot)
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
// arrives, then harvest. The homepage is the probe target because its
// inline <style> block declares the full :root token layer — the sheets its
// own page loads plus the shared bundle cover the set.
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
// The probe page must carry the same 1440x900 viewport the site loaded at:
// viewport-relative values (--f-col-width is calc(min(100vw,1440px)/48))
// resolve against it, and a browser.newPage()'s default context would size
// them for another screen.
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

// ---- resolution: probe document with the real sheets, four scopes ----
// gladia.io's :root semantic roles are dark. An emulated prefers-color-scheme
// dark pass measures what the scheme changes on the root (expected: nothing —
// the site ships no scheme-keyed redeclaration). The lightMode pass resolves
// the same names inside a .light-mode ancestor — the scope /library carries —
// and sectionWhite inside .section--white, the white-section scope dark pages
// mount. Names not re-pointed in a scope resolve to their :root value.
const shell = (scope) => '<!doctype html><html><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body>' + (scope ? `<div class="${scope}"><div id="probe-root"></div></div>` : '<div id="probe-root"></div>') + '</body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const [pass, scope] of [['dark', ''], ['light', ''], ['lightMode', 'light-mode'], ['sectionWhite', 'section--white']]) {
  if (pass === 'dark' || pass === 'light') await probe.emulateMedia({ colorScheme: pass });
  await probe.setContent(shell(scope), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate(([names, scoped]) => {
    const readEl = scoped ? document.getElementById('probe-root') : document.documentElement;
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
      // `none` is a missing channel (Chromium serialises the achromatic hue of
      // figma.com's color-mix alphas as `oklch(0 0 none / 0.08)`): read as 0.
      else if ((m = c.match(/^oklab\(([-\d.e]+%?|none) ([-\d.e]+|none) ([-\d.e]+|none)(?: \/ ([\d.]+%?))?\)$/))) { rgb = fromOklab(num(m[1]) || 0, m[2] === 'none' ? 0 : +m[2], m[3] === 'none' ? 0 : +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
      else if ((m = c.match(/^oklch\(([-\d.e]+%?|none) ([-\d.e]+|none) ([-\d.e]+|none)(?: \/ ([\d.]+%?))?\)$/))) { const h = (m[3] === 'none' ? 0 : +m[3]) * Math.PI / 180, C = m[2] === 'none' ? 0 : +m[2]; rgb = fromOklab(num(m[1]) || 0, C * Math.cos(h), C * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
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
    for (const name of names) {
      const raw = noUrl(getComputedStyle(readEl).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      p.removeAttribute('style');
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
      else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
        p.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(p).color);
        if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
      } else if (!raw.includes('%') && CSS.supports('width', raw)) {
        if (/(em|ex|ch|cap|ic|lh|rlh)$/.test(raw)) {
          // A font-relative length resolves against the element's own font
          // size; the empty probe's width would report it at this probe's
          // size, not the text it actually spaces (.005em read 0.078125px).
          r.kind = 'other'; r.note = 'font-relative length; resolves per element';
        } else {
          p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width;
          if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900';
          // max-content/min-content/fit-content/auto resolve to 0px on an empty
          // probe: keep the keyword instead of publishing a bogus length.
          if (r.value === '0px' && !/^[.\d]/.test(raw)) { r.value = raw; r.note = 'sizing keyword, not a fixed length'; }
        }
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
  }, [want, !!scope]);
}
await browser.close();

const THEME = /^--(color|alpha|space|radius|shadow|font|line-height|letter-spacing|text|bg|border|duration|ease|label|badge|filter|max-w|gradient|nb|nav|hero|cta|surf|bar|plans|duo|dark|liquid|gladia-draw|mq|anim-order|enter)-?/;
const SKIN = /\.(light-mode|section--white)\b/; // the light-page and white-section re-point scopes
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|--intercom-|vimeo|sanity|statsig|hubspot|--hub|ahrefs|googletagmanager|gtm/i;
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
  source: 'the stylesheet bodies read during a live signed-out load of www.gladia.io / (the linked /assets/*.css and /css/*.css bundles from network responses plus the inline <style> blocks, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets on :root under an emulated light colour scheme and again under emulated dark (the site ships no scheme-keyed redeclaration, so the passes agree), then inside a .light-mode ancestor (the scope /library paints) and inside .section--white (the white-section scope dark pages mount), at 1440 x 900',
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
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}, lightMode ${Object.keys(resolved.lightMode).length}, sectionWhite ${Object.keys(resolved.sectionWhite).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
