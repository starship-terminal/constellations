// Reads page geometry from the locally-served Wayback pages and writes raw/layout.json:
// the content column, the layout grids, fixed/sticky layers, dialogs and menus, at
// 1440, 1920, 1024 and 390 wide. raw/pages.md is written by hand from it.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { servePages, open, launch, closePromo, RAW, SCRATCH, PAGES } from './public/lib.mjs';

const { srv, port } = await servePages(`${SCRATCH}/pages`, `${SCRATCH}/assets`);
const URLS = Object.fromEntries(Object.keys(PAGES).map((k) => [k, `http://127.0.0.1:${port}/pages/${k}.html`]));
const WIDTHS = [1440, 1920, 1024, 390];

function measure() {
  const R = (e) => { if (!e) return null; const r = e.getBoundingClientRect(); return { x: Math.round(r.left * 10) / 10, y: Math.round(r.top * 10) / 10, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10 }; };
  const vis = (e) => { if (!e) return false; const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility === 'visible' && cs.display !== 'none'; };
  const inVp = (e) => { const r = e.getBoundingClientRect(); return r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, vh: innerHeight };
  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 300 && parseFloat(m) <= 1800 && inVp(e); })
    .map((e) => ({ el: e.tagName.toLowerCase(), max: getComputedStyle(e).maxWidth, ...R(e) }))
    .filter((o) => { const k = o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 10);
  // the centred content column: the widest max-width-capped element in view
  const col = out.maxWidths.filter((o) => o.w > 0.5 * innerWidth).sort((a, b) => b.w - a.w)[0];
  out.main = col ? { x: col.x, w: col.w } : R(document.querySelector('main, [role=main], #main, .ltr-9h8nxx + *') || document.body);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2 && R(e).w > 200 && inVp(e); })
    .map((e) => { const cs = getComputedStyle(e); return { el: e.tagName.toLowerCase(), cols: cs.gridTemplateColumns, colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e) }; }).slice(0, 10);
  out.fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 100)
    .map((e) => ({ el: e.tagName.toLowerCase(), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, ...R(e) })).slice(0, 10);
  out.dialogs = [...document.querySelectorAll('[role=dialog]')].filter(vis).map((d) => ({ ...R(d), radius: getComputedStyle(d).borderTopLeftRadius }));
  out.menus = [...document.querySelectorAll('[role=menu], [role=listbox]')].filter(vis).map((d) => ({ ...R(d), items: d.querySelectorAll('[role^=menuitem], [role=option]').length }));
  out.body = { font: getComputedStyle(document.body).fontFamily.slice(0, 120), size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color };
  const head = document.querySelector('header, [data-component="TopBar"]');
  out.header = head && vis(head) ? R(head) : null;
  const form = document.querySelector('[data-testid="search-input"], [data-component="SearchInputContainer"]');
  out.searchForm = form ? R(form.closest('form') || form) : null;
  const card = document.querySelector('[data-testid="product-card"], [data-testid="productCard"], [data-component="ProductCard"]');
  out.resultCard = card ? R(card) : null;
  const list = document.querySelector('[data-testid="product-list-container"], [data-testid="showcase-layout"]');
  out.productGrid = list ? R(list) : null;
  return out;
}

const out = {};
for (const [label, url] of Object.entries(URLS)) {
  for (const w of WIDTHS) {
    const { browser, context } = await launch(w === 390 ? { mobile: true } : { width: w, height: 900 });
    const page = await context.newPage();
    await open(page, url, { wait: 5000 });
    await closePromo(page);
    out[`${label}@${w}`] = await page.evaluate(measure);
    console.log(label, w, 'main', JSON.stringify(out[`${label}@${w}`].main), 'grids', out[`${label}@${w}`].grids.length);
    await browser.close();
  }
}
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(out, null, 1) + '\n');
srv.close();
console.log('->', path.join(RAW, 'layout.json'));
