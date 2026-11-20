// Captures glorify.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The
// marketing pages paint light only — glorify.com is a Framer site, color-scheme
// normal with no dark media query. app.glorify.com paints its dark chrome on
// the signed-out auth cards and the anonymous editor, so those shots are named
// `-app` to keep the surface in the filename. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
//
// Nothing is sent, bought or signed into: the only activations are local UI
// toggles — the marketing nav's "Features" dropdown (hover), the pricing
// billing switcher, the mobile burger menu, the editor's inspector tabs, the
// "Try with Placeholder Image" card and the Craft dialog's style pick, on a
// scratch file the SPA itself creates for a signed-out visitor. "Add to canvas"
// starts an AI generation and is never pressed. The sign-in and sign-up forms
// are shot at rest, never submitted; Login, Signup, Share, Download and every
// "Start a free trial" link are shot and measured, never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP, LOGIN_URL, SIGNUP_URL, DESIGNER_URL } from './lib.mjs';

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
    // Autoplaying hero videos can stall a full-page raster; pausing media and
    // allowing 120s keeps the shot on heavy pages.
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW)) {
      if (old === `${this.prefix}-${name}.png` || old === `${this.prefix}-${name}.png.capture.json`
          || (old.startsWith(`${this.prefix}-${name}.part`) && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.unlinkSync(`${RAW}/${old}`);
    }
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
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens the marketing nav's "Features" dropdown — a Framer nav item that opens
// its panel on hover. A local UI state; its links are never followed.
async function featuresMenu(p, S, shotName) {
  const t = p.locator('[data-framer-name="Features"], [data-framer-name*="Feature"]').filter({ hasText: /features/i }).filter({ visible: true }).first();
  const fb = p.locator('a, div').filter({ hasText: /^Features$/ }).filter({ visible: true }).first();
  const trig = (await t.count()) ? t : fb;
  if (!(await trig.count())) { log('  ! no Features nav trigger'); return; }
  await trig.hover();
  await wait(p, 1400);
  const open = await p.evaluate(() => {
    const els = [...document.querySelectorAll('a[href*="features/"], a[href*="mockup"], a[href*="background-remover"]')];
    return els.some((a) => { const r = a.getBoundingClientRect(); return r.y > 40 && r.y < 400 && r.width > 80; });
  }).catch(() => false);
  if (!open) { log('  ! features dropdown did not report open'); }
  await S.view(shotName);
  await p.mouse.move(700, 600);
  await wait(p, 600);
}

// Clicks the pricing billing switcher — a Framer variant toggle that only
// swaps the displayed prices (Monthly / Yearly). A local UI toggle.
async function billingTab(p, S, tabRe, shotName) {
  const t = await p.evaluate((src) => {
    const re = new RegExp(src, 'i');
    const els = [...document.querySelectorAll('div, a, button, span, p')].filter((el) => {
      const r = el.getBoundingClientRect();
      const own = (el.innerText || '').trim();
      return r.width > 30 && r.height > 10 && r.y > 0 && r.y < innerHeight && own.length < 30 && re.test(own) && ![...el.children].some((c) => (c.innerText || '').trim() === own);
    });
    if (!els.length) return null;
    const el = els[0];
    el.setAttribute('data-m-billing', '1');
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2, t: (el.innerText || '').slice(0, 30) };
  }, tabRe.source);
  if (!t) { log('  ! no billing toggle', tabRe); return; }
  await p.mouse.click(t.x, t.y);
  await wait(p, 1200);
  await p.evaluate(() => scrollTo(0, 0));
  await S.view(shotName);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('features-menu', () => featuresMenu(p, S, 'features-menu'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('billed-yearly', () => billingTab(p, S, /yearly|annual/i, 'billed-yearly'));
    await step('billed-monthly', () => billingTab(p, S, /monthly/i, 'billed-monthly'));
    await S.full();
  } },
  'feature-bg': { url: BASE + '/features/background-remover', wait: 9000, theme: 'light', run: BOTH },
  templates: { url: BASE + '/templates', wait: 9000, theme: 'light', run: BOTH },
  marketplace: { url: BASE + '/template-marketplace', wait: 9000, theme: 'light', run: BOTH },
  learn: { url: BASE + '/learn', wait: 9000, theme: 'light', run: BOTH },
  'learn-article': { url: BASE + '/learn/facebook-ad-sizes-best-practices-2024', wait: 9000, theme: 'light', run: BOTH },
  team: { url: BASE + '/team', wait: 8000, theme: 'light', run: BOTH },
  affiliates: { url: BASE + '/affiliates', wait: 8000, theme: 'light', run: BOTH },
  webinars: { url: BASE + '/webinars', wait: 8000, theme: 'light', run: BOTH },
  'submit-template': { url: BASE + '/submit-template', wait: 8000, theme: 'light', run: BOTH },
  'canva-alternative': { url: BASE + '/canva-alternative', wait: 8000, theme: 'light', run: BOTH },
  terms: { url: BASE + '/terms-of-service', wait: 7000, theme: 'light', run: BOTH },
  privacy: { url: BASE + '/privacy-policy', wait: 7000, theme: 'light', run: BOTH },
  login: { url: LOGIN_URL, wait: 9000, theme: 'app', run: BOTH },
  register: { url: SIGNUP_URL, wait: 9000, theme: 'app', run: BOTH },
  designer: { url: DESIGNER_URL, wait: 14000, theme: 'app', run: async (p, S) => {
    await S.view('default');
    // The advertised Play-for-free path on a scratch file the SPA created:
    // placeholder image → Craft dialog → pick a style → Add to canvas.
    const ph = p.locator('a,button,div,span').filter({ hasText: /Placeholder Image/i }).filter({ visible: true }).last();
    if (await ph.count()) {
      await step('placeholder', async () => {
        await ph.click({ timeout: 6000 });
        await wait(p, 18000);
        await S.view('dialog');
      });
      await step('style-pick', async () => {
        const st = p.locator('div,button').filter({ hasText: /^Modern$/ }).filter({ visible: true }).last();
        if (!(await st.count())) return;
        await st.click({ timeout: 5000 });
        await wait(p, 2000);
        await S.view('style-picked');
      });
      // Add to canvas: a boundary, not a step. It runs a server-side AI generation for the visitor (generation
      // quota on a live service), so the capture stops at the enabled button. The committed designer-*-canvas
      // shot was taken past that step (README, What to distrust).
      await step('layers-tab', async () => {
        const tab = p.locator('div,button,span').filter({ hasText: /^LAYERS$/ }).filter({ visible: true }).first();
        if (!(await tab.count())) return;
        await clickEl(tab, 4000);
        await wait(p, 1200);
        await S.view('layers');
      });
    } else log('  ! no Placeholder Image card; onboarding only');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    // The mobile hero's reveal animation runs on intersection: without a
    // scroll nudge the 390px hero captures empty while the -full stitch
    // (which scrolls the whole page) paints it.
    await p.evaluate(() => scrollTo(0, 400));
    await wait(p, 800);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 1500);
    await S.view('default');
    await step('menu', async () => {
      // The burger in the Top nav opens the mobile menu — a local UI toggle;
      // its links are never followed.
      // The burger is the 60x60 "Menu Icon" at the top right — NOT
      // [data-framer-name="Menu"], which is the whole menu overlay (tapping
      // its centre would press a link inside and navigate away).
      const t = p.locator('[data-framer-name="Menu Icon"], button[aria-label*="menu" i]').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await t.tap({ timeout: 4000 }).catch(() => t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click())));
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: BOTH },
  login: { url: LOGIN_URL, wait: 9000, theme: 'app', run: async (p, S) => { await S.view('default'); } },
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
  log(name, spec.url);
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
