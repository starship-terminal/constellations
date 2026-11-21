// Captures Anam's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   [RAW=<dir, default ~/.design-systems/anam/raw-shots>] PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Two public surfaces on one host:
//   anam.ai         the Framer marketing site plus Next.js app pages. See site-tree.md.
//   anam.ai/docs    the Mintlify docs: /docs/introduction/overview, /docs/api-reference/overview
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix, docs-dark runs are
// {page}-dark-{state}.png. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together.
//
// Nothing is sent, created or signed into: the cookie card is hidden without a consent click; the
// only presses are local UI toggles (a persona chip on home, the docs theme button, the ⌘K/⌘I
// panels, a billing period switch). "Talk with Sophie" starts a live avatar call and is never
// pressed; the /get-demo form is measured and photographed, never submitted; lab.anam.ai is the
// app and is never opened.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const base = `${this.prefix}-${name}`;
    // The new shot goes to a scratch folder first. Only once every tile is
    // written are this shot's earlier name.png and name.partN.png (and their
    // .capture.json sidecars) removed — stale tiles would otherwise be
    // stitched over the new shot — and the new files moved in, so a failed
    // refresh leaves the earlier full-colour shot in place.
    const tmp = fs.mkdtempSync(path.join(RAW, '.shot-'));
    try {
      const f = path.join(tmp, base);
      // An infinite or growing page reports a scrollHeight without end: tile at most 8 chunks
      // and log the boundary (the kit's cap), never one tile per chunk for ever.
      const MAXH = 8 * chunk;
      const hCap = Math.min(H, MAXH);
      if (H > MAXH) console.log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
      if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
      else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      for (const old of fs.readdirSync(RAW)) if (old === base + '.png' || old === base + '.png.capture.json' || (old.startsWith(base + '.part') && /\.part\d+\.png(\.capture\.json)?$/.test(old))) fs.rmSync(path.join(RAW, old));
      for (const n of fs.readdirSync(tmp)) fs.renameSync(path.join(tmp, n), path.join(RAW, n));
    } finally {
      fs.rmSync(tmp, { recursive: true, force: true });
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// Hovers one top-nav item so its ContentSubMenu opens (Framer opens them on hover).
async function navMenu(p, S) {
  // Next.js pages open one dropdown from the Developers or Resources button.
  // The Framer home has no such button; fall back to hovering the Developers link.
  const btn = p.getByRole('button', { name: /^developers$/i }).filter({ visible: true }).first();
  if (await btn.count()) {
    await btn.click();
    await wait(p, 900);
    await S.view('nav-submenu');
    await p.keyboard.press('Escape');
    await wait(p, 400);
    return;
  }
  const link = p.locator('a', { hasText: 'Developers' }).filter({ visible: true }).first();
  await link.hover().catch(() => {});
  await wait(p, 900);
  await S.view('nav-submenu');
  await p.mouse.move(20, 800);
  await wait(p, 400);
}

async function cookieSettings(p, S) {
  const manage = p.getByRole('button', { name: /manage cookies/i }).filter({ visible: true }).first();
  if (!(await manage.count())) return;
  await manage.click();
  await wait(p, 800);
  await S.view('cookie-settings');
  await p.keyboard.press('Escape');
  await wait(p, 400);
}

// Presses one persona chip under the hero demo ("sales Liv", "medical-services Talk with Mia",
// ...): a local tab that swaps which avatar the demo card shows. The chips are div[role=button],
// and the call buttons are never pressed.
async function persona(p, S) {
  const chip = p.locator('[role=button]').filter({ hasText: /sales|customer-support|skill-training|language-tutor|medical-services/i }).filter({ visible: true }).first();
  await chip.scrollIntoViewIfNeeded();
  await chip.click({ timeout: 8000 }).catch(() => chip.dispatchEvent('click'));
  await wait(p, 2500);
  await S.view('persona-tab');
}

const desktop = {
  home: { path: '/', promo: 'keep', run: async (p, S) => {
    await S.view('consent');                    // the cookie card as it first renders
    await step('cookie-settings', () => cookieSettings(p, S));
    await closePromo(p);                        // display:none, never a consent click
    await S.view('default');
    await S.full();
    await step('nav-submenu', () => navMenu(p, S));
    await step('persona-tab', () => persona(p, S));
  } },
  api: { path: '/api', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-submenu', () => navMenu(p, S));
    await step('billing-toggle', async () => {
      const t = p.locator('button, [role=switch], [role=tab]').filter({ hasText: /annual|yearly|monthly/i }).first();
      if (await t.count()) { await t.click(); await wait(p, 1500); await S.view('billing-toggle'); }
    });
  } },
  'interactive-avatars': { path: '/interactive-avatars', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  research: { path: '/research', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'case-studies': { path: '/case-studies', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  tools: { path: '/tools', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'cara-4-1': { path: '/cara-4-1', run: async (p, S) => { await S.view('default'); await S.full(); } },
  glossary: { path: '/resources/glossary', run: async (p, S) => { await S.view('default'); await S.full(); } },
  compare: { path: '/compare', run: async (p, S) => { await S.view('default'); await S.full(); } },
  guides: { path: '/resources/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  cookbook: { path: '/cookbook', run: async (p, S) => { await S.view('default'); await S.full(); } },
  governance: { path: '/ai-governance', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'get-demo': { path: '/get-demo', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('field-focused', async () => {
      const f = p.locator('input[type=text], input:not([type]), input[type=email]').filter({ visible: true }).first();
      await f.click();
      await wait(p, 600);
      await S.view('field-focused');
      await p.mouse.click(200, 60);
    });
  } },
  'docs-overview': { path: '/docs/introduction/overview', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('search', async () => {
      // The cookie dialog covers ⌘K. Hide it with display:none. Never Accept or Decline.
      await closePromo(p);
      const search = p.getByRole('button', { name: /open search/i }).first();
      if (await search.count()) await search.click();
      else await p.keyboard.press('ControlOrMeta+k');
      await wait(p, 900);
      await S.view('search-dialog');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    });
    await step('assistant', async () => {
      await p.keyboard.press('ControlOrMeta+i');
      await wait(p, 1500);
      await S.view('assistant-panel');
      await p.keyboard.press('Escape');
      await wait(p, 600);
    });
  } },
  'docs-api': { path: '/docs/api-reference/overview', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-dark': { path: '/docs/introduction/overview', wait: 7000, theme: 'dark', run: async (p, S) => {
    // "Change theme preference" opens a local menu; its Dark item switches the docs theme.
    const t = p.getByRole('button', { name: 'Change theme preference' }).first();
    if (await t.count()) {
      await t.click(); await wait(p, 1200);
      const dark = p.getByRole('menuitem', { name: /^dark$/i }).or(p.locator('[role=menu] *, [data-component-part*=item]').filter({ hasText: /^dark$/i })).first();
      if (await dark.count()) { await dark.click(); await wait(p, 1200); }
    }
    const isDark = await p.evaluate(() => document.documentElement.className.includes('dark') || document.documentElement.getAttribute('data-theme-preference') === 'dark');
    log('  docs dark?', isDark, await p.evaluate(() => document.documentElement.className + ' pref=' + document.documentElement.getAttribute('data-theme-preference')));
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', promo: 'keep', run: async (p, S) => {
    await S.view('consent');
    await closePromo(p);
    await S.view('default');
    await S.full();
    await step('nav-open', async () => {
      // Framer paints the hamburger as div[data-framer-name=Icon]. A synthetic
      // click does not open it; a real Playwright click does. Never click Sign in.
      const icon = p.locator('[data-framer-name="Icon"]').first();
      if (await icon.count()) {
        await icon.click({ force: true });
        await wait(p, 1000);
        await S.view('nav-open');
      }
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-open', async () => {
      const t = p.getByRole('button', { name: /open menu/i }).or(p.locator('header button').filter({ hasText: /menu/i })).first();
      if (await t.count()) { await t.click(); await wait(p, 900); await S.view('nav-open'); }
    });
  } },
  'docs-overview': { path: '/docs/introduction/overview', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme === 'dark' ? 'dark' : 'light'}`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
