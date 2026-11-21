// Captures aaply.app's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only press is the pricing billing toggle, a local
// Monthly/Yearly state swap. aaply.app is a Tilda site with no challenge; the app host
// (go.aaply.app) returns "Not found" to this client for every auth/demo route — probed as an
// opportunistic boundary, recorded as blocked when it stays unreachable.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < H; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// -- shared bits -------------------------------------------------------------
const clickEl = async (loc, ms = 10000) => {
  await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click()));
};
// The pricing toggle is a Monthly/Yearly pair of 152x60 pills — a local state
// swap, no submission. Clicks the unheld segment so the tour can shoot both.
const clickToggle = async (p, label) => {
  const t = p.locator(`.tn-atom:has-text("${label}")`).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await clickEl(t); await wait(p, 900); return true;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { path: '/features', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  value: { path: '/value', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('toggle', async () => { if (await clickToggle(p, 'Yearly')) await S.view('yearly'); });
    await S.full();
  } },
  'our-story': { path: '/our-story', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  team: { path: '/team', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'figma-plugin': { path: '/figma_plugin', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // Sitemap-only public pages. No nav, footer, or phone-menu control points
  // here (see site-tree.md). /workflow is the same walkthrough as /features.
  'early-program': { path: '/early-program', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  manual: { path: '/manual', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

// Reviews carousel dots (aria-label "N of 6") select a slide in place.
// Shot on its own so a refresh does not rewrite the existing default/full pair.
const reviewsSlide = {
  'reviews-slide': { path: '/reviews', run: async (p, S) => {
    const dot = p.locator('button[aria-label="2 of 6"]').first();
    if (!(await dot.count())) return;
    await dot.click({ timeout: 5000 }).catch(() => dot.evaluate((el) => el.click()));
    await wait(p, 900);
    await S.view('slide-2');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    // Burger opens an in-page overlay (href="#open-nav"). Close it after the shot.
    await step('menu', async () => {
      const burger = p.locator('a[href="#open-nav"]').first();
      if (!(await burger.count())) return;
      await burger.evaluate((el) => el.click());
      await wait(p, 900);
      await S.view('menu-open');
      const close = p.locator('a[href="#close-nav"]').first();
      if (await close.count()) await close.evaluate((el) => el.click());
      await wait(p, 400);
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  value: { path: '/value', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { path: '/reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'our-story': { path: '/our-story', run: async (p, S) => { await S.view('default'); await S.full(); } },
  team: { path: '/team', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'figma-plugin': { path: '/figma_plugin', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'early-program': { path: '/early-program', run: async (p, S) => { await S.view('default'); await S.full(); } },
  manual: { path: '/manual', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

// Auth and demo live on the app host go.aaply.app, which returns a bare
// "Not found" to this client — attempted once, recorded as blocked.
const opportunistic = {
  login: { url: 'https://go.aaply.app/sign' },
  signup: { url: 'https://go.aaply.app/signup' },
  demo: { url: 'https://go.aaply.app/workspace/demo' },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, table: desktop })),
  ...Object.keys(reviewsSlide).map((k) => ({ k, mob: false, table: reviewsSlide })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, table: mobile })),
];
for (const { k, mob, table } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = table[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      // Tilda animates blocks in on scroll — wait the settle window before
      // deciding the page is clean.
      let clean = true;
      for (let i = 0; i < 8; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED challenge-or-error', spec.path); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  for (const [name, spec] of Object.entries(opportunistic)) {
    if (pageArg.length && !pageArg.includes(name)) continue;
    const S = new Shooter(p, `${name}-light`, 1440, 900, 1);
    let ok = false;
    for (let attempt = 0; attempt < 2 && !ok; attempt++) {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
      if (!(await clearChallenge(p, { tries: 6 }))) break;
      let clean = true;
      for (let i = 0; i < 6; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('BLOCKED unreachable', name); continue; }
    log(name, 'cleared');
    try { await killGeo(p); await S.view('default'); await S.full(); } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
  }
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
