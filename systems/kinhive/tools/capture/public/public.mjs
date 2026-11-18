// Captures kinhive.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// The live document paints light (no data-app-theme attribute). A dark palette
// exists under prefers-color-scheme and is captured as home-dark-* by a
// separate colorScheme pass, labelled as the system preference, not a toggle.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, *-full shots at CSS
// scale. Nothing is sent, bought or signed into. The only presses are local
// UI toggles: Features and Use Cases nav menus, the mobile menu, and the shop
// cart drawer (0 items). Forms are shot at rest. Consent overlays are hidden,
// never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 120); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW)) {
      if (old === `${this.prefix}-${name}.png` || old === `${this.prefix}-${name}.png.capture.json`
          || (old.startsWith(`${this.prefix}-${name}.part`) && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p, label) {
  const btn = p.getByRole('button', { name: label, exact: true }).first();
  await btn.click({ timeout: 5000 });
  await wait(p, 500);
}

const pageOf = (path, extra = {}) => ({ path, ...extra, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu-features', async () => { await openMenu(p, 'Features'); await S.view('menu-features'); await p.keyboard.press('Escape'); await wait(p, 300); });
    await step('menu-usecases', async () => { await openMenu(p, 'Use Cases'); await S.view('menu-usecases'); await p.keyboard.press('Escape'); await wait(p, 300); });
  } },
  pricing: pageOf('/pricing'),
  about: pageOf('/about'),
  blog: pageOf('/blog'),
  'blog-article': pageOf('/blog/how-to-find-a-cofounder-female-founder'),
  feature: pageOf('/feature/ai-networking-matchmaking-women'),
  cowork: pageOf('/feature/virtual-coworking-women'),
  templates: pageOf('/templates'),
  'template-nda': pageOf('/templates/nda'),
  funding: pageOf('/funding'),
  resources: pageOf('/resources'),
  product: pageOf('/shop/founders-hat'),
  shop: { path: '/shop', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('cart', async () => {
      const cart = p.getByRole('button', { name: /cart/i }).first();
      await cart.click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('cart');
      await p.keyboard.press('Escape');
    });
  } },
  contact: pageOf('/contact'),
  join: pageOf('/join'),
  signin: pageOf('/sign-in'),
  privacy: pageOf('/privacy'),
  terms: pageOf('/terms'),
  accessibility: pageOf('/accessibility'),
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('drawer', async () => {
      const btn = p.getByRole('button', { name: 'Open menu' });
      await btn.click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('drawer');
    });
  } },
  pricing: pageOf('/pricing'),
  join: pageOf('/join'),
  signin: pageOf('/sign-in'),
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, scheme: 'light' })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, scheme: 'light' })),
  { k: 'home', mob: false, scheme: 'dark', spec: desktop.home },
];
for (const { k, mob, scheme, spec: given } of runs) {
  const theme = scheme === 'dark' ? 'dark' : 'light';
  const name = (mob ? 'mobile-' : '') + k;
  const fileName = name;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(name + '-' + theme) && !pageArg.includes(theme + '-' + name)) continue;
  if (scheme === 'dark' && pageArg.length && !pageArg.some((a) => a.includes('dark'))) continue;
  const spec = given || (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
    colorScheme: scheme,
  });
  await patch(ctx);
  const p = await ctx.newPage();
  const prefix = scheme === 'dark' ? `${name}-dark` : `${name}-light`;
  log(prefix);
  const S = new Shooter(p, prefix, vw, vh, dpr, BASE + spec.path);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2200);
    if (scheme === 'dark') {
      // The dark palette is scoped to html[data-app-theme=system] inside
      // prefers-color-scheme: dark. The live document leaves the attribute
      // unset, so colorScheme alone does not paint it. Setting the attribute
      // is how the declared palette is reached; it is not a user toggle.
      await p.evaluate(() => document.documentElement.setAttribute('data-app-theme', 'system'));
      await wait(p, 400);
    }
    const ok = await clearChallenge(p, { tries: 3, step: 800 });
    if (!ok) log('  challenge still up', prefix);
    await closePromo(p);
    if (scheme === 'dark') {
      await S.view('default');
      await S.full();
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', prefix, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
