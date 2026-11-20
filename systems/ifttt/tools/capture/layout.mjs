// Reads layout geometry (shell, column widths, grids, sticky and fixed
// elements, inner scrollers) for each public IFTTT page at 1440, 1920, 1024
// and 390 wide and writes raw/layout.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
//
// IFTTT's signed-out pages scroll the document; there is no inner overflow
// pane on the captured surfaces, but scrollers are still recorded so a
// shell change shows up in the raw file.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, HOME, RAW, chromium, UA, UA_MOBILE, closePromo, patch } from './public/lib.mjs';

const paths = {
  home: HOME + '/',
  explore: BASE + '/explore',
  'explore-services': BASE + '/explore/services',
  plans: BASE + '/plans',
  'service-twitter': BASE + '/twitter',
  applet: BASE + '/applets/A38TqjpD-start-irobot-cleaning-when-you-leave-home',
  connect: BASE + '/connect/discord/instagram',
  'solutions-productivity': BASE + '/solutions/productivity',
  mcp: BASE + '/mcp',
  about: BASE + '/about',
  careers: BASE + '/careers',
  terms: BASE + '/terms',
};

function measure() {
  const R = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) }; };
  const tag = (e) => e.tagName.toLowerCase() + [...e.classList].slice(0, 3).map((c) => '.' + String(c)).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, docH: document.documentElement.scrollHeight, bodyBg: getComputedStyle(document.body).backgroundColor };
  const h1 = document.querySelector('main h1, h1'); out.h1 = h1 && { text: h1.innerText.slice(0, 60), font: getComputedStyle(h1).font.slice(0, 140), ...R(h1) };
  // The fixed/sticky layers: the unified header, the Back pill, the share
  // wrapper and anything else fixed wider than a button.
  out.fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 100).map((e) => ({ el: tag(e), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, z: getComputedStyle(e).zIndex, ...R(e) })).slice(0, 12);
  out.scrollers = all.filter((e) => { const cs = getComputedStyle(e); return (cs.overflowY === 'auto' || cs.overflowY === 'scroll') && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 200; })
    .map((e) => ({ el: tag(e), contentH: e.scrollHeight, ...R(e) })).sort((a, b) => b.contentH - a.contentH).slice(0, 6);
  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 400 && parseFloat(m) <= 1800; })
    .map((e) => ({ el: tag(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight, ...R(e) })).filter((o) => { const k = o.el + o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 12);
  // `.container` is IFTTT's page column — record the real ones even when
  // max-width is not set (a fixed width instead).
  out.containers = all.filter((e) => e.classList && [...e.classList].some((c) => c === 'container')).filter(vis)
    .map((e) => ({ el: tag(e), ...R(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight })).slice(0, 10);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return (cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2) && R(e).w > 300; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), cols: cs.gridTemplateColumns, colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e) }; }).slice(0, 10);
  out.flexRows = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'flex' && cs.flexWrap === 'wrap' && R(e).w > 300 && e.children.length >= 3; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), gap: cs.gap, ...R(e) }; }).slice(0, 6);
  const hd = document.querySelector('header.unified-header') || document.querySelector('header');
  out.header = hd && { el: tag(hd), bg: getComputedStyle(hd).backgroundColor, cls: hd.className, ...R(hd) };
  out.sections = [...document.querySelectorAll('main section, section, .container')].filter((e) => vis(e) && R(e).w > 300 && R(e).h > 100).map((e) => { const h = e.querySelector('h1,h2,h3'); return { el: tag(e), bg: getComputedStyle(e).backgroundColor, ...R(e), heading: h ? h.innerText.slice(0, 50).replace(/\n/g, ' ') : '' }; }).slice(0, 16);
  out.body = { font: getComputedStyle(document.body).fontFamily.slice(0, 120), size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color };
  return out;
}

const b = await chromium.launch();
// Incremental by default: keys already measured in raw/layout.json are kept,
// so a flaky-network rerun only re-shoots what it missed. FULL=1 re-measures
// every key for a clean pass.
const OUT_JSON = path.join(RAW, 'layout.json');
const res = (!process.env.FULL && fs.existsSync(OUT_JSON)) ? JSON.parse(fs.readFileSync(OUT_JSON, 'utf8')) : {};
for (const [vw, vh, mob] of [[1440, 900, false], [1920, 1080, false], [1024, 768, false], [390, 844, true]]) {
  const ctx = await b.newContext(mob
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  for (const [name, url] of Object.entries(paths)) {
    const key = `${name}@${vw}`;
    if (res[key]) { console.log('keep', key); continue; }
    const p = await ctx.newPage();
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(6000);
      await closePromo(p);
      res[key] = { url, ...(await p.evaluate(measure)) };
      console.log('measured', key, 'docH', res[key].docH);
    } catch (e) { console.log('failed', key, e.message.split('\n')[0]); }
    await p.close();
  }
  await ctx.close();
}
await b.close();
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(OUT_JSON, JSON.stringify(res, null, 1) + '\n');
console.log('raw/layout.json', Object.keys(res).length, 'page/width pairs');
