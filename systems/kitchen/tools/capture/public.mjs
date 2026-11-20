// Captures Kitchen.co's public marketing pages into RAW (full-colour PNGs).
//
//   RAW=/some/scratch PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Kitchen.co ships one
// theme, so there is no dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x.
// Nothing is sent, created or signed into. Cookie overlays are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from './screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, PAGES } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'kitchen', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

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
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.min(4000, Math.floor(8000 / this.dpr));
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openSolutions(p) {
  const item = p.locator('li.has-dropdown').first();
  await item.hover();
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('solutions-menu', async () => {
      await openSolutions(p);
      await S.view('solutions-menu');
      await p.mouse.move(10, 400);
      await wait(p, 200);
    });
  } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => {
      const head = p.locator('button.accordion__head').first();
      await head.scrollIntoViewIfNeeded();
      await head.click();
      await wait(p, 500);
      await S.view('faq-open');
    });
    await step('plans-tab', async () => {
      const tab = p.locator('.plans-tabs__button').nth(1);
      if (await tab.count()) {
        await tab.scrollIntoViewIfNeeded();
        await tab.click();
        await wait(p, 500);
        await S.view('plans-tab');
      }
    });
  } },
  buy: { path: '/buy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { path: '/reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  tutorials: { path: '/tutorials', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'how-it-works': { path: '/how-it-works', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const field = p.locator('input, .form-search__field').first();
      if (await field.count()) {
        await field.click();
        await wait(p, 300);
        await S.view('search-focused');
      }
    });
  } },
  login: { path: '/login', run: async (p, S) => {
    await S.view('default');
    await step('field-focused', async () => {
      const field = p.locator('input').first();
      await field.click();
      await wait(p, 250);
      await S.view('field-focused');
    });
  } },
  'get-started': { path: '/get-started', run: async (p, S) => { await S.view('default'); } },
  'get-demo': { path: '/get-demo', run: async (p, S) => { await S.view('default'); } },
  'cookie-policy': { path: '/legal/cookie-policy', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const btn = p.locator('a.header__nav-mobile, .header__nav-mobile').first();
      await btn.click();
      await wait(p, 600);
      await S.view('menu-open');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  reviews: { path: '/reviews', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 1800);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
