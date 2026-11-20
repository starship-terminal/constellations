// Captures esquire.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. esquire.com paints one
// light theme everywhere: the home page, the section fronts (/style/, /entertainment/, /news-politics/,
// /food-drink/), articles (a long cover interview and a shorter essay), the
// /offers/premium-membership plan page, the /esq-premium-exclusive/ hub, the search results page and
// the about page. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought or signed into: the only press is a local UI toggle — the desktop "More" nav
// dropdown and the mobile hamburger drawer. Sign In, Subscribe, Join, Follow and every article link
// are never followed. The OneTrust consent layer and any fixed promo overlay are hidden, never
// answered. Third-party ad and tracker requests are aborted before they leave the browser, so ad
// slots paint as blank containers; the "Advertisement" furniture the page itself renders stays.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour originals stay outside the repo (quantize.py writes screenshots/ from them).
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'esquire', 'raw', 'full') // as README Rebuild;
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

// Opens the desktop "More" dropdown: a local UI toggle under the megaMenu
// strip that drops the full-width "Sports | Member Exclusives | For You"
// panel. Its links are never followed.
async function openMore(p) {
  const more = p.locator('.megaMenu button, .megaMenu [role="button"]').filter({ hasText: /^\s*More\s*$/ }).filter({ visible: true }).first();
  if (!(await more.count())) return false;
  for (let i = 0; i < 3; i++) {
    await clickEl(more);
    const open = await p.waitForFunction(() => [...document.querySelectorAll('.megaMenu div, .megaMenu ul')].some((el) => el.getBoundingClientRect().height > 60 && /Member Exclusives/.test(el.innerText || '')), undefined, { timeout: 4000 }).then(() => true).catch(() => false);
    if (open) return true;
    await wait(p, 700);
  }
  return false;
}

const desktop = {
  home: { url: BASE + '/', wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      if (await openMore(p)) { await wait(p, 800); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 500); }
    });
    await S.full();
  } },
  style: { url: BASE + '/style/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  entertainment: { url: BASE + '/entertainment/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  politics: { url: BASE + '/news-politics/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  food: { url: BASE + '/food-drink/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  article: { url: BASE + '/entertainment/movies/a71465908/dwayne-johnson-the-rock-interview-2026/', wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  essay: { url: BASE + '/lifestyle/sex/a74076291/ai-chatbots-flirting-texts/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  offers: { url: BASE + '/offers/premium-membership/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  premium: { url: BASE + '/esq-premium-exclusive/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  search: { url: BASE + '/search/?q=suits', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about/a26377/about-us/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const ham = p.locator('nav button').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 1600);
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    await S.full();
  } },
  article: { url: BASE + '/entertainment/movies/a71465908/dwayne-johnson-the-rock-interview-2026/', wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  style: { url: BASE + '/style/', wait: 9000, theme: 'light', run: async (p, S) => {
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
  // Tiled full-page shots on a 38k-px article can need longer than the 30s
  // default while the renderer walks the page.
  p.setDefaultTimeout(120000);
  log(name);
  // The sidecar records the page without its query string (a search term or tracking id).
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url && spec.url.split(/[?#]/)[0]);
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
