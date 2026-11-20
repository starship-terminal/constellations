// Captures jace.ai public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/. Signed-out only. Follows signup as far as
// the OAuth card. Never presses Google, Outlook, Apple, SSO, or a form
// submit. Consent overlays are hidden, never clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, APP, patch, clearChallenge } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'jace', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 120); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p) {
  const b = p.getByRole('button', { name: /open main menu/i });
  if (await b.count()) { await b.first().click(); await wait(p, 700); return true; }
  return false;
}

const desktop = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const q = p.getByRole('button', { name: /How much does Jace AI cost/i });
      if (await q.count()) { await q.first().click(); await wait(p, 500); await q.first().scrollIntoViewIfNeeded(); await S.view('faq-open'); }
    });
    await step('monthly', async () => {
      const b = p.getByRole('button', { name: /^Bill monthly$/i });
      if (await b.count()) { await b.first().click(); await wait(p, 500); await p.evaluate(() => scrollTo(0, 0)); await S.view('monthly'); }
    });
    await S.full();
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  brand: { path: '/brand', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { path: '/docs/guides-getting-started', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gmail: { path: '/integrations/gmail', run: async (p, S) => { await S.view('default'); await S.full(); } },
  lawyers: { path: '/lawyers', run: async (p, S) => { await S.view('default'); } },
  press: { path: '/press', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact/sales', run: async (p, S) => {
    // Boundary: shown at rest. The page ships with sample values in the name
    // and email fields. Clear them so the shot is the empty form. Do not submit.
    await p.evaluate(() => {
      for (const el of document.querySelectorAll('input, textarea')) {
        el.value = '';
        el.setAttribute('placeholder', '');
        el.dispatchEvent(new Event('input', { bubbles: true }));
      }
    });
    await wait(p, 300);
    await S.view('default');
  } },
  signin: { path: APP + '/signin', abs: true, run: async (p, S) => {
    // Boundary: the product sign-in card. No OAuth click, no typing, no submit.
    await S.view('default');
  } },
  signup: { path: APP + '/signup', abs: true, run: async (p, S) => {
    // Signup landing, signed out, shot at rest. Consent boundary: Continue opens a privacy notice
    // whose "Continue to signup" acknowledges it, so neither is clicked (never choose a consent
    // option). The privacy and OAuth cards are recorded as a boundary, not reached.
    await S.view('default');
  } },
  notfound: { path: '/features', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openMenu(p)) await S.view('menu'); });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  signin: { path: APP + '/signin', abs: true, run: async (p, S) => { await S.view('default'); } },
  signup: { path: APP + '/signup', abs: true, run: async (p, S) => {
    // Consent boundary, as on desktop: Continue and Continue to signup are never clicked.
    await S.view('default');
  } },
  docs: { path: '/docs/guides-getting-started', run: async (p, S) => { await S.view('default'); } },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.abs || spec.path.startsWith('http') ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await clearChallenge(p);
    await wait(p, spec.wait || 2200);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
