// Captures Monarch Money public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/monarch-money/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Desktop 1440x900 at 1x. Mobile 390x844 at 2x, prefixed mobile-.
// The Osano banner is hidden, never clicked. Sign-up, OAuth, bank linking,
// checkout and off-site account flows are never followed. Sign-in is
// photographed at the boundary and not submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, APP, HELP, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'monarch-money', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function settle(p) {
  await hideConsent(p);
  // Headless Chromium cannot decode the Mux hero. The error card lives in
  // the player shadow root, so a page query misses it. Hide the dialog
  // inside every open shadow root. The video is not evidence.
  await p.evaluate(() => {
    const visit = (root) => {
      root.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch {} });
      root.querySelectorAll('div, p, span, h2, h3, [role="dialog"], [class*="error"]').forEach((el) => {
        const t = (el.innerText || '').trim();
        if (/media error/i.test(t) && t.length < 280) {
          el.style.setProperty('display', 'none', 'important');
        }
      });
      root.querySelectorAll('*').forEach((el) => { if (el.shadowRoot) visit(el.shadowRoot); });
    };
    visit(document);
  }).catch(() => {});
}

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 16; i++) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (h === last && i > 2) break;
    last = h;
    const y = Math.min(i * 700, Math.max(0, h - 800));
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 350);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await settle(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(path.join(RAW, old));
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

async function guard(p, url) {
  const title = await p.title();
  const body = await p.evaluate(() => (document.body?.innerText || '').slice(0, 200));
  if (/just a moment|cf-challenge|checking your browser/i.test(title + ' ' + body)) {
    throw new Error('Cloudflare challenge on ' + url);
  }
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'features-tracking': { url: BASE + '/features/tracking', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'features-budgeting': { url: BASE + '/features/budgeting', run: async (p, S) => { await S.view('default'); } },
  'features-planning': { url: BASE + '/features/planning', run: async (p, S) => { await S.view('default'); } },
  'for-couples': { url: BASE + '/for-couples', run: async (p, S) => { await S.view('default'); } },
  'for-professionals': { url: BASE + '/for-professionals', run: async (p, S) => { await S.view('default'); } },
  download: { url: BASE + '/download', run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { url: BASE + '/security', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); } },
  'whats-new': { url: BASE + '/whats-new', run: async (p, S) => { await S.view('default'); } },
  careers: { url: BASE + '/careers', run: async (p, S) => { await S.view('default'); } },
  press: { url: BASE + '/press', run: async (p, S) => { await S.view('default'); } },
  canada: { url: BASE + '/canada', run: async (p, S) => { await S.view('default'); } },
  compare: { url: BASE + '/compare/mint-alternative', run: async (p, S) => { await S.view('default'); } },
  calculator: { url: BASE + '/calculators/mortgage-calculator', run: async (p, S) => { await S.view('default'); } },
  privacy: { url: BASE + '/privacy', run: async (p, S) => { await S.view('default'); } },
  terms: { url: BASE + '/terms', run: async (p, S) => { await S.view('default'); } },
  help: { url: HELP + '/hc/en-us', run: async (p, S) => { await S.view('default'); } },
  signin: { url: APP + '/login', run: async (p, S) => { await S.view('default'); } },
  signup: { url: APP + '/signup', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); } },
  // app.monarch.com reports devicePixelRatio 1 in this host. A 2x context
  // writes a PNG the screenshot helper rejects. Capture the wall at 1x.
  signin: { url: APP + '/login', dpr: 1, run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
try {
  for (const { k, mob } of runs) {
    const name = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
    const spec = (mob ? mobile : desktop)[k];
    const vw = mob ? 390 : 1440;
    const vh = mob ? 844 : 900;
    const dpr = spec.dpr ?? (mob ? 2 : 1);
    const ctx = await b.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    await ctx.addInitScript((sel) => {
      const hide = () => document.querySelectorAll(sel).forEach((el) => {
        el.style.setProperty('display', 'none', 'important');
      });
      const start = () => new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
      if (document.documentElement) start();
      else document.addEventListener('DOMContentLoaded', start);
    }, '.osano-cm-window, .osano-cm-dialog, .osano-cm-widget');
    const p = await ctx.newPage();
    log(name, spec.url);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 70000 });
      await wait(p, 2200);
      await guard(p, spec.url);
      await hideConsent(p);
      await spec.run(p, S);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
      if (/Cloudflare/.test(e.message)) {
        await ctx.close();
        throw e;
      }
    }
    total += S.count;
    await ctx.close();
  }
} finally {
  log('done', total, 'screenshots ->', RAW);
  await b.close();
}
