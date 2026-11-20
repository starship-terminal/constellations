// Captures helloklean.com's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// helloklean.com is a Shopify storefront (theme BF26 / Quickfire). It paints
// light only. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x.
// Nothing is bought or submitted. The only presses are local UI toggles:
// the nav menu, the cart drawer, a FAQ row, search, a product variant, and
// the mobile menu. Consent, newsletter and chat overlays are hidden, never
// answered. Checkout is never entered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'helloklean', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 600);
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
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/en-int', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /open menu/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 900); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await step('search', async () => {
      const b = p.getByRole('button', { name: /open search/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 800); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await step('cart', async () => {
      const b = p.getByRole('button', { name: /^cart$/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 900); await S.view('cart'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  shop: { path: '/en-int/collections/hello-klean-2-0', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  filters: { path: '/en-int/collections/filters', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  hair: { path: '/en-int/collections/haircare', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  product: { path: '/en-int/products/hello-klean-skin-filter', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('variant', async () => {
      const swatch = p.locator('input[type="radio"], [class*="swatch"] label, fieldset label').filter({ visible: true }).nth(1);
      if (await swatch.count()) { await swatch.click({ timeout: 4000 }).catch(() => {}); await wait(p, 800); await S.view('variant'); }
    });
    await S.full();
  } },
  shampoo: { path: '/en-int/products/full-cover-anti-thinning-hard-water-shampoo', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  about: { path: '/en-int/pages/about-us', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  faq: { path: '/en-int/pages/faqs', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await step('open', async () => {
      const row = p.locator('details summary, [class*="accordion"] button, [class*="faq"] button').filter({ visible: true }).first();
      if (await row.count()) { await row.click(); await wait(p, 700); await S.view('open'); }
    });
  } },
  subscription: { path: '/en-int/pages/hello-klean-subscription', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/en-int/pages/contact-us', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  water: { path: '/en-int/pages/check-your-water-quality', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  cart: { path: '/en-int/cart', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  login: { path: '/account/login', wait: 8000, run: async (p, S) => { await S.view('default'); } },
  search: { path: '/en-int/search?q=filter', wait: 6000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/en-int', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /open menu/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 900); await S.view('menu'); }
    });
    await S.full();
  } },
  shop: { path: '/en-int/collections/filters', wait: 6000, run: async (p, S) => { await S.view('default'); } },
  product: { path: '/en-int/products/hello-klean-skin-filter', wait: 7000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-GB' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 5000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
