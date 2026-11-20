// Captures fourmula.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix, and the theme
// is the PAINTED theme: the Webflow marketing site paints light when body carries the
// `.dark` class (localStorage isDarkMode=true, the first-visit default) and dark on a
// plain `.body`; the file names say light/dark for the paint, not the class. The theme is
// driven through the site's own isDarkMode storage key — the same key the header's
// data-theme-toggle writes — never by editing CSS. app.fourmula.ai is a separate
// dark-only Next.js app; its pages are named -dark- for the paint.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py
// stitches back together; an unbounded page truncates at 8 chunks and the log records
// the boundary. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header Menu button, the FAQ accordion, the app's Open main menu, the
// What's a PDP and Recommendations dialog triggers and the auth card's Sign up
// switcher. The "Forgot password?" control is deliberately not pressed: it is a
// form action that validates the email field and submits, not a view switch.
// The finsweet cookie-consent layer is shot once as
// evidence, then hidden for every other shot; its Accept/Settings/Save buttons are
// never pressed. The sign-in, sign-up and forgot-password fields and the create-pdp
// uploaders are shot at rest, never filled or submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, themeInit, paintedTheme, chromium, UA, UA_MOBILE, BASE, START_URL, AUTH_URL, PDP_URL } from './lib.mjs';

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
  async view(name, { promo = true } = {}) { if (promo) await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // A fresh full capture invalidates the previous whole-image output first:
    // the earlier name.png, its .capture.json sidecar and every stale part
    // tile. If the tiled capture below now fails before writing its first
    // PNG, quantize.py finds no name.png to republish — an old image can
    // never ride in on a new run — and a partial tile set dies on the
    // contiguous-run check in check_tiles instead of stitching short.
    for (const old of fs.readdirSync(RAW)) {
      if (old === `${this.prefix}-${name}.png` || old === `${this.prefix}-${name}.png.capture.json`
          || (old.startsWith(`${this.prefix}-${name}.part`) && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.unlinkSync(`${RAW}/${old}`);
    }
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

// Dismisses the app's headless-ui dialog without pressing any page control:
// Escape, then a click on the backdrop. It never clicks a text-matched
// "close" — on create-pdp that could be "Cancel and close", which leaves
// the generator.
async function dismissDialog(p) {
  for (let i = 0; i < 3; i++) {
    await p.keyboard.press('Escape').catch(() => {});
    await wait(p, 500);
    const open = await p.locator('[role="dialog"]').filter({ visible: true }).count().catch(() => 0);
    if (!open) return;
    await p.mouse.click(12, 12).catch(() => {});
    await wait(p, 500);
  }
}

// The header's "Menu" button toggles the fixed .menu nav overlay — a local UI
// toggle; its links are never followed.
async function menuOpen(p, S, state = 'menu') {
  const btn = p.locator('.header__menu').filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no menu trigger'); return; }
  const isOpen = () => p.evaluate(() => {
    const el = document.querySelector('.menu');
    if (!el) return false;
    const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return (r.height > 200 || el.className.includes('open') || el.className.includes('active')) && cs.visibility !== 'hidden' && cs.opacity !== '0';
  }).catch(() => false);
  if (!(await isOpen())) { await clickEl(btn, 4000).catch(() => {}); await wait(p, 1400); }
  if (!(await isOpen())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 1200); }
  if (!(await isOpen())) { log('  ! menu did not report open'); }
  await S.view(state);
  await p.keyboard.press('Escape');
  await clickEl(btn, 2000).catch(() => {});
  await wait(p, 600);
}

// An FAQ row opens its answer on click — a local UI toggle.
async function faqOpen(p, S) {
  const item = p.locator('.faq__item').filter({ visible: true }).first();
  if (!(await item.count())) { log('  ! no faq item'); return; }
  await item.evaluate((el) => el.scrollIntoView({ block: 'center' }));
  await wait(p, 600);
  await clickEl(item, 4000).catch(() => {});
  await wait(p, 1000);
  await S.view('faq-opened');
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('cookie', { promo: false }); // the consent layer as a visitor sees it — then hidden, never answered
    await S.view('default');
    await step('menu', () => menuOpen(p, S, 'menu'));
    await step('faq', () => faqOpen(p, S));
    await S.full();
  } },
  'home-dark': { url: BASE + '/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu', () => menuOpen(p, S, 'menu'));
    await S.full();
  } },
  privacy: { url: BASE + '/privacy-policy', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: BASE + '/terms-of-service', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'terms-dark': { url: BASE + '/terms-of-service', wait: 7000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  start: { url: START_URL, wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.getByRole('button', { name: 'Open main menu' }).first();
      if (!(await btn.count())) return;
      await clickEl(btn, 4000).catch(() => {});
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape'); await wait(p, 500);
    });
  } },
  auth: { url: AUTH_URL, wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default'); // the sign-in card
    await step('signup', async () => {
      await p.getByRole('button', { name: 'Sign up' }).last().click();
      await wait(p, 1200);
      await S.view('signup');
      await p.getByRole('button', { name: 'Sign in' }).last().click().catch(() => {});
      await wait(p, 800);
    });
    // No 'forgot' shot: "Forgot password?" is a submit, not a view switch —
    // pressing it only paints the email validation on the sign-in card.
  } },
  'create-pdp': { url: PDP_URL, wait: 10000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
    await step('pdp-info', async () => {
      await p.getByRole('button', { name: /What's a PDP/ }).first().click();
      await wait(p, 1500);
      await S.view('pdp-dialog');
      await dismissDialog(p);
    });
    await step('recommendations', async () => {
      await p.getByRole('button', { name: 'Recommendations' }).first().click();
      await wait(p, 1500);
      await S.view('recommendations');
      await dismissDialog(p);
    });
    await step('menu', async () => {
      const btn = p.getByRole('button', { name: 'Open main menu' }).first();
      if (!(await btn.count())) return;
      await clickEl(btn, 4000).catch(() => {});
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape'); await wait(p, 500);
    });
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', () => menuOpen(p, S, 'menu'));
    await S.full();
  } },
  'home-dark': { url: BASE + '/', wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  start: { url: START_URL, wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  auth: { url: AUTH_URL, wait: 9000, theme: 'dark', run: async (p, S) => {
    await S.view('default');
  } },
  'create-pdp': { url: PDP_URL, wait: 10000, theme: 'dark', run: async (p, S) => {
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
  if (spec.theme === 'dark' && spec.url.startsWith(BASE)) await ctx.addInitScript(themeInit, 'dark');
  const p = await ctx.newPage();
  log(name);
  // Files are {page}-{painted theme}-{state}.png: a page key like 'home-dark'
  // is the dark pass over the same 'home' page.
  const file = spec.file || k.replace(/-dark$/, '');
  const S = new Shooter(p, `${(mob ? 'mobile-' : '') + file}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    // the file name says the painted theme, so check the paint before any
    // shot: a marketing page that did not repaint is skipped, never written
    // as *-dark-*.png (2026-11 audit, finding 17-5; not run since)
    if (spec.url.startsWith(BASE)) {
      const t = await paintedTheme(p);
      if (t.painted !== spec.theme) { log('  THEME MISMATCH', name, 'painted', t.painted, 'body', t.bodyClass); await ctx.close(); continue; }
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
