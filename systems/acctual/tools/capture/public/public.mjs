// Captures acctual.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, submitted or signed into: the app.acctual.com Log-in and
// Sign-up links are never opened, and the invoice demo is measured at rest.
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
    const maxChunks = 8; // an unbounded tiler hangs on a runaway page; truncate at the boundary
    const f = `${RAW}/${this.prefix}-${name}`;
    // Clear this capture's stale tiles first: a page that shrank since the
    // last run would otherwise leave old partN files for quantize.py to
    // stitch over the fresh capture.
    for (const old of fs.readdirSync(RAW)) if (old.startsWith(`${this.prefix}-${name}.part`)) fs.rmSync(`${RAW}/${old}`, { force: true });
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      const capped = Math.min(H, chunk * maxChunks);
      for (let i = 0, y = 0; y < capped; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, capped - y) } }, this.requested);
      if (H > capped) log('  TRUNCATED', name, 'at', capped, 'of H=' + H, '(' + maxChunks, 'chunks max)');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('invoice-demo', async () => {
      await p.evaluate(() => document.querySelector('[data-framer-name="hero"], [data-framer-name*="InputContainer" i], [data-framer-name*="Dropdown" i]')?.scrollIntoView({ block: 'center' }));
      await wait(p, 1200);
      await S.view('invoice-demo');
      await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  teams: { path: '/teams', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/acctual-joins-altitude', run: async (p, S) => { await S.view('default'); await S.full(); } },
  altitude: { path: '/altitude', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'freelancer-invoicing': { path: '/freelancer-invoicing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'stablecoin-invoicing': { path: '/stablecoin-invoicing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  location: { path: '/locations/us-to-japan', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => {
      // The framer nav trigger is an unnamed icon box on the right of the top
      // bar (a local disclosure): tag it by geometry, then tap it.
      await p.evaluate(() => {
        const bar = document.querySelector('[data-framer-name="Navigation/Topbar"]');
        if (!bar) return;
        const small = [...bar.querySelectorAll('div,button,a')].filter((e) => {
          const r = e.getBoundingClientRect();
          return r.width >= 10 && r.width <= 90 && r.height <= 80 && r.x > window.innerWidth - 140 && e.querySelector('svg');
        });
        const el = small.find((e) => !small.some((o) => o !== e && o.contains(e))) || small[0];
        if (el) el.setAttribute('data-m-mark', 'mtr');
      }).catch(() => {});
      const btn = p.locator('[data-m-mark="mtr"], [data-framer-name="navtrigger"], [data-framer-name*="nav" i] button, [aria-label*="menu" i]').filter({ visible: true }).first();
      if (await btn.count()) { await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click())); await wait(p, 900); await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
