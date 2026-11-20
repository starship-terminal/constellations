// Reads every custom property hitchd.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// hitchd.com serves three surfaces, harvested from live signed-out loads:
//   marketing   /, /blog/<post>, /terms, /trips/<dest>, /guides/<guide> —
//               static pages on marketing/css/{foundation,styles}.min.css
//   couple app  /login, /signup, /forgot-password — an Angular SPA whose
//               styles arrive in couple_*.bundle.js and mount as <style>
//   guest app   /zoeandnoah — the public demo registry, an Angular SPA on
//               *.bundle.js plus cdn.jsdelivr.net/foundation/5.3.3
//
// Linked sheets are read from network responses, the apps' injected <style>
// blocks through the CSSOM, then re-parsed in the page with a constructed
// CSSStyleSheet — the same parse the browser does. Every rule declaring a
// --* property is kept with its selector and enclosing @media/@layer
// context, and @font-face rules are kept too. The site declares almost no
// custom properties (three --*-in-* breakpoint toggles in the marketing
// sheet, a few --display flags in the guest app) — the harvest records them
// and the @font-face inventory, and the token layer is built from measured
// computed styles instead (build_component_tokens.py).
//
// Each name is resolved in a probe document that carries the real sheets —
// there is one theme (no dark variant or theme control exists), so a single
// light pass applies each name to a real typed property the way a component
// consumes it, at 1440 x 900.
//
// Bins:
//   app       names the product's own sheets declare
//   vendor    third-party widget vars (reCAPTCHA, StackAdapt, Intercom)
//   utility   a one-off `[--x:value]` arbitrary-property utility class
//   framework Foundation grid internals
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, patch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();
const bodies = new Map();   // url -> stylesheet body (linked sheets)
const inline = new Map();   // 'inline:<page>:<i>' -> css text (apps' <style> blocks)
let htmlClass = '', bodyClass = '';

const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await patch(context);
const p = await context.newPage();
p.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
});
for (const [key, path_] of [['home', '/'], ['login', '/login'], ['registry', '/zoeandnoah'], ['blog-post', '/blog/what-is-a-honeymoon-registry'], ['trips', '/trips/australia']]) {
  await p.goto(process.env.VARS_URL || BASE + path_, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(7000);
  const [inlines, bc, hc] = await p.evaluate(() => [
    [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean),
    document.body.className,
    document.documentElement.className,
  ]).catch(() => [[], '', '']);
  for (const [n, css] of inlines) if (css && css.length > 200) inline.set(key + ':' + n, css);
  if (path_ === '/') { bodyClass = bc; htmlClass = hc; }
}
await context.close();

// ---- harvest: every rule with --* declarations, plus @font-face ----
const sheets = [...bodies.entries()].concat([...inline.entries()]);
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
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

// ---- resolution: probe document with the real sheets, one light pass ----
const escAttr = (s) => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
const shell = '<!doctype html><html class="' + escAttr(htmlClass) + '"><head>'
  + sheets.map(([n, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body class="' + escAttr(bodyClass) + '"><div id="probe-root"></div></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !/^--(tw-|_)/.test(n)).sort();
await probe.setContent(shell, { waitUntil: 'load' });
const resolved = await probe.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const readEl = document.getElementById('probe-root');
  const box = document.createElement('div');
  box.style.cssText = 'position:absolute;left:0;top:0;width:1000px;height:1000px;visibility:hidden';
  const p = document.createElement('div');
  box.appendChild(p);
  document.body.appendChild(box);
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(readEl).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    p.removeAttribute('style');
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (/currentcolor/i.test(raw)) { r.kind = 'other'; r.note = 'depends on currentColor'; }
    else if (CSS.supports('color', raw)) { p.style.color = raw; r.kind = 'color'; r.value = getComputedStyle(p).color; }
    else if (!raw.includes('%') && CSS.supports('width', raw)) {
      if (/(em|ex|ch|cap|ic|lh|rlh)$/.test(raw)) { r.kind = 'other'; r.note = 'font-relative length; resolves per element'; }
      else { p.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(p).width; if (/vw|vh|dvh/.test(raw)) r.note = 'viewport-relative, resolved at 1440 x 900'; }
    }
    else if (CSS.supports('box-shadow', raw)) { p.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(p).boxShadow; }
    else if (CSS.supports('transition-duration', raw)) { p.style.transitionDuration = raw; r.kind = 'duration'; r.value = getComputedStyle(p).transitionDuration; }
    else if (CSS.supports('transition-timing-function', raw)) { r.kind = 'easing'; r.value = raw; }
    else if (/[A-Za-z]/.test(raw) && CSS.supports('font-family', raw)) { r.kind = 'fontFamily'; r.value = raw; }
    else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, want);
await browser.close();

const VENDOR = /recaptcha|grecaptcha|stackadapt|intercom|stripe|gtm|googletagmanager|--gigya|--hs-|cookiebot/i;
// Vendor vars that carry an identifier rather than a style (StackAdapt's
// --sa-uid is a base64 visitor id): record that the name exists, never its
// value — a design package has no use for a tracker token and a copy of it
// is a needless identifier leak.
const IDENT = /uid|uuid|token|secret|api[-_]?key|session|visitor/i;
const maskIdents = (rules) => rules.map((r) => ({
  ...r,
  properties: Object.fromEntries(Object.entries(r.properties).map(([k, v]) => [k, IDENT.test(k) ? '<identifier omitted>' : v])),
}));
const FRAMEWORK = /^--(desktop|mobile|tablet)-in-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (VENDOR.test(r.file || '') || VENDOR.test(r.selector || '') || names.every((n) => VENDOR.test(n))) return 'vendor';
  if (names.every((n) => FRAMEWORK.test(n))) return 'framework';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const bySelector = {};
for (const r of result.rules) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'the stylesheet bodies read during live signed-out loads of hitchd.com /, /login, /zoeandnoah, /blog/what-is-a-honeymoon-registry and /trips/australia — the linked marketing/css/*.min.css and cdn.jsdelivr.net Foundation sheets from network responses plus the Angular apps\' injected <style> blocks through the CSSOM, re-parsed with CSSStyleSheet; resolved in a probe carrying the real sheets and the live home page\'s html/body classes in the single light theme (no dark variant or theme control exists), each name applied to a real typed property at 1440 x 900',
  sheets: sheets.map(([n, t]) => `${n} (${t.length} bytes)`),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { app: names('app').length, vendor: names('vendor').length, framework: names('framework').length, utility: names('utility').length },
    bySelector,
  },
  errors: result.errors,
  app: maskIdents(result.rules.filter((r) => r.bin === 'app')),
  vendor: maskIdents(result.rules.filter((r) => r.bin === 'vendor')),
  framework: maskIdents(result.rules.filter((r) => r.bin === 'framework')),
  utility: maskIdents(result.rules.filter((r) => r.bin === 'utility')),
  fonts: result.fonts,
  resolved: { light: Object.fromEntries(Object.entries(resolved).map(([k, r]) => [k, IDENT.test(k) ? { kind: r.kind, value: '<identifier omitted>' } : r])) },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${out.counts.rules} rules, ${result.fonts.length} font faces; names app ${out.counts.names.app}, vendor ${out.counts.names.vendor}, framework ${out.counts.names.framework}, utility ${out.counts.names.utility}`);
console.log(`resolved light: ${Object.keys(resolved).length}`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 20)) console.log(`  ${v}\t${k.slice(0, 150)}`);
