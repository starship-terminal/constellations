// Captures helloivy.co's signed-out public pages into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix,
// app.helloivy.co ones an `app-` prefix. The marketing site paints
// html[toggle-theme=light] by default and repaints through the footer's own
// "Change theme" control (a real click on the painted toggle, persisted as
// localStorage.currentToggleState — verified painted before each shot, then
// switched back). The app surface (/login and the public Media-kit share)
// has no theme control and paints light only. Desktop shots are 1440x900 at
// 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the
// boundary. Nothing is sent, bought, typed, searched or signed into: the
// only presses are local UI toggles — the nav Menu overlay (desktop
// hamburger and the phone's menu box), the footer "Change theme" toggle, a
// pricing FAQ row, and the share page's own Settings menu.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, setTheme, chromium, UA, UA_MOBILE, BASE, APP, SHARE } from './lib.mjs';

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

// helloivy.co scrolls the document itself (Framer pages carry no inner
// scroller); findScroller() still picks the largest scrollable pane when a
// page grows one, and lazyScroll walks it so lazy sections paint before the
// shot.
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

// For the full shot an inner scroller's ancestors are relaxed to natural
// height so the document itself becomes as tall as the content — a normal
// fullPage capture then paints every section. restore() puts the shell back
// so later shots see the real layout. (Marketing pages have no inner
// scroller, so this is a no-op there.)
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

// The nav's menu button — the bordered hamburger box at the nav bar's right
// edge (data-framer-name "Menu" on the phone, the same box drawn at desktop
// widths) — opens the 01 HOME / 02 FEATURES … overlay. A local UI toggle;
// its links are never followed. Closed by the overlay's own X or reload.
async function menuOverlay(p, S) {
  // The menu box sits in the top strip: at a scrolled position its painted
  // element is not the live control, so the overlay only opens from the top.
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 1200);
  const ok = await p.evaluate(() => {
    const els = [...document.querySelectorAll('[data-framer-name="Menu"], [data-framer-name="menu"]')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (r.width === 0 || r.top > 200) return false;
      let anc = e;
      while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
      return true;
    });
    const el = els[0];
    if (!el) return false;
    const r = el.getBoundingClientRect();
    el.setAttribute('data-menu-xy', `${r.x + r.width / 2},${r.y + r.height / 2}`);
    return true;
  });
  if (!ok) { log('  ! nav menu control missing'); return; }
  const [x, y] = (await p.evaluate(() => document.querySelector('[data-menu-xy]').getAttribute('data-menu-xy'))).split(',').map(Number);
  const isTouch = await p.evaluate(() => 'ontouchstart' in window && navigator.maxTouchPoints > 0);
  // The overlay's own painted box reports open — html/body also carry the
  // text when the overlay never mounted, so they cannot count.
  const isOpen = () => p.evaluate(() => [...document.querySelectorAll('*')].some((e) => e !== document.documentElement && e !== document.body && /01\s*HOME/i.test(e.innerText || '') && /FEATURES/i.test(e.innerText || '') && (e.innerText || '').length < 4000 && e.getBoundingClientRect().height > 300));
  // The press is flaky while the nav bar is still animating: press until the
  // overlay reports open (up to four tries), never a double-toggle — a retry
  // only fires while the overlay is still closed.
  let open = false;
  for (let i = 0; i < 4 && !open; i++) {
    if (isTouch) await p.touchscreen.tap(x, y).catch(() => p.mouse.click(x, y));
    else await p.mouse.click(x, y);
    await wait(p, 2600);
    open = await isOpen();
  }
  if (!open) log('  ! menu overlay did not report open; shooting anyway');
  await S.view('menu');
  // The Framer overlay ignores Escape: its own X box closes it. A missed
  // close leaves the overlay covering every later state, so the run order
  // shoots the menu last and the close is belt-and-braces.
  const closed = await p.evaluate(() => {
    const x = [...document.querySelectorAll('div')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (r.width === 0 || r.top > 120 || r.left < (innerWidth - 200)) return false;
      const hasX = e.querySelector('svg') && (e.innerText || '').trim() === '';
      let anc = e, ok = true;
      while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') { ok = false; break; } anc = anc.parentElement; }
      return ok && hasX;
    })[0];
    if (x) { const r = x.getBoundingClientRect(); x.setAttribute('data-close-xy', `${r.x + r.width / 2},${r.y + r.height / 2}`); }
    return Boolean(x);
  });
  if (closed) {
    const [cx, cy] = (await p.evaluate(() => document.querySelector('[data-close-xy]').getAttribute('data-close-xy'))).split(',').map(Number);
    await p.mouse.click(cx, cy).catch(() => {});
    await wait(p, 1000);
  }
}

// The footer's theme control itself, open for the shot: scroll it into view
// (no press — the press is the theme switch, covered by darkPass).
async function themeControl(p, S) {
  const leaf = await p.evaluate(() => {
    const cands = [...document.querySelectorAll('div,span,p,a,button')].filter((e) => (e.innerText || '').trim() === 'Change theme');
    for (const e of cands) {
      const r = e.getBoundingClientRect();
      if (r.width === 0) continue;
      let anc = e, ok = true;
      while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden' || cs.opacity === '0') { ok = false; break; } anc = anc.parentElement; }
      if (ok) { e.scrollIntoView({ block: 'center', behavior: 'instant' }); return true; }
    }
    return false;
  });
  if (!leaf) { log('  ! change-theme control missing'); return; }
  await wait(p, 700);
  await S.view('theme-control');
}

// A FAQ accordion row on /pricing: its own press reveals the answer — a
// local UI toggle; pressed again to close.
async function faqOpen(p, S) {
  const q = await p.evaluate(() => {
    const rows = [...document.querySelectorAll('div,p,h1,h2,h3,button,a')].filter((e) => /^Is Hello Ivy only useful for design teams\??$/i.test((e.innerText || '').trim()));
    const el = rows[0];
    if (!el) return false;
    // Scroll first, then read the press point — coordinates taken before
    // the scroll are stale the moment the row moves.
    el.setAttribute('data-faq-xy', '1');
    el.scrollIntoView({ block: 'center', behavior: 'instant' });
    return true;
  });
  if (!q) { log('  ! faq question missing'); return; }
  await wait(p, 800);
  const pt = await p.evaluate(() => {
    const el = document.querySelector('[data-faq-xy]');
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2, h: document.documentElement.scrollHeight };
  });
  if (!pt || pt.y < 0 || pt.y > (p.viewportSize()?.height ?? 900)) { log('  ! faq question off-viewport after scroll'); return; }
  await p.mouse.click(pt.x, pt.y).catch(() => {});
  await wait(p, 1200);
  // The shot is only 'faq-open' when the row actually opened: the answer
  // grows the document, or a row reports expanded.
  const opened = await p.evaluate((h) =>
    document.documentElement.scrollHeight > h + 20 || Boolean(document.querySelector('[aria-expanded="true"]')), pt.h);
  if (!opened) { log('  ! faq press opened no answer — shot skipped'); return; }
  await S.view('faq-open');
}

// The share page's own "Settings" button: a local UI toggle opening the
// document menu (Send to mail / Print / word count). Closed with Escape.
async function shareSettings(p, S) {
  const btn = p.locator('button, a, [role="button"]').filter({ hasText: /^settings$/i }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! share settings button missing'); return; }
  await btn.click({ timeout: 5000 }).catch(() => {});
  await wait(p, 1600);
  await S.view('settings-menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

// Dark shots of a marketing page: switch through the footer's own "Change
// theme" control (the painted check is inside setTheme), shoot, switch back.
async function darkPass(p, name, vw, vh, dpr, url, shots = ['default']) {
  if (!(await setTheme(p, 'dark'))) { log('  ! dark theme never painted; dark shots skipped'); return 0; }
  // The toggle lives in the footer — the page is scrolled there after the
  // switch, and a viewport shot taken now would be the footer, not the
  // page top the light default shows.
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 900);
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) { if (s === 'full') await Sd.full(); else await Sd.view(s); }
  await setTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('theme-control', () => themeControl(p, S));
    await S.full();
    ctx.extra += await darkPass(p, 'home', 1440, 900, 1, BASE + '/', ['default', 'full']);
    // the overlay ignores Escape and covers the page, so the menu is the
    // last state shot on this page.
    await step('menu', () => menuOverlay(p, S));
  } },
  features: { url: BASE + '/features', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'features', 1440, 900, 1, BASE + '/features');
  } },
  'feature-tasks': { url: BASE + '/features/tasks', wait: 9000, run: BOTH },
  'feature-annotate': { url: BASE + '/features/annotate', wait: 9000, run: BOTH },
  'feature-portal': { url: BASE + '/features/client-portal', wait: 9000, run: BOTH },
  pricing: { url: BASE + '/pricing', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await step('faq-open', () => faqOpen(p, S));
    await S.full();
    ctx.extra += await darkPass(p, 'pricing', 1440, 900, 1, BASE + '/pricing');
  } },
  about: { url: BASE + '/about', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'about', 1440, 900, 1, BASE + '/about');
  } },
  blog: { url: BASE + '/blog', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'blog', 1440, 900, 1, BASE + '/blog');
  } },
  'blog-post': { url: BASE + '/blog/announcing-hello-ivy-2-0', wait: 9000, run: BOTH },
  docs: { url: BASE + '/docs', wait: 9000, run: async (p, S, ctx) => {
    await S.view('default');
    await S.full();
    ctx.extra += await darkPass(p, 'docs', 1440, 900, 1, BASE + '/docs');
  } },
  'doc-page': { url: BASE + '/docs/create-a-project', wait: 9000, run: BOTH },
  'release-notes': { url: BASE + '/release-notes', wait: 9000, run: BOTH },
  'project-management': { url: BASE + '/project-management', wait: 9000, run: BOTH },
  'project-collab': { url: BASE + '/project-collaboration-software', wait: 9000, run: BOTH },
  'alt-notion': { url: BASE + '/notion-alternative', wait: 9000, run: BOTH },
  terms: { url: BASE + '/terms', wait: 9000, run: BOTH },
  'app-login': { url: APP + '/login', wait: 10000, run: BOTH },
  'app-share': { url: SHARE, wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('settings-menu', () => shareSettings(p, S));
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    // shot last — the overlay ignores Escape and covers the page.
    await step('drawer', () => menuOverlay(p, S));
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, run: BOTH },
  features: { url: BASE + '/features', wait: 9000, run: BOTH },
  blog: { url: BASE + '/blog', wait: 9000, run: BOTH },
  'app-login': { url: APP + '/login', wait: 10000, run: BOTH },
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
