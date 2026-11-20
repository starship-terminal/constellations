// Captures grow.google's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// grow.google is the signed-out public site of Grow with Google (Google's
// glue marketing framework). It paints light only — the bundle declares no
// dark media query and the header ships no theme control — so every shot is
// a light one. The site serves two regional editions: the US site and, for
// a visitor whose request announces a locale, the regional /intl/<locale>/
// edition. From this capture host (SG) the bare headless context gets the
// US site at /, while a real Chrome/Safari user agent or an explicit
// Accept-Language locale is 302'd to /intl/ALL_sg/ (the APAC edition).
// Deep links are never redirected. Both editions are captured: the US
// edition bare (the canonical surface) and the APAC home under the real-UA
// context as `apac-*` — the regional variant a local visitor actually sees.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought, booked or signed into: the only presses are
// local UI toggles — the deep-nav mega-menu trigger, the phone's "Open the
// navigation drawer" button, a certificate page's expansion-panel row, and
// the hero video's play button, which opens a glue-dialog YouTube modal
// (opened, never played through). The footer's
// <select name="lang-selector"> is measured but never changed: its form
// posts to services.google.com.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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

// grow.google scrolls the document normally; the helper still copes with an
// inner overflow pane if a page mounts one. lazyScroll walks it so lazy
// sections paint before the shot.
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

// For the full shot an inner scroller's ancestors are relaxed to natural
// height so the document becomes as tall as the content — a normal fullPage
// capture then paints every section, header still fixed at top. restore()
// puts the shell back so later shots see the real layout.
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

// The header's deep-nav mega-menu: the "Career Certificates" item is a real
// dropdown trigger (li.glue-header__item.dropdown, aria-haspopup). Its own
// click opens the panel — a local UI toggle verified by aria-expanded
// flipping true; the links inside are never followed. Escaped afterwards.
async function megaMenu(p, S) {
  await p.evaluate(() => {
    const li = [...document.querySelectorAll('.glue-header__item.dropdown')].find((l) => /Career Certificates/.test(l.innerText || '') && l.getBoundingClientRect().width > 50);
    if (li) li.querySelector('a').click();
  });
  await wait(p, 1600);
  const open = await p.evaluate(() => [...document.querySelectorAll('.glue-header__item.dropdown')].some((li) => li.getAttribute('aria-expanded') === 'true' || li.getAttribute('aria-selected') === 'true' || (li.querySelector('a[aria-expanded="true"], a[aria-selected="true"]'))));
  if (!open) { log('  ! mega-menu did not report open; shooting anyway'); }
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
  await p.evaluate(() => { const a = [...document.querySelectorAll('.glue-header__item.dropdown a')].find((x) => x.getAttribute('aria-expanded') === 'true'); if (a) a.click(); }).catch(() => {});
}

// The hero video's play button opens a glue-dialog carrying a YouTube embed —
// a local UI toggle. Opened for the shot, then closed; the video itself is
// never played through.
async function videoDialog(p, S) {
  const btn = p.locator('.glue-video.glue-modal__trigger, .glue-video__preview-container, glue-video button, button[aria-label*="play" i]').filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! video play button missing'); return; }
  const box = await btn.boundingBox().catch(() => null);
  if (box) await p.mouse.click(box.x + box.width / 2, box.y + box.height / 2);
  else await btn.dispatchEvent('click').catch(() => {});
  await wait(p, 3500);
  const open = await p.locator('.glue-modal.glue-modal-open, glue-dialog[open], [role="dialog"]:visible').first().isVisible().catch(() => false);
  if (!open) { log('  ! video dialog did not open'); await p.keyboard.press('Escape'); return; }
  await S.view('video');
  await p.keyboard.press('Escape');
  await wait(p, 700);
  await p.evaluate(() => { const c = document.querySelector('.glue-dialog__close, glue-dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]'); if (c) c.click(); }).catch(() => {});
}

// A certificate page's FAQ row: glue-expansion-panel rows toggle on their own
// header — a local UI toggle, opened for the shot then closed again.
async function faqOpen(p, S) {
  const t = p.locator('.glue-expansion-panel__toggle, .glue-expansion-panel__button').filter({ visible: true }).first();
  if (!(await t.count())) { log('  ! expansion panel missing'); return; }
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await wait(p, 1200);
  const open = await p.locator('.glue-expansion-panel:not(.glue-is-collapsed), [aria-expanded="true"].glue-expansion-panel__button').first().isVisible().catch(() => false);
  if (!open) log('  ! panel did not report open; shooting anyway');
  await S.view('faq-open');
  await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click())).catch(() => {});
  await wait(p, 500);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('menu', () => megaMenu(p, S));
    await step('video', () => videoDialog(p, S));
    await S.full();
  } },
  certificates: { url: BASE + '/certificates', wait: 7000, run: BOTH },
  'cert-ux': { url: BASE + '/certificates/ux-design/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('faq-open', () => faqOpen(p, S));
    await S.full();
  } },
  'cert-data': { url: BASE + '/certificates/data-analytics/', wait: 7000, run: BOTH },
  ai: { url: BASE + '/ai/', wait: 7000, run: BOTH },
  'ai-pro': { url: BASE + '/ai-professional/', wait: 7000, run: BOTH },
  stories: { url: BASE + '/stories/', wait: 7000, run: BOTH },
  mission: { url: BASE + '/our-mission/', wait: 7000, run: BOTH },
  partners: { url: BASE + '/partners/', wait: 7000, run: BOTH },
  employers: { url: BASE + '/employers/', wait: 7000, run: BOTH },
  news: { url: BASE + '/news-insights/', wait: 7000, run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Open the navigation drawer" button opens the phone's stepped-nav
      // drawer — a local UI toggle; its links are never followed.
      const ham = p.getByRole('button', { name: /open the navigation drawer|navigation drawer|menu/i }).filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! drawer toggle missing'); return; }
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1600);
      const open = await p.locator('.glue-header__drawer--open, [class*="drawer"][class*="open"], .glue-header [aria-expanded="true"]').first().isVisible().catch(() => false);
      if (!open) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await p.evaluate(() => { const c = document.querySelector('.glue-header__drawer-close-btn, [aria-label*="lose the navigation drawer" i]'); if (c) c.click(); }).catch(() => {});
    });
    await S.full();
  } },
  certificates: { url: BASE + '/certificates', wait: 7000, run: BOTH },
  'cert-ux': { url: BASE + '/certificates/ux-design/', wait: 7000, run: BOTH },
  ai: { url: BASE + '/ai/', wait: 7000, run: BOTH },
};

// The APAC regional variant: a real user agent and an explicit locale get
// the /intl/ALL_sg/ edition a local visitor sees. One home pass plus the
// phone's drawer documents the variant; its nav has no dropdown menus.
const apac = {
  'apac-home': { url: BASE + '/', wait: 8000, run: BOTH },
};
const apacMobile = {
  'apac-mobile-home': { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const ham = p.getByRole('button', { name: /open the navigation drawer|navigation drawer|menu/i }).filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! drawer toggle missing'); return; }
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1600);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, apac: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, apac: false })),
  ...Object.keys(apac).map((k) => ({ k, mob: false, apac: true })),
  ...Object.keys(apacMobile).map((k) => ({ k, mob: true, apac: true })),
];
for (const { k, mob, apac: isApac } of runs) {
  const name = (mob && !isApac ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (isApac ? (mob ? apacMobile : apac) : (mob ? mobile : desktop))[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  // US-edition contexts are bare: no locale, no user agent — grow.google
  // 302s a request that announces either to the regional /intl/ edition.
  const ctx = await b.newContext(isApac
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, isMobile: mob, hasTouch: mob });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  const runCtx = { extra: 0 };
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 8000);
    await spec.run(p, S, runCtx);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count + runCtx.extra;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
