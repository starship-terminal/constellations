// Captures kit.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// kit.com page paints light — there is no user theme toggle and no dark mode.
// app.kit.com/users/login is the signed-out edge of the product app, captured
// at rest. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full`
// shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates
// at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's Features / Use Cases / Resources buttons
// (aria-haspopup), the mobile menu, pricing FAQ summaries, and the features
// search field (typed, then cleared). Login, signup, demo request and every
// checkout link are measured, never followed. Any consent overlay is hidden,
// never answered.
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // A fresh full capture invalidates the previous whole-image output first:
    // the earlier name.png, its .capture.json sidecar and every stale part
    // tile. If the tiled capture below now fails before writing its first
    // PNG, quantize.py finds no name.png to republish — an old image can
    // never ride in on a new run — and a partial tile set dies on the
    // contiguous-run check in check_tiles instead of stitching short.
    for (const old of fs.readdirSync(RAW)) {
      if (old === `${this.prefix}-${name}.png` || old === `${this.prefix}-${name}.png.capture.json`
          || (old.startsWith(`${this.prefix}-${name}.part`) && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.unlinkSync(`${RAW}/${old}`);
    }
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
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens one of the #mega-nav dropdowns (Features / Use Cases / Resources —
// buttons with aria-haspopup, local UI toggles, never followed) and shoots
// the panel.
async function navMenu(p, S, name) {
  const btn = p.locator('#mega-nav button[aria-haspopup]').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no', name, 'trigger'); return; }
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await clickEl(btn, 4000).catch(() => {});
    await wait(p, 800);
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 800); }
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-features', () => navMenu(p, S, 'Features'));
    await step('menu-use-cases', () => navMenu(p, S, 'Use Cases'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const s = p.locator('summary').filter({ hasText: /How many emails/i }).first();
      if (!(await s.count())) return;
      await s.scrollIntoViewIfNeeded();
      await clickEl(s, 4000);
      await wait(p, 700);
      await S.view('faq-open');
    });
    await S.full();
  } },
  features: { url: BASE + '/features', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const f = p.locator('#feature-explorer-search');
      if (!(await f.count())) return;
      await f.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  'features-email': { url: BASE + '/features/email-marketing', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'request-demo': { url: BASE + '/request-demo', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  compare: { url: BASE + '/compare/mailchimp', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  migrations: { url: BASE + '/migrations', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  brand: { url: BASE + '/brand', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy', wait: 4000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  login: { url: LOGIN_URL, wait: 6000, theme: 'light', run: async (p, S) => {
    await p.locator('input[name="user[email]"], input[type="email"]').first().fill('').catch(() => {});
    await p.locator('input[name="user[password]"], input[type="password"]').first().fill('').catch(() => {});
    // The empty fields paint jane@example.com and a dotted password as CSS
    // placeholders. Hide that paint so the stored shot is an empty form.
    await p.addStyleTag({ content: 'input::placeholder{color:transparent!important} input::-webkit-input-placeholder{color:transparent!important}' }).catch(() => {});
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const ham = p.locator('#mega-nav button[aria-label="Toggle mobile menu"], button[aria-label="Toggle mobile menu"]').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham, 4000);
      await wait(p, 900);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { url: BASE + '/features', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 6000, theme: 'light', run: async (p, S) => {
    await p.locator('input[name="user[email]"], input[type="email"]').first().fill('').catch(() => {});
    await p.locator('input[name="user[password]"], input[type="password"]').first().fill('').catch(() => {});
    // The empty fields paint jane@example.com and a dotted password as CSS
    // placeholders. Hide that paint so the stored shot is an empty form.
    await p.addStyleTag({ content: 'input::placeholder{color:transparent!important} input::-webkit-input-placeholder{color:transparent!important}' }).catch(() => {});
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
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
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
