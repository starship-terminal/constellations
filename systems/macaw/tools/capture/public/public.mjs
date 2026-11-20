// Captures Macaw's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a mobile- prefix.
// Macaw ships one painted theme (light). Desktop is 1440x900 at 1x.
// Phone is 390x844 at 2x. *-full shots are 1x.
// Nothing is signed into, submitted, purchased or consented: overlays are hidden.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium, UA, UA_MOBILE, BASE, hideOverlays } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// The kit helper's dimension check, inlined: a PNG whose size is not what the viewport, clip and
// scale ask for is deleted and the shot fails, instead of being kept with a sidecar that says it is fine.
function checkDimensions(target, opts, requested) {
  const png = fs.readFileSync(target);
  const width = png.readUInt32BE(16), height = png.readUInt32BE(20);
  const dpr = requested.deviceScaleFactor || 1;
  const want = opts.clip
    ? { width: Math.round(opts.clip.width * dpr), height: Math.round(opts.clip.height * dpr) }
    : { width: Math.round(requested.viewport.width * dpr),
        // A whole-page shot is checked against the document height the caller measured (opts.docHeight).
        height: Math.round((opts.fullPage ? opts.docHeight : requested.viewport.height) * dpr) };
  if (opts.fullPage && !opts.clip && !opts.docHeight) throw new Error('a full-page shot needs opts.docHeight to be checked');
  if (Math.abs(width - want.width) > 1 || Math.abs(height - want.height) > 1) {
    fs.unlinkSync(target);
    throw new Error(`dimension mismatch: ${path.basename(target)} is ${width}x${height}, expected ${want.width}x${want.height}`);
  }
  return { width, height };
}

async function screenshotWithMetadata(page, opts, requested) {
  const target = opts.path;
  await page.screenshot({ path: target, fullPage: !!opts.fullPage, clip: opts.clip });
  const pixels = checkDimensions(target, opts, requested);
  const side = {
    pixels,
    dimensionCheck: 'pass',
    schemaVersion: 1,
    capturedAt: new Date().toISOString(),
    screenshot: path.basename(target),
    requested,
    capture: opts.clip ? { mode: 'clip', clip: opts.clip } : { mode: opts.fullPage ? 'fullPage' : 'viewport' },
  };
  fs.writeFileSync(target + '.capture.json', JSON.stringify(side, null, 1) + '\n');
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, docHeight: hCap }, this.requested);
    else {
      const written = [];
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        const part = `${f}.part${i}.png`;
        await screenshotWithMetadata(p, { path: part, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
        written.push(part);
      }
      const expected = Math.ceil(hCap / chunk);
      if (written.length !== expected || written.some((part) => !fs.existsSync(part))) {
        throw new Error(`${name}: wrote ${written.length} of ${expected} tiles`);
      }
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p) {
  const toggle = p.locator('.navbar_dropdown-toggle').first();
  await toggle.hover();
  await wait(p, 500);
}

async function openMobileNav(p) {
  const btn = p.locator('.navbar_menu-button, .w-nav-button').first();
  await btn.click();
  await wait(p, 600);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-hover', async () => {
      await p.locator('.navbar_link, .w-nav-link').filter({ hasText: 'Pricing' }).first().hover();
      await wait(p, 350);
      await S.view('nav-hover');
    });
    await step('resources-menu', async () => {
      await openMenu(p);
      await S.view('resources-menu');
    });
    await step('primary-hover', async () => {
      await p.mouse.move(8, 8);
      await p.locator('a.button').filter({ hasText: 'Start for free' }).first().hover();
      await wait(p, 350);
      await S.view('primary-hover');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('monthly', async () => {
      await p.locator('.pricing-toggle-button').filter({ hasText: 'Monthly' }).first().click();
      await wait(p, 500);
      await S.view('monthly');
    });
    await step('faq-open', async () => {
      await p.locator('.faq01_question').first().click();
      await wait(p, 500);
      await p.locator('.faq01_question').first().scrollIntoViewIfNeeded();
      await S.view('faq-open');
    });
  } },
  contact: { path: '/contact-us', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('field-focus', async () => {
      await p.locator('input.form-input').first().focus();
      await wait(p, 300);
      await S.view('field-focus');
    });
    await step('field-filled', async () => {
      const field = p.locator('input.form-input').first();
      await field.fill('Sample');
      await wait(p, 200);
      await S.view('field-filled');
      await field.fill('');
    });
    await step('invalid', async () => {
      // Native constraint UI only. The form is not submitted.
      await p.locator('input[type=email]').focus();
      await p.locator('input[type=email]').fill('not-an-email');
      await p.evaluate(() => {
        const f = document.querySelector('form.contact05_form');
        if (f) f.reportValidity();
      });
      await wait(p, 400);
      await S.view('invalid');
      await p.locator('input[type=email]').fill('');
    });
  } },
  tool: { path: '/free-tools/blog-title-generator', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { path: '/terms-and-conditions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  missing: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => { await openMobileNav(p); await S.view('menu'); });
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact-us', run: async (p, S) => { await S.view('default'); } },
  tool: { path: '/free-tools/blog-title-generator', run: async (p, S) => { await S.view('default'); } },
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
    await wait(p, spec.wait || 2200);
    await hideOverlays(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
