// Captures craft.do's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. craft.do paints a
// single light surface. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing
// is sent, bought or signed into: the only presses are local UI toggles — the pricing billing
// switch and the mobile nav button. There is no auth card on www.craft.do (Log in links out to
// docs.craft.do and is never followed; Try Craft Free leads to /download). No consent banner
// exists; the hiding stays as defence-in-depth. Checkout and every download action are never used.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'craft', 'raw-shots');
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl && String(sourceUrl).split(/[?#]/)[0] /* the sidecar reads it from here */ }; this.sourceUrl = sourceUrl; this.count = 0; }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.sourceUrl }, this.requested);
    this.count++; log('  shot', name);
  }
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
    const opts = (extra) => ({ path: extra, sanitizedSourceUrl: this.sourceUrl });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

async function openHeaderMenu(p, controls) {
  await p.evaluate(() => scrollTo(0, 0));
  await p.keyboard.press('Escape').catch(() => {});
  const btn = p.locator(`header button[aria-controls="${controls}"]`).first();
  if (await btn.count()) await clickEl(btn);
  await wait(p, 700);
}

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => {
      await openHeaderMenu(p, 'header-product-menu');
      await S.view('menu-product');
      await p.keyboard.press('Escape');
    });
    await step('community-menu', async () => {
      await openHeaderMenu(p, 'header-community-menu');
      await S.view('menu-community');
      await p.keyboard.press('Escape');
    });
    await step('language', async () => {
      const lang = p.locator('button').filter({ hasText: /^English$/ }).last();
      if (await lang.count()) {
        await lang.scrollIntoViewIfNeeded();
        await clickEl(lang);
        await wait(p, 700);
        await S.view('language');
        await p.keyboard.press('Escape');
      }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('billing', async () => {
      // The plan billing switch (monthly / annual): a local UI toggle.
      const sw = p.locator('button[role="switch"], button').filter({ hasText: /annual|monthly|yearly/i }).filter({ visible: true }).first();
      if (await sw.count()) { await clickEl(sw); await wait(p, 1500); await S.view('billing'); await clickEl(sw); }
    });
    await S.full();
  } },
  download: { path: '/download', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  imagine: { path: '/imagine', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  learn: { path: '/learn', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  write: { path: '/write', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  plan: { path: '/plan', wait: 7000, run: async (p, S) => { await S.view('default'); } },
  organize: { path: '/organize', wait: 7000, run: async (p, S) => { await S.view('default'); } },
  customize: { path: '/customize', wait: 7000, run: async (p, S) => { await S.view('default'); } },
  pricingfaq: { path: '/pricing', wait: 7000, run: async (p, S) => {
    await step('faq', async () => {
      const row = p.locator('button').filter({ hasText: /\?|what |how |can /i }).filter({ visible: true }).first();
      if (await row.count()) { await row.scrollIntoViewIfNeeded(); await clickEl(row); await wait(p, 600); await S.view('faq'); }
    });
  } },
  login: { url: 'https://docs.craft.do/', wait: 8000, run: async (p, S) => {
    // Empty wall only. Do not type, do not click an identity provider, do not submit.
    await S.view('empty');
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile header's menu button: a local overlay toggle.
      const m = p.locator('header button, nav button').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: 'https://docs.craft.do/', wait: 8000, run: async (p, S) => {
    await S.view('empty');
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
  const target = spec.url || BASE + spec.path;
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, target);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
