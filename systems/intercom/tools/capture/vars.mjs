// Reads every custom property intercom.com's stylesheets declare and writes raw/css-vars.json.
// Adapted from the kit's vars.mjs for the public route: the marketing site is a Next.js app whose
// CSS ships as same-origin inline <style> blocks (Tailwind v4), readable straight off the live
// page's CSSOM. No copies are needed.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs [url]
//
// What it reads (seen 2026-11-17):
//   - @layer theme :root, :host       the design-token layer: --color-* (warm neutral ramp
//                                     cream/off-white/chalk/canvas/linen/clay, brand blue #000ce1,
//                                     navy, fin orange #ff5600, helpdesk #0007cb, the blueprint
//                                     blues and Tailwind's own ramp), --font-*, --text-*-*
//                                     responsive type scale, --radius-*, --ease-*, --animate-*,
//                                     --z-index-*, --container-*, --breakpoint-*, --spacing
//   - :root (unlayered)               --button-* component tokens, --font-fallback-*, --body-bg,
//                                     --bento-bg, --scroll-behavior
//   - .theme-light                    the nav's semantic colours (--color-nav-*); body carries it.
//                                     There is no .theme-dark anywhere and no theme switch.
//   - .intercom-legacy                the older palette (MediumLL/IvoryLL/DmMono fonts, the
//                                     pink/teal/yellow ramps, --color-nav-* legacy names)
//   - .brand-i2y4                     the "i2y4" campaign scope (operator/ecom/voice accents, the
//                                     blueprint-blue ramp, Saans/Serrif/SaansMono stacks)
//   - [data-media-player]             the media player component's vars
//   - utility classes \[--x:y]        one-off arbitrary values
//   - --tw-* / @layer properties      Tailwind internals
// Each rule is kept with its selector and enclosing @media/@supports/@layer context, every name is
// resolved the way the browser resolves it on a probe document carrying the sheets and the real
// theme class (body.theme-light, plus a scoped probe per named scope), then classified by assigning
// it to a real property. lab()/color-mix() progressive overrides resolve to sRGB. Viewport 1440x900.
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const URL_ARG = process.argv[2] || 'https://www.intercom.com/';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch();
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
await page.goto(URL_ARG, { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(6000);

// Pull every inline <style> block's text off the live page (the sheets are
// same-origin, so the CSSOM text and the block text are the same).
const rawBlocks = await page.evaluate(() => [...document.querySelectorAll('style')].map((s) => ({ css: s.textContent || '', media: s.getAttribute('media') || '' })));
const blocks = new Map();
for (const b of rawBlocks) {
  if (!b.css.trim()) continue;
  const key = crypto.createHash('sha1').update(b.media + b.css).digest('hex').slice(0, 10);
  if (!blocks.has(key)) blocks.set(key, { name: 'inline-' + key, media: b.media, bytes: b.css.length, css: b.css, copies: ['live:' + URL_ARG] });
}
const sheets = [...blocks.values()].sort((a, b) => b.bytes - a.bytes || a.name.localeCompare(b.name));

const parsePage = await browser.newPage();
await parsePage.setContent('<!doctype html><html><head></head><body></body></html>');
const result = await parsePage.evaluate((sheets) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      const isStyle = !!r.style;
      if (r.cssRules && r.cssRules.length && !isStyle) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.cssText.split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!isStyle) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    const ss = new CSSStyleSheet({ media: s.media || undefined });
    try { ss.replaceSync(s.css); } catch (e) { rules.push({ file: s.name, error: String(e) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts };
}, sheets.map(({ name, media, css }) => ({ name, media, css })));

// ---------------------------------------------------------------- resolution
//
// A declared value says little on its own (`var(--color-black) 80%` inside a color-mix), so every
// name is also resolved the way the browser resolves it. The probe document carries every sheet
// and body.theme-light — the class the real body carries — so .theme-light nav colours and the
// :root layer resolve as painted. Scope-scoped names resolve on matching probes: .intercom-legacy,
// .brand-i2y4 and [data-media-player] elements sit under body.theme-light, exactly the way a real
// scoped element would. One pass: light — the site has no dark theme.
const page2 = await browser.newPage();
const shell =
  '<!doctype html><html lang="en"><head>'
  + sheets.map((s) => '<style' + (s.media ? ' media="' + s.media + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="theme-light"><div id="probe-root"></div>'
  + '<div class="intercom-legacy"><div id="probe-legacy"></div></div>'
  + '<div class="brand-i2y4"><div id="probe-brand"></div></div>'
  + '<div data-media-player><div id="probe-media"></div></div>'
  + '</body></html>';
await page2.setContent(shell, { waitUntil: 'load' });

// Which probe resolves which name: rules scoped to a named theme scope go to
// that scope's probe, everything else to the root probe under body.theme-light.
const SCOPE_PROBE = [
  [/\.intercom-legacy\b/, 'probe-legacy', 'legacy'],
  [/\.brand-i2y4\b/, 'probe-brand', 'brand'],
  [/data-media-player\b/, 'probe-media', 'media'],
];
const want = [...new Set(result.rules.filter((r) => !r.error && !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
// names per scope: a name declared under .intercom-legacy resolves on that
// scope's probe (it can differ from the :root value — --color-black does).
const scopeNames = { legacy: new Set(), brand: new Set(), media: new Set() };
for (const r of result.rules) {
  if (r.error) continue;
  for (const [re, , scope] of SCOPE_PROBE) {
    if (re.test(r.selector || '')) for (const n of Object.keys(r.properties)) if (want.includes(n)) scopeNames[scope].add(n);
  }
}

const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
const RESOLVE_BODY = `({ names, probeId, noUrl }) => {
  const host = document.getElementById(probeId);
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0';
  box.appendChild(probe);
  host.appendChild(box);
  const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
  const fromOklab = (L, a, b) => {
    const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
    return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
  };
  // CSS lab() is D50. Convert to D65 (Bradford) before the sRGB matrix, the
  // same path as css-colour.mjs. Treating the D50 XYZ as D65 shifts
  // --color-blue-600 from #155dfc to #0062fb.
  const fromLab = (L, a, b) => {
    const fy = (L + 16) / 116, fx = fy + a / 500, fz = fy - b / 200, e = 216 / 24389, k = 24389 / 27;
    const finv = (t) => (t ** 3 > e ? t ** 3 : (116 * t - 16) / k);
    const X = finv(fx) * 0.3457 / 0.3585, Y = L > k * e ? fy ** 3 : L / k, Z = finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585;
    const x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z, y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z, z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z;
    return [3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z, -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z, 0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
  };
  const num = (x) => (x.endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
  const norm = (c) => {
    let m = c.match(/^rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)$/);
    let rgb, a = 1;
    if (m) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v)); a = m[4] === undefined ? 1 : +m[4]; }
    else if ((m = c.match(/^color\\(srgb ([-\\d.e]+) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^oklab\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^oklch\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^lab\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = fromLab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
    else if ((m = c.match(/^lch\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromLab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
    else return { unparsed: c };
    a = Math.round(a * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : 'rgba(' + rgb.join(', ') + ', ' + a + ')';
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(host).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    const hsl = /^-?[\\d.]+(deg)? [\\d.]+% [\\d.]+%$/.test(raw);
    const asColor = hsl ? 'hsl(' + raw + ')' : raw;
    probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\\d*\\.?\\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (/^calc\\(\\s*(-?[\\d.e]+)\\s*\\/\\s*(-?[\\d.e]+)\\s*\\)$/.test(raw)) { r.kind = 'number'; r.value = +(raw.match(/-?[\\d.e]+/g).reduce((a, b) => a / b)); } // Tailwind v4 calc(a / b) ratios (line-heights)
    else if (/^(normal|none|auto|inherit|initial|unset|revert|revert-layer|cover|contain)$/.test(raw)) { r.kind = 'other'; r.value = raw; r.note = 'keyword'; }
    else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
    else if (CSS.supports('color', asColor) && !/^(inherit|initial|unset|revert)$/.test(asColor)) {
      probe.style.color = asColor; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
      if (hsl) r.hslTriplet = true;
    } else if (!raw.includes('%') && raw !== 'auto' && CSS.supports('width', raw)) { probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
    else if (CSS.supports('box-shadow', raw)) { probe.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(probe).boxShadow; }
    else if (CSS.supports('transition-duration', raw)) { probe.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(probe).transitionDuration; }
    else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
    else if (/[\\d.]m?s\\b|infinite|cubic-bezier|steps\\(/.test(raw) && CSS.supports('animation', raw)) { r.kind = 'animation'; r.value = raw; } // a lone ident (cover, inherit) is not an animation
    else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
    else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}`;
const resolveIn = async (names, probeId) => page2.evaluate(({ names, probeId, body, noUrlSource }) => {
  const fn = new Function('a', 'return (' + body + ')(a)');
  const pageNoUrl = new Function('return (' + noUrlSource + ')')();
  return fn({ names, probeId, noUrl: pageNoUrl });
}, { names, probeId, body: RESOLVE_BODY, noUrlSource: noUrl.toString() });
const resolved = {
  light: await resolveIn(want, 'probe-root'),
  scopes: {
    legacy: await resolveIn([...scopeNames.legacy], 'probe-legacy'),
    brand: await resolveIn([...scopeNames.brand], 'probe-brand'),
    media: await resolveIn([...scopeNames.media], 'probe-media'),
  },
};

// Does any page paint differently under prefers-color-scheme: dark? Read on the
// live page: the computed body/background colours before and after emulation.
const themeChecks = await page.evaluate(() => ({ colorScheme: getComputedStyle(document.documentElement).colorScheme, bodyClass: document.body.className }));
await page.emulateMedia({ colorScheme: 'dark' });
await page.waitForTimeout(600);
themeChecks.darkEmulated = await page.evaluate(() => ({ bodyBg: getComputedStyle(document.body).backgroundColor, mainBg: getComputedStyle(document.querySelector('main') || document.body).backgroundColor, color: getComputedStyle(document.body).color, bodyClass: document.body.className }));
await page.emulateMedia({ colorScheme: 'light' });
await page.waitForTimeout(400);
themeChecks.lightEmulated = await page.evaluate(() => ({ bodyBg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color }));
await browser.close();

// ---------------------------------------------------------------- bins
const binOf = (r) => {
  const sel = r.selector || '';
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(sel)) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (/\.intercom-legacy\b/.test(sel)) return 'legacy';
  if (/\.brand-i2y4\b/.test(sel)) return 'brand';
  if (/data-media-player\b/.test(sel)) return 'media';
  if (/\.theme-(light|dark)\b/.test(sel)) return 'nav';
  if (/^:root\b|^:root,\s*:host|^html\b/.test(sel)) return 'theme';
  return 'component';
};
const ok = result.rules.filter((r) => !r.error);
for (const r of ok) r.bin = binOf(r);

const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'), // the local date of the run
  source: 'the inline <style> blocks of the live www.intercom.com home page (Tailwind v4 build), deduplicated by content, read through the CSSOM of a headless Chromium; resolved on a probe document carrying body.theme-light plus .intercom-legacy/.brand-i2y4/[data-media-player] scoped probes',
  url: URL_ARG,
  sheets: sheets.map(({ name, media, bytes }) => ({ name, media, bytes })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: Object.fromEntries(['theme', 'nav', 'legacy', 'brand', 'media', 'component', 'utility', 'tailwind'].map((b) => [b, names(b).length])),
    bySelector,
  },
  errors: result.rules.filter((r) => r.error),
  theme: ok.filter((r) => r.bin === 'theme'),
  nav: ok.filter((r) => r.bin === 'nav'),
  legacy: ok.filter((r) => r.bin === 'legacy'),
  brand: ok.filter((r) => r.bin === 'brand'),
  media: ok.filter((r) => r.bin === 'media'),
  component: ok.filter((r) => r.bin === 'component'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  themeChecks,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`resolved: light ${Object.keys(resolved.light).length}`);
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names`, out.counts.names);
console.log('themeChecks', JSON.stringify(themeChecks));
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 160)}`);
