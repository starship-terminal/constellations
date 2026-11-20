// Captures hitchd.com's signed-out public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// hitchd.com ships one theme — no dark mode or theme switcher exists on the
// marketing pages, the couple app or the guest registry app — so there is no
// dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary
// (the /blog index is ~46,000px of article rows).
// Nothing is sent, typed, bought or signed into: the only presses are local
// UI toggles — the registry's "Sort by" filter select, a gift card opening
// the gift modal, and the phone's #menuToggle hamburger. The auth forms
// (/login, /signup, /forgot-password) are shot at rest only; the gift
// modal's Give/contribute and payment steps are never entered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, openRegistry } from './lib.mjs';

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
  const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  // The Angular apps' boot resets the read of devicePixelRatio, so the
  // sidecar's expected size (css x dpr-at-eval-time) can disagree with the
  // PNG while the PNG itself is the right 2x capture — log the mismatch and
  // keep the shot rather than aborting the page.
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); /* a dimension mismatch fails the shot (2026-11 audit) */ this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
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
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    const snap = (o) => screenshotWithMetadata(p, o, this.requested); /* a dimension mismatch fails the shot (2026-11 audit) */
    // a manifest tells quantize.py how many tiles the page owed: a tile that
    // times out leaves a shortened part set, and without the intended count a
    // partial sheet could stitch and pass as complete
    const manifest = () => `${f}.full.json`;
    fs.writeFileSync(manifest(), JSON.stringify({ scrollHeight: H, capturedHeight: hCap, chunkHeight: chunk, expectedTiles: Math.ceil(hCap / chunk), tilesWritten: 0 }, null, 1) + '\n');
    let written = 0;
    try {
      if (hCap <= chunk) { await snap({ ...opts(f + '.png'), fullPage: true }); written = 1; }
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) { await snap({ ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }); written++; }
    } catch (e) {
      log('  ! full shot failed:', String(e.message).split('\n')[0]);
    }
    fs.writeFileSync(manifest(), JSON.stringify({ scrollHeight: H, capturedHeight: hCap, chunkHeight: chunk, expectedTiles: Math.ceil(hCap / chunk), tilesWritten: written }, null, 1) + '\n');
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The registry's "Sort by" filter: a styled <select> inside .toggle-dd.gift-filter.
// Two stacked variants are rendered and only one paints at a given width —
// the visible one is the same element measure.mjs reads. Picking an option
// re-filters the gift list — a local UI toggle; nothing is submitted.
// "opened" focuses the select's own dropdown state; then "Still needed" is
// selected and shot as its own state — but only once that state is true.
async function registryFilters(p, S) {
  const sel = p.locator('.toggle-dd.gift-filter select:visible, .gift-filter select:visible, select:visible').first();
  if (!(await sel.count())) { log('  ! sort select missing'); return; }
  await sel.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 600);
  await S.view('sort-open');
  const opt = await sel.locator('option').allInnerTexts();
  const still = opt.findIndex((t) => /still needed/i.test(t));
  if (still >= 0) {
    await sel.selectOption({ index: still }).catch(() => {});
    await wait(p, 1200);
    // require the requested state before saving: the select must report the
    // "Still needed" option selected, otherwise the shot would record the
    // default list under the filtered name
    const applied = (await sel.evaluate((el, i) => el.selectedIndex === i, still).catch(() => false));
    if (!applied) { log('  ! filter did not apply; skipping state'); await sel.selectOption({ index: 0 }).catch(() => {}); return; }
    await S.view('filter-still-needed');
    await sel.selectOption({ index: 0 }).catch(() => {});
    await wait(p, 800);
  }
}

// A gift card's own tap navigates to /<registry>/<gift-slug> and the guest
// app renders the gift modal over the registry. Shot open at rest — the
// "Give" button, amount field and payment steps are never entered — then the
// history goes back to the registry.
async function giftModal(p, S) {
  // the same elements measure.mjs reads: ol.gift-list .giftz tiles, and the
  // tile's own .click-space / .view-gift hit target — a bare div click can
  // land on a child that swallows the event instead of navigating
  const card = p.locator('ol.gift-list .giftz:visible').filter({ hasText: /Accommodation|Airbnb|Seafood|Road Trip|Dinner|Lessons|Tour/ }).first();
  const target = (await card.count()) ? card : p.locator('ol.gift-list .giftz:visible').first();
  if (!(await target.count())) { log('  ! gift card missing'); return; }
  await target.scrollIntoViewIfNeeded();
  await target.locator('.click-space, .view-gift').first().click({ timeout: 8000 }).catch(() => {});
  await wait(p, 5000);
  const modal = p.locator('.gift-modal:visible, .modalDialog:visible').first();
  if (!(await modal.count())) { log('  ! gift modal did not open; no shot saved'); await p.goBack().catch(() => {}); return; }
  await S.view('gift-modal');
  await p.goBack({ waitUntil: 'domcontentloaded' }).catch(() => p.goto('https://www.hitchd.com/zoeandnoah'));
  await wait(p, 4000);
}

// The phone hamburger: a hidden #menuToggle checkbox drives the .mobile-menu
// drawer (`input:checked ~ ul`). Clicking its label toggles the menu — a
// local UI toggle; the menu links are never followed.
async function mobileMenu(p, S) {
  const toggle = p.locator('#menuToggle input, .mobile-menu #menuToggle input').first();
  if (!(await toggle.count())) { log('  ! #menuToggle missing'); return; }
  const before = await p.evaluate(() => !document.querySelector('.mobile-menu') || document.querySelector('.mobile-menu').classList.contains('mobile-menu-hidden'));
  await toggle.click({ timeout: 4000, force: true }).catch(() => toggle.evaluate((el) => { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); }));
  await wait(p, 1200);
  const openCls = await p.evaluate(() => (document.querySelector('.mobile-menu') || { className: '' }).className);
  if (/mobile-menu-hidden/.test(openCls)) log('  ! menu still hidden after toggle; shooting anyway');
  await S.view('menu');
  await toggle.evaluate((el) => { if (el.checked) el.click(); }).catch(() => {});
  await wait(p, 600);
  return before;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };
const REST = async (p, S) => { await S.view('default'); };  // auth forms: rest only, nothing focused or typed

const desktop = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: BASE + '/login', wait: 8000, run: REST },
  signup: { url: BASE + '/signup', wait: 8000, run: REST },
  'forgot-password': { url: BASE + '/forgot-password', wait: 8000, run: REST },
  blog: { url: BASE + '/blog', wait: 7000, run: BOTH },
  post: { url: BASE + '/blog/what-is-a-honeymoon-registry', wait: 7000, run: BOTH },
  terms: { url: BASE + '/terms', wait: 7000, run: BOTH },
  privacy: { url: BASE + '/privacy', wait: 7000, run: BOTH },
  trips: { url: BASE + '/trips/australia', wait: 7000, run: BOTH },
  guide: { url: BASE + '/guides/add-hitchd-to-knot-wedding-webiste', wait: 7000, run: BOTH },
  registry: { url: BASE + '/zoeandnoah', painted: true, run: async (p, S) => {
    await S.view('default');
    await step('sort', () => registryFilters(p, S));
    await step('gift-modal', () => giftModal(p, S));
    await S.full();
  } },
  'coming-soon': { url: BASE + '/avaandbenjamin', wait: 30000, run: REST },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: BOTH },
  login: { url: BASE + '/login', wait: 8000, run: REST },
  blog: { url: BASE + '/blog', wait: 7000, run: REST },
  post: { url: BASE + '/blog/what-is-a-honeymoon-registry', wait: 7000, run: BOTH },
  registry: { url: BASE + '/zoeandnoah', painted: true, run: async (p, S) => {
    await S.view('default');
    await step('menu', () => mobileMenu(p, S));
    await S.full();
  } },
  'coming-soon': { url: BASE + '/avaandbenjamin', wait: 30000, run: REST },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    if (spec.painted) {
      // the guest registry boots its Angular data fetch nondeterministically;
      // share measure.mjs's painted-wait (a nonzero-size .giftz tile) rather
      // than trusting a fixed sleep
      if (!(await openRegistry(p))) log('  ! registry never painted; default shot records the shell it reached');
    } else {
      await wait(p, spec.wait || 8000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
