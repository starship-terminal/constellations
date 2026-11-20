// Captures Allbirds' public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light). Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are dialog dismissals, the MEN/WOMEN
// mega-menu buttons, Search, a size chip, the header cart button and FAQ/product
// accordions. Add to Cart is never pressed (it writes a cart on the store's server).
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // An infinite or growing page reports a scrollHeight without end: tile at most 8 chunks
    // and log the boundary (the kit's cap), never one tile per chunk for ever.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// -- shared bits -------------------------------------------------------------
// Header mega-menu: the MEN/WOMEN buttons open a flyout on hover on desktop.
const openMenu = async (p) => {
  const btn = p.getByRole('button', { name: 'MEN', exact: true })
    .filter({ visible: true }).first();
  if (!(await btn.count())) return;
  await btn.hover(); await wait(p, 1200);
  const fly = p.locator('header a[href*="/collections/mens-"]').filter({ visible: true }).first();
  if (!(await fly.count())) { await btn.click(); await wait(p, 2000); }
};
const openSearch = async (p) => {
  const s = p.locator('header a[href$="/search"], header a[aria-label="Search"]')
    .filter({ visible: true }).first();
  if (await s.count()) { await s.click(); await wait(p, 1500); return true; }
  return false;
};
// PDP helpers: size chip, then the session-cart button (never checkout).
// Real clicks are tried first; a sticky buy bar can cover the element where
// Playwright scrolls it, so we fall back to dispatching el.click().
const clickEl = async (loc, ms = 10000) => {
  await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click()));
};
const pickSize = async (p) => {
  await closePromo(p);
  const chip = p.locator('button.btn-size:not(.disabled)').filter({ visible: true }).first();
  if (await chip.count()) { await clickEl(chip); await wait(p, 800); return true; }
  return false;
};
// Opens the cart drawer through the header cart button, never Add to Cart
// (state change: recorded as a boundary), so the drawer shown is the empty cart.
const addToCart = async (p) => {
  await closePromo(p);
  const b = p.locator('button[aria-label*="cart" i], a[aria-label*="cart" i], button:has-text("View cart")')
    .filter({ visible: true }).first();
  if (await b.count()) { await clickEl(b); await wait(p, 2500); return true; }
  return false;
};
const openAccordion = async (p) => {
  const a = p.locator('button[aria-expanded="false"], summary').filter({ visible: true }).first();
  if (await a.count()) { await clickEl(a); await wait(p, 800); return true; }
  return false;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await closePromo(p);
    await S.view('default');
    await step('menu', async () => { await openMenu(p); await S.view('menu'); await p.mouse.move(10, 10); await wait(p, 800); });
    await step('search', async () => { if (await openSearch(p)) { await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 600); } });
    await S.full();
  } },
  collection: { path: '/collections/mens', run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const f = p.getByRole('button', { name: /filter/i }).first();
      if (await f.count()) { await f.click({ timeout: 8000 }).catch(() => f.evaluate((el) => el.click())); await wait(p, 1200); await S.view('filter'); await p.keyboard.press('Escape'); await wait(p, 500); }
    });
    await step('sort', async () => {
      const s = p.getByRole('button', { name: /sort/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 800); await S.view('sort'); await p.keyboard.press('Escape'); await wait(p, 500); }
    });
    await S.full();
  } },
  product: { path: '/products/mens-tree-runner-nz-medium-grey', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('options', async () => { await pickSize(p); await S.view('options'); });
    await step('accordion', async () => { if (await openAccordion(p)) await S.view('accordion'); });
    await step('cart', async () => { if (await addToCart(p)) { await S.view('cart-drawer'); await p.keyboard.press('Escape'); await wait(p, 800); } });
    await S.full();
  } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); } },
  searchpage: { path: '/search', run: async (p, S) => { await S.view('default'); } },
  account: { path: '/account/login', run: async (p, S) => {
    await S.view('default');
    await step('focus', async () => { const i = p.locator('input[type="email"]').first(); if (await i.count()) { await i.click(); await wait(p, 500); await S.view('focus'); } });
  } },
  story: { path: '/pages/our-story', run: async (p, S) => { await S.view('default'); await S.full(); } },
  materials: { path: '/pages/materials', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/pages/help', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => { if (await openAccordion(p)) await S.view('faq'); });
    await S.full();
  } },
  blog: { path: '/blogs/the-perch', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await closePromo(p);
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button.header-mobile-menu, .header-mobile-menu button, header button[aria-label*="menu" i], header button[aria-expanded]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 800); }
    });
    await S.full();
  } },
  collection: { path: '/collections/mens', run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: { path: '/products/mens-tree-runner-nz-medium-grey', wait: 8000, run: async (p, S) => {
    await closePromo(p);
    await S.view('default');
    await step('options', async () => { await pickSize(p); await S.view('options'); });
    await step('cart', async () => { if (await addToCart(p)) await S.view('cart-drawer'); });
  } },
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') { await killGeo(p); await closePromo(p); }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
