// Captures dock.us's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The public surface
// paints light only (there is no dark theme; dark-painted sections use per-component .dark
// classes). Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the Product nav dropdown
// (a <details>/<summary> toggle) and the mobile navigation menu. The auth cards on auth.dock.us
// are surfaces, never filled or submitted. Any consent/chat overlay is hidden, never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, AUTH } from './lib.mjs';

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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The header's Product/Resources triggers are <details>/<summary> dropdowns
// inside dock-site-header's shadow root. A click toggles them. Local UI
// only, never a link, never a form, never an identity provider.
async function openMenu(p, S, label, shot) {
  const opened = await p.evaluate((label) => {
    const host = document.querySelector('dock-site-header');
    const root = host && host.shadowRoot;
    if (!root) return false;
    const t = [...root.querySelectorAll('summary.nav-trigger')].find((el) => (el.textContent || '').replace(/\s+/g, ' ').trim() === label);
    if (!t) return false;
    t.click();
    return true;
  }, label);
  if (!opened) throw new Error('no ' + label + ' trigger in dock-site-header');
  await wait(p, 1400);
  await S.view(shot);
  await p.keyboard.press('Escape');
  await wait(p, 400);
}

const page = (path, wait = 10000) => ({ path, wait, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('product menu', async () => { await openMenu(p, S, 'Product', 'product'); });
    await step('resources menu', async () => { await openMenu(p, S, 'Resources', 'resources'); });
    await S.full();
  } },
  pricing: page('/pricing'),
  customers: page('/customers'),
  library: page('/library'),
  templates: page('/templates'),
  // Earlier pass named this route "product". Kept so the old shot name still regenerates.
  product: page('/product/content-management'),
  solutions: page('/solutions/client-portal'),
  about: page('/about-us', 8000),
  demo: page('/demo', 14000),
  // The auth application on auth.dock.us: the sign-in and sign-up cards are
  // surfaces only. Photographed empty. Never filled or submitted. Identity
  // providers are not clicked.
  login: { url: AUTH + '/login', wait: 10000, run: async (p, S) => { await S.view('empty'); } },
  signup: { url: AUTH + '/sign-up', wait: 10000, run: async (p, S) => { await S.view('empty'); } },
  // Public pages the 2026-11-21 site tree names and the earlier pass did not photograph.
  'dock-ai': page('/product/dock-ai'),
  sales: page('/solutions/sales'),
  learning: page('/product/learning-management'),
  integrations: page('/product/integrations'),
  updates: page('/product-updates'),
  events: page('/events'),
  privacy: { path: '/legal/privacy', wait: 8000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile menu control is the header's <summary.navigation-toggle>
      // (see measure.mjs's m-menu-button) — a missing toggle is a failed
      // shot, so it is thrown, not silently skipped.
      const opened = await p.evaluate(() => {
        const host = document.querySelector('dock-site-header');
        const root = host && host.shadowRoot;
        const t = root && [...root.querySelectorAll('button.navigation-toggle, summary.navigation-toggle')].find((el) => /menu/i.test(el.getAttribute('aria-label') || el.textContent || ''));
        if (!t) return false;
        t.click();
        return true;
      });
      if (!opened) throw new Error('no mobile menu toggle found in dock-site-header');
      await wait(p, 1800);
      await S.view('menu');
      await p.keyboard.press('Escape');
    });
    // Full-page at 2x exceeds the screenshot helper's 1px tolerance on this
    // page (PNG height drifted 18px on 2026-11-21). Viewport shots are the
    // phone evidence. The desktop full-page shot covers the long page.
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
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
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path || spec.url) {
      await p.goto(spec.url || BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
