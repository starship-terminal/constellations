// Captures elevenmusic.io's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. elevenmusic.io is a
// Next.js app shell — sidebar + header in a fixed-height flex layout, the page scrolling inside
// one inner element — painting dark by default (html.dark) with a declared light theme flipped by
// the footer's own System/Light/Dark segmented control (a local UI toggle, persisted by a cookie;
// the light shots reuse the same context after the flip). Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x. The document does not scroll: `*-full` shots first release the inner scroller and
// its ancestors from their viewport-height constraints, then take a fullPage shot and restore; an
// unbounded page truncates at 8 chunks and the log records the boundary. Nothing is sent, created,
// booked, bought or signed into: the only presses are local UI toggles — the header Resources
// dropdown, the footer theme buttons, the sidebar Search dialog, a track card's Play (local media
// playback that opens the player bar; Like, Remix, Share and every Create are measured, never
// pressed). The Cookiebot overlay (implied consent) is hidden, never answered.
import fs from 'fs';
import path from 'path';
import os from 'os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, findScroller, scrollMain, expandScroller, restoreScroller } from './lib.mjs';

// Full-colour shots stay outside the repo (the kit's default); quantize.py writes screenshots/.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'elevenmusic', 'raw-shots') + '/';
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// Lazy-load the inner scroller: scroll it through its height, then back to top.
async function lazyScroll(p) {
  const sc = await findScroller(p);
  if (!sc) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
    return null;
  }
  const h = await sc.evaluate((el) => el.scrollHeight);
  for (let y = 0; y < h; y += 600) { await scrollMain(p, y); await wait(p, 200); }
  await scrollMain(p, 0); await wait(p, 900);
  return h;
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, src) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: src }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const innerH = await lazyScroll(p);
    const hasScroller = innerH !== null;
    let H;
    if (hasScroller) {
      await expandScroller(p);
      await wait(p, 800);
      H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    } else {
      H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    }
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H + (hasScroller ? ' (inner scroller expanded)' : ''));
    if (hasScroller) await restoreScroller(p);
    await scrollMain(p, 0).catch(() => {});
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Flips the product's own footer theme segmented control: scroll the inner
// scroller to its bottom, press the named theme button, come back to the top.
// A local UI toggle persisted by the product's cookie — no consent, no form.
async function setTheme(p, theme) {
  const sc = await findScroller(p);
  if (sc) await scrollMain(p, 'bottom');
  await wait(p, 1500);
  const b = p.locator(`button[aria-label="${theme} theme"]`).first();
  if (await b.count()) { await clickEl(b); await wait(p, 1200); }
  await scrollMain(p, 0).catch(() => {});
  await wait(p, 600);
  return (await paintsDark(p)) === (theme === 'Dark');
}

// What the page paints, not what was requested: the product's dark theme is html.dark.
const paintsDark = (p) => p.evaluate(() => document.documentElement.classList.contains('dark')).catch(() => null);

const desktop = {
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('resources', async () => {
      const t = p.locator('header button, header a').filter({ hasText: /^\s*Resources\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await step('search', async () => {
      // The sidebar Search icon opens the sign-in dialog (search is gated
      // behind an account) — captured as the auth-modal evidence, then
      // dismissed with Escape. Nothing is submitted.
      const s = p.locator('button[aria-label="Search"]').filter({ visible: true }).first();
      if (await s.count()) { await clickEl(s); await wait(p, 1500); await S.view('search'); await p.keyboard.press('Escape'); await wait(p, 500); }
    });
    await S.full();
  } },
  explore: { path: '/explore', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('playing', async () => {
      // A track card's own Play control — local media playback that opens the
      // player bar. If the product gates playback behind sign-in the wall is
      // captured instead; Like/Remix/Share are never pressed.
      const t = p.locator('button[aria-label^="Play "]').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 2500); await S.view('playing'); }
    });
    await S.full();
  } },
  charts: { path: '/charts', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tracks: { path: '/tracks', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  genres: { path: '/genres', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'genre-electronic': { path: '/genres/electronic', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  sounds: { path: '/sounds', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { path: '/tools', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  artist: { path: '/artists/ghostmkc-5JuuiL', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  playlist: { path: '/playlists/69eb381eb3c0fe73c21c695c', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('options', async () => {
      // "Show other options" expands the auth choices in place — a local UI
      // reveal. If it navigates, the state is skipped; nothing is submitted.
      const t = p.locator('button').filter({ hasText: /Show other options/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1500); if (p.url().includes('/login')) await S.view('options'); }
    });
  } },
  signin: { path: '/sign-in', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

// The light pass: same context after the footer's own theme toggle flips
// html.dark off. Only the surfaces worth proving in light get a second pass.
const light = {
  'home-light': { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'explore-light': { path: '/explore', wait: 11000, run: async (p, S) => {
    await S.view('default');
  } },
  'charts-light': { path: '/charts', wait: 11000, run: async (p, S) => {
    await S.view('default');
  } },
  'pricing-light': { path: '/pricing', wait: 10000, run: async (p, S) => {
    await S.view('default');
  } },
  'login-light': { path: '/login', wait: 9000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  explore: { path: '/explore', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  charts: { path: '/charts', wait: 11000, run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, lite: false })),
  ...Object.keys(light).map((k) => ({ k, mob: false, lite: true })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, lite: false })),
];
for (const { k, mob, lite } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (lite ? light : mob ? mobile : desktop)[k];
  const theme = lite ? 'light' : 'dark';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, lite ? `${name}` : `${name}-${theme}`, vw, vh, dpr, spec.path ? BASE + spec.path : null);
  try {
    if (spec.path) {
      if (lite) {
        // Flip the product's own footer theme control on the home page once —
        // the choice persists by cookie, so later routes in this context load
        // light directly (the bare auth card carries no footer to toggle).
        await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        if (!(await clearChallenge(p))) { log('  BLOCKED challenge', '/'); await ctx.close(); continue; }
        await wait(p, 8000);
        if (!(await setTheme(p, 'Light'))) { log('  THEME toggle did not paint light, skipped', name); await ctx.close(); continue; }
      }
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
      // A light-named shot only when the route really paints light (the cookie may not carry).
      if (lite && (await paintsDark(p)) !== false) { log('  THEME not light, skipped', name); await ctx.close(); continue; }
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
