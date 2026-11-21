// Captures endel.io's and app.endel.io's public signed-out pages into RAW
// (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix. Both surfaces paint one
// dark theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, downloaded or signed into: the only presses are local UI toggles that open
// an overlay — the mobile menu, the marketing header's "More" flyout, the player's "Set Timer"
// dialog — each closed again without submitting. No consent overlay mounts on these routes.
import fs from 'fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

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
        // Register the temp path BEFORE capture: a rejected shot (dimension
        // check) still leaves `.new.png` on disk, and it must join the
        // cleanup list or quantize.py would publish it as a normal PNG.
        staged.push([f + '.new.png', f + '.png']);
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          staged.push([tmp, `${f}.part${i}.png`]);
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
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

// The marketing header's "More" MenuButton opens a flyout of nav groups inside
// the header itself (a local toggle, no navigation).
const openMore = async (p) => {
  const b = p.locator('[class*="MenuButton-module"]').first();
  if (!(await b.count())) return false;
  await clickEl(b); await wait(p, 1600);
  return true;
};
// The phone header replaces the nav with a "Menu" text button (Button-module,
// text "Menu"): press it by its label.
const openMobileMenu = async (p) => {
  const b = p.locator('header button').filter({ hasText: /^Menu$/ }).first();
  if (!(await b.count())) return false;
  await clickEl(b); await wait(p, 1600);
  return true;
};
// The player page's "Set Timer" button opens the TimerForm overlay; Escape
// (or the Done button) closes it again. A local dialog — nothing is sent.
const openTimer = async (p) => {
  const b = p.locator('button').filter({ hasText: /Set Timer/i }).first();
  if (!(await b.count())) return false;
  await clickEl(b); await wait(p, 1500);
  return true;
};
const closeTimer = async (p) => {
  await p.keyboard.press('Escape'); await wait(p, 700);
  const open = await p.evaluate(() => !!document.querySelector('[class*="TimerForm-module"]'));
  if (open) { const d = p.locator('button').filter({ hasText: /^Done$/ }).first(); if (await d.count()) await clickEl(d); await wait(p, 700); }
};

const plain = { run: async (p, S) => { await S.view('default'); await S.full(); } };

// app.endel.io/login redirects to the explore page on a fresh load: the
// sign-in card only mounts through the app's own Sign In button, which is
// plain in-app navigation to a public auth page — nothing is entered or sent.
const openLogin = async (p) => {
  await p.locator('header button').filter({ hasText: /Sign In/ }).first().click({ timeout: 8000 }).catch(() => {});
  await p.waitForURL('**/login**', { timeout: 15000 }).catch(() => {});
  await wait(p, 2500);
  // The email field's placeholder is the product's own example address, and
  // Chromium paints it as the field value. Hide it for the shot. Nothing is typed.
  await p.addStyleTag({ content: 'input::placeholder{color:transparent!important}' }).catch(() => {});
};

const desktop = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMore(p)) await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await S.full();
  } },
  focus: { url: BASE + '/focus', wait: 8000, ...plain },
  sleep: { url: BASE + '/sleep', wait: 8000, ...plain },
  relax: { url: BASE + '/relax', wait: 8000, ...plain },
  activity: { url: BASE + '/activity', wait: 8000, ...plain },
  adhd: { url: BASE + '/adhd', wait: 8000, ...plain },
  soundscapes: { url: BASE + '/soundscapes', wait: 8000, ...plain },
  science: { url: BASE + '/science', wait: 8000, ...plain },
  technology: { url: BASE + '/technology', wait: 8000, ...plain },
  streaming: { url: BASE + '/streaming', wait: 8000, ...plain },
  community: { url: BASE + '/community', wait: 8000, ...plain },
  about: { url: BASE + '/about', wait: 8000, ...plain },
  blog: { url: BASE + '/blog', wait: 8000, ...plain },
  newsroom: { url: BASE + '/newsroom', wait: 8000, ...plain },
  scenarios: { url: BASE + '/scenarios', wait: 8000, ...plain },
  'privacy-policy': { url: BASE + '/privacy-policy', wait: 7000, ...plain },
  impressum: { url: BASE + '/impressum', wait: 7000, ...plain },
  'app-explore': { url: APP + '/', wait: 9000, ...plain },
  'app-player': { url: APP + '/player/focus', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('timer-open', async () => { if (await openTimer(p)) await S.view('timer-open'); await closeTimer(p); });
    await S.full();
  } },
  'app-login': { url: APP + '/', wait: 8000, pre: openLogin, ...plain },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await S.full();
  } },
  focus: { url: BASE + '/focus', wait: 8000, ...plain },
  soundscapes: { url: BASE + '/soundscapes', wait: 8000, ...plain },
  scenarios: { url: BASE + '/scenarios', wait: 8000, ...plain },
  'app-explore': { url: APP + '/', wait: 9000, ...plain },
  'app-login': { url: APP + '/', wait: 8000, pre: openLogin, ...plain },
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
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    if (spec.pre) await spec.pre(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
