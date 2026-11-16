// Captures flowmapp.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Both hosts
// paint light only — www.flowmapp.com (Webflow) declares color-scheme normal with no
// dark media query anywhere, and the app.flowmapp.com SPA has no theme toggle — so
// every shot is `-light`. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI toggles —
// the Features nav popover (hover), the pricing billed-monthly/annually tab, a FAQ
// disclosure, the mobile burger menu, and on the published read-only demo share the
// Structure/Estimation tabs and the Demo Project dropdown. The signin, signup and
// restore forms are shot at rest, never submitted; every link is measured, never
// followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP, LOGIN_URL, SIGNUP_URL, RESTORE_URL, SHARE, SHARE_SITEMAP, SHARE_USERFLOW } from './lib.mjs';

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

// Opens the marketing nav's Features popover — a real hover-driven Webflow
// dropdown (div.nav__link.pop__is-br-8 → .nav__pop panel). A local UI state;
// its links are never followed.
async function featuresMenu(p, S, shotName) {
  const t = p.locator('.nav__link.pop__is-br-8').filter({ hasText: /Features/ }).first();
  if (!(await t.count())) return;
  await t.hover();
  await wait(p, 1400);
  const open = await p.evaluate(() => {
    const pop = document.querySelector('.nav__pop');
    if (!pop) return false;
    const r = pop.getBoundingClientRect();
    return r.height > 100 && parseFloat(getComputedStyle(pop).opacity) > 0.05;
  }).catch(() => false);
  if (!open) { log('  ! features popover did not report open'); return; }
  await S.view(shotName);
  await p.mouse.move(700, 500);
  await wait(p, 600);
}

// Clicks a pricing billing tab — a Webflow w-tab-link that only switches the
// displayed price pane (Billed monthly / Billed annually). A local UI toggle.
async function billingTab(p, S, tabText, shotName) {
  const t = p.locator('a.p-tabs__btn').filter({ hasText: tabText }).first();
  if (!(await t.count())) return;
  await clickEl(t);
  await wait(p, 900);
  await S.view(shotName);
}

// Opens one FAQ disclosure on the pricing page — the question row is a local
// toggle that expands its answer.
async function faqOpen(p, S, shotName) {
  const q = p.locator('.faq__q-wrap').filter({ visible: true }).first();
  if (!(await q.count())) return;
  await q.scrollIntoViewIfNeeded();
  await clickEl(q);
  await wait(p, 900);
  await S.view(shotName);
}

// On the shared demo sitemap: the Structure/Estimation buttons are the
// viewer's own tabs — a local UI toggle on a read-only public share.
async function shareTab(p, S, tabText, shotName) {
  const b = p.getByRole('button', { name: tabText, exact: true }).first();
  if (!(await b.count())) return;
  await clickEl(b);
  await wait(p, 2500);
  await S.view(shotName);
}

// On the shared demo: the "Demo Project" ant-dropdown trigger opens the
// project's item menu — a local UI toggle; its items are never activated.
async function demoMenu(p, S, shotName) {
  const b = p.locator('button.ant-dropdown-trigger').filter({ hasText: /Demo Project/ }).first();
  if (!(await b.count())) return;
  await clickEl(b);
  await wait(p, 1500);
  const open = await p.evaluate(() => !!document.querySelector('.ant-dropdown:not(.ant-dropdown-hidden), [class*="dropdown"]:not([class*="hidden"])')).catch(() => false);
  if (!open) { log('  ! demo dropdown did not report open'); }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.mouse.click(500, 500);
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('features-menu', () => featuresMenu(p, S, 'features-menu'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('billed-monthly', () => billingTab(p, S, 'Billed monthly', 'billed-monthly'));
    await step('faq-open', () => faqOpen(p, S, 'faq-open'));
    await S.full();
  } },
  'product-overview': { url: BASE + '/product-overview', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-sitemap': { url: BASE + '/features/sitemap', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-userflow': { url: BASE + '/features/userflow', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-wireframes': { url: BASE + '/features/wireframes', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'use-case': { url: BASE + '/features/use-case-boost-website-sales', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  reviews: { url: BASE + '/reviews', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'blog-article': { url: BASE + '/blog/articles/13-startups-focused-on-clean-ui', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  security: { url: BASE + '/security', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: BASE + '/terms', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact-us', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'sitemap-generator': { url: BASE + '/sitemap-generator', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: SIGNUP_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  restore: { url: RESTORE_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'share-project': { url: SHARE, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'share-sitemap': { url: SHARE_SITEMAP, wait: 12000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('estimation', () => shareTab(p, S, 'Estimation', 'estimation'));
    await step('structure-back', () => shareTab(p, S, 'Structure', 'structure-back'));
    await step('demo-menu', () => demoMenu(p, S, 'demo-menu'));
  } },
  'share-userflow': { url: SHARE_USERFLOW, wait: 12000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The burger button (.nav__burger, a Webflow w-nav-button) opens the
      // nav overlay — a local UI toggle; its links are never followed.
      const t = p.locator('.nav__burger').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'share-sitemap': { url: SHARE_SITEMAP, wait: 12000, theme: 'light', run: async (p, S) => {
    await S.view('default');
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
