// Captures byborre.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The site paints one
// light surface signed out; the Design Studio (the signed-in tool at /dashboard) redirects to
// /?redirectTo=/dashboard and opens a login dialog, which is itself a public surface. Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded
// page truncates at 8 chunks and the log records the boundary. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the About nav flyout, the cart drawer, a FAQ
// question, a colour filter and a textile view toggle. The cookie consent bar is hidden, never
// answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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

// The About / Collaborations header buttons open flyout panels (hover on
// desktop; a click also opens them). Local UI only.
async function openFlyout(p, S) {
  const t = p.locator('header button').filter({ hasText: /^\s*About\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  await t.hover({ timeout: 5000 }).catch(() => {});
  await wait(p, 900);
  const open = await p.evaluate(() => [...document.querySelectorAll('header a')].some((a) => /Knit Innovation|Responsibility|Creative Control/.test(a.innerText || '') && a.getBoundingClientRect().height > 0));
  if (!open) await clickEl(t).catch(() => {});
  await wait(p, 1200);
  await S.view('menu');
  await p.keyboard.press('Escape');
}

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('flyout', async () => { await openFlyout(p, S); });
    await step('cart', async () => {
      const c = p.locator('header button[aria-label="Cart"]').filter({ visible: true }).first();
      if (await c.count()) { await clickEl(c); await wait(p, 1400); await S.view('cart'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  collection: { path: '/collection', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('filtered', async () => {
      const f = p.locator('input[name="color-select-Blue"], label:has-text("BLUE")').filter({ visible: true }).first();
      if (await f.count()) { await clickEl(f); await wait(p, 1500); await S.view('filtered'); }
    });
    await S.full();
  } },
  textile: { path: '/collection/blink', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('render', async () => {
      // The textile viewer's own PHOTO/RENDER toggle — a local UI state, no
      // submit or navigation.
      const t = p.locator('button').filter({ hasText: /^\s*RENDER\s*$/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1400); await S.view('render'); }
    });
    await S.full();
  } },
  'creative-control': { path: '/creative-control', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'knit-innovation': { path: '/knit-innovation', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  projects: { path: '/projects', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  brands: { path: '/brands', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  designers: { path: '/designers', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'founders-story': { path: '/founders-story', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  responsibility: { path: '/responsibility', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'ways-of-working': { path: '/ways-of-working', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  team: { path: '/team', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faq: { path: '/faq', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('open', async () => {
      const qq = p.locator('button.w-full, button').filter({ hasText: /\?/ }).filter({ visible: true }).first();
      if (await qq.count()) { await clickEl(qq); await wait(p, 1200); await S.view('open'); }
    });
    await S.full();
  } },
  contact: { path: '/contact', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'popup-store': { path: '/popup-store', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/?redirectTo=/dashboard', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
  terms: { path: '/terms-and-conditions', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  privacy: { path: '/privacy-policy', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button[aria-label="Open menu"], header button').filter({ hasText: /menu/i }).filter({ visible: true }).first();
      const alt = p.locator('header button[aria-label="Open menu"]').first();
      const t = (await m.count()) ? m : alt;
      if (await t.count()) { await clickEl(t); await wait(p, 1600); await S.view('menu'); }
    });
    await S.full();
  } },
  collection: { path: '/collection', wait: 9000, run: async (p, S) => {
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
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
