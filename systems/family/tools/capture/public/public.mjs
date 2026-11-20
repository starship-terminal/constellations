// Captures family.co's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. family.co paints a
// single light theme signed out: the marketing home, /blog + /blog/<post>, /changelog, /support +
// /support/<article>, /faqs, /legal, /docs, /docs/connectkit and /docs/family-account, plus the
// public app.family.co login surface ("Aave Account", at rest). Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page truncates at 8
// chunks and the log records the boundary. Nothing is sent or signed into: the only presses are
// local UI toggles — the header's hover dropdowns, a "Watch the demo" video overlay and a blog
// filter. Log In, Get Started, Download on iOS, every Watch link and the login form are never
// followed or submitted. No consent overlay was seen.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots, as in the kit.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    // Detect a dominant inner scroller (a fixed-viewport div that scrolls the
    // page inside itself): document.scrollHeight then under-reports the real
    // page. family.co pages scroll the document, but keep the probe — it is
    // the boundary the kit records when a page tiles.
    const inner = await p.evaluate(() => {
      const doc = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
      let best = null;
      for (const e of document.querySelectorAll('body *')) {
        const cs = getComputedStyle(e);
        if (!/(auto|scroll)/.test(cs.overflowY)) continue;
        if (e.scrollHeight > Math.max(e.clientHeight + 200, doc + 200) && (!best || e.scrollHeight > best.h))
          best = { sel: null, h: e.scrollHeight, el: e };
      }
      if (!best) return null;
      best.el.setAttribute('data-capture-scroller', '1');
      return { h: best.h };
    });
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (inner) {
      const chunk = this.vh;
      const MAXH = 8 * chunk;
      const hCap = Math.min(inner.h, MAXH);
      if (inner.h > MAXH) log(`  ! ${name}: inner scroller is ${inner.h}px tall, capturing first ${hCap}px only (inner-scroller boundary)`);
      const scroller = p.locator('[data-capture-scroller="1"]').first();
      // wheel-scroll to lazy-load, then re-read the height and tile by scrollTop
      for (let y = 0; y < hCap; y += chunk) { await scroller.evaluate((e, y) => e.scrollTo(0, y), y).catch(() => {}); await wait(p, 200); }
      const H = await scroller.evaluate((e) => e.scrollHeight).catch(() => inner.h);
      const hReal = Math.min(H, MAXH);
      for (let i = 0, y = 0; y < hReal; i++, y += chunk) {
        await scroller.evaluate((e, y) => e.scrollTo(0, y), y);
        await wait(p, 350);
        // scrollTo clamps at the bottom: read the real offset and clip the
        // tile to the unshown remainder so stitching never repeats content.
        const top = await scroller.evaluate((e) => e.scrollTop).catch(() => y);
        const off = y - top;              // where the wanted region starts inside the viewport
        const vis = Math.min(chunk, Math.max(0, hReal - y));
        if (off < 0 || vis <= 0) break;
        try { await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, scale: 'css', clip: { x: 0, y: off, width: this.vw, height: vis } }, this.requested); }
        catch (e) { log('  ! part' + i, String(e.message).split('\n')[0]); }
      }
      await scroller.evaluate((e) => e.scrollTo(0, 0));
      this.count++; log('  shot', name, 'inner H=' + H);
      await wait(p, 400);
      return;
    }
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
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

// The header "Developers"/"Resources" links open their dropdown on hover — a
// local UI toggle, never a navigation.
async function openMenu(p, S, triggerText, name) {
  // `:visible` rather than filter({visible}): on the kit's Playwright 1.49 a
  // hidden responsive twin would otherwise win .first() (see measure.mjs).
  const t = p.locator('header a, header button').filter({ hasText: new RegExp('^\\s*' + triggerText + '\\s*$') }).and(p.locator(':visible')).first();
  if (!(await t.count())) { log('  no', triggerText, 'trigger'); return; }
  await t.hover();
  await wait(p, 900);
  await screenshotWithMetadata(p, { path: `${RAW}/${S.prefix}-${name}.png` }, S.requested);
  S.count++; log('  shot', name);
  await p.mouse.move(720, 500);
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-developers', () => openMenu(p, S, 'Developers', 'menu-developers'));
    await step('menu-resources', () => openMenu(p, S, 'Resources', 'menu-resources'));
    await step('demo', async () => {
      // "Watch the demo" mounts a full-viewport video overlay — a local UI
      // toggle. The video is left playing for a moment, then the overlay is
      // closed; nothing is downloaded or submitted.
      const t = p.locator('button').filter({ hasText: /Watch the demo/ }).and(p.locator(':visible')).first();
      if (!(await t.count())) { log('  no demo button'); return; }
      await t.scrollIntoViewIfNeeded();
      await wait(p, 400);
      await clickEl(t);
      await p.locator('[class*="WatchDemo__OverlayContainer"]').and(p.locator(':visible')).first().waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
      await wait(p, 1800);
      await S.view('demo');
      await p.keyboard.press('Escape');
      await wait(p, 500);
      // Escape may not close it: the overlay's own close control is the fallback.
      const x = p.locator('[class*="WatchDemo__OverlayContainer"] button, [class*="WatchDemo__OverlayContainer"] [class*="Close" i]').and(p.locator(':visible')).first();
      if (await x.count()) await x.evaluate((el) => el.click()).catch(() => {});
      await wait(p, 600);
    });
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'blog-post': { url: BASE + '/blog/why-family-accounts', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  changelog: { url: BASE + '/changelog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  support: { url: BASE + '/support', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'support-article': { url: BASE + '/support/import-a-wallet-from-metamask', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  faqs: { url: BASE + '/faqs', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  legal: { url: BASE + '/legal', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { url: BASE + '/docs', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-connectkit': { url: BASE + '/docs/connectkit', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-account': { url: BASE + '/docs/family-account', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: APP + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    // The app's public login surface ("Aave Account"), at rest: the
    // email/phone field is never filled here and the form is never
    // submitted — the measured pass does the focus/fill-then-clear reads.
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    // The full page first: the hamburger mounts a full-screen menu view that
    // replaces the document (docH collapses to the viewport), so the drawer
    // state is captured last.
    await S.full();
    await step('drawer', async () => {
      // The hamburger opens the mobile nav menu — a local UI toggle.
      const t = p.locator('button[class*="Nav__MenuButton"], header button').and(p.locator(':visible')).first();
      if (!(await t.count())) { log('  no menu button'); return; }
      await clickEl(t);
      await wait(p, 1200);
      await S.view('drawer');
    });
  } },
  support: { url: BASE + '/support', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: APP + '/', wait: 9000, theme: 'light', run: async (p, S) => {
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
