// Captures Maze's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x and get a
// mobile- prefix. *-full shots are 1x. Nothing is submitted. CookieYes is
// hidden, never accepted. auth.maze.co is never opened.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
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
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) {
      try {
        await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
      } catch (e) {
        if (!String(e.message || e).includes('dimension mismatch')) throw e;
        log('  ! full-page height shifted, saving viewport instead');
        await screenshotWithMetadata(p, { path: f + '.png' }, this.requested);
      }
    }
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function gotoPublic(page, urlPath) {
  const url = urlPath.startsWith('http') ? urlPath : BASE + urlPath;
  if (isWall(url)) { log('  WALL skip', url); return false; }
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await wait(page, 1800);
  const status = res ? res.status() : 0;
  const blocked = await page.evaluate(() => /sorry, you have been blocked|just a moment|verify you are human/i.test(document.body?.innerText || '')).catch(() => false);
  if (status >= 400 || blocked || isWall(page.url())) {
    log('  STOP', status, page.url(), blocked ? 'blocked' : '');
    return false;
  }
  return true;
}

const PAGES = {
  home: { path: '/', run: async (p, S, mobile) => {
    await S.view('consent');
    await hideConsent(p);
    await wait(p, 400);
    await S.view('default');
    await S.full();
    if (!mobile) {
      await step('platform-menu', async () => {
        const box = await p.evaluate(() => {
          const header = document.querySelector('header');
          const pricing = [...header.querySelectorAll('a')].find((a) => (a.innerText || '').trim() === 'PRICING');
          const row = pricing.closest('div')?.parentElement?.parentElement;
          const el = [...row.children].find((c) => (c.innerText || '').trim() === 'PLATFORM');
          const r = el.getBoundingClientRect();
          return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
        });
        await p.mouse.move(box.x, box.y);
        await wait(p, 700);
        await S.view('platform-menu');
        await p.mouse.move(10, 400);
        await wait(p, 300);
      });
      await step('stage-tab', async () => {
        const btn = p.getByRole('button', { name: 'DECIDE', exact: true });
        if (await btn.count()) {
          await btn.first().click();
          await wait(p, 600);
          await S.view('stage-decide');
        }
      });
    } else {
      await step('nav-open', async () => {
        const b = p.getByRole('button', { name: /open navigation/i });
        if (await b.count()) {
          await b.first().click();
          await wait(p, 700);
          await S.view('nav-open');
          await p.keyboard.press('Escape').catch(() => {});
        }
      });
    }
  } },
  pricing: { path: '/pricing/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  platform: { path: '/platform/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  ai: { path: '/ai/', run: async (p, S) => {
    await hideConsent(p);
    await S.view('default');
    await step('tab', async () => {
      const b = p.getByRole('button', { name: 'AI ANALYSIS', exact: true });
      if (await b.count()) { await b.first().click(); await wait(p, 500); await S.view('tab-analysis'); }
    });
    await S.full();
  } },
  demo: { path: '/demo/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'prototype-testing': { path: '/features/prototype-testing/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'use-case': { path: '/use-cases/wireframe-and-usability-testing/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  industry: { path: '/industry/tech/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  role: { path: '/roles/product-designers/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  integrations: { path: '/integrations/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  figma: { path: '/integrations/figma/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  customers: { path: '/customers/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'customer-lcs': { path: '/customers/lcs/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  blog: { path: '/blog/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  article: { path: '/blog/research-influence/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  templates: { path: '/templates/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  template: { path: '/templates/usability-testing-a-new-product/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  guides: { path: '/guides/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  collections: { path: '/collections/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  compare: { path: '/compare/', run: async (p, S) => {
    await hideConsent(p);
    await S.view('default');
    await step('show-more', async () => {
      const b = p.getByRole('button', { name: 'Show more', exact: true });
      if (await b.count()) { await b.first().click(); await wait(p, 500); await S.view('show-more'); }
    });
    await S.full();
  } },
  events: { path: '/events/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  podcast: { path: '/podcast/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  resources: { path: '/resources/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'question-bank': { path: '/resources/question-bank/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  glossary: { path: '/resources/glossary/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'glossary-term': { path: '/resources/glossary/card-sorting/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  'sample-size': { path: '/resources/sample-size/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  playbook: { path: '/resources/system-of-learning-playbook/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  report: { path: '/resources/market-research-report/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  about: { path: '/about-us/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  careers: { path: '/careers/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  newsroom: { path: '/newsroom/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  security: { path: '/security/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy-policy/', run: async (p, S) => { await hideConsent(p); await S.view('default'); } },
  terms: { path: '/tos/', run: async (p, S) => { await hideConsent(p); await S.view('default'); } },
  mcp: { path: '/platform/mcp/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
  reporting: { path: '/platform/ux-reporting/', run: async (p, S) => { await hideConsent(p); await S.view('default'); await S.full(); } },
};

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  const page = await context.newPage();
  page.setDefaultTimeout(12000);
  const names = pageArg.length ? pageArg : Object.keys(PAGES);
  for (const name of names) {
    const spec = PAGES[name];
    if (!spec) { log('unknown', name); continue; }
    const prefix = (mobile ? 'mobile-' : '') + name + '-light';
    log('page', prefix, spec.path);
    const ok = await gotoPublic(page, spec.path);
    if (!ok) continue;
    const S = new Shooter(page, prefix, vw, vh, dpr);
    await spec.run(page, S, mobile);
  }
  await browser.close();
}

const only = process.env.WIDTH || 'both';
if (only !== 'mobile') await runWidth(false);
if (only !== 'desktop') await runWidth(true);
log('done');
