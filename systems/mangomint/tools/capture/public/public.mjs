// Captures Mangomint public signed-out pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, prefixed mobile-.
// The Mira promo strip is hidden, never clicked. Demo, trial, login and
// booking forms are never submitted. No appointment is booked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, APP, BOOK, hidePromo } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mangomint', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function settle(p) {
  await hidePromo(p);
  await p.evaluate(() => {
    document.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch {} });
  }).catch(() => {});
}

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 16; i++) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (h === last && i > 2) break;
    last = h;
    const y = Math.min(i * 700, Math.max(0, h - 800));
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 350);
  await hidePromo(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await settle(this.p);
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(path.join(RAW, old));
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('businesses', async () => {
      const btn = p.locator('button[class*="desktopNavbarDropdown"]').filter({ hasText: 'Businesses' }).first();
      await btn.click({ timeout: 8000 });
      await wait(p, 500);
      await S.view('businesses');
      await p.keyboard.press('Escape');
      await wait(p, 200);
    });
    await step('features', async () => {
      const btn = p.locator('button[class*="desktopNavbarDropdown"]').filter({ hasText: /^Features$/ }).first();
      await btn.click({ timeout: 8000 });
      await wait(p, 500);
      await S.view('features');
      await p.keyboard.press('Escape');
    });
  } },
  pricing: { url: BASE + '/pricing/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => {
      const q = p.locator('[class*="faqs-module--questionButton"]').filter({ hasText: 'Who counts as a user' }).first();
      await q.scrollIntoViewIfNeeded();
      await q.click();
      await wait(p, 400);
      await S.view('faq-open');
    });
  } },
  booking: { url: BASE + '/features/online-booking/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  book: { url: BOOK, run: async (p, S) => {
    await wait(p, 2000);
    await S.view('default');
  } },
  login: { url: APP + '/login', run: async (p, S) => { await S.view('default'); } },
  'forgot-password': { url: APP + '/forgot-password', run: async (p, S) => { await S.view('default'); } },
  demo: { url: BASE + '/demo/', run: async (p, S) => { await S.view('default'); } },
  trial: { url: BASE + '/trial/', run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about-us/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  customers: { url: BASE + '/go/customers/', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog/', run: async (p, S) => { await S.view('default'); } },
  contact: { url: BASE + '/contact-us/', run: async (p, S) => { await S.view('default'); } },
  learn: { url: BASE + '/learn/', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/legal/privacy-policy/', run: async (p, S) => { await S.view('default'); } },
  notfound: { url: BASE + '/login', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      await p.getByRole('button', { name: 'Toggle the navigation' }).click();
      await p.locator('[class*="mobileNavbar"]').getByText('Businesses', { exact: true }).first().waitFor({ state: 'visible', timeout: 8000 }).catch(() => {});
      await wait(p, 1800);
      await S.view('menu');
    });
  } },
  pricing: { url: BASE + '/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  booking: { url: BASE + '/features/online-booking/', run: async (p, S) => { await S.view('default'); } },
  book: { url: BOOK, dpr: 1, run: async (p, S) => { await wait(p, 1800); await S.view('default'); } },
  login: { url: APP + '/login', dpr: 1, run: async (p, S) => { await S.view('default'); } },
  demo: { url: BASE + '/demo/', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = spec.dpr || (mob ? 2 : 1);
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    const sel = '[class*="banner-module--banner"]';
    const hide = () => document.querySelectorAll(sel).forEach((el) => el.style.setProperty('display', 'none', 'important'));
    const start = () => new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    if (document.documentElement) start();
  });
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 70000 });
    await wait(p, 2600);
    await hidePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
