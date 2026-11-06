// Captures Refero's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Two surfaces, both public:
//   refero.design          home, /search, /apps/search (iOS), /pricing, /mcp
//   styles.refero.design   the card gallery + the first /style/<id> entity page
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Both sites ship one light
// theme, so there is no dark run. Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together. Nothing is sent, created or signed into: the only presses are
// the promo dismissals (the MCP card's Close, the research coach's X) and hovering a styles card so
// its scroll-preview video loads.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, STYLES } from './lib.mjs';

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
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < H; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

// The first /style/<id> href the styles index lists, used by the entity run.
async function styleHref(p) {
  const href = await p.evaluate(() => {
    const a = [...document.querySelectorAll('a[href^="/style/"]')].find((x) => x.getBoundingClientRect().width > 100);
    return a && a.getAttribute('href');
  });
  if (!href) throw new Error('no /style/ link on the index');
  return href;
}

const desktop = {
  home: { url: BASE + '/', promo: 'keep', run: async (p, S) => {
    await S.view('promo');
    await closePromo(p);
    await S.view('default');
    await S.full();
    await step('research-focused', async () => {
      const ta = p.locator('textarea, [contenteditable=true]').first();
      await ta.click(); await wait(p, 800);
      await S.view('research-focused');
      await p.mouse.click(1300, 780);
    });
  } },
  search: { url: BASE + '/search', run: async (p, S) => { await S.view('default'); await S.full(); } },
  apps: { url: BASE + '/apps/search', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  mcp: { url: BASE + '/mcp', run: async (p, S) => { await S.view('default'); await S.full(); } },
  styles: { url: STYLES + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('card-hover', async () => {
      const card = p.locator('a[href^="/style/"]').filter({ visible: true }).first();
      await card.scrollIntoViewIfNeeded();
      await card.hover(); await wait(p, 3500);
      await S.view('card-hover');
    });
  } },
  'styles-entity': { url: STYLES + '/', run: async (p, S) => {
    const href = await styleHref(p);
    await p.goto(STYLES + href, { waitUntil: 'load', timeout: 90000 });
    await wait(p, 7000); // the entity video buffers, then fades in over the poster
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', promo: 'keep', run: async (p, S) => { await S.view('promo'); await closePromo(p); await S.view('default'); await S.full(); } },
  search: { url: BASE + '/search', run: async (p, S) => { await S.view('default'); await S.full(); } },
  styles: { url: STYLES + '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'load', timeout: 90000 });
    await wait(p, spec.wait || 6000);
    if (spec.promo !== 'keep') await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
