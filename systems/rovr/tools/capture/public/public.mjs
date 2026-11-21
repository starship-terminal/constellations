// Captures ROVR's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png. ROVR paints one dark theme. Desktop shots are 1440x900 at 1x,
// mobile shots 390x844 at 2x. Nothing is signed into, submitted, or sent to Google or Apple.
// A control that opens a login wall is recorded as a URL and that branch stops.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, patch } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 7200);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.p.url().split('?')[0] }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openDrawer(p) {
  const b = p.getByRole('button', { name: /open drawer menu|open menu/i }).first();
  if (!(await b.count())) return false;
  await b.click();
  await wait(p, 700);
  return true;
}
async function closeDrawer(p) {
  const b = p.getByRole('button', { name: 'close drawer' });
  if (await b.count()) { await b.click(); await wait(p, 400); }
  else { await p.keyboard.press('Escape'); await wait(p, 300); }
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('quick-menu', async () => {
      await p.getByRole('button', { name: 'Show quick menu' }).click();
      await wait(p, 500);
      await S.view('quick-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('menu', async () => { if (await openDrawer(p)) { await S.view('menu'); await closeDrawer(p); } });
    await step('alexa', async () => {
      await p.getByRole('button', { name: 'Open Alexa modal' }).click();
      await wait(p, 700);
      await S.view('alexa');
      await p.getByRole('button', { name: 'Close' }).first().click().catch(() => {});
      await wait(p, 300);
    });
    await step('playing', async () => {
      await p.getByRole('button', { name: 'Listen to music' }).first().click();
      await wait(p, 900);
      await S.view('playing');
    });
    await S.full();
  } },
  moods: { path: '/moods', run: async (p, S) => { await S.view('default'); await S.full(); } },
  schedule: { path: '/schedule', run: async (p, S) => { await S.view('default'); await S.full(); } },
  curators: { path: '/curators', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const input = p.getByPlaceholder('Search by name');
      await input.click();
      await input.fill('Alex');
      await wait(p, 700);
      await S.view('search');
    });
    await S.full();
  } },
  curator: { path: '/curators/andre-navarro', run: async (p, S) => { await S.view('default'); await S.full(); } },
  archive: { path: '/archive', run: async (p, S) => { await S.view('default'); await S.full(); } },
  show: { path: '/show/ffolpe55moplhgyya2mn1fjt', run: async (p, S) => {
    await S.view('default');
    await step('tracklist', async () => {
      await p.getByRole('button', { name: 'TRACKLIST' }).click();
      await wait(p, 700);
      await S.view('tracklist');
    });
  } },
  search: { path: '/search', run: async (p, S) => {
    await S.view('default');
    await step('results', async () => {
      const input = p.locator('[role="dialog"] input, input[placeholder="SEARCH"]').last();
      await input.click();
      await input.fill('morning');
      await wait(p, 900);
      await S.view('results');
    });
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  // Auth walls. Loaded so the boundary is evidenced. Nothing is typed or submitted.
  'sign-in': { path: '/sign-in', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openDrawer(p)) { await S.view('menu'); await closeDrawer(p); } });
    await S.full();
  } },
  moods: { path: '/moods', run: async (p, S) => { await S.view('default'); } },
  schedule: { path: '/schedule', run: async (p, S) => { await S.view('default'); await S.full(); } },
  curators: { path: '/curators', run: async (p, S) => { await S.view('default'); } },
  archive: { path: '/archive', run: async (p, S) => { await S.view('default'); } },
  show: { path: '/show/ffolpe55moplhgyya2mn1fjt', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  'sign-in': { path: '/sign-in', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
