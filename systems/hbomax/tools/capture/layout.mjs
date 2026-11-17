// Reads layout geometry (shell, column widths, grids, sticky and fixed elements, inner scrollers)
// for each public www.hbomax.com page at 1440, 1920, 1024 and 390 wide and writes raw/layout.json.
//
//   xvfb-run -a env PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
//
// The marketing pages scroll the document normally; the hero is a Bootstrap
// carousel and the "Discover" rows are horizontal rails. Headed under xvfb
// like the rest of the suite (Akamai 403s headless).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOCALE, RAW, chromium, UA, UA_MOBILE, closePromo, patch } from './public/lib.mjs';

const paths = {
  home: LOCALE, movies: LOCALE + '/movies', shows: LOCALE + '/shows',
  channel: LOCALE + '/channel',
  show: LOCALE + '/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf',
  movie: LOCALE + '/movie/710798da-f811-40be-9ed9-3a7443e36278',
  collection: LOCALE + '/collections/genre/kids-family',
  sitemap: LOCALE + '/sitemap', 'corp-info': LOCALE + '/corp-info',
  privacy: '/privacy',
};

function measure() {
  const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}\b/g, '');
  const R = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) }; };
  const tag = (e) => e.tagName.toLowerCase() + [...e.classList].map(strip).slice(0, 3).map((c) => '.' + c).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, docH: document.documentElement.scrollHeight, theme: document.documentElement.getAttribute('data-theme') || 'dark' };
  const h1 = document.querySelector('main h1'); out.h1 = h1 && { text: h1.innerText.slice(0, 50), font: getComputedStyle(h1).font.slice(0, 120), ...R(h1) };
  // The fixed shell: header, the page footer bar, and anything else fixed/sticky
  // wider than a button.
  out.fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 120).map((e) => ({ el: tag(e), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, z: getComputedStyle(e).zIndex, ...R(e) })).slice(0, 12);
  // The scrolling panes the shell is built from (article and sidebar) with the
  // content height each carries — docH alone would read 900 on every page.
  out.scrollers = all.filter((e) => { const cs = getComputedStyle(e); return (cs.overflowY === 'auto' || cs.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 200; })
    .map((e) => ({ el: tag(e), contentH: e.scrollHeight, ...R(e) })).sort((a, b) => b.contentH - a.contentH).slice(0, 6);
  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 400 && parseFloat(m) <= 1800; })
    .map((e) => ({ el: tag(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight, ...R(e) })).filter((o) => { const k = o.el + o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 12);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return (cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2) && R(e).w > 300; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), cols: cs.gridTemplateColumns, colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e) }; }).slice(0, 10);
  out.flexRows = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'flex' && cs.flexWrap === 'wrap' && R(e).w > 300 && e.children.length >= 3; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), gap: cs.gap, ...R(e) }; }).slice(0, 6);
  const side = document.querySelector('aside');
  out.sidebar = side && { el: tag(side), bg: getComputedStyle(side).backgroundColor, borderR: getComputedStyle(side).borderRightWidth + ' ' + getComputedStyle(side).borderRightColor, ...R(side) };
  const hd = document.querySelector('header'); out.header = hd && { el: tag(hd), bg: getComputedStyle(hd).backgroundColor, borderB: getComputedStyle(hd).borderBottomWidth + ' ' + getComputedStyle(hd).borderBottomColor, ...R(hd) };
  const main = document.querySelector('main') || document.body;
  out.main = { el: tag(main), ...R(main) };
  out.sections = [...main.querySelectorAll('section, [class*="-section"], [class*="section--"], table, .docs-search-modal')].filter((e) => vis(e) && R(e).w > 300).map((e) => { const h = e.querySelector('h1,h2,h3'); return { el: tag(e), bg: getComputedStyle(e).backgroundColor, ...R(e), heading: h ? h.innerText.slice(0, 50).replace(/\n/g, ' ') : '' }; }).slice(0, 16);
  // Keep the full font stack: truncating it mid-name produces an unterminated
  // string downstream (the truncated stack became core.font.family.primary).
  out.body = { font: getComputedStyle(document.body).fontFamily, size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color };
  return out;
}

const b = await chromium.launch({ headless: process.env.HEADLESS === '1' });
// Incremental by default: keys already measured in raw/layout.json are kept,
// so a flaky-network rerun only re-shoots what it missed. FULL=1 re-measures
// every key for a clean pass.
const OUT_JSON = path.join(RAW, 'layout.json');
const res = (!process.env.FULL && fs.existsSync(OUT_JSON)) ? JSON.parse(fs.readFileSync(OUT_JSON, 'utf8')) : {};
for (const [vw, vh, mob] of [[1440, 900, false], [1920, 1080, false], [1024, 768, false], [390, 844, true]]) {
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  for (const [k, pth] of Object.entries(paths)) {
    if (vw !== 1440 && !/home|movies|show$|sitemap/.test(k)) continue;
    if (res[`${k}@${vw}`]) { console.log('keep', k, vw); continue; }
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      try {
        await p.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 90000 }); await p.waitForTimeout(6500);
        await closePromo(p);
        res[`${k}@${vw}`] = await p.evaluate(measure);
        console.log(k, vw);
        ok = true;
      } catch (e) { console.log('failed', k, vw, `try${attempt + 1}`, e.message.split('\n')[0]); }
    }
  }
  await ctx.close();
}
await b.close();
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(OUT_JSON, JSON.stringify(res, null, 1) + '\n');
console.log('raw/layout.json', Object.keys(res).length, 'pages');
