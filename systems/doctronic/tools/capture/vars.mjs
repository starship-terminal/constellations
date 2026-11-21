// Read custom properties declared on doctronic.ai stylesheets (live, public).
// Writes raw/css-vars.json. No signed-in copies.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, UA } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'css-vars.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const bodies = [];
page.on('response', async (res) => {
  const ct = res.headers()['content-type'] || '';
  if (!/text\/css|javascript/.test(ct) && !res.url().includes('.css')) return;
  if (!/text\/css/.test(ct) && !res.url().endsWith('.css')) return;
  try {
    const text = await res.text();
    if (text.includes('--')) bodies.push({ url: res.url().split('?')[0].slice(0, 180), css: text });
  } catch { /* cross-origin body unavailable */ }
});
await page.goto(BASE + '/', { waitUntil: 'networkidle', timeout: 60000 });
await page.waitForTimeout(1000);

const parsed = await page.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.cssText.split('{')[0].trim().slice(0, 160);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText || '', ctx, file, props });
    }
  };
  for (const sheet of document.styleSheets) {
    let list;
    try { list = sheet.cssRules; } catch { continue; }
    walk(list, [], sheet.href || 'inline');
  }
  // also parse fetched css text via constructed sheets
  const extra = [];
  for (const s of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(s.css);
      const before = rules.length;
      walk(sheet.cssRules, [], s.url);
      extra.push({ url: s.url, added: rules.length - before });
    } catch (e) {
      extra.push({ url: s.url, error: String(e).slice(0, 120) });
    }
  }
  const resolved = {};
  const cs = getComputedStyle(document.documentElement);
  const names = new Set(rules.flatMap((r) => Object.keys(r.props)));
  for (const name of names) resolved[name] = cs.getPropertyValue(name).trim();
  const brand = {
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || '',
    maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || '',
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
  };
  return { rules, fonts, extra, resolved, brand, ruleCount: rules.length };
}, bodies.map((b) => ({ url: b.url, css: b.css.slice(0, 1_500_000) })));

const light = {};
for (const [name, value] of Object.entries(parsed.resolved)) {
  if (!value) continue;
  light[name] = { raw: value, value };
}
const out = {
  product: 'doctronic.ai',
  captured: '2026-11-21',
  route: 'public-web live stylesheets',
  brand: parsed.brand,
  fonts: parsed.fonts.slice(0, 40),
  ruleCount: parsed.ruleCount,
  extra: parsed.extra,
  rules: parsed.rules.filter((r) => Object.keys(r.props).some((k) => k.startsWith('--color-') || k.startsWith('--font') || k.startsWith('--radius') || k.startsWith('--space') || k.startsWith('--shadow'))).slice(0, 400),
  resolved: { light, dark: {} },
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
console.log('vars', Object.keys(light).length, 'rules', parsed.ruleCount, 'fonts', parsed.fonts.length, '->', OUT);
await browser.close();
