// Captures replo.app's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix. The site paints one dark
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, downloaded or signed into. Presses are local UI only: nav menus,
// homepage accordions, the mobile drawer. Login and signup URLs are opened and
// recorded, never filled. Google and Apple are never clicked.
import fs from 'fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems', 'replo', 'raw-shots');
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

// Desktop nav uses named buttons. The phone header uses a button labelled
// Open menu. This helper is a fallback for an unlabelled icon button.
const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const h = document.querySelector('header');
    if (!h) return false;
    // The hamburger is a tiny icon control at the bar's right edge — on this
    // build a 14x14 nested `header` element with cursor:pointer, no text.
    const cand = [...h.querySelectorAll('*')].filter((n) => {
      const r = n.getBoundingClientRect(); const c = getComputedStyle(n);
      const iconish = n.tagName === 'BUTTON' || c.cursor === 'pointer' || (n.querySelector('svg,img') && !(n.innerText || '').trim());
      return r.width >= 12 && r.width <= 72 && r.height >= 12 && r.height <= 72 && r.x > 260 && iconish;
    });
    const el = cand[cand.length - 1];
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  const b = p.locator('[data-m-menu="1"]');
  await clickEl(b); await wait(p, 1600);
  return true;
};

const openNav = async (p, label) => {
  const b = p.getByRole('button', { name: label, exact: true }).first();
  if (!(await b.count())) return false;
  await clickEl(b);
  await wait(p, 900);
  return true;
};

const pageShot = (path, wait = 7000) => ({ path, wait, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => { if (await openNav(p, 'Product')) { await S.view('product-menu'); await p.keyboard.press('Escape'); await wait(p, 400); } });
    await step('solutions-menu', async () => { if (await openNav(p, 'Solutions')) { await S.view('solutions-menu'); await p.keyboard.press('Escape'); await wait(p, 400); } });
    await step('resources-menu', async () => { if (await openNav(p, 'Resources')) { await S.view('resources-menu'); await p.keyboard.press('Escape'); await wait(p, 400); } });
    await step('accordion', async () => {
      const b = p.getByRole('button', { name: /Copy any website/i }).first();
      if (await b.count()) { await b.scrollIntoViewIfNeeded(); await clickEl(b); await wait(p, 700); await S.view('accordion'); }
    });
    await S.full();
  } },
  pricing: pageShot('/pricing'),
  contact: pageShot('/contact'),
  customers: pageShot('/case-studies'),
  products: pageShot('/products'),
  website: pageShot('/website-builder'),
  research: pageShot('/research'),
  analytics: pageShot('/analytics'),
  integrations: pageShot('/integrations', 6000),
  blog: pageShot('/blog', 6000),
  guides: pageShot('/guides', 6000),
  compare: pageShot('/compare', 6000),
  templates: pageShot('/templates', 6000),
  tools: pageShot('/tools', 6000),
  use: pageShot('/use-cases', 6000),
  privacy: pageShot('/privacy', 5000),
  careers: pageShot('/careers', 6000),
  notfound: pageShot('/login', 4000),
  login: { path: 'https://dashboard.replo.app/auth/login', absolute: true, wait: 5000, run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Open menu' });
      if (await b.count()) { await clickEl(b); await wait(p, 900); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: pageShot('/pricing'),
  contact: pageShot('/contact', 5000),
  customers: pageShot('/case-studies'),
  products: pageShot('/products'),
  website: pageShot('/website-builder'),
  research: pageShot('/research'),
  analytics: pageShot('/analytics'),
  integrations: pageShot('/integrations', 6000),
  blog: pageShot('/blog', 6000),
  guides: pageShot('/guides', 6000),
  compare: pageShot('/compare', 6000),
  templates: pageShot('/templates', 6000),
  tools: pageShot('/tools', 6000),
  use: pageShot('/use-cases', 6000),
  privacy: pageShot('/privacy', 5000),
  careers: pageShot('/careers', 6000),
  notfound: pageShot('/login', 4000),
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
    const url = spec.absolute ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
