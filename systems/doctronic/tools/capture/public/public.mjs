// Captures doctronic.ai public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/doctronic/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Nothing is submitted. Login and signup walls are opened empty. Get Login Code,
// Get Sign up Code, Google, Apple and Facebook are never clicked. No email is typed.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'doctronic', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
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
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openSidebar(p) {
  const t = p.locator('[data-test-id="sidebar-toggle"]');
  if (await t.count()) { await t.first().click({ force: true }); await wait(p, 700); }
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('sidebar', async () => { await openSidebar(p); await S.view('sidebar'); await p.keyboard.press('Escape'); });
    await step('login', async () => {
      await p.locator('[data-test-id="log-in-button"]').first().click();
      await wait(p, 900);
      await S.view('login');
      await p.keyboard.press('Escape');
    });
    await step('signup', async () => {
      await p.goto(BASE + '/?modal=signup', { waitUntil: 'domcontentloaded' });
      await wait(p, 900);
      await S.view('signup');
    });
    await step('login-email', async () => {
      await p.goto(BASE + '/?modal=signin', { waitUntil: 'domcontentloaded' });
      await wait(p, 800);
      await p.locator('[data-test-id="start-email-button"]').click();
      await wait(p, 700);
      await S.view('login-email');
    });
    await step('anonymous', async () => {
      await p.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
      await wait(p, 800);
      await p.locator('[data-test-id="anon-info-badge"]').first().click();
      await wait(p, 600);
      await S.view('anonymous');
    });
  } },
  chat: { path: '/chat/', run: async (p, S) => { await S.view('default'); } },
  philosophy: { path: '/our-philosophy/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about/', run: async (p, S) => { await S.view('default'); } },
  careers: { path: '/careers/', run: async (p, S) => { await S.view('default'); } },
  partners: { path: '/partners/', run: async (p, S) => { await S.view('default'); } },
  treatment: { path: '/online-treatment/', run: async (p, S) => { await S.view('default'); } },
  symptoms: { path: '/symptom-checker/', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); } },
  resources: { path: '/resource-center/', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy-policy/', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms-of-service/', run: async (p, S) => { await S.view('default'); } },
  dns: { path: '/do-not-sell/', run: async (p, S) => { await S.view('default'); } },
  portal: { path: '/prescription-refill/portal/', run: async (p, S) => { await S.view('default'); } },
  'not-found': { path: '/for-partners/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openSidebar(p); await S.view('menu'); });
  } },
  chat: { path: '/chat/', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/?modal=signin', run: async (p, S) => { await S.view('default'); } },
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 2000);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
