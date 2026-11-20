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
// that open a mega-menu; a click toggles them. Local UI only, never a link.
async function openMenu(p, S) {
  const t = p.locator('summary.nav-trigger').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  await clickEl(t);
  await wait(p, 1400);
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMenu(p, S); });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { path: '/customers', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  library: { path: '/library', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  templates: { path: '/templates', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { path: '/product/content-management', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  solutions: { path: '/solutions/client-portal', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about-us', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  demo: { path: '/demo', wait: 14000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // The auth application on auth.dock.us: the sign-in and sign-up cards are
  // surfaces only — measured, never filled or submitted.
  login: { url: AUTH + '/login', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: AUTH + '/sign-up', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile menu control is the header's <summary.navigation-toggle>
      // (see measure.mjs's m-menu-button) — a missing toggle is a failed
      // shot, so it is thrown, not silently skipped.
      const m = p.locator('summary.navigation-toggle, .nav-mobile-toggle, button[aria-label*="menu" i], button[aria-label*="navigation" i]').filter({ visible: true }).first();
      if (!(await m.count())) throw new Error('no mobile menu toggle found (expected summary.navigation-toggle)');
      await clickEl(m); await wait(p, 1800); await S.view('menu'); await p.keyboard.press('Escape');
    });
    await S.full();
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
