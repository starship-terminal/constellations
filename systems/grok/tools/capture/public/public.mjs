// Captures docs.x.ai's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// docs.x.ai is the Grok product family's docs portal — the only public
// Grok surface the capture host can reach: grok.com sits behind a
// Cloudflare managed challenge that never clears, and x.ai,
// console.x.ai, status.x.ai and accounts.x.ai answer a Cloudflare 403
// block page (2026-11-16, recorded as boundaries in the package README).
// The site paints `light` by default (html.light); its header carries a
// real "Switch to dark theme" button — dark shots are painted via that
// toggle, verified by the painted surface before each shot (setTheme in
// lib.mjs), then switched back. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is
// saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the
// boundary. Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the Ctrl+K search dialog, the header's product
// switcher and "More links" menus, the theme button, the sidebar's
// collapsible groups and the phone's "Open navigation menu" button.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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

// docs.x.ai never scrolls the document: the shell is viewport-high and the
// article scrolls inside its own overflow-y-auto pane (the sidebar has one of
// its own). findScroller() picks the pane with the most scrollable content —
// the article. lazyScroll walks it so lazy sections paint before the shot.
async function findScroller(p) {
  return p.evaluate(() => {
    let sc = null, best = 0;
    for (const el of document.querySelectorAll('div,main,section')) {
      const cs = getComputedStyle(el);
      if ((cs.overflowY === 'auto' || cs.overflowY === 'scroll') && el.scrollHeight > el.clientHeight + 50 && el.clientHeight > 300 && el.scrollHeight > best) { best = el.scrollHeight; sc = el; }
    }
    if (sc) sc.setAttribute('data-fp-scroller', '1');
    return sc ? { h: sc.scrollHeight, inner: true } : { h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight), inner: false };
  });
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
// restore() puts the shell back so later shots see the real layout.
async function expandScroller(p) {
  return p.evaluate(() => {
    const sc = document.querySelector('[data-fp-scroller]');
    if (!sc) return null;
    for (let el = sc; el && el !== document.documentElement; el = el.parentElement) {
      el.setAttribute('data-fp-expand', '1');
      for (const prop of ['height', 'max-height', 'min-height']) el.style.setProperty(prop, 'auto', 'important');
      el.style.setProperty('overflow', 'visible', 'important');
      el.style.setProperty('flex', 'none', 'important');
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
      for (const prop of ['height', 'max-height', 'min-height', 'overflow', 'flex']) el.style.removeProperty(prop);
      el.removeAttribute('data-fp-expand');
    }
    const sc = document.querySelector('[data-fp-scroller]');
    if (sc) { sc.removeAttribute('data-fp-scroller'); sc.scrollTop = 0; }
  });
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await expandScroller(p);
    await wait(p, 1200);
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.pause())).catch(() => {});
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css', timeout: 120000 });
    try {
      try {
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, this.requested);
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
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

// The Ctrl+K docs-search dialog (cmdk): a local UI surface the page's own
// shortcut opens. Shot open with its empty-state list, then closed with
// Escape. Nothing is typed or searched.
async function searchDialog(p, S) {
  await p.keyboard.press('Control+k');
  await wait(p, 1500);
  const open = await p.locator('[cmdk-root], [role="dialog"] .docs-search-modal, .docs-search-modal').first().isVisible().catch(() => false);
  if (!open) { log('  ! search dialog did not open'); return; }
  await S.view('search');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The header's product switcher: the "Open API sections" / product button
// opens a Radix menu of the five docs sections. A local UI toggle; the menu's
// links are never followed.
async function sectionsMenu(p, S) {
  const btn = p.locator('button').filter({ hasText: /API|Grok|Build|Subscription/ }).filter({ visible: true }).first();
  const alt = p.getByRole('button', { name: /open .*sections|sections/i }).first();
  const trigger = (await alt.count()) ? alt : btn;
  if (!(await trigger.count())) { log('  ! product switcher missing'); return; }
  await trigger.click({ timeout: 5000 }).catch(() => trigger.evaluate((el) => el.click()));
  await wait(p, 1200);
  const open = await p.locator('[role="menu"], [data-radix-popper-content-wrapper] [role="menu"]').first().isVisible().catch(() => false);
  if (!open) { log('  ! product menu did not open'); await p.keyboard.press('Escape'); return; }
  await S.view('sections');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// Dark shots of a page: switch through the site's own theme control (the
// painted check is inside setTheme), shoot, switch back. A page that never
// paints dark takes no shot: earlier evidence keeps its own date rather than
// being republished as fresh dark evidence.
async function darkPass(p, name, vw, vh, dpr, url, total, shots = ['default', 'full']) {
  if (!(await setTheme(p, 'dark'))) { log('  ! dark theme never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/overview', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('search', () => searchDialog(p, S));
    await step('sections', () => sectionsMenu(p, S));
    await S.full();
    ctx.extra += await darkPass(p, 'home', 1440, 900, 1, BASE + '/overview');
  } },
  quickstart: { url: BASE + '/developers/quickstart', wait: 6000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('nav-open', async () => {
      // A sidebar collapsible group: its own chevron button opens it — a
      // local UI toggle; the links inside are never followed.
      const grp = p.locator('button.peer\\/menu-button, button[class*="peer/menu-button"]').filter({ visible: true }).last();
      if (!(await grp.count())) { log('  ! sidebar group missing'); return; }
      await grp.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('nav-open');
    });
    await S.full();
    ctx.extra += await darkPass(p, 'quickstart', 1440, 900, 1, BASE + '/developers/quickstart', ['default']);
  } },
  models: { url: BASE + '/developers/models', wait: 6000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/developers/pricing', wait: 6000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'pricing', 1440, 900, 1, BASE + '/developers/pricing', ['default']);
  } },
  'release-notes': { url: BASE + '/developers/release-notes', wait: 6000, run: BOTH },
  'generate-text': { url: BASE + '/developers/model-capabilities/text/generate-text', wait: 6000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('tab', async () => {
      // An SDK language tab in a code sample: the tab's own activation —
      // a local UI toggle showing a different published snippet.
      const tab = p.locator('[role="tab"]').filter({ hasText: /Python/ }).filter({ visible: true }).first();
      if (!(await tab.count())) { log('  ! sdk tab missing'); return; }
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
      await S.view('tab-python');
    });
    await S.full();
    ctx.extra += await darkPass(p, 'generate-text', 1440, 900, 1, BASE + '/developers/model-capabilities/text/generate-text', ['default']);
  } },
  'api-reference': { url: BASE + '/developers/rest-api-reference/inference', wait: 6000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'api-reference', 1440, 900, 1, BASE + '/developers/rest-api-reference/inference', ['default']);
  } },
  faq: { url: BASE + '/developers/faq/general', wait: 6000, run: BOTH },
  cookbook: { url: BASE + '/cookbook', wait: 6000, run: BOTH },
  'rate-limits': { url: BASE + '/developers/rate-limits', wait: 6000, run: BOTH },
  'grok-home': { url: BASE + '/grok/overview', wait: 6000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'grok-home', 1440, 900, 1, BASE + '/grok/overview');
  } },
  'grok-faq': { url: BASE + '/grok/faq', wait: 6000, run: BOTH },
  'grok-user-guide': { url: BASE + '/grok/user-guide', wait: 6000, run: BOTH },
  'grok-bot': { url: BASE + '/grok-bot/overview', wait: 7000, run: BOTH },
  build: { url: BASE + '/build/overview', wait: 6000, run: BOTH },
  'x-subscription': { url: BASE + '/x-subscription/overview', wait: 6000, run: BOTH },
};

const mobile = {
  home: { url: BASE + '/overview', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Open navigation menu" button opens the phone's nav sheet — a
      // local UI toggle; its links are never followed.
      const ham = p.getByRole('button', { name: /open navigation menu|menu/i }).filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! hamburger missing'); return; }
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      const open = await p.locator('[role="dialog"], [data-state="open"], aside').first().isVisible().catch(() => false);
      if (!open) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  quickstart: { url: BASE + '/developers/quickstart', wait: 6000, run: BOTH },
  'grok-home': { url: BASE + '/grok/overview', wait: 6000, run: BOTH },
  pricing: { url: BASE + '/developers/pricing', wait: 6000, run: BOTH },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, spec.url);
  const runCtx = { extra: 0 };
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 8000);
    await spec.run(p, S, runCtx);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count + runCtx.extra;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
