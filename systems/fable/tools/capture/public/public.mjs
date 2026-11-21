// Captures fable.co's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every fable.co page
// paints one light marketing/catalog surface: cream and white pages with scoped dark surfaces —
// the forest-green hero/promo/masthead bands, the black footer — except /discover, a whole-page
// dark cover-wall app. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary. Nothing is
// sent, bought, joined or signed into: the only presses are local UI toggles — the /clubs
// "Search thousands of book and TV clubs" dialog trigger (aria-haspopup="dialog"), the book
// page's "May contain spoilers!" disclosure and the mobile "Open menu" button.
// The /signin and /signup forms are measured and shot at rest, never submitted; "Get the app",
// "Want to read", "Download the app to join", "Shop 1M+ ebooks…", "Start a club" and every store
// or join action are left at rest. The Osano consent banner is hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, BOOK_URL, CLUB_URL } from './lib.mjs';

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
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 300); }
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
    const v = p.viewportSize();
    if (hCap <= chunk) {
      // A fullPage shot renders the whole document with the scroll position
      // back at zero, so sections revealed by IntersectionObserver or an
      // in-view animation stay at their pre-reveal styles (the marketing
      // page's feature bands captured as empty colour). Grow the viewport
      // to the document instead — every section is then inside the rendered
      // frame — let the reveals settle, and shoot that.
      //
      // The tall viewport inflates every vh unit first (a 10vh margin is
      // 600px, not 90px, and pushes real bands apart), so before expanding,
      // record the computed geometry of every element styled with vh and
      // pin those declarations back to their real-viewport px values.
      await p.evaluate(() => {
        const geo = ['width', 'minWidth', 'maxWidth', 'height', 'minHeight', 'maxHeight',
                     'marginTop', 'marginBottom', 'marginLeft', 'marginRight',
                     'paddingTop', 'paddingBottom', 'paddingLeft', 'paddingRight',
                     'top', 'bottom', 'left', 'right',
                     'blockSize', 'minBlockSize', 'maxBlockSize', 'inlineSize',
                     'marginBlockStart', 'marginBlockEnd', 'paddingBlockStart', 'paddingBlockEnd',
                     'insetBlockStart', 'insetBlockEnd'];
        const VUNIT = /\d[a-z]{0,2}vh|\d[a-z]{0,2}vb/;
        const targets = new Set();
        const walk = (rs) => {
          for (const r of rs) {
            // CSSStyleRule.cssRules exists in Chrome for nesting — an empty
            // truthy list — so guard on the type, not the property.
            if (r.cssRules && !(r instanceof CSSStyleRule)) { walk(r.cssRules); continue; }
            if (!r.style || !r.selectorText) continue;
            if (geo.some((pr) => VUNIT.test(r.style[pr] || ''))) targets.add(r.selectorText);
          }
        };
        for (const sh of document.styleSheets) { try { walk(sh.cssRules); } catch { /* cross-origin */ } }
        window.__vhPin = [];
        for (const sel of targets) {
          let els; try { els = document.querySelectorAll(sel); } catch { continue; }
          for (const el of els) {
            const cs = getComputedStyle(el);
            const vals = {};
            for (const pr of geo) vals[pr] = cs[pr];
            window.__vhPin.push({ el, vals });
          }
        }
      });
      await p.setViewportSize({ width: this.vw, height: Math.max(hCap, v.height) });
      await wait(p, 2600);
      await p.evaluate(() => {
        for (const rec of window.__vhPin || []) {
          const cs = getComputedStyle(rec.el);
          for (const [pr, val] of Object.entries(rec.vals)) if (cs[pr] !== val) rec.el.style[pr] = val;
        }
      });
      await wait(p, 600);
      await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
      await p.setViewportSize(v);
    } else {
      // Taller than one texture: walk real viewports so every tile's content
      // has actually entered the rendered frame, rather than clipping a
      // top-rendered fullPage shot where never-entered sections stay blank.
      await p.setViewportSize({ width: this.vw, height: chunk });
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await p.evaluate((y) => scrollTo(0, y), y);
        await wait(p, 1700);
        // scrollTo clamps to H - viewport, so the last tile's requested
        // start can be unreachable: clip from where the page actually
        // scrolled (the tile's page offset minus real scrollY), not from
        // the top of the viewport.
        const at = await p.evaluate(() => window.scrollY);
        await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), clip: { x: 0, y: y - at, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
      await p.evaluate(() => scrollTo(0, 0));
      await p.setViewportSize(v);
      await wait(p, 500);
    }
    this.count++; log('  shot', name, 'H=' + H);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens the /clubs search dialog: its trigger is an aria-haspopup="dialog"
// button — a local UI toggle, never a submit. Fires a click, then keyboard
// Enter as a fallback, and reports whether a dialog appeared.
async function searchDialog(p, S) {
  const btn = p.locator('button[aria-haspopup="dialog"]').filter({ hasText: /Search thousands/i }).first();
  if (!(await btn.count())) { log('  ! no search trigger'); return; }
  // Osano mounts its own role="dialog" nodes, so count only a visible,
  // non-consent dialog.
  const open = () => p.evaluate(() => !![...document.querySelectorAll('[role="dialog"]')].find((x) => !/osano/i.test(x.className) && x.getBoundingClientRect().width > 100));
  for (let i = 0; i < 3 && !(await open()); i++) {
    if (i === 0) await clickEl(btn).catch(() => {});
    else { await btn.focus(); await p.keyboard.press('Enter'); }
    await wait(p, 900);
  }
  if (!(await open())) { log('  ! search dialog did not open'); return; }
  await S.view('search');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// Opens the phone's off-canvas nav drawer: the hamburger is a div with
// aria-label="Open menu" (not a button), the drawer slides in from x=-390.
// A local UI toggle; Escape closes it again.
async function navDrawer(p, S) {
  const btn = p.locator('[aria-label="Open menu"]').first();
  try { await btn.waitFor({ timeout: 15000 }); } catch { log('  ! no menu trigger'); return; }
  await clickEl(btn).catch(() => {});
  await wait(p, 1200);
  const open = await p.evaluate(() => {
    const b = [...document.querySelectorAll('header button')].find((x) => x.innerText.trim() === 'Clubs');
    if (!b) return false;
    for (let n = b; n && n.tagName !== 'HEADER'; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 250 && r.left > -10) return true;
    }
    return false;
  });
  if (!open) { log('  ! nav drawer did not open'); return; }
  await S.view('nav');
  // The drawer's own X ("Close menu" / close aria-label) is the sure close;
  // Escape may not be wired to it.
  const closeBtn = p.locator('[aria-label="Close menu"], [aria-label*="Close" i]').filter({ visible: true }).first();
  if (await closeBtn.count()) await clickEl(closeBtn).catch(() => {});
  else await p.keyboard.press('Escape');
  await wait(p, 800);
}

// Opens the "May contain spoilers!" disclosure on the book page — a local UI
// toggle revealing pre-published content warning text; nothing is posted.
async function spoilers(p, S) {
  const btn = p.locator('button').filter({ hasText: /May contain spoilers/i }).first();
  if (!(await btn.count())) { log('  ! no spoilers disclosure'); return; }
  await btn.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' })).catch(() => {});
  await wait(p, 400);
  await clickEl(btn).catch(() => {});
  await wait(p, 900);
  await S.view('spoilers');
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  clubs: { url: BASE + '/clubs', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => searchDialog(p, S));
    await S.full();
  } },
  genre: { url: BASE + '/club/fantasy', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  club: { url: CLUB_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  books: { url: BASE + '/books', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  book: { url: BOOK_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('spoilers', () => spoilers(p, S));
    await S.full();
  } },
  discover: { url: BASE + '/discover', wait: 12000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  blog: { url: BASE + '/blog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blogpost: { url: BASE + '/blog/how-to-start-a-book-club', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  support: { url: BASE + '/support', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: BASE + '/signin', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: BASE + '/signup', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  guidelines: { url: BASE + '/community-guidelines', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  notfound: { url: BASE + '/book/this-book-does-not-exist', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    // The hamburger is a div with aria-label="Open menu"; clicking it slides
    // the full-screen nav sheet in from the left — a local UI toggle.
    await step('nav', () => navDrawer(p, S));
    await S.full();
  } },
  clubs: { url: BASE + '/clubs', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  book: { url: BOOK_URL, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  discover: { url: BASE + '/discover', wait: 12000, theme: 'dark', run: async (p, S) => {
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
