// Unsplash public screenshots. Headed Chromium only: headless stops on Anubis.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Writes full-colour PNGs to ~/.design-systems/unsplash/raw-shots. quantize.py
// copies them into screenshots/. Nothing is submitted. Login is photographed
// with empty fields.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, open, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'unsplash', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
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
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    await lazyScroll(this.p);
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log('  !', name, 'page is', H, 'px, capturing first', hCap);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) await screenshotWithMetadata(this.p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.p, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await this.p.evaluate(() => scrollTo(0, 0));
  }
}

async function firstHref(page, sel) {
  return page.evaluate((sel) => {
    const a = [...document.querySelectorAll(sel)].find((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 40 && r.height > 40;
    });
    if (!a) return null;
    const u = new URL(a.href);
    return u.pathname;
  }, sel);
}

const desktop = {
  home: async (p, S) => {
    await S.view('default');
    await p.getByRole('button', { name: 'Menu', exact: true }).click();
    await wait(p, 700);
    await S.view('menu');
    await p.keyboard.press('Escape');
    await wait(p, 400);
    await p.locator('input[name="searchKeyword"]').first().click();
    await wait(p, 700);
    await S.view('search-focus');
    await p.keyboard.press('Escape');
    await wait(p, 300);
    const vis = p.getByRole('button', { name: 'Visual Search' }).first();
    if (await vis.count()) {
      await vis.click();
      await wait(p, 700);
      await S.view('visual-search');
      await p.keyboard.press('Escape');
    }
    await S.full();
  },
  illustrations: async (p, S) => { await S.view('default'); await S.full(); },
  explore: async (p, S) => { await S.view('default'); await S.full(); },
  topic: async (p, S) => { await S.view('default'); await S.full(); },
  photo: async (p, S) => { await S.view('default'); await S.full(); },
  plus: async (p, S) => { await S.view('default'); await S.full(); },
  about: async (p, S) => { await S.view('default'); await S.full(); },
  license: async (p, S) => { await S.view('default'); },
  developers: async (p, S) => { await S.view('default'); await S.full(); },
  images: async (p, S) => { await S.view('default'); },
  login: async (p, S) => { await S.view('default'); },
  awards: async (p, S) => { await S.view('default'); },
};

const mobile = {
  home: async (p, S) => {
    await S.view('default');
    const menu = p.getByRole('button', { name: 'Menu', exact: true });
    if (await menu.count()) {
      await menu.click();
      await wait(p, 700);
      await S.view('menu');
      await p.keyboard.press('Escape');
    }
    const search = p.locator('input[name="searchKeyword"]').first();
    if (await search.count()) {
      await search.click();
      await wait(p, 600);
      await S.view('search-focus');
      await p.keyboard.press('Escape');
    }
    await S.full();
  },
  photo: async (p, S) => { await S.view('default'); },
  login: async (p, S) => { await S.view('default'); },
};

const paths = {
  home: '/',
  illustrations: '/illustrations',
  explore: '/explore',
  topic: '/t/nature',
  plus: '/plus',
  about: '/about',
  license: '/license',
  developers: '/developers',
  images: '/images',
  login: '/login',
  awards: '/awards/2026/winners',
  photo: '/photos/two-generations-of-woman-dairy-farmers-posing-together-8ORoxxsxNXA',
};

const browser = await chromium.launch({ headless: false });
let total = 0;

async function runSet(specs, mobileFlag) {
  const vw = mobileFlag ? 390 : 1440;
  const vh = mobileFlag ? 844 : 900;
  const dpr = mobileFlag ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobileFlag ? UA_MOBILE : UA,
    isMobile: mobileFlag,
    hasTouch: mobileFlag,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  for (const [k, run] of Object.entries(specs)) {
    const name = (mobileFlag ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
    const route = paths[k];
    if (!route) { log('skip', name, 'no path'); continue; }
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    log(name, route);
    try {
      await open(p, BASE + route);
      if (/\/login|\/join/.test(p.url()) && k !== 'login') {
        log('  wall', p.url(), 'stop branch');
        await S.view('login-wall');
        continue;
      }
      await run(p, S);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
  }
  await ctx.close();
}

await runSet(desktop, false);
await runSet(mobile, true);
log('done', total, '->', RAW);
await browser.close();
