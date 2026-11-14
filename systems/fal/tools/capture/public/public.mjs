// Captures fal.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. fal.ai paints
// three surfaces signed out: the single-theme Webflow marketing pages (/, /pricing/,
// /serverless/, /contact-sales/) labelled `light`, the Next.js app (/explore, /models/*,
// /login, the 404) which follows prefers-color-scheme — `light` shots run in a light
// context, `dark` shots in a dark one — and the fumadocs /docs/* surface, whose
// theme is set explicitly through its own switcher button (a local display
// toggle) and verified on <html> before any shot, so `docs-dark` is really dark. Desktop shots are 1440x900 at
// 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought, downloaded or signed into: the only presses are local UI toggles —
// a nav menu trigger, the mobile drawer, the docs theme switcher — never a
// Get-Started, Contact-Sales, Sign-up, Log-in, OAuth, "Sign in to run" or
// "Open in Sandbox" action. The .dg-consent-banner cookie card is hidden, never
// answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
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

// Puts the docs on an explicit theme with the page's own switcher (a local
// display toggle): the "Switch to <theme> theme" button, then waits for the
// <html> class and the painted colour scheme to follow. Throws when the page
// never reaches the requested theme, so a light capture can no longer be
// filed as dark.
async function docsTheme(p, want) {
  const btn = p.locator(`button[aria-label="Switch to ${want} theme"]`).filter({ visible: true }).first();
  if (!(await btn.count())) throw new Error(`docs: no "Switch to ${want} theme" control`);
  await clickEl(btn);
  const ok = await p.waitForFunction((w) => {
    const root = document.documentElement;
    return root.classList.contains(w) && !root.classList.contains(w === 'dark' ? 'light' : 'dark')
      && getComputedStyle(root).colorScheme === w;
  }, want, { timeout: 8000 }).then(() => true).catch(() => false);
  if (!ok) throw new Error(`docs: page did not become ${want} after the theme switch`);
  await wait(p, 900);
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  serverless: { url: BASE + '/serverless', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact-sales', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  explore: { url: BASE + '/explore', wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'explore-light': { url: BASE + '/explore', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  model: { url: BASE + '/models/krea/v3/text-to-image', wait: 10000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'model-light': { url: BASE + '/models/krea/v3/text-to-image', wait: 10000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  api: { url: BASE + '/models/krea/v3/text-to-image/api', wait: 10000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: BASE + '/login', wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  'login-light': { url: BASE + '/login', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  notfound: { url: BASE + '/this-page-does-not-exist', wait: 8000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  docs: { url: BASE + '/docs/documentation', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-dark': { url: BASE + '/docs/documentation', wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await docsTheme(p, 'dark');
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', scheme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  explore: { url: BASE + '/explore', wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The phone header carries a menu toggle (button or control with a
      // menu/burger affordance): open it as its own local toggle.
      const ham = p.locator('button[aria-label*="menu" i], button[aria-label*="navigation" i], [class*="burger" i], [class*="hamburger" i]').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 1400);
      await S.view('drawer');
      await p.keyboard.press('Escape');
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
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: spec.scheme || 'light' });
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
