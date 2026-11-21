// Captures letterboxd.com's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/letterboxd/raw-shots PLAYWRIGHT=… node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Full pages at CSS scale,
// truncated at 8 chunks. Nothing is typed, submitted, or signed into.
// Sign-in and create-account are photographed empty and left alone.

import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, FILM, LIST } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
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
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          ...opts(`${f}.part${i}.png`),
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
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

async function hideAds(p) {
  await p.addStyleTag({ content: 'iframe, .adsbygoogle, [id*="google_ads"], .ad-banner, #remove-ads-modal { visibility: hidden !important; }' }).catch(() => {});
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await hideAds(p);
    await S.view('default');
    await S.full();
    await step('search-focus', async () => {
      await p.locator('#search-q').click();
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape');
    });
  } },
  films: { url: BASE + '/films/', run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  film: { url: FILM, run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  lists: { url: BASE + '/lists/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  list: { url: LIST, run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  members: { url: BASE + '/members/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  journal: { url: BASE + '/journal/', run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about/', run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  pro: { url: BASE + '/pro/', run: async (p, S) => { await hideAds(p); await S.view('default'); await S.full(); } },
  apps: { url: BASE + '/apps/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  contact: { url: BASE + '/contact/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  welcome: { url: BASE + '/welcome/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  missing: { url: BASE + '/this-page-is-not-real-404/', run: async (p, S) => { await hideAds(p); await S.view('default'); } },
  signin: { url: BASE + '/sign-in/', run: async (p, S) => {
    await hideAds(p);
    await S.view('default');
  } },
  signup: { url: BASE + '/create-account/', run: async (p, S) => {
    await hideAds(p);
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await hideAds(p);
    await S.view('default');
    await step('menu', async () => {
      const b = p.locator('button, a').filter({ hasText: /^menu$/i }).first();
      if (await b.count()) {
        await b.click({ timeout: 3000 }).catch(() => {});
        await wait(p, 600);
        await S.view('menu');
      } else {
        log('  no phone menu control');
      }
    });
  } },
  film: { url: FILM, run: async (p, S) => { await hideAds(p); await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
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
  await ctx.route('**/*', (route) => {
    const u = route.request().url();
    if (/doubleclick|googlesyndication|google-analytics|adservice|adnxs|taboola|outbrain/i.test(u)) return route.abort();
    return route.continue();
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
