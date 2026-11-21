// Public Playwright capture of zapier.com. Photographs reachable public states.
// Stops a branch when a control opens a login or signup wall. Never types, never
// submits, never clicks Google, Facebook, Microsoft, or any other identity provider.
//
//   RAW=~/.design-systems/zapier/raw-shots PLAYWRIGHT=... node public.mjs [name,name]
//
// Desktop 1440x900 at 2x. Phone 390x844 at 2x. Names are {page}-light-{state}.png
// with a mobile- prefix on the phone run.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { safeUrl } from '../safe-url.mjs';
import { chromium, UA, UA_MOBILE, BASE, WALL, stripUrl, hideOverlays, blocked } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'zapier', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const tree = { captured: new Date().toISOString().slice(0, 10), pages: [], walls: [], errors: [] };

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: safeUrl(stripUrl(p.url())) };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    this.requested.sanitizedSourceUrl = safeUrl(stripUrl(this.p.url()));
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name, stripUrl(this.p.url()));
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    this.requested.sanitizedSourceUrl = stripUrl(p.url());
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

async function go(p, urlPath) {
  const res = await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await wait(p, 2800);
  await hideOverlays(p);
  const status = res ? res.status() : null;
  const url = stripUrl(p.url());
  const isBlocked = await blocked(p);
  return { status, url, blocked: isBlocked };
}

function recordWall(from, url, status) {
  tree.walls.push({ from, url, status, stopped: true });
  log('  WALL', url, 'from', from);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    for (const name of ['Products', 'Solutions', 'Resources']) {
      await p.getByRole('button', { name, exact: true }).first().click();
      await wait(p, 700);
      await S.view('menu-' + name.toLowerCase());
      await p.keyboard.press('Escape');
      await wait(p, 250);
    }
    const feature = p.getByRole('button', { name: 'Instant access to 9,000+ apps' });
    if (await feature.count()) {
      await feature.first().click();
      await wait(p, 600);
      await p.evaluate(() => scrollTo(0, 1750));
      await wait(p, 400);
      await S.view('feature-apps');
      await p.evaluate(() => scrollTo(0, 0));
    }
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    const monthly = p.getByRole('button', { name: /monthly/i });
    if (await monthly.count()) {
      await monthly.first().click();
      await wait(p, 600);
      await S.view('monthly');
    }
    const tab = p.getByRole('tab').first();
    if (await tab.count()) {
      await tab.click();
      await wait(p, 400);
    }
  } },
  workflows: { path: '/workflows', run: async (p, S) => { await S.view('default'); } },
  apps: { path: '/apps', run: async (p, S) => { await S.view('default'); } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); } },
  templates: { path: '/templates', run: async (p, S) => { await S.view('default'); } },
  mcp: { path: '/mcp', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/app/login', wall: true, run: async (p, S) => { await S.view('empty'); } },
  signup: { path: '/sign-up', wall: true, run: async (p, S) => { await S.view('empty'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await hideOverlays(p);
    await S.view('default');
    const opener = p.getByRole('button', { name: 'Open menu' });
    if (await opener.count()) {
      await opener.first().click();
      await wait(p, 700);
      await hideOverlays(p);
      await S.view('menu');
    }
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/app/login', wall: true, run: async (p, S) => { await S.view('empty'); } },
  signup: { path: '/sign-up', wall: true, run: async (p, S) => { await S.view('empty'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
try {
  for (const { k, mob } of runs) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name)) continue;
    const spec = (mob ? mobile : desktop)[k];
    const vw = mob ? 390 : 1440;
    const vh = mob ? 844 : 900;
    const dpr = 2;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    await ctx.addInitScript(() => {
      Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    });
    const p = await ctx.newPage();
    log(name);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      const landed = await go(p, spec.path);
      tree.pages.push({ name, requested: BASE + spec.path, ...landed, wall: !!spec.wall });
      if (landed.blocked) {
        log('  BLOCKED', name);
        tree.errors.push({ name, error: 'challenge or empty body' });
      } else if (spec.wall || WALL.test(landed.url)) {
        recordWall(name, landed.url, landed.status);
        await spec.run(p, S);
      } else {
        await spec.run(p, S);
      }
    } catch (e) {
      const msg = String(e.message).split('\n')[0];
      log('  PAGE FAILED', name, msg);
      tree.errors.push({ name, error: msg });
    }
    total += S.count;
    await ctx.close();
  }
} finally {
  fs.writeFileSync(path.join(RAW, 'tree.json'), JSON.stringify(tree, null, 2) + '\n');
  log('done', total, 'screenshots ->', RAW);
  await browser.close();
}
