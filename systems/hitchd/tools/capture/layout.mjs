// Reads page geometry from hitchd.com's signed-out public pages — the
// regions, grids, fixed/sticky layers, dialogs and scroll containers — and
// writes raw/layout.json. Companion to the screenshots: this is the
// measurable half of "what is on the page".
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/layout.mjs
//
// Public route: live pages in a plain headless context, 1440 x 900 and
// 390 x 844. Nothing is clicked, typed or submitted; the gift modal is
// opened by its own card's tap (a local UI toggle) and read at rest.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, UA_MOBILE, launch, patch, clearChallenge, openRegistry } from './public/lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const PAGES = [
  ['home', '/'], ['login', '/login'], ['signup', '/signup'], ['forgot-password', '/forgot-password'],
  ['blog', '/blog'], ['post', '/blog/what-is-a-honeymoon-registry'], ['terms', '/terms'], ['privacy', '/privacy'],
  ['trips', '/trips/australia'], ['guide', '/guides/add-hitchd-to-knot-wedding-webiste'], ['registry', '/zoeandnoah'],
];

// `read` is serialized into the page, so every helper it uses must live inside it.
const read = () => {
  const region = (el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return { node: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.') : ''), rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) }, position: cs.position, display: cs.display, columns: cs.display === 'grid' ? cs.gridTemplateColumns : undefined, zIndex: cs.zIndex !== 'auto' ? cs.zIndex : undefined };
  };
  const vh = innerHeight, vw = innerWidth;
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.bottom > -r.height && r.top < vh + r.height; };
  const fixed = [...document.querySelectorAll('*')].filter((el) => { const p = getComputedStyle(el).position; return (p === 'fixed' || p === 'sticky') && el.getBoundingClientRect().width > 0; }).slice(0, 30).map(region);
  const scrollers = [...document.querySelectorAll('*')].filter((el) => el.scrollHeight > el.clientHeight + 8 && /(auto|scroll)/.test(getComputedStyle(el).overflowY)).slice(0, 20).map((el) => ({ ...region(el), scrollH: el.scrollHeight, clientH: el.clientHeight }));
  const landmarks = [...document.querySelectorAll('header, nav, main, footer, section, article, [role="dialog"], [role="navigation"], [role="main"], [role="contentinfo"], [role="banner"]')].filter(vis).slice(0, 60).map(region);
  const grids = [...document.querySelectorAll('.row, [class*="grid" i], .gift-list, ol, ul')].filter(vis).slice(0, 40).map(region);
  return { viewport: { w: vw, h: vh }, scrollHeight: document.documentElement.scrollHeight, landmarks, grids, fixed, scrollers, dialogs: [...document.querySelectorAll('[role="dialog"], .gift-modal, .modalDialog')].filter(vis).map(region) };
};

const { browser } = await launch();
const out = { readAt: new Date().toLocaleDateString('en-CA'), source: 'getBoundingClientRect + computed positions read in live headless Chromium on the signed-out public pages below, at 1440 x 900 and 390 x 844; nothing clicked or submitted', pages: {} };
for (const [w, h, ua, tag] of [[1440, 900, UA, 'desktop'], [390, 844, UA_MOBILE, 'mobile']]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, userAgent: ua });
  await patch(ctx);
  const p = await ctx.newPage();
  for (const [label, path_] of PAGES) {
    try {
      if (label === 'registry') {
        // the guest registry is an Angular app whose data fetch stalls on
        // some loads — share measure.mjs's painted-wait (a nonzero-size
        // .giftz tile) instead of reading a fixed-sleep shell
        const painted = await openRegistry(p);
        if (!painted) { out.pages[`${label}@${tag}`] = { blocked: 'gift list never painted' }; continue; }
      } else {
        await p.goto(BASE + path_, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        if (!(await clearChallenge(p))) { out.pages[`${label}@${tag}`] = { blocked: 'bot challenge' }; continue; }
        await p.waitForTimeout(7000);
      }
      out.pages[`${label}@${tag}`] = { url: BASE + path_, ...(await p.evaluate(read)) };
      console.log('ok', label, tag);
    } catch (e) { out.pages[`${label}@${tag}`] = { error: String(e.message).split('\n')[0] }; console.log('FAIL', label, tag); }
  }
  await ctx.close();
}
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'layout.json'), JSON.stringify(out, null, 1) + '\n');
console.log('layout.json:', Object.keys(out.pages).length, 'page passes');
await browser.close();
