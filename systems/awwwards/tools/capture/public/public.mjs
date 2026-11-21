// Captures awwwards.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary.
//
// awwwards.com serves headless Chrome a 200 (see lib.mjs). Nothing is voted on, sent, submitted
// or signed into: the only presses are local UI toggles — the winners-grid filter dropdown and the
// mobile menu. The site-detail Vote button is never clicked (voting records a score). Consent or
// promo layers are hidden, never answered (no Accept/Reject is ever clicked); the as-it-arrives
// view is captured before anything is hidden.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, pickSiteDetail } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// Scrolls far enough to trigger lazy loading, but never past maxY: on an
// unbounded page the scroll target is the tile cap, not the reported height.
async function lazyScroll(p, maxY = Infinity) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, maxY); y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the page as it arrives, consent layer included if it shows.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const chunk = Math.floor(14000 / this.dpr);
    // Infinite-scroll pages grow scrollHeight without bound while lazyScroll
    // walks them; the tile ceiling is applied to the scroll itself, so a page
    // reporting millions of pixels cannot tie up the run before the cap.
    const MAXH = 8 * chunk;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    await lazyScroll(p, Math.min(H0, MAXH));
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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

// Click the first winners-grid filter item: its js-nav-filters-item toggle
// opens the sublist dropdown; the shot is skipped when nothing opens.
const openFilter = async (p) => {
  const m = p.locator('.nav-filters__item.js-nav-filters-item, .nav-filters__item').filter({ visible: true }).first();
  if (await m.count()) { await m.click({ timeout: 5000 }).catch(() => m.evaluate((el) => el.click())); await wait(p, 1600); return true; }
  return false;
};

const viewAndFull = async (p, S) => { await S.view('default'); await S.full(); };

// Section indexes from site-tree.md. Each is a public page reached from the
// homepage header, Explore dropdown, or footer. No form is submitted.
const sections = {
  nominees: '/websites/nominees/',
  sotd: '/websites/sites_of_the_day/',
  sotm: '/websites/sites_of_the_month/',
  soty: '/websites/sites_of_the_year/',
  honors: '/honors/winners',
  winners: '/winner-list/',
  jury: '/jury/2026/',
  awards: '/annual-awards/',
  library: '/library/',
  directory: '/directory/',
  academy: '/academy/',
  jobs: '/jobs/',
  market: '/market/',
  pro: '/pro',
  elements: '/elements/',
  conferences: '/conferences/',
  blog: '/blog/',
  faqs: '/faqs/',
  about: '/about-us/',
  contact: '/contact-us/',
  cookies: '/cookies-policy/',
  terms: '/terms/',
  privacy: '/privacy-policy/',
  plans: '/plans/user-plans',
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.raw('arrival');                       // the page as it arrives, any consent layer included
    await S.view('default');
    await step('explore-open', async () => {
      const item = p.locator('li.nav-header-main__item.has-dropdown').first();
      if (await item.count()) { await item.hover(); await wait(p, 600); await item.locator('span.nav-header-main__link').click({ timeout: 4000 }).catch(() => {}); await wait(p, 900); await S.view('explore-open'); await p.keyboard.press('Escape').catch(() => {}); }
    });
    await step('card-hover', async () => {
      const card = p.locator('a.figure-rollover__link').filter({ visible: true }).first();
      if (await card.count()) { await card.hover(); await wait(p, 1200); await S.view('card-hover'); await p.mouse.move(20, 400); await wait(p, 500); }
    });
    await S.full();
  } },
  websites: { path: '/websites/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('filter-open', async () => { if (await openFilter(p)) await S.view('filter-open'); });
    await S.full();
  } },
  site: { path: '/websites/', wait: 9000, run: async (p, S) => {
    // The site-detail URL is discovered with the same rule measure.mjs uses
    // (pickSiteDetail in lib.mjs): first card whose page still shows a Vote
    // control, so screenshots and measurements describe the same entry.
    // Voting is never clicked.
    const href = await pickSiteDetail(p);
    if (!href) { log('  no site link found'); return; }
    await clearChallenge(p); await wait(p, 2000);
    await S.view('default');
    await S.full();
  } },
  collections: { path: '/collections/', wait: 9000, run: async (p, S) => viewAndFull(p, S) },
  submit: { path: '/submit/', wait: 9000, run: async (p, S) => {
    // The submission intro/pricing page: captured, never submitted.
    await viewAndFull(p, S);
  } },
};
for (const [name, path] of Object.entries(sections)) {
  desktop[name] = { path, wait: 6000, run: viewAndFull };
}

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    // The full-page shot comes first: once the menu is open it covers the
    // home view, and full() hides consent/promo layers only.
    await S.full();
    await step('menu', async () => {
      const m = p.locator('header .header-main__hamburger, header [class*="hamburger" i], header [class*="burger" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); }
    });
  } },
  websites: { path: '/websites/', wait: 9000, run: async (p, S) => viewAndFull(p, S) },
  collections: { path: '/collections/', wait: 6000, run: viewAndFull },
  directory: { path: '/directory/', wait: 6000, run: viewAndFull },
  academy: { path: '/academy/', wait: 6000, run: viewAndFull },
  jobs: { path: '/jobs/', wait: 6000, run: viewAndFull },
  market: { path: '/market/', wait: 6000, run: viewAndFull },
  blog: { path: '/blog/', wait: 6000, run: viewAndFull },
  submit: { path: '/submit/', wait: 6000, run: viewAndFull },
};

const b = await chromium.launch({ channel: 'chrome', headless: true });
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
    await p.goto(spec.url || BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
