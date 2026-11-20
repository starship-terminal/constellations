// Reads every custom property fresha.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Fresha ships one Panda CSS system (:root carries --made-with-panda) across
// three signed-out surfaces, plus one legacy surface:
//   www.fresha.com       consumer marketplace + auth shell (Next.js, sheets
//                        under /assets/_next/static/chunks/*.css)
//   www.fresha.com +   the B2B marketing app (/for-business, /pricing, /blog,
//     /assets/b2b-mktg /careers, /help-center — Next.js under
//                        /assets/b2b-mktg/_next/static/css/)
//   partners.fresha.com the professional sign-in (cdn-partners sheets)
//   /lp/en/...          the older marketplace microsite: its own stylesheet
//                        with NO token vars (literal values; hashed classes)
//
// The Panda token variables are hashed (--cNjPpP), so this script also parses
// the atomic class table the same sheets ship (bg-c_foreground.neutral,
// trs-tmf_easeInOut, bdr_m, anim-dur_medium.m …) and maps each var back to its
// design-token name: that map is written as `tokenMap` for
// build_component_tokens.py. The scopes observed are:
//   :where(:root,:host)                                the scales (spacing,
//                                                      sizes, radii, border
//                                                      widths, durations,
//                                                      easings, shadows…)
//   :where(:root,[data-theme=light],[data-theme=auto]) the colour palette
//   :where(:root,[data-theme=dark])                    the dark palette
//   @media (prefers-color-scheme: dark) [data-theme=auto]  same dark palette
//   [data-theme=accent]                                an accent scope
// No public page sets a data-theme (verified per host under `live`), so the
// light scope is what every signed-out page paints; `dark`/`accent` are
// DECLARED scopes resolved in probes and labelled declared, never painted.
//
// Resolution: probe documents carry each surface's real sheets; `light` and
// `lp` resolve the :root defaults, `dark` a data-theme=dark probe, `accent`
// a data-theme=accent probe. Colours come back as sRGB hex, lengths as px at
// 1440 x 900.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, PARTNER_SIGNIN, LP_BROWSE, UA, launch, clearChallenge, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Load each surface once, collecting stylesheet bodies from network responses
// and inline <style> blocks from the CSSOM. `live` records what theme the real
// document carries (root classes/attributes, any element with data-theme).
const HOSTS = [
  ['consumer', BASE + '/'],
  ['b2b', BASE + '/for-business'],
  ['partner', PARTNER_SIGNIN],
  ['lp', LP_BROWSE],
];
const sheets = [];
const live = {};
for (const [host, url] of HOSTS) {
  let got = null;
  for (let tries = 0; tries < 4 && !got; tries++) {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
    await patch(context);
    const p = await context.newPage();
    const bodies = new Map();
    p.on('response', async (r) => {
      if (r.request().resourceType() !== 'stylesheet') return;
      try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
    });
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(9000);
    if (await clearChallenge(p, { tries: 3, step: 1500 })) {
      const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
      live[host] = await p.evaluate(() => ({
        url: location.pathname,
        title: document.title.slice(0, 80),
        htmlAttrs: Object.fromEntries([...document.documentElement.attributes].map((a) => [a.name, a.value.slice(0, 60)])),
        colorScheme: getComputedStyle(document.documentElement).colorScheme,
        themedElements: [...document.querySelectorAll('[data-theme]')].slice(0, 12).map((n) => ({ theme: n.getAttribute('data-theme'), node: n.tagName.toLowerCase(), text: (n.innerText || '').trim().slice(0, 40) })),
        prefersDarkRules: [...document.styleSheets].reduce((n, s) => { try { return n + [...s.cssRules].filter((r) => r.media && /prefers-color-scheme:\s*dark/.test(r.media.mediaText)).length; } catch { return n; } }, 0),
      })).catch(() => null);
      got = [...bodies.entries(), ...inline];
    } else {
      console.log('challenge page on', host, '(try ' + (tries + 1) + ')');
      await context.close();
      continue;
    }
    await context.close();
  }
  if (!got) { console.log('blocked on', host, '; continuing without its sheets'); continue; }
  for (const [name, css] of got) sheets.push([`${host} ${name}`, css]);
}
if (!sheets.length) { console.log('no sheets harvested; css-vars.json not written'); await browser.close(); process.exit(2); }

// ---- harvest: every rule with --* declarations, plus the atomic class table ----
const probe = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const atomic = []; // [className, prop, value] for rules whose value references var(--x)
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
      const sel = r.selectorText || '';
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        const v = noUrl(r.style.getPropertyValue(k).trim());
        if (k && k.startsWith('--')) { props[k] = noUrl(v); n++; }
        if (/var\(--/.test(v) && sel && !/\\\[--/.test(sel)) {
          for (const cls of sel.split(',')) {
            const c = cls.trim().replace(/\\(.)/g, '$1').split(/\s|>|\+|~/).pop().replace(/^\./, '');
            if (c && c.length < 120) atomic.push({ cls: c, prop: k, value: v.slice(0, 160), file });
          }
        }
      }
      if (n) rules.push({ file, selector: sel.slice(0, 200), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, sel.slice(0, 120)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name, error: String(e) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors, atomic };
}, sheets);

// ---- token-name mapping: hashed var -> Panda token path, via class names ----
// .bg-c_background.page -> colors.background.page ; .anim-dur_medium.m -> durations.medium.m
function tokenOf(cls) {
  const c = cls.split(':').pop();
  let m = c.match(/-c_([A-Za-z][\w.]*)/) || c.match(/^(?:c|bg-c)_([A-Za-z][\w.]*)/);
  if (m) return 'colors.' + m[1];
  m = c.match(/^(?:p|px|py|ps|pe|pbs|pbe|pis|pie|pt|pr|pb|pl|m|mx|my|ms|me|mbs|mbe|mis|mie|mt|mr|mb|ml|gap|row-gap|column-gap|grid-gap|scroll-m|scroll-p|scr-p)_(-?\d+)$/);
  if (m) return 'spacing.' + m[1];
  if (/_(-?)sidePadding\./.test(c)) return 'spacing.' + c.match(/(-?)sidePadding\.[\w.]+/)[0];
  m = c.match(/^(?:bdr?|br)_(\w+)$/);
  if (m) return 'radii.' + m[1];
  m = c.match(/bd(?:-[a-z]+)?-w_(-?\d+)/);
  if (m) return 'borderWidths.' + m[1];
  if (/_breakpoint-/.test(c)) return 'sizes.' + c.match(/breakpoint-[\w-]+/)[0];
  if (/_fullWidth$/.test(c)) return 'sizes.fullWidth';
  m = c.match(/^(?:w-is|h-bs|min-w|min-h|max-w-is|max-b|size|w|h)_(-?[\d.]+)$/);
  if (m) return 'sizes.' + m[1];
  m = c.match(/^(?:fs|textSize|text)_([\w.]+)$/);
  if (m) return 'fontSizes.' + m[1];
  m = c.match(/^(?:anim-dur|trs-dur|anim-dly|trs-dly|--duration-var|anim|dur)_([\w.]+)$/);
  if (m) return 'durations.' + m[1].replace(/^durations\./, '');
  m = c.match(/^(?:anim-tmf|trs-tmf|--easing-var)_([\w.]+)$/);
  if (m) return 'easings.' + m[1];
  m = c.match(/^bx-sh_(\w+)$/);
  if (m) return 'shadows.' + m[1];
  m = c.match(/^asp_(\w+)$/);
  if (m) return 'aspectRatios.' + m[1];
  m = c.match(/^(?:op|opacity)_(\.?[\d]+)$/);
  if (m) return 'opacity.' + m[1];
  m = c.match(/^z_(-?\d+)$/);
  if (m) return 'zIndex.' + m[1];
  m = c.match(/^bkdp-blur_(\w+)$/);
  if (m) return 'backdropBlurs.' + m[1];
  m = c.match(/^fw_(\w+)$/);
  if (m) return 'fontWeights.' + m[1];
  m = c.match(/^lh_(\w+)$/);
  if (m) return 'lineHeights.' + m[1];
  m = c.match(/^ls_(\w+)$/);
  if (m) return 'letterSpacings.' + m[1];
  return null;
}

const tokenMap = {}; // var -> {token, classes[]}
for (const a of result.atomic) {
  const tn = tokenOf(a.cls);
  if (!tn) continue;
  for (const vm of a.value.matchAll(/var\((--[\w-]+)/g)) {
    const e = (tokenMap[vm[1]] ??= { token: tn, classes: [] });
    if (!e.token) e.token = tn;
    if (e.classes.length < 6 && !e.classes.includes(a.cls)) e.classes.push(a.cls);
  }
}

// ---- resolution probes ----
const hostsOf = (...prefixes) => sheets.filter(([n]) => prefixes.some((p) => n.startsWith(p + ' '))).map(([, css]) => css);
const panda = hostsOf('consumer', 'b2b', 'partner');
const SHELLS = {
  light: { css: panda, theme: null },
  dark: { css: panda, theme: 'dark' },
  accent: { css: hostsOf('partner', 'b2b'), theme: 'accent' },
  lp: { css: hostsOf('lp'), theme: null },
};
const shell = ({ css, theme }) => '<!doctype html><html' + (theme ? ' data-theme="' + theme + '"' : '') + '><head>'
  + css.map((c) => '<style>' + c.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.filter((r) => !r.context.includes('@layer properties') && !/\\\[--/.test(r.selector || '')).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|lightningcss-)/.test(n)).sort();
const resolved = {};
for (const pass of Object.keys(SHELLS)) {
  if (!SHELLS[pass].css.length) continue;
  await probe.setContent(shell(SHELLS[pass]), { waitUntil: 'load' });
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
      let raw = noUrl(getComputedStyle(document.body).getPropertyValue(name).trim());
      if (!raw) raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
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

// Bins:
//   token    a var the class table maps to a named Panda token (or one declared
//            in the :where(:root,:host) scale block)
//   theme    colour vars declared inside a theme scope ([data-theme=*])
//   app      other component/app vars (--color-var aliases, per-component vars)
//   vendor   widget/framework vars (recaptcha, stripe, intercom, map libs)
//   utility  a one-off [--x:value] arbitrary-property class
const VENDOR = /recaptcha|grecaptcha|stripe|intercom|mapbox|maplibre|swiper|sonner|--toast-|video-js|vjs-|sentry/i;
const SCALE_SCOPE = /^:where\(:root,:host\)$/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.some((n) => tokenMap[n])) return 'token';
  if (SCALE_SCOPE.test((r.selector || '').trim())) return 'token';
  if (/\[data-theme=/.test(r.selector || '')) return 'theme';
  return 'app';
};
const ok = result.rules;
for (const r of ok) r.bin = binOf(r);
const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ${r.file.split(' ')[0]} ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during live signed-out loads of www.fresha.com / (consumer), /for-business (B2B marketing app), partners.fresha.com sign-in and /lp/en/bt/hair-salons/in/singapore, re-parsed with CSSStyleSheet; resolved in probes carrying each surface\'s real sheets at 1440 x 900. `dark` and `accent` are data-theme probes: the partner sign-in sets data-theme="auto" and paints the dark values under prefers-color-scheme: dark (screenshots/partner-signin-dark-*.png); on the consumer and B2B signed-out routes nothing sets data-theme, so their dark and accent declarations are declared-but-unpainted (see `live`).',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  live,
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length },
    bySelector,
  },
  errors: result.errors,
  tokenMap,
  token: ok.filter((r) => r.bin === 'token'),
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  fonts: result.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${ok.length} rules, ${result.fonts.length} font faces; names token ${out.counts.names.token}, theme ${out.counts.names.theme}, app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, utility ${out.counts.names.utility}`);
console.log(`tokenMap: ${Object.keys(tokenMap).length} vars mapped to token names`);
console.log(`resolved: ${Object.entries(resolved).map(([k, v]) => k + ' ' + Object.keys(v).length).join(', ')}`);
for (const [k, v] of Object.entries(live)) console.log(`live ${k}:`, JSON.stringify({ title: v && v.title, colorScheme: v && v.colorScheme, themed: v && v.themedElements && v.themedElements.length, darkRules: v && v.prefersDarkRules }));
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 25)) console.log(`  ${v}\t${k.slice(0, 150)}`);
