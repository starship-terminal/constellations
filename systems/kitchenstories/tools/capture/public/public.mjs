// Captures kitchenstories.com's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/kitchenstories/raw-shots PLAYWRIGHT=… node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// kitchenstories.com paints one light theme. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots at CSS scale. A page taller than one
// GPU texture is saved as name.partN.png tiles; an unbounded page truncates
// at 8 chunks. Nothing is sent, bought or signed into. The only presses are
// local UI toggles: the search opener and the menu button. Consentmanager
// is hidden, never answered. Checkout, profile, cart and rating submit are
// never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, PAGES } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const RECIPE = BASE + '/huhnersuppe-mit-zitrone-a-a/192140';

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 700);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openSearch(p) {
  const b = p.getByRole('button', { name: /Suche öffnen/i }).first();
  if (await b.count()) { await b.click().catch(() => {}); await wait(p, 600); return true; }
  return false;
}
async function openMenu(p) {
  // Two .mobile-menu-toggle nodes exist. The first sits in the off-canvas
  // header track (x ~728 at 390). The painted hamburger is the visible one.
  const b = p.locator('button.mobile-menu-toggle').filter({ visible: true }).last();
  if (!(await b.count())) return false;
  await b.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 800);
  return true;
}

const desktop = {
  home: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => { if (await openSearch(p)) { await S.view('search-open'); await p.keyboard.press('Escape'); } });
    await S.full();
  } },
  recipes: { url: BASE + '/rezepte', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  category: { url: BASE + '/backen', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  recipe: { url: RECIPE, wait: 5500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  stories: { url: BASE + '/stories', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { url: BASE + '/?s=pasta', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  partners: { url: BASE + '/partners', wait: 4000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  team: { url: BASE + '/team', wait: 4000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  author: { url: BASE + '/author/johanna', wait: 4000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { url: BASE + '/kontakt', wait: 4000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { url: BASE + '/impressum', wait: 4000, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: PAGES + '/de/about', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  app: { url: PAGES + '/de/app', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  plus: { url: PAGES + '/de/plus', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  career: { url: PAGES + '/de/career', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  missing: { url: BASE + '/en', wait: 3000, theme: 'light', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', wait: 5000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { if (await openMenu(p)) { await S.view('menu'); await p.keyboard.press('Escape'); } });
    await S.full();
  } },
  recipe: { url: RECIPE, wait: 5500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  recipes: { url: BASE + '/rezepte', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  plus: { url: PAGES + '/de/plus', wait: 4500, theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'de-DE' });
  await patch(ctx);
  const p = await ctx.newPage();
  p.setDefaultTimeout(120000);
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
