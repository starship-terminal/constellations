// Captures Square's public marketing pages.
// Full-colour shots go to RAW (default ~/.design-systems/square/raw-shots).
// quantize.py turns the chosen ones into screenshots/.
//
//   PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Nothing is submitted, signed
// into, or typed. Cookie dialogs are hidden, never accepted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'square', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H0 = await p.evaluate(() => document.documentElement.scrollHeight);
    const step = 700;
    const ceiling = Math.min(H0 + 2000, 12000);
    for (let y = 0; y < ceiling; y += step) {
      await p.evaluate((y) => scrollTo(0, y), y);
      await wait(p, 120);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openProducts(p) {
  await p.getByRole('button', { name: 'Products', exact: true }).first().click();
  await wait(p, 700);
}
async function openBusiness(p) {
  await p.getByRole('button', { name: 'Business types', exact: true }).first().click();
  await wait(p, 700);
}
async function openCategory(p, name) {
  const panel = p.locator('[id^="global-nav-desktop-dropdown-content"]').first();
  await panel.getByRole('button', { name, exact: true }).first().click();
  await wait(p, 400);
}

const desktop = {
  home: { path: '/us/en', run: async (p, S) => {
    await S.view('default');
    await step('products-menu', async () => { await openProducts(p); await S.view('products-menu'); await p.keyboard.press('Escape'); });
    await step('products-payments', async () => { await openProducts(p); await openCategory(p, 'Payments'); await S.view('products-payments'); await p.keyboard.press('Escape'); });
    await step('business-menu', async () => { await openBusiness(p); await S.view('business-menu'); await p.keyboard.press('Escape'); });
    await step('whats-new', async () => { await p.getByRole('button', { name: "What's new", exact: true }).first().click(); await wait(p, 500); await S.view('whats-new'); await p.keyboard.press('Escape'); });
    await step('cart', async () => { await p.getByRole('button', { name: /Your Cart/i }).first().click(); await wait(p, 500); await S.view('cart'); await p.keyboard.press('Escape'); });
    await step('disclosure', async () => {
      await p.locator('summary').filter({ hasText: 'Take payments' }).first().click();
      await wait(p, 500);
      await S.view('disclosure');
    });
    await S.full();
  } },
  pricing: { path: '/us/en/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  hardware: { path: '/us/en/hardware', run: async (p, S) => { await S.view('default'); await S.full(); } },
  payments: { path: '/us/en/payments', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pos: { path: '/us/en/point-of-sale', run: async (p, S) => { await S.view('default'); await S.full(); } },
  restaurants: { path: '/us/en/restaurants', run: async (p, S) => { await S.view('default'); await S.full(); } },
  banking: { path: '/us/en/banking', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/help/us/en', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const field = p.locator('input[type="search"], input[type="text"], input[placeholder]').first();
      await field.click();
      await wait(p, 400);
      await S.view('search-focused');
    });
    await S.full();
  } },
  login: { path: 'https://app.squareup.com/login', absolute: true, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/us/en/sales/contact', run: async (p, S) => {
    await S.view('default');
    await step('field-focused', async () => {
      const field = p.locator('input:not([type="hidden"]), textarea').first();
      await field.click();
      await wait(p, 300);
      await S.view('field-focused');
    });
  } },
  cart: { path: '/shop/hardware/us/en/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { path: '/us/en/legal/general/privacy', run: async (p, S) => { await S.view('default'); } },
  software: { path: '/us/en/software', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/us/en/about', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/us/en', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.locator('button').filter({ hasText: /menu|open/i }).first();
      const hamburger = p.locator('header button, [class*="PublicWebNav"] button').first();
      const target = (await btn.count()) ? btn : hamburger;
      await target.click();
      await wait(p, 700);
      await S.view('menu');
    });
    await S.full();
  } },
  pricing: { path: '/us/en/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  hardware: { path: '/us/en/hardware', run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://app.squareup.com/login', absolute: true, run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help/us/en', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const url = spec.absolute ? spec.path : BASE + spec.path;
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, url.split('?')[0]);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2800);
    await hideConsent(p);
    const landed = p.url();
    if (/app\.squareup\.com\/(login|signup)/.test(landed) && !/login/.test(url)) {
      log('  AUTH WALL', landed.split('?')[0], 'stopping branch');
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
