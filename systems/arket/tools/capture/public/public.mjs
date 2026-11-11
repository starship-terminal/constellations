// Captures arket.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// arket.com runs behind Akamai, which serves "Access Denied" to headless Chromium and to every
// /en-ww/product/<slug>-<id>/ URL (document and RSC fetch alike): all shots run in headed real
// Chrome (channel 'chrome'), and product pages are a documented boundary. Nothing is bought, sent
// or signed into: the only presses are local UI toggles — the mobile menu, the header search and
// cart drawers, the PLP filter panel and a PDP-less colour swatch. The cookie-consent popup and
// the "Please confirm your location" dialog are captured once as they arrive (home-light-consent,
// home-light-location), then hidden before every shot — never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LAUNCH_OPTS } from './lib.mjs';

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
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the consent card and the location dialog still up, as the page arrives.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    // Stage every tile under a .new name and swap it in only after the whole
    // shot succeeds, so a failed tile never truncates the previous capture.
    const staged = [];
    try {
      if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) { for (const f of [tmp, tmp + '.capture.json']) fs.existsSync(f) && fs.unlinkSync(f); }
      throw e;
    }
    // `.new.png` staging names also start with `${prefix}-${name}.part`, so the
    // stale-tile sweep must skip them or it deletes the files about to be renamed.
    const stale = (n) => !n.includes('.new') && (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`);
    for (const old of fs.readdirSync(RAW).filter(stale)) fs.unlinkSync(`${RAW}/${old}`);
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      // The sidecar follows the image: rename it and point its `screenshot`
      // name at the final file, or a finished capture has no matching record.
      const sidecar = tmp + '.capture.json';
      if (fs.existsSync(sidecar)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sidecar, 'utf8'));
          if (meta.screenshot) meta.screenshot = final.split('/').pop();
          fs.writeFileSync(sidecar, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* leave the record as-is rather than lose it */ }
        fs.renameSync(sidecar, final + '.capture.json');
      }
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// A UI toggle is opened by its own control. The consent and location dialogs
// are never answered; a control whose text names an action the kit never
// takes is refused outright.
const NEVER = /^(accept all|only required cookies|continue to|stay in|send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order)$/i;
async function toggle(p, loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await clickEl(l);
}

// The header "menu" button opens the nav drawer (a <dialog>).
const openMenu = async (p) => {
  const m = p.locator('button').filter({ hasText: /^menu$/ }).filter({ visible: true }).first()
    .or(p.locator('button[aria-label*="menu" i], button[aria-label*="nav" i]').filter({ visible: true }).first());
  if (await m.count()) { await clickEl(m); await wait(p, 1500); return true; }
  return false;
};

// The header Search pill opens the search dialog.
const openSearch = async (p) => {
  const s = p.locator('button, a').filter({ hasText: /^Search$/ }).filter({ visible: true }).first();
  if (await s.count()) { await clickEl(s); await wait(p, 1600); return true; }
  return false;
};

// The header Cart button opens the (empty) bag drawer.
const openCart = async (p) => {
  const c = p.locator('button, a').filter({ hasText: /^Cart$/ }).filter({ visible: true }).first();
  if (await c.count()) { await clickEl(c); await wait(p, 1500); return true; }
  return false;
};

// The PLP "Filter" button opens the filter panel.
const openFilter = async (p) => {
  const f = p.locator('button').filter({ hasText: /^Filter$/ }).filter({ visible: true }).first();
  if (await f.count()) { await f.scrollIntoViewIfNeeded(); await clickEl(f); await wait(p, 1500); return true; }
  return false;
};

const desktop = {
  home: { path: '/en-ww/', wait: 9000, run: async (p, S) => {
    await S.raw('consent');                       // the cookie card + location dialog, as the page arrives
    await S.raw('location');
    await S.view('default');
    await step('search', async () => { if (await openSearch(p)) await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 600); });
    await step('cart', async () => { if (await openCart(p)) await S.view('cart'); await p.keyboard.press('Escape'); await wait(p, 600); });
    await S.full();
  } },
  women: { path: '/en-ww/women/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'new-arrivals': { path: '/en-ww/women/new-arrivals/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  clothing: { path: '/en-ww/women/clothing/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => { if (await openFilter(p)) await S.view('filter'); await p.keyboard.press('Escape'); await wait(p, 600); });
    await S.full();
  } },
  'men-clothing': { path: '/en-ww/men/clothing/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'gift-shop': { path: '/en-ww/gift-shop/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  editorial: { path: '/en-ww/editorial/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'customer-service': { path: '/en-ww/customer-service/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  account: { path: '/en-ww/account/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'previous-collections': { path: '/en-ww/previous-collections/women/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  // /en-ww/ is Akamai-blocked for this client; the women landing carries the
  // same header and menu.
  home: { path: '/en-ww/women/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openMenu(p)) await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 600); });
    await S.full();
  } },
  clothing: { path: '/en-ww/women/clothing/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch(LAUNCH_OPTS);
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
    // Akamai answers some first hits on a fresh context with 403; a reload
    // after a wait clears most of them (see lib.mjs open()).
    let ok = false;
    for (let a = 0; a < 3 && !ok; a++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      ok = await clearChallenge(p);
      if (!ok) await wait(p, 5000);
    }
    if (!ok) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
