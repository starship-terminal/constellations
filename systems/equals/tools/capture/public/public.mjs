// Captures Equals' public signed-out pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Equals' public
// surface is three sites: the equals.com marketing site (light only; no consent banner seen,
// no dark scheme in its stylesheet), the go.equals.com sign-in card (light) and the
// docs.equals.com Mintlify docs, which paints light and dark (captured in
// prefers-color-scheme contexts — never through its theme menu). Desktop shots are
// 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together; an
// unbounded page truncates at 8 chunks and the log records the boundary. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the header "Use cases"
// mega-menu trigger, a pricing FAQ question (checkbox accordion) and the guide's
// "Start reading" splash button; every "Get a demo" email capture and the sign-in form
// are shot and measured, never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP_BASE, DOCS_BASE } from './lib.mjs';

// Full-colour originals stay outside the repo (quantize.py writes screenshots/ from them).
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'equals', 'raw-shots');
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

// The "Use cases" mega-menu: a header__menu-trigger button toggles
// .header__menu--use-cases open. A local UI toggle; its links are never followed.
async function openUseCasesMenu(p) {
  const trig = p.locator('button.header__menu-trigger').filter({ visible: true }).first();
  if (!(await trig.count())) return;
  await clickEl(trig);
  await p.waitForTimeout(1200);
}

// A pricing FAQ item: .faq__question labels toggle a hidden checkbox — a local
// accordion, never a form post.
async function openFaq(p) {
  const q = p.locator('label.faq__question').filter({ visible: true }).first();
  if (!(await q.count())) return;
  await q.evaluate((el) => el.scrollIntoView({ block: 'center' }));
  await p.waitForTimeout(400);
  await clickEl(q);
  await p.waitForTimeout(900);
}

// The guide splash: Guide__SplashButton dismisses the full-page splash
// (body.splash-active -> content). A local UI toggle, never a submission.
async function dismissSplash(p) {
  const b = p.locator('button.Guide__SplashButton').filter({ visible: true }).first();
  if (!(await b.count())) return;
  await clickEl(b);
  await p.waitForTimeout(1200);
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await openUseCasesMenu(p);
      await S.view('menu');
      await p.keyboard.press('Escape');
      await p.locator('body').click({ position: { x: 700, y: 500 }, timeout: 2000 }).catch(() => {});
      await wait(p, 700);
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      await openFaq(p);
      await S.view('faq-open');
    });
    await S.full();
  } },
  usecase: { url: BASE + '/use-cases/arr-dashboard/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  usecases: { url: BASE + '/use-cases/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { url: BASE + '/customers/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  launches: { url: BASE + '/launches/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  guide: { url: BASE + '/guides/saas-metrics/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('splash');
    await step('reading', async () => {
      await dismissSplash(p);
      await S.view('default');
      await S.full();
    });
  } },
  signin: { url: APP_BASE + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  docs: { url: DOCS_BASE + '/docs/getting-started', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-dark': { url: DOCS_BASE + '/docs/getting-started', wait: 8000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-spreadsheet': { url: DOCS_BASE + '/docs/how-to-spreadsheet', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-spreadsheet-dark': { url: DOCS_BASE + '/docs/how-to-spreadsheet', wait: 8000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-charts': { url: DOCS_BASE + '/docs/charts', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The mobile nav is a label.hamburger toggling a hidden checkbox.
      const ham = p.locator('label.header__mobile-nav-toggle, .header__hamburger').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 1200);
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  usecase: { url: BASE + '/use-cases/arr-dashboard/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signin: { url: APP_BASE + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  'docs-dark': { url: DOCS_BASE + '/docs/getting-started', wait: 8000, theme: 'dark', scheme: 'dark', run: async (p, S) => {
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