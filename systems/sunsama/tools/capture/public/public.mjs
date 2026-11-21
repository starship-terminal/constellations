// Captures Sunsama's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. *-full shots are 1x.
// The site paints one theme (color-scheme: normal). There is no dark run.
//
// Nothing is signed into, typed, or submitted. Termly consent is hidden,
// never accepted. Login, Google, Outlook, SSO, and the signup email form
// are not used. See site-tree.md for which control opens which page.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, patch } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const simple = (path) => ({ path, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('ai-panel', async () => {
      await p.locator('button.ss-pill').first().click();
      await wait(p, 700);
      await S.view('ai-panel');
      await p.locator('button.ss-panel_tile').filter({ hasText: 'ChatGPT' }).first().click();
      await wait(p, 400);
      await S.view('ai-chatgpt');
      await p.locator('button.ss-panel_close').click();
      await wait(p, 300);
    });
    await step('slider', async () => {
      await p.locator('.sliderarrow.w-slider-arrow-right').first().click();
      await wait(p, 600);
      await S.view('slider-next');
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const h = p.getByText('Frequently Asked', { exact: false }).first();
      await h.scrollIntoViewIfNeeded();
      await wait(p, 400);
      await S.view('faq');
    });
    await S.full();
  } },
  love: simple('/love'),
  about: { path: '/about', run: async (p, S) => {
    await S.view('default');
    await step('slider', async () => {
      await p.locator('.about_right-arrow').first().click();
      await wait(p, 500);
      await S.view('slider-next');
    });
    await S.full();
  } },
  blog: simple('/blog'),
  'blog-articles': simple('/blog-categories/articles'),
  compare: { path: '/compare', run: async (p, S) => {
    await S.view('default');
    await step('motion-tab', async () => {
      await p.locator('.compare_tab-link').nth(1).click();
      await wait(p, 500);
      await S.view('motion-tab');
    });
    await S.full();
  } },
  desktop: simple('/desktop'),
  mobile: simple('/mobile'),
  'feature-planning': { path: '/features/daily-planning', run: async (p, S) => {
    await S.view('default');
    await step('demo', async () => {
      const b = p.locator('.ap-demo_go').first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 800);
      await S.view('demo');
    });
    await S.full();
  } },
  'feature-focus': simple('/features/focus-mode'),
  'feature-timeboxing': simple('/features/timeboxing'),
  'feature-ai': simple('/features/ai'),
  integration: { path: '/integrations/asana', run: async (p, S) => {
    await S.view('default');
    await step('lightbox', async () => {
      const b = p.locator('.integration_lightbox-link, .w-lightbox').first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 900);
      await S.view('lightbox');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  'role-executives': simple('/role/executives'),
  'team-design': simple('/team/design'),
  'protips': { path: '/pro-tips', run: async (p, S) => {
    await S.view('default');
    await step('categories', async () => {
      await p.locator('.pt-select__button').click();
      await wait(p, 400);
      await S.view('categories');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  'for-adhd': simple('/for-adhd'),
  privacy: simple('/privacy'),
  terms: simple('/terms'),
  // Signup wall only. No email typed. No submit.
  signup: { path: '/start/signup', run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('.menu-button-2').click();
      await wait(p, 600);
      await S.view('menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await S.full();
  } },
  pricing: simple('/pricing'),
  blog: simple('/blog'),
  compare: simple('/compare'),
  signup: { path: '/start/signup', run: async (p, S) => { await S.view('wall'); } },
};

const browser = await chromium.launch();
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2200);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
