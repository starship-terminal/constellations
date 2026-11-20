// Captures Soundtrap's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; phone shots get a mobile- prefix.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. One public theme.
// Nothing is submitted. Login, signup, social, and invite branches are
// recorded as walls and not filled. OneTrust is hidden, never answered.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, UA, UA_MOBILE, BASE, closePromo, isWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'soundtrap', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, 12000); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function goto(p, url) {
  const res = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 2200);
  await closePromo(p);
  return { status: res && res.status(), url: p.url() };
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('get-started-dialog', async () => {
      await p.getByRole('button', { name: 'Get started for free' }).click();
      await wait(p, 700);
      await closePromo(p);
      await S.view('get-started-dialog');
      await p.keyboard.press('Escape');
    });
    await step('language-menu', async () => {
      await p.locator('summary').filter({ hasText: 'English' }).first().click();
      await wait(p, 500);
      await S.view('language-menu');
      await p.keyboard.press('Escape');
    });
    await step('play-preview', async () => {
      await p.getByRole('button', { name: /Play High Fashion/ }).first().click();
      await wait(p, 600);
      await S.view('play-preview');
    });
    await step('carousel-next', async () => {
      await p.getByRole('button', { name: 'Next slide' }).first().click();
      await wait(p, 600);
      await S.view('carousel-next');
    });
  } },
  features: { url: BASE + '/content/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  edu: { url: BASE + '/edu/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Monthly', exact: true }).click();
      await wait(p, 500);
      await S.view('monthly');
    });
  } },
  'pricing-education': { url: BASE + '/pricing-education', run: async (p, S) => {
    await S.view('default');
    await step('tooltip', async () => {
      await p.getByRole('button', { name: /More info: Time restore/ }).click();
      await wait(p, 500);
      await S.view('tooltip');
      await p.keyboard.press('Escape');
    });
  } },
  originals: { url: BASE + '/originals', run: async (p, S) => { await S.view('default'); await S.full(); } },
  explore: { url: BASE + '/originals/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  storytellers: { url: BASE + '/storytellers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  developers: { url: BASE + '/developers', run: async (p, S) => { await S.view('default'); } },
  product: { url: BASE + '/content/product/record-voice-online', run: async (p, S) => { await S.view('default'); await S.full(); } },
  instruments: { url: BASE + '/content/instruments', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/legal/cookies', run: async (p, S) => { await S.view('default'); } },
  login: { url: BASE + '/login', run: async (p, S) => {
    if (!isWall(p.url()) && !/login/i.test(p.url())) log('  unexpected login url', p.url());
    await S.view('default');
  } },
  signup: { url: BASE + '/signup', run: async (p, S) => { await S.view('default'); } },
  'edu-login': { url: BASE + '/edu/login', run: async (p, S) => { await S.view('default'); } },
  blog: { url: 'https://blog.soundtrap.com/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      await p.getByRole('button', { name: /search blog/i }).click();
      await wait(p, 600);
      await closePromo(p);
      await S.view('search');
      await p.keyboard.press('Escape');
    });
  } },
  support: { url: 'https://support.soundtrap.com/', run: async (p, S) => { await S.view('default'); } },
  careers: { url: 'https://careers.soundtrap.com/', run: async (p, S) => {
    await S.view('default');
    await step('share', async () => {
      await p.getByRole('button', { name: 'Share page' }).click();
      await wait(p, 500);
      await S.view('share-menu');
      await p.keyboard.press('Escape');
    });
  } },
  notfound: { url: BASE + '/supported_browsers', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav', async () => {
      await p.getByRole('button', { name: /Open navigation menu/ }).click();
      await wait(p, 700);
      await closePromo(p);
      await S.view('nav');
      await p.keyboard.press('Escape');
    });
    await step('get-started-dialog', async () => {
      await p.getByRole('button', { name: 'Get started for free' }).click();
      await wait(p, 700);
      await closePromo(p);
      await S.view('get-started-dialog');
    });
  } },
  features: { url: BASE + '/content/features', run: async (p, S) => { await S.view('default'); } },
  edu: { url: BASE + '/edu/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Monthly', exact: true }).click();
      await wait(p, 500);
      await S.view('monthly');
    });
  } },
  originals: { url: BASE + '/originals', run: async (p, S) => { await S.view('default'); } },
  storytellers: { url: BASE + '/storytellers', run: async (p, S) => { await S.view('default'); } },
  login: { url: BASE + '/login', run: async (p, S) => { await S.view('default'); } },
  blog: { url: 'https://blog.soundtrap.com/', run: async (p, S) => { await S.view('default'); } },
  support: { url: 'https://support.soundtrap.com/', run: async (p, S) => { await S.view('default'); } },
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
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const landed = await goto(p, spec.url);
    log('  landed', landed.status, landed.url);
    if (isWall(landed.url) && !/login|signup|edu-login/.test(k)) log('  WALL', landed.url);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
void PKG;
