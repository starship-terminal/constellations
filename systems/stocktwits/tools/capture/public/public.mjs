// Captures Stocktwits public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [name,name,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, names prefixed mobile-.
// Consent is hidden, never accepted. Login and signup are recorded and not
// filled. No form is submitted. Apple, Google, Facebook and X are not clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'stocktwits', 'raw-shots');
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
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
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
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function dismissExperience(p) {
  const open = await p.getByRole('heading', { name: 'Choose Your Experience' }).count().catch(() => 0);
  if (!open) return;
  await p.keyboard.press('Escape');
  await wait(p, 250);
  await p.mouse.click(1100, 760);
  await wait(p, 200);
}

async function gotoPath(p, pathName) {
  const resp = await p.goto(BASE + pathName, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 2500);
  await hideConsent(p);
  const title = await p.title();
  const challenged = /just a moment|security verification|attention required/i.test(title);
  const status = resp && resp.status();
  if (challenged || (status && status >= 400)) log('  blocked', pathName, status, title.slice(0, 60));
  return { status, challenged, title, url: p.url() };
}

async function clickTickerAll(p) {
  await p.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => {
      const r = el.getBoundingClientRect();
      return (el.innerText || '').trim() === 'All' && r.top > 30 && r.top < 120 && r.height < 40;
    });
    if (b) b.setAttribute('data-st', 'ticker-all');
  });
  const b = p.locator('[data-st="ticker-all"]');
  if (!(await b.count())) return false;
  await b.click();
  await wait(p, 700);
  return true;
}

async function clickByText(p, tag, text) {
  const ok = await p.evaluate(({ tag, text }) => {
    const el = [...document.querySelectorAll(tag)].find((node) => (node.innerText || '').trim() === text);
    if (!el) return false;
    el.setAttribute('data-st', 'click');
    return true;
  }, { tag, text });
  if (!ok) return false;
  await p.locator('[data-st="click"]').click();
  await p.evaluate(() => document.querySelector('[data-st="click"]')?.removeAttribute('data-st'));
  return true;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('consent');
    await hideConsent(p);
    await S.view('default');
    await S.full();
    await step('experience', async () => {
      const btn = p.locator('button').filter({ has: p.locator('svg.fa-chevron-down') }).first();
      await btn.click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('experience');
      await dismissExperience(p);
    });
    await step('search', async () => {
      await p.locator('input[name="desktopSearch"]').click({ timeout: 5000 });
      await wait(p, 700);
      await S.view('search');
      await p.keyboard.press('Escape');
    });
    await step('ticker-filter', async () => {
      await dismissExperience(p);
      if (await clickTickerAll(p)) await S.view('ticker-filter');
      await p.keyboard.press('Escape');
    });
    await step('ticker-paused', async () => {
      await p.getByRole('button', { name: 'Pause trending ticker animation' }).click({ timeout: 5000 });
      await wait(p, 400);
      await S.view('ticker-paused');
    });
    await step('following', async () => {
      if (await clickByText(p, 'button', 'Following')) {
        await wait(p, 900);
        await S.view('following');
      }
    });
    await step('reply-wall', async () => {
      const before = p.url();
      await dismissExperience(p);
      await p.getByRole('button', { name: 'Reply', exact: true }).first().click({ timeout: 5000 });
      await wait(p, 1500);
      log('  reply url', p.url());
      if (isWall(p.url()) || p.url() !== before) await S.view('reply-wall');
      if (isWall(p.url())) log('  wall, stop branch', p.url());
    });
  } },
  sentiment: { path: '/sentiment', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'sentiment-trending': { path: '/sentiment/trending', run: async (p, S) => { await S.view('default'); } },
  'sentiment-calendar': { path: '/sentiment/calendar', run: async (p, S) => { await S.view('default'); await S.full(); } },
  news: { path: '/news-articles', run: async (p, S) => { await S.view('default'); await S.full(); } },
  symbol: { path: '/symbol/AAPL', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('chart', async () => {
      const b = p.getByRole('button', { name: /Full Chart|Expand full chart/i }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 1200);
        await S.view('chart');
        await p.keyboard.press('Escape');
      }
    });
    await step('about-more', async () => {
      const b = p.getByRole('button', { name: /Show more about/i }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 500);
        await S.view('about-more');
      }
    });
    await step('button-hover', async () => {
      const b = p.getByRole('link', { name: 'Sign Up' }).first();
      if (await b.count()) { await b.hover(); await wait(p, 300); await S.view('signup-hover'); }
    });
  } },
  'symbol-news': { path: '/symbol/AAPL/news', run: async (p, S) => { await S.view('default'); } },
  'symbol-sentiment': { path: '/symbol/AAPL/sentiment', run: async (p, S) => { await S.view('default'); } },
  'symbol-earnings': { path: '/symbol/AAPL/earnings', run: async (p, S) => { await S.view('default'); } },
  'symbol-about': { path: '/symbol/AAPL/about', run: async (p, S) => { await S.view('default'); } },
  'symbol-directory': { path: '/symbol', run: async (p, S) => { await S.view('default'); await S.full(); } },
  coins: { path: '/coins', run: async (p, S) => { await S.view('default'); } },
  bitcoin: { path: '/coins/bitcoin', run: async (p, S) => { await S.view('default'); await S.full(); } },
  discussions: { path: '/discussions', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  subscriptions: { path: '/subscriptions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); } },
  widgets: { path: '/widgets', run: async (p, S) => { await S.view('default'); } },
  newsletters: { path: '/newsletters', run: async (p, S) => { await S.view('default'); } },
  rules: { path: '/about/rules', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/about/legal/privacy', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/signin', run: async (p, S) => {
    await S.view('default');
    await step('login-focus', async () => {
      const field = p.locator('input[name="login"]');
      if (await field.count()) {
        await field.focus();
        await wait(p, 300);
        await S.view('login-focus');
      }
    });
    log('  wall recorded, no credentials typed', p.url());
  } },
  signup: { path: '/signup', run: async (p, S) => {
    await S.view('default');
    log('  wall recorded, no email typed', p.url());
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await hideConsent(p);
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const btn = p.locator('button').first();
      await btn.click();
      await wait(p, 700);
      await S.view('menu');
    });
  } },
  sentiment: { path: '/sentiment', run: async (p, S) => { await S.view('default'); } },
  news: { path: '/news-articles', run: async (p, S) => { await S.view('default'); } },
  symbol: { path: '/symbol/AAPL', run: async (p, S) => { await S.view('default'); await S.full(); } },
  bitcoin: { path: '/coins/bitcoin', run: async (p, S) => { await S.view('default'); } },
  subscriptions: { path: '/subscriptions', run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/signin', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({
  headless: true,
  args: ['--disable-blink-features=AutomationControlled'],
});
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const opened = await gotoPath(p, spec.path);
    if (!opened.challenged) await spec.run(p, S);
    else log('  skipped interactions, challenge page');
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
