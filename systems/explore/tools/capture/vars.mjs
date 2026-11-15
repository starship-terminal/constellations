// Reads every declaration the explore.family stylesheet bundle carries and
// writes raw/css-declarations.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// explore.family's February 2023 build ships one compiled stylesheet
// (mirror/css/app.4ef09b07.css, captured from web.archive.org on the
// 2023-02-23 snapshot). It declares NO custom properties — not a single
// `--name:` declaration; the `--x` tokens grep finds are all BEM modifier
// class names (.btn--yellow, .page--arrow). There is no token layer to
// resolve, so this script records the sheet the way the browser parses it:
// every style rule's selector, its enclosing @media context, and its full
// declaration block, plus the @font-face rules. Values are the literals the
// site shipped; colours are additionally normalised through the browser to
// sRGB hex so build_tokens.py reads one spelling.
//
// The CSS is read from the local mirror on disk — no network. MIRROR env
// overrides the default location.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { MIRROR } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const CSS_FILE = path.join(MIRROR, 'css', 'app.4ef09b07.css');
const css = fs.readFileSync(CSS_FILE, 'utf8');

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.setContent('<!doctype html><html><head></head><body></body></html>');

const result = await page.evaluate((cssText) => {
  // A declaration can hold a url() with a signed or per-account query: record it as url(…).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const colors = new Map();
  const norm = (c) => {
    const probe = document.createElement('i');
    probe.style.color = c;
    const cs = getComputedStyle(probe).color;
    const m = cs.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return c;
    const a = m[4] === undefined ? 1 : +m[4];
    return a === 1 ? '#' + [m[1], m[2], m[3]].map((v) => Math.round(+v).toString(16).padStart(2, '0')).join('')
      : `rgba(${Math.round(+m[1])}, ${Math.round(+m[2])}, ${Math.round(+m[3])}, ${Math.round(a * 1000) / 1000})`;
  };
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = {};
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head]);
        continue;
      }
      if (!r.style || !r.selectorText) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        const v = noUrl(r.style.getPropertyValue(k).trim());
        props[k] = v;
        if (/color|background/.test(k) && !/url|gradient|var\(/.test(v)) colors.set(v, norm(v));
      }
      rules.push({ selector: r.selectorText, context: ctx.length ? ctx : undefined, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText]);
    }
  };
  const ss = new CSSStyleSheet();
  ss.replaceSync(cssText);
  walk(ss.cssRules, []);
  // Distinct value histograms for the token builders.
  const hist = {};
  for (const key of ['font-size', 'font-weight', 'line-height', 'border-radius', 'color', 'background', 'background-color', 'padding', 'padding-left', 'margin', 'gap']) {
    const c = {};
    for (const r of rules) if (r.properties[key] !== undefined) c[r.properties[key]] = (c[r.properties[key]] || 0) + 1;
    hist[key] = Object.fromEntries(Object.entries(c).sort((a, b) => b[1] - a[1]));
  }
  return { rules, fonts, colors: Object.fromEntries([...colors.entries()].sort()), histograms: hist };
}, css);

await browser.close();

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'css/app.4ef09b07.css in the local Internet Archive mirror (web.archive.org snapshot 2023-02-23 of https://explore.family/css/app.4ef09b07.css)',
  note: 'Explore declares no CSS custom properties and no prefers-color-scheme rules: one fixed light theme, every value hardcoded. --x strings found by grep are BEM modifier class names (.btn--yellow), not variables.',
  bytes: css.length,
  rules: result.rules.length,
  fontFaces: result.fonts.length,
  fonts: result.fonts,
  colors: result.colors,
  histograms: result.histograms,
  declarations: result.rules,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-declarations.json'), JSON.stringify(out, null, 1) + '\n');
console.log(`css-declarations.json: ${out.rules} rules, ${out.fontFaces} font faces, ${Object.keys(result.colors).length} distinct colours`);
