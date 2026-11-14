// Captures Exa's public signed-out pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Exa's public
// surface is three sites: the exa.ai marketing site (light only — its one
// prefers-color-scheme:dark rule is a single utility class, not a theme), the
// Mintlify docs under exa.ai/docs, which paints light and dark (captured in
// prefers-color-scheme contexts — never through its theme menu), and the
// auth.exa.ai login card that dashboard.exa.ai redirects to (light only).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8 chunks
// and the log records the boundary. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the header's hover mega-menus, the
// home demo's latency/category/output pills (which only switch the widget's
// request preview, never fire it), pricing's use-case pills, docs' code tabs
// and the mobile "Toggle menu" button. The demo's "Run preview" arrow, every
// Get-started/Sign-up button and the login form are shot and measured, never
// pressed or submitted. websets.exa.ai returns 429 to headless browsers and
// is a documented boundary.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, hoverNavMenu, chromium, UA, UA_MOBILE, BASE, DOCS_BASE, AUTH_BASE } from './lib.mjs';

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

// A local pill inside the home demo widget (latency, category, output) — it
// only re-configures the preview; it never fires a request. The "Run preview"
// arrow is never pressed.
async function demoPill(p, text) {
  const b = await p.evaluate((want) => {
    const el = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim().replace(/\s+/g, ' ') === want && x.getBoundingClientRect().width > 0);
    if (!el) return false;
    el.click();
    return true;
  }, text);
  await p.waitForTimeout(900);
  return b;
}

const desktop = {
  home: { url: BASE + '/', wait: 10000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      if (await hoverNavMenu(p, 'Products')) await S.view('menu');
      await p.mouse.move(720, 500);
      await p.keyboard.press('Escape');
      await wait(p, 700);
    });
    await step('demo-deep', async () => {
      await p.evaluate(() => scrollTo(0, 200));
      await demoPill(p, 'Deep ~10s');
      await demoPill(p, 'News');
      await S.view('demo-tabs');
      await demoPill(p, 'Auto 1s');
      await demoPill(p, 'Full Web');
      await p.evaluate(() => scrollTo(0, 0));
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('usecase-pill', async () => {
      const b = await p.evaluate(() => {
        const el = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim() === 'Chatbots' && x.getBoundingClientRect().width > 0);
        if (!el) return false;
        el.scrollIntoView({ block: 'center' });
        el.click();
        return true;
      });
      if (b) { await wait(p, 900); await S.view('usecase-chatbots'); await p.evaluate(() => scrollTo(0, 0)); }
    });
    await S.full();
  } },
  product: { url: BASE + '/products/search', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  demos: { url: BASE + '/demos', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  evals: { url: BASE + '/evals', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  brand: { url: BASE + '/brand', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { url: BASE + '/customers', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  versus: { url: BASE + '/versus', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: AUTH_BASE, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  websets: { url: 'https://websets.exa.ai/websets', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  docs: { url: DOCS_BASE, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('code-tab', async () => {
      const b = await p.evaluate(() => {
        const el = [...document.querySelectorAll('button, [role="tab"]')].find((x) => (x.innerText || '').trim() === 'JavaScript' && x.getBoundingClientRect().width > 0);
        if (!el) return false;
        el.click();
        return true;
      });
      if (b) { await wait(p, 800); await S.view('code-js'); }
    });
    await S.full();
  } },
  'docs-dark': { url: DOCS_BASE, wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-ref': { url: DOCS_BASE + '/quickstart', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      const t = p.locator('button[aria-label="Toggle menu"], button:has-text("Toggle menu")').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1200);
      await S.view('drawer');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: AUTH_BASE, wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'docs-dark': { url: DOCS_BASE, wait: 9000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
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
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: spec.scheme || 'light' });
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
