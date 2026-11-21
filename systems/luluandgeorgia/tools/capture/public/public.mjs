// Captures luluandgeorgia.com's public signed-out pages.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a mobile- prefix.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Full pages cap at 8 chunks.
// Nothing is signed into, added to cart, or submitted. Consent (DataGrail)
// and the Klaviyo newsletter embed are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, hideOverlays, clearChallenge, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 8 * 7000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 600);
  await hideOverlays(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    await this.p.evaluate(() => scrollTo(0, 0)).catch(() => {});
    await wait(this.p, 300);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
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
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Local UI only. Never Add to cart, Sign In, checkout, or a form submit.
async function openSearch(p) {
  // Focus only. Do not type a query and do not submit.
  const input = p.locator('input.marqo-header-search__input, input[name="q"][type="search"]').first();
  await input.click({ timeout: 5000 });
  await wait(p, 600);
}

async function openAccountDrawer(p) {
  const b = p.locator('button.js-account-toggle').first();
  await b.click({ timeout: 5000 });
  await wait(p, 800);
}

async function openCartDrawer(p) {
  const b = p.locator('a.js-cart-drawer-toggle, a.cart-drawer-toggle').first();
  await b.click({ timeout: 5000 });
  await wait(p, 800);
}

async function openNav(p) {
  // The class string is longer than a strict locator match, and hidden mobile
  // copies share the word. Hover the visible desktop link by its box.
  const box = await p.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((el) => (el.innerText || '').trim() === 'FURNITURE' && el.getBoundingClientRect().width > 20);
    if (!a) return null;
    const r = a.getBoundingClientRect();
    return { x: r.x, y: r.y, w: r.width, h: r.height };
  });
  if (!box) throw new Error('FURNITURE link has no box');
  await p.mouse.move(box.x + box.w / 2, box.y + box.h / 2);
  await wait(p, 800);
  const open = await p.evaluate(() => [...document.querySelectorAll('.nav-dropdown')].some((d) => {
    const s = getComputedStyle(d);
    return s.visibility === 'visible' && d.getBoundingClientRect().height > 40 && /All Furniture/.test(d.innerText || '');
  }));
  if (!open) throw new Error('furniture mega-menu did not open');
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => { await openNav(p); await S.view('nav'); await p.mouse.move(10, 800); await wait(p, 300); });
    await step('footer', async () => {
      // Headless Chromium collapses .site-footer (inner column display:none,
      // footer height 0). Set display on the elements themselves. A stylesheet
      // injection did not stick. This does not click or submit.
      await p.evaluate(() => {
        const el = document.querySelector('.site-footer');
        if (!el) return;
        el.style.setProperty('display', 'block', 'important');
        el.style.setProperty('height', 'auto', 'important');
        const inner = el.querySelector('.max-w-screen-xl');
        if (inner) inner.style.setProperty('display', 'block', 'important');
        const top = el.getBoundingClientRect().top + window.scrollY;
        const h = el.getBoundingClientRect().height;
        window.scrollTo(0, Math.max(0, top + h - window.innerHeight + 8));
      });
      await wait(p, 400);
      await hideOverlays(p);
      await S.view('footer');
      await p.evaluate(() => scrollTo(0, 0));
      await wait(p, 200);
    });
    await step('search', async () => { await openSearch(p); await S.view('search'); await p.keyboard.press('Escape'); });
    await step('account', async () => { await openAccountDrawer(p); await S.view('account'); await p.keyboard.press('Escape'); });
    await step('cart', async () => { await openCartDrawer(p); await S.view('cart'); await p.keyboard.press('Escape'); });
  } },
  collection: { path: '/collections/furniture', run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const b = p.getByRole('button', { name: /filter|sort/i }).first();
      if (await b.count()) { await b.click({ timeout: 4000 }); await wait(p, 800); await S.view('filter'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  product: { path: '/products/sachs-dining-table', run: async (p, S) => {
    await S.view('default');
    await step('details', async () => {
      const b = p.getByText('Shipping & Returns', { exact: false }).first();
      if (await b.count()) { await b.click({ timeout: 4000 }); await wait(p, 600); await S.view('details'); }
    });
    await S.full();
  } },
  search: { path: '/search?q=rug&type=product', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'search-empty': { path: '/search?q=zzznomatchlg999&type=product', run: async (p, S) => {
    await S.view('default');
  } },
  about: { path: '/pages/about-us', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/account/login', run: async (p, S) => {
    // Photograph the wall empty. Do not type, submit, or click an identity provider.
    await S.view('default');
  } },
  signup: { path: '/account/register', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.locator('a.js-menu-toggle, button.js-menu-toggle, .header__menu-toggle').first();
      if (await b.count()) { await b.click({ timeout: 4000 }); await wait(p, 800); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  collection: { path: '/collections/furniture', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
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
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await clearChallenge(p);
    await wait(p, spec.wait || 4000);
    await hideOverlays(p);
    const meta = await p.evaluate(() => ({
      w: window.innerWidth, h: window.innerHeight, dpr: window.devicePixelRatio,
      vv: window.visualViewport && { w: window.visualViewport.width, h: window.visualViewport.height, s: window.visualViewport.scale },
    }));
    log('  viewport', JSON.stringify(meta));
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
