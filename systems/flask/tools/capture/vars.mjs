// Dumps the custom properties flask.do's public bundle declares, then asks a live
// public page what each one resolves to.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node vars.mjs
//
// The properties live in the inline <style id="ds-theme"> block every page
// ships (channel triplets like `--ds-surface-0: 12 12 12`, plus px/rem scalars)
// and in the linked root-*.css bundle (a handful of structural vars like
// --ds-font-sans/--ds-radius and the --ds-row-hover "channel / alpha" form).
// The file is parsed textually for :root and [data-ds-theme="default"] rules —
// flask.do declares exactly one theme, "default" on <html data-ds-theme>, and
// every public page paints it. Resolution is a live computed-style probe in
// the live dark context only: the site ships no light variant or toggle, so
// the output's resolved.dark object is the only resolved layer.
//
// Every value is what the live page resolves — computed, never re-derived here.
// No token, value or theme is invented.

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium, BASE } from './public/lib.mjs';

// systems/<slug>/raw — the package's committed raw evidence, same place
// measure.mjs writes components-computed.json.
const OUT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', 'raw');

const sheetTexts = async () => {
  const texts = [];
  const ctx = await chromium.launch().then((b) => b.newContext());
  const p = await ctx.newPage();
  const seen = new Set();
  for (const url of [BASE + '/', BASE + '/pricing']) {
    p.on('response', async (r) => {
      if (!r.request().isNavigationRequest() && /\.css($|\?)/.test(r.url()) && !seen.has(r.url())) {
        seen.add(r.url());
        try { texts.push(await r.text()); } catch {}
      }
    });
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(4000);
    // Also pull the inline ds-theme block out of the live DOM.
    const inline = await p.evaluate(() => [...document.querySelectorAll('style')]
      .map((s) => s.textContent || '').filter((t) => /--ds-[\w-]+\s*:/.test(t)));
    for (const t of inline) if (!texts.includes(t)) texts.push(t);
  }
  await ctx.browser().close();
  return texts;
};

const blocks = (css) => {
  const out = [];
  const re = /:root(?:\[data-ds-theme=["']?([\w-]+)["']?\])?\s*\{([^}]*)\}/g;
  let m;
  while ((m = re.exec(css))) out.push({ sel: m[0].match(/^[^\{]+/)[0].trim(), theme: m[1] || null, body: m[2] });
  return out;
};

const decls = (body) => {
  const d = {};
  for (const m of body.matchAll(/(--[\w-]+)\s*:\s*([^;}]+?)\s*;/g)) d[m[1]] = m[2].trim();
  return d;
};

const texts = await sheetTexts();
const declared = { root: {}, themes: {} };
const seenThemes = new Set();
for (const css of texts) for (const b of blocks(css)) {
  const d = decls(b.body);
  if (!Object.keys(d).length) continue;
  if (b.theme) { seenThemes.add(b.theme); declared.themes[b.theme] = { ...(declared.themes[b.theme] || {}), ...d }; }
  else declared.root = { ...declared.root, ...d };
}
// Merge the :root layer into the theme's resolved set: on flask.do the inline
// block declares most tokens under :root itself while [data-ds-theme] and the
// html selector redeclare or add a few; a :root computed read resolves all.
const themeKey = [...seenThemes][0] || 'default';
const allDecl = { ...declared.root, ...(declared.themes[themeKey] || {}) };
const names = Object.keys(allDecl).sort();

const b2 = await chromium.launch();
const ctx2 = await b2.newContext({ viewport: { width: 1440, height: 900 } });
const p2 = await ctx2.newPage();
await p2.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await p2.waitForTimeout(5000);
// A custom property can hold a url() with a signed or per-account query, so
// every resolved value is recorded through noUrl, which blanks url() bodies.
const attrs = await p2.evaluate(() => ({ dsTheme: document.documentElement.getAttribute('data-ds-theme'), scheme: getComputedStyle(document.documentElement).colorScheme }));
const resolved = await p2.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const cs = getComputedStyle(document.documentElement);
  const out = {};
  for (const n of names) out[n] = noUrl(cs.getPropertyValue(n).trim());
  return out;
}, names);
await b2.close();

fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, 'css-vars.json'), JSON.stringify({ attrs, declared, resolved: { dark: resolved } }, null, 2) + '\n');
console.log('theme attr', JSON.stringify(attrs), '| themes seen:', JSON.stringify([...seenThemes]));
console.log(`${names.length} custom props (${Object.keys(declared.root).length} on :root, ${Object.keys(declared.themes[themeKey] || {}).length} under [data-ds-theme]) ->`, path.join(OUT, 'css-vars.json'));
