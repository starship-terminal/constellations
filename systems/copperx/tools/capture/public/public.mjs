// Captures Copperx's signed-out marketing pages.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x, mobile 390x844 at 2x. Full-colour shots go to
// ~/.design-systems/copperx/raw-shots. Consent overlays are hidden, never clicked.
// Log in and Get Started open an account-choice dialog; the dialog is photographed
// and closed. Its links (dashboard.copperx.io, payout.copperx.io) are not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function assertNotChallenge(p) {
  const title = await p.title();
  const body = await p.evaluate(() => (document.body && document.body.innerText || '').slice(0, 500));
  if (/just a moment|verify you are human|cf-challenge|attention required/i.test(title + ' ' + body)) {
    throw new Error('cloudflare challenge on ' + p.url());
  }
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
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
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
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

async function openAccountDialog(p) {
  const btn = p.locator('button.btn-light').filter({ hasText: 'Log in' }).first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 4000 });
  await wait(p, 700);
  const open = await p.evaluate(() => /Choose your account/.test(document.body.innerText));
  return open;
}

async function closeDialog(p) {
  await p.keyboard.press('Escape');
  await wait(p, 300);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const login = p.locator('button.btn-light').filter({ hasText: 'Log in' }).first();
    if (await login.count()) {
      await login.hover();
      await wait(p, 350);
      await S.view('login-hover');
    }
    if (await openAccountDialog(p)) {
      await S.view('account-dialog');
      await closeDialog(p);
    }
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gateway: { path: '/crypto-payment-gateway', run: async (p, S) => { await S.view('default'); } },
  banking: { path: '/personal-banking', run: async (p, S) => { await S.view('default'); } },
  cards: { path: '/credit-cards', run: async (p, S) => { await S.view('default'); } },
  payout: { path: '/payout', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const menu = p.locator('header button, button').filter({ hasText: /^$/ }).locator('svg').first();
    const burger = p.locator('header button').last();
    if (await burger.count()) {
      await burger.click({ timeout: 3000 }).catch(() => {});
      await wait(p, 500);
      await S.view('menu-open');
      await p.keyboard.press('Escape').catch(() => {});
    }
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); } },
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
    locale: 'en-US',
  });
  // automation flag: left as the browser sets it (navigator.webdriver is not masked).
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 45000 });
    log('  status', res && res.status(), p.url());
    await wait(p, spec.wait || 1600);
    await assertNotChallenge(p);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
    if (/cloudflare/i.test(e.message)) {
      await ctx.close();
      await b.close();
      process.exit(3);
    }
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
