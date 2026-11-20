// Captures untitled.stream's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are the consent-card dismissal and
// in-page accordion/menu toggles. untitled.stream sits behind a Cloudflare managed challenge:
// a route whose challenge does not clear on its own is recorded as blocked, not captured. The
// committed shots were taken with navigator.webdriver masked; that mask is removed (README).
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots, as the kit's public.mjs does.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
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
  // shot() without the consent sweep — for documenting the consent card itself.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const base = `${this.prefix}-${name}`;
    // The new shot goes to a scratch folder first. Only once every tile is
    // written are this shot's earlier name.png and name.partN.png (and their
    // .capture.json sidecars) removed — stale tiles would otherwise be
    // stitched over the new shot — and the new files moved in, so a failed
    // refresh leaves the earlier full-colour shot in place.
    const tmp = fs.mkdtempSync(path.join(RAW, '.shot-'));
    try {
      const f = path.join(tmp, base);
      // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
      // without a ceiling the tile loop writes forever. Truncate at 8 chunks, as
      // the kit does, and record the boundary instead.
      const MAXH = 8 * chunk;
      const hCap = Math.min(H, MAXH);
      if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
      if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      for (const old of fs.readdirSync(RAW)) if (old === base + '.png' || old === base + '.png.capture.json' || (old.startsWith(base + '.part') && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.rmSync(path.join(RAW, old));
      for (const n of fs.readdirSync(tmp)) fs.renameSync(path.join(tmp, n), path.join(RAW, n));
    } finally {
      fs.rmSync(tmp, { recursive: true, force: true });
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// -- shared bits -------------------------------------------------------------
const clickEl = async (loc, ms = 10000) => {
  await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click()));
};
// The landing nav is a row of links (pricing, trust, login) — any flyout, if
// one exists, opens on hover; try hover then click as fallback.
const openAccordion = async (p) => {
  const a = p.locator('button[aria-expanded="false"], details:not([open]) summary').filter({ visible: true }).first();
  if (await a.count()) { await clickEl(a); await wait(p, 900); return true; }
  return false;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await step('consent', async () => {
      if (await p.locator('button:has-text("Reject all")').first().isVisible().catch(() => false)) await S.raw('consent');
    });
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => { if (await openAccordion(p)) await S.view('faq'); });
    await S.full();
  } },
  trust: { path: '/trust', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  trust: { path: '/trust', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

// Routes that usually stall inside Cloudflare's waiting room headless —
// attempted opportunistically: when the challenge happens to clear, the
// page is captured like any other; when it stalls, the route is logged as
// blocked rather than captured mid-interstitial.
const opportunistic = {
  login: { path: '/login' },
  terms: { path: '/terms' },
  privacy: { path: '/privacy' },
  'cookie-policy': { path: '/cookie-policy' },
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
  // bot check: Cloudflare's challenge is recorded as a boundary, not bypassed (no navigator.webdriver mask).
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      // The Remix error boundary can appear well after first paint — poll the
      // whole settle window and only proceed if it never shows.
      let clean = true;
      for (let i = 0; i < 10; i++) {
        await wait(p, 1500);
        if (await p.evaluate(() => /something went wrong/i.test(document.body.innerText)).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED cf-challenge-or-error', spec.path); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
  // bot check: Cloudflare's challenge is recorded as a boundary, not bypassed (no navigator.webdriver mask).
  const p = await ctx.newPage();
  for (const [name, spec] of Object.entries(opportunistic)) {
    if (pageArg.length && !pageArg.includes(name)) continue;
    const S = new Shooter(p, `${name}-light`, 1440, 900, 1);
    let ok = false;
    for (let attempt = 0; attempt < 2 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p, { tries: 10 }))) break;
      let clean = true;
      for (let i = 0; i < 8; i++) {
        await wait(p, 1500);
        if (await p.evaluate(() => /something went wrong/i.test(document.body.innerText)).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('BLOCKED cf-challenge-or-error', name); continue; }
    log(name, 'cleared');
    try { await killGeo(p); await S.view('default'); await S.full(); } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
  }
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
