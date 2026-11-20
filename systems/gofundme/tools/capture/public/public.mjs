// Captures gofundme.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// Every public surface of www.gofundme.com paints the consumer `light` theme
// the `--hrt-*` tokens declare on `:where(:root)` — the sheets ship a
// `[data-theme="pro"]` layer for GoFundMe Pro and no dark variant or theme
// switcher — so every shot is -light. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, donated to, bought or signed into: the only activations
// are local UI toggles — the header's Donate/Fundraise/About dropdown panels
// and the phone's nav button. The fundraiser page is shot at rest (Donate
// now/Share/Message measured, never pressed — a press opens the donation
// flow); the /create/fundraiser/category wizard is shot at rest, its
// Continue never submitted; /sign-in is shot as a form, never submitted.
// Any consent layer (Transcend) is hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LOGIN_URL } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl && String(sourceUrl).split(/[?#]/)[0] /* no query or fragment in a sidecar */ }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    // Pages whose demos autoplay video/canvas can stall a full-page raster past
    // the default 30s; pausing media and allowing 120s keeps the shot on heavy
    // pages.
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    try {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    } catch (e) {
      log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Opens one of the header's dropdown panels (Donate / Fundraise / About —
// hrt-header-dropdown-button controls whose hrt-header-dropdown-content panel
// opens on click or hover; the panel's links are never followed). The trigger
// is activated until a panel reports non-zero size, then the shot. Escape and
// a move to the page edge close it afterwards.
async function navMenu(p, S, name) {
  const btn = p.locator('.hrt-header-dropdown-button, button.hrt-header-dropdown-button').filter({ hasText: new RegExp(`^${name}`) }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no', name, 'trigger'); return; }
  // The panels stay mounted (visibility:hidden, opacity:0) when closed, so a
  // non-zero rect proves nothing: the --open class is the real state.
  const open = async () => p.evaluate(() => !!document.querySelector('.hrt-header-dropdown-content--open')).catch(() => false);
  for (let i = 0; i < 4 && !(await open()); i++) {
    if (i === 0) await btn.hover({ timeout: 5000 }).catch(() => {});
    else await btn.click({ timeout: 5000 }).catch(() => {});
    await wait(p, 1200);
  }
  if (!(await open())) { log('  ! menu', name, 'did not report open'); }
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
  await S.view('menu-' + name.toLowerCase());
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
  await p.keyboard.press('Escape').catch(() => {});
  const vw = p.viewportSize()?.width ?? 1440;
  await p.mouse.move(vw - 2, 890); await wait(p, 800);
}

// Picks the first live fundraiser card link on /discover so the fundraiser
// shot is a real public /f/<slug> page the product itself surfaces. The page
// is only ever shot at rest: its Donate/Share/Message controls are measured
// by measure.mjs and never pressed — a press opens the donation flow.
async function firstFundraiser(p) {
  await p.goto(BASE + '/discover', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await wait(p, 8000);
  const href = await p.evaluate(() => {
    const a = [...document.querySelectorAll('a[href^="/f/"]')].find((x) => x.getBoundingClientRect().width > 0);
    return a ? a.getAttribute('href') : null;
  }).catch(() => null);
  return href && /^\/f\/[\w-]+/.test(href) ? href.match(/^\/f\/[\w-]+/)[0] : '/f/help-jong-pil-kim-keep-mun-korean-steakhouse-alive';
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-donate', () => navMenu(p, S, 'Donate'));
    await step('menu-fundraise', () => navMenu(p, S, 'Fundraise'));
    await step('menu-about', () => navMenu(p, S, 'About'));
    await S.full();
  } },
  discover: { url: BASE + '/discover', wait: 10000, theme: 'light', run: BOTH },
  search: { url: BASE + '/s?q=medical', wait: 10000, theme: 'light', run: BOTH },
  fundraiser: { url: null, wait: 12000, theme: 'light', run: async (p, S) => {
    const slug = await firstFundraiser(p);
    await p.goto(BASE + slug, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    S.requested.sanitizedSourceUrl = BASE + slug;  // a real URL (the first live card on /discover)
    await wait(p, 9000);
    await S.view('default');
    await S.full();
  } },
  'how-it-works': { url: BASE + '/c/how-it-works', wait: 9000, theme: 'light', run: BOTH },
  pricing: { url: BASE + '/c/pricing', wait: 9000, theme: 'light', run: BOTH },
  'why-gofundme': { url: BASE + '/c/why-gofundme', wait: 9000, theme: 'light', run: BOTH },
  crowdfunding: { url: BASE + '/c/crowdfunding', wait: 9000, theme: 'light', run: BOTH },
  'fundraising-ideas': { url: BASE + '/c/fundraising-ideas', wait: 9000, theme: 'light', run: BOTH },
  'charity-fundraising': { url: BASE + '/c/charity-fundraising', wait: 9000, theme: 'light', run: BOTH },
  start: { url: BASE + '/c/start', wait: 9000, theme: 'light', run: BOTH },
  about: { url: BASE + '/c/about-us', wait: 9000, theme: 'light', run: BOTH },
  careers: { url: BASE + '/c/careers', wait: 9000, theme: 'light', run: BOTH },
  blog: { url: BASE + '/c/blog', wait: 9000, theme: 'light', run: BOTH },
  safety: { url: BASE + '/c/safety', wait: 9000, theme: 'light', run: BOTH },
  'sign-in': { url: LOGIN_URL, wait: 10000, theme: 'light', allowEmpty: true, run: BOTH },
  create: { url: BASE + '/create/fundraiser/category', wait: 10000, theme: 'light', run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's nav toggle on the phone surface — a local UI toggle;
      // its links are never followed.
      const btn = p.locator('button[aria-label="menu" i], button.hrt-icon-button[aria-label*="menu" i], button[aria-label*="navigation" i]').filter({ visible: true }).first();
      if (!(await btn.count())) { log('  ! no mobile menu toggle found'); return; }
      await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  discover: { url: BASE + '/discover', wait: 10000, theme: 'light', run: BOTH },
  fundraiser: { url: null, wait: 12000, theme: 'light', run: async (p, S) => {
    const slug = await firstFundraiser(p);
    await p.goto(BASE + slug, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    S.requested.sanitizedSourceUrl = BASE + slug;  // a real URL (the first live card on /discover)
    await wait(p, 9000);
    await S.view('default');
    await S.full();
  } },
  'sign-in': { url: LOGIN_URL, wait: 10000, theme: 'light', allowEmpty: true, run: BOTH },
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
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    if (spec.url) {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      // sign-in carries allowEmpty: its empty body reads as a challenge to
      // clearChallenge but is itself the boundary evidence — still shot.
      if (!(await clearChallenge(p)) && !spec.allowEmpty) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
      await wait(p, spec.wait || 8000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
