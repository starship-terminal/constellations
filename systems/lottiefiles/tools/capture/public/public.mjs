// Captures lottiefiles.com public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=.../playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// The marketing site paints one light theme. Desktop shots are 1440x900 at 1x,
// mobile shots 390x844 at 2x. A page taller than one GPU texture is saved as
// name.partN.png tiles, capped at 8 chunks.
//
// Cookie banners are hidden, never clicked. Log in, Sign up, Download, checkout
// and app.lottiefiles.com are never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideConsent, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lottiefiles', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 7000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 700);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const ANIM = '/free-animation/loading-animation-for-client-book-0DK063WUDW';

async function openMenu(p) {
  const btn = p.getByRole('button', { name: 'Products' }).first();
  await btn.hover();
  await wait(p, 700);
}

async function openMobileNav(p) {
  // The phone chrome is two SVGs in a div.xl:hidden, not buttons. The right
  // one is the hamburger. Mark it, then click that mark.
  const marked = await p.evaluate(() => {
    const svgs = [...document.querySelectorAll('svg')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.top >= 0 && r.top < 70 && r.left > 280 && r.width >= 16 && r.width <= 40 && r.height >= 16 && r.height <= 40;
    });
    const icon = svgs[svgs.length - 1];
    if (!icon) return false;
    icon.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!marked) { log('  ! mobile menu icon not marked'); return; }
  await p.locator('[data-m-menu="1"]').click();
  await wait(p, 800);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('products-menu', async () => { await openMenu(p); await S.view('products-menu'); await p.keyboard.press('Escape'); await p.mouse.move(10, 700); await wait(p, 400); });
    await step('search-focus', async () => {
      const s = p.getByRole('button', { name: 'Search animations' }).first();
      await s.click();
      await wait(p, 600);
      await S.view('search-focus');
      await p.keyboard.press('Escape');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  animations: { path: '/free-animations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  animation: { path: ANIM, run: async (p, S) => {
    await S.view('default');
    await step('download-tab', async () => {
      const b = p.getByRole('tab', { name: 'Download' }).first();
      await b.click({ timeout: 8000 });
      await wait(p, 700);
      await S.view('download-tab');
    });
  } },
  marketplace: { path: '/marketplace', run: async (p, S) => { await S.view('default'); } },
  featured: { path: '/featured-free-animations', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); } },
  customers: { path: '/customers', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/this-page-does-not-exist-capture', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => { await openMobileNav(p); await S.view('menu'); });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  animations: { path: '/free-animations', run: async (p, S) => { await S.view('default'); } },
  animation: { path: ANIM, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
    // Pin the CSS viewport. Without this, a page can grow the layout viewport
    // past the requested 390 (the animation page did, to 459).
    screen: { width: vw, height: vh },
  });
  // Automation is not hidden: no navigator.webdriver mask (bot check: recorded as a boundary, not bypassed).
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, BASE + spec.path);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 3200);
    await hideConsent(p);
    if (mob) {
      // Some animation pages set a min-width that grows innerWidth past 390
      // while visualViewport stays 390. Pin the layout width to the request.
      await p.addStyleTag({ content: 'html,body{min-width:0!important;max-width:390px!important;overflow-x:hidden!important}' });
      await wait(p, 300);
    }
    const dims = await p.evaluate(() => ({ w: innerWidth, h: innerHeight, dpr: devicePixelRatio }));
    log('  viewport', dims.w + 'x' + dims.h, 'dpr', dims.dpr);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
