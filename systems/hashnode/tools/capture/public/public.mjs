// Captures hashnode.com's signed-out public pages into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix,
// blog-engine (townhall.hashnode.com) ones a `th-` prefix. hashnode.com
// paints html.light by default and repaints html.dark through the header's
// own Theme menu (Light / Dark / System — verified painted before each
// shot, then switched back). The blog engine repaints html.dark on
// prefers-color-scheme — its own "Toggle theme" button produced no repaint
// headless — so th- dark shots emulate the OS signal and reload
// (setBlogTheme in lib.mjs), never a script-applied class. Desktop shots
// are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8
// chunks and the log records the boundary (the home/feed streams are
// infinite). Nothing is sent, bought, typed, searched or signed into: the
// only presses are local UI toggles — the Ctrl+K search dialog, the header
// Theme menu, the More nav menu, FAQ accordions, changelog tabs, the
// sidebar toggle and the phone's "Open menu" button.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, setBlogTheme, chromium, UA, UA_MOBILE, BASE, BLOG } from './lib.mjs';

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

// hashnode.com never scrolls the document: the shell is viewport-high and
// the stage scrolls inside its own overflow-y-auto pane; the blog scrolls
// the document. findScroller() picks the pane with the most scrollable
// content and falls back to the document. lazyScroll walks it so lazy
// sections paint before the shot.
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

// The Ctrl+K search dialog: a local UI surface the page's own shortcut (and
// the header's "Search" button) opens. Shot open with its resting state,
// then closed with Escape. Nothing is typed or searched.
async function searchDialog(p, S, name = 'search') {
  const btn = p.locator('button').filter({ hasText: /search/i }).filter({ visible: true }).first();
  if (await btn.count()) await btn.click({ timeout: 4000 }).catch(() => p.keyboard.press('Control+k'));
  else await p.keyboard.press('Control+k');
  await wait(p, 1500);
  const open = await p.locator('[role="dialog"], [role="combobox"], [cmdk-root], [data-state="open"]').first().isVisible().catch(() => false);
  if (!open) { log('  ! search dialog did not open'); await p.keyboard.press('Escape'); return; }
  await S.view(name);
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The header's "More" overflow menu: a local UI toggle; its links are never
// followed. `btnRe` differs per surface (hashnode.com's carries a "New"
// badge; the blog engine's is a plain "More").
async function moreMenu(p, S, btnRe = /^more/i) {
  const btn = p.locator('button').filter({ hasText: btnRe }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! more menu missing'); return; }
  await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
  await wait(p, 1200);
  const open = await p.locator('[role="menu"], [role="listbox"], [data-radix-popper-content-wrapper] [role="menu"], [data-state="open"]').first().isVisible().catch(() => false);
  if (!open) { log('  ! more menu did not open'); await p.keyboard.press('Escape'); return; }
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// The header's "Theme" button opens a Light / Dark / System menu — shot
// open (the menu itself is the theme control), then closed without picking.
async function themeMenu(p, S) {
  const btn = p.locator('button').filter({ hasText: /^theme$/i }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! theme button missing'); return; }
  await btn.click({ timeout: 5000 }).catch(() => {});
  await wait(p, 1000);
  const open = await p.locator('[role="menu"], [role="listbox"]').first().isVisible().catch(() => false);
  if (!open) { log('  ! theme menu did not open'); await p.keyboard.press('Escape'); return; }
  await S.view('theme-menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// Dark shots of a hashnode.com page: switch through the site's own Theme
// menu (the painted check is inside setTheme), shoot, switch back. A page
// that never paints dark takes no shot.
async function darkPass(p, name, vw, vh, dpr, url, total, shots = ['default', 'full']) {
  if (!(await setTheme(p, 'dark'))) { log('  ! dark theme never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setTheme(p, 'light').catch(() => {});
  return Sd.count;
}

// Dark shots of a blog-engine page: the OS signal the engine honours
// (setBlogTheme emulates + reloads; the painted check still has to pass).
async function blogDarkPass(p, name, vw, vh, dpr, url, shots = ['default', 'full']) {
  if (!(await setBlogTheme(p, 'dark'))) { log('  ! blog dark never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setBlogTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('search', () => searchDialog(p, S));
    await step('theme-menu', () => themeMenu(p, S));
    await step('more-menu', () => moreMenu(p, S));
    await S.full();
    ctx.extra += await darkPass(p, 'home', 1440, 900, 1, BASE + '/');
  } },
  feed: { url: BASE + '/feed', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'feed', 1440, 900, 1, BASE + '/feed', ['default']);
  } },
  post: { url: BASE + '/posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'post', 1440, 900, 1, BASE + '/posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed', ['default']);
  } },
  profile: { url: BASE + '/@anish78', wait: 7000, run: BOTH },
  pro: { url: BASE + '/pro', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('faq-open', async () => {
      // A FAQ accordion question: its own press reveals the answer — a
      // local UI toggle; nothing is submitted.
      const q = p.locator('button').filter({ hasText: /what do i get with pro/i }).filter({ visible: true }).first();
      if (!(await q.count())) { log('  ! faq question missing'); return; }
      await q.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
      await S.view('faq-open');
    });
    await S.full();
    ctx.extra += await darkPass(p, 'pro', 1440, 900, 1, BASE + '/pro', ['default']);
  } },
  changelog: { url: BASE + '/changelog', wait: 7000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('tab-features', async () => {
      // A changelog category tab's own activation — a local UI toggle.
      const tab = p.locator('[role="tab"]').filter({ hasText: /features/i }).filter({ visible: true }).first();
      if (!(await tab.count())) { log('  ! features tab missing'); return; }
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('tab-features');
    });
    await S.full();
    ctx.extra += await darkPass(p, 'changelog', 1440, 900, 1, BASE + '/changelog', ['default']);
  } },
  agents: { url: BASE + '/agents', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('tab-cli', async () => {
      const tab = p.locator('[role="tab"]').filter({ hasText: /cli/i }).filter({ visible: true }).first();
      if (!(await tab.count())) { log('  ! cli tab missing'); return; }
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('tab-cli');
    });
    await S.full();
  } },
  hackathons: { url: BASE + '/hackathons', wait: 7000, run: BOTH },
  brand: { url: BASE + '/brand', wait: 7000, run: BOTH },
  'alt-medium': { url: BASE + '/alternatives/medium', wait: 7000, run: BOTH },
  blog: { url: BASE + '/blog', wait: 7000, run: BOTH },
  onboard: { url: BASE + '/onboard', wait: 7000, run: async (p, S) => {
    // The public onboarding form: shot at rest only — fields are never
    // focused, filled or submitted; "Next" is never pressed.
    await S.view('default');
    await S.full();
  } },
  'code-of-conduct': { url: BASE + '/code-of-conduct', wait: 6000, run: BOTH },
  'th-home': { url: BLOG + '/', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('search', () => searchDialog(p, S));
    await step('more-menu', () => moreMenu(p, S));
    await S.full();
    ctx.extra += await blogDarkPass(p, 'th-home', 1440, 900, 1, BLOG + '/', ['default']);
  } },
  'th-post': { url: BLOG + '/why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps', wait: 8000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await blogDarkPass(p, 'th-post', 1440, 900, 1, BLOG + '/why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps', ['default']);
  } },
  'th-archive': { url: BLOG + '/archive', wait: 7000, run: BOTH },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Open menu" button opens the phone's nav sheet — a local UI
      // toggle; its links are never followed.
      const ham = p.getByRole('button', { name: /open menu|menu/i }).filter({ visible: true }).first();
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
  feed: { url: BASE + '/feed', wait: 7000, run: BOTH },
  post: { url: BASE + '/posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed', wait: 7000, run: BOTH },
  pro: { url: BASE + '/pro', wait: 7000, run: BOTH },
  'th-home': { url: BLOG + '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('menu', () => moreMenu(p, S));
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
