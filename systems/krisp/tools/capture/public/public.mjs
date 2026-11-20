// Captures Krisp's public marketing pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Krisp's marketing site
// ships one light theme (krisp-v4), so there is no dark run. Desktop shots are 1440x900 at 1x,
// mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, created, signed into or consented: the only presses are a nav dropdown open,
// the pricing Monthly/Annually toggle, an FAQ summary, and the phone menu. OneTrust is hidden,
// never clicked. Sign in, Get Krisp, Book a demo, Try it Free and the contact-sales form are
// not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  for (let y = 0; y < Math.min(h, 14000); y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 600);
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
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openNav(p, label) {
  const item = p.locator('header.new a, header a').filter({ hasText: label }).first();
  await item.hover();
  await wait(p, 500);
  await item.click();
  await wait(p, 700);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-menu', async () => { await openNav(p, 'AI Meeting Assistant'); await S.view('nav-menu'); await p.keyboard.press('Escape'); await p.mouse.click(700, 500); await wait(p, 400); });
    await step('faq', async () => {
      const item = p.locator('.faq_item, .faq-item, details, .accordion_item, [class*="faq"] summary, [class*="faq"] .question').first();
      if (await item.count()) { await item.scrollIntoViewIfNeeded(); await item.click(); await wait(p, 600); await S.view('faq-open'); }
    });
  } },
  pricing: { path: '/pricing/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      const monthly = p.getByText('Monthly', { exact: true }).first();
      await monthly.scrollIntoViewIfNeeded();
      await monthly.click();
      await wait(p, 700);
      await S.view('monthly');
    });
  } },
  assistant: { path: '/ai-meeting-assistant/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  noise: { path: '/noise-cancellation/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  customers: { path: '/customers/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about-us/', run: async (p, S) => { await S.view('default'); } },
  security: { path: '/security/', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers/', run: async (p, S) => { await S.view('default'); } },
  'not-found': { path: '/download/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const btn = p.locator('header .burger, .burger').first();
      if (await btn.count()) { await btn.click(); await wait(p, 700); await S.view('menu'); }
    });
  } },
  pricing: { path: '/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  assistant: { path: '/ai-meeting-assistant/', run: async (p, S) => { await S.view('default'); } },
};

async function mask(context) {
}

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await mask(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 3500);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
