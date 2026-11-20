// Captures classpass.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page ...]
//
// Only signed-out surfaces: the marketing pages, the public studio search,
// the plan picker, the gift/review/feature pages, the /login sign-in card
// and the /walkthrough trial entry — the last two are documented boundaries,
// screenshotted never acted on. The TrustArc consent overlay is hidden, never
// answered; the promo banner is left painted (real UI).
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'classpass', 'raw-shots');
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

// Opens the header "How it works" dropdown (a Headless-UI menu button —
// a local nav toggle, never a link).
const openNavDropdown = async (p) => {
  const ok = await p.evaluate(() => {
    const el = document.querySelector('[class*="NavDesktopDropdown_Button"]');
    if (!el) return false;
    el.setAttribute('data-m-nav', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-nav="1"]'));
  await wait(p, 1200);
  return true;
};

// Opens the public search's "Activities" multi-select (a local filter
// toggle — Clear/Done are never pressed).
const openFilterPanel = async (p) => {
  const ok = await p.evaluate(() => {
    const el = [...document.querySelectorAll('[data-testid="MultiSelectFilter"]')].find((n) => /activities/i.test(n.innerText || ''));
    const btn = el && (el.tagName === 'BUTTON' ? el : el.querySelector('button'));
    if (!btn) return false;
    btn.setAttribute('data-m-filter', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-filter="1"]'));
  await wait(p, 1200);
  return true;
};

// The mobile header's menu trigger: button.Menu_toggler at the bar's right edge.
const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const el = [...document.querySelectorAll('[class*="Menu_toggler"]')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.y >= 0 && r.y < 90 && r.width >= 24;
    });
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-menu="1"]'));
  await wait(p, 1600);
  return true;
};

const desktop = {
  home: { url: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openNavDropdown(p)) { await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  search: { url: '/search', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('filter-open', async () => { if (await openFilterPanel(p)) { await S.view('filter-open'); await p.keyboard.press('Escape'); await wait(p, 400); } });
    await S.full();
  } },
  plans: { url: '/plans', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { url: '/features', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  how: { url: '/how-classpass-works', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  fitness: { url: '/fitness', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  gifts: { url: '/gifts', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  reviews: { url: '/try/reviews', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  partners: { url: '/partners', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  corp: { url: '/corporate-wellness', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: '/about', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: '/contact', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: '/terms', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  signin: { url: '/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  walk: { url: '/walkthrough', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) { await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  search: { url: '/search', wait: 11000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  plans: { url: '/plans', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
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
    const u = /^https?:/.test(spec.url) ? spec.url : BASE + spec.url;
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
