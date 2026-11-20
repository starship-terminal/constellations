// Captures acnestudios.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the Menu drawer,
// the SEARCH panel, the PLP FILTER rail, a PDP size swatch and LOAD MORE. The OneTrust cookie
// banner is hidden remove-only (its buttons are never clicked). The geo check serves the
// Singapore store (data-sid=acne_sg, /sg/en/...): the capture is of the served variant.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

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
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The nav's overlay toggles (Menu drawer, SEARCH panel, FILTER rail) are local
// state: they mount a panel over the page, never submit anything.
const openToggle = async (p, label) => {
  const t = p.getByRole('button', { name: label, exact: false }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await clickEl(t); await wait(p, 1400); return true;
};

const desktop = {
  home: { path: '/sg/en/home', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openToggle(p, /^menu$/i)) { await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 800); } });
    await step('search', async () => { if (await openToggle(p, /^search$/i)) { await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 800); } });
    await S.full();
  } },
  woman: { path: '/sg/en/woman/new-arrivals/', run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => { if (await openToggle(p, /^filter/i)) { await S.view('filter'); await p.keyboard.press('Escape'); await wait(p, 800); } });
    await step('load-more', async () => { const b = p.getByRole('button', { name: /load more/i }).filter({ visible: true }).first(); if (await b.count()) { await clickEl(b); await wait(p, 2500); await S.view('load-more'); } });
    await S.full();
  } },
  bags: { path: '/sg/en/bags/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/sg/en/woman/new-arrivals/', run: async (p, S) => {
    // A PDP has no stable URL worth hardcoding: open the first product tile on
    // the category page, the way a visitor reaches it.
    const card = p.locator('a[href*=".html"]').filter({ visible: true }).first();
    await clickEl(card); await wait(p, 5000);
    await S.view('default');
    await step('size', async () => {
      const sw = p.locator('button, [role="button"], li, a').filter({ visible: true, hasText: /^(XS|S|M|L|XL|34|36|38|40|42|44|46|48|50)$/ }).first();
      if (await sw.count()) { await clickEl(sw); await wait(p, 900); await S.view('size-picked'); }
    });
    await S.full();
  } },
  about: { path: '/sg/en/about/about.html', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faq: { path: '/sg/en/help/faq.html', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/sg/en/help/contact-us.html', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  stores: { path: '/sg/en/stores/stores.html', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cart: { path: '/sg/en/cart', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/sg/en/account', run: async (p, S) => {
    // Signed-out /account redirects to the sign-in page: a real public surface.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/sg/en/home', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openToggle(p, /^menu$/i)) { await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 800); } });
    await S.full();
  } },
  woman: { path: '/sg/en/woman/new-arrivals/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { path: '/sg/en/woman/new-arrivals/', run: async (p, S) => {
    const card = p.locator('a[href*=".html"]').filter({ visible: true }).first();
    await clickEl(card); await wait(p, 5000);
    await S.view('default'); await S.full();
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
