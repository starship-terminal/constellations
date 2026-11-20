// Captures grammarly.com's public signed-out pages into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// grammarly.com ships one theme (there is no switch and prefers-color-scheme
// does not repaint), so every shot is `light`. Desktop shots are 1440x900 at
// 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one
// GPU texture is saved as name.partN.png tiles, which quantize.py stitches
// back together.
// Nothing is sent, created or signed into: the only presses are UI toggles —
// the nav menu buttons, feature tabs, accordion summaries; the grammar
// checker's own copy button is never pressed, and the mobile menu's
// Open/Close buttons. (/plans no longer paints a Monthly/Yearly billing
// switch, so there is no billing toggle to press.) Sample text is typed
// into the free grammar checker and deleted again; nothing is submitted.
// Every "Sign Up", "Log in" submit, "Get Grammarly" and "Request a demo"
// submit is shot and measured, never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, timeout: 120000 }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, timeout: 120000 }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, timeout: 120000 }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Open a top-level nav menu (Product/Work/Education/Resources are the site's
// own menu buttons, UI toggles not links), shot it, then Escape back to rest.
async function navMenu(p, S, label = 'Product') {
  const b = p.locator('header').locator('button, a').filter({ hasText: new RegExp('^' + label + '$') }).first();
  await b.click();
  await wait(p, 900);
  await S.view('nav-' + label.toLowerCase() + '-open');
  await p.keyboard.press('Escape');
  await p.mouse.click(720, 500).catch(() => {});
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('nav-product', () => navMenu(p, S));
    await S.full();
  } },
  features: { path: '/features', run: async (p, S) => {
    await S.view('default');
    await step('tab-selected', async () => {
      const tab = p.locator('button[role="tab"]').filter({ hasText: /Proofreading/ }).first();
      await tab.scrollIntoViewIfNeeded(); await tab.click(); await wait(p, 800);
      await S.view('tab-proofreading');
    });
    await S.full();
  } },
  plans: { path: '/plans', run: async (p, S) => {
    await S.view('default');
    // No billing toggle is painted on the current /plans page (only the three
    // plan columns), so there is no billing-yearly state to capture.
    await S.full();
  } },
  enterprise: { path: '/business/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  business: { path: '/business', run: async (p, S) => { await S.view('default'); await S.full(); } },
  professionals: { path: '/professionals', run: async (p, S) => { await S.view('default'); await S.full(); } },
  students: { path: '/students', run: async (p, S) => { await S.view('default'); await S.full(); } },
  edu: { path: '/edu', run: async (p, S) => { await S.view('default'); await S.full(); } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'ai-agents': { path: '/ai-agents', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'grammar-check': { path: '/grammar-check', run: async (p, S) => {
    await S.view('default');
    // checker: recorded as a boundary, not used. Typed text is sent to Grammarly's
    // server checker for analysis, so no filled state is shot; the editor is at rest.
    await S.full();
  } },
  'plagiarism-checker': { path: '/plagiarism-checker', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'paraphrasing-tool': { path: '/paraphrasing-tool', run: async (p, S) => {
    await S.view('default');
    // paraphraser: recorded as a boundary, not used. Typed text goes to the server
    // for rewriting, so no filled state is shot; the editor is at rest.
    await S.full();
  } },
  'ai-detector': { path: '/ai-detector', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'word-counter': { path: '/word-counter', run: async (p, S) => { await S.view('default'); await S.full(); } },
  desktop: { path: '/desktop', run: async (p, S) => { await S.view('default'); await S.full(); } },
  browser: { path: '/browser', run: async (p, S) => { await S.view('default'); await S.full(); } },
  trust: { path: '/trust', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'contact-sales': { path: '/contact/sales', run: async (p, S) => {
    await S.view('default');
    await step('field-focused', async () => {
      const f = p.locator(M('form_input_')).filter({ visible: true }).first();
      await f.scrollIntoViewIfNeeded(); await f.click({ timeout: 4000 }); await wait(p, 500);
      await S.view('field-focused');
      await p.keyboard.press('Escape').catch(() => {}); await p.mouse.click(1100, 200);
    });
    await S.full();
  } },
  signin: { path: '/signin', run: async (p, S) => {
    await S.view('default');
    await step('email-filled', async () => {
      const f = p.locator('input[type="email"], input[name*="email" i]').filter({ visible: true }).first();
      await f.click({ timeout: 4000 });
      await p.keyboard.type('name@example.com', { delay: 12 });
      await wait(p, 500);
      await S.view('email-filled');
      await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.press('Backspace'); await wait(p, 400);
    });
    await S.full();
  } },
  signup: { path: '/signup', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('button[aria-label*="navigation menu" i], ' + M('openButton_')).first().click();
      await wait(p, 1200);
      await S.view('menu-open');
      await p.locator('button[aria-label*="navigation menu" i], ' + M('closeButton_')).last().click().catch(() => {});
      await wait(p, 600);
    });
    await S.full();
  } },
  plans: { path: '/plans', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'grammar-check': { path: '/grammar-check', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
