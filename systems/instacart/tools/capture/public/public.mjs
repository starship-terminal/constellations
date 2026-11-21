// Captures Instacart's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// Instacart's consumer site paints one light theme (no theme toggle on the
// public surface), so every shot is -light. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x. A page taller than one GPU texture is saved as
// name.partN.png tiles; an unbounded page truncates at 8 chunks.
// Nothing is ordered, paid for, or signed into. The only activations are
// local UI toggles: the departments drawer, a filter chip, the login card
// (never submitted). Consent and location overlays are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideOverlays, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 600);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    await lazyScroll(p);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    try {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    } catch (e) {
      log('  ! full shot failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function shotPage(context, spec, name, mobile) {
  const page = await context.newPage();
  const url = BASE + spec.path;
  log('PAGE', name, url);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(page, spec.wait || 3500);
    await hideOverlays(page);
    const vw = mobile ? 390 : 1440;
    const vh = mobile ? 844 : 900;
    const dpr = mobile ? 2 : 1;
    const S = new Shooter(page, name + '-light', vw, vh, dpr, url.split('?')[0]);
    await spec.run(page, S);
    log('  done', name, S.count);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
  }
  await page.close().catch(() => {});
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('departments', async () => {
      const b = p.getByRole('button', { name: /main menu/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 900); await hideOverlays(p); await S.view('departments'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await step('search-focused', async () => {
      const s = p.getByRole('textbox', { name: /search/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 600); await S.view('search-focused'); await p.keyboard.press('Escape'); }
    });
  } },
  'grocery-delivery': { path: '/grocery-delivery', run: async (p, S) => { await S.view('default'); await S.full(); } },
  deals: { path: '/store/hub/deals_tab', run: async (p, S) => { await S.view('default'); await S.full(); } },
  food: { path: '/categories/316-food', run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { path: '/store/s?k=milk', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/help', run: async (p, S) => { await S.view('default'); await S.full(); } },
  business: { path: '/business', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gifts: { path: '/store/hub/gifts', run: async (p, S) => { await S.view('default'); await S.full(); } },
  plus: { path: '/instacart-plus', run: async (p, S) => { await S.view('default'); await S.full(); } },
  promos: { path: '/promos-and-coupons', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'gift-cards': { path: '/p/gift-cards', run: async (p, S) => { await S.view('default'); await S.full(); } },
  ebt: { path: '/ebt-snap', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => {
    await S.view('default');
    // The email field is not focused and Continue is not clicked. An empty
    // submit opens a reCAPTCHA, and this pass does not type an email.
  } },
  signup: { path: '/signup', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /main menu/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 900); await hideOverlays(p); await S.view('menu'); }
    });
  } },
  'grocery-delivery': { path: '/grocery-delivery', run: async (p, S) => { await S.view('default'); } },
  search: { path: '/store/s?k=milk', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help', run: async (p, S) => { await S.view('default'); } },
  plus: { path: '/instacart-plus', run: async (p, S) => { await S.view('default'); } },
  promos: { path: '/promos-and-coupons', run: async (p, S) => { await S.view('default'); } },
};

// Automation is not hidden: no AutomationControlled flag, no webdriver mask.
const browser = await chromium.launch();
const desktopCtx = await browser.newContext({
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US',
});
const mobileCtx = await browser.newContext({
  viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US',
});

for (const [k, spec] of Object.entries(desktop)) {
  const name = k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  await shotPage(desktopCtx, spec, name, false);
}
for (const [k, spec] of Object.entries(mobile)) {
  const name = 'mobile-' + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  await shotPage(mobileCtx, spec, name, true);
}
await browser.close();
log('capture done', RAW);
