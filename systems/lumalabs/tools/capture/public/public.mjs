// Captures lumalabs.ai's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png. Inner pages (pricing, about, API,
// news) paint a light page. The home hero and /ray paint a dark video or
// image under a light nav, so those viewport shots are named dark. Desktop
// shots are 1440x900 at 1x, phone shots 390x844 at 2x, *-full shots at the
// same scale. A page taller than one GPU texture is tiled; an unbounded page
// truncates at 4 chunks.
//
// Nothing is signed into, submitted or purchased. Sign In, Try for free,
// Start Now, Use the API, Subscribe and the enterprise form Submit are never
// clicked. The home prompt is filled and cleared, never submitted. Consent
// overlays are hidden, never answered. Local toggles only: pricing interval,
// news filter, FAQ, mobile nav, API model tab.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', theme: 'dark', wait: 4000, run: async (p, S) => {
    await S.view('default');
    await step('prompt-filled', async () => {
      const field = p.locator('textarea, [contenteditable="true"]').first();
      if (!(await field.count())) return;
      await field.click({ timeout: 4000 });
      await p.keyboard.type('a short product film of a ceramic cup', { delay: 8 });
      await wait(p, 400);
      await S.view('prompt-filled');
      await p.keyboard.press('Meta+a');
      await p.keyboard.press('Backspace');
      await wait(p, 300);
    });
    await S.full();
  } },
  pricing: { path: '/pricing', theme: 'light', wait: 3500, run: async (p, S) => {
    await S.view('default');
    await step('yearly', async () => {
      const b = p.getByRole('button', { name: /^Yearly$/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('yearly'); }
    });
    await S.full();
  } },
  about: { path: '/about', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  api: { path: '/api', theme: 'light', wait: 3000, run: async (p, S) => {
    await S.view('default');
    await step('uni', async () => {
      const b = p.getByRole('button', { name: /^Uni-1\.1$/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('uni'); }
    });
    await S.full();
  } },
  enterprise: { path: '/enterprise', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  ray: { path: '/ray', theme: 'dark', wait: 3500, run: async (p, S) => { await S.view('default'); await S.full(); } },
  uni: { path: '/uni-1', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  news: { path: '/news', theme: 'light', wait: 3000, run: async (p, S) => {
    await S.view('default');
    await step('product', async () => {
      const b = p.getByRole('button', { name: /^Product$/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('product'); }
    });
    await S.full();
  } },
  mcp: { path: '/mcp', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  cases: { path: '/case-studies', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  learning: { path: '/learning-center', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  create: { path: '/create/ai-video-generator', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  agents: { path: '/models/luma-dream-machine-evolved-into-luma-agents', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/legal/terms-of-service', theme: 'light', wait: 2500, run: async (p, S) => { await S.view('default'); } },
  // A missing path on lumalabs.ai is served by Vercel as "Invalid slug" (the
  // captures/genie shell), not a Luma 404. That page is not this product and
  // is not captured.
  docs: { path: 'https://docs.lumalabs.ai/docs/welcome', theme: 'light', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', theme: 'dark', wait: 4000, run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      const b = p.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], header button').last();
      if (!(await b.count())) return;
      await b.click({ timeout: 8000 });
      await wait(p, 800);
      await S.view('nav');
      await p.keyboard.press('Escape');
    });
  } },
  pricing: { path: '/pricing', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  ray: { path: '/ray', theme: 'dark', wait: 3000, run: async (p, S) => { await S.view('default'); } },
  news: { path: '/news', theme: 'light', wait: 3000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = spec.theme || 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
    colorScheme: theme === 'dark' ? 'dark' : 'light',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name, theme);
  const target = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, target.split('?')[0]);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 3000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
