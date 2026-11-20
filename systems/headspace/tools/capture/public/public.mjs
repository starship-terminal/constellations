// Captures headspace.com's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// headspace.com paints one theme (light) — there is no theme control anywhere
// signed out, so there is no dark run. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought, redeemed or signed into: the only presses are the
// header's own hover mega-menu and the phone's nav button — local UI toggles
// whose links are never followed. The login and signup surfaces are reached
// through /login and /signup, which redirect to auth.headspace.com; the
// fields there are measured, never filled, and the buttons never pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, ORG, CHECKOUT } from './lib.mjs';

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
    try {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    } catch (e) {
      log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The header mega-menu is a CSS/JS hover dropdown: a real pointer hover over a
// category link opens the pane of subcategory links. The pane's links are
// never followed.
async function megaMenu(p, S) {
  const cat = p.locator('header a[data-testid="navbar-category-link"]').filter({ visible: true }).first();
  if (!(await cat.count())) { log('  ! category link missing'); return; }
  const b = await cat.boundingBox();
  await p.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
  await wait(p, 1400);
  const sub = await p.locator('header a[data-testid="navbar-subcategory-link"]').first().isVisible().catch(() => false);
  if (!sub) log('  ! mega menu did not open; shooting anyway');
  await S.view('menu');
  await p.mouse.move(p.viewportSize().width - 8, p.viewportSize().height - 8);
  await wait(p, 600);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', () => megaMenu(p, S));
    await S.full();
  } },
  app: { url: BASE + '/app', wait: 8000, run: BOTH },
  meditation: { url: BASE + '/meditation', wait: 7000, run: BOTH },
  mindfulness: { url: BASE + '/mindfulness', wait: 7000, run: BOTH },
  sleep: { url: BASE + '/sleep', wait: 7000, run: BOTH },
  therapy: { url: BASE + '/online-therapy', wait: 7000, run: BOTH },
  coaching: { url: BASE + '/coaching', wait: 7000, run: BOTH },
  ebb: { url: BASE + '/ai-mental-health-companion', wait: 7000, run: BOTH },
  'mental-health': { url: BASE + '/mental-health', wait: 7000, run: BOTH },
  anxiety: { url: BASE + '/mental-health/anxiety', wait: 7000, run: BOTH },
  science: { url: BASE + '/science', wait: 7000, run: BOTH },
  about: { url: BASE + '/about-us', wait: 7000, run: BOTH },
  articles: { url: BASE + '/articles', wait: 7000, run: BOTH },
  article: { url: BASE + '/articles/can-you-use-hsa-or-fsa-for-mental-health', wait: 7000, run: BOTH },
  content: { url: BASE + '/content', wait: 8000, run: BOTH },
  topic: { url: BASE + '/content/topics/100', wait: 8000, run: BOTH },
  subscriptions: { url: BASE + '/subscriptions', wait: 8000, run: BOTH },
  family: { url: BASE + '/family-plan', wait: 7000, run: BOTH },
  gift: { url: BASE + '/buy/gift', wait: 7000, run: BOTH },
  share: { url: BASE + '/share-headspace', wait: 7000, run: BOTH },
  redeem: { url: BASE + '/code', wait: 7000, run: BOTH },
  'mindful-families': { url: BASE + '/app/mindful-families', wait: 7000, run: BOTH },
  'org-home': { url: ORG + '/', wait: 8000, run: BOTH },
  'org-employers': { url: ORG + '/employers', wait: 7000, run: BOTH },
  checkout: { url: CHECKOUT + '/checkout', wait: 9000, run: BOTH },
  // /login and /signup redirect to auth.headspace.com's universal login —
  // a public surface. The fields are shot, never filled; the buttons never
  // pressed. The redirect's `state` query is never recorded (the sidecar's
  // sanitizedSourceUrl is the /login or /signup URL the page was opened on).
  login: { url: BASE + '/login', wait: 9000, run: BOTH },
  signup: { url: BASE + '/signup', wait: 9000, run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The phone's nav button opens the nav sheet — a local UI toggle; the
      // links inside are never followed.
      const ham = p.locator('header button, header [role="button"]').filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! hamburger missing'); return; }
      await ham.tap({ timeout: 5000 }).catch(() => ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click())));
      await wait(p, 1600);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
      await p.evaluate(() => { const c = document.querySelector('[class*="close" i] button, button[aria-label*="close" i]'); if (c) c.click(); });
    });
    await S.full();
  } },
  subscriptions: { url: BASE + '/subscriptions', wait: 8000, run: BOTH },
  meditation: { url: BASE + '/meditation', wait: 7000, run: BOTH },
  content: { url: BASE + '/content', wait: 8000, run: BOTH },
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
    await wait(p, spec.wait || 8000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
