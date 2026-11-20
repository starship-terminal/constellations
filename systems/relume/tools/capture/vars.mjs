// Read Relume's declared custom properties from the Webflow CDN stylesheet
// (cross-origin, so the page CSSOM cannot see the rules) and resolve each
// name in light and dark on the live homepage.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const bodies = [];
page.on('response', async (r) => {
  const ct = r.headers()['content-type'] || '';
  const url = r.url();
  if (!ct.includes('text/css') && !url.includes('.css')) return;
  if (!url.includes('website-files.com') && !url.includes('relume')) return;
  try {
    const css = await r.text();
    if (css.includes('--')) bodies.push({ url, css });
  } catch { /* body already consumed */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(4000);

const parsed = await page.evaluate((sheets) => {
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({ file, family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style') });
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : (r.cssText || '').split('{')[0].trim().slice(0, 140);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim().slice(0, 180);
      }
      if (Object.keys(props).length) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.url, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], s.url.split('/').pop());
  }
  return { rules, fonts, errors };
}, bodies.map((b) => ({ url: b.url, css: b.css })));

function declaredNames() {
  const names = new Set();
  for (const rule of parsed.rules) for (const k of Object.keys(rule.properties)) names.add(k);
  return [...names];
}

async function resolve(theme) {
  await page.evaluate((theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    document.body.classList.toggle('p-theme-dark', theme === 'dark');
    let probe = document.getElementById('capture-var-probe');
    if (!probe) {
      probe = document.createElement('div');
      probe.id = 'capture-var-probe';
      document.body.appendChild(probe);
    }
  }, theme);
  await page.waitForTimeout(300);
  return page.evaluate((names) => {
    const probe = document.getElementById('capture-var-probe');
    const cs = getComputedStyle(probe);
    const bodyVars = {};
    for (const name of names) bodyVars[name] = cs.getPropertyValue(name).trim();
    const h1 = document.querySelector('h1');
    const cta = [...document.querySelectorAll('a, button')].find((el) => /Start for free/.test(el.innerText || ''));
    return {
      body: {
        backgroundColor: getComputedStyle(document.body).backgroundColor,
        color: getComputedStyle(document.body).color,
        fontFamily: getComputedStyle(document.body).fontFamily,
        fontSize: getComputedStyle(document.body).fontSize,
      },
      h1: h1 ? {
        fontFamily: getComputedStyle(h1).fontFamily,
        fontSize: getComputedStyle(h1).fontSize,
        fontWeight: getComputedStyle(h1).fontWeight,
        lineHeight: getComputedStyle(h1).lineHeight,
        letterSpacing: getComputedStyle(h1).letterSpacing,
        color: getComputedStyle(h1).color,
      } : null,
      cta: cta ? {
        backgroundColor: getComputedStyle(cta).backgroundColor,
        color: getComputedStyle(cta).color,
        borderRadius: getComputedStyle(cta).borderRadius,
        fontSize: getComputedStyle(cta).fontSize,
        fontWeight: getComputedStyle(cta).fontWeight,
        padding: getComputedStyle(cta).padding,
      } : null,
      themeClass: document.body.className,
      dataTheme: document.documentElement.getAttribute('data-theme'),
      bodyVars,
    };
  }, declaredNames());
}

const light = await resolve('light');
const dark = await resolve('dark');
await browser.close();

const declared = {};
for (const rule of parsed.rules) {
  for (const [k, v] of Object.entries(rule.properties)) {
    if (!declared[k]) declared[k] = { value: v, selector: rule.selector, file: rule.file };
  }
}

const out = {
  read: new Date().toISOString().slice(0, 10),
  url: BASE + '/',
  sheets: bodies.map((b) => ({ url: b.url.split('/').pop(), bytes: b.css.length })),
  declaredCount: Object.keys(declared).length,
  ruleCount: parsed.rules.length,
  fonts: parsed.fonts.slice(0, 40),
  errors: parsed.errors,
  declared,
  resolved: { light, dark },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('rules', parsed.rules.length, 'declared', Object.keys(declared).length, 'body vars light', Object.keys(light.bodyVars).length, 'dark', Object.keys(dark.bodyVars).length);
console.log('errors', parsed.errors.length);
