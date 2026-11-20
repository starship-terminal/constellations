// Captures Mangomint's public marketing pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Desktop shots are 1440x900 at 1x, phone shots 390x844 at 2x. Nothing is submitted.
// Login, demo and trial walls are recorded and the branch stops. Cookie banners are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mangomint', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.source = source;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openNav(p, name) {
  const btn = p.locator('button.desktopNavbarDropdown-module--link--047eb', { hasText: name }).first();
  await btn.hover();
  await btn.click();
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-businesses', async () => { await openNav(p, 'Businesses'); await S.view('nav-businesses'); await p.keyboard.press('Escape'); await p.mouse.click(20, 500); });
    await step('nav-features', async () => { await openNav(p, 'Features'); await S.view('nav-features'); await p.keyboard.press('Escape'); await p.mouse.click(20, 500); });
    await step('nav-mira', async () => { await openNav(p, 'AI Receptionist'); await S.view('nav-mira'); await p.keyboard.press('Escape'); await p.mouse.click(20, 500); });
    await step('carousel', async () => {
      const slide = p.getByRole('button', { name: 'Slide 2' }).first();
      if (await slide.count()) { await slide.click(); await wait(p, 700); await S.view('carousel-online-booking'); }
    });
    await step('video-tour', async () => {
      const b = p.locator('button.videoSelectionButton').first();
      if (await b.count()) { await b.click(); await wait(p, 1200); await S.view('video-tour'); await p.keyboard.press('Escape'); }
    });
  } },
  pricing: { path: '/pricing/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('calculator', async () => {
      const inc = p.getByRole('button', { name: 'Increase Locations' });
      if (await inc.count()) { await inc.click(); await wait(p, 500); await S.view('locations-up'); }
    });
    await step('faq', async () => {
      const q = p.locator('button, [role="button"]').filter({ hasText: /\?/ }).first();
      if (await q.count()) { await q.scrollIntoViewIfNeeded(); await q.click(); await wait(p, 500); await S.view('faq-open'); }
    });
  } },
  why: { path: '/why-mangomint/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  tour: { path: '/tour/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { path: '/integrations/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  payments: { path: '/payments/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  scheduling: { path: '/features/scheduling/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  booking: { path: '/features/online-booking/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  phone: { path: '/features/phone/', run: async (p, S) => { await S.view('default'); } },
  forms: { path: '/features/integrated-forms/', run: async (p, S) => { await S.view('default'); } },
  memberships: { path: '/features/memberships-and-packages/', run: async (p, S) => { await S.view('default'); } },
  flows: { path: '/features/automated-flows/', run: async (p, S) => { await S.view('default'); } },
  reporting: { path: '/features/reporting/', run: async (p, S) => { await S.view('default'); } },
  staff: { path: '/features/staff-management/', run: async (p, S) => { await S.view('default'); } },
  solution: { path: '/solutions/hair-salon-software/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  medspa: { path: '/solutions/medical-spa-software/', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/introducing-mira-the-ai-receptionist-for-beauty-and-wellness/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  learn: { path: '/learn/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'learn-article': { path: '/learn/add-a-new-client/', run: async (p, S) => { await S.view('default'); } },
  videos: { path: '/videos/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about-us/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  updates: { path: '/updates/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact-us/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('chat', async () => {
      const b = p.getByRole('button', { name: 'Start a chat' });
      if (await b.count()) { await b.click(); await wait(p, 1500); await S.view('chat'); }
    });
  } },
  security: { path: '/security/', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/legal/privacy-policy/', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/legal/website-terms-of-use/', run: async (p, S) => { await S.view('default'); } },
  demo: { path: '/demo/', wall: true, run: async (p, S) => { await S.view('wall'); } },
  trial: { path: '/trial/', wall: true, run: async (p, S) => { await S.view('wall'); } },
  login: { path: 'https://app.mangomint.com/login', wall: true, absolute: true, run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Toggle the navigation' });
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('menu'); }
    });
  } },
  pricing: { path: '/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  why: { path: '/why-mangomint/', run: async (p, S) => { await S.view('default'); } },
  scheduling: { path: '/features/scheduling/', run: async (p, S) => { await S.view('default'); } },
  solution: { path: '/solutions/hair-salon-software/', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact-us/', run: async (p, S) => { await S.view('default'); } },
  demo: { path: '/demo/', wall: true, run: async (p, S) => { await S.view('wall'); } },
  login: { path: 'https://app.mangomint.com/login', wall: true, absolute: true, run: async (p, S) => { await S.view('wall'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  const url = spec.absolute ? spec.path : BASE + spec.path;
  log(name, url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, url.split('?')[0]);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
    await wait(p, 1800);
    await hideConsent(p);
    if (spec.wall) {
      const blocked = await p.evaluate(() => /email address|password|which services do you offer|book a demo/i.test(document.body.innerText || ''));
      log('  wall', blocked, 'url', p.url().split('?')[0]);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
