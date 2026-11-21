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
import { M, closePromo, killGeo, clearChallenge, chromium, patch, launchOptions, UA, UA_MOBILE, BASE } from './lib.mjs';

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
// Cloudflare lets each browser context load exactly one document before it
// starts issuing Turnstile challenges, so a PDP is reached as a first load in
// its own context: the product URL (…/<SKU>.html) is resolved on the
// catalogue page in a throwaway context, then handed to the page run as its
// path. Turnstile does not auto-solve in headless; a still-blocked route is
// an honest boundary.
const resolvePdp = async (browser, mobile) => {
  const ctx = await browser.newContext({ viewport: { width: mobile ? 390 : 1440, height: mobile ? 844 : 900 }, userAgent: mobile ? UA_MOBILE : UA, isMobile: mobile, hasTouch: mobile, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  let url = null;
  try {
    await p.goto(BASE + '/shop-all/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p, { tries: 6, step: 2000 });
    url = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href$=".html"]')].find((n) => /\/[A-Z]+\d[A-Z0-9]*\.html/i.test(n.getAttribute('href') || ''));
      return a ? a.href : null;
    });
  } finally { await ctx.close(); }
  return url || BASE + '/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html';
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
  pdp: { resolve: (b) => resolvePdp(b, false), run: async (p, S) => {
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
    // "unexpected error" page may serve instead of the form; whichever serves
    // is the honest record.
    await S.view('default');
    await S.full();
  } },
  notfound: { path: '/account', run: async (p, S) => {
    // /account 404s — the error page in chrome is the capture.
    await S.view('default');
    await S.full();
  } },
  login404: { path: '/account/login', run: async (p, S) => {
    // Probe note: this URL 404s. Record the styled error page and stop.
    await S.view('default');
    await S.full();
  } },
  gifts: { path: '/gifts.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  library: { path: '/library.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  experience: { path: '/experience.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  story: { path: '/our-story.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/customer-service/contact-us.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  finder: { path: '/gift-finder/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gathering: { path: '/the-aesop-gift-gathering/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  sitemap: { path: '/customer-service/customer-service-sitemap.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  skincare: { path: '/skin-care.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gifts: { path: '/gifts.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  stores: { path: '/stores', run: async (p, S) => { await S.view('default'); await S.full(); } },
  cart: { path: '/cart', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/customer-service/contact-us.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  library: { path: '/library.html', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { resolve: (b) => resolvePdp(b, true), run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      const acc = p.locator('.c-accordion__title').filter({ visible: true }).first();
      if (await acc.count()) { await clickEl(acc); await wait(p, 1200); await S.view('accordion'); }
    });
    await S.full();
  } },
};

const b = await chromium.launch(launchOptions());
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const path = spec.resolve ? await spec.resolve(b) : spec.path;
    const target = path && path.startsWith('http') ? path : BASE + path;
    log('  ->', target);
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      let clean = true;
      for (let i = 0; i < 6; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$|page cannot be found/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED challenge-or-error', spec.path); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
