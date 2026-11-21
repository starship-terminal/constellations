// Captures LinkedIn's public guest pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x, named
// mobile-*. Nothing is submitted. A control that lands on a login or signup
// wall is recorded and that branch stops. Consent banners are hidden, not
// clicked. Language menus are opened and closed, never changed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const walls = [];

async function hideConsent(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('#artdeco-global-alert-container, .artdeco-global-alert, [data-test-global-alert]')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 7200);
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
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
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
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function noteWall(p, from) {
  const url = p.url().split('?')[0];
  walls.push({ from, url });
  log('  WALL', from, '->', url);
}

async function clickRole(p, role, name) {
  const loc = p.getByRole(role, { name }).first();
  if (!(await loc.count())) return false;
  await loc.click({ timeout: 5000 });
  await wait(p, 700);
  return true;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('show-more-jobs', async () => {
      if (await clickRole(p, 'button', /show more jobs/i)) await S.view('jobs-expanded');
    });
    await step('language-menu', async () => {
      const lang = p.locator('button, [role=button]').filter({ hasText: /^Language$/ }).first();
      if (await lang.count()) {
        await lang.click();
        await wait(p, 600);
        await S.view('language-menu');
        await p.keyboard.press('Escape');
      }
    });
    await step('signin-hover', async () => {
      const a = p.getByRole('link', { name: 'Sign in', exact: true }).first();
      if (await a.count()) { await a.hover(); await wait(p, 300); await S.view('signin-hover'); }
    });
  } },
  'top-content': { path: '/top-content', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'top-content-career': { path: '/top-content/career/', run: async (p, S) => {
    await S.view('default');
    await step('share', async () => {
      const share = p.getByRole('button', { name: /^Share$/ }).first();
      if (await share.count()) { await share.click(); await wait(p, 600); await S.view('share'); await p.keyboard.press('Escape'); }
    });
  } },
  learning: { path: '/learning/', run: async (p, S) => {
    await S.view('default');
    await step('search-focus', async () => {
      const s = p.getByRole('combobox', { name: /skills, subjects/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 400); await S.view('search-focused'); }
    });
    await step('tab-technology', async () => {
      if (await clickRole(p, 'tab', /^Technology$/)) await S.view('tab-technology');
    });
  } },
  'learning-search': { path: '/learning/search', run: async (p, S) => { await S.view('default'); } },
  'jobs-engineering': { path: '/jobs/engineering-jobs', run: async (p, S) => {
    await S.view('default');
    await step('date-filter', async () => {
      if (await clickRole(p, 'button', /date posted/i)) await S.view('date-filter');
      await p.keyboard.press('Escape');
    });
    await step('filters-notice', async () => {
      if (await clickRole(p, 'button', /where are the filters/i)) await S.view('filters-notice');
    });
  } },
  games: { path: '/games', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'games-zip': { path: '/games/zip/', run: async (p, S) => { await S.view('default'); } },
  products: { path: '/products', run: async (p, S) => {
    await S.view('default');
    await step('search-focus', async () => {
      const s = p.getByRole('combobox', { name: /search products/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 400); await S.view('search-focused'); }
    });
  } },
  'products-category': { path: '/products/categories/e-commerce-platforms', run: async (p, S) => { await S.view('default'); } },
  services: { path: '/services', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { path: '/legal/user-agreement', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      if (await clickRole(p, 'button', /open navigation/i)) await S.view('nav-open');
    });
  } },
  privacy: { path: '/legal/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help/linkedin', run: async (p, S) => {
    await S.view('notice');
    await step('dismiss', async () => {
      const d = p.getByRole('button', { name: /dismiss/i }).first();
      if (await d.count()) { await d.click(); await wait(p, 500); }
      await S.view('default');
    });
    await step('menu', async () => {
      const m = p.getByRole('button', { name: /^LinkedIn$/ }).first();
      if (await m.count()) { await m.click(); await wait(p, 500); await S.view('product-menu'); }
    });
  } },
  accessibility: { path: '/accessibility', run: async (p, S) => { await S.view('default'); } },
  'top-companies': { path: '/hubs/top-companies', run: async (p, S) => { await S.view('default'); } },
  'company-jobs': { path: '/company/linkedin/jobs', run: async (p, S) => { await S.view('default'); } },
  directory: { path: '/directory/people', run: async (p, S) => { await S.view('default'); } },
  apps: { path: 'https://members.linkedin.com/apps', abs: true, run: async (p, S) => { await S.view('default'); } },
  about: { path: 'https://about.linkedin.com/', abs: true, run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', wall: true, run: async (p, S) => { await S.view('wall'); } },
  signup: { path: '/signup', wall: true, run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'top-content': { path: '/top-content', run: async (p, S) => { await S.view('default'); } },
  learning: { path: '/learning/', run: async (p, S) => { await S.view('default'); } },
  'jobs-engineering': { path: '/jobs/engineering-jobs', run: async (p, S) => { await S.view('default'); } },
  games: { path: '/games', run: async (p, S) => { await S.view('default'); } },
  products: { path: '/products', run: async (p, S) => { await S.view('default'); } },
  services: { path: '/services', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/legal/user-agreement', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => { if (await clickRole(p, 'button', /open navigation/i)) await S.view('nav-open'); });
  } },
  help: { path: '/help/linkedin', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', wall: true, run: async (p, S) => { await S.view('wall'); } },
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
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
    colorScheme: 'light',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.abs ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await hideConsent(p);
    const landed = p.url();
    if (!spec.wall && isWall(landed)) {
      await noteWall(p, name);
      await S.view('wall');
    } else {
      if (spec.wall) await noteWall(p, name);
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
fs.writeFileSync(path.join(RAW, 'walls.json'), JSON.stringify(walls, null, 2) + '\n');
log('done', total, 'screenshots ->', RAW);
await browser.close();
