// Captures joinhandshake.com's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// joinhandshake.com is the marketing site — a Next.js app that serves every
// signed-out page to a plain headless load. The consumer app on
// app.joinhandshake.com sits behind a Cloudflare managed challenge that lets
// a load through only intermittently: /access is retried in fresh contexts
// until the real "Log in or sign up" page arrives, and /explore, /signup and
// support.joinhandshake.com never cleared on 2026-11-17 — recorded as
// boundaries in the package README, never shot.
// The site paints light only (no theme control, no prefers-color-scheme
// rule), so there is no dark pass. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the nav's hover-opened mega menu, the employers segment tabs,
// the FAQ and careers accordions, and the phone's "Open menu" button. The
// Ketch consent banner is shot if it appears (consent) and then hidden,
// never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP_URL } from './lib.mjs';

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

// The marketing pages scroll the document; lazy content (images below the
// fold, deferred sections) is walked to the bottom and back so the full shot
// paints every section.
async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await wait(p, 800);
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
      try {
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
      }
    } finally {
      await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    }
    this.count++; log('  shot', name, 'H=' + H);
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The Ketch consent banner: shot once as evidence of the signed-out surface,
// then hidden by closePromo — never answered.
async function consentShot(p, S) {
  const seen = await p.evaluate(() => {
    const els = [...document.querySelectorAll('[id*="ketch" i], [class*="ketch" i], iframe[src*="ketch" i]')];
    return els.some((e) => { const r = e.getBoundingClientRect(); return r.width > 200 && r.height > 60; });
  });
  if (!seen) { log('  - no consent banner visible; consent shot skipped'); return; }
  await S.view('consent');
  await closePromo(p);
}

// The fixed nav's "Employers" item opens the mega menu on hover (its own
// aria-expanded state) — a local UI surface; the menu's links are never
// followed.
async function navMenu(p, S) {
  const item = p.locator('nav').first().locator('a,button').filter({ hasText: /^Employers$/ }).first();
  if (!(await item.count())) { log('  ! nav Employers item missing'); return; }
  const b = await item.boundingBox();
  if (!b) { log('  ! nav Employers item has no box'); return; }
  await p.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
  await wait(p, 1400);
  const open = await item.getAttribute('aria-expanded').catch(() => null);
  if (open !== 'true') log('  ! mega menu did not report open (aria-expanded=' + open + '); shooting anyway');
  await S.view('nav-open');
  await p.mouse.move(720, 820);
  await wait(p, 800);
}

// The employers segment switcher ("Source" / "Automate" / "Brand" /
// "Measure"): the buttons' own activation — a local UI toggle that swaps the
// published feature panel.
async function segmentTab(p, S) {
  const tab = p.locator('button').filter({ hasText: /^Automate$/ }).first();
  if (!(await tab.count())) { log('  ! segment tab missing'); return; }
  await tab.click({ timeout: 5000 }).catch(() => {});
  await wait(p, 1200);
  await S.view('tab-automate');
  const back = p.locator('button').filter({ hasText: /^Source$/ }).first();
  await back.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 600);
}

// An FAQ accordion row: the question button's own press opens the answer —
// a local UI toggle.
async function faqOpen(p, S, reText = /./) {
  const q = p.locator('button:visible').filter({ hasText: reText }).last();
  if (!(await q.count())) { log('  ! faq button missing'); return; }
  await q.scrollIntoViewIfNeeded().catch(() => {});
  await q.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 900);
  await S.view('faq-open');
  await q.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 400);
}

// The careers department filter: the "All departments" dropdown button opens
// the department list — a local UI toggle; the job links are never followed.
async function deptOpen(p, S) {
  const btn = p.locator('button:visible').filter({ hasText: /all departments|departments/i }).first();
  if (!(await btn.count())) { log('  ! dept accordion missing'); return; }
  await btn.scrollIntoViewIfNeeded().catch(() => {});
  await btn.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 1000);
  await S.view('dept-open');
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('nav-open', () => navMenu(p, S));
    await S.full();
  } },
  students: { url: BASE + '/students/', wait: 6000, run: BOTH },
  'whos-hiring': { url: BASE + '/students/whos-hiring/', wait: 6000, run: BOTH },
  employers: { url: BASE + '/employers/', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await step('tab-automate', () => segmentTab(p, S));
    await step('faq-open', () => faqOpen(p, S, /free plan|post a job directly|compare/i));
    await S.full();
  } },
  pricing: { url: BASE + '/employers/pricing/', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await step('faq-open', () => faqOpen(p, S, /how much does handshake cost/i));
    await S.full();
  } },
  'request-more-info': { url: BASE + '/employers/request-more-info/', wait: 8000, run: BOTH },
  'career-centers': { url: BASE + '/career-centers/', wait: 6000, run: BOTH },
  'cc-contact': { url: BASE + '/career-centers/contact/', wait: 8000, run: BOTH },
  'marketing-toolkit': { url: BASE + '/career-centers/marketing-toolkit/', wait: 6000, run: BOTH },
  careers: { url: BASE + '/careers/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('dept-open', () => deptOpen(p, S));
    await S.full();
  } },
  about: { url: BASE + '/about/', wait: 6000, run: BOTH },
  ai: { url: BASE + '/ai/', wait: 6000, run: BOTH },
  'ai-enterprise': { url: BASE + '/ai/enterprise/', wait: 6000, run: BOTH },
  'ai-opportunities': { url: BASE + '/ai/opportunities/', wait: 6000, run: BOTH },
  'research-ai': { url: BASE + '/research/ai/', wait: 6000, run: BOTH },
  blog: { url: BASE + '/blog/', wait: 6000, run: BOTH },
  'blog-article': { url: BASE + '/blog/students/how-to-search-for-jobs-on-handshake/', wait: 6000, run: BOTH },
  learn: { url: BASE + '/learn/', wait: 6000, run: BOTH },
  legal: { url: BASE + '/legal/tos/', wait: 6000, run: BOTH },
  privacy: { url: BASE + '/privacy-policy/', wait: 6000, run: BOTH },
  newsroom: { url: BASE + '/newsroom/', wait: 6000, run: BOTH },
  accessibility: { url: BASE + '/accessibility/', wait: 5000, run: BOTH },
  security: { url: BASE + '/security/', wait: 5000, run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Open menu" button opens the phone's nav sheet — a local UI
      // toggle; its links are never followed.
      const ham = p.getByRole('button', { name: /open menu|menu/i }).first();
      if (!(await ham.count())) { log('  ! hamburger missing'); return; }
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    await S.full();
  } },
  students: { url: BASE + '/students/', wait: 6000, run: BOTH },
  employers: { url: BASE + '/employers/', wait: 6000, run: BOTH },
  pricing: { url: BASE + '/employers/pricing/', wait: 6000, run: BOTH },
  blog: { url: BASE + '/blog/', wait: 6000, run: BOTH },
};

// The consumer app's "Log in or sign up" surface: reached through
// /login -> /access, behind a Cloudflare challenge that clears only
// intermittently — fresh contexts until the real page arrives.
const app = {
  access: { url: APP_URL, wait: 9000, app: true, run: BOTH },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, app: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, app: false })),
  ...Object.keys(app).map((k) => ({ k, mob: false, app: true })),
  { k: 'access', mob: true, app: true },
];
for (const { k, mob, app: isApp } of runs) {
  const spec = (isApp ? app : mob ? mobile : desktop)[k];
  if (!spec) continue;
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  log(name);
  let done = false;
  // The app surface's challenge clears only on some loads: retry fresh
  // contexts (up to 6) before recording the page as blocked.
  const tries = isApp ? 6 : 1;
  for (let attempt = 0; attempt < tries && !done; attempt++) {
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    await patch(ctx);
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
    try {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p, { tries: isApp ? 8 : 12, step: 2000 }))) { log('  BLOCKED challenge', spec.url, `(try ${attempt + 1})`); await ctx.close(); continue; }
      await wait(p, spec.wait || 8000);
      // The consent banner is shot where the page mounts it, before the first
      // closePromo hides it — hiding it first would always skip the shot.
      if (!isApp && name === 'home') await step('consent', () => consentShot(p, S));
      if (!isApp) await closePromo(p);
      await spec.run(p, S);
      done = true;
      total += S.count;
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    await ctx.close();
  }
  if (!done) log('  BOUNDARY', name, 'never loaded a real page');
}
log('done', total, 'screenshots ->', RAW);
await b.close();
