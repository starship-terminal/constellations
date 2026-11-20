// Reads layout geometry (nav, fixed/sticky elements, grids, inner scrollers,
// section bands, containers) for each public joinhandshake.com page at 1440,
// 1920, 1024 and 390 wide and writes raw/layout.json. raw/pages.md was
// written from it.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
//
// The marketing pages scroll the document (docH records each page's full
// height); the fixed pill nav sits over it and the Ketch banner pins to the
// top when it appears. app.joinhandshake.com/access is measured too when its
// Cloudflare challenge clears — a run where it does not leaves earlier rows
// alone (incremental keeps keys already measured).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP_URL, RAW, chromium, UA, UA_MOBILE, closePromo, clearChallenge, patch } from './public/lib.mjs';

const paths = {
  home: '/', students: '/students/', employers: '/employers/', pricing: '/employers/pricing/',
  'request-more-info': '/employers/request-more-info/', 'career-centers': '/career-centers/',
  careers: '/careers/', blog: '/blog/', legal: '/legal/tos/', about: '/about/', ai: '/ai/',
  learn: '/learn/', access: APP_URL,
};

function measure() {
  const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}\b/g, '');
  const R = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) }; };
  const tag = (e) => e.tagName.toLowerCase() + [...e.classList].map(strip).slice(0, 3).map((c) => '.' + c).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, docH: document.documentElement.scrollHeight, theme: document.documentElement.classList.contains('dark') ? 'dark' : 'light' };
  // The responsive templates ship a hidden h1 copy for each breakpoint; the
  // probe wants the one that actually paints.
  const h1 = [...document.querySelectorAll('main h1')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; }); out.h1 = h1 && { text: h1.innerText.slice(0, 50), font: getComputedStyle(h1).font.slice(0, 120), ...R(h1) };
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
  out.body = { font: getComputedStyle(document.body).fontFamily.slice(0, 90), size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color };
  return out;
}

const b = await chromium.launch();
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
    if (vw !== 1440 && !/home|employers|pricing|students|access/.test(k)) continue;
    if (res[`${k}@${vw}`]) { console.log('keep', k, vw); continue; }
    let ok = false;
    for (let attempt = 0; attempt < 4 && !ok; attempt++) {
      try {
        const url = pth.startsWith('http') ? pth : BASE + pth;
        await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }); await p.waitForTimeout(6500);
        if (!(await clearChallenge(p, { tries: 4, step: 1500 }))) { console.log('blocked', k, vw, `try${attempt + 1}`); continue; }
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
