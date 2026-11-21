// Captures SavvyCal's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full pages tile past
// one GPU texture and stop at 8 chunks.
//
// Nothing is submitted. Login and signup are photographed as walls.
// Password fields are not typed. Google, Microsoft, Fastmail and Apple
// are not clicked. FAQ, billing, search, demo day and the phone menu are
// local UI only.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'savvycal', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const cap = Math.min(h, 8 * 14000);
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
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openFaq(p) {
  const s = p.locator('summary').first();
  if (await s.count()) {
    await s.scrollIntoViewIfNeeded();
    await s.click();
    await wait(p, 400);
    return true;
  }
  return false;
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => { if (await openFaq(p)) await S.view('faq-open'); });
  } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Monthly', exact: true }).click();
      await wait(p, 500);
      await p.evaluate(() => scrollTo(0, 0));
      await S.view('monthly');
    });
    await step('faq', async () => { if (await openFaq(p)) await S.view('faq-open'); });
  } },
  demo: { path: '/demo', run: async (p, S) => {
    await S.view('default');
    await step('next-month', async () => {
      await p.getByRole('button', { name: 'Go to the Next Month' }).click();
      await wait(p, 600);
      await S.view('next-month');
    });
    await step('day', async () => {
      const day = p.locator('button').filter({ hasText: /^1[0-9]$/ }).first();
      if (await day.count()) { await day.click(); await wait(p, 700); await S.view('day'); }
    });
  } },
  integrations: { path: '/integrations-directory', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const box = p.getByPlaceholder('Search integrations');
      await box.click();
      await box.fill('calendar');
      await wait(p, 500);
      await S.view('search');
    });
    await step('category', async () => {
      await p.getByRole('button', { name: 'Calendar', exact: true }).click();
      await wait(p, 500);
      await S.view('category');
    });
  } },
  articles: { path: '/articles', run: async (p, S) => { await S.view('default'); await S.full(); } },
  availability: { path: '/features/availability', run: async (p, S) => { await S.view('default'); await S.full(); } },
  sales: { path: '/solutions/sales', run: async (p, S) => { await S.view('default'); } },
  compare: { path: '/calendly-vs-savvycal', run: async (p, S) => { await S.view('default'); } },
  company: { path: '/company', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  ai: { path: '/ai', run: async (p, S) => {
    await S.view('default');
    await step('tab', async () => {
      await p.getByRole('button', { name: 'ChatGPT', exact: true }).click();
      await wait(p, 400);
      await S.view('chatgpt');
    });
  } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signup: { path: '/signup', run: async (p, S) => { await S.view('default'); await S.full(); } },
  polls: { path: '/meeting-polls', run: async (p, S) => { await S.view('default'); } },
  brand: { path: '/brand', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      await p.getByRole('button', { name: 'Open main menu' }).click();
      await wait(p, 600);
      await S.view('menu');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Monthly', exact: true }).click();
      await wait(p, 400);
      await p.evaluate(() => scrollTo(0, 0));
      await S.view('monthly');
    });
  } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); } },
  demo: { path: '/demo', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations-directory', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  signup: { path: '/signup', run: async (p, S) => { await S.view('default'); } },
  articles: { path: '/articles', run: async (p, S) => { await S.view('default'); } },
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
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name, PKG);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1600);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
