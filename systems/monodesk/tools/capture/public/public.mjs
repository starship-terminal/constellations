// Captures MonoDesk's public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/monodesk/raw-shots PLAYWRIGHT=... node public.mjs [page,page]
//
// Names are {page}-dark-{state}.png. The marketing shell paints one dark theme.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Full pages tile at 8 chunks max.
// Nothing is submitted. Login and signup URLs are recorded and not entered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, isWall, hideOverlays, dismissDesktopPrompt } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'monodesk', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
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
    await wait(p, 200);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function visible(locator) {
  const n = await locator.count();
  for (let i = 0; i < n; i++) if (await locator.nth(i).isVisible().catch(() => false)) return locator.nth(i);
  return null;
}

const shell = async (p, S, extra) => {
  await dismissDesktopPrompt(p);
  await S.view('default');
  if (extra) await extra(p, S);
  await S.full();
};

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await dismissDesktopPrompt(p);
    await S.view('default');
    await step('faq', async () => {
      const q = await visible(p.locator('button.faq-question').filter({ hasText: 'What is MonoDesk?' }));
      if (!q) return;
      await q.click();
      await wait(p, 400);
      await S.view('faq');
    });
    await step('quote', async () => {
      const d = await visible(p.getByRole('button', { name: 'Show quote 2' }));
      if (!d) return;
      await d.click();
      await wait(p, 400);
      await S.view('quote-2');
    });
    await step('pillar', async () => {
      const el = p.locator('[aria-expanded="false"]').filter({ hasText: /Project management/ }).first();
      if (!(await el.count()) || !(await el.isVisible().catch(() => false))) return;
      await el.click();
      await wait(p, 400);
      await S.view('pillar-projects');
    });
    await step('video', async () => {
      const b = await visible(p.locator('button.video-modal-trigger'));
      if (!b) return;
      await b.click();
      await wait(p, 800);
      await S.view('video-dialog');
      await p.keyboard.press('Escape').catch(() => {});
      const close = await visible(p.locator('button.video-modal-close'));
      if (close) await close.click().catch(() => {});
      await wait(p, 300);
    });
    await S.full();
  } },
  features: { path: '/features', run: shell },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('table', async () => {
      const t = await visible(p.locator('button.ptable-toggle'));
      if (!t) return;
      await t.click();
      await wait(p, 500);
      await S.view('table-open');
    });
    await step('faq', async () => {
      const q = await visible(p.locator('button.faq-question').first());
      if (!q) return;
      await q.click();
      await wait(p, 400);
      await S.view('faq');
    });
    await S.full();
  } },
  about: { path: '/about-us', run: shell },
  help: { path: '/help', run: async (p, S) => {
    await S.view('default');
    await step('search-focus', async () => {
      const input = p.locator('input[type="search"]').first();
      if (!(await input.count())) return;
      await input.focus();
      await wait(p, 300);
      await S.view('search-focused');
      await input.blur();
    });
    await S.full();
  } },
  'help-start': { path: '/help/getting-started', run: shell },
  'help-article': { path: '/help/getting-started/what-is-monodesk', run: shell },
  blog: { path: '/blog', run: shell },
  'blog-post': { path: '/blog/meet-your-co-worker', run: shell },
  alternatives: { path: '/alternatives', run: shell },
  'alt-notion': { path: '/alternatives/notion', run: shell },
  audiences: { path: '/for-creative-pros', run: shell },
  freelancers: { path: '/for-creative-pros/freelancers', run: shell },
  'feature-today': { path: '/features/today', run: shell },
  'feature-projects': { path: '/features/projects', run: shell },
  'feature-invoices': { path: '/features/invoices', run: shell },
  terms: { path: '/terms', run: shell },
  campaign: { path: '/admin-sorted', run: shell },
  playground: { path: '/playground', run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      const b = await visible(p.locator('button.pg-nav-btn'));
      if (!b) return;
      await b.click();
      await wait(p, 400);
      await S.view('nav-open');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  'pg-magic8': { path: '/playground/magic8', run: shell },
  'pg-invoice': { path: '/playground/invoice-generator', run: shell },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('prompt');
    await dismissDesktopPrompt(p);
    await S.view('default');
    await step('menu', async () => {
      const b = await visible(p.locator('button.hamburger-btn'));
      if (!b) return;
      await b.click();
      await wait(p, 500);
      await S.view('menu');
      const more = await visible(p.locator('a.mobile-nav-parent, a').filter({ hasText: /^More$/ }));
      if (more) {
        await more.click();
        await wait(p, 400);
        await S.view('menu-more');
      }
      await b.click().catch(() => {});
      await wait(p, 300);
    });
    await step('faq', async () => {
      const q = await visible(p.locator('button.faq-question').filter({ hasText: 'What is MonoDesk?' }));
      if (!q) return;
      await q.scrollIntoViewIfNeeded();
      await q.click();
      await wait(p, 400);
      await S.view('faq');
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await dismissDesktopPrompt(p);
    await S.view('default');
    await step('menu', async () => {
      const b = await visible(p.locator('button.hamburger-btn'));
      if (!b) return;
      await b.click();
      await wait(p, 500);
      await S.view('menu');
    });
    await S.full();
  } },
  features: { path: '/features', run: async (p, S) => { await dismissDesktopPrompt(p); await S.view('default'); await S.full(); } },
  help: { path: '/help', run: async (p, S) => { await dismissDesktopPrompt(p); await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await dismissDesktopPrompt(p); await S.view('default'); await S.full(); } },
  playground: { path: '/playground', run: async (p, S) => { await dismissDesktopPrompt(p); await S.view('default'); await S.full(); } },
  about: { path: '/about-us', run: async (p, S) => { await dismissDesktopPrompt(p); await S.view('default'); await S.full(); } },
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
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-dark`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1600);
    if (isWall(p.url())) {
      log('  WALL', p.url(), 'status', res?.status());
    } else {
      await hideOverlays(p);
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, String(e.message).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
