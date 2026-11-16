// Reads every custom property fourthwall.com's stylesheets declare and
// writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Fourthwall ships five public surfaces on three style systems:
//   fourthwall.com          the Webflow marketing site — Webflow variable
//                           layers on :root: --_primitives---* (ink/paper,
//                           Suisse Intl/Saans type, space/radius scales),
//                           --_surface---* semantics that invert under the
//                           "on-ink" scope classes (.on-ink, .site-footer,
//                           .nav-menu, .closer-section, .leg-section.*, …),
//                           plus flat ramps --gs*/--b*/--g*/--r*/--y*/--twitch*
//   products.fourthwall.com the public product catalogue — the Fourthwall
//                           design system proper: --color-* ramps and
//                           --bg-*/--border-*/--text-*/--icon-*/--font-*/
//                           --space-*/--radius-*/--shadow-*/--motion-*/
//                           --input-*/--button-*/--panel-* semantics wrapped
//                           in light-dark() — the dark branch is declared only
//                           (no theme toggle, never painted signed out)
//   /get-started            redirects to auth.fourthwall.com (Keycloak) —
//                           the same catalogue DS behind the signed-out
//                           Google/Apple/email choices
//   docs.fourthwall.com     Mintlify docs — --gray-* ramp, --primary*,
//                           --background-*, a "Change theme preference"
//                           control that sets html.dark
//   help.fourthwall.com     Docusaurus — --ifm-* plus --fw-* Fourthwall
//                           overrides and --eli-*/--ask-ai-* assistant vars;
//                           a real data-theme="dark" toggle
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector, its host and enclosing
// @media/@layer context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries one host's real
// sheets: `light` the marketing :root, `ink` the marketing shell with the
// on-ink scope class applied to body (the dark-section remap the real pages
// paint), `catalog` the products shell, `catalogDark` the products shell
// resolved under an emulated prefers-color-scheme: dark (the declared
// light-dark() dark branch — a forced probe, not an observed theme), `signup` the get-started/auth
// sheets, `docs` the Mintlify shell, `docsDark` it with html.dark (the site's
// own theme menu), `help` the Docusaurus shell and `helpDark` it under
// data-theme="dark" (the site's own toggle). Colours come back as sRGB hex,
// lengths as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared —
//             the palette names, --border* and the rest ...
//   app       any other custom property the sites' own sheets declare
//   skins     scoped theme-variant redeclarations (the marketing on-ink/dark
//             section scopes, data-theme="dark", html.dark)
//   vendor    embedded widget/framework vars (the Osano --cc-* cookie
//             consent, toastify/twoslash/intercom internals)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, PRODUCTS, DOCS, HELP, SIGNUP_URL, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Load each host's entry route once, collecting stylesheet bodies from network
// responses and inline <style> blocks from the CSSOM. `sheets` is one list of
// [label, cssText] per host.
const HOSTS = [
  ['marketing', BASE + '/'],
  ['marketing', BASE + '/blog'],   // the blog index loads extra sheet vars the home page does not
  ['catalog', PRODUCTS + '/'],
  ['signup', SIGNUP_URL],          // follows the auth.fourthwall.com redirect; no form is touched
  ['docs', DOCS + '/'],
  ['help', HELP + '/'],
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
    await p.waitForTimeout(6000);
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
// `dark` resolves the help host's body.dark-mode remap (the toggle the docs
// site really ships); `appDark` the app's declared-but-gated remap. The
// remapped vars are declared on `body.dark-mode`, so they are read off body.
const hostsOf = (prefix) => sheets.filter(([n]) => n.startsWith(prefix + ' ')).map(([, css]) => css);
// `ink` carries the marketing on-ink scope classes the real pages put on dark
// sections (.on-ink is the umbrella the sheet defines); `catalogDark` is the
// same products sheets resolved under an emulated dark color-scheme (the
// declared light-dark() branch, not an observed paint); `docsDark` adds
// html.dark, `helpDark` data-theme="dark" — both are the hosts' own toggle
// classes.
const SHELLS = {
  light: { css: hostsOf('marketing'), html: '', body: '' },
  ink: { css: hostsOf('marketing'), html: '', body: 'on-ink site-footer' },
  catalog: { css: hostsOf('catalog'), html: '', body: '', scheme: 'light' },
  // The catalogue declares its dark side inside light-dark(): the media
  // emulation alone does not flip it (light-dark resolves against the
  // element's used color-scheme), so the probe pins color-scheme: dark —
  // the same value the live page computes when the preference is dark.
  catalogDark: { css: hostsOf('catalog'), html: '', body: '', scheme: 'dark', htmlStyle: 'color-scheme: dark' },
  // The auth sheets declare the same light-dark() pairs and paint light for a
  // light-preference visitor; pin light so the probe does not inherit the
  // catalogue dark emulation (emulateMedia persists across setContent).
  signup: { css: hostsOf('signup'), html: '', body: '', scheme: 'light' },
  docs: { css: hostsOf('docs'), html: '', body: '' },
  docsDark: { css: hostsOf('docs'), html: 'dark', body: '' },
  help: { css: hostsOf('help'), html: 'light', body: '', theme: 'light' },
  helpDark: { css: hostsOf('help'), html: 'dark', body: '', theme: 'dark' },
};
const shell = ({ css, html, body, theme, htmlStyle }) => `<!doctype html><html class="${html}"${theme ? ` data-theme="${theme}"` : ''}${htmlStyle ? ` style="${htmlStyle}"` : ''}><head>`
  + css.map((c) => '<style>' + c.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + `</head><body class="${body}"><div id="probe-root"></div></body></html>`;
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-|wp--preset-)/.test(n)).sort();
const resolved = {};
for (const pass of Object.keys(SHELLS)) {
  if (!SHELLS[pass].css.length) continue;
  if (SHELLS[pass].scheme) await probe.emulateMedia({ colorScheme: SHELLS[pass].scheme });
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
      // The theme remap lives on body (.light-mode/.dark-mode); :root keeps the
      // shared palette. Read body first, then documentElement as the fallback.
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

const THEME = /^--(_primitives---|_rhythm---|_surface---|gs\d|b\d\d\d|g\d\d\d|r\d\d\d|y\d\d\d|twitch|font-|bottom-radius|bg-|border-|color-|icon-|image-|input-|motion-|panel-|radius-|shadow-|space-|text-|blur-|button-|popover-|gray-|primary|background-|spacing-|code-|topbar-|assistant-|ifm-|fw-|doc-|docusaurus-|eli-|ask-ai-|scroll-mt|fade-width|banner-height|navbar-|sidebar-|search-local-|container-|grid-|leading-|tracking-|weight-|ease-|breakpoint-|min-|max-|viewport-|line-|ink|surface-|divider-|elevation-|width-|height-|aspect-|white|black|grey|blue|orange|red|green|fs\d|animate)-?/;
// Scoped theme-variant redeclarations: the marketing "on-ink" dark sections
// (the sheet's own scope classes), the Mintlify html.dark remap and the
// Docusaurus data-theme remap. They keep their real selectors as evidence.
const SKIN = /\.on-ink|\.site-footer\b|\.nav-menu\b|\.mega-clip\b|\.closer-section|\.wordmark-section|\.leg-section|\.tile--dark|data-theme|html\.dark|\.dark\b|dark-mode|\.dark-mode|is-warm/;
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|toastify|twoslash|cookiebot|cybot|--cb-|--cc-|osano|cookieconsent|gdpr|--hs-|--intercom|--wp--preset|--wpg-|--snippet-|--otat-|--ghost--|--ultraghost|--code-editable|lightningcss/i;
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
  const key = `[${r.bin}] ${r.file.split(' ')[0]} ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during live signed-out loads of fourthwall.com / and /blog (the Webflow mkt.css + inline styles), products.fourthwall.com / (the catalogue\'s styled-components DS sheet), fourthwall.com /get-started (the auth.fourthwall.com Keycloak sheets it redirects to — no form touched), docs.fourthwall.com / (Mintlify) and help.fourthwall.com / (Docusaurus), re-parsed with CSSStyleSheet; resolved in per-host probes carrying each host\'s real sheets — light (marketing :root), ink (marketing body.on-ink, the dark-section scope), catalog (products, light), catalogDark (products under emulated prefers-color-scheme: dark), signup (the auth shell), docs (Mintlify light), docsDark (Mintlify html.dark — its own theme menu), help (Docusaurus data-theme=light) and helpDark (data-theme=dark — its own toggle), at 1440 x 900',
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
console.log(`resolved: ${Object.entries(resolved).map(([k, v]) => k + ' ' + Object.keys(v).length).join(', ')}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
