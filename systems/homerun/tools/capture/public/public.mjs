// Captures homerun.co's public pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page ...]
//
// Only signed-out surfaces: the www.homerun.co Webflow marketing routes,
// jobs.homerun.co (the employer careers site the product publishes) and its
// open-application form at rest, and the app.homerun.co / app.homerun.hr
// sign-in cards — the last a boundary, screenshotted never acted on.
// Nothing is sent, created or signed into: the only presses are local UI
// toggles — the nav Resources/Log-in dropdowns, FAQ accordions and the
// mobile nav button.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, JOBS, APP, APPHR } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    // Stage every tile under a .new name and swap it in only after the whole
    // shot succeeds, so a failed tile never truncates the previous capture.
    const staged = [];
    try {
      if (hCap <= chunk) {
        // Push the temp name before the capture: if the size check inside
        // screenshotWithMetadata fails after writing the PNG, the cleanup
        // below must still find and remove the .new file.
        staged.push([f + '.new.png', f + '.png']);
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          staged.push([tmp, `${f}.part${i}.png`]);
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) {
        fs.existsSync(tmp) && fs.unlinkSync(tmp);
        fs.existsSync(tmp + '.capture.json') && fs.unlinkSync(tmp + '.capture.json');
      }
      throw e;
    }
    // Swap the staged files in first: a `.new.png` tile is not a stale tile,
    // and the previous capture stays intact until its replacement is fully
    // renamed. The .capture.json sidecar moves with its PNG and records the
    // final screenshot name.
    const keep = new Set();
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      keep.add(path.basename(final));
      const sideTmp = tmp + '.capture.json', sideFinal = final + '.capture.json';
      if (fs.existsSync(sideTmp)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sideTmp, 'utf8'));
          meta.screenshot = path.basename(final);
          fs.writeFileSync(sideTmp, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* keep the sidecar as written */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    // Only now drop leftovers the new shot does not produce: higher part
    // numbers of a previous taller capture (and their sidecars), or the old
    // single-file shot.
    const isStaged = (n) => n.endsWith('.new.png') || n.endsWith('.new.png.capture.json');
    for (const old of fs.readdirSync(RAW).filter((n) =>
      !isStaged(n) && !keep.has(n) &&
      (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The desktop nav's two dropdowns are hover-open Webflow toggles
// (w-dropdown data-hover="true"): Resources opens a link panel, Log in opens
// the ATS/HR sign-in menu. They are held open under the pointer for the shot;
// the toggle is never navigated.
const openNavDropdown = async (p, which) => {
  const ok = await p.evaluate((w) => {
    const el = [...document.querySelectorAll('.nav_component .w-dropdown-toggle, .nav-primary .w-dropdown-toggle, nav .w-dropdown-toggle')].find((e) => (e.innerText || '').trim().toLowerCase().startsWith(w));
    if (!el) return false;
    el.setAttribute('data-m-nav-' + w, '1');
    return true;
  }, which);
  if (!ok) return false;
  const loc = p.locator(`[data-m-nav-${which}="1"]`);
  await loc.hover({ timeout: 5000 });
  await wait(p, 1400);
  const shown = await p.evaluate((w) => {
    const t = document.querySelector(`[data-m-nav-${w}="1"]`);
    const dd = t && t.closest('.w-dropdown');
    const list = dd && dd.querySelector('.w-dropdown-list');
    return !!(list && getComputedStyle(list).display !== 'none');
  }, which);
  if (!shown) { await clickEl(loc); await wait(p, 900); }
  return shown || (await p.evaluate((w) => {
    const t = document.querySelector(`[data-m-nav-${w}="1"]`);
    const dd = t && t.closest('.w-dropdown');
    const list = dd && dd.querySelector('.w-dropdown-list');
    return !!(list && getComputedStyle(list).display !== 'none');
  }, which));
};

// The mobile bar's hamburger: the visible .w-nav-button in the 390 nav — a
// local menu toggle, never a link. There are two copies in the DOM (the
// hidden one sizes 0x0), and Playwright's tap never reaches the visible
// one through the nav's pointer-event layering, so the open is an in-page
// click on the painted button; the menu reports itself open by the
// w--open class and the w-nav-menu painting.
const openMobileMenu = async (p) => {
  await p.evaluate(() => {
    const el = [...document.querySelectorAll('.w-nav-button')].find((e) => e.offsetParent && e.getBoundingClientRect().width > 0);
    if (el) el.click();
  });
  await wait(p, 1600);
  return p.evaluate(() => [...document.querySelectorAll('.nav_menu-new, .w-nav-menu')].some((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 0 && r.height > 40 && getComputedStyle(e).display !== 'none';
  }));
};

const mk = (url, waitMs, full = true, theme = 'light') => ({ url, wait: waitMs, theme, run: async (p, S) => { await S.view('default'); if (full) await S.full(); } });
const desktop = {
  home: { url: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('nav-resources-open', async () => { if (await openNavDropdown(p, 'resources')) { await S.view('nav-resources-open'); await p.keyboard.press('Escape'); await p.mouse.click(720, 480); await wait(p, 700); } });
    await step('nav-login-open', async () => { if (await openNavDropdown(p, 'log')) { await S.view('nav-login-open'); await p.keyboard.press('Escape'); await p.mouse.click(720, 480); await wait(p, 700); } });
    await S.full();
  } },
  ats: mk('/ats', 8000),
  hr: mk('/hr', 8000),
  features: mk('/product/features', 8000),
  pricing: { url: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('faq-open', async () => {
      // Scope to the pricing FAQ block: a bare .w-dropdown search finds the
      // shared nav dropdowns first, which answers nothing about the FAQ.
      const item = await p.evaluate(() => {
        const el = [...document.querySelectorAll('.section_pricing_faq .h-new_features-item.w-dropdown, .pricing_faq-block .h-new_features-item.w-dropdown')].find((e) => (e.innerText || '').trim().length > 5);
        if (!el) return false;
        const t = el.querySelector('.w-dropdown-toggle');
        (t || el).setAttribute('data-m-faq', '1');
        return true;
      });
      if (item) {
        await clickEl(p.locator('[data-m-faq="1"]'));
        await wait(p, 1300);
        // Only save once an answer actually painted; scroll the opened item
        // into view so the shot shows the FAQ, not the page top.
        const open = await p.evaluate(() => {
          const el = document.querySelector('[data-m-faq="1"]') && document.querySelector('[data-m-faq="1"]').closest('.w-dropdown');
          const list = el && el.querySelector('.w-dropdown-list');
          if (!list) return false;
          const r = list.getBoundingClientRect();
          if (!r.height || getComputedStyle(list).display === 'none') return false;
          el.scrollIntoView({ block: 'center' });
          return true;
        });
        if (open) { await wait(p, 600); await S.view('faq-open'); }
      }
    });
    await S.full();
  } },
  customers: mk('/customers', 8000),
  about: mk('/about', 8000),
  contact: mk('/contact', 8000),
  blog: mk('/blog', 8000),
  templates: mk('/templates', 8000),
  integrations: mk('/integrations', 8000),
  guides: mk('/guides', 8000),
  updates: mk('/updates/', 8000),
  // The trial page: the signup form itself is injected by a script Cookiebot
  // holds back until consent — never answered, so the skeleton preview is
  // what a visitor who never answers sees. Consent banner hidden, not clicked.
  trial: mk('/trial', 12000),
  privacy: mk('/privacy-statement', 7000),
  // jobs.homerun.co is Homerun's own careers site — the product's public
  // employer surface. Its own cookie banner is hidden, never answered.
  careers: mk('https://jobs.homerun.co/', 9000),
  // An open-application page in English (the listed jobs post in Dutch).
  job: mk('https://jobs.homerun.co/open/en', 9000),
  // The public application form, at rest — measured never submitted.
  apply: mk('https://jobs.homerun.co/open/en/apply', 10000, false),
  // The two sign-in boundaries, at rest only.
  signin: mk('https://app.homerun.co/login', 15000, false),
  signinhr: mk('https://app.homerun.hr/Account/Logon', 12000, false),
};

const mobile = {
  home: { url: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) { await S.view('menu-open'); await p.keyboard.press('Escape'); await wait(p, 500); } });
    await S.full();
  } },
  pricing: mk('/pricing', 8000),
  ats: mk('/ats', 8000),
  careers: mk('https://jobs.homerun.co/', 9000),
  apply: mk('https://jobs.homerun.co/open/en/apply', 10000, false),
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
  p.setDefaultTimeout(90000);
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme || 'light'}`, vw, vh, dpr);
  try {
    const u = /^https?:/.test(spec.url) ? spec.url : BASE + spec.url;
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
