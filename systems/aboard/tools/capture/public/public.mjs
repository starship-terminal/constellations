// Captures aboard.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, submitted or signed into: the contact and newsletter forms are never touched.
// The CookieYes consent strip (.cky-consent-container) and its preferences modal (.cky-modal) are
// hidden, never answered.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots go to a scratch dir outside the repo (the kit's default), never into
// systems/<slug>/raw/: quantize.py reads them from there and writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(fileURLToPath(new URL('../../..', import.meta.url))), 'raw-shots');
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
  home: { path: '/', run: async (p, S) => {
    // The CookieYes strip is hidden by the pre-tour sweep; un-hide it for one
    // documented shot of the component as rendered, then hide it again.
    await p.evaluate(() => { const el = document.querySelector('.cky-consent-container'); if (el) el.style.display = ''; });
    await wait(p, 400);
    await S.raw('cookie-banner');
    await p.evaluate(() => { const el = document.querySelector('.cky-consent-container'); if (el) el.style.display = 'none'; });
    await S.view('default');
    await step('contact', async () => {
      await p.evaluate(() => document.querySelector('#contact')?.scrollIntoView({ block: 'start' }));
      await wait(p, 900);
      await S.view('contact');
      await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
    });
    await S.full();
  } },
  'how-we-work': { path: '/how-we-work/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'case-studies': { path: '/case-studies/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'case-study': { path: '/case-studies/city-of-boston-scheduling-app/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  foundry: { path: '/foundry/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  perspectives: { path: '/perspectives/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  newsletter: { path: '/newsletter/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  podcast: { path: '/podcast/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'podcast-episode': { path: '/podcast/jason-goldman-from-vc-pitches-to-ai-kill-switches/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  events: { path: '/events/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  media: { path: '/media/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  faq: { path: '/faq/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'aboard-sign': { path: '/meet-aboard-sign/', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => {
      const btn = p.locator('button[aria-label*="menu" i], .menu-toggle, [class*="hamburger" i], header button').first();
      if (await btn.count()) { await btn.click(); await wait(p, 900); await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  'how-we-work': { path: '/how-we-work/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'case-studies': { path: '/case-studies/', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
