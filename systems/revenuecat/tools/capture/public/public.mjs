// Captures RevenueCat's public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/revenuecat/raw-shots PLAYWRIGHT=... node public.mjs [name,name]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Nothing is submitted, typed into a
// login, signup, newsletter or contact field, or accepted on a consent banner.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'revenuecat', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
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
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
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
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  await btn.click({ timeout: 5000 });
  await wait(p, 600);
}

async function closeMenu(p) {
  await p.keyboard.press('Escape');
  await p.mouse.move(8, 860);
  await wait(p, 250);
}

const desktopPages = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    for (const name of ['Why RevenueCat?', 'Solutions', 'Developers', 'Resources']) {
      await step('menu-' + name, async () => {
        await openMenu(p, name);
        const slug = name.toLowerCase().replace(/[^a-z]+/g, '-').replace(/-$/, '');
        await S.view('menu-' + slug);
        await closeMenu(p);
      });
    }
    await step('locale', async () => {
      const b = p.locator('header button, nav button').filter({ hasText: /Eng/ }).first();
      if (await b.count()) {
        await b.click({ timeout: 4000 });
        await wait(p, 500);
        await S.view('locale-menu');
        await p.keyboard.press('Escape');
      }
    });
    await step('testimonial', async () => {
      const b = p.getByRole('button', { name: 'Go to Photoroom testimonial' });
      if (await b.count()) {
        await b.first().click();
        await wait(p, 700);
        await p.evaluate(() => scrollTo(0, 9600));
        await wait(p, 400);
        await S.view('testimonial');
        await p.evaluate(() => scrollTo(0, 0));
      }
    });
    await step('primary-hover', async () => {
      const a = p.getByRole('link', { name: 'Sign up' }).first();
      await a.hover();
      await wait(p, 300);
      await S.view('signup-hover');
    });
    await step('primary-focus', async () => {
      await p.keyboard.press('Tab');
      await wait(p, 200);
      await S.view('focus');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    for (const tab of ['All features', 'Testimonials', 'FAQs']) {
      await step('tab-' + tab, async () => {
        const b = p.getByRole('button', { name: tab, exact: true }).first();
        if (!(await b.count())) return;
        await b.click();
        await wait(p, 600);
        await S.view('tab-' + tab.toLowerCase().replace(/[^a-z]+/g, '-'));
      });
    }
  } },
  'why-revenuecat': { path: '/why-revenuecat', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'build-vs-buy': { path: '/build-vs-buy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-developers': { path: '/for-developers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-enterprise': { path: '/for-enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  indies: { path: '/indies', run: async (p, S) => { await S.view('default'); } },
  paywalls: { path: '/feature/paywalls', run: async (p, S) => { await S.view('default'); await S.full(); } },
  charts: { path: '/feature/charts', run: async (p, S) => { await S.view('default'); } },
  experiments: { path: '/feature/experiments', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'integrations-stripe': { path: '/integrations/stripe', run: async (p, S) => { await S.view('default'); } },
  testimonials: { path: '/testimonials', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-openai': { path: '/customers/openai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.getByRole('button', { name: 'SEARCH', exact: true }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 500);
        await S.view('search-open');
        await p.keyboard.press('Escape');
      }
    });
  } },
  'talk-to-sales': { path: '/talk-to-sales', run: async (p, S) => {
    await S.view('default');
    await step('select-open', async () => {
      const b = p.getByRole('button', { name: /What would you like to discuss/ }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 500);
        await S.view('select-open');
        await p.keyboard.press('Escape');
      }
    });
  } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.getByRole('button', { name: /Search/ }).first();
      await b.click({ timeout: 5000 });
      await wait(p, 700);
      await S.view('search-open');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('dark', async () => {
      const b = p.getByRole('button', { name: /dark and light/i }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 700);
        await S.view('dark');
      }
    });
  } },
  'docs-overview': { path: '/docs/welcome/overview', run: async (p, S) => {
    await S.view('default');
    await step('sidebar', async () => {
      const b = p.getByRole('button', { name: /Projects & Apps/ }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 500);
        await S.view('sidebar-open');
      }
    });
  } },
  changelog: { path: '/changelog', run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const b = p.getByRole('button', { name: 'SDK', exact: true }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 600);
        await S.view('filter-sdk');
      }
    });
  } },
  glossary: { path: '/glossary', run: async (p, S) => {
    await S.view('default');
    await step('letter', async () => {
      const b = p.getByRole('button', { name: 'P', exact: true }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 500);
        await S.view('letter-p');
      }
    });
  } },
  calculator: { path: '/app-store-fee-calculator', run: async (p, S) => { await S.view('default'); } },
  events: { path: '/events', run: async (p, S) => { await S.view('default'); } },
  'press-kit': { path: '/press-kit', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  status: { url: 'https://status.revenuecat.com/', run: async (p, S) => { await S.view('default'); } },
  'login-wall': { url: 'https://app.revenuecat.com/login', run: async (p, S) => { await S.view('default'); } },
  'signup-wall': { url: 'https://app.revenuecat.com/signup', run: async (p, S) => { await S.view('default'); } },
};

const mobilePages = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Menu', exact: true }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 700);
        await S.view('menu-open');
        await p.keyboard.press('Escape');
      }
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  paywalls: { path: '/feature/paywalls', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  'talk-to-sales': { path: '/talk-to-sales', run: async (p, S) => { await S.view('default'); } },
  testimonials: { path: '/testimonials', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktopPages).map((k) => ({ k, mob: false })),
  ...Object.keys(mobilePages).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobilePages : desktopPages)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
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
    const url = spec.url || (BASE + spec.path);
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await wait(p, spec.wait || 2200);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
