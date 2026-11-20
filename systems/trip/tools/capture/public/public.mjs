// Captures Trip.com's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Headless Chromium is captcha-walled (verify.trip.com). This uses installed
// Chrome, headless. www.trip.com geo-redirects to sg.trip.com. The language
// suggestion is hidden, never clicked. Search is not submitted. Auth walls
// are recorded and left.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { launch, hideLanguage, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'trip', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
  await hideLanguage(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideLanguage(this.p);
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

const q = 'locale=en-SG&curr=SGD';
const desktop = {
  home: { url: 'https://www.trip.com/', run: async (p, S) => {
    await S.view('language');
    await hideLanguage(p);
    await S.view('default');
    await S.full();
    await p.evaluate(() => {
      const el = [...document.querySelectorAll('button, [role=button], span, div')].find((e) => (e.innerText || '').trim() === 'SGD' && e.getBoundingClientRect().top < 90 && e.getBoundingClientRect().height < 48);
      if (el) el.click();
    });
    await wait(p, 900);
    await S.view('currency');
    await p.keyboard.press('Escape').catch(() => {});
    await p.mouse.click(40, 700);
    await wait(p, 400);
    await p.evaluate(() => {
      const el = [...document.querySelectorAll('button, a, div')].find((e) => (e.innerText || '').trim() === 'Sign in/register' && e.getBoundingClientRect().top < 90 && e.getBoundingClientRect().height < 56);
      if (el) el.click();
    });
    await wait(p, 1200);
    await S.view('signin');
    await p.keyboard.press('Escape').catch(() => {});
  } },
  hotels: { url: `${BASE}/hotels/?${q}`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  flights: { url: `${BASE}/flights/?${q}`, run: async (p, S) => { await S.view('default'); await S.full(); } },
  trains: { url: `${BASE}/trains/?${q}`, run: async (p, S) => { await S.view('default'); } },
  cars: { url: `${BASE}/carhire/?${q}`, run: async (p, S) => { await S.view('default'); } },
  attractions: { url: `${BASE}/things-to-do/?${q}`, run: async (p, S) => { await S.view('default'); } },
  packages: { url: `${BASE}/packages/?sourceFrom=IBUBundle_home&${q}`, run: async (p, S) => { await S.view('default'); } },
  deals: { url: `${BASE}/sale/deals/?${q}`, run: async (p, S) => { await S.view('default'); } },
  support: { url: `${BASE}/pages/support/?${q}`, run: async (p, S) => { await S.view('default'); } },
  about: { url: `${BASE}/pages/about-us/?${q}`, run: async (p, S) => { await S.view('default'); } },
  app: { url: `${BASE}/pages/appdownload?${q}`, run: async (p, S) => { await S.view('default'); } },
  rewards: { url: `${BASE}/customer/loyalty/?${q}`, run: async (p, S) => { await S.view('default'); } },
  planner: { url: `${BASE}/webapp/tripmap/tripplanner?source=t_online_homepage&${q}`, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: 'https://www.trip.com/', run: async (p, S) => { await hideLanguage(p); await S.view('default'); await S.full(); } },
  hotels: { url: `${BASE}/hotels/?${q}`, run: async (p, S) => { await S.view('default'); } },
  flights: { url: `${BASE}/flights/?${q}`, run: async (p, S) => { await S.view('default'); } },
  menu: { url: 'https://www.trip.com/', run: async (p, S) => {
    await hideLanguage(p);
    const btn = p.locator('[aria-label="Menu"], button:has-text("Menu")').first();
    if (await btn.count()) await btn.click({ timeout: 3000 }).catch(() => {});
    await wait(p, 800);
    await S.view('menu');
  } },
};

const { browser } = await launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob
      ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1'
      : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-SG',
    timezoneId: 'Asia/Singapore',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 5000);
    const url = p.url();
    if (/verify\.trip\.com|signin|passport\//i.test(url)) {
      log('  STOP', url.slice(0, 120));
      await S.view('stopped');
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
