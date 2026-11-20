// Captures lego.com public surfaces into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x, mobile 390x844 at 2x. Consent is hidden, never
// answered. Add to Bag, Sign In, checkout and the email field are never used.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, withGate } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lego', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 7200);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 160); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, scale: 'css' }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, scale: 'css', clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}

const desktop = {
  home: { url: BASE + '/en-us', shot: 'home' },
  theme: { url: BASE + '/en-us/themes/city', shot: 'theme' },
  bestsellers: { url: BASE + '/en-us/categories/bestsellers', shot: 'bestsellers' },
  product: { url: BASE + '/en-us/product/dump-truck-front-end-loader-60494', shot: 'product' },
  offers: { url: BASE + '/en-us/page/lego-offers-promotions', shot: 'offers' },
  service: { url: BASE + '/en-us/service', shot: 'service' },
  about: { url: BASE + '/en-us/aboutus', shot: 'about' },
  search: { url: BASE + '/en-us/search?q=city', shot: 'search' },
};

const mobile = {
  home: { url: BASE + '/en-us', shot: 'home' },
  theme: { url: BASE + '/en-us/themes/city', shot: 'theme' },
  product: { url: BASE + '/en-us/product/dump-truck-front-end-loader-60494', shot: 'product' },
};

const b = await chromium.launch({ headless: true });
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
  const url = withGate(spec.url);
  const S = new Shooter(p, `${mob ? 'mobile-' : ''}${spec.shot}`, vw, vh, dpr, url.split('?')[0]);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED', url); await ctx.close(); continue; }
    await wait(p, 4500);
    await closePromo(p);
    await S.view('default');
    await S.full();
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
