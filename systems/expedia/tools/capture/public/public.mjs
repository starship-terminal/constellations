// Captures Expedia's public pages into RAW (full-colour PNGs); quantize.py turns them into
// screenshots/.
//
//   PAGES=<dir of saved pages> RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs \
//     node public.mjs [page,page,...]
//
// www.expedia.com is behind a PerimeterX wall (HTTP 429 "Bot or Not?" on every route and mirror,
// headless and headed alike), so the pages can't be fetched live. What is captured instead:
// server-rendered page copies saved from the Wayback Machine under PAGES/, served by a local
// static server this script spins up, and painted with the LIVE *.travel-assets.com CSS/JS — the
// very files the real site serves. Interactions that need no network (opening the calendar, the
// room picker, the destination field) are driven on the hydrated render; the results list is shot
// on the JS-blocked render because hydration refetches (and empties) regions when the GraphQL API
// fails. Nothing is sent, created, signed into or booked.
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site ships one
// painted theme (light-1); dark-shaded regions (the marketing-3 hero) are always dark regardless.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { servePages, open, chromium, UA, UA_MOBILE } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const PAGES = process.env.PAGES || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'pages');
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
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const BASE = process.env.BASE_OVERRIDE; // set by the run loop below

// Opens one of the server-rendered uitk-menu dropdowns without JavaScript from
// the page: its checkbox carries aria-checked for the state the SSR intended,
// so flipping checked + the container's display paints the menu exactly as the
// site's own no-JS path would. Nothing is submitted; menus are local UI state.
async function openUitkMenu(p, ariaChecked = 'true') {
  return p.evaluate((want) => {
    for (const m of document.querySelectorAll('.uitk-menu')) {
      const cb = m.querySelector('input.uitk-menu-checkbox');
      if (!cb || cb.getAttribute('aria-checked') !== want) continue;
      cb.checked = true;
      const c = m.querySelector('.uitk-menu-container');
      if (c) c.style.display = 'block';
      return true;
    }
    return false;
  }, ariaChecked);
}
const closeUitkMenus = (p) => p.evaluate(() => {
  for (const m of document.querySelectorAll('.uitk-menu')) {
    const cb = m.querySelector('input.uitk-menu-checkbox');
    if (cb) cb.checked = false;
    const c = m.querySelector('.uitk-menu-container');
    if (c) c.style.removeProperty('display');
  }
});

const desktop = {
  // The JS-blocked render paints the full SSR page, including the header nav
  // hydration strips. Used for the resting shots and the no-JS menu states.
  home: { file: 'home.html', hydrate: false, wait: 6000, run: async (p, S) => {
    await S.view('default');
    await step('signin-open', async () => {
      // the Sign in menu's checkbox is server-marked aria-checked="true"
      if (!(await openUitkMenu(p, 'true'))) throw new Error('sign-in uitk-menu not found');
      await wait(p, 700);
      await S.view('signin-open');
      await closeUitkMenus(p); await wait(p, 400);
    });
    await step('shoptravel-open', async () => {
      // "Shop travel" is the other header menu (aria-checked="false" at rest)
      if (!(await openUitkMenu(p, 'false'))) throw new Error('shop-travel uitk-menu not found');
      await wait(p, 700);
      await S.view('shoptravel-open');
      await closeUitkMenus(p); await wait(p, 400);
    });
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
    await S.full();
  } },
  // The hydrated render runs the site's own JS: the search form's panels open
  // on click. The header does not re-render here (its data refetch fails), so
  // resting shots stay on the JS-blocked page above.
  'home-i': { file: 'home.html', hydrate: true, wait: 12000, run: async (p, S) => {
    // the search fields are button.uitk-form-field-trigger (the text inputs are
    // pointer-events:none — the button is the real control): 0 = Where to?,
    // 1 = Dates, 2 = Travelers. Each opens its own panel; Escape closes it.
    const triggers = p.locator('button.uitk-form-field-trigger');
    await step('calendar-open', async () => {
      await triggers.nth(1).click({ force: true });
      await wait(p, 3500);
      await S.view('calendar-open');
      await p.keyboard.press('Escape'); await wait(p, 800);
    });
    await step('travelers-open', async () => {
      await triggers.nth(2).click({ force: true });
      await wait(p, 2500);
      await S.view('travelers-open');
      await p.keyboard.press('Escape'); await wait(p, 800);
    });
    await step('whereto-open', async () => {
      await triggers.nth(0).click({ force: true });
      await wait(p, 2500);
      await S.view('whereto-open');
      await p.keyboard.press('Escape'); await wait(p, 800);
    });
    // product tab variant: the Flights form (Roundtrip/One-way/Multi-city).
    // A tab switch is local UI state; no search is submitted.
    await step('flights-tab', async () => {
      await p.locator('[role=tab]:has-text("Flights")').first().click({ force: true });
      await wait(p, 2500);
      await S.view('flights-tab');
    });
  } },
  // Hotel results: the SSR list paints only with JavaScript blocked —
  // hydration refetches the results API and empties the cards when it fails.
  search: { file: 'search.html', hydrate: false, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('sort-open', async () => {
      const s = p.locator('select, [data-stid*="sort"], button:has-text("Sort by")').first();
      await s.click().catch(() => {});
      await wait(p, 1200);
      await S.view('sort-open');
      await p.keyboard.press('Escape'); await wait(p, 500);
    });
  } },
};

const mobile = {
  home: { file: 'home.html', hydrate: false, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'home-i': { file: 'home.html', hydrate: true, wait: 12000, run: async (p, S) => {
    const triggers = p.locator('button.uitk-form-field-trigger');
    await step('calendar-open', async () => {
      await triggers.nth(1).click({ force: true });
      await wait(p, 3000);
      await S.view('calendar-open');
      await p.keyboard.press('Escape'); await wait(p, 800);
    });
  } },
  search: { file: 'search.html', hydrate: false, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const { srv, port } = await servePages(PAGES);
const base = `http://127.0.0.1:${port}`;
const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await open(p, `${base}/pages/${spec.file}`, { hydrate: spec.hydrate, wait: spec.wait });
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
srv.close();
