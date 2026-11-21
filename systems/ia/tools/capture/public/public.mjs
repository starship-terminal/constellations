// Captures iA Writer's public pages on ia.net into RAW (full-colour PNGs).
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The
// Writer marketing pages paint a light page and ship no theme switch.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x. Nothing is
// submitted, downloaded, or bought. Presses are the menu, one review "More",
// and the Notebook shipping dialog (opened, then closed). Store, App Store,
// and mailto links are not followed. Download buttons are not pressed.
const ADAPTED_FOR = 'ia-writer';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';
void ADAPTED_FOR;
import { scrubConsole } from '../no-query.mjs';
scrubConsole();   // logs are committed: no query, from a locator or a page URL, is printed

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
    const MAXH = Math.min(8 * chunk, 9000);
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const notNow = async (p) => { const b = p.getByRole('button', { name: 'Not now' }); if (await b.count()) { await b.click(); await wait(p, 1200); } };
const gate = async (p) => { const b = p.getByRole('button', { name: 'Continue', exact: true }); if (await b.count()) { await b.click(); await wait(p, 4000); } };
const pause = async (p) => { const b = p.getByRole('button', { name: /^Pause/ }); if (await b.count()) { await b.first().click().catch(() => {}); await wait(p, 600); } };

const desktop = {
  home: { path: '/writer', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('summary[aria-label="Menu"]').click();
      await wait(p, 600);
      await S.view('menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('quote', async () => {
      const more = p.locator('button.markdown-section__quote-toggle').first();
      await more.scrollIntoViewIfNeeded();
      await more.click();
      await wait(p, 500);
      await S.view('quote');
    });
    await step('shipping', async () => {
      await p.evaluate(() => scrollTo(0, document.body.scrollHeight));
      await wait(p, 400);
      const buy = p.locator('a.open-lightbox, a.page-teasers__buy').first();
      if (await buy.count()) {
        await buy.scrollIntoViewIfNeeded();
        await buy.click();
        await wait(p, 700);
        await S.view('shipping');
        const close = p.locator('button.notebook-shipping-dialog__close').first();
        if (await close.count()) await close.click();
      }
    });
    await p.evaluate(() => scrollTo(0, 0));
    await S.full();
  } },
  pricing: { path: '/writer/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  download: { path: '/writer/download', run: async (p, S) => { await S.view('default'); await S.full(); } },
  support: { path: '/writer/support', run: async (p, S) => { await S.view('default'); await S.full(); } },
  extras: { path: '/downloads/writer', run: async (p, S) => { await S.view('default'); await S.full(); } },
  topics: { path: '/topics/category/writer', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/writer', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('summary[aria-label="Menu"]').click();
      await wait(p, 600);
      await S.view('menu');
    });
    await S.full();
  } },
  pricing: { path: '/writer/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  download: { path: '/writer/download', run: async (p, S) => { await S.view('default'); } },
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
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
