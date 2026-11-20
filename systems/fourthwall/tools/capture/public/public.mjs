// Captures fourthwall.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. fourthwall.com
// (Webflow) paints one light surface with scoped dark "on-ink" sections — there is no
// marketing theme toggle, so the dark sections are shot as part of the light page, not
// as a theme. products.fourthwall.com paints the catalogue DS in light (its light-dark()
// dark branch is declared only — no theme toggle, so there are no catalog-dark shots).
// /get-started redirects to auth.fourthwall.com (Keycloak); shot at rest, nothing typed.
// docs.fourthwall.com (Mintlify) ships a real "Change theme preference" menu — the
// docs-dark shots are the genuinely toggled theme. help.fourthwall.com (Docusaurus)
// ships a real dark toggle — the help-dark shots are toggled for real. Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the
// Features mega-menu, the signup modal's open/close, the pricing billing toggle, a FAQ
// disclosure, the compare search field, the catalogue search field and quiz option, the
// PDP size-guide dialog and print-type option, the docs search dialog and theme menu,
// the help search and dark toggle. The signup/auth choices and every commerce action
// ("Sign in to design", "Start now" destinations) are measured, never activated; every
// link is measured, never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, PRODUCTS, DOCS, HELP, SIGNUP_URL, PDP_URL, ALL_URL } from './lib.mjs';

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
    const opts = (extra) => ({ path: extra, scale: 'css', animations: 'disabled', timeout: 90000 });
    if (hCap <= chunk) {
      try {
        await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      } catch (e) {
        // A single tall fullPage render can stall on image-heavy pages (the
        // get-inspired wall timed out at 90s): fall back to 6000px clips.
        if (!/timeout/i.test(e.message)) throw e;
        log('  ! full-page render timed out, falling back to 6000px clips');
        const small = 6000;
        for (let i = 0, y = 0; y < hCap; i++, y += small) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(small, hCap - y) } }, this.requested);
      }
    }
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Hovers the "Features" nav item — the Webflow mega-menu opens on hover and
// the .mega-clip panel appears. A local UI toggle; its links are never followed.
async function megaMenu(p, S, shotName) {
  const trig = p.locator('.nav-bar a, .nav-bar [role="button"], .nav-bar .nav-link, .nav-bar .w-dropdown-toggle').filter({ hasText: /Features/i }).first();
  if (!(await trig.count())) { log('  ! no Features nav item'); return; }
  await trig.hover({ timeout: 5000 }).catch(() => trig.hover({ timeout: 5000, force: true }));
  await wait(p, 1200);
  const open = await p.evaluate(() => {
    const clip = document.querySelector('.mega-clip, .nav-menu .w-dropdown-list, [class*="mega"]');
    if (!clip) return false;
    const r = clip.getBoundingClientRect();
    const cs = getComputedStyle(clip);
    return r.height > 60 && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05;
  }).catch(() => false);
  if (!open) { await clickEl(trig); await wait(p, 900); }
  const open2 = await p.evaluate(() => { const c = document.querySelector('.mega-clip, .nav-menu .w-dropdown-list, [class*="mega"]'); if (!c) return false; const r = c.getBoundingClientRect(); return r.height > 60 && getComputedStyle(c).display !== 'none'; }).catch(() => false);
  if (!open2) { log('  ! mega menu did not report open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.mouse.move(10, 600);
  await wait(p, 600);
}

// Opens the marketing signup modal — the nav "Start now" control mounts
// .signup-modal with the Google/Apple/email choices. If the control navigates
// instead, the run goes back and shoots nothing. No provider button is pressed.
async function signupModal(p, S, shotName) {
  const btn = p.locator('.nav-bar a, .nav-bar button, .nav-bar [role="button"]').filter({ hasText: /^\s*Start now\s*$/i }).first();
  if (!(await btn.count())) { log('  ! no Start-now control'); return; }
  const url0 = p.url();
  await clickEl(btn);
  await wait(p, 1600);
  if (p.url() !== url0) {
    await p.goBack().catch(() => {});
    await wait(p, 2500);
    // /get-started 302s onward to auth.fourthwall.com; history.back() can land
    // on the redirector and bounce forward — reload home if we did not return.
    if (!p.url().startsWith(BASE)) { await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {}); await wait(p, 7000); }
    log('  ! Start now navigates; modal not reachable locally');
    return;
  }
  const open = await p.evaluate(() => { const m = document.querySelector('.signup-modal'); if (!m) return false; const cs = getComputedStyle(m); const r = m.getBoundingClientRect(); return cs.display !== 'none' && parseFloat(cs.opacity) > 0.05 && r.height > 100; }).catch(() => false);
  if (!open) { log('  ! signup modal did not open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.evaluate(() => { const x = document.querySelector('.signup-modal [class*="close"], .signup-modal [aria-label*="close" i], .signup-modal .w-icon-dropdown-toggle'); if (x) x.click(); }).catch(() => {});
  await wait(p, 600);
}

// Flips the pricing billing toggle to monthly — a local UI toggle that swaps
// the painted plan prices ($15 -> $19 Pro). Never touches a checkout action.
async function billingMonthly(p, S, shotName) {
  const btn = p.locator('.billing-toggle-btn').filter({ hasText: /monthly/i }).first();
  if (!(await btn.count())) { log('  ! no billing toggle'); return; }
  await clickEl(btn);
  await wait(p, 1000);
  const active = await p.evaluate(() => [...document.querySelectorAll('.billing-toggle-btn')].some((b) => /monthly/i.test(b.innerText) && /is-active/.test(b.className))).catch(() => false);
  if (!active) { log('  ! billing toggle did not report monthly'); return; }
  await S.view(shotName);
}

// Opens one FAQ disclosure on /pricing or /faq — a local UI toggle.
async function faqOpen(p, S, shotName) {
  const btn = p.locator('.ph-faq-summary, .faq-summary, summary, [class*="faq-summary"]').filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no FAQ summary'); return; }
  await btn.scrollIntoViewIfNeeded().catch(() => {});
  await clickEl(btn);
  await wait(p, 900);
  await S.view(shotName);
}

// Types into the /compare platform search — a local filter; the text is
// deleted again. Nothing is sent.
async function cmpSearch(p, S, shotName) {
  const f = p.locator('input[type="search"], input[placeholder*="earch"], .cmp-search input').filter({ visible: true }).first();
  if (!(await f.count())) { log('  ! no compare search'); return; }
  await f.click();
  await p.keyboard.type('shopify', { delay: 20 });
  await wait(p, 1200);
  await S.view(shotName);
  await f.fill('').catch(() => {});
  await wait(p, 500);
}

// Types into the catalogue search — a local filter over products; the text is
// deleted again. Nothing is sent or designed.
async function catalogSearch(p, S, shotName) {
  // The catalogue's nav search is a bare input[type=text] with no placeholder
  // or aria-label — the only visible text input in the header.
  let f = p.locator('input[type="search"], input[placeholder*="earch"], input[aria-label*="earch"], input[type="text"]').filter({ visible: true }).first();
  if (!(await f.count())) {
    const trig = p.locator('button[aria-label*="earch"], a[href*="search"], [class*="search"]').filter({ visible: true }).first();
    if (!(await trig.count())) { log('  ! no catalog search'); return; }
    await clickEl(trig);
    await wait(p, 900);
    f = p.locator('input[type="search"], input[placeholder*="earch"], input[aria-label*="earch"], input[type="text"]').filter({ visible: true }).first();
    if (!(await f.count())) { log('  ! catalog search field did not appear'); return; }
  }
  await f.click();
  await p.keyboard.type('hoodie', { delay: 20 });
  await wait(p, 2000);
  await S.view(shotName);
  await f.fill('').catch(() => {});
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// Clicks one answer option in the catalogue's "What are you looking for?"
// quiz card — a local selection that retints the card; no recommendation is
// submitted (the quiz never leaves the page without more choices).
async function quizPick(p, S, shotName) {
  const opt = p.locator('button, [role="button"], a, li, label').filter({ hasText: /^(Premium quality|Budget-friendly|Streetwear|Accessories|Drinkware|Home & living)$/i }).filter({ visible: true }).first();
  if (!(await opt.count())) { log('  ! no quiz option'); return; }
  const url0 = p.url();
  await opt.scrollIntoViewIfNeeded().catch(() => {});
  await clickEl(opt);
  await wait(p, 1000);
  if (p.url() !== url0) { await p.goBack().catch(() => {}); await wait(p, 2000); log('  ! quiz option navigated'); return; }
  await S.view(shotName);
}

// Opens the PDP size-guide dialog — a local UI toggle mounting a size table.
async function sizeGuide(p, S, shotName) {
  const btn = p.locator('button, [role="button"], a').filter({ hasText: /Size guide/i }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no size guide'); return; }
  await clickEl(btn);
  await wait(p, 1200);
  const open = await p.evaluate(() => { const d = document.querySelector('[role="dialog"], [class*="dialog"], [class*="modal"]'); return d && d.getBoundingClientRect().height > 60; }).catch(() => false);
  if (!open) { log('  ! size guide did not open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// Selects the "Embroidered (stitched)" print-type option — a local option
// toggle on the PDP; it changes the displayed price/decorator only.
async function printType(p, S, shotName) {
  const opt = p.locator('button, [role="button"], label, [role="radio"]').filter({ hasText: /Embroidered \(stitched\)/i }).filter({ visible: true }).first();
  if (!(await opt.count())) { log('  ! no embroidery option'); return; }
  await opt.scrollIntoViewIfNeeded().catch(() => {});
  await clickEl(opt);
  await wait(p, 1100);
  await S.view(shotName);
}

// Clicks the docs search — opens the Mintlify dialog on the
// button[aria-label="Open search"] trigger; the "Search..." input takes focus
// and results paint under it. Nothing is sent.
async function docsSearch(p, S, shotName) {
  const f = p.locator('button[aria-label="Open search"], button[data-search-item="trigger"], input[placeholder*="earch"], button[aria-label*="earch"]').filter({ visible: true }).first();
  if (!(await f.count())) { log('  ! no docs search'); return; }
  await clickEl(f);
  await wait(p, 1500);
  const open = await p.evaluate(() => [...document.querySelectorAll('[role="dialog"], [cmdk-root], input[placeholder="Search..."]')].some((d) => { const r = d.getBoundingClientRect(); return r.width > 100 && r.height > 40; })).catch(() => false);
  if (!open) { log('  ! docs search did not open'); return; }
  await p.keyboard.type('auth', { delay: 15 });
  await wait(p, 1200);
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 600);
}

// Opens the docs "Change theme preference" menu — a local UI toggle listing
// Light/Dark/System. The menu is shot; the choice happens in docsDarkOn.
async function docsThemeMenu(p, S, shotName) {
  const btn = p.locator('button[aria-label="Change theme preference"], button[aria-label*="theme preference" i]').filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no theme menu button'); return; }
  await clickEl(btn);
  await wait(p, 900);
  const open = await p.evaluate(() => { const m = document.querySelector('[role="menu"], [data-radix-popper-content-wrapper], [class*="dropdown"]'); return m && m.getBoundingClientRect().height > 40; }).catch(() => false);
  if (!open) { log('  ! theme menu did not open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// The docs site's real dark toggle: theme menu -> Dark, sets html.dark
// (persisted in localStorage inside this context).
async function docsDarkOn(p) {
  const cur = await p.evaluate(() => document.documentElement.classList.contains('dark')).catch(() => false);
  if (cur) return true;
  const btn = p.locator('button[aria-label="Change theme preference"], button[aria-label*="theme preference" i]').filter({ visible: true }).first();
  if (!(await btn.count())) return false;
  await clickEl(btn);
  await wait(p, 900);
  const dk = p.locator('[role="menu"] *, [data-radix-popper-content-wrapper] *, [role="menuitem"], [role="option"]').filter({ hasText: /^Dark$/ }).first();
  if (!(await dk.count())) { await p.keyboard.press('Escape').catch(() => {}); return false; }
  await clickEl(dk);
  await wait(p, 1200);
  return (await p.evaluate(() => document.documentElement.classList.contains('dark')).catch(() => false));
}

// Types into the help navbar search — the Docusaurus local-search filter;
// the text is deleted again, nothing is sent.
async function helpSearch(p, S, shotName) {
  const f = p.locator('.navbar input[type="search"], input[placeholder*="earch"], input[type="search"]').filter({ visible: true }).first();
  if (!(await f.count())) { log('  ! no help search'); return; }
  await f.click();
  await p.keyboard.type('storefront', { delay: 20 });
  await wait(p, 1500);
  await S.view(shotName);
  await f.fill('').catch(() => {});
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// The help site's real dark toggle: the Docusaurus colour-mode button in the
// navbar sets <html data-theme="dark"> and persists it in this context.
async function helpDark(p, on) {
  const cur = await p.evaluate(() => document.documentElement.getAttribute('data-theme')).catch(() => null);
  if ((cur === 'dark') === on) return true;
  const btn = p.locator('button[aria-label*="Switch between" i], [class*="colorModeToggle"] button, button[class*="colorModeToggle"], button[class*="toggleButton"], .navbar button[class*="toggle"]').filter({ visible: true }).first();
  // The toggle cycles system -> light -> dark -> …, so keep clicking until the
  // wanted state paints (three clicks covers the whole cycle).
  for (let i = 0; i < 3; i++) {
    let b = btn;
    if (!(await b.count())) {
      // The toggle is icon-only in some builds: fall back to the last navbar button.
      const fb = p.locator('.navbar__items--right button, .navbar__items button').filter({ visible: true }).last();
      if (!(await fb.count())) return false;
      b = fb;
    }
    await clickEl(b);
    await wait(p, 1100);
    const t = await p.evaluate(() => document.documentElement.getAttribute('data-theme')).catch(() => null);
    if ((t === 'dark') === on) return true;
  }
  return false;
}

const simple = (view = 'default') => async (p, S) => { await S.view(view); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('mega-menu', () => megaMenu(p, S, 'mega-menu'));
    await step('signup-modal', () => signupModal(p, S, 'signup-modal'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('billing-monthly', () => billingMonthly(p, S, 'billing-monthly'));
    await step('faq-open', () => faqOpen(p, S, 'faq-open'));
    await S.full();
  } },
  faq: { url: BASE + '/faq', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('faq-open', () => faqOpen(p, S, 'faq-open'));
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 7000, theme: 'light', run: simple() },
  compare: { url: BASE + '/compare', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => cmpSearch(p, S, 'search'));
    await S.full();
  } },
  'compare-shopify': { url: BASE + '/compare/fourthwall-vs-shopify', wait: 7000, theme: 'light', run: simple() },
  shops: { url: BASE + '/shops', wait: 7000, theme: 'light', run: simple() },
  'get-inspired': { url: BASE + '/get-inspired', wait: 7000, theme: 'light', run: simple() },
  features: { url: BASE + '/features', wait: 7000, theme: 'light', run: simple() },
  memberships: { url: BASE + '/memberships', wait: 7000, theme: 'light', run: simple() },
  contact: { url: BASE + '/contact', wait: 7000, theme: 'light', run: simple() },
  signup: { url: SIGNUP_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    // /get-started 302s to auth.fourthwall.com with session/query signing
    // parameters: the sidecar records the clean entry URL, never the real one.
    await S.view('default');
  } },
  catalog: { url: PRODUCTS + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => catalogSearch(p, S, 'search'));
    await step('quiz', () => quizPick(p, S, 'quiz-answer'));
    await S.full();
  } },
  'catalog-pdp': { url: PDP_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('print-type', () => printType(p, S, 'embroidered'));
    await step('size-guide', () => sizeGuide(p, S, 'size-guide'));
    await S.full();
  } },
  'catalog-all': { url: ALL_URL, wait: 9000, theme: 'light', run: simple() },
  docs: { url: DOCS + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => docsSearch(p, S, 'search'));
    await step('theme-menu', () => docsThemeMenu(p, S, 'theme-menu'));
    await S.full();
  } },
  'docs-quickstart': { url: DOCS + '/quickstart', wait: 8000, theme: 'light', run: simple() },
  'docs-dark': { url: DOCS + '/quickstart', wait: 8000, theme: 'dark', run: async (p, S) => {
    if (!(await docsDarkOn(p))) { log('  ! docs dark toggle unavailable'); return; }
    await S.view('default');
    await S.full();
  } },
  help: { url: HELP + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => helpSearch(p, S, 'search'));
    await S.full();
  } },
  'help-category': { url: HELP + '/category/setting-up-your-shop', wait: 8000, theme: 'light', run: simple() },
  'help-dark': { url: HELP + '/category/setting-up-your-shop', wait: 8000, theme: 'dark', run: async (p, S) => {
    if (!(await helpDark(p, true))) { log('  ! help dark toggle unavailable'); return; }
    await S.view('default');
    await S.full();
    await helpDark(p, false);
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: simple() },
  pricing: { url: BASE + '/pricing', wait: 7000, theme: 'light', run: simple() },
  catalog: { url: PRODUCTS + '/', wait: 9000, theme: 'light', run: simple() },
  help: { url: HELP + '/category/setting-up-your-shop', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The Docusaurus mobile menu button opens the sidebar drawer — a local
      // UI toggle; its links are never followed.
      const t = p.locator('.navbar__toggle, button[aria-label*="menu" i], button[aria-label*="avigation" i]').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1000);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
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
