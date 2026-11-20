// Captures httpie.io's signed-out public pages into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix
// and the /app client shots an `app-` prefix. httpie.io boots html.dark —
// AUTO follows prefers-color-scheme and headless Chromium's light
// preference still resolves dark — so `dark` is the painted default and the
// footer's own ThemeToggle radio stack (LIGHT MODE / AUTO / DARK MODE) is
// pressed for the light pass (setTheme in lib.mjs verifies the repaint,
// never trusts the mechanism). Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary
// (the blog index is the long one). Nothing is sent, bought, typed,
// searched or signed into: the only presses are local UI toggles — the
// footer theme radios, the /app method and Incognito-space menus, and the
// request panel tabs. Send is never pressed: issuing a request is a
// network side effect, and the signed-out response surface is recorded as
// a boundary instead of fabricated.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, chromium, UA, UA_MOBILE, BASE, openApp, dismissAppPromo } from './lib.mjs';

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

// Marketing pages scroll the document; the docs pages and /app are
// viewport-high shells whose article/columns scroll inside their own
// overflow-y-auto panes. findScroller() picks the pane with the most
// scrollable content and falls back to the document. lazyScroll walks it
// so lazy sections paint before the shot.
async function findScroller(p) {
  // The docs article pane hydrates after domcontentloaded — a page that is
  // still exactly viewport-high may simply not have its inner scroller yet,
  // so retry a few times before falling back to the document.
  for (let tries = 0; tries < 10; tries++) {
    const info = await p.evaluate(() => {
      let sc = null, best = 0;
      for (const el of document.querySelectorAll('div,main,section,article')) {
        const cs = getComputedStyle(el);
        if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > best) { best = el.scrollHeight; sc = el; }
      }
      if (sc) sc.setAttribute('data-fp-scroller', '1');
      return {
        h: sc ? sc.scrollHeight : Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        inner: !!sc,
        docH: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        vh: window.innerHeight,
      };
    });
    if (info.inner || info.docH > info.vh + 50 || tries === 9) return info;
    await wait(p, 800);
  }
}

async function lazyScroll(p) {
  const info = await findScroller(p);
  if (info.inner) {
    for (let y = 0; y < info.h; y += 700) { await p.evaluate((y) => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = y; }, y); await wait(p, 180); }
    await p.evaluate(() => { const s = document.querySelector('[data-fp-scroller]'); if (s) s.scrollTop = 0; });
  } else {
    for (let y = 0; y < info.h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
    await p.evaluate(() => scrollTo(0, 0));
  }
  await wait(p, 900);
}

// For the full shot the article pane's ancestors are relaxed to natural
// height so the document itself becomes as tall as the article — a normal
// fullPage capture then paints every section, header still fixed at top.
// restoreShell() puts the shell back so later shots see the real layout.
async function expandScroller(p) {
  return p.evaluate(() => {
    const sc = document.querySelector('[data-fp-scroller]');
    if (!sc) return null;
    for (let el = sc; el && el !== document.documentElement; el = el.parentElement) {
      el.setAttribute('data-fp-expand', '1');
      // flex:none relaxes height but also drops the flex-basis width, letting
      // the pane grow wider than the viewport — pin the measured border-box
      // width so the full-page shot keeps the real layout.
      const w = el.getBoundingClientRect().width;
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
      el.style.setProperty('flex', 'none', 'important');
      el.style.setProperty('box-sizing', 'border-box', 'important');
      el.style.setProperty('width', `${w}px`, 'important');
    }
    for (const el of [document.body, document.documentElement]) {
      el.setAttribute('data-fp-expand', '1');
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
    }
    return true;
  });
}
async function restoreShell(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('[data-fp-expand]')) {
      for (const prop of ['height', 'max-height', 'min-height', 'overflow', 'flex', 'box-sizing', 'width']) el.style.removeProperty(prop);
      el.removeAttribute('data-fp-expand');
    }
    const sc = document.querySelector('[data-fp-scroller]');
    if (sc) { sc.removeAttribute('data-fp-scroller'); sc.scrollTop = 0; }
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full', maxChunks = 8) {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await expandScroller(p);
    await wait(p, 1200);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    // The bound is in CSS pixels: scale:'css' clips are CSS px and the
    // documented bound (three chunks = 42k px) describes page coverage —
    // dividing by dpr would halve mobile coverage. A @2x tile's PNG is
    // 28k device px tall; still well inside what the stitcher handles.
    const chunk = 14000;
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and
    // record the boundary instead. The docs manuals are ~96k px of inner
    // pane — three chunks of the top is the documented bound there.
    const MAXH = maxChunks * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    const plan = { intendedHeight: hCap, pageHeight: H, chunk, parts: hCap <= chunk ? 0 : Math.ceil(hCap / chunk), scale: 'css' };
    // Written before the tiles so quantize.py can prove the stitched set is
    // whole — a mid-loop failure must never publish a truncated sheet.
    fs.writeFileSync(`${f}.plan.json`, JSON.stringify(plan, null, 1) + '\n');
    const shootTiles = async (extra = {}) => {
      if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, ...extra }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, ...extra }, this.requested);
    };
    const dropPartials = () => {
      // A tile loop that dies mid-run leaves parts 0..k of n — the stitcher
      // would publish a truncated sheet as a full page. Remove every tile so
      // quantize.py has nothing partial to stitch.
      for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.plan.json`)) fs.unlinkSync(`${RAW}/${old}`);
    };
    try {
      try {
        await shootTiles();
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        dropPartials();
        try {
          await shootTiles({ animations: 'disabled' });
        } catch (e2) {
          dropPartials();
          throw e2;
        }
      }
    } finally {
      await restoreShell(p).catch(() => {});
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The footer's LIGHT MODE / AUTO / DARK MODE stack — a real control, shot
// with the footer scrolled into view (it lives at the page bottom).
async function themeToggleShot(p, S) {
  const found = await p.evaluate(() => {
    for (const w of document.querySelectorAll('[class*="ThemeToggle_wrapper"]')) {
      const r = w.getBoundingClientRect();
      if (r.width && r.height) { w.scrollIntoView({ block: 'center' }); return true; }
    }
    return false;
  });
  if (!found) { log('  ! theme toggle not on this page'); return; }
  await wait(p, 900);
  await S.view('theme-toggle');
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

// Light shots of a page that boots dark: the footer's own DARK->LIGHT
// radio press (painted check inside setTheme), shoot, switch back.
async function lightPass(p, name, vw, vh, dpr, url, shots = ['default', 'full']) {
  if (!(await setTheme(p, 'light'))) { log('  ! light theme never painted; light shots skipped'); return 0; }
  const Sl = new Shooter(p, `${name}-light`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sl.full(); else await Sl.view(s); }
  await setTheme(p, 'dark').catch(() => {});
  return Sl.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, darkDefault: true, run: async (p, S, ctx) => {
    await S.view('default');
    await step('theme-toggle', () => themeToggleShot(p, S));
    await S.full();
    ctx.extra += await lightPass(p, 'home', 1440, 900, 1, BASE + '/');
  } },
  'desktop-page': { url: BASE + '/desktop', wait: 7000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'desktop-page', 1440, 900, 1, BASE + '/desktop', ['default']);
  } },
  cli: { url: BASE + '/cli', wait: 7000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'cli', 1440, 900, 1, BASE + '/cli', ['default']);
  } },
  ai: { url: BASE + '/ai', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    ctx.extra += await lightPass(p, 'ai', 1440, 900, 1, BASE + '/ai', ['default']);
  } },
  docs: { url: BASE + '/docs', wait: 7000, run: BOTH },
  // The docs articles are ~96k px of inner pane — the full shot expands the
  // scroller and bounds at three chunks (42k px), a documented boundary.
  'docs-desktop': { url: BASE + '/docs/desktop', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full('full', 3);
    ctx.extra += await lightPass(p, 'docs-desktop', 1440, 900, 1, BASE + '/docs/desktop', ['default']);
  } },
  'docs-cli': { url: BASE + '/docs/cli', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full('full', 3);
  } },
  jobs: { url: BASE + '/jobs', wait: 7000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'jobs', 1440, 900, 1, BASE + '/jobs', ['default']);
  } },
  blog: { url: BASE + '/blog', wait: 8000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'blog', 1440, 900, 1, BASE + '/blog', ['default']);
  } },
  'blog-post': { url: BASE + '/blog/changelog-0027', wait: 7000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'blog-post', 1440, 900, 1, BASE + '/blog/changelog-0027', ['default']);
  } },
  download: { url: BASE + '/download', wait: 7000, run: async (p, S, ctx) => {
    await BOTH(p, S);
    ctx.extra += await lightPass(p, 'download', 1440, 900, 1, BASE + '/download', ['default']);
  } },
  about: { url: BASE + '/about', wait: 7000, run: BOTH },
  terms: { url: BASE + '/terms', wait: 6000, run: BOTH },
  privacy: { url: BASE + '/privacy', wait: 6000, run: BOTH },
  notfound: { url: BASE + '/pricing', wait: 6000, run: async (p, S) => {
    // /pricing 404s — captured as the product's not-found page (error state).
    await S.view('default'); await S.full();
  } },
};

// /app — HTTPie for Web, signed out ("Incognito space"). Every shot is a
// resting surface or a local UI toggle: the method menu, the request panel
// tabs, the environments manager, the space menu. Send is never pressed —
// issuing a request is a network side effect, so the Response tab is shot
// resting (empty state) and the used response surface is a documented
// boundary. Escape can close the draft request tab on some runs, so the
// request-dependent steps run first and ensureRequestTab() reopens the
// Drafts tab if the shell lost it.
const app = {
  app: { app: true, url: BASE + '/app', wait: 9000, run: async (p, S, ctx) => {
    const requestAlive = () => p.locator('button').filter({ hasText: /^GET$/ }).count();
    const ensureRequestTab = async () => {
      if (await requestAlive()) return true;
      // The draft tab was closed (Escape raced a menu) or displaced (the
      // environments manager is a tab): back to its card, else a fresh
      // draft through the strip's "+".
      const card = p.locator('[class*="TabCard_tab"]').filter({ hasText: /untitled|GET/i }).first();
      if (await card.count()) { await card.click({ timeout: 4000 }).catch(() => {}); await wait(p, 900); }
      if (await requestAlive()) return true;
      const add = p.locator('[class*="Tabs_addButton"], button[aria-label*="new" i]').first();
      if (await add.count()) { await add.click({ timeout: 4000 }).catch(() => {}); await wait(p, 900); }
      return !!(await requestAlive());
    };
    // The first-run "Introducing HTTPie AI" card mounts only on some loads:
    // shot when it renders, a documented boundary when it does not — never
    // a mislabeled default shot.
    await step('ai-promo', async () => {
      const card = p.locator('[class*="DialogContainer"], div, section').filter({ hasText: /introducing\s+httpie ai/i }).last();
      const box = await card.boundingBox().catch(() => null);
      // A dismissed card lingers in the DOM slid off-screen (negative y):
      // only an on-viewport card is promo evidence.
      if (!box || box.y + box.height <= 0) { log('  ! AI promo did not mount — boundary'); return; }
      await S.view('ai-promo');
      await dismissAppPromo(p);
    });
    await S.view('default');
    await step('method-menu', async () => {
      if (!(await ensureRequestTab())) { log('  ! method button missing'); return; }
      const get = p.locator('button').filter({ hasText: /^GET$/ }).first();
      await get.click({ timeout: 5000 }).catch(() => {});
      await wait(p, 1100);
      await S.view('method-menu');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    for (const tab of ['headers', 'auth', 'body']) {
      await step(`tab-${tab}`, async () => {
        if (!(await ensureRequestTab())) { log(`  ! ${tab} tab missing`); return; }
        const t = p.locator('button, [role="tab"]').filter({ hasText: new RegExp(`^${tab}$`, 'i') }).first();
        if (!(await t.count())) { log(`  ! ${tab} tab missing`); return; }
        await t.click({ timeout: 4000 }).catch(() => {});
        await wait(p, 800);
        await S.view(`tab-${tab}`);
      });
    }
    await step('back-to-params', async () => {
      const t = p.locator('button, [role="tab"]').filter({ hasText: /^params$/i }).first();
      if (await t.count()) await t.click({ timeout: 4000 }).catch(() => {});
    });
    // The Response panel resting: Send is never pressed, so its empty state
    // is the honest signed-out evidence for that surface.
    await step('tab-response', async () => {
      if (!(await ensureRequestTab())) { log('  ! response tab missing'); return; }
      const t = p.locator('button, [role="tab"]').filter({ hasText: /^response$/i }).first();
      if (!(await t.count())) { log('  ! response tab missing'); return; }
      await t.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('tab-response');
      const req = p.locator('button, [role="tab"]').filter({ hasText: /^request$/i }).first();
      if (await req.count()) await req.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 600);
    });
    await step('environments', async () => {
      const env = p.locator('button, [role="tab"]').filter({ hasText: /^environments$/i }).first();
      if (!(await env.count())) { log('  ! environments tab missing'); return; }
      await env.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1000);
      await S.view('environments');
      const set = p.locator('button, [role="tab"]').filter({ hasText: /^settings$/i }).first();
      if (await set.count()) { await set.click({ timeout: 4000 }).catch(() => {}); await wait(p, 800); await S.view('env-settings'); }
      // The environments manager is a tab in the strip: the way back to the
      // request is its own tab card, NOT the sidebar's "+ Collection" add
      // button (that opens the Create-collection dialog).
      const reqCard = p.locator('[class*="TabCard_tab"]').filter({ hasText: /untitled|GET/i }).first();
      if (await reqCard.count()) await reqCard.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 600);
    });
    // Shot last: the 'Incognito space' switcher is a real control — its own
    // press opens the current space's tab (the space's variables/settings
    // panel; signed out it holds Defaults only). No dropdown menu paints
    // for the unsigned product.
    await step('space-panel', async () => {
      const inc = p.locator('aside button[class*="Spaces_button"], button[class*="Spaces_button"], aside button').filter({ hasText: /incognito/i }).first();
      if (!(await inc.count())) { log('  ! incognito button missing'); return; }
      await inc.click({ timeout: 5000 }).catch(() => {});
      await wait(p, 1400);
      await S.view('space-panel');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    // Light pass over the resting app: the theme choice persists in
    // localStorage.theme (the footer control on a marketing page), so
    // setTheme detours through home and reloads /app painted light.
    await step('app-light', async () => {
      if (!(await setTheme(p, 'light'))) { log('  ! light never painted on /app'); return; }
      await dismissAppPromo(p);
      const Sl = new Shooter(p, 'app-light', 1440, 900, 1, BASE + '/app');
      await Sl.view('default');
      ctx.extra += Sl.count;
      await setTheme(p, 'dark').catch(() => {});
    });
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: BOTH },
  cli: { url: BASE + '/cli', wait: 7000, run: BOTH },
  blog: { url: BASE + '/blog', wait: 8000, run: BOTH },
  'docs-desktop': { url: BASE + '/docs/desktop', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full('full', 3);
  } },
  app: { app: true, url: BASE + '/app', wait: 9000, run: async (p, S) => {
    // The shell is viewport-high; there is no taller page to shoot, so no
    // -full exists for /app. The AI promo is shot only when it mounts.
    await step('ai-promo', async () => {
      const card = p.locator('[class*="DialogContainer"], div, section').filter({ hasText: /introducing\s+httpie ai/i }).last();
      const box = await card.boundingBox().catch(() => null);
      if (!box || box.y + box.height <= 0) { log('  ! AI promo did not mount — boundary'); return; }
      await S.view('ai-promo');
      await dismissAppPromo(p);
    });
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false, dict: desktop })), ...Object.keys(app).map((k) => ({ k, mob: false, dict: app })), ...Object.keys(mobile).map((k) => ({ k, mob: true, dict: mobile }))];
for (const { k, mob, dict } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = dict[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr, spec.url);
  const runCtx = { extra: 0 };
  try {
    if (spec.app) { if (!(await openApp(p, { wait: spec.wait, keepPromo: true }))) { log('  BLOCKED', spec.url); await ctx.close(); continue; } }
    else {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
      await wait(p, spec.wait || 8000);
    }
    await spec.run(p, S, runCtx);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count + runCtx.extra;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
