// Captures Gauth's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Gauth ships one theme, so there
// is no dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, created or signed into: the only presses are dialog dismissals, tabs, Show more, the
// lesson's own Not now, Continue (the audio gate), Pause, Settings and chapters, and a story card's
// Explore, which opens a published story.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, openStory, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
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
const notNow = async (p) => { const b = p.getByRole('button', { name: 'Not now' }); if (await b.count()) { await b.click(); await wait(p, 1200); } };
const gate = async (p) => { const b = p.getByRole('button', { name: 'Continue', exact: true }); if (await b.count()) { await b.click(); await wait(p, 4000); } };
const pause = async (p) => { const b = p.getByRole('button', { name: /^Pause/ }); if (await b.count()) { await b.first().click().catch(() => {}); await wait(p, 600); } };

// PRODUCT (adapt): FoodNoms public Framer site. No promo dialog. App Store
// document navigations are aborted so a download link is recorded, not followed
// into a store checkout. Newsletter and search fields are never submitted.
async function blockStore(p) {
  await p.route('**/*', (route) => {
    const u = route.request().url();
    if (/apps\.apple\.com|itunes\.apple\.com|play\.google\.com/.test(u) && route.request().resourceType() === 'document') {
      log('  abort store document', u.slice(0, 120));
      return route.abort();
    }
    return route.continue();
  });
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  news: { path: '/news', run: async (p, S) => {
    await S.view('default');
    await step('newsletter', async () => {
      const email = p.locator('input[type="email"]').first();
      await email.scrollIntoViewIfNeeded();
      await email.focus();
      await wait(p, 300);
      await S.view('newsletter-focus');
    });
    await step('view-more', async () => {
      await p.getByRole('button', { name: 'View More' }).click();
      await wait(p, 800);
      await S.view('view-more');
    });
  } },
  help: { path: '/help', run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      await p.getByText('About Foodnoms', { exact: true }).click();
      await wait(p, 500);
      await S.view('accordion');
    });
    await step('search', async () => {
      await p.getByRole('button', { name: /search/i }).first().click();
      await wait(p, 600);
      await S.view('search');
      await p.locator('input[placeholder="Search..."]').fill('widgets');
      await wait(p, 700);
      await S.view('search-results');
    });
  } },
  plus: { path: '/plus', run: async (p, S) => { await S.view('default'); await S.full(); } },
  press: { path: '/press', run: async (p, S) => {
    await S.view('default');
    await step('copied', async () => {
      await p.getByRole('button', { name: /website/i }).first().click();
      await wait(p, 400);
      await S.view('copied');
    });
  } },
  family: { path: '/family-plan', run: async (p, S) => { await S.view('default'); } },
  compare: { path: '/vs/myfitnesspal', run: async (p, S) => { await S.view('default'); } },
  article: { path: '/news/foodnoms-cloud', run: async (p, S) => { await S.view('default'); } },
  'help-article': { path: '/help/about-foodnoms', run: async (p, S) => { await S.view('default'); } },
  'open-signup': { path: '/open/settings/sign-up', run: async (p, S) => { await S.view('default'); } },
  'login-404': { path: '/login', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.getByRole('button', { name: /open navigation menu/i }).click();
      await wait(p, 500);
      await S.view('menu');
    });
  } },
  help: { path: '/help', run: async (p, S) => { await S.view('default'); } },
  news: { path: '/news', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const themes = (process.env.THEMES || 'light,dark').split(',').filter(Boolean);
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const theme of themes) {
  for (const { k, mob } of runs) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(`${name}-${theme}`)) continue;
    const spec = (mob ? mobile : desktop)[k];
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: theme });
    const p = await ctx.newPage();
    await blockStore(p);
    log(name, theme);
    const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
    try {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
      await wait(p, spec.wait || 1800);
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', name, theme, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await b.close();
