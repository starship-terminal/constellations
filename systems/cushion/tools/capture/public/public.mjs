// Captures cushion.so's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. cushion.so
// paints a single light theme (no .dark set), so every shot is `-light`. Desktop shots
// are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
//
// cushion.so is a Tailwind marketing site for the async-messaging app — it scrolls in
// the document, but the same inner-scroller expansion runs as a safety net. Log in and
// Sign up are header links, never followed; any consent/chat overlay is hidden, never
// answered. Nothing is submitted, signed into or followed off the site.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'cushion', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  // cushion.so scrolls inside Lenis containers, not the window — scroll each
  // inner scroller through its range so lazy content mounts, then restore.
  const scrl = () => [...document.querySelectorAll('*')]
    .filter((e) => e && e.scrollHeight > e.clientHeight + 50 && e.clientHeight > 100);
  const H = await p.evaluate(`(${scrl.toString()})().reduce((m, e) => Math.max(m, e.scrollHeight), document.documentElement.scrollHeight)`);
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

// Expand inner scroll containers (Lenis smooth-scroll) so document.scrollHeight
// covers the real content height for the bounded full-page shot.
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl && String(sourceUrl).split(/[?#]/)[0] /* the sidecar reads it from here */ }; this.sourceUrl = sourceUrl; this.count = 0; }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.sourceUrl }, this.requested);
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
    const opts = (extra) => ({ path: extra, sanitizedSourceUrl: this.sourceUrl });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { path: '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  updates: { path: '/updates', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { path: '/download', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  integrations: { path: '/integrations', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  slackalt: { path: '/slack-alternative', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { path: '/terms', wait: 6000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], nav button, [class*="hamburger" i]').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1200); await S.view('menu'); await clickEl(m); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 6000, run: async (p, S) => {
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
