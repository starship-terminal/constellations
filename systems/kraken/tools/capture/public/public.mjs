// Captures kraken.com public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Signed-out only. Desktop 1440x900 at 1x, phone 390x844 at 2x.
// OneTrust is hidden, never clicked. Sign-in and sign-up are photographed
// at rest; no field is filled and no OAuth control is pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, clearAutofill, patch } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'kraken', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 24; i++) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const y = Math.min(i * 700, Math.max(0, h - 400));
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
    if (h === last && y + 800 >= h) break;
    last = h;
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, theme, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.theme = theme;
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: sourceUrl,
    };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await clearAutofill(this.p);
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const meta = this.requested;
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested, meta);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested, meta);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); } };

async function openSearch(p) {
  const btn = p.locator('button[aria-label="Search"]').first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 700);
  return true;
}

async function openMobileMenu(p) {
  // The rightmost header button has no aria-label. The one beside it is Search.
  // Click only the unlabeled control so the search overlay is not opened instead.
  const ok = await p.evaluate(() => {
    const buttons = [...document.querySelectorAll('header button')].filter((b) => {
      const r = b.getBoundingClientRect();
      const label = (b.getAttribute('aria-label') || '').toLowerCase();
      return r.width > 0 && r.top < 80 && r.height < 48 && !label.includes('search');
    });
    const el = buttons.sort((a, b) => b.getBoundingClientRect().x - a.getBoundingClientRect().x)[0];
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await p.locator('[data-m-menu="1"]').click({ timeout: 4000 }).catch(() => {});
  await wait(p, 900);
  return true;
}

const desktop = {
  home: { url: BASE + '/', theme: 'light', wait: 4500, run: async (p, S) => {
    await S.view('default');
    await step('search', async () => { if (await openSearch(p)) { await S.view('search-open'); await p.keyboard.press('Escape'); await wait(p, 400); } });
    await step('tab', async () => {
      const tab = p.getByRole('tab', { name: 'Futures' }).first();
      if (await tab.count()) { await tab.click(); await wait(p, 800); await S.view('tab-futures'); }
    });
    await S.full();
  } },
  prices: { url: BASE + '/prices', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  bitcoin: { url: BASE + '/prices/bitcoin', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pro: { url: BASE + '/pro', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  wallet: { url: BASE + '/wallet', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  prime: { url: BASE + '/prime', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  vip: { url: BASE + '/vip', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  app: { url: BASE + '/app', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { url: BASE + '/features', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  why: { url: BASE + '/why-kraken', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  learn: { url: BASE + '/learn', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { url: BASE + '/careers', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/legal', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  buy: { url: BASE + '/buy', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  institutions: { url: BASE + '/institutions', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  cli: { url: BASE + '/kraken-cli', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  signup: { url: BASE + '/sign-up', theme: 'light', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  signin: { url: 'https://id.kraken.com/sign-in', theme: 'light', wait: 5000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', theme: 'light', wait: 4500, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); });
    await S.full();
  } },
  prices: { url: BASE + '/prices', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pro: { url: BASE + '/pro', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signup: { url: BASE + '/sign-up', theme: 'light', run: async (p, S) => { await S.view('default'); } },
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
  log(name, spec.theme);
  const theme = spec.theme || 'light';
  const sourceUrl = spec.url.split('?')[0];
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, theme, sourceUrl);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 3500);
    await hideConsent(p);
    await clearAutofill(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
