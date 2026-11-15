// Captures figma.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// marketing page on www.figma.com paints the :root light token layer — the
// `--fig-theme-*` roles; a `:root[data-theme='dark']` layer is declared but no
// public page was seen to paint it, so every shot is -light. /community,
// /login and /signup are served by the product app shell (data-product-locale
// on <html>), a different stack that also paints light. Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than
// one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log records
// the boundary. Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the header's "Products"/"Solutions" nav-dropdown triggers
// and the phone's "Open navigation menu" button. The contact, make-prompt,
// login and signup forms are shot at rest, never submitted. The "This website
// uses cookies" consent dialog is hidden before every shot, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LOGIN_URL } from './lib.mjs';

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
    await closePromo(p);
    await lazyScroll(p);
    // Pages whose demos autoplay video/canvas (figjam, dev-mode, design-systems)
    // can stall a full-page raster past the default 30s; pausing media and
    // allowing 120s keeps the shot on heavy pages.
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    try {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    } catch (e) {
      log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Opens one of the header's nav-dropdown menus ("Products"/"Solutions" —
// button[data-nav-dropdown-trigger], local UI toggles whose panels mount beside
// the button, never links) and shoots the open panel. A pointer click flips
// aria-expanded; keyboard Enter is the fallback. The panel's demo videos pause
// while it is open so a frame cannot be starved.
async function navMenu(p, S, name) {
  const btn = p.locator(`button[data-nav-dropdown-trigger]`).filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await btn.click({ timeout: 5000 }).catch(() => {});
    await wait(p, 700);
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 700); }
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
  await S.view('menu-' + name.toLowerCase());
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-products', () => navMenu(p, S, 'Products'));
    await step('menu-solutions', () => navMenu(p, S, 'Solutions'));
    await S.full();
  } },
  design: { url: BASE + '/design/', wait: 8000, theme: 'light', run: BOTH },
  figjam: { url: BASE + '/figjam/', wait: 8000, theme: 'light', run: BOTH },
  slides: { url: BASE + '/slides/', wait: 8000, theme: 'light', run: BOTH },
  'dev-mode': { url: BASE + '/dev-mode/', wait: 8000, theme: 'light', run: BOTH },
  make: { url: BASE + '/make/', wait: 8000, theme: 'light', run: BOTH },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: BOTH },
  community: { url: BASE + '/community', wait: 9000, theme: 'light', run: BOTH },
  'community-plugins': { url: BASE + '/community/plugins', wait: 9000, theme: 'light', run: BOTH },
  blog: { url: BASE + '/blog/', wait: 8000, theme: 'light', run: BOTH },
  customers: { url: BASE + '/customers/', wait: 8000, theme: 'light', run: BOTH },
  enterprise: { url: BASE + '/enterprise/', wait: 8000, theme: 'light', run: BOTH },
  careers: { url: BASE + '/careers/', wait: 8000, theme: 'light', run: BOTH },
  contact: { url: BASE + '/contact/', wait: 8000, theme: 'light', run: BOTH },
  downloads: { url: BASE + '/downloads/', wait: 8000, theme: 'light', run: BOTH },
  'design-systems': { url: BASE + '/design-systems/', wait: 8000, theme: 'light', run: BOTH },
  'release-notes': { url: BASE + '/release-notes/', wait: 8000, theme: 'light', run: BOTH },
  login: { url: LOGIN_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signup: { url: BASE + '/signup', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's "Open navigation menu" button toggles the phone nav — a
      // local UI toggle; its links are never followed. The button flips
      // aria-expanded and the overlay mounts as a fixed body-level div.
      const ham = p.locator('button[aria-label="Open navigation menu"]').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      const open = () => p.evaluate(() => {
        const b = [...document.querySelectorAll('button')].find((x) => /navigation menu/i.test(x.getAttribute('aria-label') || ''));
        return !!b && b.getAttribute('aria-expanded') === 'true';
      }).catch(() => false);
      if (!(await open())) await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 1500); }
      if (!(await open())) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: BOTH },
  community: { url: BASE + '/community', wait: 9000, theme: 'light', run: BOTH },
  contact: { url: BASE + '/contact/', wait: 8000, theme: 'light', run: BOTH },
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
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 8000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
