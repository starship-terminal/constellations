// Reads every custom property homerun.co's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Four signed-out surfaces, each with its own stylesheet set:
//   www    www.homerun.co — a Webflow build: one shared CDN sheet
//          (css-rules readable through the CSSOM because the <link> carries
//          crossorigin=anonymous) plus small inline <style> embeds, and
//          the Google-Fonts + cookie-banner sheets fetched directly.
//   jobs   jobs.homerun.co — the employer careers site: static.homerun.co
//          sheets are cross-origin to the CSSOM and fetched directly.
//   app    app.homerun.co/login — the ATS sign-in card: same-origin Angular
//          bundles (--gray1-12 Radix greys, --ui-* roles, toast vars).
//   apphr  app.homerun.hr/Account/Logon — the .NET HR sign-in: Tailwind
//          variables.
// Every rule declaring a --* property is kept with its selector and
// enclosing @media/@layer context, and @font-face rules are kept too.
//
// All four surfaces paint one light theme (no dark control exists on any).
// Each name is resolved in a probe document carrying its own surface's
// stylesheets, computed the way the browser computes it: colours come back
// as sRGB hex, lengths as px at 1440 x 900.
//
// Bins:
//   token     namespaced design-token names (--ui-*, --token-*)
//   app       other custom names the site's own rules declare
//   framework third-party internals (--tw-*, toast/editor vendors)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, JOBS, APP, APPHR, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const SURFACES = [
  { key: 'www', url: BASE + '/' },
  { key: 'jobs', url: JOBS + '/' },
  { key: 'app', url: APP + '/login', wait: 14000 },
  { key: 'apphr', url: APPHR + '/Account/Logon', wait: 9000 },
];

const { browser, context } = await launch();

// The Webflow sheet and the careers/login stylesheets sit on CDNs — some
// CSSOM-readable, some cross-origin. The unreadable ones are static public
// stylesheets, so their text is fetched directly and parsed the same way.
import https from 'node:https';
const fetchText = (url) => new Promise((resolve, reject) => {
  https.get(url, { headers: { 'user-agent': 'Mozilla/5.0' } }, (res) => {
    if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location)
      return resolve(fetchText(new URL(res.headers.location, url).href));
    if (res.statusCode !== 200) return reject(new Error('HTTP ' + res.statusCode));
    let body = ''; res.on('data', (d) => (body += d)); res.on('end', () => resolve(body));
  }).on('error', reject);
});

const surfaceData = [];
for (const s of SURFACES) {
  const page = await context.newPage();
  await page.goto(s.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(s.wait || 7000);
  const sheets = await page.evaluate(() => [...document.styleSheets].map((sh, i) => {
    try { return { name: sh.href || 'inline-' + i, media: sh.media.mediaText || '', css: [...sh.cssRules].map((r) => r.cssText).join('\n') }; }
    catch { return { name: sh.href || 'sheet-' + i, media: '', css: '', unreadable: true }; }
  }));
  await page.close();
  for (const sh of sheets) {
    if (sh.unreadable && /^https?:/.test(sh.name)) {
      try { sh.css = await fetchText(sh.name); sh.fetched = true; delete sh.unreadable; }
      catch (e) { sh.fetchError = String(e); }
    }
  }
  surfaceData.push({ key: s.key, url: s.url, sheets });
  console.log(s.key, sheets.length, 'sheets,', sheets.filter((x) => x.css).length, 'readable/fetched');
}

// ---- harvest: every rule with --* declarations ----
const probe = await browser.newPage();
const allRules = [];
const allFonts = [];
const allErrors = [];
for (const sd of surfaceData) {
  const result = await probe.evaluate(({ sheets, key }) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const errors = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file, surface: key };
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
        if (n) rules.push({ file, surface: key, selector: r.selectorText, context: ctx, properties: props });
        if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
      }
    };
    for (const s of sheets) {
      if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: 'cross-origin to the CSSOM' }); continue; }
      const ss = new CSSStyleSheet();
      try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e) }); continue; }
      walk(ss.cssRules, [], s.name);
    }
    return { rules, fonts, errors };
  }, { sheets: sd.sheets, key: sd.key });
  allRules.push(...result.rules);
  allFonts.push(...result.fonts);
  allErrors.push(...result.errors);
}
await probe.close();

// ---- resolve each name the way the browser does, per surface ----
const resolved = {};
for (const sd of surfaceData) {
  const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await probe2.setContent('<!doctype html><html><head>'
    + sd.sheets.filter((s) => s.css).map((s) => '<style' + (s.media ? ' media="' + s.media + '"' : '') + '>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
  const want = [...new Set(allRules.filter((r) => r.surface === sd.key).flatMap((r) => Object.keys(r.properties)))]
    .filter((n) => !/^--tw-/.test(n)).sort(); // --_updated-colors-v2-* is Homerun's real palette layer, kept
  const res = await probe2.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const rootProbe = document.getElementById('probe-root');
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
    const probe = document.createElement('div');
    probe.style.cssText = 'position:absolute;left:0;top:0';
    box.appendChild(probe);
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
      else return { unparsed: c };
      a = Math.round(a * 1000) / 1000;
      return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
    };
    const out = {};
    for (const name of names) {
      const raw = noUrl(getComputedStyle(rootProbe).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
      probe.removeAttribute('style'); probe.style.cssText = 'position:absolute;left:0;top:0';
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
      else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
        probe.style.color = raw; r.kind = 'color'; r.value = norm(getComputedStyle(probe).color);
        if (typeof r.value === 'object') { r.kind = 'other'; r.note = 'colour space not converted: ' + r.value.unparsed; delete r.value; }
      } else if (!raw.includes('%') && CSS.supports('width', raw)) { probe.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(probe).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
      else if (CSS.supports('box-shadow', raw)) { probe.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(probe).boxShadow; }
      else if (CSS.supports('transition-duration', raw)) { probe.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(probe).transitionDuration; }
      else if (CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
      else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
      else r.kind = 'other';
      out[name] = r;
    }
    box.remove();
    return out;
  }, want);
  resolved[sd.key] = res;
  await probe2.close();
}
await browser.close();

const FRAMEWORK = /^--(tw-|sc-|framer|toast-|sonner|joy-|border|grid|section|stack|variant|ticker|cursor|overlay|scroll|breakpoint|blending|mask|filters?|transform|layout|styles)-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.some((n) => n.startsWith('--token-') || n.startsWith('--ui-'))) return 'token';
  if (names.every((n) => FRAMEWORK.test(n))) return 'framework';
  return 'app';
};
for (const r of allRules) r.bin = binOf(r);
const bySelector = {};
for (const r of allRules) {
  const key = `[${r.surface}:${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(allRules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'four signed-out homerun surfaces: www.homerun.co (Webflow shared CDN sheet, CSSOM-readable, plus Google-Fonts/cookie-banner sheets fetched directly), jobs.homerun.co (static.homerun.co sheets fetched), app.homerun.co/login (same-origin Angular bundles) and app.homerun.hr/Account/Logon (Tailwind sheet), read on the live pages and re-parsed in probe documents; each surface\'s names resolved on a probe carrying that surface\'s own sheets',
  surfaces: Object.fromEntries(surfaceData.map((sd) => [sd.key, { url: sd.url, sheets: sd.sheets.map(({ name, media, css }) => ({ name, media, bytes: css.length })) }])),
  counts: {
    rules: allRules.length,
    fonts: allFonts.length,
    names: { token: names('token').length, app: names('app').length, framework: names('framework').length, utility: names('utility').length },
    bySelector,
  },
  errors: allErrors,
  token: allRules.filter((r) => r.bin === 'token'),
  app: allRules.filter((r) => r.bin === 'app'),
  framework: allRules.filter((r) => r.bin === 'framework'),
  utility: allRules.filter((r) => r.bin === 'utility'),
  fonts: allFonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${allRules.length} rules, ${allFonts.length} font faces; names token ${out.counts.names.token}, app ${out.counts.names.app}, framework ${out.counts.names.framework}, utility ${out.counts.names.utility}`);
for (const k of Object.keys(resolved)) console.log(`  ${k}: ${Object.keys(resolved[k]).length} resolved`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 160)}`);
