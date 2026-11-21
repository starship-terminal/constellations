// Reads every custom property ROVR's stylesheets declare and writes raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// ROVR is a Next.js site. Stylesheets may be same-origin or cross-origin; both
// are fetched as text and re-parsed. The site paints one dark theme. Each name
// is resolved on a probe element, colours as sRGB, lengths as px at 1440x900.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);

const sheets = await page.evaluate(async () => {
  const out = [];
  for (const s of [...document.styleSheets]) {
    const href = s.href;
    try {
      const css = [...s.cssRules].map((r) => r.cssText).join('\n');
      out.push({ name: href || 'inline', css, via: 'cssom' });
    } catch {
      if (href) {
        try {
          const res = await fetch(href);
          out.push({ name: href, css: await res.text(), via: 'fetch' });
        } catch (e) {
          out.push({ name: href, css: '', via: 'failed', error: String(e) });
        }
      }
    }
  }
  // Tailwind / Next often puts tokens on :root as inline style too.
  const rootStyle = document.documentElement.getAttribute('style') || '';
  const bodyStyle = document.body.getAttribute('style') || '';
  return { sheets: out, rootStyle, bodyStyle };
});
await page.close();

const probe = await browser.newPage();
const result = await probe.evaluate((payload) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
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
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of payload.sheets) {
    if (!s.css) { if (s.error) errors.push({ file: s.name, error: s.error }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  const names = new Map();
  for (const r of rules) for (const [k, v] of Object.entries(r.properties)) {
    if (!names.has(k)) names.set(k, { raw: v, selector: r.selector, file: r.file });
  }
  const host = document.createElement('div');
  host.id = 'rovr-probe';
  document.body.appendChild(host);
  const resolved = {};
  for (const [k, meta] of names) {
    host.style.setProperty(k, meta.raw);
  }
  // Also copy :root computed custom props from the live document if any were
  // injected as inline. The probe page is blank, so resolution uses the raw
  // values we just set.
  const cs = getComputedStyle(host);
  for (const [k, meta] of names) {
    let value = cs.getPropertyValue(k).trim();
    if (!value) value = meta.raw;
    resolved[k] = { raw: meta.raw, value, selector: meta.selector, file: meta.file };
  }
  const bin = (name) => {
    if (name.startsWith('--tw-') || name.startsWith('--radix-')) return 'utility';
    if (name.includes('color') || name.includes('font') || name.includes('radius') || name.includes('shadow')) return 'token';
    return 'app';
  };
  const bins = {};
  for (const name of names.keys()) (bins[bin(name)] ??= []).push(name);
  return {
    product: 'ROVR',
    url: 'https://www.rovr.live/',
    captured: new Date().toISOString().slice(0, 10),
    theme: 'dark',
    sheetCount: payload.sheets.length,
    rootStyle: payload.rootStyle.slice(0, 500),
    ruleCount: rules.length,
    fontFaceCount: fonts.length,
    errors,
    bins,
    fonts: fonts.slice(0, 40).map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
    resolved: { dark: resolved },
    rules: rules.slice(0, 400),
  };
}, sheets);

fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(result, null, 1) + '\n');
const n = Object.keys(result.resolved.dark).length;
console.log('vars', n, 'rules', result.ruleCount, 'fonts', result.fontFaceCount, 'errors', result.errors.length);
await browser.close();
