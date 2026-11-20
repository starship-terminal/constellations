// Captures masterclass.com's public signed-out pages into RAW.
//
//   RAW=/some/scratch PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Consent overlays are hidden,
// never clicked. Nothing is signed into, purchased, or submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

// Full-colour shots go outside the repo (the kit's default), never into systems/ or the repo root.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'masterclass', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 24; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h === last && i > 2) break;
    last = h;
    const y = Math.min(i * 700, Math.max(0, h - 800));
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Bounded: at most 8 viewport tiles (AGENTS.md "Bound every full-page capture").
    const MAXH = Math.min(8 * chunk, 8 * this.p.viewportSize().height);
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    // Always clip to the configured viewport width. fullPage uses document width,
    // which at deviceScaleFactor 2 produced a PNG half as wide as the check expected.
    const tile = async (file, y, height) => {
      await p.evaluate((yy) => scrollTo(0, yy), y);
      await wait(p, 200);
      await screenshotWithMetadata(p, { path: file }, this.requested);
    };
    if (hCap <= this.p.viewportSize().height) await tile(f + '.png', 0, hCap);
    else for (let i = 0, y = 0; y < hCap; i++, y += this.p.viewportSize().height) {
      await tile(`${f}.part${i}.png`, y, Math.min(this.p.viewportSize().height, hCap - y));
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('browse', async () => {
      const b = p.locator('header button').filter({ hasText: /^Browse$/ }).first();
      if (await b.count()) {
        await b.click({ timeout: 5000 });
        await wait(p, 900);
        await S.view('browse');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      }
    });
    await S.full();
  } },
  class: { path: '/classes/revolutionize-your-workflows-with-ai', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  checkout: { path: '/checkout', wait: 5000, run: async (p, S) => {
    await S.view('default');
    // Plan Select on /checkout is not clicked: it changes checkout state on the live site.
    // The plans are shot at rest; a selected plan is a boundary, not captured.
    await step('faq', async () => {
      const q = p.locator('button').filter({ hasText: /What is MasterClass/i }).first();
      if (await q.count()) {
        await q.click({ timeout: 5000 });
        await wait(p, 500);
        await S.view('faq');
      }
    });
    await S.full();
  } },
  login: { path: '/auth/login', wait: 4000, run: async (p, S) => { await S.view('default'); } },
  categories: { path: '/categories', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  gift: { path: '/gift', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  business: { path: '/for-business', wait: 4500, run: async (p, S) => { await S.view('default'); await S.full(); } },
  quiz: { path: '/find-my-classes', wait: 4000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button').filter({ hasText: /^Menu$/ }).first();
      const alt = p.locator('header button[aria-label*="menu" i], header button[aria-label*="Menu" i]').first();
      const btn = (await m.count()) ? m : alt;
      if (await btn.count()) {
        await btn.click({ timeout: 5000 });
        await wait(p, 900);
        await S.view('menu');
      }
    });
    await S.full();
  } },
  class: { path: '/classes/revolutionize-your-workflows-with-ai', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  checkout: { path: '/checkout', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  // Automation is not hidden (no webdriver mask): a bot check is recorded as a boundary, not bypassed.
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 4000);
    await hideConsent(p);
    const title = await p.title();
    const url = p.url();
    log('  landed', url, title);
    if (/just a moment|attention required|verify you are human/i.test(title)) {
      log('  BLOCKED challenge', spec.path);
      await ctx.close();
      continue;
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
