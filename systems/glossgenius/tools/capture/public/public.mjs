// Captures glossgenius.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// surface paints light only — glossgenius.com (Webflow) declares color-scheme
// normal with no dark media query, and neither app.glossgenius.com nor the
// booking subdomain shows a theme toggle — so every shot is `-light`. Desktop
// shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary.
// Nothing is sent, bought, booked or signed into: the only presses are local
// UI toggles — the "How it works" nav dropdown, the pricing Monthly/Annual
// toggle, the Beauty-&-Wellness/Medspa tier dropdown, a pricing FAQ details,
// the mobile burger menu, and on the published booking site the professional
// select (opened, never chosen). The public /booking-flow date-picker is
// photographed empty. No service is selected and "BOOK n SERVICE" is never
// pressed. The sign-in, sign-up, forgot-password and demo forms are shot
// empty, never typed into, never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP, LOGIN_URL, SIGNUP_URL, FORGOT_URL, BOOK_HOME, BOOK_SERVICES, BOOK_BOOK } from './lib.mjs';

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

// Opens a header mega-menu — the Webflow w-dropdown behind "How it works" /
// "Businesses". It is CSS-hover driven: the .dropdown_new__list flips
// visibility hidden->visible and pointer-events none->auto; no w--open class
// is added, so "open" is read off the list's computed visibility. A local UI
// state; its links are never followed.
async function navMenu(p, S, label, shotName) {
  const dd = p.locator('.dropdown_new--header').filter({ hasText: label }).first();
  if (!(await dd.count())) { log('  ! no nav dropdown labelled', label); return; }
  const t = dd.locator('.w-dropdown-toggle').first();
  const open = async () => await p.evaluate((text) => {
    for (const dd of document.querySelectorAll('.dropdown_new--header')) {
      if (!dd.innerText || !text.test(dd.innerText)) continue;
      const l = dd.querySelector('.dropdown_new__list');
      if (l && getComputedStyle(l).visibility === 'visible') return true;
    }
    return false;
  }, label).catch(() => false);
  for (let i = 0; i < 4 && !(await open()); i++) {
    await t.hover({ timeout: 4000 }).catch(() => {});
    await wait(p, 1200);
    if (await open()) break;
    await dd.hover({ timeout: 4000 }).catch(() => {});
    await wait(p, 1200);
  }
  if (!(await open())) { log('  ! nav dropdown did not report open'); return; }
  // Park the pointer over the opened list so the CSS-hover menu stays up for
  // the shot.
  const list = dd.locator('.dropdown_new__list').first();
  const box = await list.boundingBox().catch(() => null);
  if (box) await p.mouse.move(box.x + Math.min(200, box.width / 2), box.y + 40);
  await wait(p, 600);
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.mouse.move(700, 500);
  await wait(p, 700);
}

// The pricing Monthly/Annual switch — a checkbox-backed .toggle_new that
// loads ANNUAL (checked; "Billed annually, you save 14%"). The click selects
// Monthly — a local UI toggle repricing the cards; the input is clicked
// directly since label clicks do not always reach the checkbox.
async function monthlyToggle(p, S, shotName) {
  const root = p.locator('.toggle_new').filter({ visible: true }).first();
  if (!(await root.count())) return;
  await root.scrollIntoViewIfNeeded();
  const before = await p.evaluate(() => { const i = document.querySelector('.toggle_new input'); return i ? i.checked : null; }).catch(() => null);
  const input = root.locator('input[type="checkbox"], input').first();
  if (await input.count()) await input.click({ timeout: 4000, force: true }).catch(() => input.evaluate((el) => el.click()));
  else await clickEl(root);
  await wait(p, 1200);
  const after = await p.evaluate(() => { const i = document.querySelector('.toggle_new input'); return i ? i.checked : null; }).catch(() => null);
  if (before !== null && after === before) log('  ! billing switch did not change checked state');
  await S.view(shotName);
}

// The pricing "Beauty & Wellness / Medspa & Aesthetics" tier picker — a
// Webflow w-dropdown whose list toggles display:none->block on click (no
// w--open class). A local UI toggle; its options are never activated.
async function tierMenu(p, S, shotName) {
  const t = p.locator('.dropdown_new--pricing-tiers .w-dropdown-toggle').filter({ visible: true }).first();
  if (!(await t.count())) return;
  await t.scrollIntoViewIfNeeded();
  const open = async () => await p.evaluate(() => {
    for (const dd of document.querySelectorAll('.dropdown_new--pricing-tiers')) {
      const l = dd.querySelector('.w-dropdown-list');
      if (l && getComputedStyle(l).display !== 'none') return true;
    }
    return false;
  }).catch(() => false);
  for (let i = 0; i < 3 && !(await open()); i++) {
    await clickEl(t);
    await wait(p, 900);
  }
  if (!(await open())) log('  ! pricing tier dropdown did not report open');
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.mouse.move(600, 400);
  await wait(p, 600);
}

// Opens one FAQ accordion row — a <details>/<summary> disclosure, a local UI
// toggle that expands its answer.
async function faqOpen(p, S, shotName) {
  const q = p.locator('summary.accordion-trigger, .accordion-item summary, summary').filter({ visible: true }).first();
  if (!(await q.count())) return;
  await q.scrollIntoViewIfNeeded();
  await clickEl(q);
  await wait(p, 900);
  await S.view(shotName);
}

// On the booking site: the "Select a Professional" react-select opens a
// .gg-dropdown__menu. A local UI toggle; the options are never chosen.
async function proMenu(p, S, shotName) {
  const t = p.locator('[class*="selectOuterContainer"], .gg-dropdown__control').filter({ visible: true }).first();
  if (!(await t.count())) return;
  await clickEl(t);
  await wait(p, 1200);
  const open = await p.evaluate(() => !!document.querySelector('.gg-dropdown__menu')).catch(() => false);
  if (!open) { log('  ! professional dropdown did not report open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 500);
}

// Selecting a service starts a booking. The capture does not click Select.

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('hiw-menu', () => navMenu(p, S, /how it works/i, 'hiw-menu'));
    await step('biz-menu', () => navMenu(p, S, /businesses/i, 'biz-menu'));
    await step('resources-menu', () => navMenu(p, S, /resources/i, 'resources-menu'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('monthly', () => monthlyToggle(p, S, 'monthly'));
    await step('tiers-menu', () => tierMenu(p, S, 'tiers-menu'));
    await step('faq-open', () => faqOpen(p, S, 'faq-open'));
    await S.full();
  } },
  'feature-booking': { url: BASE + '/online-booking', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-payments': { url: BASE + '/payment-processing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-ai': { url: BASE + '/ai-business-tools', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  audience: { url: BASE + '/for-solo-professionals', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customer: { url: BASE + '/customers/hair-salon-software', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'blog-article': { url: BASE + '/blog/salon-spa-front-desk-productivity', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact-us', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'get-demo': { url: BASE + '/get-demo', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'free-trial': { url: BASE + '/free-trial', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/legal/privacy', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: SIGNUP_URL, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  forgot: { url: FORGOT_URL, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'book-home': { url: BOOK_HOME, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'book-services': { url: BOOK_SERVICES, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('pro-menu', () => proMenu(p, S, 'pro-menu'));
    await S.full();
  } },
  'book-flow': { url: BOOK_BOOK, wait: 10000, theme: 'light', run: async (p, S) => {
    // Empty public date-picker. Do not choose a professional, a service, or a day.
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The burger button (.header_new__m-menu-btn) opens the mobile menu —
      // a local UI toggle; its links are never followed.
      const t = p.locator('.header_new__m-menu-btn, .w-nav-button, [class*="menu-btn"]').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1200);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signup: { url: SIGNUP_URL, wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'book-services': { url: BOOK_SERVICES, wait: 10000, theme: 'light', run: async (p, S) => {
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
