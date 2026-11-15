// Reads every custom property family.co's and app.family.co's stylesheets declare and writes
// raw/css-vars.json (marketing) and raw/app-css-vars.json (the login surface).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// family.co is a styled-components site: every rule lives in inline <style>
// tags readable through the CSSOM — there are no linked stylesheets on the
// marketing pages. Its token layer is a small declared set (--body,
// --body-muted, --heading, --blue, --orange, --beige, --gray-light, the
// --graphic-* brand fills, --app-*, --color-* form roles, --focus, --white)
// in Display-P3. app.family.co ("Aave Account") is a Next.js app that serves
// linked CSS chunks; it declares the product's real token layer
// (--family-*/--primary-*/--danger-*/--valid-*/--warning-* 100-800 scales,
// the --wallet-* palette, --overlay-*/--input-*/--body-* roles, --duration-*/
// --ease-* motion tokens, --font-*, --hr-color, --icon-*, --focus-color).
// External bodies are read from the network responses, inline <style>
// blocks through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too.
//
// Each name is resolved on the live document root of the page that declares
// it (the marketing probe carries a second pass with no theme class — there
// is no dark theme on either surface; prefers-color-scheme rules are counted
// but none exist). Display-P3 and other colour notations come back as sRGB
// hex, lengths as px at 1440 x 900.
//
// Bins:
//   theme     design-token-looking names wherever they are declared —
//             the marketing --color-*/--app-*/--graphic-* set and the app's
//             --family-*/--primary-*/--danger-*/--valid-*/--warning-*/
//             --wallet-*/--overlay-*/--input-*/--duration-*/--ease-* roles
//   app       any other custom property the site's own sheets declare
//   vendor    embedded widget/framework vars
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   tailwind  Tailwind internals: --tw-*, @layer properties
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Loads `url` and returns the page's stylesheet bodies: linked sheets from
// network responses, inline <style> blocks through the CSSOM.
async function harvest(url, { wait = 7000 } = {}) {
  const bodies = new Map();
  for (let tries = 0; tries < 6; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(wait);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      await p.close();
      await context.close();
      return { sheets: [...bodies.entries()].concat(inline) };
    }
    console.log('challenge page on', url, '(try ' + (tries + 1) + ')');
    await context.close();
  }
  console.log('blocked by the edge on every try for', url);
  return { sheets: [] };
}

const mkt = await harvest(BASE + '/');
const app = await harvest(APP + '/', { wait: 9000 });
if (!mkt.sheets.length && !app.sheets.length) { console.log('nothing harvested; css-vars.json not written'); await browser.close(); process.exit(2); }

// ---- shared colour/length resolution helpers, injected into the probe ----
// noUrl is the kit's canonical declaration (kept byte-identical for the
// privacy test); its function source is bound as `const noUrl` inside
// probeFns so the injected code can call it by name.
const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
const probeFns = `
const noUrl = ${noUrl};
const lin = (c) => (c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055);
const linInv = (c) => (c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
const fromOklab = (L, a, b) => {
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
  return [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s, -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s].map((v) => Math.round(Math.min(1, Math.max(0, lin(v))) * 255));
};
const p3ToSrgb = (r, g, b) => {
  const rl = linInv(r), gl = linInv(g), bl = linInv(b);
  const lr = 1.2249401 * rl - 0.2249404 * gl, lg = -0.0420569 * rl + 1.0420571 * gl, lb = -0.0196376 * rl - 0.0786361 * gl + 1.0982735 * bl;
  return [lr, lg, lb].map((v) => Math.round(Math.min(1, Math.max(0, lin(Math.min(1, Math.max(0, v))))) * 255));
};
const num = (x) => (x.endsWith('%') ? parseFloat(x) / 100 : parseFloat(x));
const norm = (c) => {
  let m = c.match(/^rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)$/);
  let rgb, a = 1;
  if (m) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v)); a = m[4] === undefined ? 1 : +m[4]; }
  else if ((m = c.match(/^#([0-9a-fA-F]{3,8})$/))) { let h = m[1]; if (h.length <= 4) h = [...h].map((x) => x + x).join(''); rgb = [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16)); a = h.length === 8 ? Math.round(parseInt(h.slice(6, 8), 16) / 2.55) / 100 : 1; }
  else if ((m = c.match(/^color\\(srgb ([-\\d.e]+) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = [m[1], m[2], m[3]].map((v) => Math.round(Math.min(1, Math.max(0, +v)) * 255)); a = m[4] === undefined ? 1 : num(m[4]); }
  else if ((m = c.match(/^color\\(display-p3 ([-\\d.e]+) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = p3ToSrgb(+m[1], +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
  else if ((m = c.match(/^oklab\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { rgb = fromOklab(num(m[1]), +m[2], +m[3]); a = m[4] === undefined ? 1 : num(m[4]); }
  else if ((m = c.match(/^oklch\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) { const h = (+m[3] * Math.PI) / 180; rgb = fromOklab(num(m[1]), +m[2] * Math.cos(h), +m[2] * Math.sin(h)); a = m[4] === undefined ? 1 : num(m[4]); }
  else if ((m = c.match(/^lab\\(([-\\d.e]+%?) ([-\\d.e]+) ([-\\d.e]+)(?: \\/ ([\\d.]+%?))?\\)$/))) {
    const fy = (num(m[1]) + 16) / 116, fx = fy + (+m[2]) / 500, fz = fy - (+m[3]) / 200;
    const eps = 216 / 24389, kap = 24389 / 27;
    const f = (t) => (t ** 3 > eps ? t ** 3 : (116 * t - 16) / kap);
    const X = 0.96422 * f(fx), Y = f(fy), Z = 0.82521 * f(fz);
    const r = 3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z, g = -0.9787684 * X + 1.9161415 * Y + 0.033454 * Z, bl = 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z;
    rgb = [r, g, bl].map((v) => Math.round(Math.min(1, Math.max(0, lin(Math.min(1, Math.max(0, v))))) * 255)); a = m[4] === undefined ? 1 : num(m[4]);
  }
  else return { unparsed: c };
  a = Math.round(a * 1000) / 1000;
  return a === 1 ? '#' + rgb.map((v) => Math.min(255, Math.max(0, v)).toString(16).padStart(2, '0')).join('') : 'rgba(' + rgb.map((v) => Math.min(255, Math.max(0, v))).join(', ') + ', ' + a + ')';
};
`;

// ---- harvest pass: re-parse each surface's sheets, keep every --* rule ----
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const probe = await probeCtx.newPage();
async function parseSheets(sheets) {
  return probe.evaluate(({ sheets, fns }) => {
    const { noUrl } = new Function(fns + '; return {noUrl};')();
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
  }, { sheets, fns: probeFns });
}

// ---- resolution: probe document carrying the surface's sheets ----
async function resolveSheets(sheets, names, theme) {
  const html = `<!doctype html><html${theme ? ` data-theme="${theme}"` : ''}><head>`
    + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body><div id="probe-root"></div></body></html>';
  await probe.setContent(html, { waitUntil: 'load' });
  return probe.evaluate(({ names, fns }) => {
    const { noUrl, norm } = new Function(fns + '; return {noUrl, norm};')();
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
    const p = document.createElement('div');
    box.appendChild(p);
    document.body.appendChild(box);
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
        if (/(em|rem)$/.test(raw)) { r.value = raw; r.note = 'font-relative length, kept as declared'; }
        if (r.value === '0px' && !/^[.\d]/.test(raw)) { r.value = raw; r.note = 'sizing keyword, not a fixed length'; }
      }
      else if (CSS.supports('box-shadow', raw)) { p.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(p).boxShadow; }
      else if (CSS.supports('transition-duration', raw)) { p.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(p).transitionDuration; }
      else if ((CSS.supports('transition-timing-function', raw) && !/^[a-z-]+$/.test(raw)) || /^(ease|ease-in|ease-out|ease-in-out|linear)$/.test(raw)) { r.kind = 'easing'; r.value = raw; }
      else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
      else r.kind = 'other';
      out[name] = r;
    }
    box.remove();
    return out;
  }, { names, fns: probeFns });
}

async function surface({ sheets, source, file }) {
  const parsed = await parseSheets(sheets);
  const want = [...new Set(parsed.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
    .filter((n) => !/^--(tw-|_|lightningcss-|radix-|removed-body-scroll-bar-size)/.test(n)).sort();
  // Names that resolve to nothing on :root (component-scoped defaults) are
  // still recorded raw under their rule; resolved only keeps what resolves.
  const resolvedLight = await resolveSheets(sheets, want, '');
  // The app declares a real [data-theme="dark"] theme (the login never paints
  // it signed out, but the declarations are honest evidence); the marketing
  // sheet declares no theme attribute, so its dark pass re-resolves the same
  // values — "no theme switch exists" for that surface.
  const resolvedDark = await resolveSheets(sheets, want, 'dark');
  const out = {
    readAt: new Date().toLocaleDateString('en-CA'),
    source,
    sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
    counts: { rules: parsed.rules.length, fonts: parsed.fonts.length, names: {} },
    errors: parsed.errors,
    rules: parsed.rules,
    fonts: parsed.fonts,
    resolved: { light: resolvedLight, dark: resolvedDark },
  };
  return { parsed, out };
}

const THEME = /^--(color|app|graphic|background|beige|blue|body|focus|font|gap|gray|grey|heading|h-pad|nh-pad|orange|scrollbar|twitter|white|family|primary|danger|valid|warning|wallet|overlay|input|hr|icon|logo|selection|hyperlink|duration|ease|banner|card|dropdown|verified|verified-|txn|loading|otp|qr|skeleton|success|token-picker|sidebar|page|padding|border|shadow|text|z|dark)/;
const VENDOR = /video-js|vjs-|stripe|sonner|geist|inter_[0-9a-f]+-module|swiper|slick|gdpr|osano|intercom|ck-|--s-|--chakra-|__nextjs|full-paste|radix/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.every((n) => THEME.test(n))) return 'theme';
  return 'app';
};

fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
async function write(tag, surf, source) {
  if (!surf.sheets.length) { console.log('no sheets for', tag); return; }
  const { parsed, out } = await surface({ sheets: surf.sheets, source });
  for (const r of parsed.rules) r.bin = binOf(r);
  out.rules = parsed.rules;
  for (const bin of ['theme', 'app', 'vendor', 'utility', 'tailwind']) {
    out.counts.names[bin] = [...new Set(parsed.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].length;
    out[bin] = parsed.rules.filter((r) => r.bin === bin);
  }
  const bySelector = {};
  for (const r of parsed.rules) {
    const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
    bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
  }
  out.counts.bySelector = bySelector;
  fs.writeFileSync(path.join(REF, 'raw', tag), JSON.stringify(out, null, 1) + '\n');
  console.log(`${tag}: ${parsed.rules.length} rules, ${parsed.fonts.length} font faces; names`, out.counts.names, '; resolved', Object.keys(out.resolved.light).length);
  for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 12)) console.log(`  ${v}\t${k.slice(0, 140)}`);
}

await write('css-vars.json', mkt, 'the stylesheet bodies read during a live signed-out load of / on family.co (styled-components inline <style> blocks, re-parsed with CSSStyleSheet); resolved on a probe document carrying the real sheets at 1440 x 900. Display-P3 declarations are reported as sRGB hex');
await write('app-css-vars.json', app, 'the linked CSS chunks read during a live signed-out load of / on app.family.co ("Aave Account" login), re-parsed with CSSStyleSheet; resolved on a probe document carrying the real sheets at 1440 x 900. Display-P3 declarations are reported as sRGB hex');

await probeCtx.close().catch(() => {});
await browser.close();
