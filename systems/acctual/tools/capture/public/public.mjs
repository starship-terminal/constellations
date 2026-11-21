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

// Page list is the reachable public graph in systems/acctual/site-tree.md
// (mapped 2026-11-21 from the homepage). Auth walls are not in this list.
// Blog posts share one article template: the index, the announcement post,
// and the footer-linked posts are captured. Remaining posts are the same
// template and stay in the site tree.
const page = (path) => ({ path, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('invoice-demo', async () => {
      await p.evaluate(() => document.querySelector('[data-framer-name="hero"], [data-framer-name*="InputContainer" i], [data-framer-name*="Dropdown" i]')?.scrollIntoView({ block: 'center' }));
      await wait(p, 1200);
      await S.view('invoice-demo');
      await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
    });
    await step('faq-open', async () => {
      const item = p.locator('[data-framer-name="Closed"]').first();
      if (await item.count()) {
        await item.scrollIntoViewIfNeeded();
        await item.click({ timeout: 4000 });
        await wait(p, 700);
        await S.view('faq-open');
        await p.evaluate(() => scrollTo(0, 0));
        await wait(p, 300);
      }
    });
    await S.full();
  } },
  pricing: page('/pricing'),
  teams: page('/teams'),
  about: page('/about'),
  blog: page('/blog'),
  'blog-post': page('/blog/acctual-joins-altitude'),
  altitude: page('/altitude'),
  'freelancer-invoicing': page('/freelancer-invoicing'),
  'agency-invoicing': page('/agency-invoicing'),
  'stablecoin-invoicing': page('/stablecoin-invoicing'),
  'usdc-invoicing': page('/usdc-invoicing'),
  'usdt-invoicing': page('/usdt-invoicing'),
  exporters: page('/exporters'),
  'invoice-templates': page('/invoice-templates'),
  'freshbooks-alternative': page('/freshbooks-alternative'),
  location: page('/locations/us-to-japan'),
  'location-us-uk': page('/locations/us-to-uk'),
  terms: page('/terms'),
  privacy: page('/privacy'),
  'old-home': page('/old-home'),
  'blog-old': page('/blog-old'),
  'not-found': page('/404'),
  'blog-recurring': page('/blog/how-to-set-up-recurring-invoices'),
  'blog-graphic': page('/blog/graphic-design-invoice'),
  'blog-web': page('/blog/web-design-development-invoice'),
  'blog-video': page('/blog/video-film-production-invoices'),
  'blog-paypal': page('/blog/paypal-invoice-fees-are-they-worth-it'),
  'blog-upwork': page('/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026'),
  'blog-pastdue': page('/blog/past-due-vs-overdue-invoices'),
  'free-invoice-software': page('/free-invoice-software'),
  'guide': { path: 'https://guides.acctual.com/guide/getting-started', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'guide-overview': { path: 'https://guides.acctual.com/guide/overview', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'guide-invoice': { path: 'https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'guide-pay': { path: 'https://guides.acctual.com/guide/pay-a-bill/pay-a-bill-from-wallet', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'guide-rates': { path: 'https://guides.acctual.com/guide/resources/rates-fees', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => {
      // Phone - Open is a local disclosure. The trigger is the 18px icon
      // named Group 1171277804 on the right of Navigation/Topbar.
      const named = p.locator('[data-framer-name="Group 1171277804"]').first();
      if (await named.count()) {
        await named.click({ timeout: 4000 });
      } else {
        await p.evaluate(() => {
          const bar = document.querySelector('[data-framer-name="Navigation/Topbar"]');
          if (!bar) return;
          const small = [...bar.querySelectorAll('div,button,a')].filter((e) => {
            const r = e.getBoundingClientRect();
            return r.width >= 10 && r.width <= 90 && r.height <= 80 && r.x > window.innerWidth - 140 && e.querySelector('svg');
          });
          const el = small.find((e) => !small.some((o) => o !== e && o.contains(e))) || small[0];
          if (el) el.click();
        });
      }
      await wait(p, 900);
      await S.view('menu-open');
      await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 400);
    });
    await S.full();
  } },
  pricing: page('/pricing'),
  blog: page('/blog'),
  'freelancer-invoicing': page('/freelancer-invoicing'),
  'agency-invoicing': page('/agency-invoicing'),
  altitude: page('/altitude'),
  'invoice-templates': page('/invoice-templates'),
  'blog-post': page('/blog/acctual-joins-altitude'),
  location: page('/locations/us-to-uk'),
  terms: page('/terms'),
  privacy: page('/privacy'),
  guide: { path: 'https://guides.acctual.com/guide/getting-started', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'guide-invoice': { path: 'https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      const url = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
