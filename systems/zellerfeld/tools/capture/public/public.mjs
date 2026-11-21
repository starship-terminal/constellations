// Captures Zellerfeld's public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/zellerfeld/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// One light theme. Desktop 1440x900 at 1x, mobile 390x844 at 2x.
// Nothing is submitted. Sign-in, signup, Google, phone, password, passkey,
// newsletter, onboarding fields, fit-profile sizes and checkout are not used.
// A control that opens a login wall is recorded as a screenshot of the wall
// and that branch stops.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideCookies, dismissNotice, launchBrowser, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) { await p.evaluate((yy) => scrollTo(0, yy), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 600);
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
    await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function settle(p) {
  await hideCookies(p);
  await dismissNotice(p);
  await hideCookies(p);
}

async function openNav(p) {
  const desktop = p.locator('button[aria-label="Open navigation"]').filter({ visible: true }).first();
  const mobile = p.getByRole('button', { name: 'Menu', exact: true }).filter({ visible: true }).first();
  if (await desktop.count()) await desktop.click();
  else await mobile.click();
  await p.locator('[role="dialog"][data-state="open"]').first().waitFor({ state: 'visible', timeout: 8000 });
  await wait(p, 700);
}

async function openSearch(p, query) {
  const input = p.locator('input[placeholder="What are you looking for?"]').first();
  if (!(await input.isVisible().catch(() => false))) {
    const menu = p.getByRole('button', { name: 'Menu', exact: true }).filter({ visible: true }).first();
    if (await menu.count()) { await menu.click(); await wait(p, 700); }
  }
  if (await input.isVisible().catch(() => false)) {
    await input.click();
    if (query) await input.fill(query);
  } else if (query) {
    await input.evaluate((el, q) => {
      el.focus();
      const set = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      set.call(el, q);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }, query);
  }
  await wait(p, query ? 1600 : 500);
}

async function openSignIn(p) {
  await p.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => /sign in/i.test(el.innerText || '') && el.getBoundingClientRect().width > 0);
    if (b) b.click();
  });
  await p.getByText('Welcome back').first().waitFor({ state: 'visible', timeout: 8000 });
  await wait(p, 800);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('cookie');
    await settle(p);
    await S.view('default');
    await step('nav', async () => { await openNav(p); await S.view('nav'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await step('search', async () => { await openSearch(p, 'nike'); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('signin', async () => { await openSignIn(p); await S.view('signin'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await S.full();
  } },
  sneakers: { path: '/collections/sneakers', run: async (p, S) => {
    await settle(p);
    await S.view('default');
    await step('sort', async () => {
      const b = p.getByRole('button', { name: /NEW IN/i }).first();
      await b.click();
      await wait(p, 1200);
      await S.view('new-in');
    });
    await S.full();
  } },
  boots: { path: '/collections/boots', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  slides: { path: '/collections/slides', run: async (p, S) => { await settle(p); await S.view('default'); } },
  barefoot: { path: '/collections/barefoot', run: async (p, S) => { await settle(p); await S.view('default'); } },
  product: { path: '/products/pdf-bol-sneaker', run: async (p, S) => {
    await settle(p);
    await S.view('default');
    await step('gallery', async () => {
      const b = p.getByRole('button', { name: 'Show image 2' }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('gallery'); }
    });
    await step('more', async () => {
      const b = p.getByRole('button', { name: /SHOW MORE/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('more'); }
    });
    await step('wishlist', async () => {
      const b = p.getByRole('button', { name: /wishlist/i }).first();
      if (await b.count()) {
        await b.click();
        await p.getByText('Welcome back').first().waitFor({ timeout: 8000 });
        await wait(p, 600);
        await S.view('wishlist-signin');
        await p.keyboard.press('Escape');
        await wait(p, 400);
      }
    });
    await step('fit', async () => {
      const b = p.getByRole('button', { name: /BUY NOW/i }).first();
      if (await b.count()) {
        await b.click();
        await p.getByText('Fit Profile').first().waitFor({ timeout: 8000 });
        await wait(p, 700);
        await S.view('fit-dialog');
        await p.keyboard.press('Escape');
      }
    });
    await S.full();
  } },
  creators: { path: '/creators', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  creator: { path: '/creators/nike', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  reviews: { path: '/pages/customer-reviews', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  faq: { path: '/pages/faq', run: async (p, S) => {
    await settle(p);
    await S.view('default');
    await step('open', async () => {
      const s = p.locator('summary').first();
      if (await s.count()) { await s.click(); await wait(p, 500); await S.view('open'); }
    });
    await S.full();
  } },
  scan: { path: '/pages/how-to-scan-your-feet', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  careers: { path: '/pages/careers', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  letter: { path: '/pages/why-zellerfeld', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  newsletter: { path: '/pages/newsletter', run: async (p, S) => { await settle(p); await S.view('default'); } },
  privacy: { path: '/policies/privacy-policy', run: async (p, S) => { await settle(p); await S.view('default'); } },
  shipping: { path: '/policies/shipping-policy', run: async (p, S) => { await settle(p); await S.view('default'); } },
  terms: { path: '/policies/terms-of-service', run: async (p, S) => { await settle(p); await S.view('default'); } },
  choices: { path: '/pages/data-sharing-opt-out', run: async (p, S) => { await settle(p); await S.view('default'); } },
  gifts: { path: '/collections/gift-cards', run: async (p, S) => { await settle(p); await S.view('default'); } },
  notfound: { path: '/privacy-policy', run: async (p, S) => { await settle(p); await S.view('default'); } },
  onboarding: { path: '/onboarding', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/sign-in', run: async (p, S) => { await S.view('default'); } },
  help: { path: 'https://help.zellerfeld.com/hc/en-us', absolute: true, run: async (p, S) => { await S.view('default'); await S.full(); } },
  studio: { path: 'https://studio.zellerfeld.com/', absolute: true, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('cookie');
    await settle(p);
    await S.view('default');
    await step('nav', async () => { await openNav(p); await S.view('nav'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('search', async () => { await openSearch(p, 'nike'); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await S.full();
  } },
  sneakers: { path: '/collections/sneakers', run: async (p, S) => { await settle(p); await S.view('default'); await S.full(); } },
  product: { path: '/products/pdf-bol-sneaker', run: async (p, S) => {
    await settle(p);
    await S.view('default');
    await step('fit', async () => {
      const b = p.getByRole('button', { name: /BUY NOW/i }).first();
      if (await b.count()) {
        await b.click();
        await p.getByText('Fit Profile').first().waitFor({ timeout: 8000 });
        await wait(p, 600);
        await S.view('fit-dialog');
        await p.keyboard.press('Escape');
      }
    });
    await S.full();
  } },
  creators: { path: '/creators', run: async (p, S) => { await settle(p); await S.view('default'); } },
  faq: { path: '/pages/faq', run: async (p, S) => {
    await settle(p);
    await S.view('default');
    await step('open', async () => {
      const s = p.locator('summary').first();
      if (await s.count()) { await s.click(); await wait(p, 400); await S.view('open'); }
    });
  } },
  reviews: { path: '/pages/customer-reviews', run: async (p, S) => { await settle(p); await S.view('default'); } },
  scan: { path: '/pages/how-to-scan-your-feet', run: async (p, S) => { await settle(p); await S.view('default'); } },
  notfound: { path: '/privacy-policy', run: async (p, S) => { await settle(p); await S.view('default'); } },
  signin: { path: '/sign-in', run: async (p, S) => { await S.view('default'); } },
  onboarding: { path: '/onboarding', run: async (p, S) => { await S.view('default'); } },
};

const browser = await launchBrowser();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.absolute ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await p.addStyleTag({ content: 'html{scrollbar-width:none}::-webkit-scrollbar{width:0;height:0}' }).catch(() => {});
    await wait(p, spec.wait || 3500);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
