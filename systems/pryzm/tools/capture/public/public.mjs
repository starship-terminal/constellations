// Captures Pryzm's public pages into RAW (full-colour PNGs). quantize.py turns
// them into screenshots/. Nothing is submitted: no email, no password, no
// checkout, no Google click, no newsletter.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png. Pryzm pins `class="dark"` and has no light
// theme on the public pages. Desktop shots are 1440x900 at 1x, phone shots
// 390x844 at 2x. A page taller than one GPU texture is saved as part tiles.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
  await wait(p, 400);
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
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
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
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function clickButton(p, name) {
  const b = p.getByRole('button', { name }).first();
  if (!(await b.count())) return false;
  await b.click({ timeout: 4000 });
  await wait(p, 700);
  return true;
}

async function stopIfWall(p, label) {
  if (isWall(p.url())) {
    log('  WALL', label, p.url().replace(/[?#].*$/, ''));
    return true;
  }
  return false;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('pricing-yearly', async () => {
      await p.getByRole('tab', { name: /Yearly/ }).click();
      await wait(p, 400);
      await p.locator('#pricing').scrollIntoViewIfNeeded().catch(() => {});
      await S.view('pricing-yearly');
      await p.getByRole('tab', { name: /Monthly/ }).click();
    });
    await step('faq', async () => {
      const q = p.locator('#faq button, [id*="faq"] button').first();
      if (await q.count()) {
        await q.scrollIntoViewIfNeeded();
        await q.click();
        await wait(p, 400);
        await S.view('faq-open');
      } else log('  no faq button');
    });
  } },
  gallery: { path: '/gallery', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('collapsed', async () => {
      await clickButton(p, 'Collapse');
      await S.view('sidebar-collapsed');
    });
    await step('filter', async () => {
      await p.goto(BASE + '/gallery?tag=Glass', { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(p, 1200);
      await S.view('filter-glass');
    });
  } },
  look: { path: '/gallery/bright-spark', run: async (p, S) => {
    await S.view('default');
    await step('remix', async () => {
      await clickButton(p, 'Remix');
      if (await stopIfWall(p, 'remix')) return;
      await S.view('remix-dialog');
      await p.keyboard.press('Escape');
    });
  } },
  'look-pro': { path: '/gallery/ink-facet-280dcf', run: async (p, S) => {
    await S.view('default');
    await step('remix-paywall', async () => {
      await clickButton(p, 'Remix');
      if (await stopIfWall(p, 'remix-paywall')) return;
      await S.view('remix-paywall');
      await p.keyboard.press('Escape');
    });
  } },
  studio: { path: '/studio', wait: 2500, run: async (p, S) => {
    await S.view('default');
    await step('export', async () => {
      await clickButton(p, /^Export$/);
      await S.view('export-dialog');
      await p.keyboard.press('Escape');
    });
    await step('share', async () => {
      await clickButton(p, /^Share$/);
      await S.view('share-dialog');
      await p.keyboard.press('Escape');
    });
    await step('aspects', async () => {
      await clickButton(p, 'More aspect ratios');
      await S.view('aspect-menu');
      await p.keyboard.press('Escape');
    });
    await step('square', async () => {
      await clickButton(p, 'Square');
      await S.view('square');
    });
  } },
  lab: { path: '/lab', wait: 2200, run: async (p, S) => {
    await S.view('default');
    await step('add-layer', async () => {
      await clickButton(p, 'Add a layer');
      await S.view('add-layer');
      await p.keyboard.press('Escape');
    });
    await step('export', async () => {
      await clickButton(p, /^Export$/);
      await S.view('export-dialog');
      await p.keyboard.press('Escape');
    });
  } },
  flow: { path: '/flow', wait: 2200, run: async (p, S) => {
    await S.view('default');
    await step('add-node', async () => {
      await clickButton(p, 'Add node');
      await S.view('add-node');
      await p.keyboard.press('Escape');
    });
    await step('import-empty', async () => {
      await clickButton(p, 'Import look');
      await S.view('import-empty');
      await p.keyboard.press('Escape');
    });
    await step('export', async () => {
      await clickButton(p, /^Export$/);
      await S.view('export-dialog');
      await p.keyboard.press('Escape');
    });
  } },
  docs: { path: '/docs', run: async (p, S) => {
    await S.view('default');
    await step('quick-start', async () => {
      await clickButton(p, 'Quick start');
      await wait(p, 400);
      await S.view('quick-start');
    });
  } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  post: { path: '/blog/how-to-make-a-gradient-background-for-your-website', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  support: { path: '/support', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/signin', run: async (p, S) => {
    // Wall only. Do not type, do not click Google, do not submit.
    await S.view('wall');
  } },
  login: { path: '/login', run: async (p, S) => { await S.view('404'); } },
  'my-work': { path: '/my-work', run: async (p, S) => {
    if (await stopIfWall(p, 'my-work')) await S.view('redirect-signin');
    else await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await clickButton(p, 'Menu');
      await S.view('menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await S.full();
  } },
  gallery: { path: '/gallery', run: async (p, S) => { await S.view('default'); await S.full(); } },
  studio: { path: '/studio', wait: 2500, run: async (p, S) => { await S.view('default'); } },
  lab: { path: '/lab', wait: 2000, run: async (p, S) => { await S.view('default'); } },
  flow: { path: '/flow', wait: 2000, run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/signin', run: async (p, S) => { await S.view('wall'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
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
    colorScheme: 'dark',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1600);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
