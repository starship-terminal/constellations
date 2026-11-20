// Captures mapbox.com's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// The marketing site paints one light theme (Webflow, color-mode-light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than
// one GPU texture is saved as name.partN.png tiles. An unbounded page
// truncates at 8 chunks.
//
// Nothing is signed into, submitted or purchased. The OneTrust banner is
// hidden, never answered. The only presses are local UI toggles: the Products
// nav menu, the pricing product tabs, the docs search dialog (opened and
// closed), and the mobile menu. Sign-in, sign-up, account, checkout and
// contact-form submit are never followed.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mapbox', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
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
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
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
        } catch { /* keep sidecar */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    const isStaged = (n) => n.endsWith('.new.png') || n.endsWith('.new.png.capture.json');
    for (const old of fs.readdirSync(RAW).filter((n) =>
      !isStaged(n) && !keep.has(n) &&
      (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const openNav = async (p, label) => {
  const btn = p.locator('nav button.nav_link-toggle').filter({ hasText: label }).first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 4000 });
  await wait(p, 700);
  return true;
};

const openMobileMenu = async (p) => {
  const ok = await p.evaluate(() => {
    const el = document.querySelector('a.nav_menu-toggle, .nav_control-menu-toggle');
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await p.locator('[data-m-menu="1"]').click({ timeout: 4000 });
  await wait(p, 800);
  return true;
};

const desktop = {
  home: { url: BASE + '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      if (await openNav(p, 'Products')) { await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  maps: { url: BASE + '/maps', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  navigation: { url: BASE + '/navigation', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('maps-tab', async () => {
      const tab = p.locator('[role="tab"]').filter({ hasText: /^Maps$/ }).first();
      if (await tab.count()) { await tab.click(); await wait(p, 600); await S.view('maps-tab'); }
    });
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: 'https://docs.mapbox.com/', wait: 4000, run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.getByRole('button', { name: /Search/ }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 700);
        await S.view('search');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      }
    });
    await S.full();
  } },
  'docs-gljs': { url: 'https://docs.mapbox.com/mapbox-gl-js/guides/', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-style': { url: 'https://docs.mapbox.com/style-spec/reference/layers/', wait: 4000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: 'https://docs.mapbox.com/', wait: 4000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
    reducedMotion: 'reduce',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
