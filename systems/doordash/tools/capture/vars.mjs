// Reads every custom property DoorDash's stylesheets declare and writes
// raw/css-vars.json. Also writes raw/archive-urls.json, the snapshot
// provenance table for every archived route the kit touches.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// BOUNDARY: live *.doordash.com Cloudflare-blocks this client (403 managed
// challenge on every surface tried). The harvest therefore renders the
// product's own pages from Internet Archive Wayback snapshots — the same
// SSR HTML and the same stylesheet bodies, served through web.archive.org.
// Wayback's own injected chrome/sheets are binned `archive` and never
// studied. Route URLs in ROUTES are "<snapshot>/<original url>"; recorded
// sheet names have the archive prefix stripped back to the original URL.
//
// doordash.com (consumer-web-next) declares the prism token system under
// :where(.prism-theme): --base-* primitives (colour ramps incl. the
// doordash/caviar/dashpass brand palettes, DD Norms type scale),
// --usage-* semantic roles (colour, type, elevation, radius, motion) and
// --comp-* component tokens. The same sheet ships sibling prism brand
// themes — [data-dt-theme="deliveroo"|"plus"|…][data-dt-mode="light"|"dark"]
// scope blocks — none of which a doordash.com visitor gets, so only the
// doordash (unscoped prism-theme) light set is tokenised. careersat
// doordash.com is a separate WordPress/Tailwind stack; its sheets are
// harvested for context and mostly bin as tailwind/utility.
//
// Each name is resolved in a probe document carrying the real sheets and a
// body.prism-theme scope, computed the way the browser computes it: colours
// come back as sRGB hex, lengths as px at 1440 x 900.
//
// Bins:
//   theme     the prism design-token layer: --base-*, --usage-*, --comp-*,
//             --prism-* and any other token-shaped names
//   app       other custom properties the site's own sheets declare
//   scoped    generated per-element component vars (--a1b2c3d4-0 …) the
//             consumer-web-next styled system emits inline
//   vendor    embedded widget vars (turnstile, onetrust)
//   archive   the Wayback Machine's own replay chrome
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals on the careers stack: --tw-*
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

// The archived routes the whole kit uses, single source of truth — also the
// provenance written to raw/archive-urls.json.
const ROUTES = {
  home: '20261112001404/https://www.doordash.com/',
  'food-delivery': '20261004033917/https://www.doordash.com/food-delivery/',
  business: '20261012092322/https://www.doordash.com/en-US/business/',
  dashpass: '20261012183135/https://www.doordash.com/en-US/dashpass/student',
  restaurants: '20261005002021/https://www.doordash.com/en-US/restaurants-near-me/',
  store: '20261024031734/https://www.doordash.com/en-US/store/the-sweet-tooth-north-miami-beach-33434247/',
  hsa: '20260930222321/https://www.doordash.com/en-US/p/hsa-fsa-store',
  seasonal: '20261025153234/https://www.doordash.com/en-US/p/seasonal-holidays/',
  promos: '20261008212700/https://www.doordash.com/en-US/promos/',
  careers: '20261009000533/https://careersatdoordash.com/',
};
const stripWayback = (u) => {
  const m = u.match(/^https?:\/\/web\.archive\.org\/web\/\d+[a-z_]*\/(.*)$/i);
  return m ? 'https://' + m[1].replace(/^https?:\/\//, '') : u;
};

fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'archive-urls.json'), JSON.stringify({
  note: 'DoorDash capture provenance. Live *.doordash.com answered Cloudflare 403 to every client tried on 2026-11-13; the product evidence in this package is the product\u2019s own SSR HTML/CSS rendered from these Internet Archive snapshots. Timestamps are the wayback capture id.',
  boundary: 'https://www.doordash.com/ and related hosts returned 403 "Performing security verification" (curl, headless Chromium, headed Chrome, 2026-11-13).',
  routes: Object.fromEntries(Object.entries(ROUTES).map(([k, v]) => {
    const [ts, ...rest] = v.split('/');
    return [k, { snapshot: BASE + v, archived: rest.join('/'), captured: `${ts.slice(0, 4)}-${ts.slice(4, 6)}-${ts.slice(6, 8)} ${ts.slice(8, 10)}:${ts.slice(10, 12)}:${ts.slice(12, 14)} UTC` }];
  })),
}, null, 1) + '\n');

const { browser } = await launch();
// Three routes carry distinct sheet sets: the marketing home, a storefront
// (the consumer app shell) and the WordPress careers site.
const bodies = new Map();
const inlines = [];
for (const key of ['home', 'store', 'careers']) {
  const route = ROUTES[key];
  let got = false;
  for (let tries = 0; tries < 4 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(stripWayback(r.url().split('?')[0]), await r.text()); } catch { /* body gone */ }
    });
    await p.goto(BASE + route, { waitUntil: 'commit', timeout: 120000 }).catch(() => {});
    for (let i = 0; i < 30; i++) {
      const len = await p.evaluate(() => (document.body && document.body.innerText || '').length).catch(() => 0);
      if (len > 200) break;
      await p.waitForTimeout(2000);
    }
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inl = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + location.pathname.replace(/\//g, '') + '-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      inlines.push(...inl);
      got = true;
      await context.close();
      break;
    }
    console.log(route, 'challenge/empty page, fresh context (try ' + (tries + 1) + ')');
    await context.close();
  }
  if (!got) console.log(route, 'never rendered on every try; its sheets are missing');
}
if (!bodies.size && !inlines.length) { console.log('no stylesheets harvested; css-vars.json not written'); await browser.close(); process.exit(2); }
// inline sheets read via CSSOM; link sheets via the captured bodies
const sheets = [...bodies.entries()].concat(inlines);

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

// ---- resolution: probe document with the real sheets ----
// The prism layer scopes its declarations to :where(.prism-theme), so the
// probe body carries that class; nothing else rebinds the tokens (light
// only). One pass.
const shell = '<!doctype html><html><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="prism-theme"><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const [pass, attrs] of [['light', '']]) {
  await probe.setContent(shell, { waitUntil: 'load' });
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
    for (const name of names) {
      const raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
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
await browser.close();

const THEME = /^--(base|usage|comp|prism|color|font|text|spacing|radius|breakpoint|container|shadow|inset-shadow|drop-shadow|ease|animate|duration|delay|motion|elevation|z|grid|layout|icon-size|size)-?/;
const SCOPED = /^--[a-z0-9]{5,9}-\d+$/;
const ARCHIVE = /web-static\.archive\.org|archive\.org|wombat|wayback|--wm-|#wm-ipp|sparkline|iconochive/;
const VENDOR = /turnstile|onetrust|osano|ketch|intercom|video-js|stripe|--toast-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (ARCHIVE.test(r.file || '') || ARCHIVE.test(r.selector || '')) return 'archive';
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (names.every((n) => SCOPED.test(n))) return 'scoped';
  if (VENDOR.test(r.selector || '') || VENDOR.test(r.file || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.every((n) => THEME.test(n))) return 'theme';
  if (names.some((n) => THEME.test(n))) return 'theme';
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
  source: 'stylesheet bodies read during archived renders of the DoorDash marketing home, a storefront and the careers site (Wayback-proxied web-assets.cdn4dd.com Next.js CSS bundles plus inline <style> blocks, archive prefixes stripped, re-parsed with CSSStyleSheet); resolved in a probe carrying the real sheets on a body.prism-theme scope at 1440 x 900. Live *.doordash.com is Cloudflare-blocked for this client; see raw/archive-urls.json.',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, scoped: names('scoped').length, vendor: names('vendor').length, archive: names('archive').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.errors,
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  scoped: ok.filter((r) => r.bin === 'scoped'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  archive: ok.filter((r) => r.bin === 'archive'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names theme ${out.counts.names.theme}, app ${out.counts.names.app}, scoped ${out.counts.names.scoped}, vendor ${out.counts.names.vendor}, archive ${out.counts.names.archive}, utility ${out.counts.names.utility}, tailwind ${out.counts.names.tailwind}`);
console.log(`resolved: light ${Object.keys(resolved.light).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
