// Captures forhims.co.uk public signed-out pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Ketch consent is hidden, never clicked. Nothing is signed into, paid, or submitted.
// Account routes are captured separately from the signed-in preview session.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, hideConsent, launchBrowser, newContext, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'hims', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 12000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
    await hideConsent(p);
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
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.p.url().split('?')[0] }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, sanitizedSourceUrl: p.url().split('?')[0] }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p) {
  const btn = p.locator('[data-testid="global-navigation-open-menu"]');
  await btn.click();
  await wait(p, 700);
  await hideConsent(p);
}

async function openNav(p, name, href) {
  // Hover leaves the flyout closed in headless Chromium. Click, then wait for a link.
  const b = p.getByRole('button', { name, exact: true }).first();
  await b.click();
  if (href) await p.locator(`a[href="${href}"]`).first().waitFor({ state: 'visible', timeout: 4000 });
  await wait(p, 400);
  await hideConsent(p);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('sex-menu', async () => { await openNav(p, 'Sex', '/erectile-dysfunction'); await S.view('sex-menu'); await p.mouse.move(20, 500); await wait(p, 300); });
    await step('learn-menu', async () => { await openNav(p, 'Learn', '/blog'); await S.view('learn-menu'); await p.mouse.move(20, 500); await wait(p, 300); });
    await step('menu', async () => { await openMenu(p); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('cta-hover', async () => {
      const cta = p.getByRole('button', { name: 'Explore treatments' }).first();
      await cta.hover();
      await wait(p, 400);
      await S.view('cta-hover');
    });
    await S.full();
  } },
  'weight-loss': { path: '/weight-loss', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'hair-loss': { path: '/hair-loss', run: async (p, S) => { await S.view('default'); await S.full(); } },
  ed: { path: '/erectile-dysfunction', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pe: { path: '/premature-ejaculation', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'how-it-works': { path: '/how-it-works', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  conditions: { path: '/conditions', run: async (p, S) => { await S.view('default'); } },
  reviews: { path: '/hims-reviews', run: async (p, S) => { await S.view('default'); } },
  purpose: { path: '/purpose', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/customer/login', run: async (p, S) => {
    // Empty wall only. Do not type an email, password, or code. Do not submit.
    await S.view('default');
    await step('forgot', async () => {
      await p.getByRole('button', { name: 'Forgot your password?' }).click();
      await wait(p, 700);
      await hideConsent(p);
      await S.view('forgot');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('register', async () => {
      await p.getByRole('button', { name: 'Create an account' }).click();
      await wait(p, 800);
      await hideConsent(p);
      await S.view('register');
      await p.keyboard.press('Escape');
    });
  } },
  migration: { path: '/migration-privacy', run: async (p, S) => { await S.view('default'); } },
  // /c is a consultation start ("What are you looking to do?"). Not captured.
  terms: { path: '/terms-and-conditions', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMenu(p); await S.view('menu'); });
    await S.full();
  } },
  'weight-loss': { path: '/weight-loss', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/customer/login', run: async (p, S) => { await S.view('default'); } },
  'hair-loss': { path: '/hair-loss', run: async (p, S) => { await S.view('default'); } },
};

const browser = await launchBrowser();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
try {
  for (const { k, mob } of runs) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name)) continue;
    const spec = (mob ? mobile : desktop)[k];
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await newContext(browser, { mobile: mob, width: vw, height: vh, dpr });
    const p = await ctx.newPage();
    log(name);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      await open(p, BASE + spec.path, { wait: spec.wait || 1600 });
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
} finally {
  log('done', total, 'screenshots ->', RAW);
  await browser.close();
}
