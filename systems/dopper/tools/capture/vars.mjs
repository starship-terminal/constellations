// Reads every custom property dopper.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// www.dopper.com is a Next.js/Storyblok site: its styles arrive as linked
// same-origin CSS bundles under /_next/static/css/ plus inline <style>
// blocks. The bundles declare a real token layer on :root — the brand
// palette (--darkBlue/-1..-3, --deep-sea/-1..-3/-overlay, --sand/-1..-3,
// --yellow/-1..-3, --darkTeal, --carribean/-1..-3, --glowing-coral/-1..-3,
// --white #fcfaf2, --black), eight easing curves (--ease-*, --bounce-*),
// z-index layers and radii (--border-radius-*, --touch-target-min) — plus
// component-scoped custom properties on module selectors. External bodies
// are read from the network responses, inline <style> blocks through the
// CSSOM, then re-parsed in the page with a constructed CSSStyleSheet — the
// same parse the browser does. Every rule declaring a --* property is kept
// with its selector and enclosing @media/@layer context, and @font-face
// rules are kept too.
//
// Each name is resolved in a probe document that carries the real sheets.
// The site ships one theme: nothing binds a dark class, attribute or
// prefers-color-scheme anywhere in the bundles, so there is a single light
// pass, computed the way the browser computes it: colours come back as sRGB
// hex, lengths as px at 1440 x 900.
//
// The Magento storefront (shop.dopper.com) holds no token layer: its theme
// compiles the same palette to literal values. A lighter pass records its
// stylesheet and @font-face list into out.shop for provenance; shop values
// are measured on the elements instead.
//
// Bins:
//   theme     names declared on a bare :root/html selector — dopper.com's
//             real token layer (palette, easings, z layers, radii)
//   app       custom properties declared on component selectors
//             (per-module layout/scoped vars)
//   vendor    embedded widget vars (Cookiebot, chat, third-party)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties, --lightningcss-*
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, SHOP, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Opens a URL in a fresh context, harvesting stylesheet bodies off the
// network responses and inline <style> blocks through the CSSOM. An
// edge-block page can greet a fresh client: retry on a fresh context until
// the real document (with its sheets) arrives.
async function harvest(url, tries = 6) {
  const bodies = new Map();
  for (let i = 0; i < tries; i++) {
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
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      await context.close();
      return [...bodies.entries()].concat(inline);
    }
    console.log('challenge page, fresh context (try ' + (i + 1) + ')');
    await context.close();
  }
  return null;
}

const sheets = await harvest(BASE + '/');
if (!sheets) { console.log('blocked by the edge on every try; css-vars.json not written'); await browser.close(); process.exit(2); }

// ---- harvest: every rule with --* declarations ----
// The probe resolves vw/vh/dvh and @media at the 1440 x 900 the notes below claim; a bare
// browser.newPage() would give Playwright's 1280 x 720 default (finding 19-1).
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

// ---- bins, declared before resolution so the probe only pays for the
// site's own names (the HubSpot widget declares ~4,500 vars of its own) ----
const THEME = /^--(darkBlue|deep-sea|sand|yellow|darkTeal|carribean|glowing-coral|white|black|ease-|bounce-|z-|border-radius-|touch-target)/;
const ROOTSEL = /^:root$|^html$|^:root,\s*html$|^html,\s*:root$/;
const VENDOR = /cybot|cookiebot|gorgias|widget|video-js|vjs-|stripe|sonner|--toast-|\.s-mode|\.s-theme|data-org-theme|osano-cm|--s-|hubspot|hsappstatic/i;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  // The HubSpot chat widget ships a whole theme stylesheet of its own (its
  // vars also land on :root), so bin by file and selector as well as name.
  if (VENDOR.test(r.file || '') || VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  // dopper.com's token layer sits on a bare :root selector; everything on a
  // component selector is a scoped module variable.
  if (ROOTSEL.test((r.selector || '').trim()) && names.some((n) => THEME.test(n))) return 'theme';
  if (names.every((n) => THEME.test(n))) return 'theme';
  return 'app';
};

// ---- resolution: probe document with the real sheets (the site is light-only) ----
const shell = '<!doctype html><html><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
for (const r of result.rules) r.bin = binOf(r);
const want = [...new Set(result.rules.filter((r) => r.bin !== 'vendor' && !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-|svg$|media-|controls$)/.test(n)).sort();
const resolved = {};
await probe.setContent(shell, { waitUntil: 'load' });
resolved.light = await probe.evaluate((names) => {
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
  for (const name of names) {
    const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
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

// ---- the shop pass: sheet and font list only (its theme compiles to literals) ----
const shopSheets = await harvest(SHOP + '/');
let shop = null;
if (shopSheets) {
  const shopResult = await probe.evaluate((sheets) => {
    // A font-face src can carry a signed or per-account query: record any url() as url(…).
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const fonts = [];
    const errors = [];
    const names = new Set();
    const walk = (list, file) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) { walk(r.cssRules, file); continue; }
        if (!r.style) continue;
        for (let i = 0; i < r.style.length; i++) if ((r.style[i] || '').startsWith('--')) names.add(r.style[i]);
      }
    };
    for (const [name, text] of sheets) {
      const ss = new CSSStyleSheet();
      try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
      walk(ss.cssRules, name);
    }
    return { fonts, errors, names: [...names].sort() };
  }, shopSheets);
  shop = {
    note: 'shop.dopper.com is a Magento 2 theme (Dopper/dopper_b2c): the same brand palette compiles to literal values — the names list is every custom property it declares (component-scoped only), the fonts list its @font-face rules. Shop token values are measured, not declared.',
    sheets: shopSheets.map(([n, t]) => `${n} (${t.length} bytes)`),
    names: shopResult.names,
    fonts: shopResult.fonts,
    errors: shopResult.errors,
  };
}
await browser.close();

const ok = result.rules;
const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during a live home load on www.dopper.com (the linked /_next/static/css/ bundles captured as network responses plus the inline <style> blocks, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets at 1440 x 900. The site is light-only: no dark class, attribute or prefers-color-scheme rule exists in the bundles. out.shop records the Magento storefront (shop.dopper.com) sheet and font list; its theme compiles the same palette to literal values, so shop tokens are measured on the elements',
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
  shop,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}`);
if (shop) console.log(`shop: ${shop.sheets.length} sheets, ${shop.fonts.length} font faces, ${shop.names.length} custom props`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
