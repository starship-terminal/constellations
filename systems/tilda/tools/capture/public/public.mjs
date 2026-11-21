// Captures tilda.cc public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/tilda/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Cookie banner is hidden, never
// answered. Login and registration are photographed and never filled.
import fs from 'fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems', 'tilda', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 24000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
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
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: null,
    };
    this.count = 0;
  }
  async view(name, source) {
    await closePromo(this.p);
    this.requested.sanitizedSourceUrl = source || null;
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full', source) {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(12000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    const f = `${RAW}/${this.prefix}-${name}`;
    this.requested.sanitizedSourceUrl = source || null;
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
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
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const PAGES = {
  home: '/',
  pricing: '/pricing/',
  features: '/en/features/',
  templates: '/tpls/',
  made: '/madeontilda/',
  faq: '/en/answers/',
  colors: '/colors/',
  ai: '/lp/ai/',
  sans: '/lp/tildasans/',
  terms: '/terms/',
  login: '/login/',
  registration: '/registration/',
};

async function openMore(p) {
  const hook = p.locator('.tmain-submenu__hooklink').first();
  if (!(await hook.count())) return false;
  await hook.click({ timeout: 4000 });
  await wait(p, 500);
  return true;
}

const b = await chromium.launch();
let total = 0;
const keys = Object.keys(PAGES);
for (const mob of [false, true]) {
  for (const k of keys) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
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
    const url = BASE + PAGES[k];
    const safe = url;
    log(name, url);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      if (!(await clearChallenge(p, { tries: 4, step: 800 }))) {
        log('  BLOCKED', url);
        await ctx.close();
        continue;
      }
      await wait(p, 1600);
      await closePromo(p);
      await S.view('default', safe);
      if (k === 'home') {
        if (await openMore(p)) await S.view('menu', safe);
        await p.keyboard.press('Escape').catch(() => {});
        const close = p.locator('.tmain-submenu__close').first();
        if (await close.count()) await close.click({ timeout: 2000 }).catch(() => {});
        await wait(p, 300);
      }
      if (k === 'faq' && !mob) {
        const cat = p.getByText('Domains', { exact: true }).first();
        if (await cat.count()) {
          await cat.click({ timeout: 4000 }).catch(() => {});
          await wait(p, 700);
          await S.view('category', safe);
        }
      }
      if (!['login', 'registration'].includes(k)) await S.full('full', safe);
    } catch (e) {
      log('  PAGE FAILED', name, e.message.split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, '->', RAW);
await b.close();
