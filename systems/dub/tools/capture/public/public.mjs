// Captures dub.co's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Three surfaces paint
// signed out: the Next.js marketing pages (home, product pages, pricing, customers, enterprise,
// compare, contact-sales, blog, changelog, brand), the auth cards on /login and /register (the
// app.dub.co shell, measured never submitted), and the Mintlify docs/help surface on /docs and
// /help — the only place a real theme toggle exists (html.dark, localStorage isDarkMode), so
// docs shoots run both light and dark. The marketing pages paint light only. Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary. Nothing is sent, submitted or signed
// into: the only presses are local UI toggles — the header Product mega-menu (hover), the
// Monthly/Yearly pricing toggle, the mobile menu, and the docs theme dropdown. The Mintlify AI
// assistant and any promo/cookie overlay are hidden, never answered.
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
    else {
      const tiles = [];
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        const tile = `${f}.part${i}.png`;
        await screenshotWithMetadata(p, { path: tile, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
        tiles.push(tile);
      }
      // Completion record, written only after the last tile lands: a run killed
      // mid-loop used to leave a partial tile set that quantize.py stitched
      // into a silently truncated page. The record is how the stitcher knows
      // the set on disk is the whole page.
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({
        tiles: tiles.map((t) => t.split('/').pop()),
        height: hCap, pageHeight: H, truncated: H > MAXH,
        captured: new Date().toISOString(),
      }, null, 2) + '\n');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Sets the docs surface's theme through its own "Change theme preference"
// dropdown: System/Light/Dark. A local UI toggle, never an account setting.
async function docsTheme(p, theme) {
  const t = p.locator('button[aria-label="Change theme preference"]').first();
  if (!(await t.count())) return false;
  await clickEl(t); await wait(p, 1000);
  const opt = p.locator('[role="menu"] *, [role="menuitem"], [role="option"], [class*="popover" i] *').filter({ hasText: new RegExp(`^\\s*${theme}\\s*$`) }).first();
  if (!(await opt.count())) return false;
  await clickEl(opt); await wait(p, 1200);
  // Report success only once <html> carries the class the choice paints —
  // clicking through a menu that never applied used to save light evidence
  // under dark names.
  return p.evaluate((wantDark) => document.documentElement.classList.contains('dark') === wantDark, theme === 'Dark').catch(() => false);
}

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('nav-product', async () => {
      const t = p.locator('button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await t.hover({ timeout: 5000 }); await wait(p, 1400); await S.view('menu'); await p.keyboard.press('Escape'); await p.mouse.move(700, 300); }
    });
    await S.full();
  } },
  links: { path: '/links', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  partners: { path: '/partners', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('yearly', async () => {
      const t = p.locator('button').filter({ hasText: /^\s*Yearly/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('yearly'); }
    });
    await S.full();
  } },
  customers: { path: '/customers', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  compare: { path: '/compare/bitly', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  sales: { path: '/contact/sales', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/login', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  register: { path: '/register', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  docs: { path: '/docs', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-dark': { path: '/docs', wait: 10000, theme: 'dark', run: async (p, S) => {
    if (!(await docsTheme(p, 'Dark'))) { log('  ! theme toggle did not apply Dark — skipping the dark shots rather than saving light evidence under dark names'); return; }
    await S.view('default');
    await S.full();
    if (!(await docsTheme(p, 'Light'))) log('  ! theme toggle did not return to Light');
  } },
  help: { path: '/help', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  changelog: { path: '/changelog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button.z-30.rounded-full, header + div button, [class*="rounded-full"][class*="p-2"]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { path: '/docs', wait: 10000, run: async (p, S) => {
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
  const theme = spec.theme || 'light';
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
