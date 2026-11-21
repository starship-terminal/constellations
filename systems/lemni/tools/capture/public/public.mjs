// Captures Lemni's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x. The home
// page paints dark (rgb(13, 13, 18)); pricing, docs, blog, company, brand,
// changelog, legal and the sign-in shell paint light (rgb(246, 246, 248)).
// Filenames use the theme the page actually paints. A page taller than one
// GPU texture is saved as name.partN.png tiles; an unbounded page truncates
// at 8 chunks.
//
// Nothing is signed into, submitted or purchased. The only presses are local
// UI toggles: the docs sidebar link (a public page), the phone menu, and
// Escape. Cookie overlays are hidden, never clicked. Continue, Try For Free
// and Continue with Google are photographed at rest and are not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lemni', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 700);
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n === `${path.basename(f)}.png`)) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The phone nav is a Framer hamburger: an icon control at the bar's right
// edge, with no accessible name. Mark it, then click. Escape closes it.
async function openMobileMenu(p) {
  const ok = await p.evaluate(() => {
    const nav = document.querySelector('nav');
    if (!nav) return false;
    const cand = [...nav.querySelectorAll('a, button, div')].filter((n) => {
      const r = n.getBoundingClientRect();
      const c = getComputedStyle(n);
      const iconish = n.querySelector('svg') || c.cursor === 'pointer';
      return r.width >= 16 && r.width <= 64 && r.height >= 16 && r.height <= 64 && r.x > 280 && iconish && !(n.innerText || '').trim();
    });
    const el = cand[cand.length - 1];
    if (!el) return false;
    el.setAttribute('data-m-menu', '1');
    return true;
  });
  if (!ok) return false;
  await p.locator('[data-m-menu="1"]').click({ timeout: 4000 }).catch(() => {});
  await wait(p, 900);
  return true;
}

const desktop = {
  home: { url: BASE + '/', theme: 'dark', wait: 5500, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: BASE + '/docs', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('agents', async () => {
      const a = p.locator('a[href="./agents"], a[href="/docs/agents"]').first();
      if (await a.count()) { await a.click(); await wait(p, 1800); await S.view('agents'); }
    });
    await S.full();
  } },
  blog: { url: BASE + '/blog', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { url: BASE + '/company', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { url: BASE + '/changelog', theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  brand: { url: BASE + '/brand', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  support: { url: BASE + '/support', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { url: BASE + '/privacy', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { url: BASE + '/terms', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signin: { url: APP + '/signin', theme: 'light', wait: 4000, run: async (p, S) => { await S.view('default'); } },
  signup: { url: APP + '/signup', theme: 'light', wait: 4000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', theme: 'dark', wait: 5500, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => {
      if (await openMobileMenu(p)) { await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: BASE + '/docs', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signin: { url: APP + '/signin', theme: 'light', wait: 4000, run: async (p, S) => { await S.view('default'); } },
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
  log(name, spec.theme);
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    if (!(await clearChallenge(p))) { log('  BLOCKED', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 4500);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
