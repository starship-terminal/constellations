// Captures IFTTT's signed-out public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// IFTTT paints a single light theme — there is no theme control anywhere
// (dark heroes on explore, service, connect and applet pages are painted
// sections, not a switchable theme) — so `light` is the only run. Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots at CSS
// scale. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought, typed, searched, shared or signed into: the only presses are
// local UI toggles — the plans Monthly/Yearly billing switch, the featured
// tabs, the applet page's Share button (its own modal, then its own close),
// the mobile hamburger, and "show more" text expanders. Log in, Get
// started, Connect, the plan "Get started" links and every store link are
// never pressed: they lead to sign-in, account or off-site surfaces.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, HOME } from './lib.mjs';

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

// Marketing pages scroll the document; IFTTT has no inner overflow panes on
// the signed-out surfaces, but keep the scroller detection — a long applet
// list or sticky shell could introduce one.
async function findScroller(p) {
  for (let tries = 0; tries < 10; tries++) {
    const info = await p.evaluate(() => {
      let sc = null, best = 0;
      for (const el of document.querySelectorAll('div,main,section,article')) {
        const cs = getComputedStyle(el);
        if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > best) { best = el.scrollHeight; sc = el; }
      }
      if (sc) sc.setAttribute('data-fp-scroller', '1');
      return {
        h: sc ? sc.scrollHeight : Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        inner: !!sc,
        docH: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        vh: window.innerHeight,
      };
    });
    if (info.inner || info.docH > info.vh + 50 || tries === 9) return info;
    await wait(p, 800);
  }
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
// height so the document itself becomes as tall as the content — a normal
// fullPage capture then paints every section, header still fixed at top.
// restoreShell() puts the shell back so later shots see the real layout.
async function expandScroller(p) {
  return p.evaluate(() => {
    const sc = document.querySelector('[data-fp-scroller]');
    if (!sc) return null;
    for (let el = sc; el && el !== document.documentElement; el = el.parentElement) {
      el.setAttribute('data-fp-expand', '1');
      // flex:none relaxes height but also drops the flex-basis width, letting
      // the pane grow wider than the viewport — pin the measured border-box
      // width so the full-page shot keeps the real layout.
      const w = el.getBoundingClientRect().width;
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
      el.style.setProperty('flex', 'none', 'important');
      el.style.setProperty('box-sizing', 'border-box', 'important');
      el.style.setProperty('width', `${w}px`, 'important');
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
      for (const prop of ['height', 'max-height', 'min-height', 'overflow', 'flex', 'box-sizing', 'width']) el.style.removeProperty(prop);
      el.removeAttribute('data-fp-expand');
    }
    const sc = document.querySelector('[data-fp-scroller]');
    if (sc) { sc.removeAttribute('data-fp-scroller'); sc.scrollTop = 0; }
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full', maxChunks = 8) {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await expandScroller(p);
    await wait(p, 1200);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    // The bound is in CSS pixels: scale:'css' clips are CSS px and the
    // documented bound (eight chunks = 112k px) describes page coverage —
    // dividing by dpr would halve mobile coverage. A @2x tile's PNG is
    // 28k device px tall; still well inside what the stitcher handles.
    const chunk = 14000;
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and
    // record the boundary instead.
    const MAXH = maxChunks * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    const plan = { intendedHeight: hCap, pageHeight: H, chunk, parts: hCap <= chunk ? 0 : Math.ceil(hCap / chunk), scale: 'css' };
    // Written before the tiles so quantize.py can prove the stitched set is
    // whole — a mid-loop failure must never publish a truncated sheet.
    fs.writeFileSync(`${f}.plan.json`, JSON.stringify(plan, null, 1) + '\n');
    const shootTiles = async (extra = {}) => {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, ...extra }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, ...extra }, this.requested);
    };
    const dropPartials = () => {
      // A tile loop that dies mid-run leaves parts 0..k of n — the stitcher
      // would publish a truncated sheet as a full page. Remove every tile so
      // quantize.py has nothing partial to stitch.
      for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.plan.json`)) fs.unlinkSync(`${RAW}/${old}`);
    };
    try {
      try {
        await shootTiles();
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        dropPartials();
        try {
          await shootTiles({ animations: 'disabled' });
        } catch (e2) {
          dropPartials();
          throw e2;
        }
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

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

// The Share button on detail pages opens .modal, the site's own share sheet
// (url field + social icons + Copy). It is a local UI toggle — opened for
// the shot, closed with its own X. Copy is never pressed.
async function shareShot(p, S) {
  const btn = p.locator('button.modal-open').filter({ hasText: /share/i }).first();
  if (!(await btn.count())) { log('  ! no share button on this page'); return; }
  await btn.click({ timeout: 5000 }).catch(() => {});
  await wait(p, 1200);
  if (!(await p.locator('div.share-modal:visible, div.modal:visible').count())) { log('  ! share modal did not open'); return; }
  await S.view('share-modal');
  const x = p.locator('.share-modal .modal-close, .share-modal [class*="close"], .modal .modal-close, .modal [class*="close"]').first();
  if (await x.count()) await x.click({ timeout: 4000 }).catch(() => {});
  else await p.keyboard.press('Escape');
  await wait(p, 800);
}

const desktop = {
  home: { url: HOME + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('featured-tab', async () => {
      // A featured category tab is a local UI toggle: press one, shoot the
      // repainted card row, return to Popular.
      const tab = p.locator('button.featured-tab').filter({ hasText: /^smart home$/i }).first();
      if (!(await tab.count())) return;
      await tab.click({ timeout: 5000 }).catch(() => {});
      await wait(p, 1500);
      await p.evaluate(() => scrollTo(0, 0));
      const row = p.locator('[class*="featured"]:visible').first();
      await row.scrollIntoViewIfNeeded().catch(() => {});
      await wait(p, 700);
      await S.view('featured-tab');
      const pop = p.locator('button.featured-tab').filter({ hasText: /^popular$/i }).first();
      if (await pop.count()) await pop.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
    });
    await step('prompt-focused', async () => {
      const f = p.locator('textarea.prompt-hero-input').first();
      await f.scrollIntoViewIfNeeded(); await f.click({ timeout: 4000 });
      await wait(p, 600);
      await S.view('prompt-focused');
    });
  } },
  explore: { url: BASE + '/explore', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('prompt-focused', async () => {
      const f = p.locator('textarea.prompt-hero-input').first();
      await f.scrollIntoViewIfNeeded(); await f.click({ timeout: 4000 });
      await wait(p, 600);
      await S.view('prompt-focused');
    });
  } },
  'explore-services': { url: BASE + '/explore/services', wait: 7000, run: BOTH },
  'explore-stories': { url: BASE + '/explore/stories', wait: 7000, run: BOTH },
  'explore-applets': { url: BASE + '/explore/applets', wait: 7000, run: BOTH },
  plans: { url: BASE + '/plans', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      // The Monthly/Yearly billing switch (role=switch) is a local UI
      // toggle: flip it off, shoot the repainted prices, flip it back.
      const sw = p.locator('button.switch-field[role="switch"]').first();
      if (!(await sw.count())) return;
      await sw.click({ timeout: 5000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('monthly');
      await sw.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
    });
  } },
  'service-twitter': { url: BASE + '/twitter', wait: 7000, run: async (p, S) => {
    await BOTH(p, S);
    await step('show-more', async () => {
      // "show more" expands the service blurb in place — a local toggle.
      const m = p.locator('a,button').filter({ hasText: /^show more$/i }).first();
      if (!(await m.count())) return;
      await m.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await p.evaluate(() => scrollTo(0, 0));
      await S.view('show-more');
    });
    await step('share-modal', () => shareShot(p, S));
  } },
  'service-todoist': { url: BASE + '/todoist', wait: 7000, run: async (p, S) => {
    await BOTH(p, S);
    await step('share-modal', () => shareShot(p, S));
  } },
  applet: { url: BASE + '/applets/A38TqjpD-start-irobot-cleaning-when-you-leave-home', wait: 7000, run: async (p, S) => {
    await BOTH(p, S);
    // The big Connect toggle leads to sign-in — measured and captured, never pressed.
    await step('share-modal', () => shareShot(p, S));
  } },
  connect: { url: BASE + '/connect/discord/instagram', wait: 7000, run: async (p, S) => {
    await BOTH(p, S);
    await step('share-modal', () => shareShot(p, S));
  } },
  'solutions-productivity': { url: BASE + '/solutions/productivity', wait: 7000, run: BOTH },
  'solutions-smart-home': { url: BASE + '/solutions/smart-home', wait: 7000, run: BOTH },
  mcp: { url: BASE + '/mcp', wait: 7000, run: BOTH },
  about: { url: BASE + '/about', wait: 7000, run: BOTH },
  careers: { url: BASE + '/careers', wait: 7000, run: BOTH },
  partners: { url: BASE + '/partners', wait: 7000, run: BOTH },
  terms: { url: BASE + '/terms', wait: 6000, run: BOTH },
  notfound: { url: BASE + '/this-page-does-not-exist-capture', wait: 6000, run: async (p, S) => {
    // A made-up route 404s — captured as the product's not-found page (error state).
    await S.view('default'); await S.full();
  } },
};

const mobile = {
  'mobile-home': { url: HOME + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu-open', async () => {
      const burger = p.locator('button.closed, [class*="menu"] button').first();
      if (!(await burger.count())) return;
      await burger.click({ timeout: 5000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('menu-open');
      const x = p.locator('button').filter({ hasText: /close/i }).first();
      if (await x.count()) await x.click({ timeout: 4000 }).catch(() => {});
      else await p.locator('[class*="close"]').first().click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
    });
  } },
  'mobile-explore': { url: BASE + '/explore', wait: 7000, run: BOTH },
  'mobile-plans': { url: BASE + '/plans', wait: 7000, run: BOTH },
  'mobile-service': { url: BASE + '/twitter', wait: 7000, run: BOTH },
  'mobile-applet': { url: BASE + '/applets/A38TqjpD-start-irobot-cleaning-when-you-leave-home', wait: 7000, run: BOTH },
};

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
await patch(ctx);
const mctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mctx);

for (const [name, cfg] of [...Object.entries(desktop), ...Object.entries(mobile)]) {
  if (pageArg.length && !pageArg.includes(name)) continue;
  const isMobile = name.startsWith('mobile-');
  const p = await (isMobile ? mctx : ctx).newPage();
  const shot = async () => {
    await p.goto(cfg.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    const ok = await clearChallenge(p);
    if (!ok) { log(`! ${name}: bot challenge never cleared — skipped (boundary)`); return; }
    await wait(p, cfg.wait || 7000);
    await closePromo(p);
    const S = new Shooter(p, `${name}-light`, isMobile ? 390 : 1440, isMobile ? 844 : 900, isMobile ? 2 : 1, cfg.url);
    await cfg.run(p, S);
    log(`${name}: ${S.count} shot(s)`);
  };
  try { await shot(); } catch (e) { log(`! ${name} failed: ${String(e.message).split('\n')[0]}`); }
  await p.close();
}
await b.close();
log('done ->', RAW);
