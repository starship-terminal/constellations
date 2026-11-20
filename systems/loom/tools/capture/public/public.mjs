// Captures Loom's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Names are {page}-light-{state}.png.
// The OneTrust banner is hidden. Reject, Accept and Manage preferences are never clicked.
// Sign-in buttons, SSO, signup Continue, Contact Sales, checkout and record CTAs are never pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, SHARE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
  await wait(p, 500);
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

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  await btn.click({ timeout: 4000 });
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('apps-menu', async () => {
      const btn = p.locator('header button, nav button').filter({ hasText: /^Apps$/ }).first();
      const open = await btn.getAttribute('aria-expanded', { timeout: 4000 }).catch(() => null);
      if (open !== 'true') await btn.click({ timeout: 4000 });
      await wait(p, 400);
      await S.view('apps-menu');
      await p.keyboard.press('Escape');
      await wait(p, 250);
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('billing-toggle', async () => {
      const sw = p.getByRole('switch').first();
      if (await sw.count()) {
        await sw.click();
        await wait(p, 500);
        await S.view('annual');
        await sw.click();
        await wait(p, 300);
      } else log('  no billing switch');
    });
    await step('faq', async () => {
      const q = p.locator('button, summary, [role="button"]').filter({ hasText: /what|how|can i/i }).first();
      if (await q.count()) {
        await q.scrollIntoViewIfNeeded();
        await q.click();
        await wait(p, 400);
        await S.view('faq');
      }
    });
    await S.full();
  } },
  login: { path: '/login', run: async (p, S) => {
    await S.view('default');
    await step('email-focused', async () => {
      const field = p.locator('input[type="email"], input[name="email"], input[type="text"]').first();
      await field.click({ timeout: 4000 });
      await wait(p, 250);
      await S.view('email-focused');
      await field.fill('capture@example.com');
      await wait(p, 200);
      await S.view('email-filled');
      await field.fill('');
    });
  } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'use-case': { path: '/use-case', run: async (p, S) => { await S.view('default'); } },
  desktop: { path: '/desktop', run: async (p, S) => { await S.view('default'); } },
  customers: { path: '/customers', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/legal', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/this-route-does-not-exist-loom-capture', run: async (p, S) => { await S.view('default'); } },
  share: { url: SHARE, run: async (p, S) => {
    await S.view('default');
    await step('player', async () => {
      const play = p.getByRole('button', { name: /play/i }).first();
      if (await play.count() && await play.isVisible().catch(() => false)) {
        await play.click();
        await wait(p, 800);
        await S.view('playing');
        const pause = p.getByRole('button', { name: /pause/i }).first();
        if (await pause.count()) await pause.click().catch(() => {});
      }
    });
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.getByRole('button', { name: /menu|navigation|open/i }).first();
      if (await btn.count()) {
        await btn.click();
        await wait(p, 500);
        await S.view('menu');
        await p.keyboard.press('Escape').catch(() => {});
      }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  share: { url: SHARE, run: async (p, S) => { await S.view('default'); } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); } },
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
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    const hide = () => document.querySelectorAll('#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter').forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
    });
    const start = () => new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    if (document.documentElement) start();
    else document.addEventListener('DOMContentLoaded', start);
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url || (BASE + spec.path), { waitUntil: 'domcontentloaded', timeout: 70000 });
    await wait(p, spec.wait || 2200);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
