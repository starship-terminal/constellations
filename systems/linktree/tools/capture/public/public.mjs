// Captures linktr.ee's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches. An unbounded page truncates at 8 chunks.
//
// Nothing is sent, claimed or signed into. Consent overlays are hidden, never
// clicked. The claim field is never submitted. Login, register, admin and
// analytics are not opened.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, patch, chromium, UA, UA_MOBILE, BASE, PROFILE } from './lib.mjs';

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
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 700);
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
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const staged = [];
    try {
      if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) {
        fs.existsSync(tmp) && fs.unlinkSync(tmp);
        fs.existsSync(tmp + '.capture.json') && fs.unlinkSync(tmp + '.capture.json');
      }
      throw e;
    }
    const keep = new Set();
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      keep.add(path.basename(final));
      const sideTmp = tmp + '.capture.json', sideFinal = final + '.capture.json';
      if (fs.existsSync(sideTmp)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sideTmp, 'utf8'));
          meta.screenshot = path.basename(final);
          fs.writeFileSync(sideTmp, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* keep the sidecar */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    const isStaged = (n) => n.endsWith('.new.png') || n.endsWith('.new.png.capture.json');
    for (const old of fs.readdirSync(RAW).filter((n) =>
      !isStaged(n) && !keep.has(n) &&
      (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}

async function openMenu(p) {
  const btn = p.locator('button[aria-label="Toggle menu"]').first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 700);
  return true;
}

const desktop = {
  home: { path: '/', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/s/pricing', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  profile: { path: PROFILE, wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openMenu(p)) await S.view('menu-open');
  } },
  pricing: { path: '/s/pricing', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  profile: { path: PROFILE, wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
try {
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
      const url = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await wait(p, spec.wait || 5000);
      await closePromo(p);
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
} finally {
  await b.close();
}
log('done', total, 'screenshots ->', RAW);
