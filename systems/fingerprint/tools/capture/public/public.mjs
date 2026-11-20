// Captures fingerprint.com's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// marketing page on fingerprint.com paints the light FPDS/Tailwind token layer —
// the `dark:` utility rules Tailwind ships are vestigial, so every marketing shot
// is -light. docs.fingerprint.com is a Mintlify site with a real theme toggle;
// its pages are shot -light and -dark (the theme switched by the docs' own
// preference control, a local UI toggle). dashboard.fingerprint.com /login and
// /signup are the product shell's only signed-out surfaces, shot -light at rest,
// never submitted. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png
// tiles, which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the header's Product/Use
// Cases/Resources dropdown triggers, the phone's "Mobile Menu" button and the
// docs' theme toggle. The /demo page is the product's own public demo surface; it
// is shot at rest (its signal panel can show this machine's IP and rough
// location, so shots of it are masked before quantize).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, DOCS_BASE, LOGIN_URL, SIGNUP_URL } from './lib.mjs';

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
    // Pages whose demos autoplay video/canvas (figjam, dev-mode, design-systems)
    // can stall a full-page raster past the default 30s; pausing media and
    // allowing 120s keeps the shot on heavy pages.
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

// Opens one of the header's nav-dropdown menus ("Product"/"Use Cases"/
// "Resources" — plain <button> triggers whose aria-expanded flips; the panels
// mount beside them). A pointer click flips aria-expanded; keyboard Enter is
// the fallback. Their links are never followed.
async function navMenu(p, S, name) {
  const btn = p.locator('header button').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await btn.click({ timeout: 5000 }).catch(() => {});
    await wait(p, 700);
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 700); }
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase().replace(/\s+/g, '-'));
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The docs site's theme toggle. The Mintlify article pages carry a
// "Change theme preference" menu trigger (aria-haspopup="menu") whose
// Light/Dark/System items repoint data-theme-preference AND repaint the
// page (the html class flips light/dark and color-scheme follows); the
// docs landing page carries a plain "Toggle dark mode" button that adds
// .dark to <html> and repaints the body instead. Success is the painted
// theme, not the attribute alone: a dark shot is saved only when the page
// itself reports dark (dark class, dark color-scheme, or a dark-painted
// body), so a switch that never repaints can never publish a light page
// as dark evidence. Switched once for the dark shots, then switched back
// — a local UI preference toggle.
async function docsTheme(p, want) {
  const painted = () => p.evaluate(() => {
    const bg = getComputedStyle(document.body).backgroundColor;
    const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(bg || '');
    const bodyDark = m && !(m[4] !== undefined && +m[4] === 0)
      ? (0.2126 * +m[1] + 0.7152 * +m[2] + 0.0722 * +m[3]) < 128 : null;
    return {
      pref: document.documentElement.getAttribute('data-theme-preference'),
      dark: document.documentElement.classList.contains('dark'),
      light: document.documentElement.classList.contains('light'),
      scheme: getComputedStyle(document.documentElement).colorScheme,
      bodyDark,
    };
  }).catch(() => ({}));
  const reached = async () => {
    const s = await painted();
    return want === 'dark'
      ? (s.dark || s.scheme === 'dark' || s.bodyDark === true) && s.light !== true
      : !s.dark && s.scheme !== 'dark' && s.bodyDark !== true;
  };
  if (await reached()) return true;
  const trigger = p.locator('button#theme-preference-menu-trigger, button[aria-label*="theme preference" i], button[aria-label*="dark mode" i], button[aria-label*="theme" i], button[aria-label*="color mode" i]').filter({ visible: true }).first();
  const item = () => p.locator('[role="menuitem"], [role="option"]').filter({ hasText: new RegExp(`switch to ${want} theme|^${want}$`, 'i') }).filter({ visible: true }).first();
  if (await trigger.count()) {
    for (let i = 0; i < 3; i++) {
      await trigger.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 700);
      // A menu trigger opens Light/Dark/System items; a direct toggle has
      // already flipped the theme by the time no menu appears.
      if (await item().count()) await item().click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      if (await reached()) return true;
      await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 300);
    }
  }
  // Fallback: persist the preference the way the site's own control does —
  // the localStorage choice plus the data-theme-preference attribute — and
  // reload so the site's own boot script applies it. Verification still
  // checks the painted state, never the values we just set; a page that
  // cannot be forced dark returns false and the caller skips the shot
  // rather than publishing a light page as dark evidence.
  await p.evaluate((w) => {
    try { localStorage.setItem('theme', w); localStorage.setItem('isDarkMode', w); } catch {}
    document.documentElement.setAttribute('data-theme-preference', w);
  }, want);
  await p.reload({ waitUntil: 'domcontentloaded' }).catch(() => {});
  await wait(p, 6000);
  return await reached();
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-product', () => navMenu(p, S, 'Product'));
    await step('menu-use-cases', () => navMenu(p, S, 'Use Cases'));
    await step('menu-resources', () => navMenu(p, S, 'Resources'));
    await S.full();
  } },
  identification: { url: BASE + '/products/identification/', wait: 8000, theme: 'light', run: BOTH },
  'smart-signals': { url: BASE + '/products/smart-signals/', wait: 8000, theme: 'light', run: BOTH },
  'ai-agent-detection': { url: BASE + '/products/ai-agent-detection/', wait: 8000, theme: 'light', run: BOTH },
  'use-case': { url: BASE + '/use-cases/payment-fraud/', wait: 8000, theme: 'light', run: BOTH },
  ai: { url: BASE + '/ai/', wait: 8000, theme: 'light', run: BOTH },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: BOTH },
  demo: { url: BASE + '/demo/', wait: 10000, theme: 'light', run: BOTH },
  'contact-sales': { url: BASE + '/contact-sales/', wait: 8000, theme: 'light', run: BOTH },
  blog: { url: BASE + '/blog/', wait: 8000, theme: 'light', run: BOTH },
  'case-studies': { url: BASE + '/case-studies/', wait: 8000, theme: 'light', run: BOTH },
  resources: { url: BASE + '/resources/', wait: 8000, theme: 'light', run: BOTH },
  security: { url: BASE + '/security/', wait: 8000, theme: 'light', run: BOTH },
  integrations: { url: BASE + '/integrations/', wait: 8000, theme: 'light', run: BOTH },
  'sdk-libraries': { url: BASE + '/sdk-libraries/', wait: 8000, theme: 'light', run: BOTH },
  'bot-directory': { url: BASE + '/bot-directory/', wait: 8000, theme: 'light', run: BOTH },
  'about-us': { url: BASE + '/about-us/', wait: 8000, theme: 'light', run: BOTH },
  careers: { url: BASE + '/careers/', wait: 8000, theme: 'light', run: BOTH },
  'docs-home': { url: DOCS_BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('docs dark', async () => {
      // The shot keeps the -light page prefix and takes the state name
      // 'theme-dark': the docs' own dark preference paints a real dark
      // surface on the same page, and the name records that it is a state,
      // not a second page load. A page that never paints dark takes no
      // shot: an earlier capture keeps its own date rather than being
      // republished as fresh evidence.
      if (await docsTheme(p, 'dark')) { await S.view('theme-dark'); await docsTheme(p, 'light'); }
      else log('  ! docs dark: page never painted a dark theme; theme-dark shot skipped, earlier evidence untouched');
    });
  } },
  'docs-quickstart': { url: DOCS_BASE + '/docs/quick-start-guide', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('docs dark', async () => {
      if (await docsTheme(p, 'dark')) { await S.view('theme-dark'); await docsTheme(p, 'light'); }
      else log('  ! docs dark: page never painted a dark theme; theme-dark shot skipped, earlier evidence untouched');
    });
  } },
  'docs-signals': { url: DOCS_BASE + '/docs/smart-signals-introduction', wait: 8000, theme: 'light', run: BOTH },
  login: { url: LOGIN_URL, wait: 9000, theme: 'light', run: BOTH },
  signup: { url: SIGNUP_URL, wait: 9000, theme: 'light', run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Mobile Menu" button toggles the phone nav — a local UI toggle;
      // its links are never followed.
      const ham = p.locator('button').filter({ hasText: /^Mobile Menu$/ }).filter({ visible: true }).first();
      if (!(await ham.count())) return;
      const open = async () => (await ham.getAttribute('aria-expanded').catch(() => null)) === 'true';
      if (!(await open())) await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 1500); }
      if (!(await open())) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: BOTH },
  demo: { url: BASE + '/demo/', wait: 9000, theme: 'light', run: BOTH },
  'contact-sales': { url: BASE + '/contact-sales/', wait: 8000, theme: 'light', run: BOTH },
  'docs-quickstart': { url: DOCS_BASE + '/docs/quick-start-guide', wait: 8000, theme: 'light', run: BOTH },
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
