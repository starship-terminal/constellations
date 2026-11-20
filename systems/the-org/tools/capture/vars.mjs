// Reads every custom property theorg.com declares and writes raw/css-vars.json.
//
//   PLAYWRIGHT=... node tools/capture/vars.mjs
//
// Styles arrive as styled-components inline <style> blocks. They are read
// through the CSSOM, re-parsed with CSSStyleSheet, and each --* name is
// resolved on a probe document. The public site paints one light theme.
// A dark class is probed and recorded; it is not a user-facing theme.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, chromium, patch, clearChallenge } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
await patch(context);
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
if (!(await clearChallenge(page, { tries: 4, step: 800 }))) {
  console.log('home did not load; css-vars.json not written');
  await browser.close();
  process.exit(2);
}
const inline = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return ['sheet-' + i + (s.href ? '-' + s.href.split('/').pop().slice(0, 40) : '-inline'), [...s.cssRules].map((r) => r.cssText).join('\n')]; }
  catch { return null; }
}).filter(Boolean));
const sheets = inline.filter(([, text]) => text && text.includes('--'));
console.log('sheets', inline.length, 'with vars', sheets.length, 'bytes', sheets.reduce((n, s) => n + s[1].length, 0));

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]{0,200}\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        if (o.src) o.src = 'url(…)';
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : (r.cssText || '').split('{')[0].trim().slice(0, 80);
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim()).slice(0, 240);
      }
      if (Object.keys(props).length) rules.push({ file, selector: (r.selectorText || '').slice(0, 160), context: ctx, properties: props });
    }
  };
  for (const [name, text] of sheets) {
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(text); } catch (e) { errors.push(String(e).slice(0, 160)); continue; }
    walk(ss.cssRules, [], name);
  }
  return { rules, fonts, errors };
}, sheets);

const shell = (cls) => '<!doctype html><html class="' + cls + '"><head>'
  + sheets.map(([, css]) => '<style>' + css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
  + '</head><body></body></html>';
const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].sort();
const resolved = {};
for (const pass of ['light', 'dark']) {
  await probe.setContent(shell(pass === 'dark' ? 'dark' : ''), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const cs = getComputedStyle(document.documentElement);
    const out = {};
    const box = document.createElement('div');
    document.body.appendChild(box);
    for (const name of names) {
      const raw = cs.getPropertyValue(name).trim();
      if (!raw) continue;
      const r = { raw: raw.slice(0, 200) };
      box.removeAttribute('style');
      if (CSS.supports('color', raw)) {
        box.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(box).color;
      } else if (CSS.supports('width', raw) && !raw.includes('%')) {
        box.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(box).width;
      } else if (/font|sans|serif|grotesk|inter/i.test(raw)) {
        r.kind = 'fontFamily';
        r.value = raw;
      } else r.kind = 'other';
      out[name] = r;
    }
    return out;
  }, want);
}
await browser.close();

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'inline and linked stylesheets read from a live https://theorg.com/ load, re-parsed with CSSStyleSheet, resolved on a probe at 1440x900. One painted light theme. The dark probe adds a class the public site does not use.',
  counts: { rules: result.rules.length, fonts: result.fonts.length, names: want.length },
  errors: result.errors,
  rules: result.rules,
  fonts: result.fonts.map((f) => ({ family: f['font-family'], weight: f['font-weight'], style: f['font-style'], file: f.file })),
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars', result.rules.length, 'rules', want.length, 'names', result.fonts.length, 'fonts');
console.log('resolved light', Object.keys(resolved.light).length, 'dark', Object.keys(resolved.dark).length);
