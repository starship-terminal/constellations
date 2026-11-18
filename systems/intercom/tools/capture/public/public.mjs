// Captures intercom.com's signed-out pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Intercom ships one theme
// (body.theme-light; no theme-dark rules and no theme switch anywhere), so there is no dark run.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than
// one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, created or signed into: the only presses are the nav's own Product/Resources menu
// triggers, the pricing billing toggle (a local UI state), a FAQ accordion, the mobile menu button
// and a contact-sales select's own listbox. Start free trial, Log in, Contact sales submit, Next and
// every signup/checkout path are never pressed; the contact-sales form is never advanced or sent.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, chromium, UA, UA_MOBILE, BASE, patch } from './lib.mjs';

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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, timeout: 90000 }, this.requested); this.count++; log('  shot', name); }
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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, timeout: 90000 }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, timeout: 90000 }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The nav's Product/Resources triggers open a mega-menu panel; hovering opens
// it on desktop. Never navigated: the trigger is a button, not a link.
async function openNavMenu(p, name = 'Product') {
  const t = p.getByRole('button', { name, exact: true }).first();
  await t.hover().catch(() => {});
  await wait(p, 900);
  const expanded = await t.getAttribute('aria-expanded').catch(() => null);
  if (expanded !== 'true') { await t.click().catch(() => {}); await wait(p, 900); }
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-menu', async () => { await p.evaluate(() => scrollTo(0, 0)); await openNavMenu(p, 'Product'); await S.view('nav-menu'); await p.keyboard.press('Escape'); });
    await step('accordion', async () => {
      const acc = p.locator('[class*="accordion"] button, [data-slot] button, button').filter({ hasText: /\?/ }).first();
      if (await acc.count()) { await acc.scrollIntoViewIfNeeded(); await acc.click(); await wait(p, 900); await S.view('accordion'); }
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      const t = p.getByRole('button', { name: 'Billed monthly' }).first();
      if (await t.count()) { await t.scrollIntoViewIfNeeded(); await t.click(); await wait(p, 1200); await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400); await S.view('monthly'); await p.getByRole('button', { name: 'Billed annually' }).first().click().catch(() => {}); }
    });
    await step('faq', async () => {
      const q2 = p.locator('button').filter({ hasText: /\?/ }).last();
      if (await q2.count()) { await q2.scrollIntoViewIfNeeded(); await q2.click(); await wait(p, 900); await S.view('faq'); }
    });
  } },
  helpdesk: { path: '/helpdesk', run: async (p, S) => { await S.view('default'); await S.full(); } },
  inbox: { path: '/helpdesk/inbox', run: async (p, S) => { await S.view('default'); await S.full(); } },
  copilot: { path: '/helpdesk/copilot', run: async (p, S) => { await S.view('default'); await S.full(); } },
  customers: { path: '/customers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'view-demos': { path: '/view-demos', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'contact-sales': { path: '/contact-sales', run: async (p, S) => {
    await S.view('default');
    await S.full();
    // A Base UI select's own listbox: opened by its trigger, nothing chosen, Escape to close.
    await step('select-open', async () => {
      const t = p.getByRole('combobox').or(p.locator('button').filter({ hasText: /^Select/ })).first();
      if (await t.count()) { await t.click(); await wait(p, 900); await S.view('select-open'); await p.keyboard.press('Escape'); }
    });
  } },
  'why-choose': { path: '/why-choose-intercom', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/help/en/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    // The help center search field focused (never typed, never submitted).
    await step('search-focused', async () => {
      const f = p.locator('input[type="search"], input[placeholder*="Search"]').first();
      if (await f.count()) { await f.click(); await wait(p, 600); await S.view('search-focused'); }
    });
  } },
  changes: { path: '/changes/en', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b2 = p.getByRole('button', { name: /menu|navigation/i }).first();
      if (await b2.count()) { await b2.click(); await wait(p, 1200); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  helpdesk: { path: '/helpdesk', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { path: '/help/en/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'contact-sales': { path: '/contact-sales', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
    await wait(p, spec.wait || 7000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
