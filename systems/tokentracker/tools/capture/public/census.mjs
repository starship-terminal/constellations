// Counts what TokenTracker's dashboard actually renders, page by page, in dark and light:
// every computed colour (text, fill, border), shadow, z-index layer, padding, gap, radius and
// font size on a visible element, with how many elements use it and a sample of where. Also
// reads the stylesheet's breakpoints, reduced-motion rules and the Tailwind colour utilities the
// bundle ships, so ramps, spacing, elevation and layering are read from use rather than guessed.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node census.mjs
//
// Writes raw/census.json (raw/census.partial.json, gitignored, when a page failed). Read-only: pages are loaded and nothing is clicked. mask() runs first,
// so the element samples never hold a path, session title or skill name.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, RAW, blocked } from './lib.mjs';

const PAGES = {
  dashboard: '/dashboard', sessions: '/sessions', limits: '/limits', skills: '/skills', settings: '/settings',
  widgets: '/widgets', achievements: '/achievements', pet: '/pet-settings', 'service-status': '/service-status', cloud: '/cloud',
};
const out = { _meta: {}, totals: {}, sheet: {}, pages: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const failures = [];

function add(bucket, key, where) {
  const b = (bucket[key] ??= { n: 0, where: [] });
  b.n++;
  if (b.where.length < 4 && !b.where.includes(where)) b.where.push(where);
}

const COLOUR_UTIL = /^\.(?:dark\\:)?(text|bg|border|ring|fill|stroke|from|to|via|outline|shadow)-(red|amber|orange|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|slate|gray|zinc|neutral|stone|oai-brand|oai-gray)-(\d{2,3})(?:\\\/(\d+))?(?::is\(\.dark \*\))?$/.source;

for (const theme of ['dark', 'light']) {
  const { browser, context } = await launch({ theme });
  for (const [name, url] of Object.entries(PAGES)) {
    const page = await context.newPage();
    try {
      await open(page, BASE + url, { wait: name === 'service-status' ? 8000 : 4000 });
      const r = await page.evaluate(() => {
        const desc = (e) => {
          const cls = [...e.classList].filter((c) => !c.includes(':')).slice(0, 3).join('.');
          const role = e.getAttribute('role');
          return `${e.tagName.toLowerCase()}${role ? `[role=${role}]` : ''}${cls ? '.' + cls : ''}`.slice(0, 90);
        };
        const rows = [];
        for (const e of document.querySelectorAll('body *')) {
          if (e.closest('svg') && e.tagName.toLowerCase() !== 'svg') continue;
          const rect = e.getBoundingClientRect();
          if (rect.width < 1 || rect.height < 1) continue;
          const c = getComputedStyle(e);
          if (c.visibility === 'hidden' || c.display === 'none' || parseFloat(c.opacity) === 0) continue;
          const own = [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
          const bw = parseFloat(c.borderTopWidth) > 0 && c.borderTopStyle !== 'none' ? c.borderTopColor
            : parseFloat(c.borderBottomWidth) > 0 && c.borderBottomStyle !== 'none' ? c.borderBottomColor : null;
          rows.push({
            d: desc(e), text: own ? c.color : null, fill: c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : null, border: bw,
            shadow: c.boxShadow !== 'none' ? c.boxShadow : null,
            z: c.position !== 'static' && c.zIndex !== 'auto' ? `${c.zIndex} ${c.position}` : null,
            pad: [c.paddingTop, c.paddingRight, c.paddingBottom, c.paddingLeft],
            gap: c.display.includes('flex') || c.display.includes('grid') ? (c.rowGap === c.columnGap ? [c.rowGap] : [c.rowGap, c.columnGap]) : [],
            radius: c.borderTopLeftRadius, size: own ? `${c.fontSize}/${c.lineHeight} ${c.fontWeight}` : null, family: own ? c.fontFamily : null,
          });
        }
        return rows;
      });
      const P = { text: {}, fill: {}, border: {}, shadow: {}, z: {}, space: {}, radius: {}, type: {}, family: {} };
      for (const x of r) {
        if (x.text) add(P.text, x.text, x.d);
        if (x.fill) add(P.fill, x.fill, x.d);
        if (x.border) add(P.border, x.border, x.d);
        if (x.shadow) add(P.shadow, x.shadow, x.d);
        if (x.z) add(P.z, x.z, x.d);
        for (const v of [...x.pad, ...x.gap]) if (v !== '0px' && v !== 'normal') add(P.space, v, x.d);
        if (x.radius !== '0px') add(P.radius, x.radius, x.d);
        if (x.size) add(P.type, x.size, x.d);
        if (x.family) add(P.family, x.family, x.d);
      }
      out.pages[`${name}.${theme}`] = P;
      log(name, theme, r.length, 'elements');
    } catch (e) {
      failures.push(`${name} ${theme}: ${String(e.message).split('\n')[0]}`);
      log('  ! failed', name, theme, String(e.message).split('\n')[0]);
    }
    await page.close();
  }
  if (theme === 'dark') {
    // The stylesheet once: breakpoints, reduced-motion rules and the colour utilities it ships.
    const page = await context.newPage();
    try {
      await open(page, BASE + '/dashboard');
      out.sheet = await page.evaluate((src) => {
        const re = new RegExp(src);
        const media = {}, reduced = [], utilities = {};
        const walk = (rules, cond) => {
          for (const r of rules) {
            if (r.media) {
              const m = r.media.mediaText;
              media[m] = (media[m] || 0) + r.cssRules.length;
              if (/prefers-reduced-motion/.test(m)) for (const x of r.cssRules) reduced.push({ media: m, rule: x.cssText.slice(0, 240) });
              walk(r.cssRules, m);
              continue;
            }
            if (r.cssRules && !r.selectorText) { walk(r.cssRules, cond); continue; }
            if (!r.selectorText || cond) continue;
            if (/motion-reduce|motion-safe/.test(r.selectorText)) reduced.push({ media: 'class', rule: r.cssText.slice(0, 240) });
            const m = r.selectorText.match(re);
            if (!m) continue;
            const st = r.style;
            const v = ['color', 'background-color', 'border-color', '--tw-ring-color', '--tw-gradient-from', '--tw-gradient-to', 'fill', 'stroke', 'outline-color', '--tw-shadow-color']
              .map((p) => st.getPropertyValue(p)).find((x) => x) || '';
            const rgb = v.match(/rgb\((\d+) (\d+) (\d+)/) || v.match(/#([0-9a-f]{6})/i);
            if (!rgb) continue;
            const hex = rgb.length === 4 ? '#' + rgb.slice(1).map((n) => (+n).toString(16).padStart(2, '0')).join('') : '#' + rgb[1].toLowerCase();
            const u = (utilities[m[2]] ??= {});
            const s = (u[m[3]] ??= { value: hex, uses: [] });
            const use = m[1] + (m[4] ? `/${m[4]}` : '');
            if (!s.uses.includes(use)) s.uses.push(use);
          }
        };
        for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
        for (const u of Object.values(utilities)) for (const s of Object.values(u)) s.uses.sort();
        return { media, reduced, utilities };
      }, COLOUR_UTIL);
    } catch (e) {
      failures.push(`stylesheet: ${String(e.message).split('\n')[0]}`);
    }
    await page.close();
  }
  await browser.close();
}

// Totals across every page, per theme, most used first.
for (const [key, P] of Object.entries(out.pages)) {
  const theme = key.split('.').pop();
  const T = (out.totals[theme] ??= {});
  for (const [k, bucket] of Object.entries(P)) {
    const tb = (T[k] ??= {});
    for (const [v, b] of Object.entries(bucket)) {
      const x = (tb[v] ??= { n: 0, pages: [], where: [] });
      x.n += b.n;
      x.pages.push(key.split('.')[0]);
      for (const w of b.where) if (x.where.length < 6 && !x.where.includes(w)) x.where.push(w);
    }
  }
}
for (const T of Object.values(out.totals)) for (const [k, tb] of Object.entries(T)) T[k] = Object.fromEntries(Object.entries(tb).sort((a, b) => b[1].n - a[1].n || (a[0] < b[0] ? -1 : 1)));
out._meta = {
  read: new Date().toLocaleDateString('en-CA'),
  source: 'TokenTracker v1.4.3 dashboard served by the local CLI at 127.0.0.1:7680, every visible element on each page at 1440x900, headless Chromium',
  pages: Object.keys(PAGES), failures, blockedRequests: [...new Set(blocked)].sort(),
};
// A run with a failed page writes census.partial.json (gitignored) and leaves the last full census as it was.
const file = path.join(RAW, failures.length ? 'census.partial.json' : 'census.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
log('census ->', file, failures.length ? `(${failures.length} failed: ${failures.join('; ')})` : '');
if (failures.length) process.exit(1);
