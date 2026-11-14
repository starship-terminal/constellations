// Captures faire.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. faire.com paints one
// light theme signed out (no theme attribute, no user toggle); the sign-in and sign-up dialogs
// are reached by ?signIn=1/?signUp=1 over the home page and are shot as mounted, never
// submitted. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the header's
// "All categories" dropdown and the mobile Menu button. The /apply form, the search field and
// the auth dialogs are shot at rest, never submitted. Product tiles link to ?signUp=product —
// the sign-up dialog — and are never followed. The OneTrust consent layer is hidden, never
// answered, and the intermittent Cloudflare edge challenge is waited out, never solved.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, SIGNIN_URL, SIGNUP_URL } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Opens the header's "All categories" dropdown — a local UI toggle, never a
// link — and shoots the panel. Focus+Enter is tried when a pointer activation
// does not flip it.
async function allCategories(p, S) {
  const btn = p.locator('button').filter({ hasText: /^\s*All categories\s*$/ }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no All categories button'); return; }
  const open = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true'
    || await p.evaluate(() => !!([...document.querySelectorAll('[role="menu"],[role="listbox"],header [class*="dropdown" i],header [class*="menu" i]')].find((x) => { const r = x.getBoundingClientRect(); const cs = getComputedStyle(x); return r.height > 120 && /\S/.test(x.textContent || '') && cs.visibility !== 'hidden' && cs.opacity !== '0'; }))).catch(() => false);
  for (let i = 0; i < 3 && !(await open()); i++) {
    await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    await wait(p, 800);
    if (!(await open())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 800); }
  }
  if (!(await open())) { log('  ! All categories did not report open'); return; }
  await S.view('categories-menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('categories-menu', () => allCategories(p, S));
    await S.full();
  } },
  'category-home-decor': { url: BASE + '/category/Home%20Decor', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'category-new-products': { url: BASE + '/category/New%20Products', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  brand: { url: BASE + '/brand/b_d72c56fe', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'suppliers-candles': { url: BASE + '/suppliers/Home%20Decor/subcategory/Candles%20%26%20Holders/Candles', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'suppliers-all': { url: BASE + '/suppliers/All%20Brands', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'how-faire-works': { url: BASE + '/how-faire-works', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  news: { url: BASE + '/news', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  careers: { url: BASE + '/careers', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'large-retailers': { url: BASE + '/large-retailers', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'point-of-sale': { url: BASE + '/point-of-sale/about', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  markets: { url: BASE + '/markets', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  support: { url: BASE + '/support', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  affiliates: { url: BASE + '/affiliates', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  apply: { url: BASE + '/apply', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: SIGNIN_URL, wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: SIGNUP_URL, wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  notfound: { url: BASE + '/pagenotfound', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tos: { url: BASE + '/tos', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's "Menu button" (aria-label) toggles the nav drawer — a
      // local UI toggle; its links are never followed.
      const ham = p.locator('button[aria-label*="Menu" i], header button').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      const open = () => p.evaluate(() => !!([...document.querySelectorAll('[role="dialog"],body > div[class*="drawer" i],[class*="menu" i][class*="open" i]')].find((x) => {
        const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
        return r.height > 300 && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
      }))).catch(() => false);
      for (let i = 0; i < 3 && !(await open()); i++) {
        await ham.click({ timeout: 4000 }).catch(() => ham.evaluate((el) => el.click()));
        await wait(p, 900);
        if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 900); }
      }
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await p.evaluate(() => document.querySelectorAll('[role="dialog"] .close, [aria-label*="Close" i]').forEach((x) => x.style.setProperty('display', 'none', 'important'))).catch(() => {});
    });
    await S.full();
  } },
  'category-home-decor': { url: BASE + '/category/Home%20Decor', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  apply: { url: BASE + '/apply', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: SIGNIN_URL, wait: 9000, run: async (p, S) => {
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
