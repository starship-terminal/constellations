// Captures visual.app's (formerly designstripe) public pages into RAW
// (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. visual.app paints a
// single light theme signed out: the marketing home, the public /assets
// library, /tools, /about, /contact and /blog articles. Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than
// one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log records
// the boundary. Nothing is sent or signed into: no forms exist on the
// captured routes and no toggles are pressed. No consent overlay was seen.
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
        try { await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, scale: 'css', clip: { x: 0, y: off, width: this.vw, height: vis } }, this.requested); }
        catch (e) { log('  ! part' + i, String(e.message).split('\n')[0]); }
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
    // scale css keeps a 2x phone capture at 1x and the stitch no longer
    // matches the viewport shot. Device scale keeps both at the same pixels.
    const opts = (extra) => ({ path: extra });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    // The waitlist CTAs are buttons that do not open a public form dialog on
    // this surface; the page is captured at rest.
    await S.view('default');
    await S.full();
  } },
  assets: { url: BASE + '/assets', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  avatars: { url: BASE + '/assets/avatars/replicants', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { url: BASE + '/tools', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 8000, theme: 'light', run: async (p, S) => {
    // The contact form is measured and shot at rest; it is never filled or
    // submitted.
    await S.view('default');
    await S.full();
  } },
  post: { url: BASE + '/blog/branding-consistency', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tool: { url: BASE + '/colors/color-wheel', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // /privacy is a footer link that returns the site 404 chrome. Recorded in
  // site-tree.md. Not a design surface, so it is not photographed.
  // The waitlist dialog is the only signup wall on the public site. Open it,
  // photograph what it asks for, and stop. Nothing is typed or submitted.
  waitlist: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    const btn = p.getByRole('button', { name: /^waitlist$/i }).first();
    await btn.click({ timeout: 8000 });
    await p.getByRole('dialog').waitFor({ timeout: 8000 });
    await wait(p, 600);
    await S.view('dialog');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  assets: { url: BASE + '/assets', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  nav: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    const toggle = p.locator('header button, nav button').first();
    await toggle.click({ timeout: 6000 });
    await wait(p, 500);
    await S.view('open');
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
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
