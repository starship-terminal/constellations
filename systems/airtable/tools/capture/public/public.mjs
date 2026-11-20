// Captures Airtable's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   [RAW=<dir, default ~/.design-systems/airtable/raw-shots>] PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// One public surface, one host:
//   www.airtable.com     the marketing site: /, /platform, /platform/ai, /solutions,
//                        /solutions/enterprise, /pricing, /contact-sales, /customer-stories,
//                        /templates, /marketplace, /whatsnew, /about
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Desktop shots are 1440x900
// at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved
// as name.partN.png tiles, which quantize.py stitches back together.
//
// Nothing is sent, created or signed into: the nav dropdowns are opened by hover only; the pricing
// billing toggle is local UI; the /contact-sales form is photographed, never submitted; the promo
// bar's close button is a local dismissal and is the only control pressed besides the mobile menu.
// Book Demo, Sign up for free and Log in leave for the sign-up/sign-in surface and are never
// followed. airtable.com/<workspace> (the app) is the signed-in product and is never touched.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name) { await closePromo(this.p); await wait(this.p, 300); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await closePromo(p); // Riley can mount while the lazy-scroll runs
    await wait(p, 300);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // drop this shot's earlier tiles (and sidecars) first: a shorter or capped page would
    // otherwise leave old partN files that quantize.py stitches into the new shot
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Retire any tiles from an earlier run before writing this capture's, so a
    // shorter page cannot be stitched back together with stale trailing tiles.
    for (const stale of fs.readdirSync(RAW).filter((x) => x.startsWith(`${this.prefix}-${name}.part`))) fs.rmSync(path.join(RAW, stale), { force: true });
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
const failed = new Set(); // pages and states whose capture did not complete
const step = async (label, fn) => { try { await fn(); } catch (e) { failed.add(label); log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Clicks one top-nav trigger so its drawer opens (airtable.com's drawers open on click;
// the trigger is a <button>, a local disclosure — never a link or a submission).
async function navMenu(p, S, item = 'Platform') {
  const link = p.locator('header button, nav button').filter({ hasText: new RegExp('^' + item + '$', 'i') }).filter({ visible: true }).first();
  await link.click().catch(() => {});
  await wait(p, 1800);
  await S.view('nav-dropdown');
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 600);
}

const desktop = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-dropdown', () => navMenu(p, S));
    // The promo bar's close is a local dismissal, not a consent choice.
    await step('promo-closed', async () => {
      const bar = p.locator('[class*="whatsNewNav" i], [class*="promoBar" i], [class*="promo-bar" i]').first();
      const x = bar.locator('button').filter({ hasText: /close|dismiss|×|✕/i }).first();
      const alt = p.locator('header button[aria-label*="close" i], header button[aria-label*="dismiss" i]').first();
      if (await x.count()) await x.click(); else if (await alt.count()) await alt.click();
      await wait(p, 800);
      await S.view('promo-closed');
    });
  } },
  platform: { path: BASE + '/platform', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'platform-ai': { path: BASE + '/platform/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  solutions: { path: BASE + '/solutions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: BASE + '/solutions/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: BASE + '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    // The billing period toggle is local UI.
    await step('billing-toggle', async () => {
      const t = p.locator('[role=switch], [role=tab], button').filter({ hasText: /annual|monthly|yearly|billed/i }).filter({ visible: true }).first();
      if (await t.count()) { await t.click(); await wait(p, 1500); await S.view('billing-toggle'); }
    });
  } },
  'contact-sales': { path: BASE + '/contact-sales', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-stories': { path: BASE + '/customer-stories', run: async (p, S) => { await S.view('default'); await S.full(); } },
  templates: { path: BASE + '/templates', run: async (p, S) => { await S.view('default'); await S.full(); } },
  marketplace: { path: BASE + '/marketplace', run: async (p, S) => { await S.view('default'); await S.full(); } },
  whatsnew: { path: BASE + '/whatsnew', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-open', async () => {
      const t = p.locator('button[aria-label*="side menu" i], button[aria-label*="menu" i], [class*="navToggle" i], [class*="burger" i], [class*="hamburger" i]').filter({ visible: true }).first();
      if (await t.count()) { await t.click(); await wait(p, 1500); await S.view('nav-open'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
  } },
  pricing: { path: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  platform: { path: BASE + '/platform', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  // The Google One Tap sign-in prompt is a sign-in surface: aborted at the
  // network, never rendered or answered (same as launch() in lib.mjs).
  await ctx.route(/accounts\.google\.com|apis\.google\.com\/js/, (r) => r.abort()).catch(() => {});
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { failed.add(name); log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
// A caller chaining this into quantize.py must not publish old files after a
// failed recapture, so a failure leaves a nonzero exit status.
if (failed.size) { log('failed:', [...failed].join(', ')); process.exit(1); }
