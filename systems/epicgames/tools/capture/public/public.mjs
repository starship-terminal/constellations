// Captures epicgames.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. epicgames.com paints
// one theme: dark. store.epicgames.com is the React-SPA storefront on the hashed EDS token layer
// (Discover/Browse/News tabs, hero carousel, game rails, product pages, free-games and launcher
// download), www.epicgames.com/site/home the older OpenSans marketing surface, /id/login the MUI
// sign-in dialog, /help the dark support center. Desktop shots are 1440x900 at 1x, mobile 390x844
// at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png tiles,
// which quantize.py stitches back together; an unbounded page truncates at 8 chunks and the log
// records the boundary. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the Discover search box is typed into for its suggestion dropdown (never submitted)
// and the mobile hamburger. Sign in, Download, Get, Buy, Add to Cart and Wishlist are measured,
// never pressed or followed. Cloudflare challenges a fresh headless context about half the time;
// openWithRetry retries on a fresh context, never clicks the check.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, WWW, LAUNCH_ARGS } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
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
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Types into the Discover search box for the suggestion dropdown — typed and
// left open for the shot, never submitted (no Enter, no result followed).
async function searchOverlay(p, S, name = 'search') {
  const field = p.locator('input[type="search"], input[placeholder*="earch" i], input[aria-label*="earch" i]').filter({ visible: true }).first();
  if (!(await field.count())) { log('  no search field'); return; }
  await field.click({ timeout: 4000 }).catch(() => field.evaluate((el) => el.focus()));
  await p.keyboard.type('fort', { delay: 30 });
  await p.waitForFunction(() => {
    const d = document.querySelector('[role="listbox"], [class*="suggest" i], [class*="dropdown" i], [class*="popover" i]');
    return d && d.getBoundingClientRect().height > 40;
  }, undefined, { timeout: 6000 }).catch(() => {});
  await wait(p, 900);
  await S.view(name);
  await p.keyboard.press('Escape');
  await p.evaluate(() => { const f = document.activeElement; if (f && (f.tagName === 'INPUT')) { f.value = ''; f.blur(); } });
  await wait(p, 500);
}

const desktop = {
  discover: { url: BASE + '/en-US/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('search', () => searchOverlay(p, S));
    await S.full();
  } },
  browse: { url: BASE + '/en-US/browse', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { url: BASE + '/en-US/p/fortnite', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  freegames: { url: BASE + '/en-US/free-games', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  news: { url: BASE + '/en-US/news', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { url: BASE + '/en-US/download', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: WWW + '/id/login/epic', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  sitehome: { url: WWW + '/site/en-US/home', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { url: WWW + '/help/en-US/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  discover: { url: BASE + '/en-US/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const ham = p.locator('button[aria-label*="menu" i], button[aria-label*="navigation" i], [class*="burger" i], [class*="hamburger" i]').filter({ visible: true }).first();
      if (!(await ham.count())) { log('  no hamburger'); return; }
      await clickEl(ham);
      await p.waitForFunction(() => [...document.querySelectorAll('[role="dialog"], nav, aside, [class*="drawer" i], [class*="menu" i]')].some((el) => el.getBoundingClientRect().height > 300 && getComputedStyle(el).visibility !== 'hidden'), undefined, { timeout: 5000 }).catch(() => {});
      await wait(p, 1400);
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await wait(p, 600);
    });
    await S.full();
  } },
  product: { url: BASE + '/en-US/p/fortnite', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch({ args: LAUNCH_ARGS });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  let passed = null;
  for (let i = 0; i < 4 && !passed; i++) {
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    await patch(ctx);
    const p = await ctx.newPage();
    log(name, i ? `(context retry ${i})` : '');
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (await clearChallenge(p, { tries: 6, step: 1800 })) { passed = { ctx, p }; break; }
    await ctx.close();
  }
  if (!passed) { log('  BLOCKED challenge', spec.url); continue; }
  const { ctx, p } = passed;
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
