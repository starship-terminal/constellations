// Captures elektron.se's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. elektron.se paints a
// single dark theme, so the theme slot is `dark`. Desktop shots are 1440x900 at 1x, mobile 390x844
// at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png tiles,
// which quantize.py stitches back together; an unbounded page truncates at 8 chunks and the log
// records the boundary. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's Search / Catalog / Account modal triggers, a product accordion and the
// mobile menu. The #thedock-cookie-banner consent modal is hidden, never answered; checkout,
// my-account past the magic-login form and every external link are never reached.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (the kit's default); quantize.py writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'elektron', 'raw-shots') + '/';
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The header's Search / Account anchors point at #id-* modal sections
// (modal-layout-dropdown / drawer-right): a click opens them as local UI,
// never a submission. Catalog is a plain link to /explore. The header mounts
// a mobile copy too — the trigger is picked inside the desktop .is-main-menu
// bar. hasText is a substring match: the anchors' textContent carries the
// injected icon <style> text, so an anchored label match fails.
const navTrigger = (p, text) => p.locator('.is-main-menu a').filter({ hasText: new RegExp(text) }).filter({ visible: true }).first();

async function openHeaderModal(p, S, text, name, close = true) {
  const t = navTrigger(p, text);
  if (!(await t.count())) { log('  ! no header trigger', text); return; }
  await clickEl(t);
  await wait(p, 1600);
  await S.view(name);
  if (close) {
    const x = p.locator('.modal-close').filter({ visible: true }).first();
    if (await x.count()) await clickEl(x); else await p.keyboard.press('Escape');
    await wait(p, 800);
  }
}

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('search', async () => { await openHeaderModal(p, S, 'Search', 'search'); });
    await step('account', async () => { await openHeaderModal(p, S, 'Account', 'account'); });
    await S.full();
  } },
  shop: { path: '/shop', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-digitakt': { path: '/product/digitakt-ii', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('features', async () => {
      // The "Key Features" accordion block — a local UI toggle.
      const t = p.locator('.block-button').filter({ hasText: /Key Features/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('features'); }
    });
    await S.full();
  } },
  'product-accessory': { path: '/product/pl-2-protective-lid', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  explore: { path: '/explore', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  support: { path: '/support-downloads', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/who-we-are', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/contact-us', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { path: '/cart', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  'my-account': { path: '/my-account', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'store-locator': { path: '/store-locator', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  kulture: { path: '/kulture', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The burger toggles the .is-main-menu-mobile panel — a local UI toggle.
      const m = p.locator('a[href="#menu-trigger"], [class*="menu-trigger"], a[href*="#menu"]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); }
    });
    await S.full();
  } },
  shop: { path: '/shop', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-digitakt': { path: '/product/digitakt-ii', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'dark';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
