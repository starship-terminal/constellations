// Captures Missive's public marketing pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Missive paints one light theme.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x.
// Nothing is sent or signed into. The Ketch consent banner is hidden, never clicked.
// Log in, Try for free, Sign up, Google, Apple and SSO are never followed.
// The only presses are local UI: the Product menu, a pricing FAQ, the demo lightbox, a home tab, the mobile menu.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

async function hideConsent(p) {
  await p.evaluate(() => {
    for (const id of ['ketch-banner', 'lanyard_root']) {
      const el = document.getElementById(id);
      if (el) el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const shot = (path) => ({ path, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('product-menu', async () => {
      await p.locator('.navbar:not(.mobile-only) .w-dropdown-toggle').filter({ hasText: 'Product' }).first().hover();
      await wait(p, 700);
      await S.view('product-menu');
      await p.mouse.click(8, 860);
      await wait(p, 300);
    });
    await step('resources-menu', async () => {
      await p.locator('.navbar:not(.mobile-only) .w-dropdown-toggle').filter({ hasText: 'Resources' }).first().hover();
      await wait(p, 700);
      await S.view('resources-menu');
      await p.mouse.click(8, 860);
      await wait(p, 300);
    });
    await step('demo', async () => {
      const demo = p.locator('a, button, div').filter({ hasText: /^Watch demo$/ }).first();
      await demo.click();
      await wait(p, 1200);
      await S.view('demo');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('tab', async () => {
      const tab = p.locator('.w-tab-link').nth(1);
      await tab.scrollIntoViewIfNeeded();
      await tab.click();
      await wait(p, 700);
      await S.view('tab-context');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => {
      const q = p.locator('.w-dropdown-toggle').filter({ hasText: /Can I try Missive/ }).first();
      await q.scrollIntoViewIfNeeded();
      await q.click();
      await wait(p, 700);
      await S.view('faq');
    });
  } },
  features: shot('/features'),
  collaborate: shot('/collaborate'),
  integrations: shot('/integrations'),
  'ai-assistant': shot('/ai-assistant'),
  customers: shot('/customers'),
  'customer-story': shot('/customers/morning'),
  docs: shot('/docs'),
  download: shot('/download'),
  blog: shot('/blog'),
  'blog-post': shot('/blog/team-inbox-vs-shared-inbox'),
  changelog: shot('/changelog'),
  about: shot('/about'),
  partners: shot('/partners'),
  compare: shot('/compare/frontapp-vs-missive'),
  privacy: shot('/privacy'),
  referral: shot('/referral-program'),
  'feature-sms': shot('/features/sms'),
  'solution-travel': shot('/solutions/travel'),
  'usecase-support': shot('/usecases/support'),
  'integration-asana': shot('/integrations/asana'),
  'changelog-post': shot('/changelog/10-64-1'),
  'fr-home': shot('/fr'),
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      await p.locator('.navbar.mobile-only .menu-mobile-toggle').click();
      await wait(p, 800);
      await S.view('menu');
    });
  } },
  pricing: shot('/pricing'),
  features: shot('/features'),
  docs: shot('/docs'),
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    await hideConsent(p);
    const landed = p.url();
    if (/mail\.missiveapp\.com|#login|#signup/.test(landed)) log('  LOGIN WALL', landed);
    else await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
