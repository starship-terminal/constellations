// Computed styles read headless from the 2026-10 page copies (written by unsnap.py), for the
// parts the live pass did not reach: the lesson report form's popover, the phone tab bar and top
// bar, the compact sidebar. Usage: PLAYWRIGHT=... SNAPS=... node measure-copies.mjs > raw/2026-10/copy-measurements.json
import fs from 'node:fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const { routeCdn, FONTS } = await import('./lib.mjs');
const SNAPS = process.env.SNAPS;
const P = ['width', 'height', 'background-color', 'color', 'border-top-width', 'border-top-color', 'border-right-width', 'border-bottom-width', 'border-top-left-radius', 'box-shadow', 'padding-top', 'padding-left', 'gap', 'z-index', 'position', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'display'];
// One spec per copy: name -> a function source run in the page that returns elements.
const SPECS = {
  'lesson-dark-report-form-checked': { popover: "(() => { let n = document.querySelector('input[type=checkbox]'); while (n && !(parseFloat(getComputedStyle(n).borderTopLeftRadius) >= 10 && getComputedStyle(n).backgroundColor !== 'rgba(0, 0, 0, 0)')) n = n.parentElement; return n; })()", checkboxChecked: "document.querySelectorAll('input[type=checkbox]')[5]", checkbox: "document.querySelector('input[type=checkbox]')", textarea: "document.querySelector('textarea')", label: "document.querySelector('label')" },
  'lesson-light-report-form-checked': { popover: "(() => { let n = document.querySelector('input[type=checkbox]'); while (n && !(parseFloat(getComputedStyle(n).borderTopLeftRadius) >= 10 && getComputedStyle(n).backgroundColor !== 'rgba(0, 0, 0, 0)')) n = n.parentElement; return n; })()", checkboxChecked: "document.querySelectorAll('input[type=checkbox]')[5]", checkbox: "document.querySelector('input[type=checkbox]')", textarea: "document.querySelector('textarea')" },
  'learn-light-phone': { topBar: "document.querySelector('._3sbzq')", tabBar: "document.querySelector('._1p0jQ')", tabBarInner: "document.querySelector('._1p0jQ > *')" },
  'learn-dark-phone': { topBar: "document.querySelector('._3sbzq')", tabBar: "document.querySelector('._1p0jQ')", tabBarInner: "document.querySelector('._1p0jQ > *')" },
  'learn-light-tablet': { sidebar: "document.querySelector('._3P5E_')", navItem: "document.querySelector('[data-test=\"home-nav\"]')", navIcon: "document.querySelector('[data-test=\"home-nav\"] img')" },
  'user-search-light-no-results': { message: "[...document.querySelectorAll('*')].find((e) => e.children.length === 0 && /didn.t find/.test(e.textContent))", field: "document.querySelector('form')" },
};
const b = await chromium.launch();
const out = { _meta: { source: 'headless computed styles from the 2026-10-17 page copies (tools/capture/signed-in/measure-copies.mjs)' } };
for (const [label, specs] of Object.entries(SPECS)) {
  const meta = JSON.parse(fs.readFileSync(`${SNAPS}/${label}.json`, 'utf8'));
  const ctx = await b.newContext({ viewport: { width: meta.w, height: meta.h } });
  await routeCdn(ctx);
  const p = await ctx.newPage();
  await p.goto(`file://${SNAPS}/${label}.html`, { waitUntil: 'load', timeout: 60000 });
  await p.addStyleTag({ content: FONTS });
  await p.waitForTimeout(1500);
  out[label] = {};
  for (const [name, src] of Object.entries(specs)) {
    out[label][name] = await p.evaluate(({ src, P }) => {
      const e = eval(src); if (!e) return null;
      const c = getComputedStyle(e); const r = e.getBoundingClientRect(); const o = { rect: [r.x, r.y, r.width, r.height].map(Math.round) };
      for (const k of P) o[k] = c.getPropertyValue(k);
      for (const ps of ['::before', '::after']) { const pc = getComputedStyle(e, ps); if (pc.content !== 'none' && pc.content !== 'normal') o[ps] = Object.fromEntries(P.map((k) => [k, pc.getPropertyValue(k)])); }
      return o;
    }, { src, P });
  }
  await ctx.close();
}
await b.close();
console.log(JSON.stringify(out, null, 1));
