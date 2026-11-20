// Captures 1Password's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light). Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are dialog dismissals, the nav
// Business/Personal flyout buttons, a billing-period toggle, and FAQ accordions. The sign-in
// app redirects headless browsers to /unsupported, which is captured as its own surface.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, seedConsent, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots go to a scratch dir outside the repo (the kit's default), never into
// systems/<slug>/raw/: quantize.py reads them from there and writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(fileURLToPath(new URL('../../..', import.meta.url))), 'raw-shots');
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
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // drop this shot's earlier tiles (and sidecars) first: a shorter or capped page would
    // otherwise leave old partN files that quantize.py stitches into the new shot
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // An infinite or growing page reports a scrollHeight without end: tile at most 8 chunks
    // and log the boundary (the kit's cap), never one tile per chunk for ever.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// -- shared bits -------------------------------------------------------------
const clickEl = async (loc, ms = 10000) => {
  await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click()));
};
// Nav flyout: the Business/Personal/Partners/Resources group/nav-item buttons
// open a mega flyout on hover (click as fallback).
const openMenu = async (p) => {
  const btn = p.getByRole('button', { name: 'Business', exact: true })
    .filter({ visible: true }).first();
  if (!(await btn.count())) return;
  await btn.hover(); await wait(p, 1400);
  const fly = p.locator('[class*="flyout" i], [class*="dropdown" i], [class*="mega" i], header [role="dialog"]')
    .filter({ visible: true }).first();
  if (!(await fly.count())) { await clickEl(btn); await wait(p, 1600); }
};
// The pricing FAQ's toggles carry an "Answer to '…'" label; a page-wide
// aria-expanded query hits the header's nav flyout buttons first.
const openAccordion = async (p) => {
  const a = p.locator('button[aria-label^="Answer to"][aria-expanded="false"], [class*="faq" i] button[aria-expanded="false"], details:not([open]) summary').filter({ visible: true }).first();
  if (await a.count()) { await clickEl(a); await wait(p, 900); return true; }
  return false;
};
// Pricing pages often carry a monthly/annual segmented control.
const flipBilling = async (p) => {
  const t = p.locator('button:has-text("Annual"), button:has-text("Yearly"), button:has-text("Monthly"), [role="tab"]:has-text("Annual"), label:has-text("Annual")')
    .filter({ visible: true }).first();
  if (await t.count()) { await clickEl(t); await wait(p, 1200); return true; }
  return false;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await closePromo(p);
    await S.view('default');
    await step('menu', async () => { await openMenu(p); await S.view('menu'); await p.keyboard.press('Escape'); });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('billing', async () => { if (await flipBilling(p)) await S.view('billing'); });
    await step('faq', async () => { if (await openAccordion(p)) await S.view('faq'); });
    await S.full();
  } },
  product: { path: '/product/enterprise-password-manager', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { path: '/downloads/mac', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  developer: { path: '/developer-security', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/contact-sales', run: async (p, S) => {
    await S.view('default');
    await step('focus', async () => { const i = p.locator('input[type="email"], input[name*="mail" i]').first(); if (await i.count()) { await i.click(); await wait(p, 500); await S.view('focus'); } });
    await S.full();
  } },
  // start.1password.com gates headless browsers to /unsupported; full URL, no BASE.
  account: { path: 'https://start.1password.com/unsupported?l=en', absolute: true, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await closePromo(p);
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button[aria-label*="menu" i], .header-navigation button:has(svg), header button[aria-expanded], button.hamburger')
        .filter({ visible: true }).last();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
    if (!spec.absolute) await seedConsent(p);
    await p.goto(spec.absolute ? spec.path : BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') { await killGeo(p); await closePromo(p); }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
