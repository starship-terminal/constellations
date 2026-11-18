// Reads every custom property forhers.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// www.forhers.com answers this network with a Cloudflare managed challenge on
// every route, so the evidence is the Wayback snapshots under
// ~/.design-systems/forhers/pages served locally by lib.mjs's servePages —
// with the site's /css/, /forhims/, /image/ assets and /asset/<host>/ mirrors
// under scratch. Every forhers stylesheet is therefore same-origin and
// inline: the SSR markup carries the whole styled-components sheet as one
// <style> block per page (~340 KB on the home page), so document.styleSheets
// is fully readable through the CSSOM. forhers declares no palette layer:
// its custom properties are layout globals on :root (--gridColumn,
// --gridGutter, --headerHeight, --promoHeight, --headerOffset,
// --global-nav-header-row-height) and component-scoped vars each
// styled-components class sets on itself or its subtree (--btn-*,
// --border-radius, --max-font-size, --carousel-item-*, --disclaimer--*,
// --continuity-modal--*). The site's "base" design-token layer is only
// *referenced*, with fallbacks (var(--b-color-neutral-dark-1000,#000000)),
// never declared in the SSR sheets — it ships with the web-components
// bundle the signed-in and tool surfaces load, which this capture does
// not reach. Rules declaring a --* property are kept with selector and
// @media context; @font-face rules are kept too.
//
// Each name is resolved in a probe document carrying the real sheets at
// 1440 x 900: colours come back as sRGB hex, lengths as px. forhers paints
// one theme — data-theme="light"/"hers" are per-component variants, not a
// page switch — so the "dark" pass repeats :root.
//
// Bins:
//   global     vars declared on :root / html / body (the layout globals)
//   component  vars declared on class selectors (styled-components scopes)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, servePages, launch as launchCtx, open as openPage, closePromo, PAGES, SCRATCH, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const browser = await chromium.launch();
const { srv, port } = await servePages(`${SCRATCH}/pages`, `${SCRATCH}/assets`);

// ---- collect every same-origin sheet from every archived page ----
const bodies = new Map(); // name -> cssText
const perPage = {};
for (const [key] of Object.entries(PAGES)) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  const p = await context.newPage();
  await openPage(p, `http://127.0.0.1:${port}/pages/${key}.html`, { wait: 5000 });
  await closePromo(p);
  const sheets = await p.evaluate(() => [...document.styleSheets].map((s, i) => {
    try {
      const node = s.ownerNode;
      const emo = node && node.getAttribute && node.getAttribute('data-emotion');
      const name = s.href ? s.href.split('/').pop() : 'inline-' + (emo ? emo : i);
      return [name, [...s.cssRules].map((r) => r.cssText).join('\n')];
    } catch { return null; }
  }).filter(Boolean));
  perPage[key] = sheets.length;
  for (const [n, t] of sheets) bodies.set(`${key}/${n}`, t);
  await context.close();
  console.log('page', key, sheets.length, 'sheets');
}
const sheets = [...bodies.entries()];

// ---- harvest: every rule with --* declarations ----
const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const noPayload = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(["']?)data:([^;,"')]*)[^)]*\)/gi, 'url($1data:$2;…$1)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        // Keep family/weight/style/display; point urls at url(…) and never carry an embedded font payload.
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noPayload(noUrl(r.style.getPropertyValue(r.style[i]).trim()));
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

// ---- resolution: probe document with the real sheets at 1440 x 900 ----
// browser.newPage() is 1280 wide by default. The capture declared 1440, and
// viewport-relative values (calc(100vw / 24) is 60px there, 53.3281px at 1280)
// must be resolved at that width.
await probe.setViewportSize({ width: 1440, height: 900 });
const shell = () => '<!doctype html><html><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|ot[A-Z]|onetrust)/i.test(n)).sort();
const resolved = {};
for (const pass of ['dark', 'light']) {
  await probe.setContent(shell(), { waitUntil: 'load' });
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
      const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
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
srv.close();

// forhers declares no token layer in the SSR sheets: globals live on
// :root/html/body (grid, header, promo), everything else is a var a
// styled-components class declares on itself or its subtree.
const binOf = (r) => (/^(:root|html|body)\b/.test((r.selector || '').trim()) ? 'global' : 'component');
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
  source: 'the CSSOM of the archived forhers.com SSR pages (Wayback snapshots 2025-12-23 to 2026-11-11, served locally; live forhers.com answers a Cloudflare managed challenge to this network) — each page carries its whole styled-components sheet as one inline <style> block, re-parsed with CSSStyleSheet; resolved in a probe carrying the real sheets on :root at 1440 x 900 — the site paints one theme, so the dark pass repeats :root',
  pages: Object.entries(perPage).map(([k, n]) => `${k}: ${n} sheets`),
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { global: names('global').length, component: names('component').length },
    bySelector,
  },
  errors: result.errors,
  global: ok.filter((r) => r.bin === 'global'),
  component: ok.filter((r) => r.bin === 'component'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names global ${out.counts.names.global}, component ${out.counts.names.component}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}, dark ${Object.keys(resolved.dark).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
