// Reads every custom property withjulienne.com's stylesheet declares.
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// The product ships one hashed Vite CSS bundle. Product tokens are the
// glass custom properties (--glass-rim, --control-glass-*) plus
// --page-gutter. Tailwind's --tw-* utilities are binned separately.
// Resolved twice: html.js.light (boot) and html.js.dark (the theme class
// the Toggle theme control sets).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, RECIPE, launch, patch, clearChallenge } from './public/lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const { browser } = await launch();
const bodies = new Map();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await patch(context);
const p = await context.newPage();
p.on('response', async (r) => {
  if (r.request().resourceType() !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});
for (const path_ of ['/', '/discover', RECIPE, '/team', '/privacy-policy', '/signup']) {
  await p.goto(BASE + path_, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  await clearChallenge(p);
  await p.waitForTimeout(1500);
}
const inline = await p.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => {
  try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; }
}).filter(Boolean)).catch(() => []);
await context.close();

const sheets = [...bodies.entries(), ...inline.filter(([, css]) => css && css.length > 80)];
const probeCtx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await patch(probeCtx);
const probe = await probeCtx.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : (r.cssText || '').split('{')[0].trim().slice(0, 120);
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
      if (n) rules.push({ file: String(file).slice(0, 120), selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, ctx, file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: String(name).slice(0, 80), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

async function resolve(theme) {
  const htmlClass = theme === 'dark' ? 'js dark' : 'js light';
  const shell = '<!doctype html><html class="' + htmlClass + '"><head>'
    + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body><div id="probe-root" class="glass glass-interactive"></div></body></html>';
  await probe.setContent(shell, { waitUntil: 'load' });
  const names = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !n.startsWith('--tw-')).sort();
  return probe.evaluate((want) => {
    const readEl = document.getElementById('probe-root');
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;width:1000px;height:200px;visibility:hidden';
    const child = document.createElement('div');
    box.appendChild(child);
    document.body.appendChild(box);
    const out = {};
    for (const name of want) {
      const raw = noUrl(getComputedStyle(readEl).getPropertyValue(name).trim()) || noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
      if (!raw) { out[name] = { kind: 'missing' }; continue; }
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      child.removeAttribute('style');
      if (CSS.supports('color', raw)) { child.style.color = raw; r.kind = 'color'; r.value = getComputedStyle(child).color; }
      else if (CSS.supports('box-shadow', raw)) { child.style.boxShadow = raw; r.kind = 'shadow'; r.value = getComputedStyle(child).boxShadow; }
      else if (!raw.includes('%') && CSS.supports('width', raw)) { child.style.width = raw; r.kind = 'dimension'; r.value = getComputedStyle(child).width; }
      else r.kind = 'other';
      out[name] = r;
    }
    box.remove();
    return out;
  }, names);
}

const light = await resolve('light');
const dark = await resolve('dark');
await browser.close();

const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => n.startsWith('--tw-'))) return 'utility';
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'stylesheet bodies from live signed-out loads of withjulienne.com /, /discover, a public recipe, /team, /privacy-policy and /signup. Resolved on a probe document carrying those sheets, once as html.js.light and once as html.js.dark, at 1440x900.',
  sheets: sheets.map(([n, t]) => `${String(n).slice(0, 90)} (${t.length} bytes)`),
  counts: { rules: result.rules.length, fonts: result.fonts.length, names: { app: names('app').length, utility: names('utility').length } },
  errors: result.errors,
  app: result.rules.filter((r) => r.bin === 'app').slice(0, 80),
  utilityCount: result.rules.filter((r) => r.bin === 'utility').length,
  fonts: result.fonts.slice(0, 40),
  resolved: { light, dark },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars', out.counts, 'resolved light', Object.keys(light).length, 'dark', Object.keys(dark).length);
