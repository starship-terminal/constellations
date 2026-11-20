// Captures jasper.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The signed-out
// surfaces: the Webflow marketing pages on www.jasper.ai (home, platform, agents, pricing,
// brand, blog, company, legal, demo form at rest) and the login card on app.jasper.ai.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches; an unbounded page truncates
// at 8 chunks. Nothing is sent, bought or signed into: the only presses are local UI toggles
// (the Platform nav dropdown, the mobile menu). The Transcend/HubSpot consent overlay is
// hidden, never answered. The demo form and the login card are screenshotted at rest.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'jasper', 'raw-shots');
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const pageOf = (path, extra) => ({ url: BASE + path, wait: 8000, run: async (p, S) => { await S.view('default'); if (extra) await extra(p, S); await S.full(); } });

const desktop = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('nav-platform', async () => {
      const t = p.locator('.nav_menu_item').filter({ hasText: /Platform/ }).filter({ visible: true }).first();
      if (await t.count()) { await t.hover(); await wait(p, 900); await S.view('menu'); await p.mouse.move(8, 8); await wait(p, 400); }
    });
    await S.full();
  } },
  platform: pageOf('/platform'),
  agents: pageOf('/agents'),
  pricing: pageOf('/pricing'),
  brand: pageOf('/brand'),
  blog: pageOf('/blog'),
  company: pageOf('/company'),
  legal: pageOf('/legal'),
  demo: { url: BASE + '/demo', wait: 8000, run: async (p, S) => { await S.view('default'); } },
  signin: { url: APP + '/auth/login', wait: 8000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('.nav_menu_button, .nav_button_menu, button[aria-label*="menu" i], .w-nav-button').filter({ visible: true }).first();
      const alt = p.locator('.nav_wrap button, .nav_contain button').filter({ visible: true }).last();
      const btn = (await m.count()) ? m : alt;
      if (await btn.count()) { await clickEl(btn); await wait(p, 1400); await S.view('menu'); await p.keyboard.press('Escape').catch(() => {}); }
    });
    await S.full();
  } },
  pricing: pageOf('/pricing'),
  signin: { url: APP + '/auth/login', wait: 8000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.url) {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
