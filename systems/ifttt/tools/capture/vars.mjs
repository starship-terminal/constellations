// Reads every custom property IFTTT's stylesheets declare and writes
// raw/css-vars.json — plus a `palette` section that harvests every literal
// colour the rules declare, because almost all of IFTTT's styling is
// literal hex/rgb() on Sass-compiled classes rather than variables.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// ifttt.com is a server-rendered Rails site; ifttt.ai is the marketing
// home. Both serve Vite-built sheets from web-assets.ifttt.com/builds/
// assets/*.css — each section pulls its own bundle (customer-*.css on the
// home and detail pages, explore-*.css on /explore, customer_marketing-*.css
// on /plans and the solutions pages), so the harvest visits a
// representative set: ifttt.ai/, /explore, /plans, a service page, an
// applet page, a connect page, /mcp, /about, /terms. The token layer is
// nearly absent — a handful of custom properties (--card-color,
// --hero-unit, --primary-text, the explore hero's --cycle-*) — so
// `palette` records each declared literal with the selectors that use it,
// and the token tree leans on that plus measured computed styles.
// @font-face rules are kept too: Museo Sans Rounded (300/500/700/900 +
// italics) is proprietary and never shipped in the package.
//
// IFTTT paints one theme — no theme control exists on any signed-out
// surface, so each name is resolved once under a default pass (the
// dark-painted sections read their own literals, not a switched :root).
// Bins:
//   app       any custom property the site's own sheets declare
//   vendor    embedded widget vars (reCAPTCHA, Intercom, OneTrust…)
//   other     anything left

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, HOME, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

// The representative surface set: each section loads its own sheet bundle,
// and the detail pages (service / applet / connect) share customer-*.css.
const HARVEST = [
  HOME + '/',
  BASE + '/explore',
  BASE + '/plans',
  BASE + '/twitter',
  BASE + '/applets/A38TqjpD-start-irobot-cleaning-when-you-leave-home',
  BASE + '/connect/discord/instagram',
  BASE + '/mcp',
  BASE + '/about',
  BASE + '/terms',
];

const { browser } = await launch();
const bodies = new Map();
let page = null, inline = [], bodyClass = '', htmlClass = '';
for (let tries = 0; tries < 6 && !page; tries++) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  for (const u of HARVEST) {
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(4500);
  }
  if (await clearChallenge(p, { tries: 3, step: 1500 })) {
    page = p;
    [inline, bodyClass, htmlClass] = await p.evaluate(() => [
      [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean),
      document.body.className,
      document.documentElement.className.trim(),
    ]);
    break;
  }
  console.log('challenge page, fresh context (try ' + (tries + 1) + ')');
  await context.close();
}
if (!page) { console.log('blocked by the edge on every try; css-vars.json not written'); await browser.close(); process.exit(2); }
const sheets = [...bodies.entries()].concat(inline);
await page.close();

// ---- harvest: every rule with --* declarations, every literal colour ----
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
await patch(probeCtx);
const probe = await probeCtx.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const colourRe = /#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)|lab\([^)]*\)|oklch?\([^)]*\)|light-dark\([^)]*\)|color-mix\([^)]*\)/g;
  const colours = {};   // literal -> {count, uses: [{selector, context, property}]}
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
      const colourProps = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
        else if (/^(color|background-color|border(-top|-right|-bottom|-left)?-color|outline-color|fill|stroke|box-shadow|caret-color|text-decoration-color|text-shadow)$/.test(k)) {
          const v = noUrl(r.style.getPropertyValue(k).trim());
          if (colourRe.test(v)) colourProps[k] = v;
        }
        colourRe.lastIndex = 0;
      }
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
      for (const [k, v] of Object.entries(colourProps)) {
        for (const m of v.matchAll(colourRe)) {
          const lit = m[0].toLowerCase().replace(/\s+/g, ' ');
          (colours[lit] ??= { count: 0, uses: [] }).count++;
          const uses = colours[lit].uses;
          if (uses.length < 8) uses.push({ selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(-1)[0] || '', property: k });
        }
      }
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors, colours };
}, sheets);

// ---- resolution: probe document with the real sheets, one default pass ----
// Each --* name is applied to a real typed property on a probe element, so
// channel triplets and var() chains come back the way a component consumes
// them. IFTTT declares almost no token names — the pass still records what
// the few --* names resolve to. One pass: the product paints a single theme.
const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const shell = () => '<!doctype html><html class="' + escAttr(htmlClass) + '"><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="' + escAttr(bodyClass) + '"><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(_|lightningcss-|radix-|cmdk-|tw-)/.test(n)).sort();
const resolved = {};
await probe.setContent(shell(), { waitUntil: 'load' });
resolved.light = await probe.evaluate((names) => {
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
await browser.close();

const VENDOR = /recaptcha|g-recaptcha|intercom|onetrust|cookiebot|cybot|--cb-|osano|gdpr|--hs-|hubspot|--hub|googletagmanager|gtm|--fa-|font-awesome|--_fa|video-js|vjs-|stripe|sonner|algolia|docsearch/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
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
  source: "the stylesheet bodies read during live signed-out loads of ifttt.ai/, ifttt.com/explore, /plans, /twitter, an applet page, /connect/discord/instagram, /mcp, /about and /terms (the linked web-assets.ifttt.com/builds/assets/*.css bundles from network responses plus any inline <style> blocks, re-parsed with CSSStyleSheet); each custom property resolved once in a probe carrying the real sheets — IFTTT paints one theme, so there is a single `light` pass — and `palette` is the harvest of every literal colour the rules declare with the selectors and properties that use it, because almost all of the site's styling is literal hex/rgb() on Sass-compiled classes",
  pages: HARVEST,
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    palette: Object.keys(result.colours).length,
    names: { app: names('app').length, vendor: names('vendor').length },
    bySelector,
  },
  errors: result.errors,
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  fonts: result.fonts,
  palette: result.colours,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces, ${Object.keys(result.colours).length} palette literals; names app ${out.counts.names.app}, vendor ${out.counts.names.vendor}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
