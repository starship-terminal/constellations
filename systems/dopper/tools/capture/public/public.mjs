// Captures dopper.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Two hosts, one brand
// system: the Next.js marketing site (BASE) and the Magento storefront (SHOP). Every captured
// surface paints light. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing
// is sent, bought, booked or signed into: the only presses are local UI toggles — the home
// product-selector tabs, a nav flyout trigger, the mobile menu and the PLP filter sheet. The
// Cookiebot consent dialog and the chat widget are hidden, never answered; the checkout, account
// and add-to-cart actions are never followed.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, SHOP } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
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
    if (H > MAXH) {
      log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
      // quantize.py folds this marker into the stitched shot's .capture.json.
      fs.writeFileSync(`${f}.truncated.json`, JSON.stringify({ truncated: true, documentHeight: H, capturedHeight: hCap, chunkCap: 8, note: 'page exceeded the 8-chunk cap; the tail below it was never captured' }, null, 1) + '\n');
    }
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The "Bottle" nav item may open a flyout (a click or hover toggles it). Local
// UI only, never a link. The trigger lives inside DOPPER-NAVIGATION's shadow
// root, which document.querySelectorAll cannot reach — a Playwright locator
// pierces shadow DOM. The menu only counts as open when its own copy paints
// inside the shadow root or a fixed/absolute overlay: the static "Explore our
// solutions" section carries the same words.
const flyoutOpen = (p) => p.evaluate(() => {
  const nav = document.querySelector('dopper-navigation');
  const inOverlay = (e) => {
    for (let n = e; n; n = n.parentElement || (n.getRootNode && n.getRootNode().host)) {
      if (n === document.body) break;
      const cs = getComputedStyle(n);
      if (cs.position === 'fixed' || cs.position === 'absolute') return true;
    }
    return false;
  };
  const roots = [nav && nav.shadowRoot, document].filter(Boolean);
  return roots.some((r) => [...r.querySelectorAll('h1,h2,h3,h4,p,div,span')]
    .some((e) => /range of reusable|everyone can just refill/i.test(e.innerText || '') && e.getBoundingClientRect().height > 0 && (r !== document || inOverlay(e))));
});
async function openFlyout(p, S) {
  const el = p.locator('dopper-navigation button').filter({ hasText: /^\s*Bottle\s*$/ }).filter({ visible: true }).first();
  if (!(await el.count())) throw new Error('flyout trigger not found in dopper-navigation');
  await el.hover().catch(() => {});
  await wait(p, 900);
  if (!(await flyoutOpen(p))) await el.click().catch(() => el.evaluate((e) => e.click()));
  await wait(p, 1400);
  if (!(await flyoutOpen(p))) throw new Error('flyout did not open — no menu shot saved');
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { base: BASE, path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('flyout', async () => { await openFlyout(p, S); });
    await step('producttab', async () => {
      // The home product selector's own tabs (Travel Mug / Insulated / Steel /
      // Original / Accessories) — local UI state, no navigation.
      const t = p.locator('button').filter({ hasText: /^\s*Insulated\s/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1600); await S.view('tab'); }
    });
    await S.full();
  } },
  mission: { base: BASE, path: '/en/mission/story', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-insulated': { base: BASE, path: '/en/products/insulated', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { base: BASE, path: '/en/blog/just-refill', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  shop: { base: SHOP, path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  category: { base: SHOP, path: '/bottles', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { base: SHOP, path: '/dopper-original-pacific-blue', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { base: SHOP, path: '/checkout/cart/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { base: SHOP, path: '/customer/account/login/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { base: BASE, path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], button[aria-label*="navigation" i], [role="button"][aria-label*="menu" i], button:has(svg)').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); }
    });
    await S.full();
  } },
  shop: { base: SHOP, path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  category: { base: SHOP, path: '/bottles', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const f = p.locator('button').filter({ hasText: /^\s*Filters?\s*$/ }).filter({ visible: true }).first();
      if (await f.count()) { await clickEl(f); await wait(p, 1600); await S.view('filter'); }
    });
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(spec.base + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
