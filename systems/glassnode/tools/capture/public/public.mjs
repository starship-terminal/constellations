// Captures glassnode.com's signed-out public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// glassnode.com is five public stacks signed out. The marketing site
// (glassnode.com/...) paints the declared --light_*/--base_* token layer only
// — there is no global dark theme, only dark in-page sections — so every
// marketing shot is -light. studio.glassnode.com is the React product shell:
// /pricing, /charts/*, /dashboards/*, /market-compass, /get-listed and
// /contact are reachable signed out and paint light; a
// html[data-theme="dark-theme"] layer is declared but no public theme control
// exists, so it is captured as declared evidence only, never emulated into a
// screenshot. The studio "Log in" button navigates to the Auth0 universal
// login at auth.glassnode.com/u/login?state=...; the auth-login shot reaches
// it through that real click and records the sanitized origin+path (the
// volatile state parameter is never kept). research.glassnode.com is a Ghost
// publication with a real "Switch to dark mode" toggle, shot -light and
// theme-dark. docs.glassnode.com is a GitBook site whose "Switch to dark
// theme" button paints .dark on <html>; shot -light and theme-dark.
// tokenization.glassnode.com is a dark-by-default registry app with a real
// "Switch to light theme" button; shot -dark and theme-light. Nothing is
// sent, bought or signed into: the only presses are local UI toggles — the
// marketing Products dropdown trigger, the research/docs/tokenization theme
// controls and the phone's hamburger. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, launchBrowser, UA, UA_MOBILE, BASE, STUDIO_BASE, RESEARCH_BASE, DOCS_BASE, TOKENIZATION_BASE, LOGIN_URL } from './lib.mjs';

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
    // Pause autoplaying media so a full-page raster does not stall on a video.
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

// Whether the page paints dark right now: the computed background of the
// first painted surface — body, then <html>, then the first visible
// block-level container when both are transparent — is the ground truth, so
// a theme switch that never repaints can never publish a light page as dark
// evidence.
async function paintsDark(p) {
  return p.evaluate(() => {
    const read = (bg) => {
      const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(bg || '');
      if (!m || (m[4] !== undefined && +m[4] === 0)) return null;
      return (0.2126 * +m[1] + 0.7152 * +m[2] + 0.0722 * +m[3]) < 128;
    };
    for (const el of [document.body, document.documentElement]) {
      const v = read(getComputedStyle(el).backgroundColor);
      if (v !== null) return v;
    }
    for (const el of document.querySelectorAll('main, #__next, #app, [class*="app" i], body > div')) {
      const v = read(getComputedStyle(el).backgroundColor);
      if (v !== null) return v;
    }
    return null;
  }).catch(() => null);
}

// A click that survives overlay interception: pointer first, DOM click the
// fallback (used for theme controls sitting inside popovers).
async function clickToggle(loc) {
  await loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()));
}

// The marketing header's "Products" nav dropdown. The trigger is a plain
// header <button> whose aria-expanded flips: on this site a pointer hover
// already opens the panel and a click toggles it, so hover is tried first and
// click is the fallback. Its links are never followed.
async function navMenu(p, S, name) {
  const btn = p.locator('header button').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  // Hover opens the menu; a click toggles it — so try hover first (button,
  // then its wrapper, then a DOM mouseover), and only click while closed.
  for (let i = 0; i < 4 && !(await expanded()); i++) {
    await btn.hover({ timeout: 5000 }).catch(() => {});
    await wait(p, 900);
    if (await expanded()) break;
    await btn.evaluate((el) => { el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true })); const par = el.parentElement; if (par) par.dispatchEvent(new MouseEvent('mouseover', { bubbles: true })); }).catch(() => {});
    await wait(p, 900);
    if (await expanded()) break;
    await btn.click({ timeout: 5000 }).catch(() => {});
    await wait(p, 900);
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase().replace(/\s+/g, '-'));
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The Ghost research publication's theme toggle: .gh-theme-toggle buttons
// (aria-label "Switch to dark mode"/"Switch to light mode") repoint
// data-theme on <html> and repaint. Success is the painted theme, not the
// attribute alone.
async function researchTheme(p, want) {
  const wantDark = want === 'dark';
  if ((await paintsDark(p)) === wantDark) return true;
  const btn = p.locator(`button.gh-theme-toggle, button[aria-label*="Switch to ${want} mode" i]`).filter({ visible: true }).first();
  for (let i = 0; i < 3 && (await btn.count()); i++) {
    await clickToggle(btn);
    await wait(p, 1200);
    if ((await paintsDark(p)) === wantDark) return true;
  }
  return (await paintsDark(p)) === wantDark;
}

// The GitBook docs site's theme buttons: "Switch to light/dark theme" direct
// buttons that flip .light/.dark on <html> and repaint.
async function docsTheme(p, want) {
  const wantDark = want === 'dark';
  if ((await paintsDark(p)) === wantDark) return true;
  const btn = p.locator(`button[aria-label="Switch to ${want} theme"]`).first();
  for (let i = 0; i < 3 && (await btn.count()); i++) {
    await clickToggle(btn);
    await wait(p, 1200);
    if ((await paintsDark(p)) === wantDark) return true;
  }
  return (await paintsDark(p)) === wantDark;
}

// The tokenization registry's theme button ("Switch to light theme"/"Switch
// to dark theme") flips [data-theme] on <html> and repaints.
async function tokenTheme(p, want) {
  const wantDark = want === 'dark';
  // The registry's body is transparent — the attribute flip is corroborating
  // evidence, the painted-surface check is still what gates the shot.
  const attrSays = async () => p.evaluate((d) => (document.documentElement.getAttribute('data-theme') || '').toLowerCase() === (d ? 'dark' : 'light'), wantDark).catch(() => false);
  const is = async () => (await paintsDark(p)) === wantDark || ((await paintsDark(p)) === null && (await attrSays()));
  if (await is()) return true;
  const btn = p.locator(`button[aria-label="Switch to ${want} theme"]`).filter({ visible: true }).first();
  for (let i = 0; i < 3 && (await btn.count()); i++) {
    await clickToggle(btn);
    await wait(p, 1500);
    if (await is()) return true;
  }
  return await is();
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-products', () => navMenu(p, S, 'Products'));
    await S.full();
  } },
  'products-studio': { url: BASE + '/products/studio', wait: 8000, theme: 'light', run: BOTH },
  'products-data': { url: BASE + '/products/data', wait: 8000, theme: 'light', run: BOTH },
  'products-research': { url: BASE + '/products/research', wait: 8000, theme: 'light', run: BOTH },
  'products-market-compass': { url: BASE + '/products/studio/market-compass', wait: 8000, theme: 'light', run: BOTH },
  'products-alpha-lab': { url: BASE + '/products/studio/alpha-lab', wait: 8000, theme: 'light', run: BOTH },
  'pricing-vector': { url: BASE + '/pricing/vector', wait: 8000, theme: 'light', run: BOTH },
  about: { url: BASE + '/about', wait: 8000, theme: 'light', run: BOTH },
  contact: { url: BASE + '/contact', wait: 8000, theme: 'light', run: BOTH },
  'customer-stories': { url: BASE + '/customer-stories', wait: 8000, theme: 'light', run: BOTH },
  events: { url: BASE + '/events', wait: 8000, theme: 'light', run: BOTH },
  'solutions-trading': { url: BASE + '/solutions/trading-and-investing', wait: 8000, theme: 'light', run: BOTH },
  'solutions-content': { url: BASE + '/solutions/crypto-content-creation', wait: 8000, theme: 'light', run: BOTH },
  'studio-pricing': { url: STUDIO_BASE + '/pricing', wait: 14000, theme: 'light', run: BOTH },
  'studio-charts': { url: STUDIO_BASE + '/charts', wait: 16000, theme: 'light', run: async (p, S) => { await S.view('default'); } },
  'studio-dashboards': { url: STUDIO_BASE + '/dashboards', wait: 16000, theme: 'light', run: async (p, S) => { await S.view('default'); } },
  'studio-market-compass': { url: STUDIO_BASE + '/market-compass', wait: 14000, theme: 'light', run: BOTH },
  'studio-get-listed': { url: STUDIO_BASE + '/get-listed', wait: 14000, theme: 'light', run: BOTH },
  'studio-contact': { url: STUDIO_BASE + '/contact', wait: 14000, theme: 'light', run: BOTH },
  // The Auth0 universal-login card, reached the way a visitor reaches it: the
  // studio shell's own "Log in" button. The landing URL carries a volatile
  // ?state= signed per attempt; the sidecar records the sanitized
  // origin+path (LOGIN_URL) instead. Credentials are never entered.
  'auth-login': { url: STUDIO_BASE + '/', wait: 12000, theme: 'light', run: async (p, S) => {
    const btn = p.locator('button, a').filter({ hasText: /^Log ?in$/i }).filter({ visible: true }).first();
    if (!(await btn.count())) { log('  ! auth-login: no Log in control on the studio shell'); return; }
    S.requested.sanitizedSourceUrl = LOGIN_URL;
    await Promise.all([p.waitForURL(/auth\.glassnode\.com\/u\/login/, { timeout: 45000 }).catch(() => {}), btn.click({ timeout: 8000 }).catch(() => {})]);
    await wait(p, 7000);
    if (!/auth\.glassnode\.com/.test(p.url())) { log('  ! auth-login: did not reach the auth origin'); return; }
    await S.view('default');
    await S.full();
  } },
  'research-home': { url: RESEARCH_BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('research dark', async () => {
      // theme-dark is a state name on the same -light page prefix: the
      // Ghost toggle paints a real dark surface. A page that never paints
      // dark takes no shot — earlier evidence stays under its own date.
      if (await researchTheme(p, 'dark')) { await S.view('theme-dark'); await researchTheme(p, 'light'); }
      else log('  ! research dark: page never painted a dark theme; theme-dark shot skipped, earlier evidence untouched');
    });
  } },
  // The first article in the research index (the current Week Onchain issue);
  // the sidecar records the sanitized article URL.
  'research-article': { url: RESEARCH_BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    const href = await p.evaluate(() => (document.querySelector('article a, .post-card a, h2 a, h3 a') || {}).href || null);
    if (!href) { log('  ! research-article: no article link on the index'); return; }
    S.requested.sanitizedSourceUrl = href.replace(/\?.*$/, '');
    await p.goto(href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 7000);
    await S.view('default');
    await S.full();
  } },
  'docs-home': { url: DOCS_BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('docs dark', async () => {
      if (await docsTheme(p, 'dark')) { await S.view('theme-dark'); await docsTheme(p, 'light'); }
      else log('  ! docs dark: page never painted a dark theme; theme-dark shot skipped, earlier evidence untouched');
    });
  } },
  'docs-metric': { url: DOCS_BASE + '/data/metric-catalog', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('docs dark', async () => {
      if (await docsTheme(p, 'dark')) { await S.view('theme-dark'); await docsTheme(p, 'light'); }
      else log('  ! docs dark: page never painted a dark theme; theme-dark shot skipped, earlier evidence untouched');
    });
  } },
  // The registry defaults to dark ([data-theme="dark"]); the -dark shots are
  // the painted default, theme-light is the toggled state.
  tokenization: { url: TOKENIZATION_BASE + '/', wait: 10000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('tokenization light', async () => {
      if (await tokenTheme(p, 'light')) { await S.view('theme-light'); await tokenTheme(p, 'dark'); }
      else log('  ! tokenization light: page never painted a light theme; theme-light shot skipped, earlier evidence untouched');
    });
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The hamburger button toggles the phone nav — a local UI toggle; its
      // links are never followed.
      const ham = p.locator('header button[class*="hamburger" i], header button').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      const open = async () => (await ham.getAttribute('aria-expanded').catch(() => null)) === 'true';
      for (let i = 0; i < 3 && !(await open()); i++) {
        await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
        await wait(p, 1200);
        if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 1200); }
      }
      if (!(await open())) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  'studio-pricing': { url: STUDIO_BASE + '/pricing', wait: 14000, theme: 'light', run: BOTH },
  'research-home': { url: RESEARCH_BASE + '/', wait: 9000, theme: 'light', run: BOTH },
  'docs-home': { url: DOCS_BASE + '/', wait: 9000, theme: 'light', run: BOTH },
  tokenization: { url: TOKENIZATION_BASE + '/', wait: 10000, theme: 'dark', run: BOTH },
};

const b = await launchBrowser();
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
