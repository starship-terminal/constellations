// Reads every custom property helloivy.co's and app.helloivy.co's stylesheets
// declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// www.helloivy.co is a Framer build: its whole design-token layer is five
// hashed variables declared on <body> —
//   --token-3ea41072  ink         rgb(0,0,0)      -> dark rgb(237,236,218)
//   --token-8cbad9a1  ground      rgb(250,246,240)-> dark rgb(22,22,26)
//   --token-38cd3004  muted       rgb(0,0,0)      -> dark rgb(102,102,98)
//   --token-fb7fb35d  inverse bg  rgb(255,255,255)-> dark rgb(0,0,0)
//   --token-c6b5aded  inverse ink rgb(0,0,0)      -> dark rgb(250,246,240)
// re-pointed by @media (prefers-color-scheme: dark) in the SSR sheet. The
// footer's "Change theme" toggle swaps the same tokens via the Framer
// runtime (html[toggle-theme] + localStorage.currentToggleState); emulated
// prefers-color-scheme alone does not repaint the page (verified
// 2026-11-17), so dark resolution reads the media-rule values plus the
// painted dark surface's measured colours. The site's other paint (component
// fills, borders) is declared per-component in the SSR stylesheet, so most
// roles are measured on the live pages instead.
//
// app.helloivy.co is a Vue SPA: index-*.css declares semantic names aliased
// through hashed vars (--main-color: var(--2ee30e65)) whose values are not
// in any sheet — they arrive as an inline `style=` theme block on
// section.main_section (workspace theming, default palette on the public
// share). vars.mjs records that element's inline declarations under
// `appTheme` so the build can resolve each semantic name.
//
// Bins:
//   theme     the Framer --token-* design tokens and the app's semantic --*-color layer
//   skins     the prefers-color-scheme: dark re-point scope
//   app       any other custom property the surfaces' own sheets declare
//   vendor    widget internals (--vc-* v-calendar, --fc-* fullcalendar, --toast-*)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, SHARE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
const bodies = new Map();
let page = null, inline = [], appTheme = {};
for (let tries = 0; tries < 6 && !page; tries++) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  // The marketing surface (Framer SSR ships its CSS in two inline <style>
  // blocks; any external sheet lands in `bodies` as well).
  await p.goto(process.env.VARS_URL || BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(6000);
  // Second surface: the app SPA — its index CSS is same-origin, and the
  // public share page carries the workspace theme as an inline style block
  // on section.main_section.
  await p.goto(APP + '/login', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(6000);
  await p.goto(SHARE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(9000);
  if (await clearChallenge(p, { tries: 3, step: 1500 })) {
    page = p;
    [inline, appTheme] = await p.evaluate(() => {
      // a url() in a custom property can be a signed URL: record url(…),
      // only data: and #fragment references kept
      const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
      const sec = document.querySelector('section.main_section');
      const decls = {};
      if (sec) {
        for (const n of sec.style) if (n.startsWith('--')) decls[n] = noUrl(sec.style.getPropertyValue(n).trim());
        // the hashed names resolve through computed style too — read the
        // semantic aliases back out so each has a painted value.
        const cs = getComputedStyle(sec);
        for (const n of ['--primary', '--main-color', '--link-color', '--checkbox', '--app-color', '--canvas-color', '--selection', '--canvas', '--sidebar', '--hover', '--book', '--hover-book', '--comment', '--scrollBarColor', '--scrollBarThumbColor', '--scrollBarThumbHover', '--project', '--projectHover', '--image-shadow', '--text-selection', '--book-icon', '--main-font-family', '--sidebar-width', '--header-height', '--main-header-height']) {
          const v = noUrl(cs.getPropertyValue(n).trim());
          if (v) decls['@' + n] = v;
        }
      }
      return [
        [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean),
        decls,
      ];
    });
    break;
  }
  console.log('challenge page, fresh context (try ' + (tries + 1) + ')');
  await context.close();
}
if (!page) { console.log('blocked by the edge on every try; css-vars.json not written'); await browser.close(); process.exit(2); }
// The marketing site's inline <style> blocks live on www.helloivy.co pages —
// the app page's CSSOM is empty of them, so harvest those separately.
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
await page.waitForTimeout(6000);
const webInline = await page.evaluate(() =>
  [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['web-inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
await page.close();
const sheets = [...bodies.entries()].concat(inline, webInline);

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

// ---- resolution: probe document with the real sheets, light then dark ----
// The Framer tokens re-point under @media (prefers-color-scheme: dark), so
// the dark pass emulates the OS signal on the probe page (the media rule
// applies; the site's own JS toggle is what repaints the real page).
const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const shell = () => '<!doctype html><html><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-|radix-|cmdk-)/.test(n)).sort();
const resolved = {};
await probe.setContent(shell(), { waitUntil: 'load' });
for (const pass of ['light', 'dark']) {
  await probe.emulateMedia({ colorScheme: pass }).catch(() => {});
  await probe.waitForTimeout(400);
  resolved[pass] = await probe.evaluate((names) => {
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
  }, want);
}
await browser.close();

const THEME = /^--(token-[0-9a-f]{8}-|framer-(font|text|link|paragraph)|primary|main-|link-|checkbox|app-|canvas|selection|sidebar|hover|book|comment|scroll|project|image-shadow|text-selection|popover-)/;
const SKIN = /prefers-color-scheme|(^|[\s,>+~])\.(dark|light)\b|:is\(\.(dark|light)\b|html\.(dark|light)\b|\[toggle-theme/;
const VENDOR = /video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|vimeo|sanity|statsig|hubspot|--hub|ahrefs|googletagmanager|gtm|--fa-|font-awesome|--vc-|--fc-|tippy|--popper|--ck-|--rdp|--rrc|--swiper|--plyr/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (SKIN.test(r.selector || '') || r.context.some((c) => SKIN.test(c))) return 'skins';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.every((n) => THEME.test(n) || VENDOR.test(n))) return 'theme';
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
  source: 'the stylesheet bodies read during live signed-out loads of www.helloivy.co / (the Framer SSR inline <style> blocks plus external sheets) and app.helloivy.co /login + the public Media-kit share (the same-origin index-*.css), re-parsed with CSSStyleSheet; resolved in a probe carrying the real sheets at 1440 x 900, once under emulated prefers-color-scheme: light and once under : dark — the media rule the Framer tokens re-point under. The dark paint on the live pages comes from the footer "Change theme" toggle (html[toggle-theme], localStorage.currentToggleState), not the media query alone. The app\'s semantic --*-color names hold no value in any sheet — their defaults arrive as inline style on the share page\'s section.main_section (workspace theming), recorded under appTheme',
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
  appTheme,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, skins ${out.counts.names.skins}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}; appTheme ${Object.keys(appTheme).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
