// Reads every custom property onmarathon.com's stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The archive paints one light theme (html.light). A .dark rule exists in the
// CSS and is resolved on a probe by adding class "dark" and removing "light".
// That probe is not a live theme: no public control switches it.
// Colours come back as the browser computes them. Lengths are px at 1440x900.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(2000);

const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch (e) { return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: true, error: String(e).slice(0, 160) }; }
}));
await page.close();

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
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
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    if (!s.css) { if (s.unreadable) errors.push({ file: s.name, error: s.error || 'unreadable' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 200) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

function bin(rule) {
  const sel = rule.selector || '';
  const names = Object.keys(rule.properties);
  if (sel.startsWith('[--') || /\[--[\w-]+/.test(sel)) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if (names.some((n) => n.startsWith('--tw-'))) return 'tailwind';
  return 'app';
}
const bins = { app: [], tailwind: [], utility: [] };
for (const r of result.rules) bins[bin(r)].push(r);

// Resolve on a probe that carries the real sheets, once as html.light and
// once with class "dark" forced (not a live theme).
await probe.setContent('<!doctype html><html class="light"><head></head><body></body></html>');
await probe.evaluate((sheets) => {
  for (const s of sheets) {
    if (!s.css) continue;
    const el = document.createElement('style');
    el.textContent = s.css;
    document.head.appendChild(el);
  }
}, sheets);

async function resolve(mode) {
  return probe.evaluate((mode) => {
    const html = document.documentElement;
    html.classList.remove('light', 'dark');
    html.classList.add(mode);
    const cs = getComputedStyle(html);
    const names = new Set();
    for (const sheet of document.styleSheets) {
      const walk = (rules) => {
        for (const r of rules) {
          if (r.cssRules) walk([...r.cssRules]);
          if (!r.style) continue;
          for (const n of r.style) if (n.startsWith('--') && !n.startsWith('--tw-')) names.add(n);
        }
      };
      try { walk([...sheet.cssRules]); } catch { /* cross-origin */ }
    }
    const out = {};
    for (const n of [...names].sort()) {
      out[n] = { value: cs.getPropertyValue(n).trim() };
    }
    return {
      mode,
      htmlClass: html.className,
      bodyBackground: getComputedStyle(document.body).backgroundColor,
      colorScheme: getComputedStyle(document.body).colorScheme,
      vars: out,
    };
  }, mode);
}

const light = await resolve('light');
const darkProbe = await resolve('dark');
await browser.close();

const out = {
  product: 'onmarathon.com',
  captured: '2026-11-21',
  themeNote: 'Live pages paint html.light. resolved.dark is a probe that adds class dark and removes light. No public control switches the theme.',
  sheets: sheets.map(({ name, media, css, unreadable }) => ({ name, media, bytes: (css || '').length, unreadable: !!unreadable })),
  errors: result.errors,
  fonts: result.fonts,
  app: bins.app,
  tailwind: bins.tailwind.length,
  utility: bins.utility,
  resolved: { light: light.vars, dark: darkProbe.vars },
  probe: { light: { htmlClass: light.htmlClass, bodyBackground: light.bodyBackground }, dark: { htmlClass: darkProbe.htmlClass, bodyBackground: darkProbe.bodyBackground, note: 'forced class, not a live theme' } },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', result.rules.length, 'fonts', result.fonts.length, 'app', bins.app.length, 'light vars', Object.keys(light.vars).length, 'dark probe vars', Object.keys(darkProbe.vars).length);
console.log('body light', light.bodyBackground, 'body dark-probe', darkProbe.bodyBackground);
