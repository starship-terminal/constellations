// Captures apollographql.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix. The site ships one
// theme (dark, with light content sections). Desktop shots are 1440x900 at 1x, mobile 390x844
// at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are the Products nav disclosure
// (a local menu open) and the pricing billing toggle if present. The OneTrust banner is
// captured on home-light-cookie-banner then hidden by CSS — never consented. The app host
// (studio.apollographql.com) is probed as an opportunistic boundary, recorded as blocked
// when it stays unreachable.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
    // Clear this capture's stale tiles first: a page that shrank since the
    // last run would otherwise leave old partN files for quantize.py to
    // stitch over the fresh capture.
    for (const old of fs.readdirSync(RAW)) if (old.startsWith(`${this.prefix}-${name}.part`)) fs.rmSync(`${RAW}/${old}`, { force: true });
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

// Opens the Products disclosure in the nav (a local menu open, no navigation).
const openProducts = async (p) => {
  const btn = p.getByRole('button', { name: 'Products', exact: true }).first();
  if (!(await btn.count())) return false;
  await btn.click();
  await wait(p, 1200);
  return true;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.raw('cookie-banner');        // OneTrust card as found; never answered
    await S.view('default');
    await step('nav-products-open', async () => { if (await openProducts(p)) await S.view('nav-products-open'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await S.full();
  } },
  graphos: { path: '/graphos', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'agent-services': { path: '/graphos-agent-services', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('toggle', async () => {
      const t = p.getByRole('button', { name: /annual|yearly|monthly/i }).filter({ visible: true }).first();
      if (await t.count()) { await t.click(); await wait(p, 1000); await S.view('billing-toggle'); }
    });
    await S.full();
  } },
  customers: { path: '/customers', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'why-apollo': { path: '/why-apollo', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'contact-sales': { path: '/contact-sales', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('form-fields', async () => {
      const f = p.locator('input:not([type="hidden"]):not([type="checkbox"]):not([type="radio"]), textarea').filter({ visible: true }).first();
      if (await f.count()) { await f.scrollIntoViewIfNeeded(); await wait(p, 600); await S.view('form-fields'); }
    });
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.raw('cookie-banner');
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'contact-sales': { path: '/contact-sales', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

// The app itself lives on studio.apollographql.com, reached only through
// sign-in/sign-up — probed once, recorded as blocked when unreachable.
const opportunistic = {
  login: { url: 'https://studio.apollographql.com/login?referrer=www-new' },
  signup: { url: 'https://studio.apollographql.com/signup?referrer=www-new' },
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
  const S = new Shooter(p, `${name}-${spec.theme || 'dark'}`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      let clean = true;
      for (let i = 0; i < 8; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED challenge-or-error', spec.path); await ctx.close(); continue; }
    // No promo sweep here: S.raw() must find the consent card as mounted for
    // the cookie-banner shot. S.view()/S.full() call closePromo before every
    // later shot, so nothing else needs killGeo up front.
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
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
