// Captures cakeequity.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The site paints ONE
// light marketing surface (a Webflow build): home, pricing, feature pages, blog, product tour and
// the demo-request form page. `login` shoots the app sign-in card on authentication.cakeequity.com
// (app.cakeequity.com/login redirects there) — a surface, never filled or submitted. Desktop shots
// are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the Product mega-nav hover, the pricing Yearly/Quarterly
// billing checkbox, the home FAQ accordion and the mobile menu. The Chatbase assistant widget is
// hidden, never answered.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'cakeequity', 'raw-shots');
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

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The Product mega-nav opens on hover (Webflow w-dropdown), never clicked.
      const t = p.locator('.nav-menu-dropdown .w-dropdown-toggle').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await t.hover({ timeout: 8000 }); await wait(p, 1400); await S.view('menu'); }
    });
    await step('faq-open', async () => {
      const f = p.locator('.faq-question-wrap, .faq-item-question').filter({ visible: true }).first();
      if (await f.count()) { await f.scrollIntoViewIfNeeded().catch(() => {}); await clickEl(f); await wait(p, 1200); await S.view('faq-open'); await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('quarterly', async () => {
      // The Yearly/Quarterly billing switch: a local UI toggle, never a
      // checkout. Click the Quarterly option span itself — the label's centre
      // lands on Yearly and toggles back.
      const t = p.locator('.ms-switch-option.monthy, .ms-switch-option:has-text("Quarterly")').filter({ visible: true }).first();
      if (await t.count()) { await t.scrollIntoViewIfNeeded().catch(() => {}); await clickEl(t); await wait(p, 1500); await S.view('quarterly'); await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400); }
    });
    await S.full();
  } },
  feature: { path: '/features/cap-table', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tour: { path: '/product-tour', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  demo: { path: '/demo-request', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: 'https://app.cakeequity.com/login/', wait: 11000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The hamburger sits inside the ~745px layout viewport the page forces at
      // 390 (see README): a Playwright click would pan the visual viewport right
      // to reach it, so dispatch el.click() — the menu opens at layout left, in
      // frame, the same place it opens for a phone user who pans back.
      const m = p.locator('.w-nav-button').filter({ visible: true }).first();
      if (await m.count()) { await m.evaluate((el) => el.click()); await wait(p, 1800); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
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
    const dest = spec.url || BASE + spec.path;
    await p.goto(dest, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', dest); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
