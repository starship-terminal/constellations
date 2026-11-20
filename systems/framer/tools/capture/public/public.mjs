// Captures framer.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The
// marketing pages on www.framer.com paint one surface — the dark Framer-site
// palette declared as ~580 `--token-<uuid>` colour styles on `body` (black
// page, white-alpha hairlines, the #cbff00 lime); there is no theme switcher,
// so those shots are -dark. /community/gallery and /marketplace/* are the
// product's community/marketplace stack, a different app that also paints
// dark; /login is the auth shell, a light third stack, so its shots are
// -light. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full`
// shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates
// at 8 chunks and the log records the boundary. Nothing is sent, bought or
// signed into: the only activations are local UI toggles — hovering the
// header's "Platform" mega-dropdown and the phone's nav button. The login
// form is shot at rest, never submitted. The "We use cookies to enhance your
// experience" consent card is hidden before every shot, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LOGIN_URL } from './lib.mjs';

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
    // Pages whose demos autoplay video/canvas can stall a full-page raster past
    // the default 30s; pausing media and allowing 120s keeps the shot on heavy
    // pages.
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    try {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    } catch (e) {
      log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Opens one of the header's mega-dropdowns by hovering its trigger ("Platform",
// "Solutions", "Resources" — `a` elements without href whose panels mount
// under the bar; never followed). The menu is hover-driven: the pointer rests
// on the trigger until the panel reports non-zero size, then the shot. The
// pointer leaves to the page edge afterwards so the panel closes.
async function navMenu(p, S, name) {
  const btn = p.locator('nav a, header a, div a').filter({ hasText: new RegExp(`^${name}`) }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no', name, 'trigger'); return; }
  const open = async () => p.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    return els.some((x) => {
      const t = (x.innerText || '');
      const r = x.getBoundingClientRect();
      return r.y > 20 && r.y < 400 && r.width > 300 && r.height > 150 && /^(Create|Design|Build|Grow|Product|Learn|Company)\b/.test(t.trim());
    });
  }).catch(() => false);
  for (let i = 0; i < 4 && !(await open()); i++) {
    await btn.hover({ timeout: 5000 }).catch(() => {});
    await wait(p, 1200);
  }
  if (!(await open())) { log('  ! menu', name, 'did not report open'); }
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
  await S.view('menu-' + name.toLowerCase());
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
  const vw = p.viewportSize()?.width ?? 1440;
  await p.mouse.move(vw - 2, 890); await wait(p, 800);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu-platform', () => navMenu(p, S, 'Platform'));
    await step('menu-solutions', () => navMenu(p, S, 'Solutions'));
    await step('menu-resources', () => navMenu(p, S, 'Resources'));
    await S.full();
  } },
  ai: { url: BASE + '/ai/', wait: 9000, theme: 'dark', run: BOTH },
  agents: { url: BASE + '/agents/', wait: 9000, theme: 'dark', run: BOTH },
  design: { url: BASE + '/design/', wait: 9000, theme: 'dark', run: BOTH },
  mcp: { url: BASE + '/mcp/', wait: 9000, theme: 'dark', run: BOTH },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'dark', run: BOTH },
  enterprise: { url: BASE + '/enterprise/', wait: 9000, theme: 'dark', run: BOTH },
  about: { url: BASE + '/about', wait: 9000, theme: 'dark', run: BOTH },
  updates: { url: BASE + '/updates', wait: 9000, theme: 'dark', run: BOTH },
  academy: { url: BASE + '/academy/', wait: 9000, theme: 'dark', run: BOTH },
  developers: { url: BASE + '/developers/', wait: 9000, theme: 'dark', run: BOTH },
  blog: { url: BASE + '/blog/', wait: 9000, theme: 'dark', run: BOTH },
  stories: { url: BASE + '/stories/', wait: 9000, theme: 'dark', run: BOTH },
  careers: { url: BASE + '/careers/', wait: 9000, theme: 'dark', run: BOTH },
  contact: { url: BASE + '/contact/', wait: 9000, theme: 'dark', run: BOTH },
  downloads: { url: BASE + '/downloads/', wait: 9000, theme: 'dark', run: BOTH },
  compare: { url: BASE + '/compare', wait: 9000, theme: 'dark', run: BOTH },
  'solutions-designers': { url: BASE + '/solutions/designers/', wait: 9000, theme: 'dark', run: BOTH },
  'community-gallery': { url: BASE + '/community/gallery/', wait: 10000, theme: 'dark', run: BOTH },
  'marketplace-templates': { url: BASE + '/marketplace/templates/', wait: 10000, theme: 'dark', run: BOTH },
  login: { url: LOGIN_URL, wait: 10000, theme: 'light', run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's nav toggle on the phone surface — a local UI toggle;
      // its links are never followed. Framer sites switch the nav control
      // to a menu variant under the 810px breakpoint; the button may carry
      // an aria-label or no text at all.
      const btn = p.locator('[data-framer-name="Mobile Menu"], [data-framer-name="Menu"], [data-framer-name="navswitch"], button[aria-label*="menu" i], button[aria-label*="navigation" i]').filter({ visible: true }).first();
      if (!(await btn.count())) { log('  ! no mobile menu toggle found'); return; }
      await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'dark', run: BOTH },
  'community-gallery': { url: BASE + '/community/gallery/', wait: 10000, theme: 'dark', run: BOTH },
  contact: { url: BASE + '/contact/', wait: 9000, theme: 'dark', run: BOTH },
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
    await wait(p, spec.wait || 8000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
