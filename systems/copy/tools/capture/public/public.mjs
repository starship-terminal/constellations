// Captures copy.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. copy.ai paints a
// single light theme (some sections are ink-dark bands inside the light page). Desktop shots
// are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the Platform mega-menu, an
// FAQ accordion row and the mobile navigation menu — plus focusing the contact form's first
// field (never submitted). The HubSpot cookie banner and chat widget are hidden, never
// answered; the product behind app.copy.ai is never reached — only the public login.copy.ai
// auth card is captured as a surface.
import fs from 'fs';
import path from 'node:path';
import os from 'node:os';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

// Full-colour shots stay outside the repo (docs/PACKAGE.md): quantize.py writes the
// committed screenshots/ from this scratch folder.
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'copy', 'raw-shots');
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl && String(sourceUrl).split(/[?#]/)[0] /* the sidecar reads it from here */ }; this.sourceUrl = sourceUrl; this.count = 0; }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, sanitizedSourceUrl: this.sourceUrl }, this.requested);
    this.count++; log('  shot', name);
  }
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
    const opts = (extra) => ({ path: extra, sanitizedSourceUrl: this.sourceUrl });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// The Platform/Use cases/Resources/GTM AI mega-menus are Webflow dropdowns:
// hover opens them on desktop, click is the fallback. Local UI only.
async function openMegaMenu(p, S) {
  const t = p.locator('.mega--nav_dd_toggle').filter({ hasText: /Platform/ }).filter({ visible: true }).first();
  if (!(await t.count())) return;
  await t.hover({ timeout: 5000 }).catch(() => {});
  await wait(p, 1200);
  const list = p.locator('.mega--nav_dd_list:visible, .w-dropdown-list.w--open:visible').first();
  if (!(await list.count())) { await clickEl(t); await wait(p, 1200); }
  await S.view('menu');
  await p.keyboard.press('Escape');
  await p.mouse.move(700, 500);
  await wait(p, 800);
}

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMegaMenu(p, S); });
    await S.full();
  } },
  pricing: { path: '/prices', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      // An FAQ accordion row: a local UI toggle.
      const f = p.locator('.faq--text').filter({ visible: true }).first();
      if (await f.count()) { await f.scrollIntoViewIfNeeded(); await clickEl(f); await wait(p, 1200); await S.view('faq'); }
    });
    await S.full();
  } },
  platform: { path: '/platform/how-it-works', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'use-case': { path: '/use-cases/prospecting-cockpit', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/blog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/contact-us', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('form-focus', async () => {
      // Focus the first field: a local UI state, never submitted.
      const fld = p.locator('#Name.request_input-field').filter({ visible: true }).first();
      if (await fld.count()) { await fld.scrollIntoViewIfNeeded(); await fld.click(); await wait(p, 700); await S.view('form-focus'); }
    });
    await S.full();
  } },
  changelog: { path: '/changelog', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // The public auth surface on its own host (app.copy.ai/login redirects to
  // login.copy.ai): captured as a surface, never submitted.
  login: { url: 'https://app.copy.ai/login', wait: 12000, run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('.mega--nav_burger_trigger').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1600); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/prices', wait: 9000, run: async (p, S) => {
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
  const target = spec.url || BASE + spec.path;
  const source = spec.url ? 'https://login.copy.ai/' : target;
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, source);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
