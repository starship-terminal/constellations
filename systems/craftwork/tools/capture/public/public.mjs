// Captures craftwork.design's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. craftwork.design paints
// both a light and a dark theme via the nav's local theme toggle (data-theme on <html>); a dark
// home shot is taken by flipping that toggle and flipping it back. Desktop shots are 1440x900 at
// 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary. Nothing is sent, bought or signed into: the only
// presses are local UI toggles — the theme switch and the mobile nav button. The OTP login card
// at /login is captured but its Send code is never pressed. A fixed cookie notice is hidden
// (never answered) by closePromo. Checkout, Pro purchase and every download action are never used.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'craftwork', 'raw-shots');
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

// The nav theme toggle: button[aria-label="Dark theme"|"Light theme"]. Local UI switch.
const themeToggle = (p) => p.locator('header button[aria-label*="theme" i], nav button[aria-label*="theme" i], button[aria-label*="Dark theme" i], button[aria-label*="Light theme" i]').filter({ visible: true }).first();

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('dark', async () => {
      const t = themeToggle(p);
      if (await t.count()) {
        await clickEl(t); await wait(p, 1600);
        await closePromo(p);
        // Shoot only what painted: the root must carry data-theme="dark" and the body a dark ground,
        // or a failed toggle is written as a light page named -dark.
        // The ground is the first opaque background from body up through html (a transparent
        // body shows what is behind it, which is not black); none at all is the canvas white.
        const dark = await p.evaluate(() => {
          let ground = [255, 255, 255];
          for (const el of [document.body, document.documentElement]) {
            const m = (getComputedStyle(el).backgroundColor.match(/[\d.]+/g) || []).map(Number);
            if (m.length >= 3 && (m.length < 4 || m[3] > 0.5)) { ground = m.slice(0, 3); break; }
          }
          const [r, g, b] = ground;
          return document.documentElement.getAttribute('data-theme') === 'dark' && 0.2126 * r + 0.7152 * g + 0.0722 * b < 80;
        });
        const shot = `${RAW}/home-dark-default.png`;
        if (dark) {
          await screenshotWithMetadata(p, { path: shot, sanitizedSourceUrl: S.sourceUrl }, S.requested);
          S.count++; log('  shot dark-default');
        } else {
          // an earlier run's file in a reused RAW dir would still be published by quantize.py
          for (const f of [shot, `${shot}.capture.json`]) fs.rmSync(f, { force: true });
          log('  ! the theme toggle did not paint dark; no dark shot (any earlier one removed)');
        }
        await clickEl(t); await wait(p, 1200);
      }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  components: { path: '/components', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  catalog: { path: '/catalog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  deal: { path: '/black-friday', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/login', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('filled', async () => {
      const e = p.locator('input[type="email"]').first();
      if (await e.count()) { await e.fill('name@example.com'); await wait(p, 800); await S.view('filled'); await e.fill(''); }
    });
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile header's nav button: a local overlay toggle.
      const m = p.locator('header button[aria-label*="menu" i], header button[aria-label*="nav" i], header button[aria-label*="Open" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
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
