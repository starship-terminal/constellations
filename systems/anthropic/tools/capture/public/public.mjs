// Captures Anthropic's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   [RAW=<dir, default ~/.design-systems/anthropic/raw-shots>] PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// This refresh stays on www.anthropic.com. claude.com, docs.claude.com, claude.ai and
// platform.claude.com are not photographed. The site tree is systems/anthropic/site-tree.md.
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Desktop shots are 1440x900
// at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved
// as name.partN.png tiles, which quantize.py stitches back together.
//
// Nothing is sent, created or signed into. Header menus open on click. Try Claude, Claude.ai,
// Console, Contact Sales, Download app, and the footer's Privacy choices dialog are never
// followed or opened. No email, password, or identity provider is touched.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, DOCS } from './lib.mjs';

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

// Infinite-scroll pages grow scrollHeight without bound; the tile cap below
// must bound the lazy-scroll pass too, not just the tile loop.
const TILE_CAP = 8;
const chunkFor = (dpr) => Math.floor(14000 / dpr);
async function lazyScroll(p, maxY = Infinity) {
  const h = Math.min(await p.evaluate(() => document.documentElement.scrollHeight), maxY);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

let failures = 0;

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    const chunk = chunkFor(this.dpr);
    const MAXH = TILE_CAP * chunk;
    // Check the height before scrolling: a runaway page fails the guard here,
    // not after a lazy-scroll pass that could take the better part of an hour.
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (H0 > MAXH) log(`  ! ${name}: page is ${H0}px tall before scrolling, capturing first ${MAXH}px only (infinite/growing page boundary)`);
    await lazyScroll(p, Math.min(H0, MAXH));
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const hCap = Math.min(H, MAXH);
    if (H > MAXH && H0 <= MAXH) log(`  ! ${name}: page grew to ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Clear last run's tiles for this shot family first: a page that is short
    // now must not pick up stale .partN files from a taller earlier capture.
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { failures++; log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Clicks one header menu button. anthropic.com opens these on click (aria-haspopup=menu).
async function navMenu(p, S, item, shot = 'nav-dropdown') {
  const link = p.locator('header button, nav button').filter({ hasText: new RegExp('^' + item + '$') }).filter({ visible: true }).first();
  await link.click({ timeout: 8000 });
  await wait(p, 800);
  await S.view(shot);
  await p.keyboard.press('Escape');
  await wait(p, 400);
}

const desktop = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-research', () => navMenu(p, S, 'Research', 'nav-research'));
    await step('nav-policy', () => navMenu(p, S, 'Policy', 'nav-policy'));
    await step('nav-commitments', () => navMenu(p, S, 'Commitments', 'nav-commitments'));
    await step('nav-company', () => navMenu(p, S, 'Company', 'nav-company'));
    await step('nav-try', () => navMenu(p, S, 'Try Claude', 'nav-try'));
  } },
  news: { path: BASE + '/news', run: async (p, S) => { await S.view('default'); await S.full(); } },
  research: { path: BASE + '/research', run: async (p, S) => { await S.view('default'); await S.full(); } },
  engineering: { path: BASE + '/engineering', run: async (p, S) => { await S.view('default'); await S.full(); } },
  policy: { path: BASE + '/policy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  constitution: { path: BASE + '/constitution', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { path: BASE + '/company', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: BASE + '/careers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { path: BASE + '/search', run: async (p, S) => { await S.view('default'); await S.full(); } },
  model: { path: BASE + '/claude/opus', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { path: BASE + '/legal', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-open', async () => {
      const t = p.getByRole('button', { name: 'Open menu' });
      if (await t.count()) { await t.click(); await wait(p, 1200); await S.view('nav-open'); }
    });
  } },
  news: { path: BASE + '/news', run: async (p, S) => { await S.view('default'); await S.full(); } },
  research: { path: BASE + '/research', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${spec.name || name}-${spec.theme === 'dark' ? 'dark' : 'light'}`, vw, vh, dpr);
  try {
    await p.goto(spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { failures++; log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
if (failures) { console.error(`${failures} capture(s) failed`); process.exit(1); }
