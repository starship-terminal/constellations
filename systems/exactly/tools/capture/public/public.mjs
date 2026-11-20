// Captures exactly.ai's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. exactly.ai is a
// Framer-published site that paints light on every surface: the photo-hero home page, the
// marketing offers at /pricing, the brand gallery at /showcase (+ /showcase/<brand>), the
// /case-studies index + articles, /industries (+ per-industry pages), the doc-style
// /help-center (+ collections and articles) and /book-a-demo with its embedded scheduler.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back
// together; an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the
// mobile "Mobile menu toggle" hamburger and the help-center "Search…" trigger (it opens
// the Framer search modal; nothing typed is submitted). The Gleap support bubble and the
// scheduler's cookie line are hidden, never answered.
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
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  showcase: { url: BASE + '/showcase', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'showcase-brand': { url: BASE + '/showcase/revolut', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'case-studies': { url: BASE + '/case-studies', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'case-study': { url: BASE + '/case-studies/how-indrive-scales-global-brand-assets-at-the-speed-of-mobility-with-exactly-ai', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  industries: { url: BASE + '/industries', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  industry: { url: BASE + '/industries/saas-n-mobile-apps', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'help-center': { url: BASE + '/help-center', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      // "Search…" is a fake field that opens the Framer search modal — a local
      // UI toggle; nothing typed is submitted.
      const t = p.locator('p').filter({ hasText: /^\s*Search…\s*$/ }).filter({ visible: true }).last();
      if (!(await t.count())) return;
      // A transparent <button> covers the fake field: click its centre.
      await t.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await wait(p, 500);
      const bb = await t.boundingBox();
      if (bb) await p.mouse.click(bb.x + bb.width / 2, bb.y + bb.height / 2);
      await wait(p, 1200);
      await S.view('search');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  'help-faq': { url: BASE + '/help-center/frequently-asked-questions', wait: 9000, theme: 'light', run: async (p, S) => {
    // The FAQ page is a doc article: questions are anchor-linked H3s with
    // answers below, not an accordion. Nothing toggles here.
    await S.view('default');
    await S.full();
  } },
  'book-a-demo': { url: BASE + '/book-a-demo', wait: 12000, theme: 'light', run: async (p, S) => {
    // The scheduler is a Calendly embed: measured at rest, no day or time picked.
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The hamburger is the div labelled "Mobile menu toggle"; it opens the
      // full-viewport nav overlay. A local UI toggle; its links are never followed.
      const ham = p.locator('div[aria-label="Mobile menu toggle"]').filter({ visible: true }).last();
      if (!(await ham.count())) return;
      await clickEl(ham);
      await wait(p, 1500);
      await S.view('drawer');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 9000, theme: 'light', run: async (p, S) => {
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
