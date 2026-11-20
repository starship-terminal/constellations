// Captures withjulienne.com's public signed-out pages.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [name,name]
//
// Desktop 1440x900 at 1x, mobile 390x844 at 2x. Light is the boot theme
// (html.js.light). Dark is the header's own Toggle theme control, verified
// by html.js.dark before the shot. Auth, Save, Cook, Buy and search submit
// are never pressed. Consent overlays are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, RECIPE, COLLECTION, closePromo, setTheme, clearChallenge } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'julienne', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 9000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function goto(p, url) {
  await p.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await clearChallenge(p);
  await wait(p, 1800);
  await closePromo(p);
}

async function theme(p, which) {
  const got = await setTheme(p, which);
  if (got !== which) log('  ! theme wanted', which, 'got', got);
  return got;
}

const desktop = {
  home: { path: '/', run: async (p, S, themeName) => {
    await S.view('default');
    if (themeName === 'light') await S.full();
    await p.evaluate(() => scrollTo(0, 720));
    await wait(p, 400);
    await S.view('recipes');
  } },
  discover: { path: '/discover', run: async (p, S, themeName) => {
    await S.view('default');
    if (themeName === 'light') await S.full();
    const chip = p.getByRole('button', { name: 'Breakfast', exact: true }).first();
    if (await chip.count()) {
      await chip.click();
      await wait(p, 900);
      await S.view('filtered');
    }
  } },
  recipe: { path: RECIPE, run: async (p, S, themeName) => {
    await S.view('default');
    if (themeName === 'light') await S.full();
  } },
  search: { path: '/search?ingredients=apple', run: async (p, S) => { await S.view('default'); } },
  collection: { path: COLLECTION, run: async (p, S) => { await S.view('default'); } },
  team: { path: '/team', run: async (p, S, themeName) => {
    await S.view('default');
    if (themeName === 'light') await S.full();
    const menu = p.getByRole('button', { name: 'Menu' });
    if (await menu.count()) {
      await menu.click();
      await wait(p, 600);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    }
  } },
  roadmap: { path: '/roadmap', run: async (p, S) => { await S.view('default'); } },
  shop: { path: '/shop', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  signup: { path: '/signup', run: async (p, S) => {
    // Rest only. The form is visible; nothing is typed or submitted.
    await wait(p, 1500);
    await S.view('default');
  } },
  cookbook: { path: '/cookbook', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S, themeName) => {
    await S.view('default');
    if (themeName === 'light') await S.full();
  } },
  discover: { path: '/discover', run: async (p, S) => { await S.view('default'); } },
  recipe: { path: RECIPE, run: async (p, S) => { await S.view('default'); } },
  team: { path: '/team', run: async (p, S) => {
    await S.view('default');
    const menu = p.getByRole('button', { name: 'Menu' });
    if (await menu.count()) {
      await menu.click();
      await wait(p, 600);
      await S.view('menu');
    }
  } },
  signup: { path: '/signup', run: async (p, S) => { await wait(p, 1200); await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const spec = (mob ? mobile : desktop)[k];
  const themes = mob && k !== 'home' ? ['light'] : ['light', 'dark'];
  for (const themeName of themes) {
    const name = (mob ? 'mobile-' : '') + k + '-' + themeName;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k) && !pageArg.includes((mob ? 'mobile-' : '') + k)) continue;
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await b.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
    const p = await ctx.newPage();
    log(name);
    const S = new Shooter(p, name, vw, vh, dpr);
    try {
      await goto(p, spec.path);
      await theme(p, themeName);
      await spec.run(p, S, themeName);
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await b.close();
