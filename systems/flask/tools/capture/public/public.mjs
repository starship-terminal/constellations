// Captures flask.do's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// public flask.do page paints the dark `default` theme — the --ds-* layer the
// inline <style id="ds-theme"> block declares on :root and
// [data-ds-theme="default"] — so every shot is -dark; the site ships no light
// variant or toggle. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded
// page truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the mobile
// "Open menu" hamburger, a /pricing FAQ accordion and the billing switch
// (toggled to the "Billed quarterly" view, then back to "Billed yearly") —
// and the demo mock's own "Version" chip.
// The login form is shot at rest, never submitted. No consent banner was
// observed on any route.
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

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('demo-asset-2', async () => {
      // The hero demo's own "Version" chip swaps the mock asset — a local UI
      // toggle in the marketing demo, not a product action.
      const chip = p.locator('button').filter({ hasText: /^Version 2$/ }).filter({ visible: true }).first();
      if (!(await chip.count())) return;
      await chip.evaluate((el) => el.scrollIntoView({ block: 'center' })); await wait(p, 400);
      await chip.click({ timeout: 5000 }).catch(() => chip.evaluate((el) => el.click()));
      await wait(p, 1500);
      await S.view('demo-asset-2');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('faq-open', async () => {
      const q = p.locator('button').filter({ hasText: /storage limit/i }).filter({ visible: true }).first();
      if (!(await q.count())) return;
      await q.evaluate((el) => el.scrollIntoView({ block: 'center' })); await wait(p, 400);
      await q.click({ timeout: 5000 }).catch(() => q.evaluate((el) => el.click()));
      await wait(p, 900);
      await S.view('faq-open');
    });
    await step('billed-quarterly', async () => {
      // The billing switch is a local UI toggle; it is flipped to the
      // quarterly-price view, then flipped back. Scrolled and clicked through
      // evaluate: a Playwright actionability scroll stalls on the pricing
      // page's animated layout.
      const sw = p.locator('[role="switch"]').filter({ visible: true }).last();
      if (!(await sw.count())) return;
      await sw.evaluate((el) => el.scrollIntoView({ block: 'center' }));
      await wait(p, 600);
      await sw.evaluate((el) => el.click());
      await wait(p, 1400);
      await S.view('billed-quarterly');
      await sw.evaluate((el) => el.click()).catch(() => {});
      await wait(p, 800);
    });
    await S.full();
  } },
  mcp: { url: BASE + '/mcp', wait: 7000, theme: 'dark', run: BOTH },
  about: { url: BASE + '/about', wait: 7000, theme: 'dark', run: BOTH },
  security: { url: BASE + '/security', wait: 7000, theme: 'dark', run: BOTH },
  'video-collaboration': { url: BASE + '/video-collaboration', wait: 7000, theme: 'dark', run: BOTH },
  'frame-io-alternative': { url: BASE + '/frame-io-alternative', wait: 7000, theme: 'dark', run: BOTH },
  'privacy-policy': { url: BASE + '/privacy-policy', wait: 6000, theme: 'dark', run: BOTH },
  'terms-of-service': { url: BASE + '/terms-of-service', wait: 6000, theme: 'dark', run: BOTH },
  login: { url: LOGIN_URL, wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile hamburger is an icon-only `button[aria-label="Open menu"]`
      // floating top-right (md:hidden — it exists only at this width).
      const ham = p.locator('button[aria-label="Open menu"]').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'dark', run: BOTH },
  login: { url: LOGIN_URL, wait: 8000, theme: 'dark', run: BOTH },
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
    await wait(p, spec.wait || 8000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
