// Captures enode.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Most enode.com
// marketing pages paint `data-mode="light"`; /platform/overview and /platform/flexibility paint
// `data-mode="dark"` on <html> itself, and the light pages carry scoped [data-mode="dark"]
// showcase/mega-menu sections. platform.enode.com/login is dark-framed with a light sign-in
// panel, captured signed out at rest. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the header's "Platform"
// and "Resources" mega-menu buttons (aria-haspopup="dialog" panels) and the mobile hamburger.
// The /contact and /login forms are measured and shot at rest, never submitted. The dormant
// Cookiebot script shows no banner; any consent overlay is hidden, never answered.
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

// Opens one of the header mega-menus ("Platform"/"Resources" — aria-haspopup
// dialog buttons, local UI toggles, never links) and shoots the panel. The
// Platform panel holds autoplaying video tiles whose repaints can starve a
// screenshot frame, so videos pause while the menu is open.
async function navMenu(p, S, name) {
  const btn = p.locator('header button[aria-haspopup="dialog"]').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return;
  // The trigger opens on keyboard activation: pointer clicks do not flip it in
  // headless Chromium, so it is focused and opened with Enter.
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await btn.focus();
    await p.keyboard.press('Enter');
    await wait(p, 900);
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
  await S.view('menu-' + name.toLowerCase());
  await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-platform', () => navMenu(p, S, 'Platform'));
    await step('menu-resources', () => navMenu(p, S, 'Resources'));
    await S.full();
  } },
  'platform-overview': { url: BASE + '/platform/overview', wait: 7000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'platform-homes': { url: BASE + '/platform/homes', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'platform-flexibility': { url: BASE + '/platform/flexibility', wait: 7000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'platform-assets': { url: BASE + '/platform/assets', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { url: BASE + '/enterprise', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { url: BASE + '/customers', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'customers-vattenfall': { url: BASE + '/customers/vattenfall', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  company: { url: BASE + '/company', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  careers: { url: BASE + '/careers', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  partnerships: { url: BASE + '/partnerships', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  newsroom: { url: BASE + '/newsroom', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'newsroom-article': { url: BASE + '/newsroom/vattenfall-and-enode-bring-smart-charging-to-ev-owners-in-sweden', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  updates: { url: BASE + '/updates', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'updates-article': { url: BASE + '/updates/introducing-asset-overview-find-the-right-assets-in-seconds-not-days', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'contact-partnerships': { url: BASE + '/contact/partnerships', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy-policy', wait: 6000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's round menu button (no text, icon-only) toggles the nav
      // overlay — a local UI toggle; its links are never followed. Falls back
      // to keyboard Enter when a pointer activation does not flip it.
      const ham = p.locator('header button').filter({ visible: true }).last();
      if (!(await ham.count())) return;
      const open = () => p.evaluate(() => !!([...document.querySelectorAll('body > div, body > nav, [role="dialog"]')].find((x) => {
        const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
        return r.height > 300 && /\S/.test(x.textContent || '') && cs.position === 'fixed' && cs.visibility !== 'hidden' && cs.opacity !== '0';
      }))).catch(() => false);
      if (!(await open())) await clickEl(ham);
      await wait(p, 1000);
      if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 1000); }
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  'platform-overview': { url: BASE + '/platform/overview', wait: 7000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  updates: { url: BASE + '/updates', wait: 7000, theme: 'light', run: async (p, S) => {
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
