// Captures flutterflow.io's public signed-out pages into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// The site paints light and dark (the footer theme switch, data-theme on
// <html>, prefers-color-scheme otherwise): most pages are shot light, the
// home/pricing/product/enterprise pages get a dark pass too, seeded through
// the page's own ff-theme localStorage key — never through an account.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full`
// shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together.
// Nothing is sent, created or signed into: the only presses are UI toggles —
// the snav menu buttons, the billing-period segmented control, product
// tabs, FAQ accordion summaries and the mobile menu's Open/Close buttons.
// The composer textareas, the enterprise form and every "Start building" /
// "Sign in" link are shot and measured, never submitted or followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

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
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
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

// Open the Product dropdown in the top nav (the site's own button; a UI
// toggle, not a link), shot it, then Escape back to rest.
async function navMenu(p, S, label = 'Product') {
  const b = p.locator('.ff-snav-menu', { hasText: label }).first();
  await b.click();
  await wait(p, 900);
  await S.view('nav-' + label.toLowerCase() + '-open');
  await p.keyboard.press('Escape');
  await p.mouse.click(720, 500).catch(() => {});
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('composer-focused', async () => { await p.locator('#describe-hero').click(); await wait(p, 600); await S.view('composer-focused'); await p.mouse.click(720, 800); });
    await step('nav-product', () => navMenu(p, S));
    await S.full();
  } },
  'home-dark': { path: '/', theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('nav-product', () => navMenu(p, S));
    await S.full();
  } },
  product: { path: '/product', run: async (p, S) => {
    await S.view('default');
    await step('tab', async () => { await p.locator('#backend-t1').click(); await wait(p, 800); await p.evaluate(() => scrollTo(0, document.getElementById('backend-t1').getBoundingClientRect().top + scrollY - 200)); await wait(p, 500); await S.view('tab-selected'); });
    await S.full();
  } },
  'product-dark': { path: '/product', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('billing-yearly', async () => { await p.locator('[data-ff-seg] [data-ff-value="yearly"]').first().click(); await wait(p, 700); await S.view('billing-yearly'); });
    await step('faq-closed', async () => { const item = p.locator('.ff-acc-item').first(); const s = item.locator('summary, .ff-acc-x').first(); await s.scrollIntoViewIfNeeded(); if (await item.evaluate((el) => el.open ?? el.hasAttribute('open'))) { await s.click(); await wait(p, 700); } await S.view('faq-closed'); });
    await S.full();
  } },
  'pricing-dark': { path: '/pricing', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: '/enterprise', run: async (p, S) => {
    await S.view('default');
    await step('form', async () => { const f = p.locator('#contact-first'); await f.scrollIntoViewIfNeeded(); await wait(p, 400); await S.view('form'); });
    await step('field-focused', async () => { await p.locator('#contact-first').click(); await wait(p, 500); await S.view('field-focused'); await p.keyboard.press('Escape').catch(() => {}); await p.mouse.click(1100, 200); });
    await S.full();
  } },
  'enterprise-dark': { path: '/enterprise', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  studio: { path: '/studio', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'studio-showcase': { path: '/studio/showcase', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'studio-faq': { path: '/studio/faq', run: async (p, S) => {
    await S.view('default');
    await step('faq-closed', async () => { const item = p.locator('.ff-acc-item').first(); const s = item.locator('summary, .ff-acc-x').first(); await s.scrollIntoViewIfNeeded(); if (await item.evaluate((el) => el.open ?? el.hasAttribute('open'))) { await s.click(); await wait(p, 700); } await S.view('faq-closed'); });
    await S.full();
  } },
  'studio-apply': { path: '/studio/apply-to-be-a-developer', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-stories': { path: '/customer-stories', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'about-us': { path: '/about-us', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'contact-us': { path: '/contact-us', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'vs-studio': { path: '/flutterflow-vs-studio', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'dev-groups': { path: '/flutterflow-developer-groups', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'student-ambassadors': { path: '/student-ambassadors', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('.ff-ibtn[aria-label="Open menu"]').first().click();
      await wait(p, 1200);
      await S.view('menu-open');
      await p.locator('.ff-ibtn[aria-label="Close menu"]').first().click().catch(() => {});
      await wait(p, 600);
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = spec.theme || 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx, { theme });
  const p = await ctx.newPage();
  log(name, theme === 'dark' ? '(dark)' : '');
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.theme) await p.evaluate(() => document.documentElement.dataset.theme = 'dark'); // belt and braces: the seed sets localStorage, the attr wins
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
