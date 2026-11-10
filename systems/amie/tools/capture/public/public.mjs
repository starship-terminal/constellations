// Captures amie.so's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, downloaded or signed into: the only presses are local UI toggles — the Features
// nav flyout, the pricing billing toggle and FAQ accordions, and the mobile menu. No consent
// overlay mounts on these routes.
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
      for (const [tmp] of staged) fs.existsSync(tmp) && fs.unlinkSync(tmp);
      throw e;
    }
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png`)) fs.unlinkSync(`${RAW}/${old}`);
    for (const [tmp, final] of staged) fs.renameSync(tmp, final);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The Features flyout is a local Radix popover under the nav.
const openFlyout = async (p) => {
  const m = p.locator('header button, nav button').filter({ hasText: /features/i }).filter({ visible: true }).first();
  if (await m.count()) { await clickEl(m); await wait(p, 1200); return true; }
  return false;
};

// "Bill yearly" flips the pricing toggle in place.
const flipBilling = async (p) => {
  const b = p.locator('button').filter({ hasText: /bill yearly/i }).filter({ visible: true }).first();
  if (await b.count()) { await clickEl(b); await wait(p, 1000); return true; }
  return false;
};

// A pricing FAQ expands a Radix accordion in place.
const openAccordion = async (p) => {
  const a = p.locator('button[data-state="closed"], button[aria-expanded="false"], details:not([open]) summary').filter({ visible: true }).last();
  if (await a.count()) { await a.scrollIntoViewIfNeeded(); await clickEl(a); await wait(p, 900); return true; }
  return false;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('features', async () => { if (await openFlyout(p)) await S.view('features'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('yearly', async () => { if (await flipBilling(p)) await S.view('yearly'); });
    await step('faq', async () => { if (await openAccordion(p)) await S.view('faq'); });
    await S.full();
  } },
  changelog: { path: '/changelog', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  stories: { path: '/stories', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  calendar: { path: '/calendar', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { path: '/tools', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  templates: { path: '/templates', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { path: '/download', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/contact', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], [class*="hamburger" i], header button:has(svg), nav button:has(svg)').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
