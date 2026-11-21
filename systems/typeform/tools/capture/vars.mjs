// Read every custom property Typeform's public stylesheets declare and write
// raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// typeform.com is a Webflow site. The shared CSS is cross-origin
// (cdn.prod.website-files.com), so the CSSOM cannot read it. This script
// collects stylesheet bodies from network responses, parses them headless,
// and resolves each --* name on a probe element the way the browser does.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, hideConsent, BASE } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const sheets = new Map();
page.on('response', async (res) => {
  const url = res.url();
  const ct = (res.headers()['content-type'] || '');
  if (!/text\/css|stylesheet/i.test(ct) && !/\.css(\?|$)/.test(url)) return;
  if (sheets.has(url)) return;
  try {
    const css = await res.text();
    if (css && css.includes('--')) sheets.set(url, css);
  } catch { /* body already consumed or failed */ }
});
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(5000);
await hideConsent(page);
// also pull link[rel=stylesheet] that the listener missed
const hrefs = await page.evaluate(() => [...document.querySelectorAll('link[rel="stylesheet"]')].map((l) => l.href));
for (const href of hrefs) {
  if (sheets.has(href)) continue;
  try {
    const r = await page.request.get(href, { timeout: 30000 });
    if (r.ok()) {
      const css = await r.text();
      if (css.includes('--')) sheets.set(href, css);
    }
  } catch { /* skip */ }
}
console.log('sheets', sheets.size, [...sheets.keys()].map((u) => u.slice(0, 90)));

const probe = await browser.newPage();
const payload = [...sheets.entries()].map(([name, css]) => ({ name, css }));
const result = await probe.evaluate(async (payload) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(...)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file: file.slice(0, 120) };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : (r.cssText || '').split('{')[0].trim().slice(0, 100);
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
      if (n) rules.push({ file: file.slice(0, 140), selector: (r.selectorText || '').slice(0, 180), context: ctx.slice(0, 4), properties: props });
    }
  };
  const adopted = new CSSStyleSheet();
  for (const s of payload) {
    try {
      const ss = new CSSStyleSheet();
      ss.replaceSync(s.css);
      walk(ss.cssRules, [], s.name);
      for (const r of ss.cssRules) {
        try { adopted.insertRule(r.cssText, adopted.cssRules.length); } catch { /* skip invalid */ }
      }
    } catch (e) { errors.push({ file: s.name.slice(0, 120), error: String(e).slice(0, 200) }); }
  }
  document.adoptedStyleSheets = [adopted];
  const el = document.createElement('div');
  el.id = 'probe';
  document.body.appendChild(el);
  const cs = getComputedStyle(el);
  const names = new Set();
  for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
  const resolved = {};
  for (const name of names) {
    const raw = cs.getPropertyValue(name).trim();
    resolved[name] = { raw: raw || ruleRaw(name), value: raw || ruleRaw(name) };
  }
  function ruleRaw(name) {
    for (let i = rules.length - 1; i >= 0; i--) {
      if (rules[i].properties[name] && (!rules[i].selector || rules[i].selector === ':root' || rules[i].selector === 'body' || rules[i].selector === 'html')) {
        return rules[i].properties[name];
      }
    }
    for (let i = rules.length - 1; i >= 0; i--) if (rules[i].properties[name]) return rules[i].properties[name];
    return '';
  }
  // Prefer the computed value when the browser resolved it.
  for (const name of names) {
    const computed = cs.getPropertyValue(name).trim();
    if (computed) resolved[name] = { raw: resolved[name].raw, value: computed };
  }
  return { rules, fonts: fonts.slice(0, 40), errors, resolved, nameCount: names.size };
}, payload);

const bins = { tokens: [], typography: [], webflow: [], other: [] };
for (const rule of result.rules) {
  const keys = Object.keys(rule.properties);
  const bucket = keys.some((k) => k.startsWith('--tokens--') || k.startsWith('--_typography'))
    ? (keys.some((k) => k.startsWith('--_typography')) && !keys.some((k) => k.startsWith('--tokens--')) ? 'typography' : 'tokens')
    : keys.some((k) => k.startsWith('--wf-') || k.includes('webflow')) ? 'webflow' : 'other';
  bins[bucket].push(rule);
}

const out = {
  source: 'https://www.typeform.com/ public Webflow stylesheets, read 2026-11-21, signed out, 1440x900',
  sheetCount: sheets.size,
  nameCount: result.nameCount,
  errors: result.errors,
  fonts: result.fonts,
  tokens: bins.tokens,
  typography: bins.typography,
  webflow: bins.webflow.slice(0, 30),
  other: bins.other.slice(0, 80),
  resolved: { light: result.resolved },
};
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('names', result.nameCount, 'rules', result.rules.length, 'errors', result.errors.length, 'fonts', result.fonts.length);
await browser.close();
