// Captures ableton.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought, downloaded or signed into: the only press is the main nav's "More"
// disclosure button, a local menu toggle. The cookie-consent bar (#biscuits-overlay) is hidden,
// never answered; /en/login/ is captured at rest as the auth boundary (no credentials, no submit);
// shop's Add-to-cart buttons and trial's download links are never followed.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
    // drop this shot's earlier tiles (and sidecars) first: a shorter or capped page would
    // otherwise leave old partN files that quantize.py stitches into the new shot
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // An infinite or growing page reports a scrollHeight without end: tile at most 8 chunks
    // and log the boundary (the kit's cap), never one tile per chunk for ever.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/en/', run: async (p, S) => {
    // The consent bar is hidden by the pre-tour sweep; un-hide it for one
    // documented shot of the component as rendered, then hide it again.
    await p.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) el.style.display = ''; });
    await wait(p, 400);
    await S.raw('cookie-banner');
    await p.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) el.style.display = 'none'; });
    await S.view('default');
    await step('more-menu', async () => {
      const more = p.locator('.js-main-nav-more-button').first();
      if (await more.count()) { await more.click(); await wait(p, 900); await S.view('more-menu'); await more.click(); await wait(p, 400); }
    });
    await S.full();
  } },
  live: { path: '/en/live/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  push: { path: '/en/push/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  move: { path: '/en/move/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  note: { path: '/en/note/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  link: { path: '/en/link/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  packs: { path: '/en/packs/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  shop: { path: '/en/shop/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  trial: { path: '/en/trial/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/en/blog/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/en/about/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { path: '/en/help/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  jobs: { path: '/en/jobs/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/en/login/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/en/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  live: { path: '/en/live/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  shop: { path: '/en/shop/', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      let clean = true;
      for (let i = 0; i < 6; i++) {
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
log('done', total, 'screenshots ->', RAW);
await b.close();
