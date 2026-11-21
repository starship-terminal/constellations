// Captures aloyoga.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is bought, sent or signed into: the only presses are local UI toggles — the mobile menu,
// the WOMEN mega-menu hover and a PDP colour swatch. The Osano consent dialog is hidden, never
// answered (no Accept/Reject/Save is ever clicked); the consent view is captured before it is hidden.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the consent dialog still up, as the page arrives.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
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

// Hover the first mega-nav item: WOMEN opens the category flyout in place.
const openMega = async (p) => {
  const m = p.locator('a.main-nav__item').filter({ visible: true }).first();
  if (await m.count()) { await m.hover(); await wait(p, 1500); return true; }
  return false;
};

// Search icon opens an in-page drawer. Never type into it and never submit.
const openSearch = async (p) => {
  const s = p.locator('#main-navbar-search-icon, button.mobile-search-button').filter({ visible: true }).first();
  if (!(await s.count())) return false;
  await clickEl(s);
  await wait(p, 1200);
  return true;
};

// Sort / filter triggers are local menus. Open and close; do not apply a filter
// and do not submit. A missing control is a gap, not a failure of the page.
const openSort = async (p) => {
  const s = p.locator('button').filter({ hasText: /^sort$/i }).filter({ visible: true }).first();
  if (!(await s.count())) return false;
  await s.scrollIntoViewIfNeeded().catch(() => {});
  await clickEl(s);
  await wait(p, 900);
  return true;
};

// A PDP colour swatch is a local selection toggle, never an add-to-bag.
const pickSwatch = async (p) => {
  const s = p.locator('button.SwatchUI.swatch:not(.active)').filter({ visible: true }).first();
  if (await s.count()) { await s.scrollIntoViewIfNeeded(); await clickEl(s); await wait(p, 1200); return true; }
  return false;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.raw('consent');                       // the Osano dialog as it arrives
    await S.view('default');
    await step('megamenu', async () => { if (await openMega(p)) await S.view('megamenu'); await p.mouse.move(20, 400); await wait(p, 600); });
    await step('search', async () => {
      if (await openSearch(p)) { await S.view('search'); await p.keyboard.press('Escape').catch(() => {}); await wait(p, 400); }
    });
    await S.full();
  } },
  'shop-women': { path: '/collections/womens-shop-all', run: async (p, S) => {
    await S.view('default');
    await step('sort', async () => { if (await openSort(p)) { await S.view('sort'); await p.keyboard.press('Escape').catch(() => {}); await wait(p, 400); } });
    await S.full();
  } },
  'shop-men': { path: '/collections/mens-shop-all', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'new-arrivals': { path: '/collections/new-arrivals', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/collections/womens-shop-all', run: async (p, S) => {
    // The PDP URL is discovered at run time: first product card on the shop grid.
    const href = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href*="/products/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
      return a ? a.getAttribute('href') : null;
    });
    if (!href) { log('  no product link found'); return; }
    await p.goto(new URL(href, 'https://www.aloyoga.com').toString(), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 8000);
    await S.view('default');
    await step('swatch', async () => { if (await pickSwatch(p)) await S.view('swatch'); });
    await S.full();
  } },
  'new-to-alo': { path: '/pages/new-to-alo', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { path: '/cart', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // Login wall only. The server redirects /account to /account/login. Never
  // type, never click Google or Apple, never submit.
  account: { path: '/account/login', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  shoes: { path: '/collections/shoes', run: async (p, S) => { await S.view('default'); await S.full(); } },
  atelier: { path: '/collections/summer-atelier', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'gift-guide': { path: '/pages/gift-guide', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/pages/help-center', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'size-guide': { path: '/pages/size-chart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  stores: { path: '/pages/stores', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'we-are-alo': { path: '/pages/we-are-alo', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button.hamburger, button.navbar__toggler.hamburger').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape').catch(() => {}); await wait(p, 500); }
    });
    await step('search', async () => {
      if (await openSearch(p)) { await S.view('search'); await p.keyboard.press('Escape').catch(() => {}); await wait(p, 400); }
    });
    await S.full();
  } },
  'shop-women': { path: '/collections/womens-shop-all', run: async (p, S) => { await S.view('default'); await S.full(); } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { path: '/collections/womens-shop-all', run: async (p, S) => {
    const href = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href*="/products/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
      return a ? a.getAttribute('href') : null;
    });
    if (!href) { log('  no product link found'); return; }
    await p.goto(new URL(href, 'https://www.aloyoga.com').toString(), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 7000);
    await S.view('default');
    await S.full();
  } },
  'gift-guide': { path: '/pages/gift-guide', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/pages/help-center', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
