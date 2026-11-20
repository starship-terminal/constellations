// Reads every custom property glossgenius.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// GlossGenius ships three public surfaces signed out:
//   glossgenius.com    the Webflow marketing site — a bundled CDN sheet plus
//                      inline <style> blocks over the Webflow-variables
//                      layer: --_color---primary--* (gloss-black/gloss-white/
//                      gray-*), --_color---super--* (a 16-hue accent family),
//                      --_color---primary-opacity--*, --bg-* flat names,
//                      --_size---*px, --_typography---*, --_layout---*,
//                      --_components---*, --_responsive---*, --_opacity---*,
//                      --_theme-v2---* and the stock --_apps---* collections.
//                      Light only: no theme toggle and no prefers-color-
//                      scheme dark rule anywhere in the readable sheets.
//   app.glossgenius.com the Next.js SPA (CSS modules) — its own token layer
//                      on :root: --content-*, --surface-*, --gray-*/
//                      --gloss-gray-*, --brand-*, --space-*x, --size-*x,
//                      --radius-*, --font-*, --border-* and component vars
//                      (--button-*, --input-*, --checkbox-*…). /login is the
//                      lightest signed-out entry.
//   honeyhivesalon.glossgenius.com  a real published booking website — its
//                      own CSS-module token family (--button-*, --text-*,
//                      --space-*, --chip-*, --input-*, --gray-*, --bg-*).
//                      /services loads the booking surface's sheets.
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector, its host and enclosing
// @media/@layer context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries one host's real
// sheets: `light` is the marketing shell, `app` the app shell and `booking`
// the booking-website shell. Colours come back as sRGB hex, lengths as px at
// 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared — the
//             --_x---* Webflow variable collections and the flat palette
//             names, and the app's/booking's --content-*/--surface-*/
//             --space-*/--brand-*/*-color families
//   app       any other custom property the sites' own sheets declare
//   vendor    embedded widget/framework vars (swiper, recaptcha, cookie
//             banners, Webflow internals, react-select's css-* hashes)
//   external  third-party stylesheet bodies entirely (decagon.ai's chat
//             widget, reCAPTCHA, jsdelivr icon fonts) — harvested for
//             provenance, never resolved or emitted into a token set
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, LOGIN_URL, BOOK_SERVICES, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Load each host's entry route once, collecting stylesheet bodies from network
// responses and inline <style> blocks from the CSSOM. `sheets` is one list of
// [label, cssText] per host.
const HOSTS = [
  ['marketing', BASE + '/'],
  ['app', LOGIN_URL],
  ['booking', BOOK_SERVICES],
];
// A stylesheet is first-party when the host being visited owns its origin:
// the glossgenius.com hosts themselves, the Webflow CDN that serves the
// site's own compiled bundle, and Google Fonts' css2 the site requests for
// its font stack. Everything else (decagon.ai's chat widget, reCAPTCHA's
// gstatic frame sheet, jsdelivr's icon font) is an embedded widget or vendor
// frame — collected for provenance but never part of the host's token set,
// and never loaded into that host's resolution shell, where its variables
// would otherwise resolve as if they were the site's own.
const FIRST_PARTY = (hostname) => hostname === 'cdn.prod.website-files.com'
  || hostname === 'fonts.googleapis.com'
  || hostname === 'glossgenius.com'
  || hostname.endsWith('.glossgenius.com');
const sheets = [];      // [label, cssText, party]
const scopes = {};      // host -> { html, body, wrapper } class strings from the live DOM
let page = null;
for (const [host, url] of HOSTS) {
  let got = null;
  for (let tries = 0; tries < 4 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    const bodies = new Map();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(9000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      // The classes the live page scopes its variables under: the app's
      // glossDS layer declares on :root and a .light/.dark scope element;
      // a booking site declares on its own .tokens_glossDS__* layout
      // wrapper. The resolution shells replay them so class-scoped names
      // resolve instead of silently dropping.
      scopes[host] = await p.evaluate(() => {
        const cls = (el) => (el && typeof el.className === 'string' ? el.className : '');
        const tok = document.querySelector('[class*="tokens_"]');
        const scopeEl = document.querySelector('.light, .dark');
        return {
          html: cls(document.documentElement),
          body: cls(document.body),
          wrapper: [cls(tok), cls(scopeEl)].filter(Boolean).join(' '),
        };
      }).catch(() => ({ html: '', body: '', wrapper: '' }));
      got = [
        ...[...bodies.entries()].map(([u, css]) => {
          let host3 = '';
          try { host3 = new URL(u).hostname; } catch { /* keep third */ }
          return [u, css, FIRST_PARTY(host3) ? 'first' : 'third'];
        }),
        ...inline.map(([n, css]) => [n, css, 'first']),
      ];
      page = p;
    } else {
      console.log('challenge page on', host, '(try ' + (tries + 1) + ')');
      await context.close();
    }
  }
  if (!got) { console.log('blocked on', host, '; continuing without its sheets'); continue; }
  for (const [name, css, party] of got) sheets.push([`${host} ${name}`, css, party]);
}
if (!sheets.length) { console.log('no sheets harvested; css-vars.json not written'); await browser.close(); process.exit(2); }
if (page) await page.close();

// ---- harvest: every rule with --* declarations, tagged by host ----
// The probe resolves viewport-relative declarations (min(100vh, 100dvh)), so
// it must carry the same 1440 x 900 viewport the captures label them with.
const probe = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file, party) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file, party };
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
        walk(r.cssRules, [...ctx, head], file, party);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, party, selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file, party);
    }
  };
  for (const [name, text, party] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name, party);
  }
  return { rules, fonts, errors };
}, sheets);

// ---- resolution: one probe document per host carrying its own sheets ----
// Every surface is light-only: no dark media query and no theme attribute
// anywhere in the harvested sheets, so each shell resolves one light pass.
// The probe shells replay each host's real scope classes — the app's .light
// scope and a booking site's .tokens_glossDS__* layout wrapper — so names
// declared under those selectors resolve on the probe element instead of
// dropping. Custom properties inherit, so the inner probe reads every
// ancestor scope at once.
const hostsOf = (prefix) => sheets.filter(([n, , party]) => n.startsWith(prefix + ' ') && party === 'first').map(([, css]) => css);
const SHELLS = {
  light: { css: hostsOf('marketing'), scope: scopes.marketing || {} },
  app: { css: hostsOf('app'), scope: scopes.app || {} },
  booking: { css: hostsOf('booking'), scope: scopes.booking || {} },
};
const shell = ({ css }) => '<!doctype html><html><head>'
  + css.map((c) => '<style>' + c.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => r.party !== 'third' && !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-|wp--preset-)/.test(n)).sort();
const resolved = {};
for (const pass of Object.keys(SHELLS)) {
  if (!SHELLS[pass].css.length) continue;
  await probe.setContent(shell(SHELLS[pass]), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate(({ names, scope }) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    if (scope.html) document.documentElement.className = scope.html;
    if (scope.body) document.body.className = scope.body;
    const box = document.createElement('div');
    box.className = scope.wrapper || '';
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
      // The inner probe inherits every ancestor scope — :root, the replayed
      // html/body classes and the wrapped layout scope — before the
      // document-level fallbacks.
      let raw = noUrl(getComputedStyle(p).getPropertyValue(name).trim());
      if (!raw) raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
      if (!raw) raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
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
  }, { names: want, scope: SHELLS[pass].scope });
}
await browser.close();

const THEME = /^--(_apps|---|_?[a-z]+---|(bg|black|white|dark|light|off-white|aaa|basel|burgandy|primary|secondary|tertiary|transparent|neutral|gray|grey|gloss|brand|content|surface|border|text|space|size|radius|font|shadow|elevation|accent|error|success|warning|info|red|green|orange|yellow|pink|purple|blue|amber|cerulean|coral|fuchsia|gold|jade|mauve|midnight|opal|orchid|pine|sage|sienna|smoke|sunset|violet|card|popover|input|ring|chart|destructive|muted|icon|container|line|ink|overlay|link|nav|button|chip|tag|badge|toggle|toast|input|checkbox|avatar|banner|alert|dialog|drawer|calendar|booking|book|member|service|screen|target|control|segment|gap|padding|organic|letter|bottom|temp|deprecated|white)-?)/;
const VENDOR = /swiper|recaptcha|--wp--preset|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|video-js|vjs-|stripe|sonner|--toast-|--w-|--webflow|css-[\da-z]+|emotion|gg-dropdown/i;
const binOf = (r) => {
  if (r.party === 'third') return 'external';
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n) || n.startsWith('--toast-'))) return 'vendor';
  if (r.context.some((c) => c === '@layer theme') || names.every((n) => THEME.test(n) || VENDOR.test(n))) return 'theme';
  return 'app';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ${r.file.split(' ')[0]} ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during live signed-out loads of glossgenius.com / (the Webflow CDN bundle + marketing-assets + inline <style> blocks), app.glossgenius.com /login (the Next.js CSS chunks) and honeyhivesalon.glossgenius.com /services (a real published booking site\'s chunks), re-parsed with CSSStyleSheet; resolved in per-host probes carrying each host\'s first-party sheets at 1440 x 900 with the page\'s own scope classes replayed (.light, .tokens_glossDS__*) — every surface is light-only (no dark media query, no theme attribute). Third-party sheets (the decagon.ai chat widget, reCAPTCHA, icon fonts) are harvested under `external` for provenance only: never resolved, never part of a token set',
  sheets: sheets.map(([n, t, party]) => `${n} (${t.length} bytes)${party === 'third' ? ' [third-party]' : ''}`),
  scopes,
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length, external: names('external').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  external: ok.filter((r) => r.bin === 'external'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}, external ${out.counts.names.external}`);
console.log(`resolved: ${Object.entries(resolved).map(([k, v]) => k + ' ' + Object.keys(v).length).join(', ')}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
