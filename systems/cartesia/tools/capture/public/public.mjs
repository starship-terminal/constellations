// Captures cartesia.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The signed-out
// surfaces: the Astro/Tailwind marketing pages on www.cartesia.ai (home, sonic, ink, agents,
// voice-cloning, voices, pricing, tools, mcp, research, blog, contact, customers — all light;
// the site declares a .dark token layer but nothing on these pages binds it), the Clerk auth
// cards on play.cartesia.ai (sign-in, sign-up, the only playground surface reachable signed
// out) and the Mintlify docs landing on docs.cartesia.ai. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page truncates
// at 8 chunks and the log records the boundary. Nothing is sent, bought, generated or signed
// into: the only presses are local UI toggles — the Products nav menu, the mobile menu and a
// voice row's own play control on /sonic and /voices (a public demo the page offers signed
// out). The cookie consent island is hidden, never answered; Talk to Skylar / Talk to Cartesia
// live-agent calls are never started; the Playground sign-in card is never filled or submitted.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, PLAY, DOCS } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'cartesia', 'raw-shots');
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

const desktop = {
  home: { url: BASE + '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('nav-products', async () => {
      const t = p.locator('header button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  sonic: { url: BASE + '/sonic', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('voice-menu', async () => {
      // Open the demo's voice picker (a local select popover) — local UI state.
      const t = p.locator('button').filter({ hasText: /American English/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('voice-menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  ink: { url: BASE + '/ink', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  agents: { url: BASE + '/agents', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'voice-cloning': { url: BASE + '/product/voice-cloning', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  voices: { url: BASE + '/voices', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { url: BASE + '/tools', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  mcp: { url: BASE + '/mcp', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  research: { url: BASE + '/research', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { url: BASE + '/customers', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: PLAY + '/sign-in', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: PLAY + '/sign-in/create', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
  docs: { url: DOCS + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button').filter({ visible: true }).last();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  sonic: { url: BASE + '/sonic', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: PLAY + '/sign-in', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
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
