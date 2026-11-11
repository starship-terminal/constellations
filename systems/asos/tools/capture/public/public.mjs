// Captures asos.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
//
// Akamai 403s headless Chromium and headless Chrome, so every page opens in HEADED Chrome
// (channel 'chrome', headless false — see lib.mjs). Nothing is bought, sent or signed into: the
// only presses are local UI toggles — the mobile menu and a PDP colour/size select where the DOM
// offers one. The OneTrust consent SDK is hidden, never answered (no Accept/Reject/Save is ever
// clicked); the consent view is captured before it is hidden.
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

// Hover the first category nav item: "New in" opens the category flyout if the
// site has one; the shot is skipped when nothing opens.
const openMega = async (p) => {
  const m = p.locator('nav a, header nav a, [class*="nav" i] a').filter({ hasText: /new in|clothing|dresses/i }).filter({ visible: true }).first();
  if (await m.count()) { await m.hover(); await wait(p, 1600); return true; }
  return false;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.raw('consent');                       // the page as it arrives, consent layer included
    await S.view('default');
    await step('megamenu', async () => { if (await openMega(p)) await S.view('megamenu'); await p.mouse.move(20, 400); await wait(p, 600); });
    await S.full();
  } },
  women: { path: '/women/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  men: { path: '/men/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'shop-women': { path: '/women/new-in/new-in-clothing/cat/?cid=2623', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'shop-men': { path: '/men/new-in/new-in-clothing/cat/?cid=27110', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/women/new-in/new-in-clothing/cat/?cid=2623', wait: 9000, run: async (p, S) => {
    // The PDP URL is discovered at run time: first product on the shop grid.
    const href = await p.evaluate(() => {
      const a = [...document.querySelectorAll('a[href*="/prd/"]')].find((x) => x.offsetParent && (x.innerText || '').trim().length > 3);
      return a ? a.getAttribute('href') : null;
    });
    if (!href) { log('  no product link found'); return; }
    await p.goto(href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 9000);
    await S.view('default');
    await step('size-picked', async () => {
      const sel = p.locator('select').filter({ visible: true }).first();
      if (await sel.count()) { await sel.selectOption({ index: 1 }).catch(() => {}); await wait(p, 700); await S.view('size-picked'); }
    });
    await S.full();
  } },
  bag: { path: '/bag', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'saved-lists': { path: '/saved-lists/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  account: { url: 'https://my.asos.com/my-account', wait: 9000, run: async (p, S) => {
    // my.asos.com/my-account lands signed-out visitors on the identity gate
    // ("Hi friend!" — email, CONTINUE, social buttons). Never submitted.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    // The full-page shot comes first: once the side-panel menu is open it
    // covers the home view, and full() hides consent/promo layers only.
    await S.full();
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], button[aria-label*="navigation" i], .hamburger, [class*="hamburger" i], header button:has(svg), [class*="burger" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); }
    });
  } },
  'shop-women': { path: '/women/new-in/new-in-clothing/cat/?cid=2623', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch({ channel: 'chrome', headless: false });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-GB' });
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
