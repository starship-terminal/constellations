// Captures Leonardo.Ai's public signed-out pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/leonardo/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Surfaces: leonardo.ai marketing (dark canvas, one theme), app.leonardo.ai
// signed-out shell (dark, one theme), docs.leonardo.ai (ReadMe, dark), and
// the OAuth login card measured at rest. Desktop 1440x900 at 1x, phone
// 390x844 at 2x. Nothing is signed into, submitted, purchased or followed
// through OAuth. Consent overlays are hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP, DOCS } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      const tiles = [];
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        const tile = `${f}.part${i}.png`;
        await screenshotWithMetadata(p, { path: tile, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
        tiles.push(path.basename(tile));
      }
      // Written only after the last tile lands. quantize.py refuses to stitch
      // a set that has no record, or whose tiles do not match this list.
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({
        tiles, height: hCap, pageHeight: H, truncated: H > MAXH,
        captured: new Date().toISOString(),
      }, null, 2) + '\n');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc) => { await loc.click({ timeout: 8000 }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { url: BASE + '/', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  api: { url: BASE + '/api', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  learn: { url: BASE + '/learn', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { url: BASE + '/contact-us', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  imagegen: { url: BASE + '/ai-image-generator', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { url: BASE + '/this-page-does-not-exist-capture', theme: 'dark', wait: 4000, run: async (p, S) => { await S.view('default'); } },
  app: { url: APP + '/', theme: 'dark', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  blueprints: { url: APP + '/blueprints', theme: 'dark', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { url: APP + '/auth/login', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  docs: { url: DOCS + '/docs/getting-started', theme: 'dark', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { url: BASE + '/', theme: 'dark', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const ham = p.locator('button[aria-label*="menu" i], button[aria-label*="navigation" i], header button').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 900);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  app: { url: APP + '/', theme: 'dark', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { url: APP + '/auth/login', theme: 'dark', wait: 5000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  log(name);
  let shot = 0;
  for (let attempt = 1; attempt <= 3 && !shot; attempt++) {
    const ctx = await b.newContext({
      viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: 'dark',
    });
    await patch(ctx);
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
    try {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p, { tries: 8, step: 1500 }))) {
        log('  challenge attempt', attempt, spec.url);
        await ctx.close();
        continue;
      }
      // bot check: recorded as a boundary, not bypassed. Each context starts
      // empty; challenge-clearance cookies are never saved or replayed.
      await wait(p, spec.wait || 5000);
      await spec.run(p, S);
      shot = S.count;
      total += S.count;
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    await ctx.close();
  }
  if (!shot) log('  BLOCKED', spec.url);
}
log('done', total, 'screenshots ->', RAW);
await b.close();
