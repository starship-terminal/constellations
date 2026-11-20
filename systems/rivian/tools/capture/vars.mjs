// Read every custom property rivian.com declares and write raw/css-vars.json.
// Live page, not a snapshot: the CSSOM can read the same-origin sheets.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, open, BASE } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();
await open(page, BASE + '/', { wait: 1500 });

const harvested = await page.evaluate(() => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const sheets = [];
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
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
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
  for (const s of document.styleSheets) {
    const name = s.href || 'inline';
    try {
      sheets.push({ name, media: s.media.mediaText || '', rules: s.cssRules.length });
      walk(s.cssRules, [], name);
    } catch (e) {
      errors.push({ file: name, error: String(e).slice(0, 180) });
    }
  }
  return { rules, fonts, errors, sheets };
});

const names = [...new Set(harvested.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_)/.test(n)).sort();

const resolved = await page.evaluate((want) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
  const root = document.documentElement;
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
  document.body.appendChild(probe);
  const out = {};
  for (const name of want) {
    const raw = noUrl(getComputedStyle(root).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 300 ? raw.slice(0, 300) + '…' : raw };
    probe.removeAttribute('style');
    probe.style.cssText = 'position:absolute;left:0;top:0;visibility:hidden';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|currentcolor)$/i.test(raw)) {
      probe.style.color = raw;
      const c = getComputedStyle(probe).color;
      const m = c.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)$/);
      if (m) {
        const rgb = [m[1], m[2], m[3]].map((v) => (+v).toString(16).padStart(2, '0')).join('');
        const a = m[4] === undefined ? 1 : +m[4];
        r.kind = 'color';
        r.value = a === 1 ? '#' + rgb : `rgba(${m[1]}, ${m[2]}, ${m[3]}, ${a})`;
      } else { r.kind = 'other'; r.note = c; }
    } else if (!raw.includes('%') && CSS.supports('width', raw)) {
      probe.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probe).width;
    } else if (/^(ease|ease-in|ease-out|ease-in-out|linear|cubic-bezier\()/.test(raw)) {
      r.kind = 'easing'; r.value = raw;
    } else if (/^\d+(\.\d+)?m?s$/.test(raw)) {
      r.kind = 'duration'; r.value = raw;
    } else if (CSS.supports('font-family', raw)) {
      r.kind = 'fontFamily'; r.value = raw;
    } else r.kind = 'other';
    out[name] = r;
  }
  probe.remove();
  const body = getComputedStyle(document.body);
  const header = document.querySelector('header');
  const hs = header ? getComputedStyle(header) : null;
  return {
    vars: out,
    computed: {
      body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize },
      header: hs && { backgroundColor: hs.backgroundColor, color: hs.color, height: hs.height, fontFamily: hs.fontFamily },
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
    },
  };
}, names);

await browser.close();

const binOf = (r) => {
  const ns = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (ns.every((n) => n.startsWith('--tw-') || n.startsWith('--_'))) return 'tailwind';
  if (ns.some((n) => n.startsWith('--consumer-ui-') || n.startsWith('--navbar-') || n.startsWith('--radius-') || n.startsWith('--gap-'))) return 'app';
  return 'app';
};
for (const r of harvested.rules) r.bin = binOf(r);
const nameList = (bin) => [...new Set(harvested.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'rivian.com live stylesheets, read through the CSSOM on the public home page at 1440x900 after Reject All. One light theme. color-scheme is normal.',
  sheets: harvested.sheets,
  counts: {
    rules: harvested.rules.length,
    fonts: harvested.fonts.length,
    names: { app: nameList('app').length, utility: nameList('utility').length },
  },
  errors: harvested.errors,
  app: harvested.rules.filter((r) => r.bin === 'app'),
  utility: harvested.rules.filter((r) => r.bin === 'utility'),
  fonts: harvested.fonts,
  resolved: { light: resolved.vars },
  computed: resolved.computed,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', harvested.rules.length, 'fonts', harvested.fonts.length, 'resolved', Object.keys(resolved.vars).length, 'errors', harvested.errors.length);
console.log('computed', JSON.stringify(resolved.computed));
