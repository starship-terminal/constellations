// Reads every custom property joinhandshake.com's and app.joinhandshake.com's
// stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Two signed-out surfaces ship two token layers:
//
//   joinhandshake.com (the marketing site, a Next.js app) — route-scoped
//   /_next/static/css/*.css chunks: a thin declared layer over Tailwind v4
//   utilities. The declared names are the font faces (--font-noi-grotesk,
//   --font-sans-plomb(-swap)), the --spacing unit, --container-3xs..7xl,
//   --leading-xs..xl, --tracking-sm/-lg, --font-weight-light..bold, the
//   --ease-*/--default-transition-*/--animate-*/--blur-*/--drop-shadow-*
//   motion and filter scales, --breakpoint-lg, --aspect-video, and the
//   product's own nav/hero geometry vars (--desktop-nav-height,
//   --mobile-nav-height, --notification-banner-height, --full-*-nav-height,
//   --banner-height, --csa-*, --hero-*, --grid-*, --container-padding,
//   --content-max-width, --condensed-nav-width). Colour is authored mostly
//   as literal hexes inside utilities (#14151c ink, #d3fb52 lime, ...) plus
//   a few component vars (--lime-30/-50, --cta(-hover|-active|-visited),
//   --link-hover-color, --nav-background-color, --bg(-color), --text).
//   Light only: no theme class, no theme control, no prefers-color-scheme.
//
//   app.joinhandshake.com (the consumer app) — the "Log in or sign up" page
//   at /access (reached through /login) ships the Rosetta design system from
//   handshake-production-cdn.joinhandshake.com: --rosetta-bg-*/--rosetta-fg-*/
//   --rosetta-interactive-*/--rosetta-shadow-*/--rosetta-size-*/
//   --rosetta-spacing-*/--rosetta-type-*/--rosetta-font-family-*/--rosetta-
//   avatar-* plus component vars (--button-*, --nav-*, --popover-*,
//   --modal-*, --listbox-*, --select-*, --tag-*, --slider-*, --tooltip-*,
//   --day-picker-*, --feature-callout-*, --segmented-toggle-*,
//   --skeleton-loader-*, --date-picker-*) and the deprecated
//   --rosetta-colors-* legacy names. Light only. The host sits behind a
//   Cloudflare managed challenge that clears intermittently: the harvest
//   retries fresh contexts; a run where it never clears leaves the earlier
//   css-vars.json alone.
//
// External bodies are read from the network responses, inline <style> blocks
// through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets —
// marketing names under the marketing page's own html/body classes, rosetta
// names under the app's — computed the way the browser computes it: a colour
// comes back as sRGB, a length as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared
//   app       any other custom property the sites' own sheets declare
//   vendor    embedded widget sheets (Ketch consent, Marketo forms2, Google GSI)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP_URL, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
const bodies = new Map();
const inline = [];
let bodyClass = '', htmlClass = '', appBodyClass = '', appHtmlClass = '';

// Sheets seen while a page loads are kept by URL; several marketing pages are
// visited because each route loads its own /_next/static/css chunk.
const MARKETING_PAGES = ['/', '/employers/', '/employers/pricing/', '/employers/request-more-info/', '/career-centers/', '/careers/', '/about/', '/ai/', '/blog/', '/learn/', '/legal/tos/', '/newsroom/', '/students/', '/research/ai/', '/security/', '/privacy-policy/'];
{
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  for (const u of MARKETING_PAGES) {
    await p.goto(BASE + u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(2200);
    if (!bodyClass) {
      [bodyClass, htmlClass] = await p.evaluate(() => [document.body.className, document.documentElement.className]).catch(() => ['', '']);
      const inl = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean)).catch(() => []);
      inline.push(...inl);
    }
  }
  await context.close();
}

// The app surface: /access behind the intermittent Cloudflare challenge —
// fresh contexts until the real page arrives (or the run is a boundary).
let appOk = false;
for (let tries = 0; tries < 8 && !appOk; tries++) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set('app:' + r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  await p.goto(APP_URL, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(6000);
  if (await clearChallenge(p, { tries: 3, step: 1500 })) {
    appOk = true;
    const inl = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['app-inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean)).catch(() => []);
    inline.push(...inl);
    [appBodyClass, appHtmlClass] = await p.evaluate(() => [document.body.className, document.documentElement.className]).catch(() => ['', '']);
  } else {
    console.log('app challenge page, fresh context (try ' + (tries + 1) + ')');
  }
  await context.close();
}
if (!appOk) console.log('! app.joinhandshake.com never cleared the challenge; marketing vars only');
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
          : r.type === CSSRule.SUPPORTS_RULE ? r.conditionText
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

// ---- resolution: probe documents carrying the real sheets ----
// Marketing names are read inside the marketing sheets under the marketing
// page's own classes; --rosetta-* names inside the app sheets under the app
// page's own classes (the consumer app also scopes some names to its root
// classes). Each name is applied to a real typed property: colour -> sRGB,
// length -> px at 1440 x 900, shadow/duration/easing/font through their own
// properties.
const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const mkShell = (names, cls, bodyCls) => '<!doctype html><html class="' + escAttr(cls) + '"><head>'
  + sheets.filter(([n]) => names(n)).map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="' + escAttr(bodyCls) + '"><div id="probe-root"></div></body></html>';
const isAppSheet = (n) => n.startsWith('app:') || n.startsWith('app-inline');
const isMkSheet = (n) => !isAppSheet(n);
const wantOf = (sheetTest) => [...new Set(result.rules.filter((r) => sheetTest(r.file) && !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-|radix-|cmdk-|ketch)/.test(n)).sort();

const resolvePass = async (names, sheetTest, cls, bodyCls) => {
  if (!names.length) return {};
  await probe.setContent(mkShell(sheetTest, cls, bodyCls), { waitUntil: 'load' });
  return probe.evaluate((names) => {
    const readEl = document.getElementById('probe-root');
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
    const CHANNELS = /var\(--[\w-]+\)|^[-\d.]+%?\s+[-\d.]+%\s+[-\d.]+%\s*(?:\/\s*[-\d.]+%?)?$/;
    const colourOf = (raw) => {
      for (const t of (CHANNELS.test(raw) ? [`hsl(${raw})`, raw] : [raw, `hsl(${raw})`])) {
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
          if (/(em|ex|ch|cap|ic|lh|rlh)$/.test(raw)) {
            r.kind = 'other'; r.note = 'font-relative length; resolves per element';
          } else {
            p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width;
            if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900';
            if (r.value === '0px' && !/^[.\d]/.test(raw)) { r.value = raw; r.note = 'sizing keyword, not a fixed length'; }
          }
        }
        else if (CSS.supports('box-shadow', raw)) { p.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(p).boxShadow; }
        else if (CSS.supports('transition-duration', raw)) { p.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(p).transitionDuration; }
        else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
        else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
        else r.kind = 'other';
      }
      out[name] = r;
    }
    box.remove();
    return out;
  }, names);
};

const mkNames = wantOf(isMkSheet);
const appNames = wantOf(isAppSheet);
const resolved = {};
resolved.site = await resolvePass(mkNames, isMkSheet, htmlClass, bodyClass);
if (appOk) resolved.app = await resolvePass(appNames, isAppSheet, appHtmlClass, appBodyClass);
await browser.close();

const THEME = /^--(font|spacing|container|breakpoint|leading|tracking|ease|default-|animate|blur|drop-shadow|aspect|lime|cta|link|nav|notification|banner|csa|hero|grid|content|condensed|btn|bg|text|full-|mobile-|desktop-|tablet-|distance|delay|input|padding|pinned|custom|angle|next|previous|small|medium|large|disabled|selected|selecting|in-range|outside|today|clearable|no-label|hover-reveal|keyboard-selected|left|flex|icon-font)-?/;
const ROSETTA = /^--(rosetta|button|checkbox|avatar|badge|breadcrumbs|date-picker|day-picker|feature-callout|listbox|loading-spinner|menu|modal|nav|popover|select|segmented-toggle|side-sheet|skeleton|slider|submenu|tag|tip-popover|tooltip)/;
const VENDOR = /ketch|mkto|marketo|forms2|lanyard|gstatic|gsi|google|video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|vimeo|sanity|statsig|hubspot|--hub|googletagmanager|gtm/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  const appSheet = isAppSheet(r.file);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.file || '') || VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (appSheet) return ROSETTA.test(names.join(' ')) || names.some((n) => ROSETTA.test(n)) ? 'app-theme' : 'app';
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
  source: 'the stylesheet bodies read during live signed-out loads: ' + MARKETING_PAGES.length + ' joinhandshake.com routes (the linked /_next/static/css/*.css chunks from network responses plus inline <style> blocks, re-parsed with CSSStyleSheet)' + (appOk ? ' and app.joinhandshake.com/access once its Cloudflare challenge cleared (the handshake-production-cdn dist/consumer sheets plus its inline blocks)' : '; app.joinhandshake.com never cleared its challenge this run') + '. Each name resolved in a probe carrying the real sheets and the live pages\' own html/body classes — the marketing names in the marketing shell, the rosetta names in the app shell — applied to a real typed property at 1440 x 900',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, 'app-theme': names('app-theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  'app-theme': ok.filter((r) => r.bin === 'app-theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
// A run where the app's challenge never clears must not erase the app
// readings a previous run captured: carry the earlier file's app bins,
// resolved names and sheet list forward.
if (!appOk) {
  try {
    const prev = JSON.parse(fs.readFileSync(path.join(REF, 'raw', 'css-vars.json'), 'utf8'));
    if (prev.resolved && prev.resolved.app && Object.keys(prev.resolved.app).length) {
      out.resolved.app = prev.resolved.app;
      out.app = prev.app;
      out['app-theme'] = prev['app-theme'];
      out.sheets = [...out.sheets, ...(prev.sheets || []).filter((s) => s.startsWith('app:') || s.startsWith('app-inline'))];
      out.counts.names.app = [...new Set((out.app || []).flatMap((r) => Object.keys(r.properties)))].sort().length;
      out.counts.names['app-theme'] = [...new Set((out['app-theme'] || []).flatMap((r) => Object.keys(r.properties)))].sort().length;
      console.log(`  kept previous run's app readings: ${Object.keys(prev.resolved.app).length} resolved names, ${(prev.app || []).length + (prev['app-theme'] || []).length} rules`);
    }
  } catch { /* no previous file — nothing to carry */ }
}
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app-theme ${out.counts.names['app-theme']}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: site ${Object.keys(resolved.site || {}).length}, app ${Object.keys(resolved.app || {}).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
