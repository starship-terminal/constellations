// Captures explore.family's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// The domain is dead (the product closed 2023-04-19 and lapsed), so every URL
// is replayed from the Internet Archive mirror by lib.mjs's wireMirror():
// era 'feb' is the 2023-02-23 product build, era 'jun' the 2023-06-08 closure
// announcement. `ssr` pages are the server-rendered profile HTML the app
// sent crawlers, replayed with JavaScript disabled — the SPA cannot render
// profiles because /user/* API responses were never archived. On the SPA's
// own /{username} and /p/{id} routes that same archive gap leaves the shell
// empty; those pages are captured as evidence of exactly that boundary.
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// Explore paints one fixed theme — a grey field, no prefers-color-scheme
// rules and no theme toggle in the signed-out UI (a per-user "dark mode"
// exists only on member portfolios, an authenticated surface). Desktop shots
// are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, capped at 8
// chunks, which quantize.py stitches back together.
// Nothing is sent, created or signed into: there are no presses at all —
// every form is measured at rest only.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, wireMirror, patch, mirrorMisses } from './lib.mjs';

// Full-colour shots are working files, never committed.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, url, era, ssr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.count = 0;
    // The misses this run hit before this page opened, so each sidecar can
    // record only the archive gaps its own page walked into.
    this.missBase = mirrorMisses.length;
    this.archive = { era, snapshot: era === 'jun' ? '2023-06-08' : '2023-02-23', route: new URL(url).pathname + new URL(url).search, ssr: ssr || null };
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: url };
  }
  req() { return { ...this.requested, provenance: { archive: this.archive, mirrorMisses: [...new Set(mirrorMisses.slice(this.missBase))] } }; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.req()); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.req());
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.req());
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Desktop pages on the February (product) build.
const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  discover: { path: '/discover', wait: 12000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  register: { path: '/register', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'forgot-password': { path: '/forgot-password', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  conduct: { path: '/conduct', run: async (p, S) => { await S.view('default'); await S.full(); } },
  // The SPA's own profile/post routes: their API endpoints were never
  // archived, so the app renders the shell only. Captured as the honest
  // boundary of the replay.
  'profile-shell': { path: '/sawdust', wait: 9000, run: async (p, S) => { await S.view('default'); } },
  'post-shell': { path: '/p/2193', wait: 9000, run: async (p, S) => { await S.view('default'); } },
};

// Server-rendered profile HTML (the crawler-facing surface), JavaScript off.
const ssr = {
  'profile-malika': { path: '/malikafavre', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'profile-sawdust': { path: '/sawdust', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

// The June 2023 closure announcement (the last live state of the site).
const june = {
  announcement: { path: '/', wait: 10000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  discover: { path: '/discover', wait: 12000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  register: { path: '/register', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, era: 'feb', ssr: null, spec: desktop[k] })),
  ...Object.keys(ssr).map((k) => ({ k: `ssr-${k}`, mob: false, era: 'feb', ssr: ssr[k].path, spec: ssr[k] })),
  ...Object.keys(june).map((k) => ({ k, mob: false, era: 'jun', ssr: null, spec: june[k] })),
  ...Object.keys(mobile).map((k) => ({ k: `mobile-${k}`, mob: true, era: 'feb', ssr: null, spec: mobile[k] })),
];
for (const { k, mob, era, ssr, spec } of runs) {
  if (pageArg.length && !pageArg.includes(k)) continue;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', javaScriptEnabled: !ssr });
  await patch(ctx);
  await wireMirror(ctx, { era, ssr });
  const p = await ctx.newPage();
  // Tiled full-page shots on a 23k-px page can need longer than the 30s
  // default while the renderer walks the tiles.
  p.setDefaultTimeout(120000);
  log(k);
  const S = new Shooter(p, `${k}-light`, vw, vh, dpr, BASE + spec.path, era, ssr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await wait(p, spec.wait || 6000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', k, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('mirror misses (archive gaps):', JSON.stringify([...new Set(mirrorMisses)], null, 1));
log('done', total, 'screenshots ->', RAW);
await b.close();
