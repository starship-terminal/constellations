// Captures elevenlabs.io's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The public surface
// paints light only (the #FDFCFC eggshell field) — elevenlabs.io has no dark theme. Desktop shots
// are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded
// page truncates at 8 chunks and the log records the boundary. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the Products nav flyout, the hero product tabs,
// the pricing billing dropdown and the mobile navigation menu — plus the home playground's own
// textarea (sample text typed, never sent). Its Play is shot at rest, never pressed: a press asks
// the server to generate speech. The Cookiebot consent layer is hidden, never answered; /app
// redirects to /app/sign-in and the workspace behind it is never reached.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (the kit's default); quantize.py writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'elevenlabs', 'raw-shots') + '/';
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

// The header's Products/Solutions/Customers/Resources buttons open the nav
// flyout (a click toggles it). Local UI only, never a link.
async function openFlyout(p, S) {
  const t = p.locator('nav button, nav [role="button"]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  await clickEl(t);
  await wait(p, 1400);
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The signed-out playground on the home page: click its own textarea and type a
// word. Play is not pressed (server-side generation: recorded as a boundary, not
// crossed); the second shot shows the filled field with Play at rest.
async function playground(p, S) {
  const ta = p.locator('textarea').filter({ visible: true }).first();
  if (!(await ta.count())) return;
  await ta.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
  await wait(p, 900);
  await S.view('playground');
  await ta.click({ timeout: 4000 }).catch(() => {});
  await p.keyboard.type('a small test', { delay: 12 });
  await wait(p, 500);
  await S.view('playground-filled');
}

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('flyout', async () => { await openFlyout(p, S); });
    await step('agents-tab', async () => {
      // The hero's product tabs (ElevenCreative / ElevenAgents / ElevenAPI).
      const t = p.locator('[role="tab"]').filter({ hasText: 'ElevenAgents' }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); await S.view('agents-tab'); }
    });
    await step('playground', async () => { await playground(p, S); });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('billing', async () => {
      // The Monthly billing dropdown — a local UI toggle, no checkout.
      const t = p.locator('button').filter({ hasText: /billing/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1400); await S.view('billing'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await S.full();
  } },
  'text-to-speech': { path: '/text-to-speech', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'conversational-ai': { path: '/conversational-ai', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'sound-effects': { path: '/sound-effects', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  api: { path: '/api', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { path: '/docs/overview/intro', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
  'sign-in': { path: '/app/sign-in', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
  'sign-up': { path: '/app/sign-up', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="navigation" i], button[aria-label*="menu" i], header button').filter({ hasText: /^\s*$/ }).filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'text-to-speech': { path: '/text-to-speech', wait: 10000, run: async (p, S) => {
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
    if (spec.path) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
