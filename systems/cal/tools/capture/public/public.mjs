// Captures cal.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The site paints TWO
// surfaces signed out: the light marketing pages (home/pricing/features/teams/enterprise/customers/
// blog/faq) plus the auth cards on app.cal.com, and the public booking page that cal.com/peer serves
// from i.cal.com — the booker paints light by default and dark under its supported ?theme=dark&embed
// mode. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is sent,
// booked or signed into: the only presses are local UI toggles — the Products nav dropdown, the
// pricing plan tabs and yearly switch, another calendar day on the booker, and a time slot, which
// opens the guest details form (captured, never filled or confirmed). No consent banner ever
// painted for this client.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, AUTH, BOOKER, BOOKER_DARK } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'cal', 'raw-shots');
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
  home: { path: BASE + '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const t = p.locator('nav button').filter({ hasText: /^Products$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: BASE + '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('teams', async () => {
      const t = p.locator('button').filter({ hasText: /^Teams$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('teams'); }
    });
    await step('monthly', async () => {
      // The YEARLY switch: toggling it is a local UI state, never a purchase.
      const t = p.locator('button[role="switch"], [role="switch"]').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('monthly'); }
    });
    await S.full();
  } },
  feature: { path: BASE + '/features/cal-video', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  teams: { path: BASE + '/teams', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: BASE + '/enterprise', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { path: BASE + '/customers', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: BASE + '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faq: { path: BASE + '/faq', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  booking: { path: BOOKER, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('day', async () => {
      // Pick another bookable day in the grid: a numbered button that is not
      // disabled and not the already-selected one. Read-only; shows its slots.
      const d = p.locator('button[data-testid="date"], td button, [role="gridcell"] button, button').filter({ hasText: /^\s*1[3-9]\s*$/ }).filter({ visible: true }).first();
      const target = (await d.count()) ? d : p.locator('button').filter({ hasText: /^\s*\d{1,2}\s*$/ }).filter({ visible: true }).nth(4);
      if (await target.count()) { await clickEl(target); await wait(p, 1500); await S.view('slots'); }
    });
    await step('form', async () => {
      // A time slot opens the guest details form — captured as a boundary,
      // never filled and never confirmed.
      const slot = p.locator('button, a').filter({ hasText: /^\s*\d{1,2}:\d{2}(am|pm)\s*$/i }).filter({ visible: true }).first();
      if (await slot.count()) { await clickEl(slot); await wait(p, 2000); await S.view('form'); }
    });
  } },
  'booking-dark': { path: BOOKER_DARK, wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  login: { path: AUTH + '/auth/login', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  signup: { path: AUTH + '/signup', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: BASE + '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('nav button[aria-label], nav button, header button').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  booking: { path: BOOKER, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = spec.theme || 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      await p.goto(spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
