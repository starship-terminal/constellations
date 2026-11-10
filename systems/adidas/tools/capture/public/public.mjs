// Captures aesop.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the Search
// disclosure, the Email sign up dialog, the My cart drawer, the burger menu and PDP accordions.
// The OneTrust consent SDK is aborted at request level (its banner never mounts; no consent button
// is ever clicked). The store served is the US site (Sites-aesop-us-Site).
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };
// A PDP is an SPA route (/pdp?articleId=<SKU>) resolved from the first tile on
// a /plp/ page in a throwaway context, then loaded directly.
const resolvePdp = async (browser, mobile) => {
  const ctx = await browser.newContext({ viewport: { width: mobile ? 390 : 1440, height: mobile ? 844 : 900 }, userAgent: mobile ? UA_MOBILE : UA, isMobile: mobile, hasTouch: mobile, locale: 'zh-CN' });
  await patch(ctx);
  const p = await ctx.newPage();
  let url = null;
  try {
    await p.goto(BASE + '/plp/sp_run_app_male', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(8000);
    url = await p.evaluate(() => {
      const a = document.querySelector('a[href*="/pdp"]');
      return a ? a.href : null;
    });
  } finally { await ctx.close(); }
  return url || BASE + '/pdp?articleId=JP1477';
};
const esc = async (p) => { await p.keyboard.press('Escape'); await wait(p, 800); };

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.locator('.icon-navigation_search_wechat_32, [class*="search" i].iconfont, [class*="search" i]').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1600); await S.view('search'); await esc(p); }
    });
    await step('nav-flyout', async () => {
      const nav = p.locator('.catalog-item-first-page').filter({ visible: true }).first();
      if (await nav.count()) { await nav.hover(); await wait(p, 1600); await S.view('nav-flyout'); await p.mouse.move(700, 500); }
    });
    await S.full();
  } },
  plp: { path: '/plp/sp_run_app_male', run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const b = p.locator('.label-1, [class*="filter" i], [class*="sort" i]').filter({ hasText: /筛选|排序|性别|全部/ }).filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1600); await S.view('filter'); await esc(p); }
    });
    await S.full();
  } },
  pdp: { resolve: (b) => resolvePdp(b, false), run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      const acc = p.locator('.lib-collapse-item, [class*="accordion" i] > *, [class*="collapse" i] > *').filter({ visible: true }).first();
      if (await acc.count()) { await clickEl(acc); await wait(p, 1200); await S.view('accordion'); }
    });
    await S.full();
  } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
};
const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.locator('[class*="hamburger" i], [class*="menu" i].iconfont, .iconfont').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1600); await S.view('menu'); await esc(p); }
    });
    await S.full();
  } },
  plp: { path: '/plp/sp_run_app_male', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { resolve: (b) => resolvePdp(b, true), run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'zh-CN' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const path = spec.resolve ? await spec.resolve(b) : spec.path;
    const target = path && path.startsWith('http') ? path : BASE + path;
    log('  ->', target);
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
