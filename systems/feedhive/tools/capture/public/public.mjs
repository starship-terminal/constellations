// Captures feedhive.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every
// www.feedhive.com page paints light — there is no user theme toggle and no
// dark mode. app.feedhive.com/signin and /signup are the signed-out edge of the
// separate Chakra-UI app: a light sign-in card over a pale field with an indigo
// blob, captured signed out at rest. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved
// as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's dropdown nav triggers (Product / Agents & Automation
// / Socials / Learn, anchors with href="#"), the mobile menu, and the pricing
// page's Monthly/Yearly billing toggle. The /tools forms and the signin/signup
// fields are shot at rest, never submitted. The vanilla-cookieconsent layer
// stays empty on every observed load; any consent overlay is hidden, never
// answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LOGIN_URL, SIGNUP_URL } from './lib.mjs';

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

// Opens one of the header dropdowns (Product / Agents & Automation / Socials /
// Learn — anchors with href="#", local UI toggles, never followed) and shoots
// the panel.
async function navMenu(p, S, name) {
  const btn = p.locator('header a[href="#"], header button').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no', name, 'trigger'); return; }
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await clickEl(btn, 4000).catch(() => {});
    await wait(p, 800);
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 800); }
  }
  const open = await p.evaluate(() => {
    const el = [...document.querySelectorAll('header [class*="absolute"], header [class*="dropdown"], header [role="menu"], body > div[class*="fixed"]')].find((x) => {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      return r.width > 200 && r.height > 100 && /\S/.test(x.textContent || '') && cs.visibility !== 'hidden' && cs.opacity !== '0';
    });
    return !!el;
  }).catch(() => false);
  if (!(await expanded()) && !open) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
  await p.keyboard.press('Escape');
  await wait(p, 600);
}

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-product', () => navMenu(p, S, 'Product'));
    await step('menu-agents', () => navMenu(p, S, 'Agents & Automation'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('billing-toggle', async () => {
      // The Monthly/Yearly billing pill is a local UI toggle that re-renders
      // the plan prices; it submits nothing.
      const m = p.locator('button, [role="tab"], a').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first();
      if (!(await m.count())) return;
      await clickEl(m, 4000).catch(() => {});
      await wait(p, 900);
      await S.view('billing-monthly');
      const y = p.locator('button, [role="tab"], a').filter({ hasText: /^Yearly$/ }).filter({ visible: true }).first();
      if (await y.count()) await clickEl(y, 4000).catch(() => {});
      await wait(p, 600);
    });
    await S.full();
  } },
  'features-scheduling': { url: BASE + '/features/scheduling', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'features-ai': { url: BASE + '/features/ai', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  integrations: { url: BASE + '/integrations', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'blog-article': { url: BASE + '/blog/the-best-time-to-post-on-instagram', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { url: BASE + '/tools', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'tools-bio': { url: BASE + '/tools/bio-generator', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  alternatives: { url: BASE + '/alternatives', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy', wait: 6000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: BASE + '/terms', wait: 6000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 12000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: SIGNUP_URL, wait: 12000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's icon-only menu button toggles the nav overlay — a local
      // UI toggle; its links are never followed.
      const ham = p.locator('header button').filter({ visible: true }).last();
      if (!(await ham.count())) return;
      const open = () => p.evaluate(() => !!([...document.querySelectorAll('body > div, body > nav, [role="dialog"], header [class*="fixed"]')].find((x) => {
        const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
        return r.height > 300 && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
      }))).catch(() => false);
      if (!(await open())) await clickEl(ham);
      await wait(p, 1000);
      if (!(await open())) { await ham.focus(); await p.keyboard.press('Enter'); await wait(p, 1000); }
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  tools: { url: BASE + '/tools', wait: 7000, theme: 'light', run: async (p, S) => {
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
