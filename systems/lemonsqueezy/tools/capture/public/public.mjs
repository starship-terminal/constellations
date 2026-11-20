// Captures Lemon Squeezy's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/lemonsqueezy/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Desktop shots are 1440x900 at 1x. Mobile shots are 390x844 at 2x. *-full
// shots are 1x. A page taller than one GPU texture is saved as part tiles
// (capped at 8). Nothing is signed into, submitted or purchased. Consent
// overlays are hidden, never clicked.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideConsent, chromium, UA, UA_MOBILE, BASE, DOCS, AUTH } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 12000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, animations: 'disabled' }, this.requested);
    this.count++;
    log('  shot', name);
  }
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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, animations: 'disabled' }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, animations: 'disabled', clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => {
      const q = p.locator('.landing-page .accordion_question, .section-faq.landing-page .accordion_question').first();
      if (await q.count()) { await q.scrollIntoViewIfNeeded(); await q.click(); await wait(p, 500); await S.view('faq-open'); }
    });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { url: BASE + '/help', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { url: BASE + '/blog/saying-goodbye-to-lemon-squeezy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { url: BASE + '/privacy', run: async (p, S) => { await S.view('default'); } },
  terms: { url: BASE + '/terms', run: async (p, S) => { await S.view('default'); } },
  charge: { url: BASE + '/why-did-lemon-squeeezy-charge-me', run: async (p, S) => { await S.view('default'); } },
  creators: { url: BASE + '/creators-guide', run: async (p, S) => { await S.view('default'); } },
  notfound: { url: BASE + '/features', run: async (p, S) => { await S.view('default'); } },
  docs: { url: DOCS + '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-help': { url: DOCS + '/help', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.getByRole('button', { name: /open search/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('search'); await p.keyboard.press('Escape'); }
    });
  } },
  'docs-api': { url: DOCS + '/api', run: async (p, S) => { await S.view('default'); } },
  'docs-migration': { url: DOCS + '/migration', run: async (p, S) => { await S.view('default'); } },
  login: { url: AUTH + '/login', run: async (p, S) => {
    await S.view('default');
    await step('email-focused', async () => {
      const f = p.locator('input[type="email"], input[name="email"]').first();
      if (await f.count()) { await f.click(); await wait(p, 300); await S.view('email-focused'); }
    });
  } },
  register: { url: AUTH + '/register', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      const b = p.locator('.w-nav-button, .nav_menu-mobile-button').first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('menu'); }
    });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: DOCS + '/', run: async (p, S) => { await S.view('default'); } },
  'docs-help': { url: DOCS + '/help', run: async (p, S) => { await S.view('default'); } },
  login: { url: AUTH + '/login', run: async (p, S) => { await S.view('default'); } },
  help: { url: BASE + '/help', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(p, spec.wait || 1800);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
