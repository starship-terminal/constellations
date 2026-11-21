// Captures vsco.co public marketing pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=.../playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png. The marketing site has one dark theme.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Full pages tile at 8 chunks max.
// Nothing is submitted. Login, signup, Google, Apple, and checkout are not opened
// except the login and signup walls, which are recorded and left unfilled.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, hideBanner, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'vsco', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, 12000); y += 700) {
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
  }
  async view(name) {
    await hideBanner(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, animations: 'disabled' }, this.requested);
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideBanner(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, animations: 'disabled' }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await p.evaluate((yy) => scrollTo(0, yy), y);
      await wait(p, 80);
      const liveH = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
      const tileH = Math.min(chunk, Math.max(1, liveH - y), hCap - y);
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, animations: 'disabled', clip: { x: 0, y: 0, width: this.vw, height: Math.min(tileH, this.p.viewportSize().height) } }, this.requested).catch(async () => {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, animations: 'disabled' }, this.requested);
      });
    }
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('products-menu', async () => {
      await p.locator('.menu_link.w-dropdown-toggle').filter({ hasText: 'PRODUCTS' }).first().click();
      await wait(p, 500);
      await S.view('products-menu');
      await p.keyboard.press('Escape');
      await p.mouse.click(700, 700);
      await wait(p, 300);
    });
    await step('tab-create', async () => {
      await p.locator('.w-tab-link').filter({ hasText: 'CREATE' }).first().click();
      await wait(p, 400);
      await S.view('tab-create');
    });
    await S.full();
  } },
  plans: { path: '/subscribe/plans', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const q = p.locator('button, .faq_accordion, [class*="accordion"]').filter({ hasText: /worth it|included in each/i }).first();
      if (await q.count()) { await q.click(); await wait(p, 400); await S.view('faq'); }
    });
    await S.full();
  } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  editor: { path: '/features/photo-editor', run: async (p, S) => { await S.view('default'); await S.full(); } },
  planspro: { path: '/pro', run: async (p, S) => { await S.view('default'); await S.full(); } },
  downloads: { path: '/downloads', run: async (p, S) => { await S.view('default'); await S.full(); } },
  learn: { path: '/learn', run: async (p, S) => { await S.view('default'); await S.full(); } },
  article: { path: '/learn/how-to-edit-photos', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { path: '/this-page-does-not-exist-capture', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://vsco.co/user/login', run: async (p, S) => { await S.view('default'); } },
  signup: { url: 'https://vsco.co/user/signup', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('.w-nav-button, [aria-label="menu"]').first().click();
      await wait(p, 500);
      await S.view('menu');
    });
    await S.full();
  } },
  plans: { path: '/subscribe/plans', run: async (p, S) => { await S.view('default'); await S.full(); } },
  editor: { path: '/features/photo-editor', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://vsco.co/user/login', run: async (p, S) => { await S.view('default'); } },
};

async function runSet(browser, specMap, mob) {
  for (const [k, spec] of Object.entries(specMap)) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    await patch(ctx);
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
    log(name);
    try {
      const target = spec.url || BASE + spec.path;
      log('  ->', target);
      await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(p, 1800);
      await hideBanner(p);
      const blocked = await p.evaluate(() => /just a moment|performing security verification/i.test(document.title + (document.body?.innerText || '').slice(0, 200))).catch(() => false);
      if (blocked) { log('  BLOCKED', target); await ctx.close(); continue; }
      await spec.run(p, S);
    } catch (e) {
      log('  PAGE FAILED', name, e.message.split('\n')[0]);
    }
    await ctx.close();
  }
}

const browser = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
await runSet(browser, desktop, false);
await runSet(browser, mobile, true);
await browser.close();
log('done', RAW);
