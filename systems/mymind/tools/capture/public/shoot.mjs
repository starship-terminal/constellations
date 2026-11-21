// Public marketing captures for mymind.com. Nothing is signed into.
// Auth hosts are never opened. Desktop 1440x900 at 1x, phone 390x844 at 2x.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs [name,name]
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mymind', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const BASE = 'https://mymind.com';
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const desktop = {
  home: '/',
  why: '/why',
  how: '/how',
  what: '/what',
  videos: '/videos',
  reviews: '/reviews',
  pricing: '/pricing',
  faq: '/faq',
  adhd: '/adhd',
  extensions: '/browser-extensions',
  manifesto: '/manifesto',
  promise: '/our-promise',
  'private-first': '/private-first',
  privacy: '/privacypolicy',
  terms: '/terms',
  'data-security': '/data-security',
  subprocessors: '/subprocessors',
  'ai-policy': '/ai-usage-policy',
  cancellation: '/cancellation-policy',
  refund: '/refund-policy',
  inactive: '/inactive-account-policy',
  restrictions: '/use-restrictions',
  'extension-privacy': '/extension-privacy',
  mobile: '/mobile',
  artworks: '/artworks',
  palace: '/palace',
  interviews: '/interviews',
  essay: '/6-reasons-mastermind',
  interview: '/into-the-mind-of-stefan-sagmeister',
  notfound: '/login',
};

const mobilePages = ['home', 'why', 'how', 'pricing', 'videos', 'faq', 'palace', 'notfound'];

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.p.url().split('?')[0] }, this.requested);
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
          sanitizedSourceUrl: p.url().split('?')[0],
        }, this.requested);
      }
    }
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function go(context, pathName) {
  const page = await context.newPage();
  page.setDefaultNavigationTimeout(30000);
  const res = await page.goto(BASE + pathName, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await wait(page, 1600);
  return { page, status: res?.status() ?? 0 };
}

const browser = await chromium.launch({ headless: true });
const desktopCtx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
});
const phoneCtx = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
});

for (const [name, pathName] of Object.entries(desktop)) {
  const key = name;
  if (pageArg.length && !pageArg.includes(key)) continue;
  log('desktop', key);
  const { page, status } = await go(desktopCtx, pathName);
  log('  status', status, page.url());
  const S = new Shooter(page, `${key}-light`, 1440, 900, 1);
  await S.view('default');
  if (['home', 'why', 'how', 'pricing', 'videos', 'palace', 'faq', 'reviews'].includes(key)) await S.full();
  if (key === 'pricing') {
    const yearly = page.getByRole('button', { name: /Yearly/ });
    if (await yearly.count()) {
      await yearly.first().click();
      await wait(page, 600);
      await S.view('yearly');
    }
    const monthly = page.getByRole('button', { name: 'Monthly' });
    if (await monthly.count()) {
      await monthly.first().click();
      await wait(page, 400);
      await S.view('monthly');
    }
  }
  if (key === 'home') {
    const cta = page.getByRole('link', { name: /TRY IT OUT/i }).first();
    if (await cta.count()) {
      await cta.hover();
      await wait(page, 400);
      await S.view('cta-hover');
    }
    const login = page.getByRole('link', { name: 'Log in' }).first();
    if (await login.count()) {
      await login.focus();
      await wait(page, 300);
      await S.view('login-focus');
    }
  }
  if (key === 'videos') {
    const play = page.getByRole('link', { name: /PLAY VIDEO/i }).first();
    if (await play.count()) {
      await play.click();
      await wait(page, 800);
      await S.view('play');
    }
  }
  await page.close();
}

for (const name of mobilePages) {
  const key = 'mobile-' + name;
  if (pageArg.length && !pageArg.includes(key)) continue;
  log('phone', key);
  const { page, status } = await go(phoneCtx, desktop[name]);
  log('  status', status, page.url());
  const S = new Shooter(page, `${key}-light`, 390, 844, 2);
  await S.view('default');
  if (['home', 'pricing', 'how'].includes(name)) await S.full();
  if (name === 'pricing') {
    const yearly = page.getByRole('button', { name: /Yearly/ });
    if (await yearly.count()) {
      await yearly.first().click();
      await wait(page, 500);
      await S.view('yearly');
    }
  }
  await page.close();
}

await browser.close();
log('done', RAW);
