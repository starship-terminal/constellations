// Captures endless.app's public pages into RAW (full-colour PNGs); quantize.py turns them into
// screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. endless.io 307-redirects
// to endless.app, a Next.js marketing surface whose token layer rebinds under .dark (next-themes:
// the site follows the system scheme and carries a footer Theme control). Light runs shoot every
// marketing route; dark runs emulate prefers-color-scheme dark, which the site genuinely paints —
// the same mechanism a visitor's dark system gets. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates at 8 chunks and the
// log records the boundary. Nothing is sent, signed into, generated or subscribed to: the only
// presses are local UI toggles — the Annual billing toggle, the mobile menu, and clicking into a
// field (which types nothing). The desktop header is flat nav links: there is no dropdown menu at
// 1440px (the Menu button is display:none until the mobile breakpoint). Sign-in goes to clerk.endless.app and
// sign-up to s.endless.app — both out of scope, never followed. Consent or chat overlays are
// hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    // No desktop nav dropdown exists: the header is flat links (Product, Models, Industries,
    // Pricing, Blog) and the Menu button only paints below the mobile breakpoint, where the
    // mobile run captures it open.
    await step('composer', async () => {
      const ta = p.locator('textarea').filter({ visible: true }).first();
      if (await ta.count()) { await ta.click({ timeout: 5000 }); await wait(p, 800); await S.view('composer'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('annual', async () => {
      const t = p.locator('button').filter({ hasText: /^\s*Annual\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('annual'); }
    });
    await S.full();
  } },
  contact: { path: '/contact', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('field', async () => {
      const f = p.locator('input').filter({ visible: true }).first();
      if (await f.count()) { await f.click({ timeout: 5000 }); await wait(p, 700); await S.view('field'); }
    });
    await S.full();
  } },
  tools: { path: '/tools', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  toolgen: { path: '/tools/ai-image-generator', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('prompt', async () => {
      const f = p.locator('input').filter({ visible: true }).first();
      if (await f.count()) { await f.click({ timeout: 5000 }); await wait(p, 700); await S.view('prompt'); }
    });
    await S.full();
  } },
  models: { path: '/models', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'model-index': { path: '/model-index', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  brand: { path: '/brand', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { path: '/docs', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  radar: { path: '/radar', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  mcp: { path: '/mcp', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  industries: { path: '/industries', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  compare: { path: '/compare', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  status: { path: '/status', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

// Dark runs emulate prefers-color-scheme: the site's own theme script picks
// .dark from the media query, so these paint the theme a dark-system visitor
// sees, not a class forced on a copy.
const darkRuns = {
  home: desktop.home,
  pricing: desktop.pricing,
  contact: desktop.contact,
  toolgen: desktop.toolgen,
  models: desktop.models,
  radar: desktop.radar,
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('header button').filter({ visible: true }).last();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  toolgen: { path: '/tools/ai-image-generator', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  models: { path: '/models', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, dark: false })),
  ...Object.keys(darkRuns).map((k) => ({ k, mob: false, dark: true })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, dark: false })),
];
for (const { k, mob, dark } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes((dark ? 'dark-' : '') + name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = dark ? 'dark' : 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: theme });
  await patch(ctx);
  const p = await ctx.newPage();
  log((dark ? 'dark ' : '') + name);
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
