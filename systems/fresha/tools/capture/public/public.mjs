// Captures fresha.com's signed-out public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every shot is
// `-light`: the Panda stack's [data-theme=dark] palette is declared in the stylesheets but
// nothing signed out paints it (documentElement carries no data-theme, no theme toggle was
// found on any public page, and prefers-color-scheme dark changes nothing without
// data-theme=auto — verified in raw/css-vars.json). Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary.
// Nothing is sent, booked or signed into: the only presses are local UI toggles — the
// header Menu drawer, the Get-the-app dialog, the search field's own suggestion popover,
// the pricing Independent/Team tab, a pricing FAQ disclosure, the B2B nav flyout, the /lp
// filter checkboxes and its See-map overlay, and the booking wizard's own service
// checkboxes (ticked then unticked — the wizard never advances past "Select services").
// The /auth and partners sign-in fields are shot at rest and filled-then-cleared, never
// submitted; every link and every Book/Continue/Search button is measured, never pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, PARTNER_SIGNIN, VENUE, VENUE_BOOKING, AUTH, USERFLOW, LP_CAT, LP_BROWSE, domFind } from './lib.mjs';

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
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
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

// Opens the header Menu drawer — a local UI toggle; its links are never
// followed. Escape or a second press closes it again.
async function menuDrawer(p, S, shotName) {
  const t = await domFind(p, /^Menu$/, { sel: 'button, [role="button"]', tag: 'smenu' });
  if (!(await t.count())) return;
  await clickEl(t.first());
  await wait(p, 1400);
  const open = await p.evaluate(() => /Log in or sign up|Download the app|For businesses/.test(document.body.innerText.slice(0, 4000))).catch(() => false);
  if (!open) { log('  ! menu drawer did not report open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
  const stillOpen = await p.evaluate(() => /Log in or sign up/.test(document.body.innerText.slice(0, 4000))).catch(() => false);
  if (stillOpen) { await clickEl(t.first()).catch(() => {}); await wait(p, 500); }
}

// Opens the Get-the-app dialog — the header button mounts a QR-code modal. A
// local UI toggle; the dialog is dismissed after the shot.
async function appDialog(p, S, shotName) {
  const t = await domFind(p, /^Get the app$/, { sel: 'button, a', tag: 'sapp' });
  if (!(await t.count())) return;
  await clickEl(t.first());
  await wait(p, 1400);
  const open = await p.evaluate(() => [...document.querySelectorAll('[role="dialog"], dialog[open]')].some((n) => n.getBoundingClientRect().width > 200)).catch(() => false);
  if (!open) { log('  ! app dialog did not mount'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// Focuses the hero treatment field — the combobox opens its suggestion
// popover on focus. A local UI state; nothing is typed or submitted.
async function searchFocus(p, S, shotName) {
  const f = p.locator('input[placeholder*="treatment" i], input[aria-label*="treatment" i], [role="combobox"]').first();
  if (!(await f.count())) return;
  await f.scrollIntoViewIfNeeded().catch(() => {});
  await clickEl(f);
  await wait(p, 1200);
  const open = await p.evaluate(() => !!document.querySelector('[role="listbox"], [role="option"]')).catch(() => false);
  if (!open) log('  ! suggestion popover did not report open');
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// Opens the B2B nav's "Business types" flyout — a local UI toggle; its links
// are never followed.
async function navFlyout(p, S, shotName) {
  const t = await domFind(p, /^Business types$/, { sel: 'button, a', tag: 'sfly' });
  if (!(await t.count())) return;
  await clickEl(t.first()).catch(() => t.first().hover({ timeout: 4000 }).catch(() => {}));
  await wait(p, 1200);
  const open = await p.evaluate(() => [...document.querySelectorAll('a')].filter((a) => /Hair salon|Nail salon|Barbershop/i.test(a.innerText || '') && a.getBoundingClientRect().top < 400).length > 2).catch(() => false);
  if (!open) log('  ! nav flyout did not report open');
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.mouse.move(700, 700).catch(() => {});
  await wait(p, 500);
}

// Opens the /lp "See map" overlay — a local UI toggle; closed afterwards.
async function mapOverlay(p, S, shotName) {
  const t = await domFind(p, /See map/i, { sel: 'button', tag: 'smap' });
  if (!(await t.count())) return;
  await clickEl(t.first());
  await wait(p, 1600);
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  const back = await domFind(p, /Back to list|Close|^List$/i, { sel: 'button', tag: 'smapx' });
  if (await back.count()) await clickEl(back.first()).catch(() => {});
  await wait(p, 600);
}

// Types into the /auth email field, shoots, then clears it. The field is never
// submitted — Continue is never pressed, so no verification code is sent.
async function authFilled(p, S, shotName) {
  const f = p.locator('input[type="email"], input[name*="email" i]').first();
  if (!(await f.count())) return;
  await clickEl(f);
  await p.keyboard.type('hello@example.com', { delay: 15 });
  await wait(p, 500);
  await S.view(shotName);
  await f.focus().catch(() => {});
  await p.keyboard.press('ControlOrMeta+a');
  await p.keyboard.press('Backspace');
  await wait(p, 300);
}

// Adds the first service to the wizard's local cart via its "+" button, shoots
// the cart line and the enabled Continue, then removes it again. The wizard
// never advances past "Select services"; nothing is booked.
// No "ticked" booking shot: pressing the service's "+" puts it in a real
// venue's cart, a state change on a third-party site. The committed
// booking-light-ticked screenshot is from a run before this edit (2026-11
// audit; not run since).

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    // The whole-page shot is taken before the interaction states: the
    // popovers these open can leave the document shortened, and the full
    // reference must be the resting page.
    await S.full();
    await step('menu', () => menuDrawer(p, S, 'menu'));
    await step('app-dialog', () => appDialog(p, S, 'app-dialog'));
    await step('search-focus', () => searchFocus(p, S, 'search-focus'));
  } },
  'user-flow': { url: USERFLOW, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  auth: { url: AUTH, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('filled', () => authFilled(p, S, 'filled'));
  } },
  'partner-signin': { url: PARTNER_SIGNIN, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  // The partner shell carries data-theme="auto" on <html> (see
  // raw/css-vars.json `live.partner`), so prefers-color-scheme dark paints a
  // real dark sign-in: #0d0d0d page, #f5f5f5 text. This is the only public
  // dark surface observed; every www.fresha.com page ignores the media query.
  'partner-signin-dark': { url: PARTNER_SIGNIN, wait: 10000, theme: 'dark', dark: true, run: async (p, S) => {
    await S.view('default');
  } },
  venue: { url: VENUE, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('services', async () => {
      const s = await domFind(p, /^Services$/, { sel: 'a,button,[role="tab"]', tag: 'svc-t' });
      if (await s.count()) { await clickEl(s.first()); await wait(p, 900); }
      await S.view('services');
    });
  } },
  booking: { url: VENUE_BOOKING, wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('faq-open', async () => {
      const faq = await domFind(p, /How do|What is|Can I/i, { sel: 'button, summary', tag: 'sfaq', minW: 200 });
      if (!(await faq.count())) return;
      await faq.first().scrollIntoViewIfNeeded().catch(() => {});
      await clickEl(faq.first());
      await wait(p, 800);
      await S.view('faq-open');
    });
  } },
  'for-business': { url: BASE + '/for-business', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('flyout', () => navFlyout(p, S, 'flyout'));
  } },
  'lp-browse': { url: LP_BROWSE, wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('map', () => mapOverlay(p, S, 'map'));
  } },
  'lp-category': { url: LP_CAT, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { url: BASE + '/help-center', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  careers: { url: BASE + '/careers', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'download-app': { url: BASE + '/download-app', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  cookies: { url: BASE + '/cookies', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('menu', () => menuDrawer(p, S, 'menu'));
  } },
  auth: { url: AUTH, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'lp-browse': { url: LP_BROWSE, wait: 11000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  venue: { url: VENUE, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
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
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: spec.dark ? 'dark' : 'light' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  // A route key that already ends in the theme (partner-signin-dark) is its
  // own stem: appending spec.theme again would write *-dark-dark files the
  // package does not link.
  const stem = name.endsWith(`-${spec.theme}`) ? name : `${name}-${spec.theme}`;
  const S = new Shooter(p, stem, vw, vh, dpr, spec.url);
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
