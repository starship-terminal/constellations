// Captures bloomberg.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the Sign In sheet
// (an iframe the button mounts), the mobile Menu, and the "Bloomberg the Company" sitemap dropdown.
// The media-ui privacy-preferences modal is captured first, then hidden — never answered (its
// checkbox and buttons are never clicked). The paywall fence is page content and is never crossed.
// PerimeterX can gate a route for this client: a blocked route is logged BLOCKED, not retried.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  // A shot without closePromo, but only while the privacy modal is actually
  // mounted — it does not appear on every load, so a blind shot would be a
  // duplicate of default labelled as consent.
  async raw(name) {
    const up = await this.p.evaluate(() => { const e = document.querySelector('[class*="media-ui-Privacy_wrapper"]'); return !!(e && e.offsetParent); }).catch(() => false);
    if (!up) { log('  (privacy modal not mounted; skipping', name + ')'); return; }
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
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

// The first /news/articles/ link on the home front: the article route is
// discovered at run time because headlines churn daily. The URL is recorded
// in the log; the article body itself is always behind the paywall.
const firstArticle = async (p, base) => {
  await p.goto(base + '/asia', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await clearChallenge(p); await wait(p, 7000);
  const href = await p.evaluate(() => {
    const a = [...document.querySelectorAll('a[href*="/news/articles/"]')].find((x) => x.offsetParent);
    return a ? a.getAttribute('href') : null;
  });
  if (!href) { log('  no article link found'); return null; }
  const u = new URL(href, base);
  u.search = ''; // drop ?srnd tracking params
  log('  article ->', u.toString());
  return u.toString();
};

// "Bloomberg the Company & Its Products" toggles the sitemap dropdown in place.
const openSitemap = async (p) => {
  const m = p.locator('button, a').filter({ hasText: /Bloomberg the Company/i }).filter({ visible: true }).first();
  if (await m.count()) { await clickEl(m); await wait(p, 1200); return true; }
  return false;
};

// The Sign In button mounts the /account/iframe/login sheet: a local toggle.
const openSignIn = async (p) => {
  const m = p.locator('button[class*="signInButton" i], button').filter({ hasText: /^Sign In$/ }).filter({ visible: true }).first();
  if (await m.count()) { await clickEl(m); await wait(p, 2500); return true; }
  return false;
};

const desktop = {
  home: { path: '/asia', wait: 9000, run: async (p, S) => {
    await S.raw('privacy');                       // the privacy modal as it arrives
    await S.view('default');
    await step('sitemap', async () => { if (await openSitemap(p)) await S.view('sitemap'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await step('signin', async () => { if (await openSignIn(p)) await S.view('signin'); await p.keyboard.press('Escape'); await wait(p, 600); });
    await S.full();
  } },
  markets: { path: '/markets', run: async (p, S) => {
    await S.raw('privacy');
    await S.view('default');
    await S.full();
  } },
  economics: { path: '/economics', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  article: { path: null, run: async (p, S) => {   // URL resolved at run time from the home front
    const url = await firstArticle(p, BASE);
    if (!url) return;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge (article)'); return; }
    await wait(p, 8000);
    await S.view('default');
    await S.full();
  } },
  quote: { path: '/quote/SPX:IND', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  live: { path: '/live', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  subscriptions: { path: '/subscriptions', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/asia', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[class*="menuMobile" i], button').filter({ hasText: /^Menu$/ }).filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
    await S.full();
  } },
  article: { path: null, run: async (p, S) => {
    const url = await firstArticle(p, BASE);
    if (!url) return;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge (article)'); return; }
    await wait(p, 8000);
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
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
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
