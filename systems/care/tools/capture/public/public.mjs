// Captures care.com's public signed-out pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The whole signed-out
// surface paints one light theme; there is no dark mode to find. Desktop shots are 1440x900 at
// 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary.
//
// DataDome gates the edge: a flagged client gets a "Challenge Validation" reCAPTCHA page, so
// this runner keeps ONE context per viewport (the clearance cookie persists across routes) and
// paces navigations (PACE env, default 20 s). A route that stays challenged is logged BLOCKED
// and skipped, never retried into a harder block. Nothing is sent, bought or signed into: the
// only presses are local UI toggles — the header "Find care" dropdown, the mobile menu and a
// listing FAQ question. The cookie banner and the "Join Care.com" signup-gate modal are hidden,
// never answered.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'care', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const PACE = +(process.env.PACE || 20000); // ms between routes; DataDome rate-limits

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
    // Scrolling mounts the "Join Care.com" signup-gate modal on the listing
    // pages: hide it again (never answered) before the tiles are shot, or it
    // would paint over every tile at its fixed position.
    await closePromo(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      const tiles = [];
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        const tile = `${f}.part${i}.png`;
        await screenshotWithMetadata(p, { path: tile, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
        tiles.push(path.basename(tile));
      }
      // quantize.py only stitches a set marked complete: a run that dies
      // mid-tiling leaves earlier tiles behind, and this manifest is written
      // after the last one lands.
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ tiles }));
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const t = p.locator('header button').filter({ hasText: /^Find care/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  'child-care': { path: '/child-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'senior-care': { path: '/senior-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'pet-care': { path: '/pet-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  housekeeping: { path: '/housekeeping', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tutoring: { path: '/tutoring', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  babysitters: { path: '/babysitters', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      await p.evaluate(() => scrollTo(0, document.documentElement.scrollHeight * 0.8));
      await wait(p, 1500);
      const t = p.locator('.MuiAccordion-root button, .MuiAccordionSummary-root, button').filter({ hasText: /\?/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('faq'); }
    });
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 800);
    await S.full();
  } },
  safety: { path: '/about/safety/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  resources: { path: '/c/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/app/vhp/plans-and-pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/vis/auth/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  join: { path: '/app/vhp/get-started', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  rates: { path: '/caregiver-rates', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { path: '/about/terms-of-use', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button, header [role="button"], header [class*="burger" i], header [class*="Hamburger" i], header [class*="MenuButton" i]').filter({ visible: true }).last();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); }
    });
    await S.full();
  } },
  'child-care': { path: '/child-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'senior-care': { path: '/senior-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'pet-care': { path: '/pet-care', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  housekeeping: { path: '/housekeeping', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tutoring: { path: '/tutoring', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  babysitters: { path: '/babysitters', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  safety: { path: '/about/safety/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/app/vhp/plans-and-pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/vis/auth/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  join: { path: '/app/vhp/get-started', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
let p = null, ctx = null, curMob = null;
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  if (!p || curMob !== mob) {
    if (ctx) await ctx.close();
    ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    await patch(ctx);
    p = await ctx.newPage();
    curMob = mob;
  }
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await wait(p, PACE); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await wait(p, PACE); // pace the next navigation
}
log('done', total, 'screenshots ->', RAW);
if (ctx) await ctx.close();
await b.close();
