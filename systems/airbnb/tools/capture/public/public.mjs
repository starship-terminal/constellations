// Captures Airbnb's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   [RAW=<dir, default ~/.design-systems/airbnb/raw-shots>] PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// One surface, all of it signed out:
//   airbnb.com   / home, /experiences, /services, /s/Tokyo--Japan/homes, the
//                first /rooms/<id> the results list, /help, /host/homes
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The
// site paints one light theme (no dark surface exists publicly), so there is
// no dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x,
// `-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together. The app
// pages' bodies are position:fixed — the document still scrolls on <html>, so
// lazyScroll drives it with window scrolls. Nothing is sent, created or signed
// into: the coachmark modals ("all fees included", "Translation on") are
// hidden by sweepOverlays, never clicked, and the search box's Where segment
// is opened once for the expanded-panel shot (a local UI toggle, no submit).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { sweepOverlays, chromium, UA, UA_MOBILE, BASE, firstRoomHref, assertProductPage } from './lib.mjs';

// Full-colour shots of the pages stay outside the repository until quantize.py has made screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'airbnb', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const blocked = {};

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (H <= this.vh + 100) { log('  skip full (page is one viewport tall)'); return; }
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // drop this shot's earlier tiles (and sidecars) first: a shorter or capped page would
    // otherwise leave old partN files that quantize.py stitches into the new shot
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // An infinite or growing page reports a scrollHeight without end: tile at most 8 chunks
    // and log the boundary (the kit's cap), never one tile per chunk for ever.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
  // A screenshot of whatever coachmark modal is up, before it is swept away.
  async modal() {
    const has = await this.p.evaluate(() => [...document.querySelectorAll('[role=dialog], [role=alertdialog], [aria-modal="true"]')].some((e) => e.getBoundingClientRect().width > 8));
    if (has) { await this.view('modal'); return true; }
    return false;
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { url: BASE + '/', sweep: 'keep', run: async (p, S) => {
    await S.modal();
    await sweepOverlays(p);
    await S.view('default');
    await step('search-open', async () => {
      // The Where segment is a pointer-cursor div; a getByText click times out
      // on the hidden duplicate copy airbnb keeps in the tree.
      const ok = await p.evaluate(() => {
        const el = [...document.querySelectorAll('body *')].find((e) => (e.innerText || '').trim() === 'Where' && getComputedStyle(e).cursor === 'pointer' && e.getBoundingClientRect().width > 100);
        if (el) { el.click(); return true; }
        return false;
      });
      if (!ok) throw new Error('no Where segment');
      await wait(p, 1600);
      await S.view('search-open');
      await p.keyboard.press('Escape').catch(() => {});
      await p.mouse.click(720, 800);
      await wait(p, 600);
    });
    await step('card-hover', async () => {
      await p.evaluate(() => {
        const a = [...document.querySelectorAll('a[href*="/rooms/"]')].find((x) => { const r = x.getBoundingClientRect(); return r.width > 150 && r.top > 100 && r.top < 800; });
        if (a) a.setAttribute('data-m-card', '1');
      });
      const card = p.locator('[data-m-card="1"]');
      await card.hover({ timeout: 8000 });
      await wait(p, 1200);
      await S.view('card-hover');
    });
    await S.full();
  } },
  experiences: { url: BASE + '/experiences', run: async (p, S) => { await S.modal().then((m) => m && sweepOverlays(p)); await S.view('default'); await S.full(); } },
  services: { url: BASE + '/services', run: async (p, S) => { await S.modal().then((m) => m && sweepOverlays(p)); await S.view('default'); await S.full(); } },
  search: { url: BASE + '/s/Tokyo--Japan/homes', sweep: 'keep', run: async (p, S) => {
    await S.modal();
    await sweepOverlays(p);
    await S.view('default');
    await S.full();
  } },
  room: { url: BASE + '/s/Tokyo--Japan/homes', sweep: 'keep', run: async (p, S) => {
    const href = await firstRoomHref(p);
    if (!href) throw new Error('no /rooms/ link on the results page');
    log('  room', href);
    await p.goto(BASE + href, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, 9000);
    await assertProductPage(p);
    await S.modal();
    await sweepOverlays(p);
    await S.view('default');
    await S.full();
  } },
  help: { url: BASE + '/help', run: async (p, S) => { await S.view('default'); await S.full(); } },
  host: { url: BASE + '/host/homes', run: async (p, S) => { await S.modal().then((m) => m && sweepOverlays(p)); await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { url: BASE + '/', sweep: 'keep', run: async (p, S) => { await S.modal(); await sweepOverlays(p); await S.view('default'); await S.full(); } },
  search: { url: BASE + '/s/Tokyo--Japan/homes', sweep: 'keep', run: async (p, S) => { await S.modal(); await sweepOverlays(p); await S.view('default'); await S.full(); } },
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
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 9000);
    await assertProductPage(p);
    if (spec.sweep !== 'keep') await sweepOverlays(p);
    await spec.run(p, S);
  } catch (e) { blocked[name] = e.message.split('\n')[0]; log('  PAGE FAILED', name, blocked[name]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
if (Object.keys(blocked).length) log('blocked:', JSON.stringify(blocked));
await b.close();
