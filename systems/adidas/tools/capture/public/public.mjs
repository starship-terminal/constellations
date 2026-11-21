// Captures adidas.com.cn's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the Search
// disclosure, the nav flyout, the filter rail and PDP accordions. There is no
// consent SDK on these routes. The store served is the China flagship (zh-CN, ¥).
import fs from 'fs';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, hideStaffDialog, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  // The storefront scrolls an inner shell, not the document. Walk that shell
  // so lazy tiles paint, then return it to the top.
  const shell = await p.evaluate(() => {
    const s = [...document.querySelectorAll('div')].find((el) => {
      const cs = getComputedStyle(el);
      const oy = cs.overflowY;
      return (oy === 'auto' || oy === 'scroll' || oy === 'hidden') && el.scrollHeight > el.clientHeight + 80 && el.clientHeight > 400 && el.getBoundingClientRect().width > 300;
    });
    if (!s) return { h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight), inner: false };
    s.setAttribute('data-m-shell', '1');
    return { h: s.scrollHeight, inner: true };
  });
  const h = shell.h;
  for (let y = 0; y < h; y += 600) {
    await p.evaluate((y) => {
      const s = document.querySelector('[data-m-shell]');
      if (s) s.scrollTop = y; else scrollTo(0, y);
    }, y);
    await wait(p, 200);
  }
  await p.evaluate(() => {
    const s = document.querySelector('[data-m-shell]');
    if (s) s.scrollTop = 0; else scrollTo(0, 0);
  });
  await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const shell = await p.evaluate(() => {
      const s = document.querySelector('[data-m-shell]');
      if (!s) return { inner: false, h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight), marked: false };
      return { inner: true, h: s.scrollHeight, marked: true, ch: s.clientHeight };
    });
    log('  shell', JSON.stringify(shell));
    const H = shell.h;
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    // Stage every tile under a .new name and swap it in only after the whole
    // shot succeeds, so a failed tile never truncates the previous capture.
    const staged = [];
    try {
      if (shell.inner) {
        // The document is one viewport tall and the header is sticky inside
        // the shell. Hide the header, scroll the shell by one content band,
        // and clip that band so the stitch is the page rather than repeated chrome.
        const band = await p.evaluate(() => {
          const header = document.querySelector('.navigation-warpper.showheaderBar, .pc-navigation-bar');
          const hh = header ? Math.round(header.getBoundingClientRect().height) : 0;
          if (header && hh > 0 && hh < 200) header.style.setProperty('visibility', 'hidden', 'important');
          const tab = document.querySelector('.lib-tab-bar');
          const tr = tab ? tab.getBoundingClientRect() : null;
          const th = tr && tr.height > 0 && tr.top < innerHeight ? Math.round(tr.height) : 0;
          if (tab && th) tab.style.setProperty('visibility', 'hidden', 'important');
          return { hh: hh > 0 && hh < 200 ? hh : 0, th, vh: window.innerHeight };
        });
        const stepY = Math.max(200, (band.vh || this.vh) - band.hh - band.th);
        const clip = { x: 0, y: band.hh, width: this.vw, height: Math.min(stepY, (band.vh || this.vh) - band.hh) };
        for (let i = 0, y = 0; y < hCap; i++, y += stepY) {
          await p.evaluate((yy) => { const s = document.querySelector('[data-m-shell]'); if (s) s.scrollTop = yy; }, y);
          await wait(p, 280);
          const remain = Math.min(clip.height, hCap - y);
          if (remain < 8) break;
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, clip: { ...clip, height: remain } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
          if (y + stepY >= hCap) break;
        }
        await p.evaluate(() => {
          document.querySelectorAll('.navigation-warpper, header, .lib-tab-bar').forEach((n) => n.style.removeProperty('visibility'));
        });
      } else if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) fs.existsSync(tmp) && fs.unlinkSync(tmp);
      throw e;
    }
    const finals = new Set(staged.map(([, final]) => path.basename(final)));
    for (const old of fs.readdirSync(RAW).filter((n) => (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png`) && !finals.has(n) && !n.includes('.new.'))) fs.unlinkSync(`${RAW}/${old}`);
    for (const [tmp, final] of staged) {
      if (tmp === final) continue;
      if (fs.existsSync(final) && path.resolve(tmp) !== path.resolve(final)) fs.unlinkSync(final);
      fs.renameSync(tmp, final);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => {
      const s = document.querySelector('[data-m-shell]');
      if (s) s.scrollTop = 0; else scrollTo(0, 0);
    }); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };
// The PDP is pinned to one SKU so the screenshot pass and the measurement
// pass (measure.mjs) always describe the same product.
const PDP = '/pdp?articleId=JP1477';
const esc = async (p) => { await p.keyboard.press('Escape'); await wait(p, 800); };

// A storefront page counts as loaded only when the navigation returned a real
// document: a failed or blank load must not overwrite the images on disk.
async function loadedOk(p, resp) {
  if (!resp || !resp.ok()) return false;
  return p.evaluate(() => !!(document.body && document.body.innerText && document.body.innerText.trim().length > 40)).catch(() => false);
}

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
  pdp: { path: PDP, run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      const acc = p.locator('.lib-collapse-item, [class*="accordion" i] > *, [class*="collapse" i] > *').filter({ visible: true }).first();
      if (await acc.count()) { await clickEl(acc); await wait(p, 1200); await S.view('accordion'); }
    });
    await S.full();
  } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  sitemap: { path: '/siteMap', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/my-account/privacy-statement', run: async (p, S) => { await S.view('default'); await S.full(); } },
  campaign: { path: '/splp?contentId=SPLP_NGuAJiSc', run: async (p, S) => { await S.view('default'); await S.full(); } },
  clp: { path: '/clp?contentId=904', run: async (p, S) => { await S.view('default'); await S.full(); } },
};
const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.locator('.search-bar-box').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1400); await S.view('search'); await esc(p); }
    });
    await S.full();
  } },
  plp: { path: '/plp/sp_run_app_male', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { path: PDP, run: async (p, S) => { await S.view('default'); await S.full(); } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  category: { path: '/category', run: async (p, S) => { await S.view('default'); await S.full(); } },
  account: { path: '/my-account', run: async (p, S) => { await S.view('default'); } },
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
    const target = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
    log('  ->', target);
    const resp = await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => null);
    if (!(await loadedOk(p, resp))) { log('  LOAD FAILED', name, '- keeping existing images'); await ctx.close(); continue; }
    await p.waitForTimeout(7000);
    await hideStaffDialog(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
