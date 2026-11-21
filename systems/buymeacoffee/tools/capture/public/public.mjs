// Captures Buy Me a Coffee's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/buymeacoffee/raw-shots PLAYWRIGHT=... node public.mjs [name,name]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Names are {page}-light-{state}.png.
// Nothing is submitted. Login and signup are photographed and not filled.
// Google, Facebook, Apple and Twitter are never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideOverlays } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'buymeacoffee', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
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
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

const desktopPages = {
  home: '/',
  faq: '/faq',
  reviews: '/reviews',
  'qr-code': '/qr-code',
  'stream-alerts': '/stream-alerts',
  brand: '/brand',
  'ko-fi': '/ko-fi-alternative',
  patreon: '/patreon-alternative',
  about: '/about',
  blog: '/blog',
  terms: '/terms',
  login: '/login',
  signup: '/signup',
  creator: '/cara.app',
  membership: '/cara.app/membership',
  wishlist: '/cara.app/wishlist',
};

const mobilePages = {
  home: '/',
  faq: '/faq',
  reviews: '/reviews',
  brand: '/brand',
  blog: '/blog',
  login: '/login',
  signup: '/signup',
  creator: '/cara.app',
};

async function desktopExtras(p, S, key) {
  if (key === 'home') {
    await step('apps-menu', async () => {
      await p.locator('#bmc-header').getByText('Apps', { exact: true }).first().hover();
      await wait(p, 400);
      await S.view('apps-menu');
    });
    await step('resources-menu', async () => {
      await p.locator('#bmc-header').getByText('Resources', { exact: true }).first().hover();
      await wait(p, 500);
      await S.view('resources-menu');
      await p.mouse.move(700, 500);
      await wait(p, 200);
    });
    await step('search', async () => {
      await p.locator('#bmc-header').getByText('Search creators', { exact: true }).click();
      await wait(p, 500);
      await S.view('search-open');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('nav-hover', async () => {
      await p.locator('#bmc-header a[aria-label="FAQ"]').hover();
      await wait(p, 300);
      await S.view('nav-hover');
    });
    await step('cta-hover', async () => {
      const cta = p.locator('a[aria-label="Start my page"]').first();
      if (await cta.count()) {
        await cta.hover();
        await wait(p, 300);
        await S.view('cta-hover');
      }
    });
  }
  if (key === 'faq') {
    await step('faq-open', async () => {
      const q = p.getByText('Who uses Buy Me a Coffee?', { exact: false }).first();
      await q.click();
      await wait(p, 400);
      await S.view('question-open');
    });
  }
  if (key === 'reviews') {
    await step('slide', async () => {
      const next = p.getByRole('button', { name: /slide next/i }).first();
      if (await next.count()) {
        await next.click();
        await wait(p, 600);
        await S.view('slide-next');
      }
    });
  }
  if (key === 'login') {
    await S.view('auth-wall');
  }
  if (key === 'signup') {
    await S.view('auth-wall');
  }
  if (key === 'creator') {
    await step('quantity', async () => {
      const radio = p.getByRole('radio', { name: '3' }).first();
      if (await radio.count()) {
        await radio.click();
        await wait(p, 300);
        await S.view('quantity-selected');
      }
    });
  }
}

async function mobileExtras(p, S, key) {
  if (key === 'home') {
    await step('menu', async () => {
      const opened = await p.evaluate(() => {
        const btn = [...document.querySelectorAll('#bmc-header button, #bmc-header [role="button"], #bmc-header svg, #bmc-header div')].find((el) => {
          const r = el.getBoundingClientRect();
          return r.width > 10 && r.width < 64 && r.top < 80 && r.left < 80;
        });
        if (btn) { btn.click(); return true; }
        return false;
      });
      if (!opened) {
        await p.locator('#bmc-header').locator('svg').first().click({ timeout: 3000 }).catch(() => {});
      }
      await wait(p, 600);
      await S.view('menu-open');
    });
  }
}

const browser = await chromium.launch({ headless: true });
let total = 0;

async function runSet(pages, mob) {
  for (const [key, pth] of Object.entries(pages)) {
    const name = (mob ? 'mobile-' : '') + key;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    log(name, pth);
    try {
      await p.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await wait(p, 2200);
      await hideOverlays(p);
      await S.view('default');
      if (!mob) await S.full();
      else if (['home', 'faq', 'creator', 'blog'].includes(key)) await S.full();
      if (mob) await mobileExtras(p, S, key);
      else await desktopExtras(p, S, key);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}

await runSet(desktopPages, false);
await runSet(mobilePages, true);
log('done', total, 'screenshots ->', RAW);
await browser.close();
