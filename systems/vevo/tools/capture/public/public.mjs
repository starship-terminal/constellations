// Captures Gauth's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Gauth ships one theme, so there
// is no dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, created or signed into: the only presses are dialog dismissals, tabs, Show more, the
// lesson's own Not now, Continue (the audio gate), Pause, Settings and chapters, and a story card's
// Explore, which opens a published story.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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

const PRESS = '/press/vevo-announces-highly-acclaimed-dscvr-artists-to-watch-list-for-2027';

async function pageShot(p, S) {
  await S.view('default');
  await S.full();
}

async function openMenu(p) {
  const ham = p.locator('#comp-lklqhtjc_r_comp-ldc6q7ym');
  if (await ham.count()) { await ham.click(); await wait(p, 900); }
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await pageShot(p, S);
    await step('video', async () => {
      await p.getByRole('button', { name: /Play video/ }).first().click();
      await wait(p, 1200);
      await S.view('video');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    });
    await step('nav-hover', async () => {
      await p.getByRole('link', { name: 'About', exact: true }).first().hover();
      await wait(p, 400);
      await S.view('nav-hover');
    });
  } },
  about: { path: '/about', run: pageShot },
  originals: { path: '/originals', run: pageShot },
  people: { path: '/people', run: pageShot },
  advertisers: { path: '/for-advertisers', run: pageShot },
  artists: { path: '/vevo-for-artists', run: pageShot },
  newsroom: { path: '/newsroom', run: pageShot },
  blog: { path: '/blog', run: pageShot },
  specs: { path: '/advertising/specs', run: async (p, S) => {
    await S.view('default');
    await step('preroll', async () => {
      await p.getByRole('button', { name: 'Video Preroll' }).first().click();
      await wait(p, 700);
      await S.view('preroll-open');
    });
  } },
  policy: { path: '/advertisingpolicy', run: async (p, S) => { await S.view('default'); } },
  'advertiser-form': { path: '/for-advertisers-contact', run: async (p, S) => {
    await S.view('default');
    await step('field-focus', async () => {
      const name = p.locator('input[name="name"]');
      await name.click();
      await wait(p, 300);
      await S.view('name-focused');
      await name.fill('');
    });
  } },
  'vevo-101': { path: '/vevo-101', run: async (p, S) => { await S.view('default'); } },
  distribution: { path: '/distribution', run: async (p, S) => { await S.view('default'); } },
  glossary: { path: '/glossary', run: async (p, S) => { await S.view('default'); } },
  'artist-support': { path: '/contact-artist-support', run: async (p, S) => { await S.view('default'); } },
  feedback: { path: '/for-artists-feedback', run: async (p, S) => { await S.view('default'); } },
  press: { path: PRESS, run: async (p, S) => {
    await S.view('default');
    await step('share', async () => {
      const more = p.getByRole('button', { name: 'More actions' });
      if (await more.count()) { await more.first().click(); await wait(p, 600); }
      await S.view('share');
    });
  } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms-of-use', run: async (p, S) => { await S.view('default'); } },
  missing: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://www.vevo.com/login', absolute: true, run: async (p, S) => { await S.view('default'); } },
  'password-wall': { path: '/home-old', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMenu(p); await S.view('menu'); });
    await S.full();
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  advertisers: { path: '/for-advertisers', run: async (p, S) => { await S.view('default'); } },
  artists: { path: '/vevo-for-artists', run: async (p, S) => { await S.view('default'); } },
  newsroom: { path: '/newsroom', run: async (p, S) => { await S.view('default'); } },
  'advertiser-form': { path: '/for-advertisers-contact', run: async (p, S) => { await S.view('default'); } },
  press: { path: PRESS, run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.absolute ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
