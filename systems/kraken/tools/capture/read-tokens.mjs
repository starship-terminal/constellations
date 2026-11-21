// Read Kraken's declared design tokens from the live public homepage CSSOM.
// Writes raw/css-vars.json. Does not click consent, does not sign in.
//
//   PLAYWRIGHT=<index.mjs> node tools/capture/read-tokens.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, open, BASE, PKG } from './public/lib.mjs';

const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const KEEP = (k) =>
  k.startsWith('--colors-ds-') ||
  k.startsWith('--fontSize-ds-') ||
  k.startsWith('--fontFamily-ds-') ||
  k.startsWith('--fontWeight-ds-') ||
  k.startsWith('--lineHeight-ds-') ||
  k.startsWith('--letterSpacing-ds-') ||
  k.startsWith('--border-radius-ds-') ||
  k.startsWith('--spacing-ds-') ||
  k.startsWith('--surface-glass-') ||
  k.startsWith('--surface-panel-');

const { browser, context } = await launch();
const page = await context.newPage();
await open(page, BASE + '/', { wait: 3000 });

const data = await page.evaluate((keepPrefixes) => {
  const keep = (k) => keepPrefixes.some((p) => k.startsWith(p));
  const rows = [];
  const fonts = [];
  const themeMeta = [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({
    content: m.content, media: m.getAttribute('media'),
  }));
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family'),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
            href: sheet.href,
          });
          continue;
        }
        if (r.cssRules && !r.style) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k.startsWith('--') && keep(k)) props[k] = r.style.getPropertyValue(k).trim();
        }
        if (Object.keys(props).length) {
          rows.push({
            selector: r.selectorText || '',
            href: (sheet.href || '').replace(/\?.*$/, ''),
            props,
          });
        }
      }
    };
    walk(rules);
  }
  const root = getComputedStyle(document.documentElement);
  const body = getComputedStyle(document.body);
  const signup = document.querySelector('a[href="/sign-up"]');
  const h1 = document.querySelector('h1');
  const computed = {
    body: {
      backgroundColor: body.backgroundColor,
      color: body.color,
      fontFamily: body.fontFamily,
    },
    htmlClass: document.documentElement.className,
    bodyClass: document.body.className,
    themeColor: themeMeta,
    signup: signup ? ((cs) => ({
      backgroundColor: cs.backgroundColor, color: cs.color, borderRadius: cs.borderRadius,
      height: cs.height, padding: cs.padding, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
      fontFamily: cs.fontFamily,
    }))(getComputedStyle(signup)) : null,
    h1: h1 ? ((cs) => ({
      color: cs.color, fontSize: cs.fontSize, fontWeight: cs.fontWeight, lineHeight: cs.lineHeight,
      fontFamily: cs.fontFamily, letterSpacing: cs.letterSpacing,
    }))(getComputedStyle(h1)) : null,
    pageVar: root.getPropertyValue('--colors-ds-semantic-surface-page').trim(),
    brandVar: root.getPropertyValue('--colors-ds-semantic-content-brand').trim(),
  };
  return { rows, fonts, computed, url: location.href, title: document.title };
}, [
  '--colors-ds-', '--fontSize-ds-', '--fontFamily-ds-', '--fontWeight-ds-',
  '--lineHeight-ds-', '--letterSpacing-ds-', '--border-radius-ds-', '--spacing-ds-',
  '--surface-glass-', '--surface-panel-',
]);

const out = {
  capturedAt: new Date().toISOString(),
  url: 'https://www.kraken.com/',
  title: data.title,
  note: 'Declared custom properties read from the homepage CSSOM. The live public marketing site applies magic-light-theme. Dark selectors are declared in the same sheets and were not switched on a public page.',
  computed: data.computed,
  fonts: data.fonts.filter((f) => /Kraken|Plex|Helvetica/i.test(f.family || '')).slice(0, 40),
  rules: data.rows,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out));
console.log('rules', data.rows.length, 'bytes', fs.statSync(path.join(RAW, 'css-vars.json')).size);
await browser.close();
