// Captures jitter.video's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Signed-out only. Login and signup cards are screenshotted and never
// acted on. Cookie/consent overlays and Intercom are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, patch } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 9000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    // Chromium refuses a fullPage PNG taller than one GPU texture. Tile by
    // scrolling one viewport at a time and clipping to the visible window,
    // which the screenshot helper can check. Eight tiles is the kit cap.
    const chunk = p.viewportSize().height;
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px (8 viewport tiles)`);
    const staged = [];
    try {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await p.evaluate((yy) => scrollTo(0, yy), y);
        await wait(p, 220);
        const tmp = `${f}.part${i}.new.png`;
        const h = Math.min(chunk, hCap - y);
        await screenshotWithMetadata(p, { path: tmp, clip: { x: 0, y: 0, width: this.vw, height: h } }, this.requested);
        staged.push([tmp, `${f}.part${i}.png`]);
      }
    } catch (e) {
      for (const [tmp] of staged) {
        fs.existsSync(tmp) && fs.unlinkSync(tmp);
        fs.existsSync(tmp + '.capture.json') && fs.unlinkSync(tmp + '.capture.json');
      }
      throw e;
    }
    const keep = new Set();
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      keep.add(path.basename(final));
      const sideTmp = tmp + '.capture.json';
      const sideFinal = final + '.capture.json';
      if (fs.existsSync(sideTmp)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sideTmp, 'utf8'));
          meta.screenshot = path.basename(final);
          fs.writeFileSync(sideTmp, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* keep sidecar */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    for (const old of fs.readdirSync(RAW).filter((n) => !keep.has(n) && (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`))) {
      if (n.includes('.new.')) continue;
      fs.unlinkSync(`${RAW}/${old}`);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const openMenu = async (p) => {
  const btn = p.getByRole('button', { name: 'Open menu' });
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 4000 });
  await wait(p, 800);
  return true;
};

const mk = (url, waitMs = 3500, full = true) => ({
  url, wait: waitMs, full,
  run: async (p, S) => { await S.view('default'); if (full) await S.full(); },
});

const desktop = {
  home: mk('/', 4000),
  product: mk('/product/', 3500),
  pricing: {
    url: '/pricing/', wait: 3500,
    run: async (p, S) => {
      await S.view('default');
      const annual = p.getByRole('button', { name: /Pay annually/i });
      if (await annual.count()) {
        await annual.click({ timeout: 4000 }).catch(() => {});
        await wait(p, 600);
        await S.view('annual');
        const monthly = p.getByRole('button', { name: /Pay monthly/i });
        if (await monthly.count()) await monthly.click({ timeout: 3000 }).catch(() => {});
      }
      await S.full();
    },
  },
  templates: mk('/templates/', 4000),
  customers: mk('/customers/', 3500),
  customer: mk('/customers/perplexity/', 3500),
  changelog: mk('/changelog/', 3500),
  agencies: mk('/jitter-for-agencies/', 3000),
  compare: mk('/jitter-vs-after-effects/', 3000),
  manifesto: mk('/ai-manifesto/', 3000),
  community: mk('/community/', 3000),
  brand: mk('/brand/', 3000),
  login: mk('/login/', 4000, false),
  signup: mk('/join/', 4000, false),
  contact: mk('/contact-sales/', 3500, false),
  notfound: mk('/this-page-is-not-real/', 2500, false),
};

const mobile = {
  home: {
    url: '/', wait: 4000,
    run: async (p, S) => {
      await S.view('default');
      if (await openMenu(p)) {
        await S.view('menu-open');
        await p.keyboard.press('Escape').catch(() => {});
        await wait(p, 400);
      }
      await S.full();
    },
  },
  pricing: mk('/pricing/', 3500),
  templates: mk('/templates/', 3500),
  product: mk('/product/', 3000, false),
  login: mk('/login/', 3500, false),
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  p.setDefaultTimeout(20000);
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const u = /^https?:/.test(spec.url) ? spec.url : BASE + spec.url;
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 3000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
