// Captures Sharewillow's public pages. Full-colour PNGs go to RAW; quantize.py
// turns the ones we keep into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, names prefixed mobile-.
// Nothing is submitted. Sign-in and sign-up are recorded as walls and not filled.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, closePromo, clearChallenge } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'sharewillow', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
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
      // Scroll each tile into the viewport. A clip taller than the viewport
      // fails the kit's PNG dimension check (mobile full-page, 2026-11-21).
      const tile = Math.min(chunk, this.p.viewportSize().height);
      for (let i = 0, y = 0; y < hCap; i++, y += tile) {
        await p.evaluate((yy) => scrollTo(0, yy), y);
        await wait(p, 200);
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png` }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function gotoPublic(p, url) {
  const resp = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 1800);
  await clearChallenge(p, { tries: 3, step: 600 });
  await closePromo(p);
  const final = p.url();
  if (/app\.sharewillow\.com\/(login|signup)/.test(final)) {
    log('  WALL', final);
    return { wall: true, status: resp && resp.status() };
  }
  return { wall: false, status: resp && resp.status(), final };
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('product-menu', async () => {
      await p.getByRole('button', { name: 'Product', exact: true }).first().click();
      await wait(p, 500);
      await S.view('product-menu');
      await p.keyboard.press('Escape');
    });
    await step('industries-menu', async () => {
      await p.getByRole('button', { name: 'Industries', exact: true }).first().click();
      await wait(p, 500);
      await S.view('industries-menu');
      await p.keyboard.press('Escape');
    });
    await step('demo-prompt', async () => {
      const b = p.getByRole('button', { name: /Last month's payouts|What did we pay out/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('demo-prompt'); }
    });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  agents: { url: BASE + '/agents', run: async (p, S) => { await S.view('default'); } },
  customers: { url: BASE + '/customers', run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); } },
  'blog-post': { url: BASE + '/blog/compensation-strategy-examples', run: async (p, S) => { await S.view('default'); } },
  docs: { url: BASE + '/docs', run: async (p, S) => { await S.view('default'); } },
  product: { url: BASE + '/product/plan-builder', run: async (p, S) => { await S.view('default'); await S.full(); } },
  industry: { url: BASE + '/industries/hvac', run: async (p, S) => { await S.view('default'); } },
  demo: { url: BASE + '/demo', run: async (p, S) => { await S.view('default'); } },
  resources: { url: BASE + '/resources', run: async (p, S) => { await S.view('default'); } },
  changelog: { url: BASE + '/changelog', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://app.sharewillow.com/login', wall: true, run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Open menu' });
      if (await b.count()) {
        await b.first().click();
        await wait(p, 600);
        await S.view('menu');
        const close = p.getByRole('button', { name: 'Close menu' });
        if (await close.count()) await close.first().click();
      }
    });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); } },
  product: { url: BASE + '/product/mobile-app', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://app.sharewillow.com/login', wall: true, run: async (p, S) => { await S.view('wall'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const nav = await gotoPublic(p, spec.url);
    if (nav.wall && !spec.wall) log('  unexpected wall, skipping interactions');
    else await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
