// Captures ballparkhq.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, downloaded or signed into: the only presses are local UI toggles — the Solutions
// nav menu (opened by its own trigger) and the mobile menu. No consent overlay mounts on these routes.
import fs from 'fs';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots go to a scratch dir outside the repo (the kit's default), never into
// systems/<slug>/raw/: quantize.py reads them from there and writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(fileURLToPath(new URL('../../..', import.meta.url))), 'raw-shots');
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

// The Solutions mega menu is a Framer overlay the nav link opens on hover.
const openSolutions = async (p) => {
  const m = p.locator('header a, nav a').filter({ hasText: /^Solutions$/ }).filter({ visible: true }).first();
  if (await m.count()) {
    await m.hover(); await wait(p, 1400);
    return p.evaluate(() => {
      const ov = [...document.querySelectorAll('[class*="framer"][class*="container"], [role="dialog"], nav + div, header + div')].some((n) => {
        const r = n.getBoundingClientRect(); const c = getComputedStyle(n);
        return r.y > 40 && r.y < 200 && r.height > 200 && c.opacity !== '0' && c.visibility !== 'hidden';
      });
      return ov || true; // the menu state is captured even when detection is unsure
    });
  }
  return false;
};

// The mobile header's menu trigger is the 36x36 pointer div at the bar's right edge.
const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const h = document.querySelector('header');
    if (!h) return false;
    const cand = [...h.querySelectorAll('div,button')].filter((n) => {
      const r = n.getBoundingClientRect(); const c = getComputedStyle(n);
      return r.width >= 28 && r.width <= 48 && r.height >= 28 && r.height <= 48 && r.x > 280 && c.cursor === 'pointer';
    });
    const el = cand[0];
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  const b = p.locator('[data-m-menu="1"]');
  await clickEl(b); await wait(p, 1600);
  return true;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('solutions-menu', async () => { if (await openSolutions(p)) await S.view('solutions-menu'); await p.keyboard.press('Escape'); await p.mouse.move(700, 400); await wait(p, 500); });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { path: '/features', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  coach: { path: '/coach', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  templates: { path: '/templates', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/contact/sales', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { path: '/sign-in', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
