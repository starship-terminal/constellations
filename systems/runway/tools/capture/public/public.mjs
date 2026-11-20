// Captures Runway's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x. Names are {page}-light-{state}.png;
// mobile ones get a mobile- prefix. Runway's marketing site is light only.
// Nothing is submitted or signed into. Consent overlays are hidden, never clicked.
// Login, Try Runway, Google and Apple are not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, hideConsent, dismissBanner, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'runway', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
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

async function hoverNav(p, S, label) {
  const loc = p.locator('header a, nav a').filter({ hasText: new RegExp('^' + label + '$') }).first();
  await loc.hover({ timeout: 4000 });
  await wait(p, 700);
  const expanded = await loc.getAttribute('aria-expanded');
  if (expanded !== 'true') log('  menu not expanded', label, expanded);
  if (isWall(p.url())) { log('  WALL after hover', label, p.url()); return; }
  await S.view('menu-' + label.toLowerCase());
  await p.mouse.move(20, 860);
  await wait(p, 250);
}

const desktop = {
  home: { url: 'https://runway.com/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    for (const label of ['Creative', 'Dev', 'Robotics', 'Research', 'Resources', 'Enterprise']) {
      await step('menu-' + label, () => hoverNav(p, S, label));
    }
    await step('language', async () => {
      await p.getByRole('button', { name: /Change language|ENGLISH/i }).first().click();
      await wait(p, 600);
      await S.view('language');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('platform-tab', async () => {
      const b = p.getByRole('button', { name: 'Runway Dev', exact: true }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('tab-dev'); }
    });
  } },
  product: { url: 'https://runway.com/product', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: 'https://runway.com/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('yearly', async () => {
      const y = p.getByRole('button', { name: /^Yearly/ }).first();
      if (await y.count()) { await y.click(); await wait(p, 500); await S.view('yearly'); }
    });
    await step('api-tab', async () => {
      const t = p.getByRole('tab', { name: 'API' }).or(p.getByRole('button', { name: /^API$/ })).first();
      if (await t.count()) { await t.click(); await wait(p, 600); await S.view('api'); }
    });
  } },
  enterprise: { url: 'https://runway.com/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'enterprise-contact': { url: 'https://runway.com/enterprise-contact', run: async (p, S) => {
    await S.view('default');
    await step('field-focus', async () => {
      const f = p.locator('input[name="first_name"]');
      if (await f.count()) { await f.focus(); await wait(p, 300); await S.view('field-focus'); }
    });
  } },
  research: { url: 'https://runway.com/research', run: async (p, S) => { await S.view('default'); await S.full(); } },
  resources: { url: 'https://runway.com/resources', run: async (p, S) => { await S.view('default'); await S.full(); } },
  robotics: { url: 'https://runway.com/product/robotics', run: async (p, S) => { await S.view('default'); await S.full(); } },
  agent: { url: 'https://runway.com/product/agent', run: async (p, S) => { await S.view('default'); } },
  ads: { url: 'https://runway.com/product/ads', run: async (p, S) => { await S.view('default'); } },
  plugins: { url: 'https://runway.com/plugins', run: async (p, S) => { await S.view('default'); } },
  mcp: { url: 'https://runway.com/mcp', run: async (p, S) => { await S.view('default'); } },
  workflows: { url: 'https://runway.com/workflows', run: async (p, S) => { await S.view('default'); } },
  'team-plan': { url: 'https://runway.com/team-plan', run: async (p, S) => { await S.view('default'); } },
  'use-cases': { url: 'https://runway.com/use-cases', run: async (p, S) => { await S.view('default'); } },
  aleph: { url: 'https://runway.com/product/aleph-2', run: async (p, S) => { await S.view('default'); } },
  characters: { url: 'https://runway.com/product/characters', run: async (p, S) => { await S.view('default'); } },
  news: { url: 'https://runway.com/news', run: async (p, S) => { await S.view('default'); } },
  about: { url: 'https://runway.com/about', run: async (p, S) => { await S.view('default'); } },
  careers: { url: 'https://runway.com/careers', run: async (p, S) => { await S.view('default'); } },
  safety: { url: 'https://runway.com/safety', run: async (p, S) => { await S.view('default'); } },
  changelog: { url: 'https://runway.com/changelog', run: async (p, S) => { await S.view('default'); } },
  'data-security': { url: 'https://runway.com/data-security', run: async (p, S) => { await S.view('default'); } },
  educators: { url: 'https://runway.com/educators', run: async (p, S) => { await S.view('default'); } },
  studios: { url: 'https://runway.com/studios', run: async (p, S) => { await S.view('default'); } },
  'brand-guidelines': { url: 'https://runway.com/brand-guidelines', run: async (p, S) => { await S.view('default'); } },
  terms: { url: 'https://runway.com/terms-of-use', run: async (p, S) => { await S.view('default'); } },
  dev: { url: 'https://dev.runwayml.com/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'dev-models': { url: 'https://dev.runwayml.com/models', run: async (p, S) => { await S.view('default'); } },
  docs: { url: 'https://docs.dev.runwayml.com/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const s = p.getByRole('button', { name: /search/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 700); if (!isWall(p.url())) await S.view('search'); await p.keyboard.press('Escape'); }
    });
  } },
  academy: { url: 'https://academy.runwayml.com/', run: async (p, S) => { await S.view('default'); } },
  help: { url: 'https://help.runwayml.com/hc/en-us', run: async (p, S) => { await S.view('default'); } },
  status: { url: 'https://status.runwayml.com/', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://app.runwayml.com/login', wall: true, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: 'https://runway.com/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Menu' });
      await b.click();
      await wait(p, 700);
      await S.view('menu');
    });
  } },
  product: { url: 'https://runway.com/product', run: async (p, S) => { await S.view('default'); } },
  pricing: { url: 'https://runway.com/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { url: 'https://runway.com/enterprise', run: async (p, S) => { await S.view('default'); } },
  research: { url: 'https://runway.com/research', run: async (p, S) => { await S.view('default'); } },
  dev: { url: 'https://dev.runwayml.com/', run: async (p, S) => { await S.view('default'); } },
  docs: { url: 'https://docs.dev.runwayml.com/', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://app.runwayml.com/login', wall: true, run: async (p, S) => { await S.view('default'); } },
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
  });
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    log('  status', resp && resp.status(), 'final', p.url());
    await wait(p, spec.wall ? 2500 : 2200);
    await hideConsent(p);
    if (!spec.wall) await dismissBanner(p);
    if (isWall(p.url()) && !spec.wall) {
      log('  WALL unexpected', p.url());
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
