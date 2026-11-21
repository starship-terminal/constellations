// Captures teenage.engineering public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// The site paints one theme (html[data-theme=default]). Desktop 1440x900 at 1x,
// phone 390x844 at 2x. Nothing is submitted: search is typed and escaped,
// menus are opened and closed, newsletter and checkout forms are not filled.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'teenage-engineering', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const steps = Math.min(24, Math.ceil(h / 700));
  for (let i = 0; i < steps; i++) {
    await p.evaluate((y) => scrollTo(0, y), i * 700);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openSearch(p) {
  await p.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => {
      const t = (el.innerText || el.getAttribute('aria-label') || '').trim();
      const r = el.getBoundingClientRect();
      return /^search$/i.test(t) && r.width > 8 && r.height > 8 && r.top >= 0 && r.top < 200;
    });
    if (b) b.click();
  });
  await p.waitForSelector('input[name="search"]', { timeout: 4000 });
  await wait(p, 400);
}

async function openMenu(p) {
  const clicked = await p.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => {
      const t = (el.innerText || el.getAttribute('aria-label') || '').trim();
      const r = el.getBoundingClientRect();
      return /^menu$/i.test(t) && r.width > 8 && r.height > 8;
    });
    if (!b) return false;
    b.click();
    return true;
  });
  await wait(p, 700);
  return clicked;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('search', async () => {
      await openSearch(p);
      await S.view('search');
      await p.locator('input[name="search"]').fill('op-1');
      await wait(p, 900);
      await S.view('search-results');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    });
  } },
  products: { path: '/products', run: async (p, S) => { await S.view('default'); await S.full(); } },
  instruments: { path: '/products/instruments', run: async (p, S) => { await S.view('default'); } },
  audio: { path: '/products/audio', run: async (p, S) => { await S.view('default'); } },
  designs: { path: '/designs', run: async (p, S) => { await S.view('default'); await S.full(); } },
  store: { path: '/store', run: async (p, S) => { await S.view('default'); await S.full(); } },
  deals: { path: '/store/special-offers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'store-category': { path: '/store/pocket-operators', run: async (p, S) => { await S.view('default'); } },
  'store-pdp': { path: '/store/ep-133', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('add-hover', async () => {
      const b = p.locator('button', { hasText: 'add to cart' }).first();
      await b.scrollIntoViewIfNeeded();
      await b.hover();
      await wait(p, 400);
      await S.view('add-hover');
    });
  } },
  product: { path: '/products/ep-133', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-op1': { path: '/products/op-1', run: async (p, S) => { await S.view('default'); } },
  guides: { path: '/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  guide: { path: '/guides/ep-133', run: async (p, S) => { await S.view('default'); await S.full(); } },
  downloads: { path: '/downloads', run: async (p, S) => { await S.view('default'); await S.full(); } },
  now: { path: '/now', run: async (p, S) => { await S.view('default'); await S.full(); } },
  press: { path: '/press', run: async (p, S) => { await S.view('default'); } },
  newsletter: { path: '/newsletter', run: async (p, S) => {
    await S.view('default');
    await step('field-focus', async () => {
      const field = p.locator('input[name="email"]');
      if (await field.count()) {
        await field.click();
        await wait(p, 300);
        await S.view('field-focused');
        await field.blur();
      }
    });
  } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); await S.full(); } },
  retailers: { path: '/retailers', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms-and-conditions', run: async (p, S) => { await S.view('default'); } },
  returns: { path: '/store/support/returns', run: async (p, S) => { await S.view('default'); } },
  checkout: { path: '/store/checkout', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  apps: { path: '/apps', run: async (p, S) => { await S.view('default'); } },
  recycle: { path: '/recycle', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const ok = await openMenu(p);
      if (!ok) throw new Error('menu button not visible');
      await S.view('menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('search', async () => {
      await openSearch(p);
      await S.view('search');
      await p.keyboard.press('Escape');
    });
  } },
  products: { path: '/products', run: async (p, S) => { await S.view('default'); await S.full(); } },
  store: { path: '/store', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'store-pdp': { path: '/store/ep-133', run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: { path: '/products/ep-133', run: async (p, S) => { await S.view('default'); } },
  guides: { path: '/guides', run: async (p, S) => { await S.view('default'); } },
  newsletter: { path: '/newsletter', run: async (p, S) => { await S.view('default'); } },
  checkout: { path: '/store/checkout', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  designs: { path: '/designs', run: async (p, S) => { await S.view('default'); } },
  now: { path: '/now', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1800);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
