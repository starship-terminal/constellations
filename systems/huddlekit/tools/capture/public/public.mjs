// Captures huddlekit.com's signed-out public pages — plus the app.huddlekit.com
// login, the only surface the app serves anonymously — into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix, the
// app's an `app-` prefix. huddlekit.com paints light only — its `.dark` rules
// exist for nested dark panels inside the light page, so the marketing pages
// take no dark pass. app.huddlekit.com paints html.dark under
// prefers-color-scheme (verified 2026-11-17): the app- dark shots emulate the
// OS signal and reload (setAppTheme in lib.mjs), never a script-applied class.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A
// page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8 chunks
// and the log records the boundary. Nothing is sent, typed, searched or
// signed into. Cookie Decline and Accept are not pressed. hideConsent() hides
// the banner in the stylesheet, which is not a consent answer. The presses
// that do happen are local UI toggles: the nav's hover-open Solutions/Resources
// menus, the home feature tabs, the pricing billing switches, "Show more
// testimonials", the phone's "Toggle menu" button and the login's "Continue
// with email" (the reveal itself is local; the email field is never filled
// and Continue is never pressed). Homepage FAQ rows are summary elements.
// The accordion opener looks for main button[aria-expanded] and misses them.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, hideConsent, patch, setAppTheme, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

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
  // A shot with the consent banner still up: closePromo would hide it, so
  // this bypasses the hide on purpose — the banner is itself evidence.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await wait(p, 800);
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
    // capturedHeight is the bound this pass meant to cover. quantize.py
    // refuses a stitch whose tiles do not span it, so a later tile that
    // fails after retry cannot publish a shortened sheet as checked.
    const partCount = hCap <= chunk ? 1 : Math.ceil(hCap / chunk);
    const tileRequest = (i) => ({ ...this.requested, capturedHeight: hCap, partCount, partIndex: i });
    try {
      try {
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, tileRequest(0));
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, tileRequest(i));
      } catch (e) {
        log('  ! full shot timed out/failed, retrying with animations disabled:', String(e.message).split('\n')[0]);
        // Drop tiles from the failed attempt. A retry that also fails must
        // not leave them for quantize.py to stitch as a complete sheet.
        for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
        if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true, animations: 'disabled' }, tileRequest(0));
        else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, tileRequest(i));
      }
    } catch (e) {
      log('  ! full shot failed:', String(e.message).split('\n')[0]);
      for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    }
    await p.evaluate(() => document.querySelectorAll('video').forEach((v) => v.play().catch(() => {}))).catch(() => {});
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The header nav menus (Solutions, Resources): they open on hover — a local
// UI reveal, never navigated. Shot open, then closed by moving the pointer
// away and pressing Escape.
async function navMenu(p, S, name) {
  const btn = p.getByRole('button', { name, exact: true }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! nav menu button missing:', name); return; }
  await btn.hover({ timeout: 5000 }).catch(() => {});
  await wait(p, 1200);
  const open = await p.locator('.nav-surface, [data-state="open"] ~ div, [role="menu"]').first().isVisible().catch(() => false);
  if (!open) { log('  ! nav menu did not open:', name); await p.mouse.move(720, 500); return; }
  await S.view('menu-' + name.toLowerCase());
  await p.mouse.move(720, 500);
  await p.keyboard.press('Escape');
  await wait(p, 700);
}

// A FAQ accordion row's own press reveals the answer — a local UI toggle.
async function faqOpen(p, S, re = /\?/) {
  // The header's Solutions trigger is also button[aria-expanded]. A question
  // lives in main and its label ends with "?".
  const q = p.locator('main button[aria-expanded]').filter({ hasText: re }).filter({ visible: true }).first();
  if (!(await q.count())) { log('  ! faq accordion missing'); return; }
  await q.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 900);
  await S.view('faq-open');
  await q.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 500);
}

const BOTH = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    // The consent banner is itself a component: shot before any dismissal.
    await S.raw('consent');
    await hideConsent(p);
    await S.view('default');
    await step('menu-solutions', () => navMenu(p, S, 'Solutions'));
    await step('menu-resources', () => navMenu(p, S, 'Resources'));
    await step('feature-tab', async () => {
      // A vertical feature tab's own activation — a local UI toggle that
      // switches the demo panel beside it (Radix role=tab, aria-selected).
      const tab = p.locator('[role="tab"]').filter({ hasText: /draw on the page/i }).filter({ visible: true }).first();
      if (!(await tab.count())) { log('  ! feature tab missing'); return; }
      await tab.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('feature-tab');
    });
    await step('faq-open', () => faqOpen(p, S));
    await step('testimonials-open', async () => {
      const btn = p.getByRole('button', { name: /show more testimonials/i }).filter({ visible: true }).first();
      if (!(await btn.count())) { log('  ! testimonials button missing'); return; }
      await btn.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1000);
      await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
      await S.view('testimonials-open');
    });
    await S.full();
  } },
  features: { url: BASE + '/features', wait: 7000, run: BOTH },
  pricing: { url: BASE + '/pricing', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await step('billing-toggle', async () => {
      const sw = p.locator('button[role="switch"]').filter({ visible: true }).first();
      if (!(await sw.count())) { log('  ! billing switch missing'); return; }
      await sw.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('billing-toggle');
      await sw.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 600);
    });
    await step('faq-open', () => faqOpen(p, S));
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 7000, run: BOTH },
  'blog-post': { url: BASE + '/blog/introducing-huddlekit', wait: 7000, run: BOTH },
  support: { url: BASE + '/support', wait: 7000, run: BOTH },
  'support-article': { url: BASE + '/support/getting-started', wait: 7000, run: BOTH },
  tools: { url: BASE + '/tools', wait: 7000, run: BOTH },
  'tool-contrast': { url: BASE + '/tools/color-contrast-checker', wait: 7000, run: BOTH },
  integrations: { url: BASE + '/integrations', wait: 7000, run: BOTH },
  'integration-linear': { url: BASE + '/integrations/linear', wait: 7000, run: BOTH },
  compare: { url: BASE + '/compare', wait: 7000, run: BOTH },
  'compare-page': { url: BASE + '/compare/pastel-alternative', wait: 7000, run: BOTH },
  customers: { url: BASE + '/customers', wait: 7000, run: BOTH },
  'case-study': { url: BASE + '/customers/leadfront', wait: 7000, run: BOTH },
  agencies: { url: BASE + '/agencies', wait: 7000, run: BOTH },
  manifesto: { url: BASE + '/manifesto', wait: 7000, run: BOTH },
  mcp: { url: BASE + '/mcp', wait: 7000, run: BOTH },
  contact: { url: BASE + '/contact', wait: 7000, run: BOTH },
  privacy: { url: BASE + '/privacy', wait: 7000, run: BOTH },
  'app-login': { url: APP + '/login', wait: 7000, run: async (p, S, ctx) => {
    await S.raw('consent');
    await hideConsent(p);
    await S.view('default');
    await step('email-open', async () => {
      // The button's own press reveals the email field — a local state
      // change; nothing is typed and Continue is never pressed.
      const btn = p.getByRole('button', { name: /continue with email/i }).first();
      await btn.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('email-open');
      const back = p.getByRole('button', { name: /back to login/i }).first();
      if (await back.count()) await back.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 800);
    });
    ctx.extra += await darkPass(p, 'app-login', 1440, 900, 1, APP + '/login', ['default', 'email-open']);
  } },
};

// Dark shots of an app page: prefers-color-scheme emulated + reloaded (the
// signal the app honours), shot, emulated back to light + reloaded.
async function darkPass(p, name, vw, vh, dpr, url, shots = ['default']) {
  if (!(await setAppTheme(p, 'dark'))) { log('  ! app dark never painted; dark shots skipped'); return 0; }
  const Sd = new Shooter(p, `${name}-dark`, vw, vh, dpr, url);
  for (const s of shots) {
    if (s === 'email-open') {
      const btn = p.getByRole('button', { name: /continue with email/i }).first();
      await btn.click({ timeout: 4000 }).catch(() => {});
      await wait(p, 1200);
    }
    await Sd.view(s);
  }
  await setAppTheme(p, 'light').catch(() => {});
  return Sd.count;
}

const mobile = {
  home: { url: BASE + '/', wait: 8000, run: async (p, S) => {
    await S.raw('consent');
    await hideConsent(p);
    await S.view('default');
    await step('drawer', async () => {
      // The "Toggle menu" button opens the phone's nav sheet — a local UI
      // toggle; its links are never followed.
      const ham = p.getByRole('button', { name: /toggle menu|menu/i }).filter({ visible: true }).first();
      if (!(await ham.count())) { log('  ! hamburger missing'); return; }
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()));
      await wait(p, 1500);
      const open = await p.locator('[role="dialog"], [data-state="open"], aside, .nav-surface').first().isVisible().catch(() => false);
      if (!open) log('  ! drawer did not report open; shooting anyway');
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 7000, run: BOTH },
  'tool-contrast': { url: BASE + '/tools/color-contrast-checker', wait: 7000, run: BOTH },
  'app-login': { url: APP + '/login', wait: 7000, run: async (p, S) => {
    await hideConsent(p);
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
