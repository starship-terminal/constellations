// Reads every custom property dock.us's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// dock.us is a Webflow marketing site plus the auth app on auth.dock.us (a
// Next.js/Chakra application). The marketing pages carry three token layers:
// Dock's own --ds-* design-system vars, the shared Webflow stylesheet's
// --_anchor---* variables and legacy named colours (--black, --royal-blue…),
// and the 2026 home redesign's --color-*/--space-*/--text-* layer; the auth
// app's inline emotion styles declare --chakra-*. External bodies are read
// from the network responses, inline <style> blocks through the CSSOM, then
// re-parsed in the page with a constructed CSSStyleSheet — the same parse the
// browser does. Every rule declaring a --* property is kept with its
// selector and enclosing @media/@layer context; @font-face rules are kept
// too.
//
// Each name is resolved in a probe document that carries the real sheets,
// once plain and once with class="chakra-ui-dark" + data-theme="dark" on
// <html> (the auth app's Chakra dark scope; the marketing site has no dark
// theme — its .dark classes paint individual components, they do not re-bind
// variables), computed the way the browser computes it: colours come back as
// sRGB hex, lengths as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared:
//             --ds-*, --color-*, --font-*, --text-*, --space-*, --radius-*,
//             --shadow-*, --ease-*, --duration-*, --control-*, --_anchor---*,
//             the legacy named colours ...
//   auth      the auth app's Chakra layer: --chakra-*
//   app       any other custom property the site's own sheets declare — here
//             the hundreds of per-component Webflow vars (--agent--*,
//             --menu-*, --hero-*, --editor-*, --product-*, --card-* …)
//   vendor    embedded widget vars (HubSpot, Turnstile, chat launchers)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties, --lightningcss-*
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, AUTH, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
// An edge-block page can greet a fresh client: retry on a fresh context until
// the real document (with its sheets) arrives, then harvest. Three routes are
// visited so every layer lands in the harvest: the marketing home ('/', which
// carries the 2026 home stylesheet), a shared-shell page ('/pricing'), and
// the auth app (auth.dock.us/login, whose Chakra vars live in inline <style>
// blocks) — each with its own context.
const bodies = new Map();
const inlines = [];
for (const route of ['/', '/pricing', AUTH + '/login']) {
  const url = route.startsWith('http') ? route : BASE + route;
  let got = false;
  for (let tries = 0; tries < 6 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(6000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inl = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + location.host + location.pathname.replace(/\//g, '') + '-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
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
// The probe must resolve at the capture viewport: vw/vh units (and the
// clamps built on them) read the page's own width — a default-context page
// resolves 100vw as 1280, not the recorded 1440 x 900.
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
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

// ---- resolution: probe document with the real sheets, light and dark ----
// Two passes: 'light' is the plain root (what the marketing site and the
// auth app paint); 'dark' applies the Chakra dark scope (data-theme="dark"
// class="chakra-ui-dark") — only the auth app's variables re-bind there, the
// marketing layers have no dark theme to resolve.
const shell = (attrs) => '<!doctype html><html ' + attrs + '><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  // The marketing token vars are scoped to container elements, not :root —
  // .dock-shared-shell, #dock-native-home, #dock-home-v2, .ds-page,
  // #dock-pricing-2026, .header and the auth app's :root. Custom properties
  // inherit, so the probe element is nested inside every scope at once.
  + '</head><body><div class="dock-shared-shell"><div id="dock-native-home"><div id="dock-home-v2" data-home-v2-id="dock-home-v2"><div class="ds-page dm-library de-shell"><div id="dock-p0-page"><div id="dock-mcp-page"><div id="dock-pricing-2026"><div class="header"><div id="probe-root"></div></div></div></div></div></div></div></div></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-|svg$|media-|controls$)/.test(n)).sort();
const resolved = {};
const PASSES = [['light', ''], ['dark', 'data-theme="dark" class="chakra-ui-dark"']];
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
    const probeEl = document.getElementById('probe-root');
    for (const name of names) {
      // Resolved on the nested probe element: the site's token layers are
      // scoped to container classes/ids (.dock-shared-shell, #dock-native-home,
      // .ds-page …), which an :root read would miss; the probe inherits them all.
      const raw = noUrl(getComputedStyle(probeEl).getPropertyValue(name).trim());
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
await probeCtx.close();
await browser.close();

// Design-token-looking names. The marketing site declares three layers:
// Dock's --ds-* system vars, the shared Webflow stylesheet's --_anchor---*
// variables and legacy named colours, and the 2026 home's --color-*/--space-*
// layer.
const THEME = /^--(_anchor|ds|color|font|text|space|spacing|radius|shadow|inset-shadow|ease|duration|leading|tracking|weight|control|header|icon|logo|border|breakpoint|container|grid|layout|max|page|opacity|z)-?/;
const LEGACY = /^--(black|black-2|black-3|white|white-smoke|royal-blue|dodger-blue|slate-grey|slate-grey-2|dark-slate-blue|dim-grey|lavender|calc-100vw-16px)$/;
const AUTHVAR = /^--chakra-/;
const VENDOR = /hubspot|hs-form|--hs-|turnstile|chilipiper|intercom|gtm-|onetrust|iubenda|osano|video-js|vjs-|stripe|sonner|--toast-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.every((n) => AUTHVAR.test(n))) return 'auth';
  if (r.context.some((c) => c === '@layer theme') || names.every((n) => THEME.test(n) || LEGACY.test(n))) return 'theme';
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
  source: 'the stylesheet bodies read during live loads of the marketing home and /pricing on dock.us plus the auth app on auth.dock.us/login (the linked cdn.prod.website-files.com Webflow bundles and the auth app\u2019s inline emotion <style> blocks, from network responses and the CSSOM, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets, plain (:root) and under data-theme="dark" class="chakra-ui-dark" (the Chakra dark scope) at 1440 x 900',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, auth: names('auth').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  auth: ok.filter((r) => r.bin === 'auth'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, auth ${out.counts.names.auth}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
