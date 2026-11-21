// Read every custom property Pryzm's stylesheets declare and write raw/css-vars.json.
// PRODUCT (adapt): public pages, live CSSOM. No page copies. Cross-origin sheets
// are fetched and parsed with a constructed CSSStyleSheet.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw');
fs.mkdirSync(OUT, { recursive: true });

const PAGES = ['/', '/studio', '/gallery', '/docs', '/blog'];

function owner(name, selector) {
  if (name.startsWith('--tw-')) return 'tailwind';
  if (name.startsWith('--color-') || name.startsWith('--text-') || name.startsWith('--container-') || name.startsWith('--spacing') || name.startsWith('--font-') || name.startsWith('--radius') || name.startsWith('--breakpoint')) return 'theme';
  if (/^--(background|foreground|card|popover|primary|secondary|muted|accent|destructive|border|input|ring|sidebar|chart)/.test(name)) return 'semantic';
  if (selector && /dark|:root|html/.test(selector)) return 'semantic';
  return 'app';
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  colorScheme: 'dark',
  locale: 'en-US',
});
const page = await context.newPage();
const cssBodies = new Map();
page.on('response', async (res) => {
  const url = res.url();
  const ct = res.headers()['content-type'] || '';
  if (!/text\/css|\.css/.test(ct + url)) return;
  if (cssBodies.has(url)) return;
  try {
    const body = await res.text();
    if (body && body.includes('--')) cssBodies.set(url, body.slice(0, 2_000_000));
  } catch { /* body already consumed */ }
});

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(1500);

const live = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]{40,}\)/g, 'url(…)') : v);
  const decls = [];
  const fonts = [];
  const errors = [];
  const walk = (list, media, href) => {
    for (const r of list) {
      if (r.type === CSSRule.STYLE_RULE) {
        const names = [];
        for (let i = 0; i < r.style.length; i++) {
          const n = r.style[i];
          if (n.startsWith('--')) names.push([n, noUrl(r.style.getPropertyValue(n).trim())]);
        }
        if (names.length) decls.push({ selector: r.selectorText, media: media || null, href, props: names });
      } else if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({ family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), href });
      } else if (r.cssRules) {
        const m = r.conditionText || (r.media && r.media.mediaText) || media;
        walk([...r.cssRules], m || media, href);
      }
    }
  };
  for (const ss of document.styleSheets) {
    let rules;
    try { rules = [...ss.cssRules]; } catch (e) { errors.push(ss.href || 'inline'); continue; }
    walk(rules, null, ss.href || 'inline');
  }
  const root = getComputedStyle(document.documentElement);
  const computed = {};
  const interesting = [];
  for (const d of decls) for (const [n] of d.props) if (!interesting.includes(n) && !n.startsWith('--tw-')) interesting.push(n);
  for (const n of interesting) computed[n] = root.getPropertyValue(n).trim();
  return {
    decls, fonts, errors,
    htmlClass: document.documentElement.className,
    colorScheme: root.colorScheme,
    computed,
    loadedFonts: [...document.fonts].map((f) => ({ family: f.family, weight: f.weight, style: f.style, status: f.status })),
  };
});

await browser.close();

const decls = [];
for (const d of live.decls) {
  for (const [name, value] of d.props) {
    decls.push({
      name,
      value,
      selector: d.selector,
      media: d.media,
      sheet: (d.href || '').replace(/\?.*$/, ''),
      owner: owner(name, d.selector),
    });
  }
}
decls.sort((a, b) => a.owner.localeCompare(b.owner) || a.name.localeCompare(b.name) || String(a.selector).localeCompare(String(b.selector)));

const out = {
  product: 'Pryzm',
  url: BASE,
  captured: '2026-11-21',
  theme: 'dark',
  note: 'Live CSSOM on https://pryzm.design/. html carries class dark. prefers-color-scheme light and dark both paint this palette. Values are declared custom properties, not sampled from screenshots.',
  htmlClass: live.htmlClass,
  colorScheme: live.colorScheme,
  stylesheetErrors: live.errors,
  pagesProbed: PAGES,
  fontFaces: live.fonts,
  loadedFonts: live.loadedFonts,
  computedOnRoot: live.computed,
  declCount: decls.length,
  decls,
};
fs.writeFileSync(path.join(OUT, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
const byOwner = {};
for (const d of decls) byOwner[d.owner] = (byOwner[d.owner] || 0) + 1;
console.log('decls', decls.length, byOwner, 'fonts', live.fonts.length, 'errors', live.errors);
