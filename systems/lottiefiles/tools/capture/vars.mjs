// Read every custom property lottiefiles.com's stylesheets declare and write
// raw/css-vars.json. Resolves each name on :root (light, the theme the public
// site paints) and on html.dark (the .dark block the stylesheet ships; no
// public page switched to it during capture).
//
//   PLAYWRIGHT=.../playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, launch, hideConsent } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const ROUTES = ['/', '/pricing', '/free-animations', '/free-animation/loading-animation-for-client-book-0DK063WUDW', '/marketplace'];

const { browser } = await launch({ dpr: 1 });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
// Automation is not hidden: no navigator.webdriver mask (bot check: recorded as a boundary, not bypassed).
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet' && !/\.css(\?|$)/.test(r.url())) return;
  try {
    const text = await r.text();
    if (text && text.includes('--')) bodies.set(r.url().split('?')[0], text);
  } catch { /* body gone */ }
});

for (const route of ROUTES) {
  await page.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => console.log('nav', route, e.message.split('\n')[0]));
  await page.waitForTimeout(2500);
  await hideConsent(page);
}
const inline = await page.evaluate(() => [...document.querySelectorAll('style')].map((s, i) => ['inline-' + i, s.textContent || '']));
const sheets = [...bodies.entries(), ...inline.filter(([, css]) => css && css.includes('--'))];
console.log('sheets', sheets.length, 'bytes', sheets.reduce((n, [, c]) => n + c.length, 0));

const probe = await browser.newPage();
await probe.setContent('<!doctype html><html><head></head><body></body></html>');
const harvested = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      try {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
            : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
            : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
            : (r.cssText || '').split('{')[0].trim().slice(0, 140);
          walk(r.cssRules, [...ctx, head], file);
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
        }
        if (Object.keys(props).length) rules.push({ selector: (r.selectorText || '').slice(0, 180), context: ctx.slice(-4), properties: props, file });
      } catch (e) { errors.push(String(e).slice(0, 160)); }
    }
  };
  for (const [name, css] of sheets) {
    try {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(css);
      walk(sheet.cssRules, [], name.split('/').pop().slice(0, 80));
    } catch (e) { errors.push(name.slice(0, 60) + ': ' + String(e).slice(0, 120)); }
  }
  return { rules, fonts, errors };
}, sheets);

function bin(rule) {
  const sel = rule.selector || '';
  const names = Object.keys(rule.properties);
  if (/\.dark\b/.test(sel) || names.some((n) => n === '--background' || n === '--foreground' || n === '--primary')) return 'theme';
  if (names.every((n) => n.startsWith('--tw-') || n.startsWith('--color-') && /-(50|100|200|300|400|500|600|700|800|900|950)$/.test(n))) return 'tailwind';
  if (sel.includes('[--') || names.some((n) => n.startsWith('--tw-'))) return 'utility';
  return 'app';
}
const bins = { theme: [], app: [], tailwind: [], utility: [] };
for (const r of harvested.rules) bins[bin(r)].push(r);

// Resolve on the live page: light is the painted theme, dark is html.dark
// forced so the stylesheet's .dark block wins. The public site never showed
// a theme switch; the dark resolution is the declared block, not a live paint.
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2000);
await hideConsent(page);
const NAMES = [...new Set(harvested.rules.flatMap((r) => Object.keys(r.properties)))];
async function resolve(mode) {
  return page.evaluate(({ names, mode }) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const html = document.documentElement;
    const prev = html.className;
    if (mode === 'dark') html.classList.add('dark');
    else html.classList.remove('dark');
    const cs = getComputedStyle(html);
    const out = {};
    for (const n of names) {
      const value = noUrl(cs.getPropertyValue(n).trim());
      if (value) out[n] = { value, raw: value };
    }
    html.className = prev;
    return out;
  }, { names: NAMES, mode });
}
const resolved = { light: await resolve('light'), dark: await resolve('dark') };
const painted = await page.evaluate(() => ({
  className: document.documentElement.className,
  colorScheme: getComputedStyle(document.documentElement).colorScheme,
  background: getComputedStyle(document.body).backgroundColor,
}));

const out = {
  product: 'lottiefiles',
  source: BASE + '/',
  captured: new Date().toISOString(),
  painted,
  note: 'light is the theme the public site painted. dark is html.dark forced so the stylesheet .dark block resolves; no public control switched the theme.',
  counts: { rules: harvested.rules.length, fonts: harvested.fonts.length, sheets: sheets.length, errors: harvested.errors.length },
  theme: bins.theme,
  app: bins.app,
  tailwind: bins.tailwind,
  utility: bins.utility,
  fonts: harvested.fonts.slice(0, 40),
  errors: harvested.errors.slice(0, 20),
  resolved,
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote css-vars.json', 'rules', harvested.rules.length, 'light', Object.keys(resolved.light).length, 'dark', Object.keys(resolved.dark).length, 'errors', harvested.errors.length);
await browser.close();
