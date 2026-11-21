// Captures Super.so's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a `mobile-` prefix.
// Super ships one theme, so there is no dark run. Desktop shots are 1440x900
// at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than
// one GPU texture is saved as name.partN.png tiles, which quantize.py stitches.
//
// Nothing is sent or signed into. The only presses are local UI: the header
// menus, the phone drawer, Load more, template filters, a search field filled
// with the word "portfolio" (cleared, never submitted), and a demo colour chip.
// Sign in, Get started, Google, Apple and passkey are not clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 150); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
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
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p, label) {
  const el = p.locator('[aria-expanded]').filter({ hasText: label }).first();
  await el.click();
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('use-cases-menu', async () => { await openMenu(p, 'Use cases'); await S.view('use-cases-menu'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await step('features-menu', async () => { await openMenu(p, 'Features'); await S.view('features-menu'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await step('nav-signin-hover', async () => {
      const a = p.locator('a.super-navbar__item', { hasText: 'Sign in' }).first();
      if (await a.count()) { await a.hover(); await wait(p, 300); await S.view('nav-signin-hover'); }
    });
    await step('cta-hover', async () => {
      const a = p.locator('a', { hasText: 'Get started for free' }).first();
      await a.scrollIntoViewIfNeeded();
      await a.hover();
      await wait(p, 300);
      await S.view('cta-hover');
    });
  } },
  templates: { path: '/templates', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('filter-menu', async () => {
      const b = p.getByRole('button', { name: 'any site' }).first();
      await b.click();
      await wait(p, 400);
      await S.view('filter-menu');
      await p.keyboard.press('Escape');
    });
    await step('search-focused', async () => {
      const input = p.locator('input').first();
      await input.click();
      await wait(p, 300);
      await S.view('search-focused');
      await input.fill('portfolio');
      await wait(p, 600);
      await S.view('search-filled');
      await input.fill('');
    });
    await step('category', async () => {
      const tab = p.locator('[data-tab="Website"]').first();
      if (await tab.count()) {
        await tab.evaluate((el) => el.click());
        await wait(p, 500);
        await S.view('category');
      }
    });
  } },
  pricing: { path: '/pricing-annual', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'pricing-monthly': { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  showcase: { path: '/showcase', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('load-more', async () => {
      const b = p.locator('.notion-collection-load-more').first();
      if (await b.count()) { await b.click(); await wait(p, 800); await S.view('load-more'); }
    });
  } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'feature-ai': { path: '/features/ai-chat', run: async (p, S) => { await S.view('default'); await S.full(); } },
  usecase: { path: '/use-cases/website', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('mono', async () => {
      const chip = p.getByText('Mono', { exact: true }).first();
      await chip.click();
      await wait(p, 500);
      await S.view('mono');
    });
  } },
  guides: { path: '/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  themes: { path: '/themes', run: async (p, S) => { await S.view('default'); } },
  icons: { path: '/icons', run: async (p, S) => { await S.view('default'); } },
  builder: { path: '/builder', run: async (p, S) => { await S.view('default'); } },
  community: { path: '/community', run: async (p, S) => { await S.view('default'); } },
  trial: { path: '/trial', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/da9e218bd10ad3ce28e44d60462b039a-super', run: async (p, S) => { await S.view('default'); } },
  docs: { path: 'https://docs.super.so/', abs: true, run: async (p, S) => { await S.view('default'); } },
  changelog: { path: 'https://changelog.super.so/', abs: true, run: async (p, S) => { await S.view('default'); } },
  status: { path: 'https://status.super.so/', abs: true, run: async (p, S) => { await S.view('default'); } },
  feedback: { path: 'https://feedback.super.so/', abs: true, run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://app.super.so/login', abs: true, run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      await p.locator('.super-navbar__menu-open').click({ force: true });
      await wait(p, 600);
      await S.view('menu');
      await p.locator('.super-navigation-menu__list-header', { hasText: 'Use cases' }).click({ force: true });
      await wait(p, 400);
      await S.view('menu-use-cases');
    });
  } },
  templates: { path: '/templates', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing-annual', run: async (p, S) => { await S.view('default'); await S.full(); } },
  usecase: { path: '/use-cases/website', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
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
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.abs ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(p, spec.wait || 1600);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
