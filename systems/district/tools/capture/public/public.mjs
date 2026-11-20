// Captures district.in's public surfaces into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{state}.png; mobile ones get a `mobile-` prefix. Two
// products paint signed out: the marketing site (/, /download, /nitro) and
// the app surfaces (/servers discovery, a /servers/<slug> detail page,
// /login, /register). There is no theme toggle signed out: app surfaces
// paint their dark theme (light exists only as a declared .theme-light
// sheet — a documented boundary). Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent or signed into: auth fields are never filled and no
// submit button is pressed. Promo overlays are hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (the kit's default); quantize.py writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'district', 'raw-shots') + '/';
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    // Some pages scroll inside one fixed-viewport div, not the document:
    // document.scrollHeight reports the viewport height while the inner
    // scroller holds the whole page. Detect the dominant scroller and tile it
    // by scrollTop steps into partN.png; otherwise fall back to the document
    // fullPage path.
    const inner = await p.evaluate(() => {
      const doc = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
      let best = null;
      for (const e of document.querySelectorAll('body *')) {
        const cs = getComputedStyle(e);
        if (!/(auto|scroll)/.test(cs.overflowY)) continue;
        if (e.scrollHeight > Math.max(e.clientHeight + 200, doc + 200) && (!best || e.scrollHeight > best.h))
          best = { sel: null, h: e.scrollHeight, el: e };
      }
      if (!best) return null;
      best.el.setAttribute('data-capture-scroller', '1');
      return { h: best.h };
    });
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (inner) {
      const chunk = this.vh;
      const MAXH = 8 * chunk;
      const hCap = Math.min(inner.h, MAXH);
      if (inner.h > MAXH) log(`  ! ${name}: inner scroller is ${inner.h}px tall, capturing first ${hCap}px only (inner-scroller boundary)`);
      const scroller = p.locator('[data-capture-scroller="1"]').first();
      // wheel-scroll to lazy-load, then re-read the height and tile by scrollTop
      for (let y = 0; y < hCap; y += chunk) { await scroller.evaluate((e, y) => e.scrollTo(0, y), y).catch(() => {}); await wait(p, 200); }
      const H = await scroller.evaluate((e) => e.scrollHeight).catch(() => inner.h);
      const hReal = Math.min(H, MAXH);
      for (let i = 0, y = 0; y < hReal; i++, y += chunk) {
        await scroller.evaluate((e, y) => e.scrollTo(0, y), y);
        await wait(p, 350);
        // scrollTo clamps at the bottom: read the real offset and clip the
        // tile to the unshown remainder so stitching never repeats content.
        const top = await scroller.evaluate((e) => e.scrollTop).catch(() => y);
        const off = y - top;              // where the wanted region starts inside the viewport
        const vis = Math.min(chunk, Math.max(0, hReal - y));
        if (off < 0 || vis <= 0) break;
        try {
          await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, scale: 'css', clip: { x: 0, y: off, width: this.vw, height: vis } }, this.requested);
          // clip.y is viewport-relative; record where the tile sits in the
          // scroller so quantize.py checks coverage, not screenshot offsets.
          const sidecar = JSON.parse(fs.readFileSync(`${f}.part${i}.png.capture.json`, 'utf8'));
          sidecar.capture.scroller = { top, wanted: y, height: hReal };
          fs.writeFileSync(`${f}.part${i}.png.capture.json`, JSON.stringify(sidecar, null, 2) + '\n');
        } catch (e) { log('  ! part' + i, String(e.message).split('\n')[0]); }
      }
      await scroller.evaluate((e) => e.scrollTo(0, 0));
      this.count++; log('  shot', name, 'inner H=' + H);
      await wait(p, 400);
      return;
    }
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The DDS theme layer resolves html[data-theme=light|dark]: dark is real
// paint flipped through the attribute, not a guess.
// The check reads what painted (the body background's luminance), not the
// attribute this function just set, so a failed switch never writes a light
// page as a *-dark-* shot.
const setTheme = async (p, t) => {
  await p.evaluate((t) => document.documentElement.setAttribute('data-theme', t), t);
  await wait(p, 1200);
  const dark = await p.evaluate(() => {
    const [r, g, b, a = 1] = (getComputedStyle(document.body).backgroundColor.match(/[\d.]+/g) || []).map(Number);
    // opaque only: a translucent body shows the page behind it
    return a === 1 && (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255 < 0.25;
  });
  if (dark !== (t === 'dark')) throw new Error('setTheme ' + t + ' did not paint: body background is ' + (dark ? 'dark' : 'light'));
};

const ARTIST = '/events/samay-raina/artist';
const TICKETS = '/events/all-stars-live-apr12-2026-buy-tickets';

const desktop = {
  home: { url: BASE + '/', wait: 9000, shot: 'home', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  homeDark: { url: BASE + '/', wait: 9000, shot: 'home-dark', run: async (p, S) => {
    await setTheme(p, 'dark');
    await S.view('default');
    await S.full();
  } },
  movies: { url: BASE + '/movies/', wait: 8000, shot: 'movies', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  moviesDark: { url: BASE + '/movies/', wait: 8000, shot: 'movies-dark', run: async (p, S) => {
    await setTheme(p, 'dark');
    await S.view('default');
    await S.full();
  } },
  dining: { url: BASE + '/dining/', wait: 8000, shot: 'dining', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  events: { url: BASE + '/events/', wait: 8000, shot: 'events', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  comedy: { url: BASE + '/events/comedy', wait: 8000, shot: 'comedy', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  stores: { url: BASE + '/stores/', wait: 8000, shot: 'stores', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  play: { url: BASE + '/play/', wait: 8000, shot: 'play', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  artist: { url: BASE + ARTIST, wait: 12000, shot: 'artist', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tickets: { url: BASE + TICKETS, wait: 12000, shot: 'tickets', run: async (p, S) => {
    // The ticket page is shot at rest: prices/dates are public, Book is a
    // measured boundary never pressed.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, shot: 'home', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  movies: { url: BASE + '/movies/', wait: 8000, shot: 'movies', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
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
  const S = new Shooter(p, `${mob ? 'mobile-' : ''}${spec.shot}`, vw, vh, dpr, spec.url);
  try {
    // 'commit': the document commits fast while domcontentloaded can hang on
    // the stream; clearChallenge + wait cover readiness.
    await p.goto(spec.url, { waitUntil: 'commit', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
