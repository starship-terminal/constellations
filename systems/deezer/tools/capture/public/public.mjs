// Captures deezer.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. deezer.com paints one
// light surface — the home hero — and dark everywhere else: the marketing offers/features/download
// pages, the public web app (artist/album/playlist catalog pages with the player bar, Chakra UI),
// the account.deezer.com login/signup forms and the whole mobile surface. Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the artist page's "View menu" track overflow (a Chakra
// popover), the offers Monthly/Annual billing toggle and the mobile hamburger drawer. The "A note
// about our cookies" GDPR modal is hidden, never answered.
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
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
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { url: BASE + '/en/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  offers: { url: BASE + '/en/offers', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('annual', async () => {
      const t = p.locator('button, [role="tab"], a, label').filter({ hasText: /^Annual$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('annual'); }
    });
    await S.full();
  } },
  premium: { url: BASE + '/en/offers/premium', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { url: BASE + '/explore/features/', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { url: BASE + '/explore/download/', wait: 7000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  artist: { url: BASE + '/en/artist/27', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const t = p.locator('button[aria-label="View menu"]').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1400);
      await S.view('menu');
      await p.keyboard.press('Escape');
      await wait(p, 600);
    });
    await S.full();
  } },
  album: { url: BASE + '/en/album/302127', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  playlist: { url: BASE + '/en/playlist/3155776842', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: 'https://account.deezer.com/en/login/', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: 'https://account.deezer.com/en/signup/', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  artist: { url: BASE + '/en/artist/27', wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The hamburger is a div.burger-menu, not a button; it toggles a
      // full-viewport ul.burger-menu-content.
      const ham = p.locator('.burger-menu').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await p.waitForSelector('ul.burger-menu-content', { state: 'visible', timeout: 4000 }).catch(() => {});
      await wait(p, 1400);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  home: { url: BASE + '/en/', wait: 8000, theme: 'dark', run: async (p, S) => {
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
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
