// Reads page geometry from withjulienne.com's signed-out public pages.
//   PLAYWRIGHT=... node tools/capture/layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, UA, UA_MOBILE, RECIPE, COLLECTION, launch, patch, clearChallenge, closePromo } from './public/lib.mjs';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const PAGES = [
  ['home', '/'], ['discover', '/discover'], ['recipe', RECIPE],
  ['search', '/search?ingredients=apple'], ['collection', COLLECTION],
  ['team', '/team'], ['roadmap', '/roadmap'], ['shop', '/shop'],
  ['legal', '/privacy-policy'], ['signup', '/signup'], ['cookbook', '/cookbook'],
];

const read = () => {
  const region = (el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const cls = typeof el.className === 'string' ? el.className.trim().split(/\s+/).slice(0, 3).join('.') : '';
    return {
      node: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (cls ? '.' + cls : ''),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      position: cs.position, display: cs.display,
      columns: cs.display === 'grid' ? cs.gridTemplateColumns : undefined,
      zIndex: cs.zIndex !== 'auto' ? cs.zIndex : undefined,
    };
  };
  const vh = innerHeight;
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.bottom > -20 && r.top < vh + 40; };
  const fixed = [...document.querySelectorAll('*')].filter((el) => {
    const pos = getComputedStyle(el).position;
    return (pos === 'fixed' || pos === 'sticky') && el.getBoundingClientRect().width > 40 && el.getBoundingClientRect().height > 8;
  }).slice(0, 24).map(region);
  const landmarks = [...document.querySelectorAll('header, nav, main, footer, section, h1')].filter(vis).slice(0, 40).map(region);
  const grids = [...document.querySelectorAll('[class*="grid"]')].filter(vis).slice(0, 20).map(region);
  return {
    viewport: { w: innerWidth, h: vh, dpr: window.devicePixelRatio },
    htmlClass: document.documentElement.className,
    scrollHeight: document.documentElement.scrollHeight,
    landmarks, grids, fixed,
  };
};

const { browser } = await launch();
const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'getBoundingClientRect on live signed-out withjulienne.com at 1440x900 and 390x844. Nothing typed or submitted.',
  pages: {},
};
for (const [w, h, ua, tag] of [[1440, 900, UA, 'desktop'], [390, 844, UA_MOBILE, 'mobile']]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, userAgent: ua, locale: 'en-US', isMobile: tag === 'mobile', hasTouch: tag === 'mobile' });
  await patch(ctx);
  const p = await ctx.newPage();
  for (const [label, path_] of PAGES) {
    if (tag === 'mobile' && !['home', 'discover', 'recipe', 'team'].includes(label)) continue;
    try {
      await p.goto(BASE + path_, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await clearChallenge(p);
      await p.waitForTimeout(1600);
      await closePromo(p);
      out.pages[`${label}@${tag}`] = { url: BASE + path_, ...(await p.evaluate(read)) };
      console.log('ok', label, tag, out.pages[`${label}@${tag}`].viewport);
    } catch (e) {
      out.pages[`${label}@${tag}`] = { error: String(e.message).split('\n')[0] };
      console.log('FAIL', label, tag);
    }
  }
  await ctx.close();
}
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'layout.json'), JSON.stringify(out, null, 1) + '\n');
console.log('layout.json', Object.keys(out.pages).length);
await browser.close();
