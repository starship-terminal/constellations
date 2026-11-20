// Reads every custom property glorify.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Glorify ships two public surfaces signed out:
//   glorify.com        the Framer marketing site — hashed design tokens on
//                      :root (--token-<uuid>) plus the --framer-* text engine
//                      (per-component font/style props, binned vendor here).
//                      Light only: color-scheme normal, no theme toggle, no
//                      prefers-color-scheme dark rule in the readable sheets.
//   app.glorify.com    the product SPA — a full semantic vocabulary on :root:
//                      the --light-*/--dark-* ramps, --neutral-light-*/,
//                      --active-*/--hover-* state colours, --icon-*/--icon-*-dark,
//                      --disabled-*/--disabled-*-dark, --field-*, --error-*/
//                      --info-*/--green-*/--orange-*/--pink-* ramps, --cta-300,
//                      --glori-gradient and layout vars (--header, --hero,
//                      --inspector, --assets…). /welcome redirects to the dark
//                      /dashboard/login card; /designer/use-template/0
//                      anonymously creates a scratch /file/<id> and paints
//                      the editor shell — Tailwind utilities plus named
//                      layers (button-primary, field-container__input,
//                      dropdown-toolbar, panel--inspector).
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector, its host and enclosing
// @media/@layer context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries one host's real
// sheets: `light` is the marketing shell, `app` the app shell (the login
// route's own sheets plus the editor route's). Colours come back as sRGB
// hex, lengths as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared — the
//             marketing --token-* hashes and the app's own semantic family
//   app       any other custom property the sites' own sheets declare
//   vendor    embedded widget/framework vars (the --framer-* text engine,
//             recaptcha, chat launchers, swiper…)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, LOGIN_URL, DESIGNER_URL, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Load each host's entry route once, collecting stylesheet bodies from network
// responses and inline <style> blocks from the CSSOM. `sheets` is one list of
// [label, cssText] per host. The designer URL auto-redirects to the anonymous
// /file/<id> onboarding — the editor shell loads with it.
const HOSTS = [
  ['marketing', BASE + '/'],
  ['app', LOGIN_URL],
  ['editor', DESIGNER_URL],
];
const sheets = [];
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
    // The designer route needs longer: it creates the scratch file, redirects
    // to /file/<id> and mounts the editor shell before its sheets are all in.
    await p.waitForTimeout(host === 'editor' ? 20000 : 9000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      got = [...bodies.entries(), ...inline];
      page = p;
    } else {
      console.log('challenge page on', host, '(try ' + (tries + 1) + ')');
      await context.close();
    }
  }
  if (!got) { console.log('blocked on', host, '; continuing without its sheets'); continue; }
  for (const [name, css] of got) sheets.push([`${host} ${name}`, css]);
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

// ---- resolution: one probe document per host carrying its own sheets ----
// The marketing host is light-only: no dark media query and no theme
// attribute anywhere in its sheets, so `light` is one pass. The app sheets
// re-declare the same :root on every signed-out route (login and editor
// chunks overlap), so both hosts' bodies resolve in one `app` pass.
const hostsOf = (...prefixes) => sheets.filter(([n]) => prefixes.some((p) => n.startsWith(p + ' '))).map(([, css]) => css);
const SHELLS = {
  light: { css: hostsOf('marketing') },
  app: { css: hostsOf('app', 'editor') },
};
const shell = ({ css }) => '<!doctype html><html><head>'
  + css.map((c) => '<style>' + c.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-|wp--preset-)/.test(n)).sort();
const resolved = {};
for (const pass of Object.keys(SHELLS)) {
  if (!SHELLS[pass].css.length) continue;
  await probe.setContent(shell(SHELLS[pass]), { waitUntil: 'load' });
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
      let raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
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
  }, want);
}
await browser.close();

const VENDOR = /--framer-|swiper|recaptcha|g-recaptcha|--wp--preset|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|intercom|crisp|video-js|vjs-|stripe|sonner|--toast-|--w-|tapfiliate|--webflow|turnstile/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n) || n.startsWith('--toast-'))) return 'vendor';
  // The marketing token layer is the hashed --token-* family; everything
  // else the Framer sheet declares is bin 'app'. On the SPA side every
  // non-vendor name is the product's own semantic vocabulary.
  const host = (r.file || '').split(' ', 1)[0];
  if (host === 'marketing') return names.every((n) => /^--token-/.test(n) || VENDOR.test(n)) ? 'theme' : 'app';
  return 'theme';
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
  source: 'the stylesheet bodies read during live signed-out loads of glorify.com / (the Framer bundle + inline <style> blocks), app.glorify.com /welcome (redirected to /dashboard/login) and /designer/use-template/0 (redirected to the anonymous /file/<id> onboarding; the SPA\'s own sheets), re-parsed with CSSStyleSheet; resolved in per-host probes carrying each host\'s real sheets at 1440 x 900 — the marketing host is light-only (no dark media query, no theme attribute), the app host paints its dark chrome',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
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
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: ${Object.entries(resolved).map(([k, v]) => k + ' ' + Object.keys(v).length).join(', ')}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
