// Read Linear's CSS variables, media queries, z-index, motion and font faces from the page copies
// and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/vars.mjs
//
// Linear (adapted from the kit's vars.mjs). Two kinds of variable matter:
//   theme   every custom property once the theme is applied, read with getComputedStyle on <main>
//           in one dark copy and one light copy (`issue-dark`, `issue-light`). Linear applies the
//           theme on .theme-provider-<hash> wrappers; :root holds only dark fallbacks, kept apart
//           as rootDefaults.
//           The theme is a script-generated constructed stylesheet that snapshot.js inlined as
//           <style data-adopted>; most of its names are stylex hashes (--sx-1yxqotz), the rest are
//           Linear's own (--color-bg-primary, --focus-ring-color, --speed-quickTransition).
//   aliases rules in the static bundle that give a hashed variable a readable name, such as
//           `:root, .sx-10sn7k { --focus-ring-color: var(--sx-ch85qk) }`. They are how a hash is
//           tied to a role without guessing.
// Two readings come from specific copies: the colour each workflow status icon is drawn in (the
// status menu, `issue-<theme>-menu`), and the z-index stack under each overlay (menu, tooltip,
// toast, dialog), walking up from the overlay to the root.
// The stylesheets are also parsed for @media conditions, z-index, transition and animation values,
// box-shadows and @font-face rules, each with the number of rules that use it. No network: copies
// are read from disk.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const SNAPS = process.env.SNAPS;
if (!SNAPS) { console.error('SNAPS=<dir of page copies> is required'); process.exit(2); }
const COPIES = { dark: 'issue-dark', light: 'issue-light' };

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch();

const out = {
  _meta: {
    read: new Date().toLocaleDateString('en-CA'),   // the date of this run (YYYY-MM-DD), not a fixed one
    source: 'Static redacted copies of the signed-in linear.app web app; theme values are getComputedStyle on <main> (inside the theme provider) in the dark copy (issue-dark) and the light copy (issue-light); everything else is parsed from the inlined stylesheets. Nothing was fetched.',
    copies: COPIES,
  },
  theme: {},
  aliases: {},
  media: {},
  zIndex: {},
  transitions: {},
  durations: {},
  easings: {},
  shadows: {},
  fontFaces: [],
  meta: {},
  statusColors: {},
  layers: {},
};

// The z-index of every positioned ancestor of an overlay, innermost first.
const LAYERS = {
  menu: ['issue-THEME-menu', () => document.querySelector('[role=listbox]')],
  tooltip: ['issue-THEME-tooltip', () => [...document.body.children].filter((c) => /Copy issue URL/.test(c.textContent)).pop()],
  toast: ['issue-THEME-toast', () => document.querySelector('[data-sonner-toast]')],
  dialog: ['composer-THEME', () => document.querySelector('[role=dialog]')],
};
async function openCopy(label) {
  const page = await browser.newPage();
  await page.route('**/*', (r) => (/^(file|data):/.test(r.request().url()) ? r.continue() : r.abort()));
  await page.goto(`file://${path.join(SNAPS, label)}.html`, { waitUntil: 'load' });
  return page;
}
for (const theme of Object.keys(COPIES)) {
  const page = await openCopy(`issue-${theme}-menu`);
  out.statusColors[theme] = await page.evaluate(() => Object.fromEntries([...document.querySelectorAll('[role=listbox] [role=option]')].map((o) => {
    const paints = [...o.querySelectorAll('svg, svg *')].flatMap((n) => { const c = getComputedStyle(n); return [n.getAttribute('stroke') && n.getAttribute('stroke') !== 'none' ? c.stroke : null, n.getAttribute('fill') && !/^(none|currentColor)$/i.test(n.getAttribute('fill')) ? c.fill : null]; }).filter(Boolean);
    return [o.textContent.replace(/\d+$/, '').trim(), paints[0] || getComputedStyle(o.querySelector('svg') || o).color];
  })));
  await page.close();
  out.layers[theme] = {};
  for (const [name, [tpl, find]] of Object.entries(LAYERS)) {
    const p = await openCopy(tpl.replace('THEME', theme));
    out.layers[theme][name] = await p.evaluate((src) => {
      const el = (0, eval)(`(${src})`)();
      const chain = [];
      for (let n = el; n && n !== document.documentElement; n = n.parentElement) { const z = getComputedStyle(n).zIndex; if (z !== 'auto') chain.push(+z); }
      return chain;
    }, find.toString());
    await p.close();
  }
}

for (const [theme, label] of Object.entries(COPIES)) {
  const page = await browser.newPage();
  await page.route('**/*', (r) => (/^(file|data):/.test(r.request().url()) ? r.continue() : r.abort()));
  await page.goto(`file://${path.join(SNAPS, label)}.html`, { waitUntil: 'load' });
  const res = await page.evaluate(() => {
    // A custom property can hold a url() with a signed or per-account query: record it as url(…).
    // Its value keeps the authored tokens, so this matches URL( too, escapes and space inside the parens.
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const names = new Set();
    const aliases = {};
    const media = {}, zIndex = {}, transitions = {}, durations = {}, easings = {}, shadows = {};
    const fontFaces = [];
    const bump = (o, k) => { if (k) o[k] = (o[k] || 0) + 1; };
    const walk = (rules) => {
      for (const r of rules) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fontFaces.push({ family: r.style.getPropertyValue('font-family').trim(), weight: r.style.getPropertyValue('font-weight').trim(), style: r.style.getPropertyValue('font-style').trim(), display: r.style.getPropertyValue('font-display').trim() });
          continue;
        }
        if (r.type === CSSRule.MEDIA_RULE) { bump(media, r.media.mediaText); walk(r.cssRules); continue; }
        if (r.cssRules && !r.style) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          const v = noUrl(r.style.getPropertyValue(k).trim());
          if (k.startsWith('--')) {
            names.add(k);
            const m = v.match(/^var\((--sx-[\w-]+)\)$/);
            if (m && !k.startsWith('--sx-') && !k.startsWith('--x-')) { aliases[k] ||= {}; aliases[k][m[1]] = (aliases[k][m[1]] || 0) + 1; }
          }
          if (k === 'z-index') bump(zIndex, v);
          if (k === 'transition-duration' || k === 'animation-duration') v.split(',').forEach((d) => bump(durations, d.trim()));
          if (k === 'transition-timing-function' || k === 'animation-timing-function') v.split(/,(?![^(]*\))/).forEach((d) => bump(easings, d.trim()));
          if (k === 'transition') bump(transitions, v);
          if (k === 'box-shadow' && v !== 'none') bump(shadows, v);
        }
        if (r.cssRules && r.cssRules.length) walk(r.cssRules);
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* none are cross-origin in a copy */ } }
    // The applied theme lives on Linear's .theme-provider-<hash> wrappers (the app root and each
    // portal); :root only carries the dark defaults the stylex bundle ships. So values are read on
    // <main>, inside the app's theme provider, and :root's are kept apart as rootDefaults.
    const root = getComputedStyle(document.documentElement);
    const app = getComputedStyle(document.querySelector('main') || document.body);
    const theme = {}, rootDefaults = {};
    for (const n of [...names].sort()) {
      const v = noUrl(app.getPropertyValue(n).trim());
      if (v) theme[n] = v;
      const d = noUrl(root.getPropertyValue(n).trim());
      if (d && d !== v) rootDefaults[n] = d;
    }
    const provider = (document.querySelector('main') || document.body).closest('[class*=theme-provider]');
    const meta = {};
    // A link href can carry a signed or per-account query: record origin and path only.
    const hrefPath = (h) => { try { const u = new URL(h, location.href); return u.origin + u.pathname; } catch { return null; } };
    document.querySelectorAll('meta[name=theme-color], link[rel=mask-icon], link[rel=manifest], meta[name=color-scheme]').forEach((m) => { meta[(m.getAttribute('name') || m.getAttribute('rel')) + (m.getAttribute('media') ? ` (${m.getAttribute('media')})` : '')] = m.getAttribute('content') || m.getAttribute('color') || hrefPath(m.getAttribute('href')); });
    return { theme, rootDefaults, provider: provider ? 'theme-provider' : null, aliases, media, zIndex, transitions, durations, easings, shadows, fontFaces, meta, htmlClass: document.documentElement.className };
  });
  out.theme[theme] = res.theme;
  (out.rootDefaults ||= {})[theme] = res.rootDefaults;
  out._meta[`read-on-${theme}`] = res.provider ? '<main>, inside a .theme-provider-<hash> wrapper' : '<main>';
  out.meta[theme] = { ...res.meta, htmlClass: res.htmlClass };
  if (theme === 'dark') Object.assign(out, { aliases: res.aliases, media: res.media, zIndex: res.zIndex, transitions: res.transitions, durations: res.durations, easings: res.easings, shadows: res.shadows, fontFaces: res.fontFaces });
  await page.close();
}
await browser.close();

const sortObj = (o) => Object.fromEntries(Object.entries(o).sort((a, b) => b[1] - a[1] || String(a[0]).localeCompare(String(b[0]))));
for (const k of ['media', 'zIndex', 'transitions', 'durations', 'easings', 'shadows']) out[k] = sortObj(out[k]);
const seen = new Set();
out.fontFaces = out.fontFaces.filter((f) => { const k = JSON.stringify(f); if (seen.has(k)) return false; seen.add(k); return true; });
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`theme vars: dark ${Object.keys(out.theme.dark).length}, light ${Object.keys(out.theme.light).length}; aliases ${Object.keys(out.aliases).length}; media ${Object.keys(out.media).length}; z-index ${Object.keys(out.zIndex).length}; font faces ${out.fontFaces.length}`);
