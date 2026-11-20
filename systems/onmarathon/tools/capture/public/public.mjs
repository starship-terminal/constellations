// Captures onmarathon.com's public archive pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// The live site paints one light theme (html.light). Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// Nothing is sent, signed into or submitted. Presses are local UI only:
// the phone menu, and the pricing Pay Monthly / Pay Annually toggle.
// Sign In and Get Started redirect to the archive homepage with no form;
// those URLs are recorded in site-tree.md and are not filled.
import fs from 'fs';
import os from 'os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'onmarathon', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
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
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
      }
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const openMobileMenu = async (p) => {
  const b = p.getByRole('button', { name: 'Open menu' });
  if (!(await b.count())) return false;
  await b.click();
  await wait(p, 600);
  return true;
};

const desktop = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  agencies: { path: '/for-agencies', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Pay Monthly' }).click();
      await wait(p, 500);
      await S.view('monthly');
      await p.getByRole('button', { name: 'Pay Annually' }).click();
      await wait(p, 400);
    });
    await S.full();
  } },
  demo: { path: '/demo', run: async (p, S) => { await S.view('default'); await S.full(); } },
  curated: { path: '/curated', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); });
    await step('menu-close', async () => {
      const b = p.getByRole('button', { name: 'Close menu' });
      if (await b.count()) { await b.click(); await wait(p, 400); }
    });
    await S.full();
  } },
  agencies: { path: '/for-agencies', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Pay Monthly' }).click();
      await wait(p, 500);
      await S.view('monthly');
    });
    await S.full();
  } },
  demo: { path: '/demo', run: async (p, S) => { await S.view('default'); await S.full(); } },
  curated: { path: '/curated', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { path: '/changelog', run: async (p, S) => { await S.view('default'); } },
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
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    if (!(await clearChallenge(p))) { log('  BLOCKED', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 1800);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
