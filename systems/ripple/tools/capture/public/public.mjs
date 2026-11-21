// Captures ripple.com's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. The public site has one light theme.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x.
// Nothing is submitted. The cookie banner is hidden, never clicked.
// Customer Login (home.ripple.com) is a wall and is not opened here.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, patch } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'ripple', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n === `${path.basename(f)}.png`)) {
      // leave previous files; overwrite below
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  await btn.click({ timeout: 8000 });
  await wait(p, 700);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('products-menu', async () => {
      await openMenu(p, 'Products');
      await S.view('products-menu');
      await p.keyboard.press('Escape');
      await p.mouse.click(20, 860);
      await wait(p, 250);
    });
    await step('search', async () => {
      await p.getByRole('button', { name: 'Open search' }).click({ timeout: 8000 });
      await wait(p, 600);
      await S.view('search');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('language', async () => {
      await p.getByRole('button', { name: 'Change language' }).click({ timeout: 8000 });
      await wait(p, 500);
      await S.view('language');
      await p.keyboard.press('Escape');
      await wait(p, 250);
    });
    await step('slide-2', async () => {
      const b = p.getByRole('button', { name: 'Go to slide 2' });
      if (await b.count()) {
        await b.first().click({ timeout: 4000 });
        await wait(p, 800);
        await S.view('slide-2');
      }
    });
    await S.full();
  } },
  payments: { path: '/products/cross-border-payments/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  usecase: { path: '/use-case/accept-stablecoin-payments/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  customers: { path: '/customers/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  insights: { path: '/insights/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  faq: { path: '/faq/', run: async (p, S) => {
    await S.view('default');
    await step('item-open', async () => {
      const item = p.locator('button, summary, [aria-expanded="false"]').filter({ hasText: /what|how|ripple/i }).first();
      if (await item.count()) {
        await item.click({ timeout: 5000 });
        await wait(p, 600);
        await S.view('item-open');
      }
    });
    await S.full();
  } },
  company: { path: '/company/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/legal/terms-of-use/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'pt-br': { path: '/pt-br/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const opened = await p.evaluate(() => {
        const buttons = [...document.querySelectorAll('button')];
        const menu = buttons.find((b) => /menu|navigation/i.test(b.getAttribute('aria-label') || b.innerText || ''));
        if (!menu) return false;
        menu.click();
        return true;
      });
      if (!opened) {
        const b = p.locator('header button').last();
        if (await b.count()) await b.click({ timeout: 4000 });
      }
      await wait(p, 800);
      await hideConsent(p);
      await S.view('menu');
    });
    await S.full();
  } },
  payments: { path: '/products/cross-border-payments/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  faq: { path: '/faq/', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact/', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2500);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
