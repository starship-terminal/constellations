// Captures MWM's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png. MWM ships one dark theme (html.dark-mode). Desktop shots are
// 1440x900 at 1x, phone shots 390x844 at 2x. Nothing is submitted, signed into, or uploaded.
// Open MWM Console and Build your app are login walls: the runner records the URL and leaves.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 160); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
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
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p, name) {
  const b = p.getByRole('button', { name, exact: true }).locator('visible=true').first();
  await b.hover();
  await wait(p, 700);
  const open = await b.getAttribute('aria-expanded');
  if (open !== 'true') { await b.click({ timeout: 5000 }); await wait(p, 500); }
}
async function openFaq(p, id) {
  const b = p.locator(`[aria-controls="${id}"]`).first();
  await b.scrollIntoViewIfNeeded();
  await b.click({ timeout: 5000 });
  await wait(p, 400);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('products-menu', async () => { await openMenu(p, 'Products'); await S.view('products-menu'); await p.mouse.click(20, 860); await wait(p, 300); });
    await step('resources-menu', async () => { await openMenu(p, 'Resources'); await S.view('resources-menu'); await p.mouse.click(20, 860); await wait(p, 300); });
    await step('agent-menu', async () => { await p.locator('[aria-controls="mwm-agent-menu"]').first().click(); await wait(p, 400); await S.view('agent-menu'); await p.keyboard.press('Escape'); });
    await step('platform-menu', async () => { await p.locator('[aria-controls="mwm-platform-menu"]').first().click(); await wait(p, 400); await S.view('platform-menu'); await p.keyboard.press('Escape'); });
    await step('model-menu', async () => { await p.locator('[aria-controls="mwm-model-menu"]').first().click(); await wait(p, 400); await S.view('model-menu'); await p.keyboard.press('Escape'); });
    await step('prompt-focused', async () => { await p.locator('textarea').first().click(); await wait(p, 300); await S.view('prompt-focused'); });
    await step('language-menu', async () => { await p.getByRole('button', { name: 'Switch language' }).click(); await wait(p, 400); await S.view('language-menu'); await p.keyboard.press('Escape'); });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); await step('faq', async () => { await openFaq(p, 'mwm-pricing-faq-answer-0'); await S.view('faq-open'); }); } },
  'mwm-ai': { path: '/mwm-ai', run: async (p, S) => { await S.view('default'); await S.full(); await step('agent-card', async () => { await p.getByRole('button', { name: 'Show Theo details' }).click(); await wait(p, 500); await S.view('agent-details'); }); await step('faq', async () => { await openFaq(p, 'mwm-ai-faq-answer-0'); await S.view('faq-open'); }); } },
  'mwm-console': { path: '/mwm-console', run: async (p, S) => { await S.view('default'); await S.full(); await step('faq', async () => { await openFaq(p, 'mwm-console-faq-answer-0'); await S.view('faq-open'); }); } },
  'mwm-publishing': { path: '/mwm-publishing', run: async (p, S) => { await S.view('default'); await S.full(); await step('faq', async () => { await openFaq(p, 'mwm-publishing-faq-answer-0'); await S.view('faq-open'); }); } },
  'mwm-intelligence': { path: '/mwm-intelligence', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'mwm-studio': { path: '/mwm-studio', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'studio-apps': { path: '/mwm-studio/apps', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'studio-app': { path: '/mwm-studio/apps/edjing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { path: '/company', run: async (p, S) => { await S.view('default'); await S.full(); } },
  story: { path: '/company/story', run: async (p, S) => { await S.view('default'); await S.full(); await step('sources', async () => { await p.locator('summary', { hasText: 'Sources' }).first().click(); await wait(p, 400); await S.view('sources-open'); }); } },
  apps: { path: '/apps/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'apps-duo': { path: '/apps/iphone-duo', run: async (p, S) => { await S.view('default'); await step('filter', async () => { await p.getByRole('button', { name: /Optimized/ }).first().click(); await wait(p, 600); await S.view('filter-optimized'); }); } },
  rankings: { path: '/rankings/countries', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'ranking-chart': { path: '/rankings/countries/US/devices/iphone/categories/6005', run: async (p, S) => { await S.view('default'); await step('faq', async () => { await p.getByRole('button', { name: /How often is the Social Networking ranking updated/ }).click(); await wait(p, 400); await S.view('faq-open'); }); } },
  tags: { path: '/tags', run: async (p, S) => { await S.view('default'); await S.full(); await step('search-focused', async () => { await p.locator('input[type="search"], input[placeholder*="Search"]').first().click(); await wait(p, 300); await S.view('search-focused'); }); } },
  tag: { path: '/tags/logic-and-brain-puzzles', run: async (p, S) => { await S.view('default'); } },
  articles: { path: '/articles', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'articles-trends': { path: '/articles/app-trends', run: async (p, S) => { await S.view('default'); await step('search-focused', async () => { await p.locator('input[placeholder*="Search"]').first().click(); await wait(p, 300); await S.view('search-focused'); }); } },
  'articles-updates': { path: '/articles/app-updates', run: async (p, S) => { await S.view('default'); } },
  'articles-reports': { path: '/articles/reports', run: async (p, S) => { await S.view('default'); await step('filter-europe', async () => { await p.getByRole('button', { name: 'Europe', exact: true }).click(); await wait(p, 500); await S.view('filter-europe'); }); } },
  article: { path: '/articles/app-trends/herdr-climbs-to-top-five-on-ios-app-store-in-november-2026', run: async (p, S) => { await S.view('default'); await S.full(); } },
  glossary: { path: '/glossary', run: async (p, S) => { await S.view('default'); await step('filter-aso', async () => { await p.getByRole('button', { name: /^ASO / }).click(); await wait(p, 400); await S.view('filter-aso'); }); } },
  'glossary-term': { path: '/glossary/aso', run: async (p, S) => { await S.view('default'); await step('faq', async () => { await p.getByRole('button', { name: 'What is ASO (App Store Optimization)?' }).click(); await wait(p, 400); await S.view('faq-open'); }); } },
  guides: { path: '/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  guide: { path: '/guides/app-store-optimization', run: async (p, S) => { await S.view('default'); await step('on-this-page', async () => { await p.locator('summary', { hasText: 'On this page' }).first().click(); await wait(p, 400); await S.view('on-this-page'); }); } },
  authors: { path: '/authors', run: async (p, S) => { await S.view('default'); } },
  author: { path: '/authors/benjamin-duvivier', run: async (p, S) => { await S.view('default'); } },
  methodology: { path: '/data-methodology', run: async (p, S) => { await S.view('default'); } },
  'methodology-nass': { path: '/data-methodology/nass', run: async (p, S) => { await S.view('default'); } },
  'aso-tool': { path: '/aso-tool', run: async (p, S) => { await S.view('default'); await step('faq', async () => { await p.locator('summary', { hasText: 'Is Scale really free?' }).click(); await wait(p, 400); await S.view('faq-open'); }); } },
  'sign-up-404': { path: '/sign-up', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms-of-service', run: async (p, S) => { await S.view('default'); } },
  'sdk-privacy': { path: '/sdk-privacy-policy', run: async (p, S) => { await S.view('default'); } },
  'sdk-terms': { path: '/sdk-terms-of-service', run: async (p, S) => { await S.view('default'); } },
  'ip-dispute': { path: '/legal/ip-dispute', run: async (p, S) => { await S.view('default'); await step('field-focused', async () => { await p.locator('input, textarea').first().click(); await wait(p, 300); await S.view('field-focused'); }); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-open', async () => { await p.getByRole('button', { name: 'Open navigation' }).click(); await wait(p, 500); await S.view('nav-open'); });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'mwm-ai': { path: '/mwm-ai', run: async (p, S) => { await S.view('default'); } },
  'mwm-console': { path: '/mwm-console', run: async (p, S) => { await S.view('default'); } },
  'mwm-studio': { path: '/mwm-studio', run: async (p, S) => { await S.view('default'); } },
  articles: { path: '/articles', run: async (p, S) => { await S.view('default'); } },
  apps: { path: '/apps/', run: async (p, S) => { await S.view('default'); } },
  glossary: { path: '/glossary', run: async (p, S) => { await S.view('default'); } },
  rankings: { path: '/rankings/countries', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
