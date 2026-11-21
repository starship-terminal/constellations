// Captures rive.app's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/rive/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix. Marketing pages paint one
// dark theme. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together. Infinite-scroll pages truncate at 8 chunks.
//
// Nothing is sent, created or signed into. Presses are local UI only: nav menus, the mobile sheet,
// the pricing period toggle, the home demo switcher, and the docs theme control if it opens a menu.
// Login, signup, Google, Apple, SSO, and every form (newsletter, search, contact) are never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 120); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openNav(p, label) {
  const clicked = await p.evaluate((label) => {
    const b = [...document.querySelectorAll('button.rn-top, button')].find((el) => (el.innerText || '').trim() === label && el.getBoundingClientRect().width > 0);
    if (!b) return false;
    b.click();
    return true;
  }, label);
  if (!clicked) throw new Error('nav button missing: ' + label);
  await wait(p, 700);
}

const viewPage = async (p, S, { full = true, extra } = {}) => {
  await closePromo(p);
  await S.view('default');
  if (extra) await extra(p, S);
  if (full) await S.full();
};

const desktop = {
  home: { path: '/', wait: 2500, run: async (p, S) => {
    await viewPage(p, S, { extra: async () => {
      await step('products-menu', async () => { await openNav(p, 'PRODUCTS'); await S.view('products-menu'); await p.keyboard.press('Escape'); await p.mouse.click(20, 860); await wait(p, 400); });
      await step('usecases-menu', async () => { await openNav(p, 'USE CASES'); await S.view('usecases-menu'); await p.keyboard.press('Escape'); await p.mouse.click(20, 860); await wait(p, 400); });
      await step('resources-menu', async () => { await openNav(p, 'RESOURCES'); await S.view('resources-menu'); await p.keyboard.press('Escape'); await p.mouse.click(20, 860); await wait(p, 400); });
      await step('demo-dashboard', async () => {
        const b = p.locator('button[aria-label="Show Dashboard"]');
        if (await b.count()) { await b.click(); await wait(p, 900); await S.view('demo-dashboard'); }
      });
    } });
  } },
  pricing: { path: '/pricing', wait: 2000, run: async (p, S) => {
    await viewPage(p, S, { extra: async () => {
      await step('monthly', async () => {
        const ok = await p.evaluate(() => {
          const el = [...document.querySelectorAll('p,div,button,a')].find((n) => (n.innerText || '').trim() === 'MONTHLY' && n.getBoundingClientRect().width > 20 && n.getBoundingClientRect().width < 120);
          if (!el) return false;
          (el.closest('a,button,[role="button"]') || el).click();
          return true;
        });
        if (!ok) throw new Error('MONTHLY missing');
        await wait(p, 700);
        await S.view('monthly');
      });
    } });
  } },
  downloads: { path: '/downloads', run: async (p, S) => viewPage(p, S) },
  editor: { path: '/editor', run: async (p, S) => viewPage(p, S) },
  agents: { path: '/agents', run: async (p, S) => viewPage(p, S) },
  games: { path: '/games', run: async (p, S) => viewPage(p, S) },
  'game-ui': { path: '/game-ui', run: async (p, S) => viewPage(p, S) },
  runtimes: { path: '/runtimes', run: async (p, S) => viewPage(p, S) },
  renderer: { path: '/renderer', run: async (p, S) => viewPage(p, S) },
  features: { path: '/features', run: async (p, S) => viewPage(p, S) },
  'use-cases': { path: '/use-cases', run: async (p, S) => viewPage(p, S) },
  'use-cases-apps': { path: '/use-cases/mobile-apps', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-websites': { path: '/use-cases/websites', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-product': { path: '/use-cases/product-design', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-characters': { path: '/use-cases/character-animation', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-vehicles': { path: '/use-cases/automotive', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-broadcast': { path: '/use-cases/broadcast', run: async (p, S) => viewPage(p, S, { full: false }) },
  'use-cases-film': { path: '/use-cases/film-tv', run: async (p, S) => viewPage(p, S, { full: false }) },
  blog: { path: '/blog', run: async (p, S) => viewPage(p, S) },
  'blog-case-studies': { path: '/blog/case-studies', run: async (p, S) => viewPage(p, S, { full: false }) },
  'blog-press': { path: '/blog/press', run: async (p, S) => viewPage(p, S, { full: false }) },
  'blog-riv-format': { path: '/blog/a-new-graphics-format-for-the-interactive-era', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-html': { path: '/rive-vs-html', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-spine': { path: '/rive-vs-spine', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-figma': { path: '/figma-to-rive', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-lottie': { path: '/blog/rive-as-a-lottie-alternative', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-ae': { path: '/blog/rive-vs-after-effects', run: async (p, S) => viewPage(p, S, { full: false }) },
  'compare-animate': { path: '/blog/adobe-animate-alternative-rive-is-what-flash-should-have-become', run: async (p, S) => viewPage(p, S, { full: false }) },
  experts: { path: '/experts', run: async (p, S) => viewPage(p, S) },
  enterprise: { path: '/enterprise', run: async (p, S) => viewPage(p, S) },
  contact: { path: '/contact', run: async (p, S) => viewPage(p, S) },
  careers: { path: '/careers', run: async (p, S) => viewPage(p, S) },
  newsletter: { path: '/newsletter', run: async (p, S) => viewPage(p, S) },
  marketplace: { path: '/marketplace/', run: async (p, S) => viewPage(p, S) },
  animascript: { path: '/rasc/index.html', run: async (p, S) => viewPage(p, S, { full: false }) },
  docs: { path: '/docs/getting-started/introduction', wait: 2500, run: async (p, S) => {
    await viewPage(p, S, { extra: async () => {
      await step('theme-menu', async () => {
        const b = p.getByRole('button', { name: /theme/i }).first();
        if (!(await b.count())) throw new Error('theme control missing');
        await b.click();
        await wait(p, 600);
        await S.view('theme-menu');
        await p.keyboard.press('Escape');
      });
    } });
  } },
  'docs-editor': { path: '/docs/editor/overview', wait: 2000, run: async (p, S) => viewPage(p, S, { full: false }) },
  login: { path: '/login/', wait: 1500, run: async (p, S) => {
    // Wall only. Do not type, do not click Google, Apple, or SSO, do not submit.
    await S.view('wall');
  } },
};

const mobilePages = ['home', 'pricing', 'downloads', 'editor', 'agents', 'games', 'features', 'use-cases', 'blog', 'experts', 'enterprise', 'contact', 'careers', 'newsletter', 'marketplace', 'docs', 'login'];
const mobile = {};
for (const k of mobilePages) {
  const spec = desktop[k];
  mobile[k] = { path: spec.path, wait: spec.wait || 1800, run: async (p, S) => {
    await closePromo(p);
    if (k === 'home') {
      await step('menu-open', async () => {
        const b = p.locator('button[aria-label="Open menu"]');
        if (!(await b.count())) throw new Error('Open menu missing');
        await b.click();
        await wait(p, 700);
        await S.view('menu-open');
        const close = p.locator('button[aria-label="Close menu"]');
        if (await close.count()) await close.click();
        else await p.keyboard.press('Escape');
        await wait(p, 400);
      });
    }
    if (k === 'login') { await S.view('wall'); return; }
    await S.view('default');
    await S.full();
  } };
}

const b = await chromium.launch({ headless: true });
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
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 1800);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
