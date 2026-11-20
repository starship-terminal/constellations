// Captures Limitless public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/limitless/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Desktop 1440x900 at 1x. Mobile 390x844 at 2x, prefixed mobile-.
// The Enzuzo cookie banner is hidden, never clicked. Sign-in, forms and
// off-site links are never followed. Solutions is a local menu toggle.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, APP, HELP, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'limitless', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function settle(p) {
  await hideConsent(p);
  await p.evaluate(() => {
    document.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch {} });
  }).catch(() => {});
}

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 18; i++) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (h === last && i > 2) break;
    last = h;
    const y = Math.min(i * 700, Math.max(0, h - 800));
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
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
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('solutions', async () => {
      await p.getByRole('button', { name: 'Solutions' }).click();
      await wait(p, 500);
      await S.view('solutions');
      await p.keyboard.press('Escape');
      await wait(p, 200);
    });
  } },
  privacy: { url: BASE + '/privacy', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq', async () => {
      const btn = p.locator('button, [role=button], summary, details').filter({ hasText: /./ }).nth(2);
      // open the first accordion that is not the nav
      const item = p.locator('main button, main summary, main [role=button]').first();
      if (await item.count()) {
        await item.click();
        await wait(p, 400);
        await S.view('faq-open');
      }
    });
  } },
  developers: { url: BASE + '/developers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { url: BASE + '/careers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  support: { url: BASE + '/support', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { url: BASE + '/terms', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'privacy-policy': { url: BASE + '/privacy-policy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-voice': { url: BASE + '/for/voice-recorder', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-students': { url: BASE + '/for/students', run: async (p, S) => { await S.view('default'); } },
  notfound: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); } },
  signin: { url: APP + '/', run: async (p, S) => { await S.view('default'); } },
  help: { url: HELP + '/en/', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', async () => {
      // The hamburger is the only visible icon button in the bar. Cookie
      // controls are hidden and must not be clicked.
      const b = p.locator('button.outline-none.text-slate-500');
      await b.click({ timeout: 5000 });
      await wait(p, 500);
      await S.view('menu');
    });
  } },
  developers: { url: BASE + '/developers', run: async (p, S) => { await S.view('default'); } },
  'for-voice': { url: BASE + '/for/voice-recorder', run: async (p, S) => { await S.view('default'); await S.full(); } },
  // app.limitless.ai reports devicePixelRatio 1 even when the context asks
  // for 2, and Playwright still writes a 2x PNG. Shoot this host at 1x so
  // the sidecar check matches the page.
  signin: { url: APP + '/signin', dpr: 1, run: async (p, S) => {
    await p.waitForTimeout(1200);
    await S.view('default');
  } },
  help: { url: HELP + '/en/', run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = spec.dpr || (mob ? 2 : 1);
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    const sel = '#ez-cookie-notification, #enzuzo-modal, .ez-consent, .enzuzo-cookiebanner-container, .enzuzo-cookie-modal';
    const hide = () => document.querySelectorAll(sel).forEach((el) => el.style.setProperty('display', 'none', 'important'));
    const start = () => new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    if (document.documentElement) start();
  });
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 70000 });
    await wait(p, 2800);
    await hideConsent(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
