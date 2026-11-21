// Captures discord.com's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/discord/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x, named
// mobile-*. A page taller than one GPU texture is tiled; an unbounded page
// truncates at 8 chunks.
//
// Nothing is submitted. Login, register, identity providers, download
// installers and Cookie Settings are never clicked. The only presses are
// local UI: hover a nav dropdown, open the language list, open the phone menu.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'discord', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 700);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
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
    await wait(p, 400);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openPage(p, urlPath, waitMs = 2500) {
  await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, waitMs);
  await closePromo(p);
}

async function hoverMenu(p, title) {
  // The phone burger duplicates these toggles at 0x0. Hover only a visible one.
  const toggles = p.locator('.nav_dd_trigger').filter({ hasText: title });
  const n = await toggles.count();
  for (let i = 0; i < n; i++) {
    const box = await toggles.nth(i).boundingBox();
    if (box && box.width > 20 && box.height > 10 && box.y < 120) {
      await toggles.nth(i).hover();
      await wait(p, 700);
      return;
    }
  }
  throw new Error('no visible nav toggle for ' + title);
}

const desktop = {
  home: { path: '/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-discover', async () => { await hoverMenu(p, 'Discover'); await S.view('menu-discover'); await p.mouse.move(10, 400); await wait(p, 300); });
    await step('menu-safety', async () => { await hoverMenu(p, 'Safety'); await S.view('menu-safety'); await p.mouse.move(10, 400); await wait(p, 300); });
    await step('menu-developers', async () => { await hoverMenu(p, 'Developers'); await S.view('menu-developers'); await p.mouse.move(10, 400); await wait(p, 300); });
    await step('language', async () => {
      await p.evaluate(() => scrollTo(0, document.body.scrollHeight));
      await wait(p, 500);
      const lang = p.locator('.dropdown-language .w-dropdown-toggle, [class*="dropdown-language"] .w-dropdown-toggle').first();
      if (await lang.count()) {
        await lang.click();
        await wait(p, 700);
        await S.view('language-menu');
        await p.keyboard.press('Escape');
      }
    });
    await S.full();
  } },
  download: { path: '/download', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  nitro: { path: '/nitro', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  servers: { path: '/servers', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const field = p.locator('input[type="search"], input[name="search"]').first();
      await field.click();
      await wait(p, 400);
      await S.view('search-focused');
      await field.fill('games');
      await wait(p, 800);
      await S.view('search-typed');
      // Do not submit. Clear by selecting and deleting, not by pressing Enter.
      await field.fill('');
    });
    await S.full();
  } },
  safety: { path: '/safety', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const field = p.locator('input[type="search"]').first();
      if (await field.count()) {
        await field.click();
        await wait(p, 400);
        await S.view('search-focused');
      }
    });
  } },
  careers: { path: '/careers', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  quests: { path: '/ads/quests', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  developers: { path: '/developers', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { path: '/company', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  branding: { path: '/branding', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  newsroom: { path: '/newsroom', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  creators: { path: '/creators', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', theme: 'dark', run: async (p, S) => {
    // Wall only. Do not type, do not click identity providers, QR or passkey.
    await S.view('wall');
  } },
  register: { path: '/register', theme: 'dark', run: async (p, S) => {
    await S.view('wall');
  } },
};

const mobile = {
  home: { path: '/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.locator('button[aria-label="Menu"], a[aria-label="Menu"]').first();
      await btn.click();
      await wait(p, 800);
      await S.view('menu');
    });
    await S.full();
  } },
  nitro: { path: '/nitro', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  servers: { path: '/servers', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  download: { path: '/download', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', theme: 'dark', run: async (p, S) => { await S.view('wall'); } },
};

const browser = await chromium.launch({ headless: true });
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const context = await browser.newContext(mob
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  const p = await context.newPage();
  log('open', name, spec.path);
  try {
    await openPage(p, spec.path);
    const theme = spec.theme || 'light';
    const S = new Shooter(p, name + '-' + theme, mob ? 390 : 1440, mob ? 844 : 900, mob ? 2 : 1);
    await spec.run(p, S);
    log('  done', name, S.count);
  } catch (e) {
    log('  FAILED page', name, String(e.message).split('\n')[0]);
  }
  await context.close();
}
await browser.close();
log('raw', RAW);
