// Captures DoorDash's public signed-out pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// BOUNDARY: every live *.doordash.com route Cloudflare-blocks this client
// (403; the "Performing security verification" challenge never resolves in
// headless or headed Chrome). The pages below are therefore rendered from
// the product's own content in the Internet Archive's Wayback Machine —
// PAGES maps each name to "<snapshot timestamp>/<original url>". The
// Wayback Machine's injected toolbar is hidden, never answered. Snapshot
// dates are October–November 2026 archive captures of the real SSR pages;
// this is archival evidence, not a live capture.
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The
// consumer-web-next stack (Next.js SSR + styled-components over the prism
// token system) paints light only — no dark theme is published. Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8
// chunks and the log records the boundary. Nothing is sent, ordered,
// searched into an address gate or signed into: the only presses are local
// UI toggles — the Top Cities/Cuisines/Chains tabs, a "Show more" reveal
// and the mobile hamburger. The cookie banner and dormant Turnstile nodes
// are hidden, never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, open } from './lib.mjs';

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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Wayback snapshot routes: "<capture timestamp>/<original URL>". Recorded
// also in systems/doordash/raw/archive-urls.json by vars.mjs.
const PAGES = {
  home: '20261112001404/https://www.doordash.com/',
  'food-delivery': '20261004033917/https://www.doordash.com/food-delivery/',
  business: '20261012092322/https://www.doordash.com/en-US/business/',
  dashpass: '20261012183135/https://www.doordash.com/en-US/dashpass/student',
  restaurants: '20261005002021/https://www.doordash.com/en-US/restaurants-near-me/',
  store: '20261024031734/https://www.doordash.com/en-US/store/the-sweet-tooth-north-miami-beach-33434247/',
  hsa: '20260930222321/https://www.doordash.com/en-US/p/hsa-fsa-store',
  seasonal: '20261025153234/https://www.doordash.com/en-US/p/seasonal-holidays/',
  promos: '20261008212700/https://www.doordash.com/en-US/promos/',
  careers: '20261009000533/https://careersatdoordash.com/',
};

const desktop = {
  home: { path: PAGES.home, wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('tab-cuisines', async () => {
      // A local reveal: the tab list swaps the city list for a cuisine list.
      const t = p.locator('[data-testid="tab-topcuisines-not-selected"]').first();
      if (await t.count()) { await t.scrollIntoViewIfNeeded(); await clickEl(t); await wait(p, 1200); await S.view('cuisines'); }
    });
    await S.full();
  } },
  'food-delivery': { path: PAGES['food-delivery'], wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  business: { path: PAGES.business, wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  dashpass: { path: PAGES.dashpass, wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  restaurants: { path: PAGES.restaurants, wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  store: { path: PAGES.store, wait: 14000, run: async (p, S) => {
    await S.view('default');
    await step('pickup-toggle', async () => {
      // Local UI state: flips the storefront header between Delivery and
      // Pickup; never an address entry or an order action.
      const t = p.locator('[data-testid="MenuOrderMethodTogglePickup"]').first();
      if (await t.count()) { await t.scrollIntoViewIfNeeded(); await clickEl(t); await wait(p, 1200); await S.view('pickup'); }
    });
    await S.full();
  } },
  hsa: { path: PAGES.hsa, wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  seasonal: { path: PAGES.seasonal, wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  promos: { path: PAGES.promos, wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  careers: { path: PAGES.careers, wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: PAGES.home, wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  store: { path: PAGES.store, wait: 14000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('[data-testid="hamburger"]').first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  'food-delivery': { path: PAGES['food-delivery'], wait: 10000, run: async (p, S) => {
    await S.view('default');
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
      await open(p, BASE + spec.path, { wait: spec.wait || 7000, promo: 'keep' });
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
