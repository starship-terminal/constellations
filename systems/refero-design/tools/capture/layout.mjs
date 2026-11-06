// Reads page geometry from Refero's live public pages (the 1440 x 900 ones and the
// 390 x 844 mobile ones) and writes raw/layout.json: the sidebar, the content pane
// and the research card on it, the h1 and section titles, every max-width container
// and grid, fixed and sticky layers, dialogs and menus, inner scrollers, and
// page-specific measures (the styles card grid pitch, the entity media frame, the
// promo card). raw/pages.md is written by hand from it. Adapted from the Manus kit.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node layout.mjs [page,page,...]
import path from 'node:path';
import { BASE, STYLES, launch, open, closePromo, firstStyleHref, RAW } from './public/lib.mjs';
import { updateReadings } from './readings.mjs';

const PAGES = [
  ['home', BASE + '/'],
  ['search', BASE + '/search'],
  ['apps', BASE + '/apps/search'],
  ['pricing', BASE + '/pricing'],
  ['mcp', BASE + '/mcp'],
  ['styles', STYLES + '/'],
  ['entity', 'ENTITY'], // first /style/<id> on the index
  ['mobile-home', BASE + '/', { mobile: true }],
  ['mobile-styles', STYLES + '/', { mobile: true }],
];
const want = (process.argv[2] || '').split(',').filter(Boolean);

function measure() {
  const R = (e) => { if (!e) return null; const r = e.getBoundingClientRect(); return { x: Math.round(r.left * 10) / 10, y: Math.round(r.top * 10) / 10, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10 }; };
  const cls = (e) => (typeof e.className === 'string' ? e.className : '');
  const tag = (e) => e.tagName.toLowerCase() + cls(e).split(/\s+/).filter((c) => c && !c.includes('[') && !c.includes(':') && !/^[A-Za-z][0-9A-Za-z]{4}$/.test(c)).slice(0, 3).map((c) => '.' + c).join('');
  const vis = (e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); if (!(r.width > 0 && r.height > 0 && cs.visibility === 'visible' && cs.display !== 'none')) return false; for (let n = e; n && n !== document.documentElement; n = n.parentElement) if (+getComputedStyle(n).opacity === 0) return false; return true; };
  const inVp = (e) => { const r = e.getBoundingClientRect(); return r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth; };
  const paints = (e) => { const cs = getComputedStyle(e); return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.boxShadow !== 'none' || parseFloat(cs.borderTopWidth) > 0; };
  const P = (e) => { for (let n = e; n && n !== document.documentElement; n = n.parentElement) if (paints(n)) return n; return null; };
  const F = (e) => { const c = getComputedStyle(e); return `${c.fontWeight} ${c.fontSize}/${c.lineHeight} ${c.fontFamily.split(',').slice(0, 2).join(',')}`; };
  const all = [...document.querySelectorAll('body *')].filter((e) => !e.closest('svg') && vis(e));
  const out = { vw: innerWidth, vh: innerHeight };

  // The shell: refero.design's fixed left rail; styles.refero's sticky header.
  const fixed = all.filter((e) => ['sticky', 'fixed'].includes(getComputedStyle(e).position) && R(e).w > 60);
  const side = fixed.filter((e) => { const r = R(e); return r.x <= 16 && r.h > 400 && r.w < 360; }).sort((a, b) => R(b).h - R(a).h)[0];
  out.sidebar = side && { el: tag(side), ...R(side), bg: getComputedStyle(side).backgroundColor };
  const foot = fixed.filter((e) => { const r = R(e); return r.y + r.h >= innerHeight - 4 && r.x <= 60 && e !== side; }).sort((a, b) => R(a).w - R(b).w)[0];
  out.sidebarFoot = foot && { el: tag(foot), ...R(foot) };
  const head = [...document.querySelectorAll('header')].find(vis) || fixed.find((e) => { const r = R(e); return r.y <= 2 && r.w > innerWidth - 200 && r.h < 120; });
  out.header = head ? { el: tag(head), pos: getComputedStyle(head).position, bg: getComputedStyle(head).backgroundColor, backdrop: getComputedStyle(head).backdropFilter, ...R(head) } : null;
  out.ground = getComputedStyle(document.body).backgroundColor;
  const h1 = [...document.querySelectorAll('h1')].find(vis);
  out.h1 = h1 && { text: h1.innerText.slice(0, 60), font: F(h1), ...R(h1) };
  const h2s = [...document.querySelectorAll('h2')].filter(vis);
  out.h2 = h2s.slice(0, 3).map((e) => ({ text: e.innerText.slice(0, 40), font: F(e), ...R(e) }));

  // The research card: the painted ancestor of the prompt field.
  const ta = [...document.querySelectorAll('textarea, [contenteditable=true], input[type=text], input:not([type])')].find(vis);
  if (ta) {
    const box = P(ta);
    out.research = { field: R(ta), box: box && R(box), radius: box && getComputedStyle(box).borderTopLeftRadius, shadow: box && getComputedStyle(box).boxShadow.slice(0, 200), chips: [...(box || ta.parentElement).querySelectorAll('button,[role=button],a')].filter(vis).slice(0, 8).map((b) => (b.innerText || '').trim().slice(0, 24)) };
  }

  const seen = new Set();
  out.maxWidths = all.filter((e) => { const m = getComputedStyle(e).maxWidth; return /px$/.test(m) && parseFloat(m) >= 300 && parseFloat(m) <= 1800 && inVp(e); })
    .map((e) => ({ el: tag(e), max: getComputedStyle(e).maxWidth, padL: getComputedStyle(e).paddingLeft, padR: getComputedStyle(e).paddingRight, ...R(e) })).filter((o) => { const k = o.max + o.x + o.w; if (seen.has(k)) return false; seen.add(k); return true; }).slice(0, 12);
  out.grids = all.filter((e) => { const cs = getComputedStyle(e); return cs.display === 'grid' && cs.gridTemplateColumns.split(' ').length >= 2 && R(e).w > 200 && inVp(e); })
    .map((e) => { const cs = getComputedStyle(e); return { el: tag(e), cols: cs.gridTemplateColumns, colGap: cs.columnGap, rowGap: cs.rowGap, ...R(e), firstChild: R(e.firstElementChild) }; }).slice(0, 10);
  out.fixed = fixed.map((e) => ({ el: tag(e), pos: getComputedStyle(e).position, top: getComputedStyle(e).top, bottom: getComputedStyle(e).bottom, z: getComputedStyle(e).zIndex, ...R(e), text: (e.innerText || '').trim().slice(0, 60) })).slice(0, 14);
  out.dialogs = [...document.querySelectorAll('[role=dialog]')].filter(vis).map((d) => ({ el: tag(d), ...R(d), radius: getComputedStyle(d).borderTopLeftRadius, bg: getComputedStyle(d).backgroundColor }));
  out.menus = [...document.querySelectorAll('[role=menu],[role=listbox]')].filter(vis).map((d) => ({ el: tag(d), ...R(d), radius: getComputedStyle(d).borderTopLeftRadius, items: d.querySelectorAll('[role^=menuitem],[role=option]').length }));
  out.scrollers = all.filter((e) => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20).map((e) => ({ el: tag(e), ...R(e), scrollHeight: e.scrollHeight, scrollTop: Math.round(e.scrollTop) })).slice(0, 8);
  out.body = { font: getComputedStyle(document.body).fontFamily.slice(0, 120), size: getComputedStyle(document.body).fontSize, bg: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color };

  // Page-specific measures.
  const cards = [...document.querySelectorAll('a[href^="/style/"]')].filter((a) => vis(a) && R(a).w > 80);
  if (cards.length > 1) out.styleCards = { count: cards.length, first: R(cards[0]), second: R(cards[1]), pitchY: Math.round((R(cards[1]).y - R(cards[0]).y) * 10) / 10 || null, pitchX: Math.round((R(cards[1]).x - R(cards[0]).x) * 10) / 10 || null, favicon: R(cards[0].querySelector('img:last-of-type')) };
  const v = [...document.querySelectorAll('video')].find(vis);
  if (v) out.video = { ...R(v), frame: R(P(v)), radius: P(v) && getComputedStyle(P(v)).borderTopLeftRadius };
  const promo = fixed.find((e) => /MCP/i.test(e.innerText || '') && R(e).w < 560 && R(e).y > 150);
  if (promo) out.promoCard = { el: tag(promo), ...R(promo), radius: getComputedStyle(promo).borderTopLeftRadius, shadow: getComputedStyle(promo).boxShadow.slice(0, 160) };
  const rows = [...document.querySelectorAll('main li, main tr')].filter((e) => vis(e) && e.querySelector('time') && inVp(e));
  if (rows.length > 1) out.listRow = { el: tag(rows[0]), first: R(rows[0]), pitch: Math.round((R(rows[1]).y - R(rows[0]).y) * 10) / 10, count: rows.length };
  return out;
}

// Merged into the existing file (readings.mjs): a run limited to some pages, or one where a page
// fails, keeps the other pages' readings instead of writing a file with only what this run measured.
const OUT = path.join(RAW, 'layout.json');
// resolve the entity page once
let entity = null;
{
  const l = await launch();
  const p = await l.context.newPage();
  entity = await firstStyleHref(p);
  await l.browser.close();
}
const jobs = [];
for (const [label, url0, opts] of PAGES) {
  if (want.length && !want.includes(label)) continue;
  const url = url0 === 'ENTITY' ? (entity ? STYLES + entity : null) : url0;
  if (!url) { console.log('skip', label, '(no /style/ link)'); continue; }
  jobs.push([`${label}@${opts?.mobile ? 390 : 1440}`, async () => {
    const l = await launch({ mobile: !!opts?.mobile });
    try {
      const p = await l.context.newPage();
      await open(p, url, { wait: url.includes('/style/') ? 8000 : 6000 });
      return { label, url: url.replace(/\/style\/[0-9a-z-]+/, '/style/<id>'), ...(await p.evaluate(measure)) };
    } finally {
      await l.browser.close();
    }
  }]);
}
const res = await updateReadings(OUT, jobs);
console.log('raw/layout.json', Object.keys(res).length, 'pages');
