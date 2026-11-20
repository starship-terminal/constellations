// Captures lovable.dev's public signed-out pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/lovable/raw-shots PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png, except enterprise-form which paints dark
// and is named enterprise-form-dark-*.png. Mobile shots get a `mobile-` prefix.
// Desktop 1440x900 at 1x, mobile 390x844 at 2x. Nothing is sent, signed into,
// purchased or submitted. Consent overlays are hidden, never clicked.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, DOCS } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lovable', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, theme) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.theme = theme;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    // Re-read height immediately before the shot. A page that settles between
    // the measure and the screenshot fails the dimension check.
    const H2 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const hCap2 = Math.min(H2, MAXH);
    // Clip tiles, never fullPage. Playwright's fullPage height and the CSS
    // scrollHeight disagree by more than one pixel on this site at 2x.
    if (hCap2 <= this.p.viewportSize().height) {
      await screenshotWithMetadata(p, { path: f + '.png', clip: { x: 0, y: 0, width: this.vw, height: hCap2 } }, this.requested);
    } else for (let i = 0, y = 0; y < hCap2; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap2 - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

function abs(spec) {
  if (spec.url) return spec.url;
  return (spec.host || BASE) + spec.path;
}

const desktop = {
  home: { path: '/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('solutions-menu', async () => {
      await p.getByRole('button', { name: 'Solutions' }).first().click();
      await wait(p, 700);
      await S.view('solutions-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
  } },
  pricing: { path: '/pricing', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('yearly', async () => {
      const b = p.getByRole('button', { name: /Yearly/ }).first();
      await b.click();
      await wait(p, 600);
      await S.view('yearly');
    });
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /What is a credit/ }).first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 500);
      await S.view('faq-open');
    });
    await S.full();
  } },
  blog: { path: '/blog', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  templates: { path: '/templates', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  'enterprise-landing': { path: '/enterprise-landing', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  'enterprise-form': { path: '/enterprise-form', theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  docs: { url: DOCS + '/introduction/welcome', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.locator('button').filter({ hasText: /Search/ }).first();
      await b.click({ timeout: 8000 });
      await wait(p, 700);
      await S.view('search-open');
      await p.keyboard.press('Escape');
    });
  } },
  'docs-plans': { url: DOCS + '/introduction/plans-and-credits', theme: 'light', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /Navigation menu|Open menu|Menu/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('menu-open'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  docs: { url: DOCS + '/introduction/welcome', theme: 'light', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const theme = spec.theme || 'light';
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, theme);
  try {
    await p.goto(abs(spec), { waitUntil: 'domcontentloaded', timeout: 90000 });
    // A bot check that never clears is not the page: no shot is written for it.
    if (!(await clearChallenge(p))) throw new Error('bot check did not clear');
    await wait(p, spec.wait || 3500);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
