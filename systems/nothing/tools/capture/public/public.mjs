// Captures nothing.tech's public store into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/nothing/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Full pages tile at 8 chunks.
// Didomi is removed, never answered. The region suggestion is dismissed with
// Stay on the current store so the page underneath can be captured. Login,
// account and signup URLs are recorded and not entered. No form is submitted
// and no field is filled.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'nothing', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function dismiss(p) {
  await p.evaluate(() => {
    document.querySelectorAll('#didomi-host, #didomi-popup, .didomi-popup-backdrop, .didomi-popup-notice').forEach((n) => {
      n.style.setProperty('display', 'none', 'important');
      n.style.setProperty('pointer-events', 'none', 'important');
    });
  }).catch(() => {});
  const stay = p.getByRole('button', { name: /stay on/i });
  if (await stay.count().catch(() => 0)) {
    await stay.first().click({ timeout: 4000 }).catch(() => {});
    await wait(p, 500);
  }
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement ? document.documentElement.scrollHeight : 0).catch(() => 0);
  if (!h) return;
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
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    await dismiss(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await dismiss(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => {
      const d = document.documentElement;
      const b = document.body;
      if (!d || !b) return 0;
      return Math.max(d.scrollHeight, b.scrollHeight);
    }).catch(() => 0);
    if (!H) { log('  skip full, document gone'); return; }
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
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openNav(p, label) {
  await dismiss(p);
  const opened = await p.evaluate((label) => {
    const a = [...document.querySelectorAll('header nav a, header a')].find((el) => (el.innerText || '').replace(/\s+/g, ' ').trim().toUpperCase() === label);
    if (!a) return false;
    a.addEventListener('click', (e) => e.preventDefault(), { capture: true });
    a.click();
    return true;
  }, label);
  await wait(p, 800);
  await dismiss(p);
  return opened;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openNav(p, 'AUDIO')) { await S.view('menu-audio'); await p.keyboard.press('Escape').catch(() => {}); }
    await p.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
    await wait(p, 800);
    await dismiss(p);
    if (await openNav(p, 'PHONES')) { await S.view('menu-phones'); await p.keyboard.press('Escape').catch(() => {}); }
    await p.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
    await wait(p, 800);
    await dismiss(p);
    const cart = p.locator('button[aria-label*="Cart"]').first();
    if (await cart.count()) { await cart.click().catch(() => {}); await wait(p, 600); await S.view('cart'); }
  } },
  sale: { path: '/collections/sale' },
  audio: { path: '/collections/audio' },
  phones: { path: '/collections/phones' },
  watches: { path: '/collections/watches' },
  cmf: { path: '/collections/cmf' },
  headphones: { path: '/collections/headphones' },
  earbuds: { path: '/collections/earbuds' },
  speakers: { path: '/collections/speakers' },
  accessories: { path: '/collections/accessories' },
  shopall: { path: '/collections/shop-all' },
  product: { path: '/products/headphone-1-pro' },
  community: { path: '/community' },
  about: { path: '/about' },
  os: { path: '/nothing-os' },
  offers: { path: '/offers' },
  support: { path: '/pages/support-centre' },
  contact: { path: '/pages/contact-support' },
  privacy: { path: '/pages/privacy-policy' },
  business: { path: '/support/business-enquiry' },
  nyc: { path: '/headphone-1-pro-nyc-launch-event' },
  ambassador: { path: '/v-global-brand-ambassador' },
  a11y: { path: '/pages/accessibility-statement' },
  notfound: { path: '/login' },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const menu = p.locator('button[aria-label="Menu"], button[aria-label*="menu" i]').first();
    if (await menu.count()) { await menu.click().catch(() => {}); await wait(p, 700); await dismiss(p); await S.view('menu'); }
  } },
  sale: { path: '/collections/sale' },
  product: { path: '/products/headphone-1-pro' },
  support: { path: '/pages/support-centre' },
  notfound: { path: '/login' },
};

async function runSet(pages, { width, height, dpr, mobile: isMobile, prefix }) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(isMobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-GB', serviceWorkers: 'block' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-GB', serviceWorkers: 'block' });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const names = pageArg.length ? pageArg : Object.keys(pages);
  for (const name of names) {
    const spec = pages[name];
    if (!spec) continue;
    const page = await context.newPage();
    page.setDefaultTimeout(20000);
    const url = BASE + spec.path;
    log('open', prefix + name, url);
    try {
      const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
      await page.waitForFunction(() => {
        const t = (document.body && document.body.innerText) || '';
        return t.length > 80;
      }, { timeout: 15000 }).catch(() => {});
      await wait(page, 1500);
      await dismiss(page);
      await wait(page, 400);
      const final = page.url();
      if (/account\.nothing\.tech/i.test(final)) {
        log('  STOP login wall', final);
        await page.close();
        continue;
      }
      await dismiss(page);
      const status = res && res.status();
      log('  status', status, 'final', final);
      const S = new Shooter(page, prefix + name + '-light', width, height, dpr);
      if (spec.run) await spec.run(page, S);
      else { await S.view('default'); await S.full(); }
    } catch (e) {
      log('  FAILED', name, String(e.message).split('\n')[0]);
    }
    await page.close().catch(() => {});
  }
  await browser.close();
}

const which = process.env.PASS || 'both';
if (which !== 'mobile') await runSet(desktop, { width: 1440, height: 900, dpr: 1, mobile: false, prefix: '' });
if (which !== 'desktop') await runSet(mobile, { width: 390, height: 844, dpr: 2, mobile: true, prefix: 'mobile-' });
log('done', RAW);
