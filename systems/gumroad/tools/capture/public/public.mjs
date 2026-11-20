// Captures gumroad.com's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// gumroad.com's signed-out surface: the marketing pages (home, features,
// pricing, about, blog, gumclaw, help, terms), the Discover catalogue (an
// infinite product grid, truncated at eight chunks and logged), a category
// page, the login and signup cards, and a product page plus a creator profile
// on a <creator>.gumroad.com subdomain (ichigo.gumroad.com, the product the
// Discover grid linked at capture time). The dark theme is real — a
// @media (prefers-color-scheme:dark) :root block plus dark:* utilities — so
// dark shots are painted through the colour-scheme emulation, verified by the
// painted surface before each shot (setTheme in lib.mjs). Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than
// one GPU texture is saved as name.partN.png tiles, which quantize.py
// stitches back together. Nothing is sent, bought, subscribed to or signed
// into: the only presses are local UI toggles — the phone's mobile-menu
// button, the featured-products carousel arrow, the product page's
// Monthly/Yearly radio and Share popover. The Subscribe button opens the
// checkout overlay: it is shot as a public form state, never filled and
// never submitted; the login and signup forms are shot, never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, chromium, UA, UA_MOBILE, BASE, PRODUCT_URL, CREATOR_URL } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

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

// gumroad.com scrolls the document itself; on some pages the <main> is an
// overflow-y-auto pane at lg widths. findScroller() picks the pane with the
// most scrollable content when one exists. lazyScroll walks it so lazy
// sections and product cards paint before the shot.
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
    const step = 600;
    for (let y = 0; y < info.h; y += step) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
    await p.evaluate(() => scrollTo(0, 0));
  }
  await wait(p, 900);
}

// For the full shot an inner scroller's ancestors are relaxed to natural
// height so the document becomes as tall as the content — a normal fullPage
// capture then paints every section. restore() puts the shell back.
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
  async view(name, sourceUrl) { await closePromo(this.p); const requested = sourceUrl ? { ...this.requested, sanitizedSourceUrl: sourceUrl } : this.requested; await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, requested); this.count++; log('  shot', name); }
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
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll
    // (the Discover grid keeps loading products); without a ceiling the tile
    // loop writes forever. Truncate hard and record the boundary instead.
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
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Dark shots of a page: repaint through the colour-scheme emulation (the
// product's own theme mechanism — painted checks inside setTheme), shoot,
// switch back. A page that never paints dark takes no shot.
async function darkPass(p, name, vw, vh, dpr, url, shots = ['default']) {
  // The page may have navigated away (e.g. the checkout step); return to the
  // route under test so theme checks and shots cover the right document.
  if (!p.url().startsWith(url)) {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await wait(p, 8000);
  }
  if (!(await setTheme(p, 'dark'))) { log('  ! dark theme never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };
const BOTH_D = (extra) => async (p, S, ctx) => { await S.view('default'); await S.full(); ctx.extra += await darkPass(p, S.prefix.replace(/-light$/, ''), 1440, 900, 1, ctx.url, ['default']); };

const desktop = {
  home: { url: BASE + '/', wait: 10000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'home', 1440, 900, 1, BASE + '/', ['default', 'full']);
  } },
  discover: { url: BASE + '/discover', wait: 15000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('carousel', async () => {
      // The featured-products carousel's own next arrow — a local UI toggle.
      // The pager reads "← 1 / 8 →"; its arrows are unlabeled svg buttons, so
      // the counter's parent tags them for the locator to click.
      const marked = await p.evaluate(() => {
        const counter = [...document.querySelectorAll('div,span')].find((n) => /^\s*\d+\s*\/\s*\d+\s*$/.test((n.innerText || '').trim()));
        if (!counter) return 0;
        const host = counter.closest('div');
        const btns = host ? [...host.parentElement.querySelectorAll('button')].filter((b) => b.getBoundingClientRect().width < 60) : [];
        btns.forEach((b, i) => b.setAttribute('data-carousel-arrow', String(i)));
        return btns.length;
      });
      if (!marked) { log('  ! carousel arrows missing'); return; }
      const t = p.locator('[data-carousel-arrow]').last();
      await clickEl(t); await wait(p, 1200); await S.view('carousel');
    });
    await S.full();
    ctx.extra += await darkPass(p, 'discover', 1440, 900, 1, BASE + '/discover', ['default']);
  } },
  category: { url: BASE + '/design', wait: 14000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'category', 1440, 900, 1, BASE + '/design', ['default']);
  } },
  features: { url: BASE + '/features', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'features', 1440, 900, 1, BASE + '/features', ['default']);
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'pricing', 1440, 900, 1, BASE + '/pricing', ['default']);
  } },
  about: { url: BASE + '/about', wait: 8000, run: BOTH },
  blog: { url: BASE + '/blog', wait: 9000, run: BOTH },
  gumclaw: { url: BASE + '/gumclaw', wait: 8000, run: BOTH },
  help: { url: BASE + '/help', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'help', 1440, 900, 1, BASE + '/help', ['default']);
  } },
  terms: { url: BASE + '/terms', wait: 7000, run: BOTH },
  login: { url: BASE + '/login', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'login', 1440, 900, 1, BASE + '/login', ['default']);
  } },
  signup: { url: BASE + '/signup', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    ctx.extra += await darkPass(p, 'signup', 1440, 900, 1, BASE + '/signup', ['default']);
  } },
  product: { url: PRODUCT_URL, wait: 12000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('yearly', async () => {
      // The billing-term select (Monthly/Yearly) — a local UI toggle on the
      // product's own purchase panel; switched back afterwards.
      const t = p.locator('select').filter({ visible: true }).first();
      const opts = await t.locator('option').allInnerTexts().catch(() => []);
      if (!(await t.count()) || !opts.some((o) => /yearly/i.test(o))) { log('  ! term select missing'); return; }
      await t.selectOption({ label: opts.find((o) => /yearly/i.test(o)).trim() }).catch(() => {});
      await wait(p, 900); await S.view('yearly');
      const m = opts.find((o) => /monthly/i.test(o));
      if (m) await t.selectOption({ label: m.trim() }).catch(() => {});
    });
    await step('share', async () => {
      // The product's Share button opens a popover — a local UI toggle.
      const t = p.locator('button').filter({ hasText: /^\s*Share\s*$/ }).filter({ visible: true }).first();
      if (!(await t.count())) { log('  ! share button missing'); return; }
      await clickEl(t); await wait(p, 1200); await S.view('share'); await p.keyboard.press('Escape'); await wait(p, 500);
    });
    await S.full();
    // Checkout: a boundary, not a step. Pressing Subscribe / I want this puts the product into a checkout
    // session on gumroad.com (a server-side cart), so the capture stops at the button and shoots it at rest.
    // The committed product-light-checkout shot was taken past that step (README, What to distrust).
    ctx.extra += await darkPass(p, 'product', 1440, 900, 1, PRODUCT_URL, ['default']);
  } },
  creator: { url: CREATOR_URL, wait: 12000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'creator', 1440, 900, 1, CREATOR_URL, ['default']);
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The header's mobile-menu button opens the phone's nav panel — a
      // local UI toggle; its links are never followed.
      const ham = p.locator('[data-toggle="mobile-menu"], button[aria-label*="menu" i]').filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! menu button missing'); return; }
      await clickEl(ham); await wait(p, 1500); await S.view('menu');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  discover: { url: BASE + '/discover', wait: 15000, run: BOTH },
  product: { url: PRODUCT_URL, wait: 12000, run: BOTH },
  login: { url: BASE + '/login', wait: 8000, run: BOTH },
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
  const runCtx = { extra: 0, url: spec.url };
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
