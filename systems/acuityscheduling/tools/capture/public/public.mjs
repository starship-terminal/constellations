// Captures acuityscheduling.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the nav
// dropdowns, the pricing FAQ accordion and the mobile hamburger menu. Consent banners are
// hidden remove-only (their buttons are never clicked). The Log in / Get started links land
// on Squarespace's public auth gate; it is photographed, never submitted.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, killGeo, clearChallenge, chromium, patch, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
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
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    let H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    // A degenerate page state (the 2026-11 run saw scrollHeight report ~7.7M px
    // on mobile with the menu stuck open) must not write thousands of tiles.
    const MAXH = 30 * chunk;
    if (H > MAXH) { log('  CLAMPED scrollHeight', H, '->', MAXH); H = MAXH; }
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < H; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The nav dropdowns and FAQ accordions are local UI state: they reveal a panel
// or answer over the page, never submit anything.
const hoverDropdown = async (p, label) => {
  const t = p.locator('button.dropdown__trigger-link').filter({ hasText: new RegExp('^\\s*' + label, 'i') }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.hover(); await wait(p, 1400); return true;
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('dropdown', async () => { if (await hoverDropdown(p, 'Solutions')) { await S.view('dropdown'); await p.mouse.move(10, 600); await wait(p, 800); } });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const acc = p.locator('button.accordion-title, .accordion-title button').filter({ visible: true }).first();
      if (await acc.count()) { await acc.scrollIntoViewIfNeeded(); await clickEl(acc); await wait(p, 900); await S.view('faq-open'); }
    });
    await S.full();
  } },
  'how-it-works': { path: '/features/how-acuity-works', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { path: '/features', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  solutions: { path: '/solutions', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  beauty: { path: '/solutions/beauty', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  learn: { path: '/learn', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'get-started': { path: '/get-started?type=professional', run: async (p, S) => {
    // Lands on Squarespace's "Create your account" gate — a real public surface.
    await S.view('default');
    await step('more-options', async () => {
      const mo = p.getByText(/more options/i).filter({ visible: true }).first();
      if (await mo.count()) { await clickEl(mo); await wait(p, 800); await S.view('more-options'); }
    });
    await S.full();
  } },
  login: { path: 'https://secure.acuityscheduling.com/login?nav=1', run: async (p, S) => {
    // Redirects to Squarespace's sign-in page: a real public surface.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const t = p.locator('button.hamburger-icon').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('menu'); await p.keyboard.press('Escape').catch(()=>{}); await wait(p, 600);
        // Belt and braces: if the menu is still open the page can report a
        // runaway scrollHeight (observed once, ~7.7M px). Force it closed.
        await p.evaluate(() => { document.querySelectorAll('.mobile-menu-container').forEach((n) => { n.style.display = 'none'; }); document.body.style.removeProperty('overflow'); });
        await wait(p, 400); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(spec.path.startsWith('http') ? spec.path : BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      let clean = true;
      for (let i = 0; i < 6; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$|page cannot be found/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED challenge-or-error', spec.path); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
