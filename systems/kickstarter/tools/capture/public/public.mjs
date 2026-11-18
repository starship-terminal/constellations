// Captures kickstarter.com public signed-out pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Headed Chrome: Cloudflare challenges headless Chromium on every route but home.
// Consent is hidden, never clicked. Nothing is signed into, pledged, or submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, hideConsent, launchBrowser, newContext, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'kickstarter', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
    await hideConsent(p);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
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
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function projectPath(p) {
  return p.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((el) => /\/projects\/[^/]+\/[^/?#]+/.test(el.getAttribute('href') || '') && el.getBoundingClientRect().width > 40);
    if (!a) return null;
    const u = new URL(a.href);
    return u.pathname;
  });
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('category-menu', async () => {
      const art = p.locator('a.category-link__link, nav a').filter({ hasText: /^Art$/ }).first();
      await art.hover();
      await wait(p, 700);
      await S.view('category-menu');
      await p.mouse.move(700, 700);
      await wait(p, 300);
    });
    await step('search-focus', async () => {
      const input = p.locator('input[aria-label*="Search"], input[placeholder*="Search"]').first();
      await input.click();
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  discover: { path: '/discover?ref=nav', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'discover-art': { path: '/discover/categories/art', run: async (p, S) => { await S.view('default'); await S.full(); } },
  games: { path: '/discover/categories/games', run: async (p, S) => { await S.view('default'); } },
  search: { path: '/discover/advanced?term=camera&sort=magic', run: async (p, S) => { await S.view('default'); await S.full(); } },
  project: { path: null, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  start: { path: '/start', run: async (p, S) => { await S.view('default'); await S.full(); } },
  creators: { path: '/creators?ref=nav', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  rules: { path: '/rules', run: async (p, S) => { await S.view('default'); await S.full(); } },
  trust: { path: '/trust', run: async (p, S) => { await S.view('default'); await S.full(); } },
  press: { path: '/press', run: async (p, S) => { await S.view('default'); } },
  environment: { path: '/environment', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], button.kds-button').filter({ hasText: /menu|Menu/ }).first();
      const hamburger = p.locator('[aria-label="Open menu"], [aria-label="Menu"], button.mobile-nav, .js-nav-toggle').first();
      const target = (await hamburger.count()) ? hamburger : btn;
      if (await target.count()) {
        await target.click();
        await wait(p, 800);
        await S.view('menu');
      }
    });
    await S.full();
  } },
  discover: { path: '/discover?ref=nav', run: async (p, S) => { await S.view('default'); await S.full(); } },
  project: { path: null, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  start: { path: '/start', run: async (p, S) => { await S.view('default'); } },
};

const browser = await launchBrowser();
let project = process.env.PROJECT || '';
if (!project) {
  const ctx = await newContext(browser);
  const p = await ctx.newPage();
  await open(p, BASE + '/');
  project = (await projectPath(p)) || '/projects/shirtaloon/hwfwm';
  await ctx.close();
  log('project', project);
}

let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await newContext(browser, { mobile: mob, width: vw, height: vh, dpr });
  const p = await ctx.newPage();
  const route = spec.path || project;
  log(name, route);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const ok = await open(p, BASE + route, { wait: spec.wait || 1800 });
    if (!ok) log('  CHALLENGE stuck', name);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW, 'project', project);
fs.writeFileSync(path.join(RAW, 'project-path.txt'), project + '\n');
await browser.close();
