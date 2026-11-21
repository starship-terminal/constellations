// Public Meta shop screenshots. RAW holds full-colour PNGs. quantize.py
// writes the 256-colour copies under screenshots/.
//
//   RAW=/tmp/meta-ai-raw PLAYWRIGHT=... node public.mjs [home,shop,...]
//
// Stays on www.meta.com. Does not type a password, email, or code. Does not
// click Google, Apple, Facebook, or any identity provider. Does not submit
// a form. Does not add to bag. Does not open checkout.
import fs from 'node:fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const RAW = process.env.RAW || '/tmp/meta-ai-raw';
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 600);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: `${f}.png`, fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function hoverNav(p, name) {
  const loc = p.getByRole('link', { name, exact: true }).first();
  if (!(await loc.count())) return false;
  await loc.hover();
  await wait(p, 900);
  return true;
}

const desktop = {
  home: {
    path: '/sg/',
    run: async (p, S) => {
      await S.view('default');
      await step('glasses-menu', async () => {
        if (await hoverNav(p, 'AI glasses')) {
          await S.view('menu-glasses');
          await p.mouse.move(8, 8);
          await wait(p, 400);
        }
      });
      await step('quest-menu', async () => {
        if (await hoverNav(p, 'Meta Quest')) {
          await S.view('menu-quest');
          await p.mouse.move(8, 8);
          await wait(p, 400);
        }
      });
      await step('support-menu', async () => {
        if (await hoverNav(p, 'Support')) {
          await S.view('menu-support');
          await p.mouse.move(8, 8);
          await wait(p, 400);
        }
      });
      await S.full();
    },
  },
  glasses: { path: '/sg/ai-glasses/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  shop: { path: '/sg/ai-glasses/shop-all/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  quest: { path: '/sg/quest/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: {
    path: '/sg/quest/quest-3s/',
    run: async (p, S) => { await S.view('default'); await S.full(); },
  },
  bag: { path: '/bag/', run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help/', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about/', run: async (p, S) => { await S.view('default'); } },
  gift: { path: '/sg/gift-guide/', run: async (p, S) => { await S.view('default'); } },
  compare: { path: '/sg/ai-glasses/compare/', run: async (p, S) => { await S.view('default'); } },
  account: { path: '/account/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: {
    path: '/sg/',
    run: async (p, S) => {
      await S.view('default');
      await step('menu', async () => {
        const m = p.locator('header button, button[aria-label*="menu" i], button[aria-label*="Menu"]').filter({ visible: true }).first();
        if (await m.count()) {
          await m.click().catch(() => {});
          await wait(p, 1000);
          await S.view('menu');
        }
      });
    },
  },
  shop: { path: '/sg/ai-glasses/shop-all/', run: async (p, S) => { await S.view('default'); } },
  quest: { path: '/sg/quest/', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto('https://www.meta.com' + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, 4500);
    log('  url', p.url().split('?')[0], 'status', res && res.status());
    const host = new URL(p.url()).hostname;
    if (!host.endsWith('meta.com')) {
      log('  STOP left meta.com', host);
      await S.view('wall');
    } else {
      await spec.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
