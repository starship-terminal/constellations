// Captures Starbucks public pages into RAW (full-colour PNGs).
//
//   RAW=/some/scratch PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Phone shots get a mobile- prefix.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Nothing is submitted.
// Sign-in and sign-up are recorded as walls and not filled.
// The store locator is not screenshotted (street addresses).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, patch, hideCookies, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'starbucks', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 12; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h <= last + 20) break;
    last = h;
    for (let y = 0; y < Math.min(h, 9000); y += 700) {
      await p.evaluate((yy) => scrollTo(0, yy), y);
      await wait(p, 120);
    }
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
    await hideCookies(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideCookies(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
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
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function hover(p, locator) {
  const el = locator.first();
  if (!(await el.count())) return false;
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await el.hover({ force: true }).catch(() => {});
  await wait(p, 350);
  return true;
}

async function focusVisible(p, locator) {
  const el = locator.first();
  if (!(await el.count())) return false;
  await el.focus().catch(() => {});
  await wait(p, 250);
  return true;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-hover', async () => {
      if (await hover(p, p.getByRole('link', { name: 'MENU', exact: true }))) await S.view('nav-hover');
    });
    await step('join-hover', async () => {
      const join = p.getByRole('link', { name: 'Join now' }).first();
      if (await hover(p, join)) await S.view('join-hover');
    });
    await step('footer', async () => {
      const b = p.getByRole('button', { name: 'About Us' }).first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('footer-open'); }
    });
  } },
  menu: { path: '/menu', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('card-hover', async () => {
      const card = p.locator('a[href*="/menu/the-latest/"]').first();
      if (await hover(p, card)) await S.view('card-hover');
    });
  } },
  'menu-category': { path: '/menu/coffee-espresso/hot-coffee-espresso', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'menu-holiday': { path: '/menu/the-latest/holiday-classics', run: async (p, S) => { await S.view('default'); } },
  'menu-favorites': { path: '/menu/favorites', run: async (p, S) => { await S.view('empty'); } },
  'menu-previous': { path: '/menu/previous', run: async (p, S) => { await S.view('empty'); } },
  product: { path: '/menu/product/407/hot', run: async (p, S) => {
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    await S.view('default');
    await step('size', async () => {
      const radio = p.locator('input[name="size"]').nth(1);
      if (await radio.count()) { await radio.check({ force: true }); await wait(p, 400); await S.view('size-selected'); }
    });
    await step('customize', async () => {
      const b = p.getByRole('button', { name: 'Customize' }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('customize'); }
    });
    await step('add-hover', async () => {
      if (await hover(p, p.getByRole('button', { name: 'Add to Order' }))) await S.view('add-hover');
    });
  } },
  rewards: { path: '/rewards', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('stars', async () => {
      const b = p.getByRole('button', { name: /100/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('stars-100'); }
    });
  } },
  partnership: { path: '/rewards/partnerships/marriottbonvoy', run: async (p, S) => { await S.view('default'); } },
  gift: { path: '/gift', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('balance', async () => {
      const b = p.getByRole('button', { name: /Check balance/i }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 800);
        await S.view('balance-dialog');
        await p.keyboard.press('Escape');
      }
    });
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /expire/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 400); await S.view('faq-open'); }
    });
  } },
  'gift-category': { path: '/gift/category/featured', run: async (p, S) => { await S.view('default'); } },
  'gift-card': { path: '/gift/00000208', run: async (p, S) => {
    // Form is visible and empty. Do not type. Do not submit.
    await S.view('form-empty');
    await step('amount-focus', async () => {
      const sel = p.locator('select[name="amount"]').first();
      if (await sel.count()) { await sel.focus(); await wait(p, 300); await S.view('amount-focus'); }
    });
  } },
  'gift-howto': { path: '/how-to-gift-a-starbucks-gift-card', run: async (p, S) => { await S.view('default'); } },
  featured: { path: '/discover/featured-menu', run: async (p, S) => { await S.view('default'); await S.full(); } },
  ordering: { path: '/stores-and-ordering', run: async (p, S) => { await S.view('default'); } },
  delivery: { path: '/stores-and-ordering/delivery', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /Ordering Delivery with the Starbucks/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 400); await S.view('faq-open'); }
    });
  } },
  app: { path: '/download-app', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/terms/privacy-notice', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms/starbucks-terms-of-use', run: async (p, S) => { await S.view('default'); } },
  health: { path: '/consumer-health-data-privacy-notice', run: async (p, S) => { await S.view('default'); } },
  'do-not-sell': { path: '/personal-information', run: async (p, S) => {
    // Email field is present. Do not type. Do not submit.
    await S.view('form-empty');
  } },
  'rewards-terms': { path: '/terms/rewards', run: async (p, S) => { await S.view('default'); } },
  landlord: { path: '/business/landlord-faq', run: async (p, S) => { await S.view('default'); } },
  suppliers: { path: '/business/suppliers', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/responsibility/reporting-hub', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/account/signin', run: async (p, S) => {
    // Wall. Record the empty form. Do not type an email. Do not submit.
    await wait(p, 1500);
    await S.view('wall');
    await step('focus', async () => {
      const user = p.locator('#username');
      if (await user.count()) { await user.focus(); await wait(p, 300); await S.view('email-focus'); }
    });
  } },
  signup: { path: '/account/create', run: async (p, S) => {
    await wait(p, 1500);
    await S.view('wall');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Open menu' });
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('menu'); }
    });
  } },
  menu: { path: '/menu', run: async (p, S) => { await S.view('default'); } },
  product: { path: '/menu/product/407/hot', run: async (p, S) => { await S.view('default'); } },
  rewards: { path: '/rewards', run: async (p, S) => { await S.view('default'); } },
  gift: { path: '/gift', run: async (p, S) => { await S.view('default'); } },
  featured: { path: '/discover/featured-menu', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/account/signin', run: async (p, S) => { await wait(p, 1500); await S.view('wall'); } },
  notfound: { path: '/responsibility/reporting-hub', run: async (p, S) => { await S.view('default'); } },
  app: { path: '/download-app', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
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
    await open(p, BASE + spec.path, { wait: spec.wait || 2800 });
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
