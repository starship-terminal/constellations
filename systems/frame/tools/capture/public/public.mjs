// Captures frame.io's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// public frame.io page paints the same dark theme (html field #000, ink #fcfcfc)
// — there is no theme switch, so shots are -dark. accounts.frame.io/welcome is
// the sign-in surface, a light page on a different stack (styled-components),
// shot as -light. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded
// page truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the header's
// "Features"/"Enterprise"/"Resources" mega-menu triggers and the phone's
// "Toggle mobile navigation" button. The contact, contact-form and sign-in
// forms are shot at rest, never submitted. The announcement banner and the
// geo-redirect notice are real chrome and stay; any consent overlay is hidden,
// never answered.
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
    // the default 30s; pausing media and allowing 120s keeps the shot on heavy pages.
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

// Opens one of the header's mega-menu overlays ("Features"/"Enterprise"/
// "Resources" — the button[class*="navigationMainItem"] copy inside
// nav.mainNavigation; the phone nav's twin set renders at 0x0). A pointer
// click flips the group's
// NavGroup_open__ class (the nav gains Navigation_subNavOpen__); keyboard
// Enter is the fallback. Links inside are never followed. Escape closes.
async function navMenu(p, S, name) {
  const btn = p.locator('nav[class*="mainNavigation"] button[class*="navigationMainItem"]').filter({ hasText: new RegExp(`^${name}$`) }).first();
  if (!(await btn.count())) { log('  ! no trigger', name); return; }
  const open = async () => p.evaluate(() => !!document.querySelector('[class*="subNavOpen"], [class*="NavGroup_open"]')).catch(() => false);
  for (let i = 0; i < 3 && !(await open()); i++) {
    await btn.click({ timeout: 5000 }).catch(() => {});
    await wait(p, 1200);
    if (!(await open())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 1200); }
  }
  if (!(await open())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase());
  await p.keyboard.press('Escape');
  await wait(p, 800);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 10000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu-features', () => navMenu(p, S, 'Features'));
    await step('menu-enterprise', () => navMenu(p, S, 'Enterprise'));
    await step('menu-resources', () => navMenu(p, S, 'Resources'));
    await S.full();
  } },
  'features-workflow': { url: BASE + '/features/workflow-management', wait: 9000, theme: 'dark', run: BOTH },
  'features-review': { url: BASE + '/features/review-and-approval', wait: 9000, theme: 'dark', run: BOTH },
  'features-c2c': { url: BASE + '/features/c2c', wait: 9000, theme: 'dark', run: BOTH },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('faq-open', async () => {
      const acc = p.locator('button[class*="FaqItem_question"], button[class*="PricingTable_categoryTitle"]').filter({ visible: true }).first();
      if (await acc.count()) { await acc.scrollIntoViewIfNeeded(); await acc.click({ timeout: 5000 }).catch(() => {}); await wait(p, 900); await S.view('accordion-open'); await acc.click({ timeout: 5000 }).catch(() => {}); }
    });
    await S.full();
  } },
  enterprise: { url: BASE + '/enterprise', wait: 9000, theme: 'dark', run: BOTH },
  'enterprise-me': { url: BASE + '/enterprise/media-and-entertainment', wait: 9000, theme: 'dark', run: BOTH },
  customers: { url: BASE + '/customers', wait: 9000, theme: 'dark', run: BOTH },
  'case-study': { url: BASE + '/case-studies/ford', wait: 9000, theme: 'dark', run: BOTH },
  integrations: { url: BASE + '/integrations', wait: 9000, theme: 'dark', run: BOTH },
  resources: { url: BASE + '/resources', wait: 9000, theme: 'dark', run: BOTH },
  'whats-new': { url: BASE + '/whats-new', wait: 9000, theme: 'dark', run: BOTH },
  contact: { url: BASE + '/contact', wait: 9000, theme: 'dark', run: BOTH },
  'contact-form': { url: BASE + '/contact/form', wait: 9000, theme: 'dark', run: BOTH },
  security: { url: BASE + '/security', wait: 9000, theme: 'dark', run: BOTH },
  ai: { url: BASE + '/ai', wait: 9000, theme: 'dark', run: BOTH },
  drive: { url: BASE + '/drive', wait: 9000, theme: 'dark', run: BOTH },
  transfer: { url: BASE + '/transfer', wait: 9000, theme: 'dark', run: BOTH },
  welcome: { url: LOGIN_URL, wait: 9000, theme: 'light', run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 10000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Toggle mobile navigation" button (ToggleButton_navMobileButton)
      // flips the full-viewport nav overlay — a local UI toggle; its links
      // are never followed.
      const ham = p.locator('button[class*="navMobileButton"], button[aria-label*="navigation" i]').filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! no drawer toggle'); return; }
      const open = () => p.evaluate(() => !!document.querySelector('[class*="subNavOpen"], [class*="mobileMenuOpen" i], [class*="navOpen" i]')).catch(() => false);
      if (!(await open())) await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'dark', run: BOTH },
  'contact-form': { url: BASE + '/contact/form', wait: 9000, theme: 'dark', run: BOTH },
  welcome: { url: LOGIN_URL, wait: 9000, theme: 'light', run: BOTH },
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
