// Read every custom property teenage.engineering declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The site ships same-origin CSS modules (root, layout, button, form, te013).
// Fonts.net is cross-origin and is recorded as skipped, not fetched.
// One theme: html[data-theme=default]. Lengths that use --client-width are
// resolved at 1440 x 900 and labelled as viewport-relative.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
const viewport = await page.evaluate(() => ({
  innerWidth: window.innerWidth,
  innerHeight: window.innerHeight,
  dpr: window.devicePixelRatio,
}));

const result = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const skipped = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.cssText.split('{')[0].trim().slice(0, 120);
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
      if (n) rules.push({ file, selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 120)], file);
    }
  };
  [...document.styleSheets].forEach((ss, i) => {
    const file = ss.href ? ss.href.split('/').pop().split('?')[0] || ss.href : `inline-${i}`;
    try { walk(ss.cssRules, [], file); } catch { skipped.push(file); }
  });
  return { rules, fonts, skipped };
});

const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))].sort();
const resolved = await page.evaluate((names) => {
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
  document.body.appendChild(probe);
  const norm = (c) => {
    const m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return { unparsed: c };
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : Math.round(+m[4] * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    if (!raw) continue;
    const r = { raw: raw.length > 400 ? raw.slice(0, 400) + '…' : raw };
    probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
    if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|transparent)$/.test(raw)) {
      probe.style.color = raw;
      const value = norm(getComputedStyle(probe).color);
      if (typeof value === 'string') { r.kind = 'color'; r.value = value; }
      else { r.kind = 'other'; r.note = 'colour not converted'; }
    } else if (CSS.supports('width', raw) && !raw.includes('%')) {
      probe.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probe).width;
      if (/vw|vh|dvh|client-width/.test(raw)) r.note = 'viewport-relative, resolved at the live viewport';
    } else if (/^-?\d*\.?\d+$/.test(raw)) {
      r.kind = 'number';
      r.value = +raw;
    } else if (/,/.test(raw) && CSS.supports('font-family', raw)) {
      r.kind = 'fontFamily';
      r.value = raw;
    } else {
      r.kind = 'other';
    }
    out[name] = r;
  }
  probe.remove();
  return out;
}, want);

const viewportNote = await page.evaluate(() => ({
  innerWidth: innerWidth,
  innerHeight: innerHeight,
  dpr: devicePixelRatio,
  theme: document.documentElement.getAttribute('data-theme'),
}));
await browser.close();

const binOf = (r) => {
  const sel = r.selector || '';
  if (sel === ':root' || sel === 'html' || sel === 'body') return 'theme';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);

const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'live CSSOM on https://teenage.engineering/ at 1440x900, html[data-theme=default]. Fonts.net sheet skipped (cross-origin).',
  viewport: viewportNote,
  launchViewport: viewport,
  sheetsSkippedCrossOrigin: result.skipped,
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: want.length,
  },
  theme: result.rules.filter((r) => r.bin === 'theme'),
  app: result.rules.filter((r) => r.bin === 'app'),
  fonts: result.fonts.map((f) => ({ ...f, src: f.src ? 'url(…)' : f.src })),
  resolved: { light: resolved },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars', out.counts, 'skipped', result.skipped, 'viewport', viewportNote);
