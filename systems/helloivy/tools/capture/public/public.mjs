// Captures Hello Ivy's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full-page shots are 1x
// (phone full-page is also 1x so a tall page stays under the GPU tile cap).
// Nothing is submitted. Login, signup, Google, Apple, and mailto are never clicked.
// The menu overlay is opened by clicking the header icon, then closed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, hideOverlays, openMenu, closeMenu, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'helloivy', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const TILE_CAP = 8;
async function lazyScroll(p, maxY = Infinity) {
  const h = Math.min(await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)), maxY);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = TILE_CAP * chunk;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (H0 > MAXH) log('  CLAMPED pre-scroll', H0, '->', MAXH);
    await lazyScroll(p, Math.min(H0, MAXH));
    let H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    if (H > MAXH) { log('  CLAMPED', H, '->', MAXH); H = MAXH; }
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < H; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

let failures = 0;
const step = async (label, fn) => {
  try { await fn(); } catch (e) { failures++; log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function menuShot(p, S) {
  const opened = await openMenu(p);
  if (!opened) { log('  menu icon missing'); return; }
  await wait(p, 400);
  await S.view('menu');
  await closeMenu(p);
  await wait(p, 300);
}

const desktop = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await menuShot(p, S); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'features-tasks': { path: '/features/tasks', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/tips-tricks-for-using-hello-ivy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-article': { path: '/docs/create-a-project', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'release-notes': { path: '/release-notes', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'project-management': { path: '/project-management', run: async (p, S) => { await S.view('default'); await S.full(); } },
  alternative: { path: '/notion-alternative', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: {
    path: 'https://app.helloivy.co/login',
    auth: true,
    run: async (p, S) => { await S.view('default'); await S.full(); },
  },
};

const mobile = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await menuShot(p, S); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); } },
  login: {
    path: 'https://app.helloivy.co/login',
    auth: true,
    run: async (p, S) => { await S.view('default'); },
  },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.path.startsWith('http') ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await hideOverlays(p);
    if (spec.auth) {
      const u = p.url();
      if (!/app\.helloivy\.co\/login/.test(u)) log('  unexpected login url', u);
    }
    await spec.run(p, S);
  } catch (e) {
    failures++;
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW, 'failures', failures);
await b.close();
if (failures) process.exitCode = 1;
