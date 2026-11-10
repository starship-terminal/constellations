// Captures Anthropic's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   [RAW=<dir, default ~/.design-systems/anthropic/raw-shots>] PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Three public surfaces, three hosts:
//   www.anthropic.com     the marketing site: /, /news, /research, /engineering
//   claude.com            the product pages: /product/overview, /platform/api, /pricing, /contact-sales
//   platform.claude.com/docs  the Claude Platform docs: /docs/en/home, /docs/en/docs/get-started,
//                             /docs/en/api/messages (API reference)
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Desktop shots are 1440x900
// at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved
// as name.partN.png tiles, which quantize.py stitches back together.
//
// Nothing is sent, created or signed into: the nav dropdown is opened by hover only; the pricing
// plan tabs and the batch-processing toggle are local UI; the /contact-sales form is photographed
// and focused, never submitted; Log in, Try Claude links that leave for claude.ai, Console and the
// footer's Privacy choices dialog are never followed or opened. claude.ai and
// console.anthropic.com are the signed-in products and are never touched.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, DOCS } from './lib.mjs';

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
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < H; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Hovers one top-nav trigger so its dropdown opens (anthropic.com opens them on hover).
async function navMenu(p, S, item = 'Product') {
  const link = p.locator('button, a').filter({ hasText: new RegExp('^' + item + '$', 'i') }).filter({ visible: true }).first();
  await link.hover().catch(() => {});
  await wait(p, 1500);
  await S.view('nav-dropdown');
  await p.mouse.move(720, 500);
  await wait(p, 600);
}

const desktop = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-dropdown', () => navMenu(p, S));
    await step('search', async () => {
      const s = p.locator('button, [role=button]').filter({ hasText: /^search$/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 1200); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 500); }
    });
  } },
  news: { path: BASE + '/news', run: async (p, S) => { await S.view('default'); await S.full(); } },
  research: { path: BASE + '/research', run: async (p, S) => { await S.view('default'); await S.full(); } },
  engineering: { path: BASE + '/engineering', run: async (p, S) => { await S.view('default'); await S.full(); } },
  product: { path: 'https://claude.com/product/overview', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'platform-api': { path: 'https://claude.com/platform/api', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: 'https://claude.com/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('plan-tab', async () => {
      const t = p.locator('[role=tab], button').filter({ hasText: /^developer$/i }).filter({ visible: true }).first();
      if (await t.count()) { await t.click(); await wait(p, 1500); await S.view('plan-tab'); }
    });
    await step('batch-toggle', async () => {
      const t = p.locator('label, button, [role=switch]').filter({ hasText: /batch processing/i }).filter({ visible: true }).first();
      if (await t.count()) { await t.click(); await wait(p, 1200); await S.view('batch-toggle'); }
    });
  } },
  'contact-sales': { path: 'https://claude.com/contact-sales', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('field-focused', async () => {
      const f = p.locator('input[type=text], input:not([type]), input[type=email]').filter({ visible: true }).first();
      if (await f.count()) { await f.click(); await wait(p, 600); await S.view('field-focused'); await p.mouse.click(200, 60); }
    });
  } },
  'docs-home': { path: DOCS + '/en/home', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('search', async () => {
      const s = p.locator('[class*="fill-field"], button').filter({ hasText: /search/i }).first();
      if (await s.count()) { await s.click(); await wait(p, 1500); await S.view('search-dialog'); await p.keyboard.press('Escape'); await wait(p, 600); }
      else { await p.keyboard.press('ControlOrMeta+k'); await wait(p, 1500); await S.view('search-dialog'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
  } },
  'docs-start': { path: DOCS + '/en/docs/get-started', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-api': { path: DOCS + '/en/api/messages', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  // The docs ship a dark theme: html carries data-mode="system", so emulating a dark
  // colour scheme flips it. The marketing and product pages have no dark theme.
  'docs-home-dark': { path: DOCS + '/en/home', wait: 7000, theme: 'dark', name: 'docs-home', run: async (p, S) => {
    await p.emulateMedia({ colorScheme: 'dark' });
    await wait(p, 1500);
    await S.view('default');
    await S.full();
  } },
  'docs-api-dark': { path: DOCS + '/en/api/messages', wait: 7000, theme: 'dark', name: 'docs-api', run: async (p, S) => {
    await p.emulateMedia({ colorScheme: 'dark' });
    await wait(p, 1500);
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-open', async () => {
      const t = p.locator('button').filter({ hasText: /menu/i }).first();
      if (await t.count()) { await t.click(); await wait(p, 1500); await S.view('nav-open'); }
    });
  } },
  pricing: { path: 'https://claude.com/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-home': { path: DOCS + '/en/home', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const S = new Shooter(p, `${spec.name || name}-${spec.theme === 'dark' ? 'dark' : 'light'}`, vw, vh, dpr);
  try {
    await p.goto(spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
