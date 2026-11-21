// Captures Overflow's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a mobile- prefix.
// Overflow's public site paints one light theme. Desktop shots are 1440x900
// at 1x, phone shots 390x844 at 2x. Nothing is submitted, downloaded, or
// signed into. The cookie bar is hidden, never accepted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideCookies, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'overflow', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: source,
    };
    this.count = 0;
  }
  async view(name) {
    await hideCookies(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideCookies(p);
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
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const desktop = {
  home: { path: '/', source: 'https://overflow.io/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('product-menu', async () => {
      await p.locator('a[href="#product-collapse"]').first().click();
      await wait(p, 600);
      await S.view('product-menu');
      await p.keyboard.press('Escape').catch(() => {});
      await p.locator('a[href="#product-collapse"]').first().click().catch(() => {});
      await wait(p, 300);
    });
    await step('demo-dialog', async () => {
      await p.evaluate(() => scrollTo(0, 0));
      const demo = p.getByText('Watch product demo', { exact: false }).first();
      await demo.click();
      await wait(p, 1500);
      await S.view('demo-dialog');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    });
    await step('view-tabs', async () => {
      for (const [label, hash] of [['Prototype view', 'prototype-view'], ['Story presentation', 'story-presentation'], ['Canvas view', 'canvas-view']]) {
        const loc = p.locator(`a[href="#${hash}"], a[href*="${hash}"]`).first();
        if (await loc.count()) {
          await loc.scrollIntoViewIfNeeded().catch(() => {});
          await loc.click().catch(() => {});
          await wait(p, 700);
          await S.view(hash);
        } else log('  missing tab', label);
      }
    });
  } },
  download: { path: '/download/', source: 'https://overflow.io/download/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'download-windows': { path: '/download/windows/', source: 'https://overflow.io/download/windows/', run: async (p, S) => { await S.view('default'); } },
  'how-it-works': { path: '/how-it-works/', source: 'https://overflow.io/how-it-works/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features/', source: 'https://overflow.io/features/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('feature-present', async () => {
      await p.locator('a[href="#feature_present"]').first().click();
      await wait(p, 600);
      await S.view('feature-present');
    });
  } },
  presentation: { path: '/design/presentation/', source: 'https://overflow.io/design/presentation/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'teams-product': { path: '/teams/product/', source: 'https://overflow.io/teams/product/', run: async (p, S) => { await S.view('default'); } },
  'teams-design': { path: '/teams/design/', source: 'https://overflow.io/teams/design/', run: async (p, S) => { await S.view('default'); } },
  'teams-agile': { path: '/teams/agile/', source: 'https://overflow.io/teams/agile/', run: async (p, S) => { await S.view('default'); } },
  agencies: { path: '/organizations/agencies/', source: 'https://overflow.io/organizations/agencies/', run: async (p, S) => { await S.view('default'); } },
  startups: { path: '/organizations/startups/', source: 'https://overflow.io/organizations/startups/', run: async (p, S) => { await S.view('default'); } },
  education: { path: '/organizations/education/', source: 'https://overflow.io/organizations/education/', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations/', source: 'https://overflow.io/integrations/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing/', source: 'https://overflow.io/pricing/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq-open', async () => {
      const opener = p.locator('.accordion__opener').first();
      await opener.scrollIntoViewIfNeeded();
      await opener.click();
      await wait(p, 500);
      await S.view('faq-open');
    });
  } },
  enterprise: { path: '/enterprise/', source: 'https://overflow.io/enterprise/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  examples: { path: '/examples/', source: 'https://overflow.io/examples/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog/', source: 'https://overflow.io/blog/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/welcome-overflow-1-0/', source: 'https://overflow.io/blog/welcome-overflow-1-0/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  stories: { path: '/stories/', source: 'https://overflow.io/stories/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  events: { path: '/events/', source: 'https://overflow.io/events/', run: async (p, S) => { await S.view('default'); } },
  'media-kit': { path: '/media-kit/', source: 'https://overflow.io/media-kit/', run: async (p, S) => { await S.view('default'); } },
  support: { path: '/support/', source: 'https://overflow.io/support/', run: async (p, S) => { await S.view('default'); } },
  eula: { path: '/eula/', source: 'https://overflow.io/eula/', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy-policy/', source: 'https://overflow.io/privacy-policy/', run: async (p, S) => { await S.view('default'); } },
  cookies: { path: '/cookie-statement/', source: 'https://overflow.io/cookie-statement/', run: async (p, S) => { await S.view('default'); } },
  'landing-2': { path: '/landing/overflow-2.0/', source: 'https://overflow.io/landing/overflow-2.0/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'diagrams-flows': { path: '/diagrams/user-flows/', source: 'https://overflow.io/diagrams/user-flows/', run: async (p, S) => { await S.view('default'); } },
  'diagrams-charts': { path: '/diagrams/flowcharts/', source: 'https://overflow.io/diagrams/flowcharts/', run: async (p, S) => { await S.view('default'); } },
  dc: { path: '/dc/', source: 'https://overflow.io/dc/', run: async (p, S) => { await S.view('default'); } },
  share: { path: '/s/Q4DI0PH6/', source: 'https://overflow.io/s/Q4DI0PH6/', run: async (p, S) => {
    await wait(p, 2500);
    await S.view('default');
    await step('prototype', async () => {
      await p.goto(BASE + '/s/Q4DI0PH6/?prototype', { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(p, 2500);
      await S.view('prototype');
    });
  } },
  'login-404': { path: '/login/', source: 'https://overflow.io/login/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', source: 'https://overflow.io/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const t = p.locator('button.navbar-toggler').first();
      await t.click();
      await wait(p, 700);
      await S.view('menu');
    });
  } },
  pricing: { path: '/pricing/', source: 'https://overflow.io/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  download: { path: '/download/', source: 'https://overflow.io/download/', run: async (p, S) => { await S.view('default'); } },
  features: { path: '/features/', source: 'https://overflow.io/features/', run: async (p, S) => { await S.view('default'); } },
  examples: { path: '/examples/', source: 'https://overflow.io/examples/', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', source: 'https://overflow.io/blog/', run: async (p, S) => { await S.view('default'); } },
  share: { path: '/s/Q4DI0PH6/', source: 'https://overflow.io/s/Q4DI0PH6/', run: async (p, S) => { await wait(p, 2000); await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
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
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.source);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await hideCookies(p);
    const box = await p.evaluate(() => ({
      w: window.innerWidth, h: window.innerHeight, dpr: window.devicePixelRatio,
    }));
    log('  viewport', box.w, box.h, 'dpr', box.dpr, 'url', spec.source);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
