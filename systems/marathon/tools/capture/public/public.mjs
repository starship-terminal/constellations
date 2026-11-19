// Captures Marathon's public pages into RAW (full-colour PNGs). quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/marathon/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Names are {page}-light-{state}.png. Mobile ones get a mobile- prefix.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. The archive paints one live theme (html.light).
// Sign-in, register and checkout are not opened as forms: both auth routes redirect to /.
// Consent is hidden, never clicked. Nothing is submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, chromium, UA, UA_MOBILE, hideConsent, PKG } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
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
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-hover', async () => {
      await p.getByRole('link', { name: 'Pricing', exact: true }).first().hover();
      await wait(p, 400);
      await S.view('nav-hover');
    });
    await step('cta-hover', async () => {
      await p.getByRole('link', { name: 'Get Started' }).first().hover();
      await wait(p, 400);
      await S.view('cta-hover');
    });
  } },
  agencies: { path: '/for-agencies', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Pay Monthly' }).click();
      await wait(p, 500);
      await S.view('monthly');
      await p.getByRole('button', { name: 'Pay Annually' }).click();
      await wait(p, 300);
    });
    await S.full();
  } },
  demo: { path: '/demo', run: async (p, S) => { await S.view('default'); await S.full(); } },
  curated: { path: '/curated', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signin: { path: '/sign-in', run: async (p, S) => { await S.view('redirect'); } },
  register: { path: '/register', run: async (p, S) => { await S.view('redirect'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.getByRole('button', { name: 'Open menu' }).click();
      await wait(p, 500);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 200);
    });
    await S.full();
  } },
  agencies: { path: '/for-agencies', run: async (p, S) => { await S.view('default'); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByRole('button', { name: 'Pay Monthly' }).click();
      await wait(p, 400);
      await S.view('monthly');
    });
    await S.full();
  } },
  demo: { path: '/demo', run: async (p, S) => { await S.view('default'); } },
  curated: { path: '/curated', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
const notes = [];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const p = await ctx.newPage();
  log(name, BASE + spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2800);
    const hidden = await hideConsent(p);
    const finalUrl = p.url();
    const size = await p.evaluate(() => ({
      w: innerWidth, h: innerHeight, dpr: devicePixelRatio,
      vw: visualViewport && visualViewport.width, vh: visualViewport && visualViewport.height,
      scale: visualViewport && visualViewport.scale,
    }));
    notes.push({ name, requested: spec.path, status: resp && resp.status(), final: finalUrl, hidden, size });
    log('  landed', resp && resp.status(), finalUrl, JSON.stringify(size), hidden.length ? 'hid ' + hidden.join(';') : '');
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    notes.push({ name, error: String(e.message || e).split('\n')[0] });
  }
  total += S.count;
  await ctx.close();
}
fs.mkdirSync(path.join(os.homedir(), '.design-systems', 'marathon'), { recursive: true });
fs.writeFileSync(path.join(os.homedir(), '.design-systems', 'marathon', 'capture-notes.json'), JSON.stringify(notes, null, 2));
log('done', total, 'screenshots ->', RAW);
await browser.close();
