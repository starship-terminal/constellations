// Captures forhers.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. www.forhers.com
// answers every request from this network with a Cloudflare managed challenge
// (cf-mitigated: challenge, HTTP 403, headless and headed alike, every route
// including robots.txt), so the DOM evidence is Wayback Machine SSR snapshots
// of the public pages (PAGES in lib.mjs), served locally with their archived
// fonts and images and every script stripped. The site paints one light theme
// (`data-theme="light"`/`"hers"` are per-component variants, not a page
// switch). Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full`
// shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought or signed into: no button is clicked on this route — every control
// is a link or a hydration-owned toggle that is never followed. Consent,
// regional-redirect and promo overlays the SSR markup mounts are hidden,
// never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { servePages, closePromo, chromium, UA, UA_MOBILE, PAGES, SCRATCH } from './lib.mjs';

const RAW = process.env.RAW || `${SCRATCH}/raw-shots`;
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
    await closePromo(p);
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

// forhers paints one light theme on the whole signed-out surface.
const THEME = 'light';
const V = async (p, S) => { await S.view('default'); await S.full(); };
const desktop = {};
const mobile = {};
for (const k of Object.keys(PAGES)) desktop[k] = { key: k, run: V };
for (const k of ['home', 'weight-loss', 'product', 'bmi-calculator', 'blog-post']) mobile[k] = { key: k, run: V };

const { srv, port } = await servePages(`${SCRATCH}/pages`, `${SCRATCH}/assets`);
const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
try {
  for (const { k, mob } of runs) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name)) continue;
    const spec = (mob ? mobile : desktop)[k];
    const pg = PAGES[spec.key];
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    const p = await ctx.newPage();
    p.setDefaultTimeout(120000);
    log(name);
    const S = new Shooter(p, `${name}-${THEME}`, vw, vh, dpr, pg.url);
    try {
      await p.goto(`http://127.0.0.1:${port}/pages/${spec.key}.html`, { waitUntil: 'load', timeout: 120000 }).catch(() => {});
      await p.waitForFunction(() => document.fonts && document.fonts.status === 'loaded', undefined, { timeout: 20000 }).catch(() => {});
      // Let the mirror fetches land and the lazy images in view complete.
      for (let i = 0; i < 12; i++) {
        await wait(p, 2500);
        const s = await p.evaluate(() => ({ done: [...document.images].filter((im) => im.complete && im.naturalWidth).length, total: document.images.length }));
        if (i > 3 && s.done >= s.total - 2) break;
      }
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
} finally {
  await b.close();
  srv.close();
}
log('done', total, 'screenshots ->', RAW);
