// Captures IKEA Singapore's public signed-out storefront into RAW.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Locale: www.ikea.com/sg/en/ (the shopping locale this host is served).
// Consent is hidden, never clicked. Add to cart, login, and checkout are not pressed.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, LOCALE, hideConsent, launchBrowser, newContext, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'ikea', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
    await hideConsent(p);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  global: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  home: { path: `${LOCALE}/`, run: async (p, S) => {
    await S.view('default');
    await step('products-menu', async () => {
      const products = p.getByRole('link', { name: 'Products', exact: true }).first();
      await products.hover();
      await wait(p, 700);
      await S.view('products-menu');
      await p.mouse.move(700, 700);
    });
    await step('search-focus', async () => {
      const input = p.locator('input[name="q"], input[type="search"]').first();
      await input.click();
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  category: { path: `${LOCALE}/cat/sofas-armchairs-700640/`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: { path: `${LOCALE}/p/billy-bookcase-white-00522047/`, run: async (p, S) => {
    await S.view('default');
    await step('qty-focus', async () => {
      const qty = p.locator('input[name="pipf-quantity-stepper-input"]').first();
      if (await qty.count()) { await qty.click(); await wait(p, 300); await S.view('qty-focused'); }
    });
    await S.full();
  } },
  search: { path: `${LOCALE}/search/?q=lamp`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  stores: { path: `${LOCALE}/stores/`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: `${LOCALE}/profile/login/`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  offers: { path: `${LOCALE}/offers/`, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: `${LOCALE}/`, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.getByRole('button', { name: /^Menu$/ }).first();
      if (await btn.count()) { await btn.click(); await wait(p, 800); await S.view('menu'); }
    });
    await S.full();
  } },
  category: { path: `${LOCALE}/cat/sofas-armchairs-700640/`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: { path: `${LOCALE}/p/billy-bookcase-white-00522047/`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { path: `${LOCALE}/search/?q=lamp`, run: async (p, S) => { await S.view('default'); } },
  stores: { path: `${LOCALE}/stores/`, run: async (p, S) => { await S.view('default'); } },
  login: { path: `${LOCALE}/profile/login/`, run: async (p, S) => { await S.view('default'); } },
};

const browser = await launchBrowser();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await newContext(browser, { mobile: mob, width: vw, height: vh, dpr });
  const p = await ctx.newPage();
  log(name, spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await open(p, BASE + spec.path, { wait: 1800 });
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
