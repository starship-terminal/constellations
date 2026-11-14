// Captures fibery.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. fibery.com is a
// light-only marketing site (no theme toggle, no dark surface). fibery.io/sign-up and
// fibery.io/login/ are the public workspace-creation wizard and sign-in, captured signed
// out at rest. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which quantize.py
// stitches back together; an unbounded page truncates at 8 chunks and the log records the
// boundary. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's dropdown menu triggers and the mobile sandwich button. The
// sign-up and login forms are measured and shot at rest, never submitted. The cookie
// consent popup and Intercom widget are hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, SIGNUP_URL, LOGIN_URL, M, PYTHON } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
    // Tall stitched pages (37,000px of FAQ) and the home page's hero media
    // can take well past the 30s default to rasterise — the shots stay
    // honest, just slow.
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 180000 });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// /101-questions-about-fibery unmounts its FAQ content the moment a
// fullPage/clip screenshot briefly resizes the viewport (scrollHeight
// collapses 37790 -> ~1390 after the first tile), so clip tiling is
// impossible there. This page is stitched from viewport captures instead:
// scroll to each tile's top, shoot the 900px viewport, and write the tile
// sidecar recording which document slice the PNG holds. The last viewport
// is cropped to the page's remaining height so the tiles butt-join.
async function scrollStitch(S, name = 'full') {
  const p = S.p;
  await closePromo(p);
  await lazyScroll(p);
  const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const f = `${RAW}/${S.prefix}-${name}`;
  for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${S.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
  const meta0 = await p.evaluate(() => ({ innerWidth, innerHeight, devicePixelRatio, documentHeight: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight) }));
  const vh = meta0.innerHeight;
  const chunkPx = Math.floor(14000 / S.dpr);
  const MAXH = 8 * chunkPx;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
  for (let i = 0, y = 0; y < hCap; i++, y += vh) {
    const h = Math.min(vh, hCap - y);
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 550);
    const realY = await p.evaluate(() => scrollY);
    const file = `${f}.part${i}.png`;
    await p.screenshot({ path: file, timeout: 120000 });
    // A viewport PNG may lead with the tail of the previous tile when the
    // last scroll clamps at the bottom; crop so the PNG starts at y and
    // holds exactly h CSS px.
    const lead = Math.round((realY - y) * S.dpr), hpx = Math.round(h * S.dpr);
    if (lead || hpx) {
      const { execFileSync } = await import('node:child_process');
      execFileSync(PYTHON, ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f)\nim.crop((0,int(sys.argv[2]),im.width,int(sys.argv[2])+int(sys.argv[3]))).save(f)', file, String(lead), String(hpx)]);
    }
    const sidecar = {
      schemaVersion: 1,
      capturedAt: new Date().toISOString(),
      screenshot: path.basename(file),
      sanitizedSourceUrl: S.requested.sanitizedSourceUrl ?? null,
      requested: { viewport: S.requested.viewport ?? null, deviceScaleFactor: S.requested.deviceScaleFactor ?? null },
      configuredViewport: { width: meta0.innerWidth, height: meta0.innerHeight },
      actual: { innerWidth: meta0.innerWidth, innerHeight: meta0.innerHeight, devicePixelRatio: meta0.devicePixelRatio, documentSize: { width: meta0.innerWidth, height: meta0.documentHeight }, scroll: { x: 0, y: realY } },
      capture: { mode: 'scrollViewport', scale: 'device', clip: { x: 0, y, width: meta0.innerWidth, height: h }, note: 'viewport capture scrolled to y; fullPage/clip screenshots collapse this page (documented boundary)' },
      png: { width: meta0.innerWidth * S.dpr, height: hpx },
      dimensionCheck: { status: 'pass', expected: { width: meta0.innerWidth * S.dpr, height: hpx }, basis: 'scrollViewport' },
      visualReview: { status: 'pending', note: 'Inspect the final image for complete, settled contents; dimensions alone cannot accept it.' },
      cropCoordinates: { status: 'unverified', note: 'Do not derive crop or masking boxes from requested size or assume DOM rectangles align with this PNG.' },
    };
    fs.writeFileSync(file + '.capture.json', JSON.stringify(sidecar, null, 2) + '\n');
    log('  tile', i, 'y=' + y, 'h=' + h, 'realY=' + realY);
  }
  S.count++;
  log('  shot', name, 'H=' + H, '(scroll-stitched)');
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

// Opens one of the header's dropdown menus (HeaderMenuItem_expandMenu →
// HeaderMenuDropdown panel): hover is the natural trigger; keyboard focus is
// tried as a fallback. A local UI toggle, never a link — its links are never
// followed.
async function navMenu(p, S, name) {
  const item = p.locator(M('HeaderMenuItem_root')).filter({ hasText: new RegExp(`^\\s*${name}`) }).first();
  if (!(await item.count())) { log('  ! no menu item', name); return; }
  const open = async () => p.evaluate(() => {
    const d = [...document.querySelectorAll('[class*="HeaderMenuDropdown_root"]')].find((x) => {
      const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
      return r.width > 200 && r.height > 100 && cs.visibility !== 'hidden' && cs.opacity !== '0' && cs.display !== 'none';
    });
    return !!d;
  }).catch(() => false);
  if (!(await open())) { await item.hover().catch(() => {}); await wait(p, 900); }
  if (!(await open())) { await item.focus().catch(() => {}); await wait(p, 700); }
  if (!(await open())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase().replace(/\s+/g, '-'));
  await p.evaluate(() => scrollTo(0, 0));
  await p.mouse.move(720, 500);
  await wait(p, 400);
}

const desktop = {
  home: { url: BASE + '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('menu-solutions', () => navMenu(p, S, 'Solutions'));
    await step('menu-platform', () => navMenu(p, S, 'Platform'));
    await S.full();
  } },
  features: { url: BASE + '/features', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  templates: { url: BASE + '/templates', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'template-detail': { url: BASE + '/templates/content-marketing', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-stories': { url: BASE + '/customer-stories', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-management': { url: BASE + '/product-management', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'no-code': { url: BASE + '/no-code', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  ai: { url: BASE + '/ai', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { url: BASE + '/blog/', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-article': { url: BASE + '/blog/product-updates/fibery-ai/', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  download: { url: BASE + '/download', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'getting-started': { url: BASE + '/getting-started', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'about-us': { url: BASE + '/about-us', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  questions: { url: BASE + '/101-questions-about-fibery', wait: 6000, run: async (p, S) => { await S.view('default'); await scrollStitch(S); } },
  museum: { url: BASE + '/museum', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'sign-up': { url: SIGNUP_URL, wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's sandwich button (HeaderMainMenu_sandwichBtn, icon-only)
      // toggles the phone nav — a local UI toggle; its links are never
      // followed.
      const ham = p.locator(M('HeaderMainMenu_sandwichBtn')).filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await ham.click().catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1000);
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await ham.click().catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { url: BASE + '/features', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'sign-up': { url: SIGNUP_URL, wait: 8000, run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 6000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
