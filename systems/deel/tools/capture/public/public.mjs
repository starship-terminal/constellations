// Captures deel.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// deel.com paints a single light theme (no dark variant), so every
// shot is `-light`. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded
// page truncates at 8 chunks and the log records the boundary.
//
// deel.com is a Next.js + MUI + Tailwind marketing site. The Solutions nav
// item opens its mega dropdown on hover — a local UI toggle, hovered for the
// `menu` shot; the mobile hamburger opens a drawer for the `drawer` shot.
// Log in, Book a demo and Claim offer lead to app.deel.com or signup flows —
// measured as links, never followed; the Cookiebot dialog is hidden, never
// answered. Nothing is submitted, signed into or followed off the site.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  // Scroll the document through its range so lazy images/posts mount, then restore.
  const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  for (let y = 0; y < H; y += 600) {
    await p.evaluate((y) => {
      window.scrollTo(0, y);
      const sels = [...document.querySelectorAll('*')]
        .filter((e) => e && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 100);
      sels.forEach((e) => { e.scrollTop = y; });
    }, y);
    await wait(p, 220);
  }
  await p.evaluate(() => {
    window.scrollTo(0, 0);
    [...document.querySelectorAll('*')]
      .filter((e) => e && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 100)
      .forEach((e) => { e.scrollTop = 0; });
  });
  await wait(p, 900);
}

// Expand inner scroll containers so document.scrollHeight covers the real
// content height for the bounded full-page shot.
async function expandScrollers(p) {
  return p.evaluate(() => {
    // Expand every inner scroll container to its real content height and
    // unclip its ancestors, so document.scrollHeight covers the whole page.
    document.querySelectorAll('*').forEach((e) => {
      if (e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 100) {
        e.style.setProperty('height', e.scrollHeight + 'px', 'important');
        e.style.setProperty('max-height', 'none', 'important');
        e.style.setProperty('overflow', 'visible', 'important');
        for (let a = e.parentElement; a; a = a.parentElement) {
          a.style.setProperty('height', 'auto', 'important');
          a.style.setProperty('max-height', 'none', 'important');
          a.style.setProperty('overflow', 'visible', 'important');
        }
      }
    });
    document.documentElement.style.setProperty('overflow', 'visible', 'important');
    document.body.style.setProperty('overflow', 'visible', 'important');
    return Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.sourceUrl = sourceUrl; this.count = 0; }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await expandScrollers(p);
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else {
      // Declare the tile count up front; quantize refuses to stitch a partial set.
      const n = Math.ceil(hCap / chunk);
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: false }) + '\n');
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: true }) + '\n');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Clicking the Solutions nav item opens the mega dropdown (a local UI
// toggle, never a link). The shot is taken with the panel open.
async function menuShot(p, S) {
  await step('menu', async () => {
    const item = p.locator('nav button, nav a').filter({ hasText: /^Solutions/ }).first();
    if (!(await item.count())) return;
    await clickEl(item);
    await wait(p, 1600);
    await S.view('menu');
  });
}

// The hamburger opens the mobile nav drawer (a local UI toggle).
async function drawerShot(p, S) {
  await step('drawer', async () => {
    const ham = p.locator('nav button[aria-label*="menu" i], nav button[aria-label*="navigation" i], nav .mui-1xqo0rs, header button').last();
    if (!(await ham.count())) return;
    await clickEl(ham);
    await wait(p, 1400);
    await S.view('drawer');
  });
}

// Closes any overlay the menu/drawer shots left open before the full-page
// pass — an open dropdown or drawer would otherwise cover the reference.
// Escape first (MUI closes panels and drawers on it), then verify; the
// trigger is only re-clicked when the overlay is still painted.
async function closeOverlays(p) {
  const open = () => p.evaluate(() => {
    const menu = [...document.querySelectorAll('a')].some((a) => /deel payroll overview/i.test(a.textContent) && a.getBoundingClientRect().width > 0);
    const drawer = [...document.querySelectorAll('[role="dialog"], [class*="MuiDrawer"], [class*="drawer" i]')].some((el) => el.getBoundingClientRect().width > 100 && getComputedStyle(el).visibility !== 'hidden');
    return menu || drawer;
  });
  if (!(await open())) return;
  await p.keyboard.press('Escape');
  await wait(p, 900);
  if (await open()) {
    // Fall back to toggling the same trigger that opened the overlay.
    const trig = p.locator('nav button, nav a, header button').filter({ hasText: /^Solutions|menu|navigation/i }).first();
    if (await trig.count()) await clickEl(trig);
    await wait(p, 900);
  }
  if (await open()) log('  ! overlay still open before full() — reference may be partially covered');
}

const desktop = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await menuShot(p, S);
    await closeOverlays(p);
    await S.full();
  } },
  pricing: { path: '/pricing/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  hr: { path: '/hr/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  payroll: { path: '/global-payroll/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about-us/', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await drawerShot(p, S);
    await closeOverlays(p);
    await S.full();
  } },
  pricing: { path: '/pricing/', wait: 7000, run: async (p, S) => {
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
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: 'light' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const target = spec.url || BASE + spec.path;
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, target);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
