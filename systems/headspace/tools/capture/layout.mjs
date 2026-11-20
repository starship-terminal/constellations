// Reads layout geometry (header, hero, column widths, grids, sticky and fixed
// elements, inner scrollers) for headspace.com's public pages at 1440, 1920,
// 1024 and 390 wide and writes raw/layout.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
//
// Unlike an app shell the marketing pages scroll the document normally;
// docH records each page's real height and `scrollers` catches the rare inner
// pane (a carousel or the mobile nav sheet).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, ORG, RAW, chromium, UA, UA_MOBILE, closePromo, patch } from './public/lib.mjs';

const paths = {
  home: BASE + '/', app: BASE + '/app', meditation: BASE + '/meditation',
  mindfulness: BASE + '/mindfulness', sleep: BASE + '/sleep', therapy: BASE + '/online-therapy',
  coaching: BASE + '/coaching', ebb: BASE + '/ai-mental-health-companion',
  'mental-health': BASE + '/mental-health', anxiety: BASE + '/mental-health/anxiety',
  science: BASE + '/science', about: BASE + '/about-us', articles: BASE + '/articles',
  article: BASE + '/articles/can-you-use-hsa-or-fsa-for-mental-health',
  content: BASE + '/content', topic: BASE + '/content/topics/100',
  subscriptions: BASE + '/subscriptions', family: BASE + '/family-plan',
  gift: BASE + '/buy/gift', share: BASE + '/share-headspace', redeem: BASE + '/code',
  'mindful-families': BASE + '/app/mindful-families',
  'org-home': ORG + '/', 'org-employers': ORG + '/employers',
};

function measure() {
  const R = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) }; };
  const tag = (e) => e.tagName.toLowerCase() + (e.getAttribute('data-testid') ? `[data-testid=${e.getAttribute('data-testid')}]` : '') + [...e.classList].map(String).slice(0, 3).map((c) => '.' + c).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && !e.closest('[id*="onetrust" i]') && vis(e));
  const out = { vw: innerWidth, docH: document.documentElement.scrollHeight };
  const h1 = document.querySelector('main h1, h1'); out.h1 = h1 && { text: h1.innerText.slice(0, 60), font: getComputedStyle(h1).font.slice(0, 140), color: getComputedStyle(h1).color, ...R(h1) };
  // The fixed shell: header and anything else fixed/sticky wider than a button.
  out.fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 120).map((e) => ({ el: tag(e), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, z: getComputedStyle(e).zIndex, ...R(e) })).slice(0, 12);
  out.scrollers = all.filter((e) => { const cs = getComputedStyle(e); return (cs.overflowY === 'auto' || cs.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 200; })
    .map((e) => ({ el: tag(e), contentH: e.scrollHeight, ...R(e) })).sort((a, b) => b.contentH - a.contentH).slice(0, 6);
  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 400 && parseFloat(m) <= 1800; })
    .map((e) => ({ el: tag(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight, ...R(e) })).filter((o) => { const k = o.el + o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 12);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return (cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2) && R(e).w > 300; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), cols: cs.gridTemplateColumns.slice(0, 120), colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e) }; }).slice(0, 10);
  out.flexRows = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'flex' && cs.flexWrap === 'wrap' && R(e).w > 300 && e.children.length >= 3; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), gap: cs.gap, ...R(e) }; }).slice(0, 6);
  const hd = document.querySelector('header'); out.header = hd && { el: tag(hd), bg: getComputedStyle(hd).backgroundColor, borderB: getComputedStyle(hd).borderBottomWidth + ' ' + getComputedStyle(hd).borderBottomColor, ...R(hd) };
  const main = document.querySelector('main') || document.body;
  out.main = { el: tag(main), ...R(main) };
  out.sections = [...main.querySelectorAll('section, table')].filter((e) => vis(e) && R(e).w > 300).map((e) => { const h = e.querySelector('h1,h2,h3'); return { el: tag(e), bg: getComputedStyle(e).backgroundColor, ...R(e), heading: h ? h.innerText.slice(0, 50).replace(/\n/g, ' ') : '' }; }).slice(0, 16);
  const ft = document.querySelector('footer'); out.footer = ft && { el: tag(ft), bg: getComputedStyle(ft).backgroundColor, color: getComputedStyle(ft).color, ...R(ft) };
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
  for (const [k, url] of Object.entries(paths)) {
    if (vw !== 1440 && !/home|subscriptions|meditation|content|org-home/.test(k)) continue;
    if (res[`${k}@${vw}`]) { console.log('keep', k, vw); continue; }
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      try {
        await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }); await p.waitForTimeout(6500);
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
