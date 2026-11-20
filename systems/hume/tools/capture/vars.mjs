// Reads every custom property the hume.ai public surfaces' stylesheets
// declare and writes raw/css-vars.json — plus a `palette` harvest of every
// literal colour the rules declare, per surface.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Four signed-out origins carry the product's design tokens:
//
//   www   www.hume.ai — Next.js + Tailwind v4. :root holds the product layer
//         (--background #fdfdfc / --foreground #1b1918, the four brand
//         families --font-sans/-serif/-mono/-japanese, the eleven-pastel
//         --accent-* ramp, five --gradient-* stops, the --title-* display
//         sizes); :root,:host holds the Tailwind default theme
//         (--color-*, --spacing, --container-*, --text-*, --font-weight-*,
//         --tracking-*, --leading-*, --radius-*, --ease-*, --animate-*,
//         --blur-*, --shadow-edge-dark, --color-spectrum-*). LIGHT ONLY —
//         no theme control exists (a .dark class and a dark colour-scheme
//         emulation both leave the painted surface unchanged).
//   docs  dev.hume.ai — a Fern docs build with a Hume-branded layer:
//         --gray-1..12 / --grayscale-* and --accent-* ramps re-pointed
//         under .dark, --background/--border/--code-background,
//         --hume-gradient, the --primitive-noul/-choice/-score/-span/-ink
//         decision-model hues, --font-body 'Fellix' / --font-code
//         'Fraktion'. The header Theme button's own menu (Light / Dark /
//         System) repaints html.light <-> html.dark — the only real theme
//         control on any captured surface.
//   demo  demo.hume.ai — the Audio Decision Model playground, gated on an
//         invitation email link. The gate page still loads the app's token
//         layer: --hume-white/-black, the --neutral-950..50 ramp, --tan-*,
//         the six --<hue>-100..400 families, --background-*/--border-*
//         roles, --body-font-weight. Light only.
//   app   app.hume.ai — the platform; /log-in is public. An oklch-based
//         shadcn layer (--background-body, --background-elevated,
//         --foreground, --muted-foreground, --border, --primary, Fellix).
//         Light only; nothing past the form was entered.
//
// Each surface's sheets are harvested from its live network responses plus
// inline <style> blocks and re-parsed; every custom property is then
// resolved in a probe document carrying that surface's real sheets — the
// docs under <html class="light"> and again under class="dark" (the
// classes the header Theme menu paints), the others at their painted
// default. Literal colour declarations are harvested into `palette` with
// their selectors. @font-face rules are kept by name only: the faces are
// proprietary (Martina Plantijn, PP Fraktion Mono/Fraktion, Fellix,
// M PLUS 1; Inter is open-licensed) and are never shipped.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, DOCS, DEMO, APP, UA, chromium, patch, clearChallenge } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

// surface -> the urls whose load warms its sheet pool, the html classes to
// resolve under, and a label for the provenance text.
const SURFACES = [
  { key: 'www', urls: [BASE + '/', BASE + '/products/decision-model-api', BASE + '/contact-form'], passes: [{ set: 'light', cls: '' }] },
  { key: 'docs', urls: [DOCS + '/audio-decisions/docs/overview', DOCS + '/audio-decisions/reference/decisions/create'], passes: [{ set: 'light', cls: 'light' }, { set: 'dark', cls: 'dark' }] },
  { key: 'demo', urls: [DEMO + '/decision-model/file'], passes: [{ set: 'light', cls: '' }] },
  { key: 'app', urls: [APP + '/log-in'], passes: [{ set: 'light', cls: '' }] },
];

const browser = await chromium.launch();
const wanted = process.argv.slice(2);
const out = { readAt: new Date().toLocaleDateString('en-CA'), surfaces: {} };

for (const S of SURFACES) {
  if (wanted.length && !wanted.includes(S.key)) continue;
  const bodies = new Map();
  let page = null, inline = [], bodyClass = '', htmlClass = '';
  for (let tries = 0; tries < 4 && !page; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    for (const u of S.urls) {
      await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(6000);
    }
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      page = p;
      [inline, bodyClass, htmlClass] = await p.evaluate(() => [
        [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean),
        document.body.className,
        document.documentElement.className.replace(/\b(light|dark)\b/g, '').trim(),
      ]);
      break;
    }
    console.log('challenge page on', S.key, '(try ' + (tries + 1) + ')');
    await context.close();
  }
  if (!page) { console.log('blocked on', S.key, '— skipped'); continue; }
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
    const colours = {};   // literal -> {count, uses:[{selector, context, property}]}
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

  // ---- resolution: probe document with the surface's real sheets, per pass ----
  const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
  const shell = (cls) => '<!doctype html><html class="' + cls + ' ' + escAttr(htmlClass) + '"><head>'
    + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body class="' + escAttr(bodyClass) + '"><div id="probe-root"></div></body></html>';
  const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
    .filter((n) => !/^--(tw-|_)/.test(n)).sort();
  const resolved = {};
  for (const pass of S.passes) {
    await probe.setContent(shell(pass.cls), { waitUntil: 'load' });
    resolved[pass.set] = await probe.evaluate((names) => {
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
  await probeCtx.close();

  const SKIN = /(^|[\s,>+~])\.(dark|light)\b|:is\(\.(dark|light)\b|html\.(dark|light)\b/;
  const VENDOR = /algolia|docsearch|ds-dropdown|video-js|vjs-|stripe|sonner|--toast-|cookiebot|cybot|--cb-|osano|gdpr|--hs-|--intercom|vimeo|sanity|statsig|hubspot|--hub|googletagmanager|gtm|--fa-|font-awesome|--_fa|intercom|clerk|fern-search/i;
  const binOf = (r) => {
    const names = Object.keys(r.properties);
    if (/\\\[--/.test(r.selector || '')) return 'utility';
    if (names.every((n) => n.startsWith('--tw-')) || r.context.some((c) => c === '@layer properties')) return 'tailwind';
    if (SKIN.test(r.selector || '') || r.context.some((c) => SKIN.test(c))) return 'skins';
    if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
    return 'app';
  };
  const rules = result.rules;
  for (const r of rules) r.bin = binOf(r);
  const names = (bin) => [...new Set(rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
  out.surfaces[S.key] = {
    urls: S.urls,
    sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
    counts: {
      rules: rules.length,
      fonts: result.fonts.length,
      palette: Object.keys(result.colours).length,
      names: { app: names('app').length, skins: names('skins').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    },
    errors: result.errors,
    app: rules.filter((r) => r.bin === 'app'),
    skins: rules.filter((r) => r.bin === 'skins'),
    vendor: rules.filter((r) => r.bin === 'vendor'),
    utility: rules.filter((r) => r.bin === 'utility'),
    tailwind: rules.filter((r) => r.bin === 'tailwind'),
    fonts: result.fonts,
    palette: result.colours,
    resolved,
  };
  console.log(`${S.key}: ${rules.length} rules, ${result.fonts.length} fonts, ${Object.keys(result.colours).length} palette literals; resolved ${Object.keys(resolved).map((k) => k + '=' + Object.keys(resolved[k]).length).join(', ')}`);
}

out.source = 'the stylesheet bodies read during live signed-out loads of the four public hume.ai surfaces (www.hume.ai marketing/product site, dev.hume.ai docs, the demo.hume.ai invitation gate, the app.hume.ai log-in) — linked bundles from network responses plus inline <style> blocks, re-parsed with CSSStyleSheet. Every custom property is resolved in a probe carrying that surface\'s own sheets: the docs under <html class="light"> and again under class="dark" (the classes the header Theme menu paints — the only real theme control on any surface), the rest at their painted default (www, demo and app are light-only). `palette` is each surface\'s harvest of literal colour declarations with the selectors that use them.';
await browser.close();
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars.json written for', Object.keys(out.surfaces).join(', '));
