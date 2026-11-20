// Captures aesop.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the Search
// disclosure, the Email sign up dialog, the My cart drawer, the burger menu and PDP accordions.
// The OneTrust consent SDK is aborted at request level (its banner never mounts; no consent button
// is ever clicked). The store served is the US site (Sites-aesop-us-Site).
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';
import { loadOnce, pageState } from './gate.mjs';

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
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };
// A bot check is a boundary (gate.mjs): each page is loaded once in its run's
// context, and a page that shows a challenge, an error or no content is
// logged BLOCKED and shot not at all. Nothing reloads it, retries it or opens
// it again in a fresh context. The product page is reached the way a visitor
// reaches it, from the catalogue in the same context, so it is that context's
// second document; Turnstile challenges a second document load, and that is
// recorded as blocked like any other page.
const toProduct = async (p) => {
  const url = await p.evaluate(() => {
    const a = [...document.querySelectorAll('a[href$=".html"]')].find((n) => /\/[A-Z]+\d[A-Z0-9]*\.html/i.test(n.getAttribute('href') || ''));
    return a ? a.href : null;
  }).catch(() => null);
  if (!url) return { ok: false, reason: 'no product tile link found on /shop-all/' };
  log('  ->', url);
  return loadOnce(p, url);
};
const esc = async (p) => { await p.keyboard.press('Escape'); await wait(p, 800); await p.evaluate(() => { for (const n of document.querySelectorAll('.c-sliding-panel.m-opened, [class*="m-opened"]')) n.classList.remove('m-opened', 'm-active'); document.body.classList.remove('m-lock', 'lock'); }).catch(() => {}); };

// The site's overlay toggles (Search disclosure, Email sign up modal, My cart
// drawer, burger menu) are local state: they mount a panel over the page,
// never submit anything.
const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.locator('button.l-header__search-button[data-js-header-search-cta-large], button.l-header__search-button').last();
      if (await b.count()) { await clickEl(b); await wait(p, 1500); await S.view('search'); await esc(p); }
    });
    await step('signup', async () => {
      const b = p.locator('button.c-signup-link').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 2200); await S.view('signup'); await esc(p); }
    });
    await step('cart', async () => {
      const b = p.locator('button.c-minicart-icon__link').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1800); await S.view('cart'); await esc(p); }
    });
    await step('nav-flyout', async () => {
      const nav = p.locator('a.c-navigation__link.m-level-1').filter({ hasText: /skin care/i }).first();
      if (await nav.count()) { await nav.hover(); await wait(p, 1600); await S.view('nav-flyout'); await p.mouse.move(700, 500); await wait(p, 800); }
    });
    await S.full();
  } },
  shopall: { path: '/shop-all/', run: async (p, S) => {
    await S.view('default');
    await step('sort', async () => {
      const b = p.locator('button.c-refinements-toggler').filter({ visible: true }).first()
        .or(p.getByRole('button', { name: /sort|filter|all filters/i }).filter({ visible: true }).first());
      if (await b.count()) { await clickEl(b); await wait(p, 1600); await S.view('sort'); await esc(p); }
    });
    await S.full();
  } },
  skincare: { path: '/skin-care/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/shop-all/', via: toProduct, run: async (p, S) => {
    await killGeo(p);
    await S.view('default');
    // The PDP's information accordion only paints at phone widths
    // (h-hide-for-large); nothing matches here at 1440 and the shot is taken
    // in the mobile run instead — a page-wide "accordion" match used to open
    // the header nav's flyout instead.
    await step('accordion', async () => {
      const acc = p.locator('.c-accordion__title').filter({ visible: true }).first();
      if (await acc.count()) { await clickEl(acc); await wait(p, 1200); await S.view('accordion'); }
    });
    await S.full();
  } },
  stores: { path: '/stores', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { path: '/cart', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show', run: async (p, S) => {
    // The Demandware sign-in pipeline. Cloudflare Turnstile or a styled
    // "unexpected error" page may serve instead of the form; either is
    // logged BLOCKED (gate.mjs) and not shot.
    await S.view('default');
    await S.full();
  } },
  notfound: { path: '/account', run: async (p, S) => {
    // /account 404s — the error page in chrome is the capture.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.locator('button.c-hamburger__button').filter({ visible: true }).first();
      if (await b.count()) { await clickEl(b); await wait(p, 1600); await S.view('menu'); await esc(p); }
    });
    await S.full();
  } },
  shopall: { path: '/shop-all/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { path: '/shop-all/', via: toProduct, run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      const acc = p.locator('.c-accordion__title').filter({ visible: true }).first();
      if (await acc.count()) { await clickEl(acc); await wait(p, 1200); await S.view('accordion'); }
    });
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const blocked = [];
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const target = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
    log('  ->', target);
    let r = await loadOnce(p, target);
    if (r.ok && spec.via) r = await spec.via(p);
    // An error page or a late challenge can replace the document while it
    // settles: watch it for a few seconds, without touching it.
    for (let i = 0; i < 6 && r.ok; i++) {
      await wait(p, 1200);
      if ((await pageState(p)) !== 'ok') r = { ok: false, reason: 'page turned into a challenge or an error after loading' };
    }
    if (!r.ok) { log('  BLOCKED', name, r.reason); blocked.push(`${name} (${r.reason})`); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
if (blocked.length) log('blocked, not shot:', blocked.join('; '));
await b.close();
