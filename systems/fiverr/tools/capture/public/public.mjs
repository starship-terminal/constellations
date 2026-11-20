// Captures fiverr.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs xvfb-run -a node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// page paints light — fiverr.com has no user theme toggle (the hero search
// form's `dark` class is a component skin inside the light page, not a site
// theme). Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full`
// shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary.
//
// PerimeterX can gate a fresh client with a full-page "It needs a human
// touch" challenge (a PRESS & HOLD widget). Bot check: recorded as a
// boundary, not bypassed: clearChallenge() only waits, and a page that stays
// challenged is logged as BLOCKED and skipped. No clearance cookie is saved
// or replayed. Run under xvfb-run to launch real Chrome headed.
//
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the "Sidebar menu" drawer button, the home hero search field
// (focused and typed into then cleared, never searched), the gig page's
// Basic/Standard/Premium package tabs, an FAQ accordion — plus the gig and
// seller routes discovered from the public search results (the first gig
// card's own links, loaded directly). Search, sign-in, join, "Continue",
// "Contact me" and every checkout control were shot at rest, never
// submitted. The UserWay accessibility widget and any consent layer are
// hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, launchBrowser, chromium, UA, UA_MOBILE, BASE, LOGIN_URL, JOIN_URL } from './lib.mjs';

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
    // Autoplaying hero videos can stall a full-page raster; pausing media and
    // allowing 120s keeps the shot on heavy pages.
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW)) {
      if (old === `${this.prefix}-${name}.png` || old === `${this.prefix}-${name}.png.capture.json`
          || (old.startsWith(`${this.prefix}-${name}.part`) && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.unlinkSync(`${RAW}/${old}`);
    }
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
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens the "Sidebar menu" drawer (the header's hamburger: a local UI toggle
// whose ARTICLE panel slides in from the left, carrying Browse categories,
// the locale/currency buttons and Join/Sign-in) and shoots it.
async function sidebar(p, S) {
  const btn = p.locator('button[aria-label*="idebar" i], button:has-text("Sidebar menu")').filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no Sidebar menu trigger'); return; }
  const open = async () => p.evaluate(() => {
    const art = [...document.querySelectorAll('article')].find((x) => {
      const r = x.getBoundingClientRect();
      return /browse categories/i.test(x.innerText || '') && r.x >= -40 && r.width > 300;
    });
    return !!art;
  }).catch(() => false);
  for (let i = 0; i < 3 && !(await open()); i++) {
    await clickEl(btn, 4000).catch(() => {});
    await wait(p, 900);
    if (!(await open())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 900); }
  }
  if (!(await open())) { log('  ! sidebar did not report open; shooting anyway'); }
  await S.view('drawer');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// Discovers one live gig page and its seller profile from the public search
// results — the first gig card's own hrefs, loaded directly (public pages).
async function gigUrls(p) {
  return p.evaluate(() => {
    const cards = [...document.querySelectorAll('a[href]')].map((a) => a.getAttribute('href') || '');
    const gigHref = cards.find((h) => /^\/[^/]+\/[^/]{8,}/.test(h) && !h.startsWith('/categories') && !h.startsWith('/search') && !/join|login|start_selling|logo-maker|cp\//.test(h));
    const seller = gigHref ? '/' + gigHref.split('/')[1] : null;
    return { gig: gigHref, seller };
  }).catch(() => ({}));
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', () => sidebar(p, S));
    await S.full();
  } },
  categories: { url: BASE + '/categories', wait: 9000, theme: 'light', run: BOTH },
  'category-design': { url: BASE + '/categories/graphics-design', wait: 9000, theme: 'light', run: BOTH },
  'subcategory-logo': { url: BASE + '/categories/graphics-design/creative-logo-design', wait: 9000, theme: 'light', run: BOTH },
  search: { url: BASE + '/search/gigs?query=logo%20design', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const { gig, seller } = await gigUrls(p);
    if (gig) fs.writeFileSync(RAW + '/.gig-url', gig);
    if (seller) fs.writeFileSync(RAW + '/.seller-url', seller);
  } },
  gig: { url: null, dynGig: true, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  seller: { url: null, dynSeller: true, wait: 10000, theme: 'light', run: BOTH },
  join: { url: JOIN_URL, wait: 9000, theme: 'light', run: BOTH },
  login: { url: LOGIN_URL, wait: 9000, theme: 'light', run: BOTH },
  'logo-maker': { url: BASE + '/logo-maker', wait: 9000, theme: 'light', run: BOTH },
  about: { url: BASE + '/about-us', wait: 9000, theme: 'light', run: BOTH },
  selling: { url: BASE + '/start_selling', wait: 9000, theme: 'light', run: BOTH },
  'how-it-works': { url: BASE + '/cp/how-fiverr-works', wait: 9000, theme: 'light', run: BOTH },
  legal: { url: BASE + '/legal-portal', wait: 9000, theme: 'light', run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', () => sidebar(p, S));
    await S.full();
  } },
  search: { url: BASE + '/search/gigs?query=logo%20design', wait: 10000, theme: 'light', run: BOTH },
  gig: { url: null, dynGig: true, wait: 10000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  join: { url: JOIN_URL, wait: 9000, theme: 'light', run: BOTH },
};

// Resolve dynamic routes first (search must run before gig/seller on desktop).
const b = await launchBrowser();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
let gigPath = null, sellerPath = null;
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  if (spec.dynGig && !gigPath) { // discover from a fresh search load if the earlier run did not leave one
    try { gigPath = fs.readFileSync(`${RAW}/.gig-url`, 'utf8').trim() || null; } catch { /* none */ }
    if (!gigPath) { log(name, 'skipped — no gig URL discovered yet (run search first)'); continue; }
  }
  if (spec.dynSeller && !sellerPath) {
    try { sellerPath = fs.readFileSync(`${RAW}/.seller-url`, 'utf8').trim() || null; } catch { /* none */ }
    if (!sellerPath) { log(name, 'skipped — no seller URL discovered yet (run search first)'); continue; }
  }
  const url = spec.dynGig ? BASE + gigPath : spec.dynSeller ? BASE + sellerPath : spec.url;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name, url);
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, url);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge (boundary, not bypassed)', url); await ctx.close(); continue; }
    await wait(p, spec.wait || 8000);
    await spec.run(p, S);
    if (k === 'search' && !mob) {
      const { gig, seller } = await gigUrls(p);
      if (gig) gigPath = gig;
      if (seller) sellerPath = seller;
    }
    if (k === 'search' && mob) {
      const { gig } = await gigUrls(p);
      if (gig) gigPath = gigPath || gig;
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
