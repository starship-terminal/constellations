// Captures editorx.com's public surface into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// editorx.com is now a redirect shell for Wix Studio: every path 301s to
// wix.com/studio (deep paths keep their tail), except /pricing which still
// serves a Wix plans page on the editorx.com domain itself. Paths on BASE are
// requested on editorx.com so the redirect is the evidence; pages with no
// editorx path left (design, plans, templates) are fetched from wix.com
// directly.
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. The
// surface paints one light theme. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x — and `*-full` shots keep the context's device scale too:
// desktop `*-full` is 1x, mobile `*-full` is 2x (a 390-wide page lands at
// 780px). Each shot's .capture.json sidecar records its real scale; mobile
// full-page images are not 1x. A page taller than one GPU texture is saved
// as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the Product nav dropdown, an FAQ expander and the mobile
// navigation menu. Consent overlays are hidden, never answered; the editor
// behind Start Creating / Log In is never reached.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go
// outside the repository, to ~/.design-systems/editorx/raw-shots.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'editorx', 'raw-shots') + '/';
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
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The header's Product/Resources/Enterprise buttons open a dropdown panel (a
// click toggles it). Local UI only, never a link.
async function openDropdown(p, S, name = 'Product') {
  const t = p.locator('nav button').filter({ hasText: new RegExp('^\\s*' + name + '\\s*$') }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  await clickEl(t);
  await wait(p, 1400);
  await S.view('menu');
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openDropdown(p, S); });
    await step('mid', async () => {
      // A scroll-jacked section mid-page: the pinned showcase scene.
      await p.evaluate(() => scrollTo(0, Math.floor(document.documentElement.scrollHeight * 0.45)));
      await wait(p, 1600);
      await S.view('mid');
      await p.evaluate(() => scrollTo(0, 0)); await wait(p, 800);
    });
    await S.full();
    await step('end', async () => {
      // The closing CTA band and footer at the bottom of the page.
      await p.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
      await wait(p, 1600);
      await S.view('end');
    });
  } },
  features: { path: '/features', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  design: { path: 'https://www.wix.com/studio/design', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  plans: { path: 'https://www.wix.com/studio/plans', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // The one page still served on the editorx.com domain itself: Wix's pricing
  // page (no redirect). Plan billing toggles are local UI, never checkout.
  pricing: { path: '/pricing', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await step('billing', async () => {
      const t = p.locator('button[role="switch"], [role="radiogroup"] label, [class*="toggle" i]').filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1400); await S.view('billing'); }
    });
    await S.full();
  } },
  inspiration: { path: '/inspiration', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  templates: { path: 'https://www.wix.com/studio/templates', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  academy: { path: '/academy', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="navigation" i], button[aria-label*="menu" i], nav button').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1800); await S.view('menu'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await S.full();
  } },
  plans: { path: 'https://www.wix.com/studio/plans', wait: 11000, run: async (p, S) => {
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
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    if (spec.path) {
      const url = /^https?:/.test(spec.path) ? spec.path : BASE + spec.path;
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
