// Reads every custom property Lemni's public stylesheets declare and writes
// raw/css-vars.json.
//
// www.lemni.com is a Framer site: its CSS is inline <style> blocks (no linked
// sheets). It declares no --token-<uuid> palette. The declared layer is
// Framer's own plumbing (--framer-font-*, --framer-link-*, --border-*,
// --text-*) plus a handful of :root fallbacks. The painted colours are
// measured from elements, not from a token sheet.
//
// The account shell at lemni.com/signin is a separate React app and is
// harvested in a second pass (inline styles plus any linked sheets).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, patch, clearChallenge, BASE, APP } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
await patch(context);
const page = await context.newPage();
const bodies = new Map();
page.on('response', async (r) => {
  const rt = r.request().resourceType();
  if (rt !== 'stylesheet') return;
  try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
});

const pages = [BASE + '/', BASE + '/pricing', BASE + '/docs', APP + '/signup'];
const inline = [];
for (const url of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (!(await clearChallenge(page, { tries: 6, step: 1200 }))) { console.log('blocked', url); continue; }
  await page.waitForTimeout(2500);
  const blocks = await page.evaluate((url) => [...document.querySelectorAll('style')].map((s, i) => [url + '#inline-' + i, s.textContent || '']), url);
  for (const [name, css] of blocks) if (css && css.length > 40) inline.push([name, css]);
}

const sheets = [...bodies.entries(), ...inline];
console.log('sheets', sheets.length, 'linked', bodies.size, 'inline', inline.length);

const probe = await context.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file: file.slice(0, 80) };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
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
      if (n) rules.push({ file: file.slice(0, 90), selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 80)], file);
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push({ file: name.slice(0, 80), error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shellCss = sheets.map(([, css]) => css.replace(/<\/style/gi, '<\\/style')).join('\n');
await probe.setContent('<!doctype html><html><head><style>' + shellCss + '</style></head><body><div id="probe"></div></body></html>', { waitUntil: 'load' });
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].filter((n) => !n.startsWith('--tw-')).sort();
const resolved = await probe.evaluate((names) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const box = document.createElement('div');
  const p = document.createElement('div');
  box.appendChild(p);
  document.body.appendChild(box);
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(document.documentElement).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
    p.removeAttribute('style');
    if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)/.test(raw)) {
      p.style.color = raw;
      r.kind = 'color';
      r.value = getComputedStyle(p).color;
    } else r.kind = 'other';
    out[name] = r;
  }
  return out;
}, want);

const FRAMER = /^--framer-/;
const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (names.every((n) => FRAMER.test(n))) return 'framer';
  if (names.some((n) => n.startsWith('--token-'))) return 'token';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'inline <style> blocks and any linked stylesheets from a signed-out load of www.lemni.com /, /pricing, /docs and lemni.com/signup (which redirects to /signin), re-parsed with CSSStyleSheet and resolved on a probe carrying those sheets. Framer publishes no --token-* palette on these pages; painted colours are measured from elements.',
  sheets: sheets.map(([n, t]) => `${n.slice(0, 100)} (${t.length} bytes)`).slice(0, 40),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { token: names('token').length, app: names('app').length, framer: names('framer').length },
  },
  errors: result.errors.slice(0, 12),
  token: result.rules.filter((r) => r.bin === 'token').slice(0, 40),
  app: result.rules.filter((r) => r.bin === 'app').slice(0, 80),
  framerNames: names('framer'),
  fonts: result.fonts.slice(0, 40).map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-vars.json: ${result.rules.length} rules, ${result.fonts.length} faces; token ${out.counts.names.token} app ${out.counts.names.app} framer ${out.counts.names.framer}`);
await browser.close();
