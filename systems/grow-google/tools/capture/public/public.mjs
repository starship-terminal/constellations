// Captures Grow with Google's public pages into RAW (full-colour PNGs).
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a `mobile-` prefix.
// One theme only: color-scheme is normal, no dark toggle was found.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x.
// Nothing is submitted, signed into, or typed into a form.
// PRODUCT (adapt): Grow with Google public site, 2026-11-21.
const ADAPTED_FOR = 'grow-google';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'grow-google', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function dismissCookies(p) {
  const labels = [/reject all/i, /only necessary/i, /decline/i, /accept all/i, /i agree/i, /got it/i];
  for (const re of labels) {
    const b = p.getByRole('button', { name: re }).first();
    if (await b.count() && await b.isVisible().catch(() => false)) {
      await b.click().catch(() => {});
      await wait(p, 500);
      return;
    }
  }
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
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
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 6 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).locator('[aria-haspopup="true"], [aria-expanded]').first();
  const fallback = p.locator(`button[aria-haspopup="true"]`).filter({ hasText: name }).first();
  const target = (await btn.count()) ? btn : fallback;
  await target.click();
  await wait(p, 700);
}

const desktop = {
  'apac-home': { path: '/intl/en_sg/', run: async (p, S) => {
    await S.view('default');
    await step('carousel-next', async () => {
      const n = p.getByRole('button', { name: /next page/i }).first();
      if (await n.count()) { await n.click(); await wait(p, 700); await S.view('carousel-next'); }
    });
    await step('about', async () => {
      const b = p.getByRole('button', { name: /About Grow with Google/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('about'); }
    });
    await S.full();
  } },
  'apac-majulah': { path: '/intl/en_sg/majulah-ai/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-skills': { path: '/intl/en_sg/skillsignitionsg/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-stories': { path: '/intl/en_sg/stories/', run: async (p, S) => {
    await S.view('default');
    await step('tab-2', async () => {
      const t = p.getByRole('button', { name: /tab 2 of 3/i }).first();
      if (await t.count()) { await t.click(); await wait(p, 600); await S.view('tab-2'); }
    });
    await S.full();
  } },
  'apac-tools': { path: '/intl/en_sg/use-tools/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-learn': { path: '/intl/en_sg/learn-skills/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-gemini': { path: '/intl/en_sg/gemini-report/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-redeem': { path: '/intl/en_sg/redeem-google-ai-pro/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-ai-pro': { path: '/intl/en_sg/ai-professional/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-challenge': { path: '/intl/en_sg/ai-challenge/', run: async (p, S) => { await S.view('default'); } },
  'us-certificates': { path: '/certificates', run: async (p, S) => {
    await S.view('default');
    await step('nav-career', async () => { await openMenu(p, 'Career Certificates'); await S.view('nav-career'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await step('nav-ai', async () => { await openMenu(p, 'AI Training'); await S.view('nav-ai'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await S.full();
  } },
  'us-cert-data': { path: '/certificates/data-analytics/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'us-ai': { path: '/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'us-stories': { path: '/stories/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'us-career': { path: '/grow-your-career/', run: async (p, S) => { await S.view('default'); } },
  'us-article': { path: '/grow-your-career/articles/what-is-vibe-coding/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'us-employers': { path: '/employers/', run: async (p, S) => { await S.view('default'); } },
  'us-sitemap': { path: '/sitemap', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'us-404': { path: '/intl/en/', run: async (p, S) => { await S.view('default'); } },
  'root-redirect': { path: '/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  'apac-home': { path: '/intl/en_sg/', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      const burger = p.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], button.glue-header__drawer-toggle, [class*="hamburger"]').first();
      if (await burger.count() && await burger.isVisible().catch(() => false)) {
        await burger.click();
        await wait(p, 700);
        await S.view('nav-open');
      }
    });
    await S.full();
  } },
  'apac-stories': { path: '/intl/en_sg/stories/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apac-tools': { path: '/intl/en_sg/use-tools/', run: async (p, S) => { await S.view('default'); } },
  'apac-learn': { path: '/intl/en_sg/learn-skills/', run: async (p, S) => { await S.view('default'); } },
  'us-certificates': { path: '/certificates', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      const burger = p.locator('button[aria-label*="menu" i], button[aria-expanded]').first();
      if (await burger.count() && await burger.isVisible().catch(() => false)) {
        await burger.click();
        await wait(p, 800);
        await S.view('nav-open');
      }
    });
    await S.full();
  } },
  'us-cert-data': { path: '/certificates/data-analytics/', run: async (p, S) => { await S.view('default'); } },
  'us-article': { path: '/grow-your-career/articles/what-is-vibe-coding/', run: async (p, S) => { await S.view('default'); } },
  'us-404': { path: '/intl/en/', run: async (p, S) => { await S.view('default'); } },
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
    locale: 'en-SG',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    await dismissCookies(p);
    log('  status', res?.status(), 'url', p.url().split('?')[0]);
    const wall = await p.evaluate(() => /enter your password|verify it.?s you|sign in to continue/i.test(document.body.innerText || ''));
    if (wall) { log('  LOGIN WALL', p.url()); await S.view('login-wall'); }
    else await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
