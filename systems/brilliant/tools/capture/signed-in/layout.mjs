// Page geometry from the 2026-10-17 page copies: every visible CSS grid (its resolved columns and
// gap), the widest content column, and the fixed header, per copy and width.
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=~/.design-systems/snaps/brilliant node tools/capture/signed-in/layout.mjs
// Writes raw/layout.json. Adapted from the kit's generic layout reader (tools/kit/capture/layout.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { chromium, RAW, openSnap, newContext, metaOf } from './lib.mjs';

const COPIES = ['home-dark-default', 'courses-dark-default', 'you-dark-empty', 'settings-dark-account', 'settings-dark-preferences', 'koji-dark-default', 'mobile-home-dark-default', 'mobile-courses-dark-default', 'mobile-you-dark-empty', 'mobile-settings-dark-account'];
const b = await chromium.launch();
const out = { _meta: { source: 'Computed layout of the 2026-10-17 page copies, headless, at the captured viewport (1440x900; mobile-* 390x844).' } };
for (const copy of COPIES) {
  const meta = metaOf(copy);
  const ctx = await newContext(b, meta);
  const page = await openSnap(ctx, copy);
  out[copy] = await page.evaluate(() => {
    const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 40 && r.height > 20; };
    const name = (e) => (e.getAttribute('data-slot') || e.tagName.toLowerCase()) + (e.getAttribute('aria-label') ? `[${e.getAttribute('aria-label')}]` : '');
    const grids = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).display.includes('grid') && vis(e)).map((e) => {
      const cs = getComputedStyle(e); const r = e.getBoundingClientRect();
      return { el: name(e), x: Math.round(r.x), width: Math.round(r.width), columns: cs.gridTemplateColumns, count: cs.gridTemplateColumns.split(' ').filter((t) => /px/.test(t)).length, gap: cs.columnGap + ' / ' + cs.rowGap };
    });
    const header = [...document.querySelectorAll('header, nav')].map((e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return { el: name(e), height: Math.round(r.height), position: cs.position, top: Math.round(r.top), width: Math.round(r.width) }; }).filter((h) => h.width > 200);
    const main = document.querySelector('main');
    const cols = [...(main || document.body).querySelectorAll('*')].filter((e) => { const cs = getComputedStyle(e); return cs.maxWidth !== 'none' && vis(e); }).map((e) => ({ el: name(e), maxWidth: getComputedStyle(e).maxWidth, width: Math.round(e.getBoundingClientRect().width), x: Math.round(e.getBoundingClientRect().x) })).filter((c) => c.width > 300).slice(0, 6);
    return { viewport: innerWidth + 'x' + innerHeight, header, contentColumns: cols, grids };
  });
  await ctx.close();
  console.log(copy, out[copy].grids.length, 'grids');
}
await b.close();
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(out, null, 1) + '\n');
