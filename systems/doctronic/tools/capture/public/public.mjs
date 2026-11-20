// Captures doctronic.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. doctronic.ai ships
// both themes: light is the default, dark is reached through the site's own persisted theme
// choice (localStorage.theme=dark, set by an init script — exactly what a user who chose dark
// gets). Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page
// taller than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, created or signed into: the only presses are local UI toggles — the home
// page's menu drawer ("open sidebar"), /chat/'s "Expand sidebar" rail, and the mobile menu.
// The chat composer is filled with sample text that is deleted again; Send/Start chat, the
// suggestion chips and every sign-in action are never pressed. The ?modal=signin URL renders
// the sign-in card — loaded directly, never submitted. The reCAPTCHA badge is hidden, never
// answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name, { promo = true } = {}) { if (promo) await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i += 1, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The chat composer: type sample text, screenshot, delete it again. Send is
// never pressed — a filled composer is a local state until submitted.
async function fillComposer(p, S, name = 'filled') {
  const ta = p.locator('textarea').filter({ visible: true }).first();
  if (!(await ta.count())) return;
  await ta.click().catch(() => ta.evaluate((el) => { el.focus(); el.click(); }));
  await ta.type('headache for two days', { delay: 8 });
  await wait(p, 700);
  // promo:false — the expanded rail holds a "Sign up for free" button whose
  // text would make closePromo hide the rail itself.
  await S.view(name, { promo: false });
  await ta.focus(); await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.press('Backspace');
  await wait(p, 400);
}

// The home page's "open sidebar" button opens the site-menu drawer (a local
// UI toggle). Escape closes it.
async function menuDrawer(p, S) {
  // A Locator is always truthy, so `a || b` never fell back: pick by count() instead.
  let b = p.getByRole('button', { name: /open sidebar|open menu|menu/i }).filter({ visible: true }).first();
  if (!(await b.count())) b = p.locator('[class*="_buttonBase"]').filter({ visible: true }).first();
  if (!(await b.count())) return;
  await clickEl(b);
  await wait(p, 1600);
  // promo:false — the drawer links include "Sign up"-worded rows; closePromo
  // would hide the drawer it just opened.
  await S.view('menu', { promo: false });
  await p.keyboard.press('Escape');
  await wait(p, 700);
}

// /chat/'s left rail collapses to icons; "Expand sidebar" is a local toggle.
async function chatSidebar(p, S) {
  const b = p.getByRole('button', { name: /expand sidebar/i }).filter({ visible: true }).first();
  if (!(await b.count())) return;
  await clickEl(b);
  await wait(p, 1400);
  // promo:false — same as the menu drawer: the expanded rail's own Sign up /
  // Log in rows would trip the promo detector.
  await S.view('sidebar', { promo: false });
}

const desktop = {
  home: { path: '/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await menuDrawer(p, S); });
    await step('focused', async () => {
      const ta = p.locator('textarea').filter({ visible: true }).first();
      if (await ta.count()) { await ta.click({ timeout: 5000 }).catch(() => ta.evaluate((el) => { el.focus(); el.click(); })); await wait(p, 700); await S.view('composer-focused'); }
    });
    await S.full();
  } },
  chat: { path: '/chat/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await step('sidebar', async () => { await chatSidebar(p, S); });
    await step('filled', async () => { await fillComposer(p, S); });
  } },
  'chat-signin': { path: '/?modal=signin', wait: 8000, themes: ['light'], run: async (p, S) => {
    // The sign-in card renders from the URL alone; nothing is submitted.
    await S.view('signin');
  } },
  'symptom-checker': { path: '/symptom-checker/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'resource-center': { path: '/resource-center/', wait: 7000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const q = p.locator('input[type="search"], input[placeholder*="Search" i]').filter({ visible: true }).first();
      if (await q.count()) { await q.click(); await q.type('sleep', { delay: 10 }); await wait(p, 1200); await S.view('search'); }
    });
    await S.full();
  } },
  telehealth: { path: '/telehealth/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  urology: { path: '/urology/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'our-philosophy': { path: '/our-philosophy/', wait: 7000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  authors: { path: '/authors/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  careers: { path: '/careers/', wait: 7000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'online-treatment': { path: '/online-treatment/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'prescription-glp-1': { path: '/prescription-glp-1/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'wall-of-love': { path: '/wall-of-love/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/about/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'privacy-policy': { path: '/privacy-policy/', wait: 6000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
  } },
  partnerships: { path: '/strategic-partnerships-driving-healthcare-innovation/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await menuDrawer(p, S); });
    await S.full();
  } },
  chat: { path: '/chat/', wait: 8000, themes: ['light', 'dark'], run: async (p, S) => {
    await S.view('default');
  } },
  'symptom-checker': { path: '/symptom-checker/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog/', wait: 8000, themes: ['light'], run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  const spec = (mob ? mobile : desktop)[k];
  for (const theme of spec.themes || ['light']) {
    const runName = `${name}-${theme}`;
    if (pageArg.length && !pageArg.includes(runName) && !pageArg.includes(name)) continue;
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    await patch(ctx, theme);
    const p = await ctx.newPage();
    log(runName);
    const S = new Shooter(p, runName, vw, vh, dpr);
    try {
      if (spec.path) {
        await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
        if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
        await wait(p, spec.wait || 7000);
        // The theme is only requested (localStorage.theme); check what painted before naming a shot
        // after it. The canvas is the first opaque ground among the page's main content area
        // (doctronic paints it on main.layoutContent while body stays transparent), body and html;
        // when all are transparent the canvas is the browser's white.
        const lum = await p.evaluate(() => {
          for (const el of [document.querySelector('main'), document.body, document.documentElement]) {
            if (!el) continue;
            const m = getComputedStyle(el).backgroundColor.match(/[\d.]+/g);
            if (m && (m.length < 4 || +m[3] > 0)) return (0.2126 * m[0] + 0.7152 * m[1] + 0.0722 * m[2]) / 255;
          }
          return 1;
        }).catch(() => null);
        if (lum === null) { log('  THEME UNCHECKED', runName, '- skipped'); await ctx.close(); continue; }
        if ((theme === 'dark') !== (lum < 0.5)) { log('  THEME MISMATCH', runName, 'painted luminance', lum.toFixed(2), '- skipped'); await ctx.close(); continue; }
      }
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', runName, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await b.close();
