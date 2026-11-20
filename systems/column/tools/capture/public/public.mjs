// Captures column.com's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   node public.mjs [page ...]
//
// Only signed-out surfaces: the marketing routes (home, the ACH/book
// transfers/wires/stablecoins product pages, global banking, loans,
// multicurrency, realtime, checks, company, careers, blog, security,
// contact, legal), and the dashboard.column.com login card — the last an
// app sign-in boundary, screenshotted never acted on. Every "Create an
// account"/"Get started" CTA points at dashboard registration or docs;
// none was followed or submitted.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'column', 'raw-shots');
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

// The mobile header's hamburger: the aria-label="Open navigation menu" toggle
// in the 390 bar — a local menu toggle, never a link.
const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const el = document.querySelector('button[aria-label*="menu" i], [data-testid*="hamburger"], header button[aria-expanded], button[aria-label="Open navigation menu"], header nav button, header button');
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await clickEl(p.locator('[data-m-menu="1"]'));
  await wait(p, 1600);
  return true;
};

const mk = (url, wait, full = true, theme = 'light') => ({ url, wait, theme, run: async (p, S) => { await S.view('default'); if (full) await S.full(); } });
const desktop = {
  home: mk('/', 12000),
  ach: mk('/ach/', 10000),
  bankaccounts: mk('/bank-accounts/', 10000),
  booktransfers: mk('/book-transfers/', 9000),
  cardprograms: mk('/card-programs/', 10000),
  checks: mk('/checks/', 9000),
  globalbanking: mk('/global-banking/', 10000),
  intlwires: mk('/international-wires/', 9000),
  loanorig: mk('/loan-origination/', 9000),
  multicurrency: mk('/multicurrency/', 9000),
  realtime: mk('/realtime/', 9000),
  stablecoins: mk('/stablecoins/', 10000),
  wire: mk('/wire/', 9000),
  company: mk('/company/', 9000),
  careers: mk('/careers/', 8000),
  blog: mk('/blog/', 8000),
  security: mk('/security/', 8000),
  contact: mk('/contact/', 8000),
  privacy: mk('/legal/privacy-notice/', 8000),
  // The sign-in boundary: dashboard.column.com/login, an app sign-in card
  // shot never acted on (waits longer — the app bundle boots first).
  signin: mk('https://dashboard.column.com/login', 15000, false, 'light'),
};

const mobile = {
  home: { url: '/', wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) { await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  ach: mk('/ach/', 9000),
  cardprograms: mk('/card-programs/', 9000),
  blog: mk('/blog/', 8000),
};

const b = await chromium.launch({ headless: true }); // column.com renders headless; no bot wall
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
  p.setDefaultTimeout(90000);
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme || 'light'}`, vw, vh, dpr);
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
