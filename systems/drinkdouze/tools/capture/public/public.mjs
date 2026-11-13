// Captures drinkdouze.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. drinkdouze.com is a
// Shopify storefront in French (the Impact-family theme plus douze-custom.css): it paints light
// only, as boxed rounded sections on a sable field. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates at 8 chunks and the
// log records the boundary. Nothing is bought, sent or signed into: the only presses are local UI
// toggles — the header newsletter toggle (opens the newsletter drawer, never submits it), the cart
// icon (opens the empty mini-cart drawer), the mobile menu and a variant swatch on the product
// page (a radio, never an add-to-cart). Any Klaviyo popup or consent overlay is hidden, never
// answered.
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
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('newsletter', async () => {
      // The header's envelope toggle opens the newsletter drawer — a local UI
      // state; the form inside is never filled or submitted.
      const t = p.locator('button[aria-controls="newsletter-popup"]').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); await S.view('newsletter'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await step('cart-drawer', async () => {
      // The cart icon opens the (empty) mini-cart drawer — a local UI state.
      const t = p.locator('a[aria-controls="mini-cart"]').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); await S.view('cart-drawer'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await S.full();
  } },
  shop: { path: '/collections/all', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { path: '/products/orange-sanguine-piment', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('variant', async () => {
      // Pick a different pack-size swatch: a radio inside the product form,
      // local UI state only — Ajouter-au-panier is never pressed.
      const v = p.locator('label.block-swatch__item').filter({ hasText: /12\s*CANETTES/i }).filter({ visible: true }).first();
      if (await v.count()) { await clickEl(v); await wait(p, 1500); await S.view('variant'); }
    });
    await S.full();
  } },
  trio: { path: '/products/trio-douze', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  story: { path: '/pages/notre-histoire', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  engagements: { path: '/pages/engagements', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faq: { path: '/pages/page-faq', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  locator: { path: '/pages/store-locator', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  abonnement: { path: '/pages/page-dabonnement', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  parrainage: { path: '/pages/parrainage', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  recipes: { path: '/blogs/recipes', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  recipe: { path: '/blogs/recipes/sirocco', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { path: '/cart', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/account/login', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  search: { path: '/search?q=douze', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The hamburger opens the mobile-navigation drawer — a local UI toggle.
      const m = p.locator('button[aria-controls="mobile-menu-drawer"]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  shop: { path: '/collections/all', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { path: '/products/orange-sanguine-piment', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'fr-FR' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
