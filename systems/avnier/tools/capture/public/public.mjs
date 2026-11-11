// Captures avnier.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary.
//
// avnier.com serves headless Chrome a 200 (see lib.mjs). Nothing is bought, sent or signed into:
// the only presses are local UI toggles — the SHOP mega-menu hover, the mobile drawer and a PDP
// variant radio where the DOM offers one. The Axeptio consent SDK and the shipping-country popup
// are hidden, never answered (no Accept/Reject is ever clicked); the consent view is captured
// before it is hidden.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// Scrolls far enough to trigger lazy loading, but never past maxY: on an
// unbounded page the scroll target is the tile cap, not the reported height.
async function lazyScroll(p, maxY = Infinity) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, maxY); y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the page as it arrives, consent layer included if it shows.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const chunk = Math.floor(14000 / this.dpr);
    // Infinite-scroll pages grow scrollHeight without bound while lazyScroll
    // walks them; the tile ceiling is applied to the scroll itself, so a page
    // reporting millions of pixels cannot tie up the run before the cap.
    const MAXH = 8 * chunk;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    await lazyScroll(p, Math.min(H0, MAXH));
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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

// Hover the SHOP mega-menu item: the Dawn theme opens its dropdown on hover;
// the shot is skipped when nothing opens.
const openMega = async (p) => {
  const m = p.locator('header .mega-menu__list > .mega-menu__item, header li').filter({ hasText: /^SHOP\b/i }).filter({ visible: true }).first();
  if (await m.count()) { await m.hover(); await wait(p, 1800); return true; }
  return false;
};

const desktop = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.raw('consent');                       // the page as it arrives, consent layer included
    await S.view('default');
    await step('megamenu', async () => { if (await openMega(p)) await S.view('megamenu'); await p.mouse.move(20, 400); await wait(p, 600); });
    await S.full();
  } },
  shop: { path: '/collections/tous-les-produits', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/collections/tous-les-produits', wait: 8000, run: async (p, S) => {
    // The PDP URL is discovered at run time: first product on the shop grid.
    const href = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href*="/products/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
      return a ? a.getAttribute('href') : null;
    });
    if (!href) { log('  no product link found'); return; }
    await p.goto(/^https?:/.test(href) ? href : BASE + href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 8000);
    await S.view('default');
    await step('variant-picked', async () => {
      const r = p.locator('fieldset input[type="radio"], variant-radios input[type="radio"]').filter({ visible: true }).nth(1);
      if (await r.count()) { await r.check().catch(() => r.evaluate((el) => el.click())); await wait(p, 700); await S.view('variant-picked'); }
    });
    await S.full();
  } },
  cart: { path: '/cart', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/account/login', wait: 8000, run: async (p, S) => {
    // The customer login form: email + password + CONNEXION. Never submitted.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    // The full-page shot comes first: once the drawer is open it covers the
    // home view, and full() hides consent/popup layers only.
    await S.full();
    await step('menu', async () => {
      const m = p.locator('header details summary, header-drawer summary, .header__icon--menu, [class*="drawer" i] summary').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); }
    });
  } },
  'shop': { path: '/collections/tous-les-produits', wait: 8000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch({ channel: 'chrome', headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'fr-FR' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url || BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
