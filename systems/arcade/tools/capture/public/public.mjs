// Captures arcade.software's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, downloaded or signed into: the only presses are local UI toggles — a prompt
// suggestion chip, a pricing FAQ accordion, the spotlight quote arrows and the mobile menu.
// The Intercom launcher and the custom play cursor are hidden (never clicked) before every shot.
import fs from 'fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots go to a scratch dir outside the repo (the kit's default), never into
// systems/<slug>/raw/: quantize.py reads them from there and writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(fileURLToPath(new URL('../../..', import.meta.url))), 'raw-shots');
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
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    // Stage every tile under a .new name and swap it in only after the whole
    // shot succeeds, so a failed tile never truncates the previous capture.
    const staged = [];
    try {
      if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) { for (const f of [tmp, tmp + '.capture.json']) fs.existsSync(f) && fs.unlinkSync(f); }
      throw e;
    }
    // `.new.png` staging names also start with `${prefix}-${name}.part`, so the
    // stale-tile sweep must skip them or it deletes the files about to be renamed.
    const stale = (n) => !n.includes('.new') && (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`);
    for (const old of fs.readdirSync(RAW).filter(stale)) fs.unlinkSync(`${RAW}/${old}`);
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      // The sidecar follows the image: rename it and point its `screenshot`
      // name at the final file, or a finished capture has no matching record.
      const sidecar = tmp + '.capture.json';
      if (fs.existsSync(sidecar)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sidecar, 'utf8'));
          if (meta.screenshot) meta.screenshot = final.split('/').pop();
          fs.writeFileSync(sidecar, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* leave the record as-is rather than lose it */ }
        fs.renameSync(sidecar, final + '.capture.json');
      }
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// A pricing FAQ opens a Webflow accordion in place.
const openFaq = async (p) => {
  const a = p.locator('.avfaq-trigger').filter({ visible: true }).first();
  if (await a.count()) { await a.scrollIntoViewIfNeeded(); await clickEl(a); await wait(p, 900); return true; }
  return false;
};

// The hero's suggestion chips swap the prompt placeholder locally.
const tapSuggestion = async (p) => {
  const s = p.locator('.arcade-prompt-suggestions button, .arcade-prompt-suggestions a').filter({ visible: true }).first();
  if (await s.count()) { await clickEl(s); await wait(p, 900); return true; }
  return false;
};

const openMenu = async (p, label) => {
  const a = p.locator('.navbar a.nav-btn, .w-nav a.nav-btn').filter({ hasText: new RegExp('^' + label + '$') }).first();
  if (!(await a.count())) return false;
  await a.hover().catch(() => {});
  await clickEl(a);
  await wait(p, 700);
  return true;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => { if (await openMenu(p, 'Product')) await S.view('product'); });
    await p.keyboard.press('Escape').catch(() => {});
    await wait(p, 300);
    await step('resources-menu', async () => { if (await openMenu(p, 'Resources')) await S.view('resources'); });
    await p.keyboard.press('Escape').catch(() => {});
    await wait(p, 300);
    await step('suggestion', async () => { if (await tapSuggestion(p)) await S.view('suggestion'); });
    await step('quote-next', async () => {
      const n = p.locator('.spotlight-next').filter({ visible: true }).first();
      if (await n.count()) { await n.scrollIntoViewIfNeeded(); await clickEl(n); await wait(p, 900); await S.view('quote-next'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => { if (await openFaq(p)) await S.view('faq'); });
    await S.full();
  } },
  'interactive-demo': { path: '/product/interactive-demo', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  agents: { path: '/agents', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'video-examples': { path: '/ai-video-examples', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  changelog: { path: '/changelog', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'contact-sales': { path: '/contact-sales', wait: 8000, run: async (p, S) => {
    // The published form ships with sample name and email values. Clear them
    // before the shot. Never type a replacement and never submit.
    await p.evaluate(() => {
      document.querySelectorAll('input, textarea').forEach((el) => {
        if (el.type === 'hidden' || el.type === 'checkbox' || el.type === 'radio') return;
        el.value = '';
        el.setAttribute('value', '');
      });
    });
    await wait(p, 400);
    await S.view('default');
    await S.full();
  } },
  apps: { path: '/apps', wait: 8000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers', wait: 8000, run: async (p, S) => { await S.view('default'); } },
  brand: { path: '/brand', wait: 8000, run: async (p, S) => { await S.view('default'); } },
  security: { path: '/security', wait: 8000, run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', wait: 8000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('.w-nav-button, .menu-button, button[aria-label*="menu" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'interactive-demo': { path: '/product/interactive-demo', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch({ headless: true });
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();

// Auth wall, photographed empty. Never type, never click an identity provider,
// never submit. A separate context so a redirect cannot ride a marketing session.
async function shootWall() {
  if (pageArg.length && !pageArg.includes('login') && !pageArg.includes('auth')) return;
  const AUTH = 'https://app.arcade.software/auth';
  for (const mob of [false, true]) {
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const prefix = mob ? 'mobile-login-light' : 'login-light';
    const browser = await chromium.launch({ headless: true });
    try {
      const context = await browser.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
      await patch(context);
      const p = await context.newPage();
      log(prefix);
      try {
        const res = await p.goto(AUTH, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => null);
        const status = res ? res.status() : 0;
        await wait(p, 4000);
        const info = await p.evaluate(() => {
          const text = (document.body && document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 800);
          const fields = [...document.querySelectorAll('input, textarea')].map((el) => ({
            type: el.type || el.tagName.toLowerCase(),
            name: el.getAttribute('name') || '',
            label: el.getAttribute('aria-label') || el.getAttribute('placeholder') || '',
            value: el.value ? 'filled' : 'empty',
          }));
          const buttons = [...document.querySelectorAll('button, a, [role="button"]')]
            .map((el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim())
            .filter(Boolean)
            .slice(0, 24);
          return { title: document.title, text, fields, buttons, host: location.host };
        }).catch(() => ({ title: '', text: '', fields: [], buttons: [], host: '' }));
        fs.writeFileSync(`${RAW}/${prefix}-probe.json`, JSON.stringify({ status, ...info }, null, 2) + '\n');
        const challenging = /just a moment|verify you are human|captcha|security verification/i.test(info.title + info.text);
        if (challenging) { log('  WALL challenge, not photographed', prefix); }
        else {
          await closePromo(p);
          const S = new Shooter(p, prefix, vw, vh, dpr);
          await S.view('empty');
        }
      } catch (e) { log('  WALL FAILED', prefix, String(e.message).split('\n')[0]); }
      await context.close();
    } finally {
      await browser.close();
    }
  }
}
await shootWall();
