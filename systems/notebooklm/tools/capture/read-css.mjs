// Reads NotebookLM's theme variables and the CSS facts the tokens need from the page copies, and
// writes raw/css-vars.json and raw/css-facts.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/read-css.mjs
//
// Replaces the kit's vars.mjs for this package: NotebookLM's own tokens are declared as
// light-dark(light, dark) and Angular Material's under .dark-theme, so a variable's raw text does
// not say what it paints. Each copy is opened headless (fonts and gstatic through the local cache,
// nothing from notebook.google.com) in dark, then again with the body class swapped to light, and
// every custom property declared anywhere in the CSSOM is resolved on <body>: colours through a
// probe element (`color: var(--x)` read back as rgb), everything else as the computed text with
// var() references substituted. Then, from the same CSSOM:
//   media      every @media condition, with how many rules sit under it
//   reduced    every rule under @media (prefers-reduced-motion: reduce), selector and declarations
//   motion     transition and animation durations and timing functions, counted
//   zIndex     every z-index declared, with its selector, plus the overlay layers' computed values
//   shadows    every box-shadow value, with the selectors that use it, and per resolved value the
//              components it paints in the copies
//   grids      grid-template-columns of the notebook grid at 1440, 1024, 800 and 390
//   widths     max-width / max-inline-size declarations and the computed content columns
//   fonts      @font-face families and the stacks the type classes resolve to
//   usage      per copy and theme, how many visible elements paint each background, text and border
//              colour, each radius and each font size
import fs from 'node:fs';
import path from 'node:path';
import { chromium, RAW, SNAPS, metaOf, newContext, openSnap } from './signed-in/lib.mjs';

if (!SNAPS) { console.error('SNAPS=<snapshot dir> is required'); process.exit(2); }
const COPIES = ['home-dark', 'notebook-dark'];
const browser = await chromium.launch();

const readPage = () => {
  const walk = (list, ctx, out) => {
    for (const r of list) {
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head], out);
        continue;
      }
      if (r.type === CSSRule.FONT_FACE_RULE) { out.fontFaces.push({ family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), src: ((r.style.getPropertyValue('src').match(/url\("?([^")]+)/) || [])[1] || '').split(/[?#]/)[0] }); continue; }
      if (!r.style) continue;
      out.rules.push({ sel: r.selectorText || '', ctx, style: r.style });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], out);
    }
  };
  const out = { rules: [], fontFaces: [] };
  for (const ss of document.styleSheets) { try { walk(ss.cssRules, [], out); } catch { /* cross-origin: fonts only */ } }
  // Every custom property name declared anywhere.
  const names = new Set();
  for (const r of out.rules) for (let i = 0; i < r.style.length; i++) if (r.style[i].startsWith('--')) names.add(r.style[i]);
  // The probe sits in a wrapper with a sentinel colour, so a variable that does not resolve to a
  // colour (invalid at computed-value time) shows up as the inherited sentinel, not as <body>'s text.
  const wrap = document.createElement('div');
  wrap.style.cssText = 'position:absolute;left:-9999px;top:0;color:rgb(7, 8, 9)';
  const probe = document.createElement('div');
  wrap.appendChild(probe);
  document.body.appendChild(wrap);
  const bodyCs = getComputedStyle(document.body);
  const vars = {};
  for (const n of [...names].sort()) {
    const raw = bodyCs.getPropertyValue(n).trim();
    if (!raw) continue;
    probe.style.color = 'rgb(1, 2, 3)';
    probe.style.color = `var(${n})`;
    const c = getComputedStyle(probe).color;
    const isColor = c !== 'rgb(1, 2, 3)' && c !== 'rgb(7, 8, 9)' && /^(rgb|color|oklch|lab)/.test(c) && !/^(inherit|initial|unset)$/.test(raw);
    // A value that also parses as a colour on a second sentinel is a real colour.
    probe.style.color = 'rgb(4, 5, 6)';
    probe.style.color = `var(${n})`;
    const c2 = getComputedStyle(probe).color;
    vars[n] = isColor && c2 === c ? { raw, color: c } : { raw };
  }
  wrap.remove();
  return { out, vars };
};

const result = { _meta: { read: '2026-10-17', copies: COPIES, method: 'Headless Chromium on the redacted page copies; dark as captured, light with body.dark-theme swapped for light-theme. Colours resolved through a probe element on <body>.' }, vars: {}, media: {}, reduced: [], motion: { durations: {}, easings: {} }, zIndex: [], shadows: {}, grids: {}, widths: [], fonts: {}, usage: {} };

for (const label of COPIES) {
  for (const light of [false, true]) {
    const theme = light ? 'light' : 'dark';
    const meta = metaOf(label);
    const ctx = await newContext(browser, meta, light);
    const page = await openSnap(ctx, label, { light });
    const data = await page.evaluate(`(${readPage.toString()})().vars`);
    for (const [n, v] of Object.entries(data)) ((result.vars[n] ||= {})[theme] = v);
    if (label === 'home-dark' && !light) {
      const facts = await page.evaluate(() => {
        const rules = []; const fontFaces = [];
        const walk = (list, ctx) => { for (const r of list) { if (r.cssRules && !r.style) { const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText : r.cssText.split('{')[0].trim(); walk(r.cssRules, [...ctx, head]); continue; } if (r.type === CSSRule.FONT_FACE_RULE) { fontFaces.push({ family: r.style.getPropertyValue('font-family').replace(/["']/g, ''), weight: r.style.getPropertyValue('font-weight'), src: ((r.style.getPropertyValue('src').match(/url\("?([^")]+)/) || [])[1] || '').split('?')[0] }); continue; } if (!r.style) continue; rules.push({ sel: r.selectorText || '', ctx, css: r.style.cssText, z: r.style.zIndex, td: r.style.transitionDuration, tt: r.style.transitionTimingFunction, ad: r.style.animationDuration, at: r.style.animationTimingFunction, sh: r.style.boxShadow, mw: r.style.maxWidth || r.style.maxInlineSize, gtc: r.style.gridTemplateColumns }); if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText]); } };
        for (const ss of document.styleSheets) { try { walk(ss.cssRules, []); } catch {} }
        return { rules, fontFaces };
      });
      for (const r of facts.rules) {
        for (const c of r.ctx.filter((x) => x.startsWith('@media'))) result.media[c] = (result.media[c] || 0) + 1;
        if (r.ctx.some((x) => /prefers-reduced-motion/.test(x))) result.reduced.push({ media: r.ctx.find((x) => /prefers-reduced-motion/.test(x)), selector: r.sel.slice(0, 160), css: r.css.slice(0, 240) });
        for (const v of [r.td, r.ad].filter(Boolean)) for (const d of v.split(',')) { const k = d.trim(); if (k && k !== '0s') result.motion.durations[k] = (result.motion.durations[k] || 0) + 1; }
        for (const v of [r.tt, r.at].filter(Boolean)) for (const e of v.split(/,(?![^(]*\))/)) { const k = e.trim(); if (k) result.motion.easings[k] = (result.motion.easings[k] || 0) + 1; }
        if (r.z && r.z !== 'auto') result.zIndex.push({ z: r.z, selector: r.sel.slice(0, 140) });
        if (r.sh && r.sh !== 'none' && !/var\(/.test(r.sh)) (result.shadows[r.sh] ||= []).push(r.sel.slice(0, 120));
        if (r.sh && /var\(/.test(r.sh)) (result.shadows[r.sh] ||= []).push(r.sel.slice(0, 120));
        if (r.mw && !/^(100%|none|0|auto)$/.test(r.mw)) result.widths.push({ maxWidth: r.mw, selector: r.sel.slice(0, 120) });
        if (r.gtc && /project|grid/.test(r.sel)) (result.grids.rules ||= []).push({ selector: r.sel.slice(0, 120), media: r.ctx.filter((x) => x.startsWith('@media')).join(' '), value: r.gtc });
      }
      const fam = {};
      for (const f of facts.fontFaces) (fam[f.family] ||= { weights: new Set(), host: new Set() }), fam[f.family].weights.add(f.weight), fam[f.family].host.add((f.src.match(/^https?:\/\/([^/]+)/) || [])[1] || 'local');
      result.fonts.faces = Object.fromEntries(Object.entries(fam).map(([k, v]) => [k, { weights: [...v.weights], hosts: [...v.host] }]));
      result.fonts.stacks = await page.evaluate(() => {
        const o = {};
        for (const n of ['--nlm-font-family-sans', '--mat-sys-body-medium-font', '--mat-sys-title-large-font', '--mat-sys-headline-small-font', '--mat-sys-label-large-font']) o[n] = getComputedStyle(document.body).getPropertyValue(n).trim();
        o['body computed'] = getComputedStyle(document.body).fontFamily;
        o['h2.projects-header'] = (document.querySelector('h2.projects-header') && getComputedStyle(document.querySelector('h2.projects-header')).fontFamily) || null;
        o['code'] = getComputedStyle(Object.assign(document.body.appendChild(document.createElement('code')), { className: 'code' })).fontFamily;
        return o;
      });
      result.zIndexComputed = await page.evaluate(() => Object.fromEntries(['.cdk-overlay-container', '.boqOnegoogleliteOgbOneGoogleBar', 'page-header', 'header'].map((s) => [s, document.querySelector(s) ? getComputedStyle(document.querySelector(s)).zIndex : null])));
      // The notebook grid's columns at four widths.
      for (const w of [1440, 1024, 800, 390]) {
        await page.setViewportSize({ width: w, height: 900 });
        await page.waitForTimeout(300);
        result.grids[w] = await page.evaluate(() => { const g = document.querySelector('project-grid .project-buttons-flow, project-grid > div, .project-buttons-flow') || document.querySelector('project-grid'); if (!g) return null; const cs = getComputedStyle(g); const kids = [...g.children].filter((c) => c.getBoundingClientRect().width > 0); const tops = new Set(kids.map((c) => Math.round(c.getBoundingClientRect().top))); const firstRow = kids.filter((c) => Math.round(c.getBoundingClientRect().top) === Math.min(...tops)); return { node: g.tagName.toLowerCase() + '.' + String(g.className).split(' ')[0], display: cs.display, gridTemplateColumns: cs.gridTemplateColumns, gap: cs.gap, columnsInFirstRow: firstRow.length, cardWidth: kids[0] ? Math.round(kids[0].getBoundingClientRect().width) : null, padding: getComputedStyle(g.parentElement).paddingLeft }; });
      }
      await page.setViewportSize({ width: meta.w, height: meta.h });
    }
    // Colour, radius and size usage among visible elements.
    result.usage[`${label}/${theme}`] = await page.evaluate(() => {
      const u = { bg: {}, text: {}, border: {}, radius: {}, fontSize: {}, fontWeight: {} };
      const inc = (o, k) => { if (k) o[k] = (o[k] || 0) + 1; };
      for (const e of document.querySelectorAll('body *')) {
        const r = e.getBoundingClientRect();
        if (r.width < 1 || r.height < 1 || r.bottom < 0 || r.top > innerHeight) continue;
        const c = getComputedStyle(e);
        if (c.visibility !== 'visible') continue;
        if (c.backgroundColor !== 'rgba(0, 0, 0, 0)') inc(u.bg, c.backgroundColor);
        if ([...e.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim())) { inc(u.text, c.color); inc(u.fontSize, c.fontSize); inc(u.fontWeight, c.fontWeight); }
        if (parseFloat(c.borderTopWidth) > 0 && c.borderTopStyle !== 'none') inc(u.border, `${c.borderTopWidth} ${c.borderTopColor}`);
        if (c.borderTopLeftRadius !== '0px') inc(u.radius, c.borderTopLeftRadius);
      }
      const top = (o) => Object.fromEntries(Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, 25));
      return Object.fromEntries(Object.entries(u).map(([k, v]) => [k, top(v)]));
    });
    await ctx.close();
  }
}
await browser.close();
// Only the variables the tokens can use: NotebookLM's own (--nlm-*, --nb-*), the Google design
// system references they point at (--gds-*), and Angular Material's system roles (--mat-sys-*).
const keep = /^--(nlm|nb|gds|mat-sys)-/;
result.vars = Object.fromEntries(Object.entries(result.vars).filter(([k]) => keep.test(k)));
const vars = result.vars;
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({ _meta: result._meta, vars }, null, 1) + '\n');
delete result.vars;
result.reduced = result.reduced.slice(0, 200);
result.zIndex = Object.values(Object.fromEntries(result.zIndex.map((z) => [z.z + z.selector, z]))).sort((a, b) => +a.z - +b.z);
for (const k of Object.keys(result.shadows)) result.shadows[k] = [...new Set(result.shadows[k])].slice(0, 8);
result.widths = result.widths.slice(0, 80);
fs.writeFileSync(path.join(RAW, 'css-facts.json'), JSON.stringify(result, null, 1) + '\n');
console.log('vars', Object.keys(vars).length, 'media', Object.keys(result.media).length, 'reduced', result.reduced.length, 'z', result.zIndex.length);
