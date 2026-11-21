// Captures MasterClass public pages. Nothing is submitted. Login and signup
// walls are recorded as a URL and that branch stops. Google and Apple are
// never clicked. Newsletter, profile, birthday, plan and quiz fields are
// never filled.
//
//   PLAYWRIGHT=... node public.mjs [page,page]
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hidePromo, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'masterclass', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('promo');
    await hidePromo(p);
    await S.view('default');
    await S.full();
    await step('browse', async () => {
      await p.getByRole('button', { name: 'Browse', exact: true }).click();
      await wait(p, 700);
      await S.view('browse');
      const food = p.getByRole('button', { name: 'Food & Drink', exact: true }).first();
      if (await food.count()) {
        await food.click();
        await wait(p, 600);
        await S.view('browse-food');
      }
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('search', async () => {
      await p.locator('#searchInput').click();
      await wait(p, 700);
      await S.view('search');
      await p.keyboard.press('Escape');
    });
    await step('trailer', async () => {
      const b = p.getByRole('button', { name: 'Watch Trailer' }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 1600);
        await S.view('trailer');
        await p.keyboard.press('Escape');
      }
    });
    await step('faq', async () => {
      const b = p.getByRole('button', { name: 'What is MasterClass?' }).first();
      if (await b.count()) {
        await b.scrollIntoViewIfNeeded();
        await b.click();
        await wait(p, 500);
        await S.view('faq');
      }
    });
  } },
  categories: { path: '/categories', run: async (p, S) => { await hidePromo(p); await S.view('default'); await S.full(); } },
  culinary: { path: '/categories/culinary', run: async (p, S) => { await hidePromo(p); await S.view('default'); await S.full(); } },
  class: { path: '/classes/gordon-ramsay-teaches-cooking', run: async (p, S) => {
    await hidePromo(p);
    await S.view('default');
    await S.full();
    await step('lesson-plan', async () => {
      const b = p.getByRole('button', { name: /View lesson plan/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 800); await S.view('lesson-plan'); }
    });
    await step('sample', async () => {
      const b = p.getByRole('button', { name: 'Sample', exact: true }).first();
      if (await b.count()) { await b.click(); await wait(p, 1200); await S.view('sample'); await p.keyboard.press('Escape'); }
    });
  } },
  session: { path: '/sessions/classes/design-stunning-floral-arrangements', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  gift: { path: '/gift', run: async (p, S) => {
    await hidePromo(p);
    await S.view('default');
    await step('chip', async () => {
      const b = p.getByRole('button', { name: 'Foodies', exact: true }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('chip'); }
    });
  } },
  promotion: { path: '/promotion', run: async (p, S) => { await hidePromo(p); await S.view('default'); await S.full(); } },
  checkout: { path: '/checkout', run: async (p, S) => { await hidePromo(p); await S.view('default'); await S.full(); } },
  quiz: { path: '/find-my-classes', run: async (p, S) => { await S.view('default'); } },
  certificates: { path: '/certificates', run: async (p, S) => { await S.view('default'); await S.full(); } },
  certificate: { path: '/certificates/ai-fundamentals-think-create-and-work-smarter', run: async (p, S) => { await S.view('default'); } },
  executive: { path: '/executive', run: async (p, S) => { await S.view('default'); await S.full(); } },
  business: { path: '/for-business', run: async (p, S) => { await S.view('default'); await S.full(); } },
  articles: { path: '/articles', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  article: { path: '/articles/ron-finley-how-to-grow-potatoes-in-a-sack-like-a-gangsta', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  help: { path: '/help-center', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  helparticle: { path: '/help-center/masterclass/answers/requesting-a-refund--id--ffUda_F-TPqkca5o9hJc5g', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  newsroom: { path: '/newsroom', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  sitemap: { path: '/sitemap', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  notfound: { path: '/this-page-is-not-a-real-masterclass-route', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/auth/login', run: async (p, S) => {
    // Wall only. Do not click Google, Apple, or any identity provider. Do not type.
    await S.view('wall');
    log('  login url', p.url());
  } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await hidePromo(p);
    await S.view('default');
    await S.full();
    await step('browse', async () => {
      await p.getByRole('button', { name: 'Browse', exact: true }).click();
      await wait(p, 700);
      await S.view('browse');
      await p.keyboard.press('Escape');
    });
    await step('menu', async () => {
      const menu = p.getByRole('button', { name: 'Menu', exact: true }).first();
      if (await menu.count()) {
        await menu.click();
        await wait(p, 700);
        await S.view('menu');
        await p.keyboard.press('Escape');
      }
    });
  } },
  login: { path: '/auth/login', run: async (p, S) => {
    await S.view('wall');
    log('  login url', p.url());
  } },
  categories: { path: '/categories', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  class: { path: '/classes/gordon-ramsay-teaches-cooking', run: async (p, S) => { await hidePromo(p); await S.view('default'); await S.full(); } },
  gift: { path: '/gift', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  checkout: { path: '/checkout', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
  certificates: { path: '/certificates', run: async (p, S) => { await S.view('default'); } },
  business: { path: '/for-business', run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help-center', run: async (p, S) => { await hidePromo(p); await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    await open(p, BASE + spec.path, { wait: spec.wait || 2800 });
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
