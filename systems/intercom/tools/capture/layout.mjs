// Reads layout geometry (shell, column widths, grids, sticky and fixed elements, section order) for each
// public page at 1440, 1920, 1024 and 390 wide and writes raw/layout.json. raw/pages.md is written from it.
// Adapted from the Gauth kit's public layout.mjs for intercom.com: no account pages, no lesson chrome —
// the shell is the shared header, the main column and the footer, plus the help center's docs nav.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, RAW, chromium, UA, UA_MOBILE, closePromo, patch } from './public/lib.mjs';

const paths = {
  home: '/', pricing: '/pricing', helpdesk: '/helpdesk', inbox: '/helpdesk/inbox',
  copilot: '/helpdesk/copilot', customers: '/customers', integrations: '/integrations',
  security: '/security', 'view-demos': '/view-demos', 'contact-sales': '/contact-sales',
  'why-choose': '/why-choose-intercom', enterprise: '/enterprise', blog: '/blog',
  help: '/help/en/', changes: '/changes/en',
};

function measure() {
  const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}\b/g, '');
  const R = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.left), y: Math.round(r.top + scrollY), w: Math.round(r.width), h: Math.round(r.height) }; };
  const tag = (e) => e.tagName.toLowerCase() + [...e.classList].map(strip).filter((c) => c && !/^(bg|text|flex|grid|block|hidden|relative|absolute|fixed|sticky|w-|h-|p-|m-|px-|py-|pt-|pb-|pl-|pr-|mt-|mb-|ml-|mr-|gap|items-|justify-|border|rounded|z-|col-|row-|overflow|inset|top-|bottom-|left-|right-|min-|max-)/.test(c)).slice(0, 2).map((c) => '.' + c).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, docH: document.documentElement.scrollHeight };
  const h1 = document.querySelector('h1'); out.h1 = h1 && { text: h1.innerText.slice(0, 50), font: getComputedStyle(h1).font.slice(0, 120), ...R(h1) };
  out.fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 120).map((e) => ({ el: tag(e), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, z: getComputedStyle(e).zIndex, ...R(e) })).slice(0, 12);
  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 400 && parseFloat(m) <= 1800; })
    .map((e) => ({ el: tag(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight, ...R(e) })).filter((o) => { const k = o.el + o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 12);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return (cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2) && R(e).w > 300; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), cols: cs.gridTemplateColumns, colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e) }; }).slice(0, 10);
  out.flexRows = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'flex' && cs.flexWrap === 'wrap' && R(e).w > 300 && e.children.length >= 3; })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), gap: cs.gap, ...R(e) }; }).slice(0, 6);
  const hd = document.querySelector('header'); out.header = hd && { el: tag(hd), bg: getComputedStyle(hd).backgroundColor, borderB: getComputedStyle(hd).borderBottomWidth + ' ' + getComputedStyle(hd).borderBottomColor, pos: getComputedStyle(hd).position, ...R(hd) };
  const nav = document.querySelector('header nav, nav'); out.nav = nav && { el: tag(nav), ...R(nav) };
  const main = document.querySelector('main') || document.body;
  out.main = { el: tag(main), ...R(main) };
  const ft = document.querySelector('footer'); out.footer = ft && { el: tag(ft), bg: getComputedStyle(ft).backgroundColor, ...R(ft), cols: ft.querySelectorAll('ul, [class*=col]').length };
  out.sections = [...main.querySelectorAll('section, [class*="Section"], [class*="section"]')].filter((e) => vis(e) && R(e).w > 300).map((e) => { const h = e.querySelector('h1,h2,h3'); return { el: tag(e), bg: getComputedStyle(e).backgroundColor, ...R(e), heading: h ? h.innerText.slice(0, 50).replace(/\n/g, ' ') : '' }; }).slice(0, 20);
  out.body = { font: getComputedStyle(document.body).fontFamily.slice(0, 90), size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color, bodyClass: document.body.className.slice(0, 120) };
  return out;
}

fs.mkdirSync(RAW, { recursive: true });
const res = fs.existsSync(path.join(RAW, 'layout.json'))
  ? JSON.parse(fs.readFileSync(path.join(RAW, 'layout.json'), 'utf8')) : {};
const save = () => fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(res, null, 1) + '\n');
let b = await chromium.launch();
// The CDN resets a session after a run of rapid loads; one fresh context per
// page plus a short gap keeps the whole map measurable. A page that still
// fails is retried once on a relaunched browser before it is skipped.
for (const [vw, vh, mob] of [[1440, 900, false], [1920, 1080, false], [1024, 768, false], [390, 844, true]]) {
  for (const [k, pth] of Object.entries(paths)) {
    if (vw !== 1440 && !/^(home|pricing|helpdesk|help|contact-sales|blog)$/.test(k)) continue;
    const key = `${k}@${vw}`;
    for (let attempt = 1; attempt <= 2; attempt++) {
      let ctx;
      try {
        ctx = await b.newContext({ viewport: { width: vw, height: vh }, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob });
        await patch(ctx);
        const p = await ctx.newPage();
        await p.goto(BASE + pth, { waitUntil: 'load', timeout: 90000 }); await p.waitForTimeout(6500);
        await closePromo(p);
        res[key] = await p.evaluate(measure);
        save();
        console.log(k, vw, attempt > 1 ? '(retry)' : '');
        break;
      } catch (e) {
        console.log('failed', k, vw, e.message.split('\n')[0]);
        if (attempt === 1) {
          // a dead context or crashed browser: relaunch before the retry
          try { await b.close(); } catch {}
          b = await chromium.launch();
          await new Promise((r) => setTimeout(r, 3000));
        }
      } finally {
        try { await ctx.close(); } catch {}
      }
    }
    await new Promise((r) => setTimeout(r, 1500));
  }
}
await b.close().catch(() => {});
save();
console.log('raw/layout.json', Object.keys(res).length, 'views');
