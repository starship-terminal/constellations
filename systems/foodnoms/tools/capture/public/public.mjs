// Captures foodnoms.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix and dark runs a
// `dark-` prefix. foodnoms.com is a Framer-published marketing site that paints both light
// and dark through a real (prefers-color-scheme: dark) media rule — the dark runs emulate
// the scheme in the browser context, the same mechanism a visitor's dark OS gets, so they
// are the site's authored theme, not a reconstruction. Routes: / (hero ticker, feature
// cards, values, review marquee, CTA, footer), /plus (Free vs Foodnoms+ comparison table),
// /help (search modal + Closed/Open accordions), /news (+ newsletter form and article
// cards), /press, /family-plan and /vs/myfitnesspal (article pages), a /help/* and a
// /news/* article, /terms, /privacy, and the /open/settings/sign-up interstitial. /download
// is skipped: it is a JS redirect to apps.apple.com. Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary (/terms is ~18k px and tiles).
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the
// help "Search" trigger (opens the Framer search modal; nothing typed is submitted), the
// help "About Foodnoms" accordion header, and the mobile "Open navigation menu" button.
// The newsletter form and every Download/App-Store link are measured, never activated.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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

const desktop = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  plus: { url: BASE + '/plus', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { url: BASE + '/help', wait: 8000, run: async (p, S) => {
    await step('search', async () => {
      // "Search" opens the Framer search modal — a local UI toggle; nothing
      // typed is submitted.
      const t = p.locator('[data-framer-name="Variant 1"]').filter({ hasText: /^\s*Search\s*$/ }).filter({ visible: true }).first();
      if (!(await t.count())) return;
      await t.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 500);
      const bb = await t.boundingBox();
      if (bb) await p.mouse.click(bb.x + bb.width / 2, bb.y + bb.height / 2);
      await wait(p, 1200);
      await S.view('search');
      await p.keyboard.press('Escape').catch(() => {});
      await wait(p, 600);
    });
    await step('accordion', async () => {
      // The section Header (tabindex=0, data-highlight) toggles the Framer
      // accordion Closed -> Open.
      const h = p.locator('[data-framer-name="Closed"] [data-framer-name="Header"]').filter({ visible: true }).first();
      if (!(await h.count())) return;
      await h.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 400);
      await clickEl(h);
      await wait(p, 900);
      await S.view('accordion-open');
      // close it again so the full shot shows the resting state
      await clickEl(p.locator('[data-framer-name="Open"] [data-framer-name="Header"]').filter({ visible: true }).first()).catch(() => {});
      await wait(p, 600);
    });
    // The search and accordion steps scrolled the page; the default view
    // must start at the top (its sidecar records scroll.y).
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 600);
    await S.view('default');
    await S.full();
  } },
  news: { url: BASE + '/news', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  press: { url: BASE + '/press', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'family-plan': { url: BASE + '/family-plan', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'vs-mfp': { url: BASE + '/vs/myfitnesspal', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'help-article': { url: BASE + '/help/barcode-scanning', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'news-article': { url: BASE + '/news/foodnoms-2', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: BASE + '/terms', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy', wait: 7000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'open-signup': { url: BASE + '/open/settings/sign-up', wait: 7000, run: async (p, S) => {
    await S.view('default');
  } },
};

// Dark runs emulate prefers-color-scheme: the site's own stylesheets repaint
// under the media rule, so these show the theme a dark-system visitor sees —
// not a forced class on a copy.
const darkRuns = {
  home: desktop.home,
  plus: desktop.plus,
  help: desktop.help,
  news: desktop.news,
  'help-article': desktop['help-article'],
  'vs-mfp': desktop['vs-mfp'],
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The "Open navigation menu" button opens the full-viewport nav
      // overlay. A local UI toggle; its links are never followed.
      const ham = p.locator('button[aria-label="Open navigation menu"]').filter({ visible: true }).first();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  plus: { url: BASE + '/plus', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { url: BASE + '/help', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, dark: false })),
  ...Object.keys(darkRuns).map((k) => ({ k, mob: false, dark: true })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, dark: false })),
];
for (const { k, mob, dark } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes((dark ? 'dark-' : '') + name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = dark ? 'dark' : 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: theme });
  await patch(ctx);
  const p = await ctx.newPage();
  log((dark ? 'dark ' : '') + name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, spec.url);
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
