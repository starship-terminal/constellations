// Captures calm.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. calm.com paints TWO
// surfaces: the light marketing pages (home/family/gift/science/mindfulness/faq/terms + the
// WordPress health.calm.com B2B site) and the dark signed-out app preview on /app/sleep,
// /app/meditate and /app/music — a real product shell, public signed-out. calm.com sits behind
// PerimeterX: a route that comes back as the 403 px-captcha shell is recorded as BLOCKED and
// retried on the SAME context (the clearance cookie lives there) with a pause, then on a fresh
// context after a longer quiet wait. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A
// page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing
// is sent, bought or signed into: the only presses are local UI toggles — the nav dropdown
// triggers, the Log In button (opens a card, never submitted) and the mobile menu. The consent
// banner is hidden, never answered.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, isChallengeText, patch, chromium, UA_DESKTOP, UA_MOBILE, BASE, HEALTH } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'calm', 'raw-shots');
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
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    // The full-page shot runs before the toggle steps: the nav-item click can
    // swap the app view (and once emptied the page, every later shot would be
    // a blank shell).
    await S.full();
    await step('login-card', async () => {
      const t = p.locator('button[data-testid="desktopnav-login-button"], header button').filter({ hasText: /^\s*Log ?In\s*$/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1600); await S.view('login'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await step('signup-flow', async () => {
      const before = p.url();
      const t = p.locator('header a, header button').filter({ hasText: /Try\s*Calm/i }).filter({ visible: true }).first();
      if (await t.count()) {
        await clickEl(t); await wait(p, 2500);
        if (p.url() !== before) {
          // /signup-flow gets its own PerimeterX challenge; the landing is
          // shot only when a real page clears, then left.
          if (await clearChallenge(p)) { await wait(p, 3000); await S.view('signup'); }
          else log('  signup landing stayed gated; no shot');
          await p.goBack({ waitUntil: 'domcontentloaded' }).catch(() => {}); await wait(p, 4000);
        } else { await S.view('signup'); await p.keyboard.press('Escape'); await wait(p, 600); }
      }
    });
    await step('nav-dropdown', async () => {
      const t = p.locator('header nav button, header button, nav[aria-label="primary"] button').filter({ hasText: /^\s*(Sleep|Stress|Mindfulness|Screening|Calm Health)/ }).filter({ visible: true }).first();
      if (await t.count()) {
        const before = p.url();
        await clickEl(t);
        await wait(p, 1400);
        const panel = await p.evaluate(() => {
          const el = [...document.querySelectorAll('[role="menu"], [class*="Dropdown" i], [class*="Submenu" i], [class*="Panel" i], [class*="Menu" i]')].find((x) => { const r = x.getBoundingClientRect(); const cs = getComputedStyle(x); return r.width > 80 && r.height > 80 && cs.visibility !== 'hidden' && cs.display !== 'none'; });
          return !!el;
        }).catch(() => false);
        if (p.url() !== before) { await p.goBack({ waitUntil: 'domcontentloaded' }).catch(() => {}); await wait(p, 4000); }
        else if (panel) { await S.view('nav-hover'); await p.keyboard.press('Escape'); }
        else log('  nav item opened no panel; no nav-hover shot');
      }
    });
  } },
  sleep: { path: '/app/sleep', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  meditate: { path: '/app/meditate', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  music: { path: '/app/music', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  family: { path: '/family', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  gift: { path: '/gift', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  science: { path: '/science', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  mindfulness: { path: '/mindfulness-tips', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faq: { path: '/faq/web', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: 'https://blog.calm.com/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  health: { url: HEALTH + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  healthOrg: { url: HEALTH + '/calm-for-organizations/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { path: '/terms', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    // the full-page shot must come before the menu opens: the panel is a
    // fixed full-screen overlay and would cover the capture's first screen
    await S.full();
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], button[data-testid*="menu" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
  } },
};

const b = await chromium.launch({ headless: !process.env.HEADED });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
// One context per width, reused across routes: PerimeterX clearance is a
// context cookie, so churning contexts restarts the scoring. When the gate
// answers with the px-captcha shell, the run waits (it decays after minutes
// of quiet), reloads the same context, and only replaces the context when
// two reloads stay blocked.
const ctxByMob = {};
async function ctxFor(mob, vw, vh, dpr) {
  if (ctxByMob[mob]) return ctxByMob[mob];
  const ctx = ctxByMob[mob] = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA_DESKTOP, locale: 'en-US' });
  await patch(ctx);
  return ctx;
}

for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = ['sleep', 'meditate', 'music'].includes(k) ? 'dark' : 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const url = spec.url || BASE + spec.path;
  let done = false;
  // A blocked run waits the gate out rather than giving up: the capture can
  // take hours of wall clock, and a recorded boundary is for routes that
  // never open, not a bad 20 minutes.
  for (let attempt = 0; attempt < 40 && !done; attempt++) {
    const ctx = await ctxFor(mob, vw, vh, dpr);
    const p = await ctx.newPage();
    log(name, attempt ? `(attempt ${attempt})` : '');
    const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (await clearChallenge(p)) {
        await wait(p, spec.wait || 7000);
        await spec.run(p, S);
        done = true;
      } else {
        log('  BLOCKED challenge', url, '- retry in same context after 90s');
        await p.close().catch(() => {});
        await new Promise((r) => setTimeout(r, 90000));
        const p2 = await ctx.newPage();
        await p2.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        if (await clearChallenge(p2)) {
          await wait(p2, spec.wait || 7000);
          const S2 = new Shooter(p2, `${name}-${theme}`, vw, vh, dpr);
          await spec.run(p2, S2);
          total += S2.count;
          done = true;
        } else {
          log('  still blocked; fresh context after a 5 min quiet wait');
          await p2.close().catch(() => {});
          await ctx.close().catch(() => {});
          ctxByMob[mob] = null;
          await new Promise((r) => setTimeout(r, 300000));
        }
      }
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await p.close().catch(() => {});
  }
  if (!done) log('  gave up on', name);
}
for (const c of Object.values(ctxByMob)) await c?.close().catch(() => {});
log('done', total, 'screenshots ->', RAW);
await b.close();
