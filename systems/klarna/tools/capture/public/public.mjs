// Captures Klarna's public pages into RAW (full-colour PNGs). quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Desktop 1440x900 at 1x, mobile 390x844 at 2x. Consent overlays are hidden, never answered.
// Nothing is signed into, submitted, or purchased. Sign-in links are never followed.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'klarna', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 8 * 6000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 600);
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
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function dismissAnnouncement(p) {
  const b = p.getByRole('button', { name: /close announcement/i });
  if (await b.count()) {
    await b.first().click({ timeout: 3000 }).catch(() => {});
    await wait(p, 500);
  }
}

const desktop = {
  international: { path: '/international/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  home: { path: '/us/', run: async (p, S) => {
    await dismissAnnouncement(p);
    await S.view('default');
    await S.full();
    await step('nav-discover', async () => {
      await p.getByRole('link', { name: 'Discover Klarna' }).first().hover();
      await wait(p, 700);
      await S.view('nav-hover');
    });
    await step('language', async () => {
      const b = p.getByRole('button', { name: /select language/i }).first();
      await b.click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('language-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('search-focus', async () => {
      const s = p.getByRole('searchbox', { name: /search for any product/i }).first();
      await s.scrollIntoViewIfNeeded();
      await s.click({ timeout: 4000 });
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape');
    });
  } },
  'what-is-klarna': { path: '/us/what-is-klarna/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  shopping: { path: '/us/shopping/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  app: { path: '/us/klarna-app/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  help: { path: '/us/help/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  'buyer-protection': { path: '/us/buyer-protection/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  'personal-account': { path: '/us/personal-account/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  phishing: { path: '/us/phishing-and-scams/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); } },
  'signin-boundary': { path: 'https://app.klarna.com/login?market=US&locale=en-US', abs: true, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  international: { path: '/international/', run: async (p, S) => { await S.view('default'); } },
  home: { path: '/us/', run: async (p, S) => {
    await dismissAnnouncement(p);
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /open navigation menu/i }).first();
      await b.click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('menu-open');
    });
  } },
  shopping: { path: '/us/shopping/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); await S.full(); } },
  help: { path: '/us/help/', run: async (p, S) => { await dismissAnnouncement(p); await S.view('default'); } },
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
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  // navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.abs ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 3500);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
