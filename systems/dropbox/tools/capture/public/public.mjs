// Captures dropbox.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The public marketing
// surface paints the dig-Theme-vis2023--bright theme on dig-Mode--bright: coconut (warm cream)
// and white sections with dark dwg-theme--graphite bands inside otherwise light pages. The
// dig-Theme-vis2023--dark scope is declared in the token layer but never paints signed out, so
// every shot is `light`. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots
// 1x. A page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py
// stitches back together; an unbounded page truncates at 8 chunks and the log records the
// boundary. Nothing is sent, bought or signed into: the only presses are local UI toggles —
// the Products nav mega-menu, the /plans billing radio and the mobile hamburger menu. The
// privacy consent banner and Google One Tap are hidden, never answered; /login and /register
// are captured as surfaces, never filled or submitted.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, blockConsent, unlockScroll, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// Finds the element that actually scrolls the page: the document normally,
// or the inner wrapper when a scroll hijacker (Lenis content mode, the
// consent scroll-lock) pins the document to viewport height while the
// content scrolls inside a container.
async function findScroller(p) {
  return p.evaluate(() => {
    document.querySelectorAll('[data-m-scroller]').forEach((n) => n.removeAttribute('data-m-scroller'));
    const doc = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
    if (doc > innerHeight * 1.3) return { mode: 'doc', height: doc };
    let best = null;
    for (const el of document.querySelectorAll('body *')) {
      if (el.scrollHeight > (best ? best.scrollHeight : 0)) best = el;
    }
    if (best && best.scrollHeight > innerHeight * 1.3) {
      best.setAttribute('data-m-scroller', '1');
      return { mode: 'inner', height: best.scrollHeight };
    }
    return { mode: 'doc', height: doc };
  });
}

async function scrollBy(p, mode, y) {
  if (mode === 'inner') await p.evaluate((y) => { const el = document.querySelector('[data-m-scroller]'); if (el) el.scrollTop = y; }, y);
  else await p.evaluate((y) => scrollTo(0, y), y);
}

async function lazyScroll(p, mode = 'doc') {
  const { height: h } = await findScroller(p);
  const m = mode === 'inner' ? 'inner' : (await findScroller(p)).mode;
  for (let y = 0; y < h; y += 600) { await scrollBy(p, m, y); await wait(p, 200); }
  await scrollBy(p, m, 0); await wait(p, 900);
}

// Wait until the page has really grown (nav mounted and a scroller taller
// than one screen — the document, or an inner wrapper when a scroll hijacker
// pins the document); one reload if it stays collapsed.
async function pageReady(p, vh, { reload = true } = {}) {
  for (let i = 0; i < 5; i++) {
    const st = await p.evaluate(() => ({
      sh: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
      nav: !!document.querySelector('nav, main'),
    })).catch(() => null);
    if (st && st.nav) {
      if (st.sh > vh * 1.3) return true;
      const sc = await findScroller(p);
      if (sc.mode === 'inner') return true; // content scrolls inside a wrapper
      await unlockScroll(p);
      const grown = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
      if (grown > vh * 1.3) return true;
    }
    if (reload && i === 2) await p.reload({ waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await wait(p, 4000);
  }
  return false;
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    let sc = await findScroller(p);
    if (sc.mode === 'doc' && sc.height <= this.vh * 1.3) { await unlockScroll(p); await wait(p, 800); sc = await findScroller(p); }
    await lazyScroll(p, sc.mode);
    sc = await findScroller(p);
    const H = sc.height;
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Bound at eight chunks — a GPU texture for a document page, a viewport
    // step for an inner scroller.
    const MAXH = 8 * (sc.mode === 'inner' ? this.vh : chunk);
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (sc.mode === 'inner') {
      // The document is pinned to the viewport and the page scrolls inside a
      // wrapper: tile by stepping the wrapper's scrollTop and shooting the
      // viewport each time.
      if (hCap <= this.vh) await screenshotWithMetadata(p, { path: f + '.png', fullPage: false }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += this.vh) {
        await scrollBy(p, 'inner', y);
        await wait(p, 500);
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: false }, this.requested);
      }
    } else if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H, sc.mode === 'inner' ? '(inner scroller)' : '');
    await scrollBy(p, sc.mode, 0); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The Products nav item opens the mega-menu panel on hover (a click toggles
// it closed again). Local UI only, never a link.
async function openMenu(p, S) {
  const t = p.locator('nav.dwg-nav button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  const box = await t.boundingBox();
  if (box) await p.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  else await t.hover({ timeout: 5000 });
  await wait(p, 1400);
  await S.view('menu');
  await p.mouse.move(2, 800);
  await wait(p, 600);
}

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMenu(p, S); });
    await S.full();
  } },
  dropbox: { path: '/dropbox', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  replay: { path: '/replay', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  sign: { path: '/sign', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docsend: { path: '/docsend', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  business: { path: '/business', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  plans: { path: '/plans', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('billing', async () => {
      // The Billed monthly/yearly radio on the plan cards — a local UI toggle,
      // no checkout. The page defaults to yearly, so the state shot clicks
      // Billed monthly.
      const t = p.locator('label').filter({ hasText: /Billed monthly/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1400); await S.view('monthly'); }
    });
    await S.full();
  } },
  features: { path: '/features', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  register: { path: '/register', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 16000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('nav.dwg-nav button[class*="hamburger"], nav.dwg-nav button[aria-label*="menu" i], nav.dwg-nav button[aria-label*="navigation" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  plans: { path: '/plans', wait: 10000, run: async (p, S) => {
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
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  await blockConsent(p);
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
      if (!(await pageReady(p, vh))) log('  ! page never grew past the viewport; capturing what is painted');
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
