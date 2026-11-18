// Captures Lummi's public signed-out pages.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. OneTrust is hidden, never clicked.
// Nothing is signed into, downloaded, purchased, or submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lummi', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
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
    await wait(p, 300);
  }
}

const failed = [];
const step = async (label, fn) => {
  try { await fn(); } catch (e) {
    failed.push(label);
    log('  FAILED', label, String(e.message).split('\n')[0]);
  }
};

async function openTools(p) {
  const b = p.locator('button').filter({ hasText: /^Tools$/ }).first();
  await b.click({ force: true });
  await wait(p, 500);
}

const PHOTO = '/photo/textured-green-powder-_wioh';

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search-palette', async () => {
      await p.locator('input[placeholder="Search or create anything!"]').first().click({ force: true });
      await wait(p, 600);
      await S.view('search-palette');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('tools-menu', async () => {
      await openTools(p);
      await S.view('tools-menu');
      await p.keyboard.press('Escape');
      await wait(p, 250);
    });
    await step('daily-picks', async () => {
      await p.locator('button').filter({ hasText: 'Daily picks' }).first().click({ force: true });
      await wait(p, 400);
      await S.view('daily-picks');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  illustration: { path: '/illustration', run: async (p, S) => { await S.view('default'); } },
  '3d': { path: '/3d', run: async (p, S) => { await S.view('default'); } },
  photo: { path: PHOTO, run: async (p, S) => {
    await S.view('default');
    await step('download-hover', async () => {
      const b = p.getByRole('button', { name: 'Download', exact: true }).first();
      const box = await b.boundingBox();
      if (box) await p.mouse.move(box.x + 20, box.y + box.height / 2);
      await wait(p, 300);
      await S.view('download-hover');
      await p.mouse.move(2, 800);
    });
  } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { path: '/s/photo/forest', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => {
    await S.view('default');
    await step('email-focused', async () => {
      await p.locator('#email').click({ force: true });
      await wait(p, 250);
      await S.view('email-focused');
    });
    // Type and delete. Never press Continue, never submit.
    await step('email-filled', async () => {
      await p.locator('#email').fill('not-submitted@example.com');
      await wait(p, 200);
      await S.view('email-filled');
      await p.locator('#email').fill('');
    });
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pro: { path: '/pro', run: async (p, S) => { await S.view('default'); } },
  updates: { path: '/updates', run: async (p, S) => { await S.view('default'); } },
  license: { path: '/license', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  creator: { path: '/creator/rena', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/this-page-is-not-a-lummi-route', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  photo: { path: PHOTO, run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); } },
  search: { path: '/s/photo/forest', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    const hide = () => document.querySelectorAll('#onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk, .onetrust-pc-dark-filter').forEach((el) => el.remove());
    const start = () => { hide(); new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true }); };
    if (document.documentElement) start();
    else document.addEventListener('DOMContentLoaded', start);
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1800);
    await hideConsent(p);
    await p.keyboard.press('Escape').catch(() => {});
    await spec.run(p, S);
  } catch (e) {
    failed.push(name);
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
    if (fs.existsSync(RAW)) for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${name}-light`))) fs.unlinkSync(`${RAW}/${old}`);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
if (failed.length) {
  log('failed', failed.join(', '));
  process.exit(1);
}
