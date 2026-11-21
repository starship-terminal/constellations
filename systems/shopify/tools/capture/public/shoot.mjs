// Captures Shopify's public marketing site. Adapted from the kit's public shooter.
//
//   RAW=~/.design-systems/shopify/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/shoot.mjs [name,name]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. US English is pinned with
// ?country=us&lang=en so the geo redirect does not swap the locale.
// Nothing is submitted. Login and signup URLs are recorded and not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'shopify', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://www.shopify.com';

function pin(urlPath) {
  const u = new URL(urlPath, BASE);
  if (!u.searchParams.get('country')) u.searchParams.set('country', 'us');
  if (!u.searchParams.get('lang')) u.searchParams.set('lang', 'en');
  return u.toString();
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 140);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
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
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function openMenu(p, which) {
  const label = p.locator(`label[for="bk-nav-${which}"]`).first();
  const box = await label.boundingBox();
  if (!box) throw new Error('no label ' + which);
  await p.mouse.move(box.x + Math.min(40, box.width / 2), box.y + box.height / 2);
  await wait(p, 700);
}

async function openDrawer(p) {
  const ham = p.locator('label[for="bk-nav-hamburger"]').first();
  await ham.click();
  await wait(p, 700);
}

const PAGES = {
  home: '/',
  start: '/start',
  sell: '/sell',
  enterprise: '/enterprise',
  checkout: '/checkout',
  sidekick: '/sidekick',
  pricing: '/pricing',
  editions: '/editions/fall2026',
  'website-builder': '/website/builder',
  domains: '/domains',
  online: '/online',
  pos: '/pos',
  payments: '/payments',
  blog: '/blog',
  compare: '/compare',
  legal: '/legal',
  sitemap: '/sitemap',
  'what-is': '/blog/what-is-shopify',
  capital: '/capital',
  'shop-pay': '/shop-pay',
  help: 'https://help.shopify.com/en',
  themes: 'https://themes.shopify.com/',
  apps: 'https://apps.shopify.com/',
};

const desktopStates = {
  home: async (p, S) => {
    await S.view('default');
    await S.full();
    await openMenu(p, 'Why Shopify');
    await S.view('why-menu');
    await p.mouse.move(10, 860);
    await wait(p, 400);
    await openMenu(p, 'Products');
    await S.view('products-menu');
    await p.mouse.move(10, 860);
    await wait(p, 300);
    await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await wait(p, 600);
    const region = p.locator('button[aria-controls="language-selector-popover"]').first();
    if (await region.count()) {
      await region.click();
      await wait(p, 700);
      await S.view('region-dialog');
      const close = p.locator('#language-selector-popover button', { hasText: 'Close' }).first();
      if (await close.count()) await close.click().catch(() => {});
      else await p.keyboard.press('Escape');
      await wait(p, 300);
    }
    await p.evaluate(() => window.scrollTo(0, 0));
    await wait(p, 300);
    const play = p.locator('button[aria-label="Play testimonial video"]').first();
    if (await play.count()) {
      await play.scrollIntoViewIfNeeded().catch(() => {});
      await play.click().catch(() => {});
      await wait(p, 900);
      await S.view('video-dialog');
      await p.keyboard.press('Escape');
    }
  },
  pricing: async (p, S) => {
    await S.view('default');
    await S.full();
    const sw = p.getByRole('switch').first();
    if (await sw.count()) {
      await sw.click();
      await wait(p, 500);
      await S.view('yearly');
      await sw.click().catch(() => {});
    }
    const summary = p.locator('summary').first();
    if (await summary.count()) {
      await summary.scrollIntoViewIfNeeded();
      await summary.click();
      await wait(p, 400);
      await S.view('faq-open');
    }
  },
};

const mobileStates = {
  home: async (p, S) => {
    await S.view('default');
    await S.full();
    await openDrawer(p);
    await S.view('menu');
    const products = p.locator('label[for="bk-nav-Products"]').first();
    if (await products.count()) {
      await products.click();
      await wait(p, 600);
      await S.view('products-menu');
    }
  },
  pricing: async (p, S) => {
    await S.view('default');
    await S.full();
  },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const jobs = [];
for (const name of Object.keys(PAGES)) jobs.push({ name, mob: false });
for (const name of ['home', 'pricing', 'enterprise', 'blog', 'pos']) jobs.push({ name, mob: true });

for (const { name, mob } of jobs) {
  const shot = (mob ? 'mobile-' : '') + name;
  if (pageArg.length && !pageArg.includes(shot) && !pageArg.includes(name)) continue;
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
  const S = new Shooter(p, `${shot}-light`, vw, vh, dpr);
  const url = PAGES[name].startsWith('http') ? PAGES[name] : pin(PAGES[name]);
  log(shot, url);
  try {
    const resp = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
    await wait(p, 2800);
    const finalUrl = p.url();
    if (/accounts\.shopify\.com|admin\.shopify\.com\/signup|\/lookup/.test(finalUrl)) {
      log('  WALL', finalUrl.split('?')[0]);
      fs.appendFileSync(path.join(RAW, 'walls.txt'), shot + ' ' + finalUrl.split('?')[0] + '\n');
    } else {
      log('  status', resp && resp.status(), 'final', finalUrl.split('?')[0]);
      const extra = mob ? mobileStates[name] : desktopStates[name];
      if (extra) await extra(p, S);
      else {
        await S.view('default');
        if (!mob) await S.full();
      }
    }
  } catch (e) {
    log('  PAGE FAILED', shot, String(e.message).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, '->', RAW);
await b.close();
