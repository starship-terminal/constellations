// Captures chargetrip.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The marketing site
// paints one light theme (warm #efede5 page, white cards, dark hero/pricing bands). Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, booked or signed into: the only presses are local UI toggles — the header
// "Products" menu trigger, the mobile menu, and the sign-in page's own Light/Dark theme switch.
// The "Cookie Settings" card is hidden, never answered; every Book-a-demo / Plan-a-route /
// Contact-sales / Sign-in / Create-account / Send action is never followed.
// signin, developers and playground are different origins on the same public surface:
// account.chargetrip.io's sign-in card and the credential-gated API playground are documented
// boundaries — the pages are captured, never filled or submitted.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'chargetrip', 'raw-shots');
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
      for (const [tmp] of staged) {
        fs.existsSync(tmp) && fs.unlinkSync(tmp);
        fs.existsSync(tmp + '.capture.json') && fs.unlinkSync(tmp + '.capture.json');
      }
      throw e;
    }
    // Swap the staged files in first: a `.new.png` tile is not a stale tile,
    // and the previous capture stays intact until its replacement is fully
    // renamed. The .capture.json sidecar moves with its PNG and records the
    // final screenshot name.
    const keep = new Set();
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      keep.add(path.basename(final));
      const sideTmp = tmp + '.capture.json', sideFinal = final + '.capture.json';
      if (fs.existsSync(sideTmp)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sideTmp, 'utf8'));
          meta.screenshot = path.basename(final);
          fs.writeFileSync(sideTmp, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* keep the sidecar as written */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    // Only now drop leftovers the new shot does not produce: higher part
    // numbers of a previous taller capture (and their sidecars), or the old
    // single-file shot.
    const isStaged = (n) => n.endsWith('.new.png') || n.endsWith('.new.png.capture.json');
    for (const old of fs.readdirSync(RAW).filter((n) =>
      !isStaged(n) && !keep.has(n) &&
      (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Clicks the header "Products" trigger to open the mega menu. The trigger is a
// Framer component container whose text is exactly "Products", inside the
// 64px top bar — a local nav toggle, never a link.
const openProductsMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const el = [...document.querySelectorAll('[class*="-container"]')].find((n) => (n.innerText || '').trim() === 'Products' && n.getBoundingClientRect().y < 64 && n.getBoundingClientRect().y >= 0);
    if (!el) return false;
    el.setAttribute('data-m-nav', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-nav="1"]'));
  await wait(p, 1600);
  return true;
};

// The account app's own Light/Dark/System select did not respond to synthetic
// pointer or keyboard input during capture (Reka select; the menu opens but
// the option never applies), so the sign-in page is captured light-only.

// The mobile header's menu trigger: the icon-only control at the bar's right
// edge — Framer renders it as `div[data-framer-name="Button Icon"]`
// (40x40 at ~x330, cursor:pointer, no text).
const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const el = [...document.querySelectorAll('[data-framer-name="Button Icon"]')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.y >= 0 && r.y < 90 && r.width >= 24 && r.width <= 72 && getComputedStyle(n).cursor === 'pointer';
    });
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-menu="1"]'));
  await wait(p, 1600);
  return true;
};

const desktop = {
  home: { url: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openProductsMenu(p)) { await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  routing: { url: '/products/routing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  api: { url: '/api', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  nocode: { url: '/no-code', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cpo: { url: '/cpo', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'pricing-api': { url: '/pricing/api', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'pricing-nocode': { url: '/pricing/nocode', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: '/about', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  newsroom: { url: '/newsroom', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: '/contact', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  sales: { url: '/contact/sales', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: '/legal/terms-and-conditions', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  signin: { url: 'https://account.chargetrip.io/sign-in', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  developers: { url: 'https://developers.chargetrip.com/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  playground: { url: 'https://playground.chargetrip.com/', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) { await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  'pricing-api': { url: '/pricing/api', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
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
    const u = /^https?:/.test(spec.url) ? spec.url : BASE + spec.url;
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
