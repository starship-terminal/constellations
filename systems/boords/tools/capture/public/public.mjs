// Captures boords.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is sent, bought
// or signed into: the only presses are local UI toggles — the mobile menu, the pricing billing
// tabs and the script-timer's own controls (states only on tool pages; the timer is a public toy).
// Consent overlays are hidden, never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
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

// The yearly/monthly billing tabs are role="tab" toggles — local UI toggles.
const billTab = async (p, want) => {
  const t = p.locator('button[role="tab"]').filter({ hasText: new RegExp(want, 'i') }).filter({ visible: true }).first();
  if (await t.count()) { await clickEl(t); await wait(p, 1000); return true; }
  return false;
};

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label="Open menu"]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1200); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('yearly', async () => { if (await billTab(p, 'year|annual')) await S.view('yearly'); });
    await S.full();
  } },
  'ai-storyboard': { path: '/ai-storyboard-generator', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'storyboard-software': { path: '/storyboard-software', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  collaborate: { path: '/collaborate', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { path: '/customers', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'customer-story': { path: '/customers/mobula', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { path: '/docs', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'script-timer': { path: '/script-timer', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('with-script', async () => {
      // The public timer ships a sample/paste area; typing sample text and
      // counting is a local action, never submitted.
      const ta = p.locator('textarea').filter({ visible: true }).first();
      if (await ta.count()) {
        await ta.fill('Fade in. A studio. Our hero opens Boords and drags three frames onto the board. The script timer reads the words and shows a running time.');
        await wait(p, 900);
        await S.view('with-script');
      }
    });
    await S.full();
  } },
  login: { path: '/login', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { path: '/signup', run: async (p, S) => {
    await S.view('default');
  } },
  demo: { path: '/demo', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label="Open menu"]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); }
    });
    await S.full();
  } },
  'script-timer': { path: '/script-timer', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch();
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
