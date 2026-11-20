// Captures Nomad Goods public storefront pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/nomadgoods/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, names prefixed mobile-.
// Cookie banner is hidden, never clicked. Klaviyo signup is closed with X,
// never submitted. Account host is not entered. No form is submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideCookies, closeSignup, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'nomadgoods', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideCookies(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideCookies(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
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

async function prepare(p, keepSignup = false) {
  await hideCookies(p);
  if (!keepSignup) await closeSignup(p);
  await hideCookies(p);
  if (isWall(p.url())) throw new Error('wall ' + p.url());
}

async function clickNamed(p, name) {
  const b = p.getByRole('button', { name, exact: true }).filter({ visible: true }).first();
  if (!(await b.count())) return false;
  await b.click({ timeout: 5000 });
  await wait(p, 800);
  await hideCookies(p);
  return true;
}

const PDP = '/sg/products/modern-leather-case-airpods-pro-3-horween-black';

const desktop = {
  home: { path: '/sg/', run: async (p, S) => {
    await S.view('signup');
    await closeSignup(p);
    await hideCookies(p);
    await S.view('default');
    await S.full();
    await step('cart', async () => {
      if (await clickNamed(p, 'Cart drawer')) await S.view('cart');
      const close = p.getByRole('button', { name: 'Close cart drawer' }).first();
      if (await close.count()) await close.click({ timeout: 3000 }).catch(() => {});
      else await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 300);
    });
    await step('locale', async () => {
      if (await clickNamed(p, 'Locale selector')) await S.view('locale');
      await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 300);
    });
    await step('search', async () => {
      if (await clickNamed(p, 'Search')) await S.view('search');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await step('notification', async () => {
      if (await clickNamed(p, 'Notification')) await S.view('notification');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await step('menu-cases', async () => {
      const a = p.locator('a[aria-label="Go to Cases"]').first();
      await a.hover({ timeout: 4000 });
      await wait(p, 700);
      await S.view('menu-cases');
      await p.mouse.move(700, 860);
    });
  } },
  bestsellers: { path: '/sg/pages/best-sellers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  cases: { path: '/sg/collections/cases', run: async (p, S) => { await S.view('default'); await S.full(); } },
  phonecases: { path: '/sg/collections/phone-cases', run: async (p, S) => { await S.view('default'); } },
  bands: { path: '/sg/collections/bands', run: async (p, S) => { await S.view('default'); } },
  charging: { path: '/sg/collections/power', run: async (p, S) => { await S.view('default'); } },
  wallets: { path: '/sg/collections/wallets', run: async (p, S) => { await S.view('default'); } },
  pdp: { path: PDP, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('accordion', async () => {
      const btn = p.locator('button').filter({ hasText: /Description|Details|Shipping|Materials/ }).filter({ visible: true }).first();
      if (await btn.count()) { await btn.click({ timeout: 4000 }); await wait(p, 500); await S.view('accordion'); }
    });
  } },
  search: { path: '/sg/search', run: async (p, S) => { await S.view('default'); } },
  support: { path: '/sg/pages/support', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/sg/pages/about', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/sg/pages/privacy', run: async (p, S) => { await S.view('default'); } },
  sale: { path: '/sg/pages/black-friday-2026', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { path: '/sg/login', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/sg/', run: async (p, S) => {
    await closeSignup(p);
    await hideCookies(p);
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      if (await clickNamed(p, 'Open menu')) await S.view('menu');
    });
  } },
  cases: { path: '/sg/collections/cases', run: async (p, S) => { await S.view('default'); } },
  pdp: { path: PDP, run: async (p, S) => { await S.view('default'); await S.full(); } },
  sale: { path: '/sg/pages/black-friday-2026', run: async (p, S) => { await S.view('default'); } },
  support: { path: '/sg/pages/support', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/sg/login', run: async (p, S) => { await S.view('default'); } },
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
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    log('  ', resp && resp.status(), p.url());
    // /sg/login is a public 404 on this host, not an account wall. Account
// walls are the account.nomadgoods.com host. Capture the 404 as evidence.
if (isWall(p.url()) && !/\/sg\/login/.test(p.url())) { log('  WALL, skipped', p.url()); await ctx.close(); continue; }
    await wait(p, 2200);
    await prepare(p, name === 'home');
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
