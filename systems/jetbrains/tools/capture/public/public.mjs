// Captures jetbrains.com public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The marketing
// site paints one scheme per page (home is a dark campaign, store/help are light). There
// is no user theme switch, so every shot is labelled light. Desktop 1440x900 at 1x,
// mobile 390x844 at 2x. Cookie banner (#ch2-dialog) is hidden, never answered.
// Nothing is submitted, purchased, downloaded or signed into. Menu and search are
// local UI toggles. account.jetbrains.com/login is shot at rest. Continue with
// email is opened on /signup so the email field can be measured; Continue after
// the email is never pressed here (that submit hit reCAPTCHA).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, ACCOUNT, patch } from './lib.mjs';

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
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
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

async function openMenu(p) {
  const b = p.getByRole('button', { name: 'Products' }).first();
  if (await b.count()) { await b.click(); await wait(p, 900); }
}
async function openSearch(p) {
  const b = p.getByRole('button', { name: 'Open search' }).first();
  if (await b.count()) { await b.click(); await wait(p, 800); }
}
async function openMobileMenu(p) {
  const b = p.getByRole('button', { name: 'Open main menu' }).first();
  if (await b.count()) { await b.click(); await wait(p, 900); }
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => { await openMenu(p); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('search', async () => { await openSearch(p); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 300); });
  } },
  idea: { path: '/idea/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  products: { path: '/products/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  store: { path: '/store/?section=personal&billing=yearly', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/help/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { path: '/company/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  education: { path: '/education/', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/legal/docs/privacy/privacy/', run: async (p, S) => { await S.view('default'); } },
  login: { url: ACCOUNT + '/login', run: async (p, S) => { await S.view('default'); } },
  'signup-email': { url: ACCOUNT + '/signup', run: async (p, S) => {
    await p.getByRole('button', { name: 'Continue with email', exact: true }).click();
    await wait(p, 1500);
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => { await openMobileMenu(p); await S.view('menu'); });
  } },
  idea: { path: '/idea/', run: async (p, S) => { await S.view('default'); } },
  store: { path: '/store/?section=personal&billing=yearly', run: async (p, S) => { await S.view('default'); } },
  products: { path: '/products/', run: async (p, S) => { await S.view('default'); } },
  login: { url: ACCOUNT + '/login', run: async (p, S) => { await S.view('default'); } },
  'signup-email': { url: ACCOUNT + '/signup', run: async (p, S) => {
    await p.getByRole('button', { name: 'Continue with email', exact: true }).click();
    await wait(p, 1500);
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const url = spec.url || (BASE + spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
