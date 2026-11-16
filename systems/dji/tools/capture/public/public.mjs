// Captures dji.com's public surfaces into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{state}.png; mobile ones get a `mobile-` prefix. One
// product paints signed out: the geo-locale brand site (/sg — the Singapore
// English site this client is routed to): mega-nav, home hero, category
// pages (/camera-drones, /handheld), product pages (/mavic-4-pro), /support,
// /company and /where-to-buy/*. The site is light-only — no data-theme
// attribute or dark sheet ships in the public bundles, and the dark hero
// sections are baked art, not a theme. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the
// boundary. Nothing is sent or signed into: auth fields are never filled
// and no Buy/Subscribe button is pressed. Promo overlays are hidden, never
// answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
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


const desktop = {
  home: { url: BASE, wait: 10000, shot: 'home', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  drones: { url: BASE + '/camera-drones', wait: 9000, shot: 'drones', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  handheld: { url: BASE + '/handheld', wait: 9000, shot: 'handheld', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { url: BASE + '/mavic-4-pro', wait: 12000, shot: 'product', run: async (p, S) => {
    // The product page is shot at rest: specs and CTAs are public, Buy Now
    // leads to the gated store — a measured boundary never pressed.
    await S.view('default');
    await S.full();
  } },
  support: { url: BASE + '/support', wait: 9000, shot: 'support', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  company: { url: BASE + '/company', wait: 9000, shot: 'company', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  stores: { url: BASE + '/where-to-buy/online-stores', wait: 9000, shot: 'stores', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE, wait: 10000, shot: 'home', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  product: { url: BASE + '/mavic-4-pro', wait: 12000, shot: 'product', run: async (p, S) => {
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
