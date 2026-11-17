// Captures www.hbomax.com's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   xvfb-run -a env PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// hbomax.com 301s to www.hbomax.com and its geo-redirect lands the browser on
// the market locale — /sg/en here ("HBO Max | Watch Better"). The site ships
// one theme, dark, so every shot is -dark: Akamai denies headless Chromium a
// 403 "Access Denied" page, so the whole suite runs headed under xvfb (the
// HEADLESS=1 escape in lib.mjs exists only to prove the block). Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than one
// GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log
// records the boundary. auth.hbomax.com (sign-in, create-account, plan
// checkout) and help.hbomax.com are documented boundaries, never opened.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the hero carousel's own Next control, the monthly/yearly plan
// toggle, the FAQ accordion's own question buttons and the phone's menu
// button when one exists. The cookie consent modal is shot once as the
// 'promo' state, then hidden (never accepted, never declined).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LOCALE } from './lib.mjs';

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

// hbomax.com scrolls the document normally; a long page's lazy sections
// (the "Discover The Best Of" rails) paint on approach, so lazyScroll walks
// the document before a full shot. Inner-scrolling panes are still handled
// the same way when one shows up.
async function findScroller(p) {
  return p.evaluate(() => {
    let sc = null, best = 0;
    for (const el of document.querySelectorAll('div,main,section')) {
      const cs = getComputedStyle(el);
      if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > best) { best = el.scrollHeight; sc = el; }
    }
    if (sc) sc.setAttribute('data-fp-scroller', '1');
    return sc ? { h: sc.scrollHeight, inner: true } : { h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight), inner: false };
  });
}

async function lazyScroll(p) {
  const info = await findScroller(p);
  if (info.inner) {
    for (let y = 0; y < info.h; y += 700) { await p.evaluate((y) => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = y; }, y); await wait(p, 180); }
    await p.evaluate(() => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = 0; });
  } else {
    for (let y = 0; y < info.h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
    await p.evaluate(() => scrollTo(0, 0));
  }
  await wait(p, 900);
}

async function expandScroller(p) {
  return p.evaluate(() => {
    const sc = document.querySelector('[data-fp-scroller]');
    if (!sc) return null;
    for (let el = sc; el && el !== document.documentElement; el = el.parentElement) {
      el.setAttribute('data-fp-expand', '1');
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
      el.style.setProperty('flex', 'none', 'important');
    }
    for (const el of [document.body, document.documentElement]) {
      el.setAttribute('data-fp-expand', '1');
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
    }
    return true;
  });
}
async function restoreShell(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('[data-fp-expand]')) {
      for (const prop of ['height', 'max-height', 'min-height', 'overflow', 'flex']) el.style.removeProperty(prop);
      el.removeAttribute('data-fp-expand');
    }
    const sc = document.querySelector('[data-fp-scroller]');
    if (sc) { sc.removeAttribute('data-fp-scroller'); sc.scrollTop = 0; }
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  // A shot of the page exactly as it arrived — for the consent modal, which
  // view() would hide first.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await expandScroller(p);
    await wait(p, 1200);
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
      await restoreShell(p).catch(() => {});
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The hero carousel's own "Next Carousel Slide" control — a local UI toggle
// that swaps the featured slide. Its links are never followed.
async function carouselNext(p, S) {
  const next = p.locator('a.carousel-control-next, button.carousel-control-next, [class*="carousel-control-next"]').filter({ visible: true }).first();
  if (!(await next.count())) { log('  ! carousel next missing'); return; }
  await next.click({ timeout: 5000 }).catch(() => next.evaluate((el) => el.click()));
  await wait(p, 1600);
  await S.view('carousel-next');
}

// The "Find Your Perfect Plan" section's own monthly/yearly toggle — a local
// UI toggle that changes which published prices the cards show.
async function planYearly(p, S) {
  const sec = p.locator('[class*="pp4experiment"], [class*="t1-parent"], section').filter({ hasText: /find your perfect plan/i }).first();
  const btn = (await sec.count() ? sec : p).locator('button').filter({ hasText: /yearly|annual/i }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! plan yearly toggle missing'); return; }
  await btn.scrollIntoViewIfNeeded();
  await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
  await wait(p, 1000);
  await S.view('plan-yearly');
}

// The FAQ section's own question buttons open published answer text — a
// local UI toggle. One item is opened, shot, then left open (harmless).
async function faqOpen(p, S) {
  const item = p.locator('.max-section-faq button, [class*="faq"] button').filter({ hasText: /sign up|bundle/i }).filter({ visible: true }).first();
  if (!(await item.count())) { log('  ! faq item missing'); return; }
  await item.scrollIntoViewIfNeeded();
  await item.click({ timeout: 5000 }).catch(() => item.evaluate((el) => el.click()));
  await wait(p, 900);
  await S.view('faq-open');
  await p.evaluate(() => scrollTo(0, 0));
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const HOME = BASE + LOCALE;
const desktop = {
  home: { url: HOME, wait: 9000, promo: 'keep', run: async (p, S) => {
    await S.raw('promo');
    await closePromo(p);
    await S.view('default');
    await step('carousel-next', () => carouselNext(p, S));
    await step('plan-yearly', () => planYearly(p, S));
    await step('faq-open', () => faqOpen(p, S));
    await S.full();
  } },
  movies: { url: BASE + LOCALE + '/movies', wait: 9000, run: BOTH },
  shows: { url: BASE + LOCALE + '/shows', wait: 9000, run: BOTH },
  channel: { url: BASE + LOCALE + '/channel', wait: 9000, run: BOTH },
  show: { url: BASE + LOCALE + '/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf', wait: 9000, run: BOTH },
  movie: { url: BASE + LOCALE + '/movie/710798da-f811-40be-9ed9-3a7443e36278', wait: 9000, run: BOTH },
  collection: { url: BASE + LOCALE + '/collections/genre/kids-family', wait: 9000, run: BOTH },
  sitemap: { url: BASE + LOCALE + '/sitemap', wait: 8000, run: BOTH },
  'corp-info': { url: BASE + LOCALE + '/corp-info', wait: 8000, run: BOTH },
  privacy: { url: BASE + '/privacy', wait: 8000, run: BOTH },
};

const mobile = {
  home: { url: HOME, wait: 9000, promo: 'keep', run: async (p, S) => {
    await S.raw('promo');
    await closePromo(p);
    await S.view('default');
    await S.full();
  } },
  movies: { url: BASE + LOCALE + '/movies', wait: 9000, run: BOTH },
  show: { url: BASE + LOCALE + '/show/e6e7bad9-d48d-4434-b334-7c651ffc4bdf', wait: 9000, run: BOTH },
};

const b = await chromium.launch({ headless: process.env.HEADLESS === '1' });
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
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr, spec.url);
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
