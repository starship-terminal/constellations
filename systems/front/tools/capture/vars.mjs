// Reads the custom properties and the class-declared design layer front.com's
// public surfaces ship, and writes raw/css-vars.json + raw/css-classes.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// Front paints four public surfaces signed out:
//
//   front.com         the Next.js + Tailwind marketing site. Its stylesheets
//                     declare almost no custom properties (only --tw-*
//                     internals plus --logo-size-modifier/--loading/--award-
//                     height); the design layer is compiled into bespoke
//                     classes: the hue ramps (.bg-violet-50..1000,
//                     .bg-citron-*, .bg-blue-*, .bg-gray-*, .text-*, .border-*),
//                     the semantic surface scale (.surface-l0..l3,
//                     .surface-highlight, .surface-outer), text roles
//                     (.text-primary/.text-secondary), the type ramp
//                     (.text-display1/.text-h1..h4/.text-p1/.text-p2/
//                     .text-caption*/.text-micro* plus .font-size-*/,
//                     .font-line-height-*/.font-letter-spacing-* companions),
//                     the button layer (.button-primary-*/.button-secondary-*/
//                     .button-size-* and the .button-surface/.button-border/
//                     .button-text states) — each redeclared under the page's
//                     three section themes [data-theme=theme-dark-violet]
//                     (the plum default), [data-theme=theme-white] and
//                     [data-theme=theme-gray].
//   app.frontapp.com  the product SPA's auth shell (/signin): a real token
//                     layer — an injected inline sheet plus button.*.css
//                     declare 332 --color-* custom properties on :root
//                     (--color-primitive-<hue>-* ramps, --color-bg-*/
//                     --color-text-*/--color-icon-*/--color-border-*/
//                     --color-input-*/--color-accent-* semantics), and
//                     [data-theme=dark] redeclares 154 of them; the theme
//                     comes from front-theme-preference localStorage, falling
//                     back to prefers-color-scheme.
//   help.front.com    Front's own Knowledge Base product serving the help
//                     centre: an inline :root block of --primary-color,
//                     --secondary-color, --gray-shade*, --article-*, button
//                     and field vars.
//   dev.frontapp.com  the developer portal on ReadMe (readme.io): vendor
//                     platform sheets plus a --color-* override layer.
//
// The marketing/app/help sheets are read two ways: external bodies from
// network responses, and the live document's CSSOM (which also sees the
// app's injected inline sheet). Every rule declaring a --* property is kept
// with its selector, host and enclosing @media/@layer context; every rule in
// the marketing bespoke layer (the class list in BESPOKE) is kept verbatim
// into css-classes.json. @font-face rules are kept too.
//
// Resolution: app names are resolved on the live signin page under
// data-theme=light and =dark (the page's own switch, restored afterwards);
// help names on the live help home; dev names on the live docs page.
// Marketing has no custom-property layer to resolve — its declared class
// values are literal rgb()/hex already.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, HELP, DEV, UA, launch, patch, closePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser } = await launch();

// Load each host's entry route once, collecting stylesheet bodies from
// network responses and the CSSOM (href-less sheets and the app's injected
// inline rules alike). `sheets` holds [label, cssText] rows labelled by host.
const HOSTS = [
  ['marketing', BASE + '/'],
  ['app', APP + '/signin'],
  ['help', HELP + '/'],
  ['dev', DEV + '/docs/welcome'],
];
const sheets = [];
let appPage = null, appCtx = null;
for (const [host, url] of HOSTS) {
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const p = await context.newPage();
  const bodies = new Map();
  p.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await p.waitForTimeout(host === 'app' ? 12000 : 8000);
  await closePromo(p).catch(() => {});
  for (const [u, css] of bodies) sheets.push([host + ' ' + u.replace(/^https?:\/\//, ''), css]);
  // The CSSOM also sees constructed and cross-fetched sheets we cannot read
  // here; take every readable rule of every href-less sheet, and record the
  // linked-sheet URLs we already have bodies for under the same label.
  const inline = await p.evaluate(() => [...document.styleSheets].map((s, i) => {
    try { return [s.href || 'inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
  }).filter(Boolean));
  for (const [u, css] of inline) if (u.startsWith('inline-') || !bodies.has(u.split('?')[0])) sheets.push([host + ' ' + u, css]);
  if (host === 'app') { appPage = p; appCtx = context; continue; }
  if (host === 'dev') { globalThis.__devPage = p; globalThis.__devCtx = context; continue; }
  if (host === 'help') { globalThis.__helpPage = p; globalThis.__helpCtx = context; continue; }
  await context.close();
}

// ---- harvest: every rule with --* declarations, and the marketing bespoke
// class layer verbatim ----
const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const classes = [];
  // The marketing site's design layer, compiled to classes. A rule whose
  // selector list is only bespoke names (under any theme scope) is kept whole.
  const BESPOKE = /^(\.surface-[a-z0-9-]+|\.text-(display[0-9]|h[1-4]|p[12]|caption[12]|micro[123]|primary|secondary)|\.font-(size|line-height|letter-spacing|weight)-[a-z0-9-]+|\.button(-[a-z0-9-]+)+|\.rounded-[0-9]+|\.ease-[a-z-]+|\.duration-[0-9]+|\.link-cover|\.hover-arrow[a-z-]*|\[data-theme=[^\]]+\]\s*)+/i;
  const PALETTE = /^\.(bg|text|border|from|via|to|ring|outline|fill|stroke|divide|placeholder|caret|accent|decoration|shadow)-[a-z]+-\d+/i;
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
      const sel = (r.selectorText || '').slice(0, 220);
      if (n) rules.push({ file, selector: sel, context: ctx, properties: props });
      // The marketing bespoke layer and palette utilities, kept verbatim.
      if (file.startsWith('marketing')) {
        const core = sel.split(',').map((s) => s.trim()).find((s) => BESPOKE.test(s) || PALETTE.test(s));
        if (core) {
          const decl = {};
          for (let i = 0; i < r.style.length; i++) { const k = r.style[i]; if (!k.startsWith('--')) decl[k] = noUrl(r.style.getPropertyValue(k).trim()); }
          classes.push({ file, selector: sel, context: ctx, declarations: decl });
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
  return { rules, fonts, errors, classes };
}, sheets);

// ---- resolution on the live surfaces ----
// Only resolve names each host declares: keep the harvest honest per surface.
const hostNames = (host) => [...new Set(result.rules.filter((r) => r.file.startsWith(host)).flatMap((r) => Object.keys(r.properties)))].filter((n) => !/^--(tw-|_)/.test(n)).sort();

const resolved = {};
// app, both themes, on the live page.
{
  const want = hostNames('app');
  for (const [pass, theme] of [['app', 'light'], ['appDark', 'dark']]) {
    resolved[pass] = await appPage.evaluate(([want, theme]) => {
      // A resolved custom property can hold a url() with a signed or per-account query:
      // record it as url(…); data: and #fragment references keep their full value.
      const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
      const html = document.documentElement;
      const saved = html.getAttribute('data-theme');
      html.setAttribute('data-theme', theme);
      const cs = getComputedStyle(html);
      const o = {};
      // Values stay whole: a mid-string cut would publish unclosed url()/string CSS.
      for (const n of want) { const v = noUrl(cs.getPropertyValue(n).trim()); if (v) o[n] = { raw: v, value: v }; }
      saved === null ? html.removeAttribute('data-theme') : html.setAttribute('data-theme', saved);
      return o;
    }, [want, theme]);
  }
  await appCtx.close();
}
// help, single theme, on the live page.
{
  const want = hostNames('help');
  resolved.help = await __helpPage.evaluate((want) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const cs = getComputedStyle(document.documentElement);
    const o = {};
    for (const n of want) { const v = noUrl(cs.getPropertyValue(n).trim()); if (v) o[n] = { raw: v, value: v }; }
    return o;
  }, want);
  await __helpCtx.close();
}
// dev (ReadMe vendor vars), single theme.
{
  const want = hostNames('dev');
  resolved.dev = await __devPage.evaluate((want) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const cs = getComputedStyle(document.documentElement);
    const o = {};
    for (const n of want) { const v = noUrl(cs.getPropertyValue(n).trim()); if (v) o[n] = { raw: v, value: v }; }
    return o;
  }, want);
  await __devCtx.close();
}
await probe.close();
await browser.close();

// ---- binning ----
const THEME_NAME = /^--(color|font|text|radius|shadow|spacing|size|ease|duration|border|z|breakpoint|opacity|leading|tracking|article|primary|secondary|tertiary|gray|grey|blue|green|orange|red|yellow|violet|purple|citron|pink|salmon|neutral|white|black|header|input|table|hr|blockquote|search|checkmark|chevron|link|hover|box-shadow|page|font)/;
const VENDOR_HOST = /readme|cdn\.readme|intercom|hubspot|qualified|onetrust|wistia|cloudfront/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (VENDOR_HOST.test(r.file)) return 'vendor';
  if (names.some((n) => THEME_NAME.test(n))) return 'theme';
  return 'app';
};
const ok = result.rules.filter((r) => !r.error);
for (const r of ok) r.bin = binOf(r);

const bySelector = {};
for (const r of ok) {
  const key = `[${r.bin}] ` + (r.context.length ? r.context.join(' ') + ' ' : '') + r.selector;
  bySelector[key] = (bySelector[key] || 0) + Object.keys(r.properties).length;
}
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();

fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify({
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "front.com's four public surfaces: the marketing site's _next CSS chunks (network responses) and inline blocks, app.frontapp.com's signin sheets incl. the injected inline token layer, help.front.com's inline :root block, and dev.frontapp.com's ReadMe sheets (all read live, same-origin CSSOM)",
  sheets: sheets.map(([name, css]) => ({ name, bytes: css.length })),
  counts: {
    rules: ok.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, vendor: names('vendor').length, utility: names('utility').length, tailwind: names('tailwind').length },
    bySelector,
  },
  errors: result.rules.filter((r) => r.error).concat(result.errors),
  theme: ok.filter((r) => r.bin === 'theme'),
  app: ok.filter((r) => r.bin === 'app'),
  vendor: ok.filter((r) => r.bin === 'vendor'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: result.fonts,
  resolved,
}, null, 1) + '\n');
fs.writeFileSync(path.join(REF, 'raw', 'css-classes.json'), JSON.stringify({
  readAt: new Date().toLocaleDateString('en-CA'),
  source: "front.com's compiled design layer: the bespoke semantic classes (surface-*, text-*, font-*, button-*, rounded-*, ease-*, duration-*) and the Tailwind colour-utility palette, verbatim from the _next CSS chunks, keyed by [data-theme] context",
  rules: result.classes,
}, null, 1) + '\n');

console.log(`css-vars.json: ${ok.length} var rules, ${result.fonts.length} font faces; names theme ${names('theme').length}, app ${names('app').length}, vendor ${names('vendor').length}, tailwind ${names('tailwind').length}`);
console.log(`resolved: app ${Object.keys(resolved.app || {}).length}, appDark ${Object.keys(resolved.appDark || {}).length}, help ${Object.keys(resolved.help || {}).length}, dev ${Object.keys(resolved.dev || {}).length}`);
console.log(`css-classes.json: ${result.classes.length} bespoke/palette rules`);
for (const [k, v] of Object.entries(bySelector).sort((a, b) => b[1] - a[1]).slice(0, 30)) console.log(`  ${v}\t${k.slice(0, 160)}`);
