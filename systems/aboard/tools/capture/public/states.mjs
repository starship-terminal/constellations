// Captures every reachable public state named in systems/aboard/site-tree.md.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/public/states.mjs [name,name,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Names are {page}-light-{state}.png
// with a mobile- prefix at phone width. One light theme. Nothing is submitted:
// newsletter, event and contact fields are never typed into, CookieYes is never
// answered, and sign.aboard.com is never opened.
//
// A page taller than one GPU texture is saved as name.partN.png tiles.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 8 * 14000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async shot(name, opts = {}) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, ...opts }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async view(name) { await closePromo(this.p); await this.shot(name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // screenshotWithMetadata rejects a full-page PNG whose height is 2px off
    // documentSize (scrollbar rounding). Fall back to a plain full-page shot
    // and record the mismatch in the sidecar ourselves.
    const takeFull = async (path, clip) => {
      const opts = clip ? { path, fullPage: true, clip } : { path, fullPage: true };
      try { await screenshotWithMetadata(p, opts, this.requested); }
      catch (e) {
        if (!/dimension mismatch/i.test(String(e.message || e))) throw e;
        await p.screenshot(opts);
        log('  dim-fallback', path.split('/').pop());
      }
    };
    if (H <= chunk) await takeFull(f + '.png');
    else {
      const tiles = Math.min(8, Math.ceil(H / chunk));
      for (let i = 0; i < tiles; i++) {
        const y = i * chunk;
        await takeFull(`${f}.part${i}.png`, { x: 0, y, width: this.vw, height: Math.min(chunk, H - y) });
      }
      if (H > tiles * chunk) log('  truncated', this.prefix, name, 'H=' + H);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function hideCookies(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('.cky-consent-container, .cky-modal, #ckyPreferenceCenter')) {
      el.style.setProperty('display', 'none', 'important');
    }
  });
}

async function showBanner(p) {
  await p.evaluate(() => {
    const el = document.querySelector('.cky-consent-container');
    if (el) { el.style.display = ''; el.style.removeProperty('display'); }
  });
}

const PAGES = [
  ['home', '/'],
  ['how-we-work', '/how-we-work/'],
  ['case-studies', '/case-studies/'],
  ['case-study', '/case-studies/city-of-boston-scheduling-app/'],
  ['case-study-sagesure', '/case-studies/sagesure-policy-logic-central/'],
  ['foundry', '/foundry/'],
  ['perspectives', '/perspectives/'],
  ['perspectives-page-2', '/perspectives/?pg=2'],
  ['newsletter', '/newsletter/'],
  ['newsletter-page-2', '/newsletter/page/2/'],
  ['podcast', '/podcast/'],
  ['podcast-page-2', '/podcast/page/2/'],
  ['podcast-episode', '/podcast/jason-goldman-from-vc-pitches-to-ai-kill-switches/'],
  ['events', '/events/'],
  ['media', '/media/'],
  ['about', '/about/'],
  ['faq', '/faq/'],
  ['careers', '/careers/'],
  ['security', '/security/'],
  ['whitepaper', '/resources/how-to-utilize-ai-agents-to-actually-deliver-results/'],
  ['essay', '/welcome-to-the-age-of-receipts/'],
  ['aboard-sign', '/meet-aboard-sign/'],
  ['tag', '/tag/ai/'],
  ['author', '/author/paul-ford/'],
];

async function interactions(p, S, key, mobile) {
  if (key === 'home') {
    if (!mobile) {
      await showBanner(p);
      await wait(p, 400);
      await S.shot('cookie-banner');
      await hideCookies(p);
    }
    await S.view('default');
    await step('carousel-tick', async () => {
      const tick = p.locator('.cc-tick').nth(2);
      if (await tick.count()) { await tick.click({ timeout: 4000 }); await wait(p, 700); await S.view('carousel-tick'); }
    });
    await step('carousel-paused', async () => {
      const pause = p.locator('.cc-pause');
      if (await pause.count()) { await pause.click({ timeout: 4000 }); await wait(p, 400); await S.view('carousel-paused'); }
    });
    await step('chip-podcast', async () => {
      const chip = p.locator('.rd-chip', { hasText: 'Podcast' }).first();
      if (await chip.count()) { await chip.click({ timeout: 4000 }); await wait(p, 500); await S.view('chip-podcast'); }
    });
    await step('contact', async () => {
      await p.evaluate(() => document.querySelector('#contact')?.scrollIntoView({ block: 'start' }));
      await wait(p, 800);
      await S.view('contact');
      await p.evaluate(() => scrollTo(0, 0));
    });
    if (!mobile) {
      await step('nav-perspectives', async () => {
        const link = p.locator('header a, .site-header a').filter({ hasText: /^Perspectives$/ }).first();
        if (await link.count()) { await link.hover(); await wait(p, 500); await S.view('nav-perspectives'); }
      });
      await step('nav-about', async () => {
        const link = p.locator('header a, .site-header a').filter({ hasText: /^About$/ }).first();
        if (await link.count()) { await link.hover(); await wait(p, 500); await S.view('nav-about'); }
      });
    }
    if (mobile) {
      await step('menu-open', async () => {
        const btn = p.locator('.rd-nav-toggle').first();
        if (await btn.count()) { await btn.click({ timeout: 4000 }); await wait(p, 700); await S.view('menu-open'); }
      });
    }
    await S.full();
    return;
  }
  if (key === 'faq') {
    await S.view('default');
    await step('faq-open', async () => {
      const opened = await p.evaluate(() => {
        const el = [...document.querySelectorAll('button.faq-q')].find((b) => b.getBoundingClientRect().height > 10);
        if (!el) return false;
        el.click();
        return true;
      });
      if (opened) { await wait(p, 400); await S.view('faq-open'); }
    });
    await S.full();
    return;
  }
  if (key === 'foundry') {
    await S.view('default');
    await step('foundry-image', async () => {
      const btn = p.getByRole('button', { name: /Open image 2 of/ }).first();
      if (await btn.count()) { await btn.click({ timeout: 4000 }); await wait(p, 500); await S.view('image-open'); }
    });
    await step('foundry-more', async () => {
      // The gallery button sits well below the fold, and Playwright's click
      // times out on it. A DOM click expands the panel (aria-expanded flips
      // true, then the script collapses it), so the shot is taken in the
      // same turn as the click, before the collapse.
      const opened = await p.evaluate(() => {
        const el = document.querySelector('button.rd-media-show');
        if (!el) return false;
        el.scrollIntoView({ block: 'center' });
        el.click();
        return el.getAttribute('aria-expanded');
      });
      if (opened) await S.view('show-more');
    });
    await S.full();
    return;
  }
  if (key === 'perspectives') {
    await S.view('default');
    await step('chip', async () => {
      const chip = p.getByRole('button', { name: /^Newsletter/ }).first();
      if (await chip.count()) { await chip.click({ timeout: 4000 }); await wait(p, 500); await S.view('chip-newsletter'); }
    });
    await S.full();
    return;
  }
  if (key === 'podcast') {
    await S.view('default');
    await step('player', async () => {
      const play = p.locator('.rd-pd-play').first();
      if (await play.count()) { await play.click({ timeout: 4000 }); await wait(p, 900); await S.view('player-open'); }
    });
    await S.full();
    return;
  }
  if (key === 'events') {
    await S.view('default');
    await step('event-anchor', async () => {
      await p.evaluate(() => {
        const a = document.querySelector('a[href*="#event-"]');
        if (a) a.click();
      });
      await wait(p, 500);
      await S.view('event-open');
    });
    await S.full();
    return;
  }
  if (key === 'media') {
    await S.view('default');
    await step('show-more', async () => {
      const more = p.getByRole('button', { name: 'Show more' }).first();
      if (await more.count()) { await more.click({ timeout: 4000 }); await wait(p, 600); await S.view('show-more'); }
    });
    await S.full();
    return;
  }
  if (key === 'careers') {
    await S.view('default');
    await step('positions', async () => {
      await p.evaluate(() => document.querySelector('#open-positions')?.scrollIntoView({ block: 'start' }));
      await wait(p, 500);
      await S.view('positions');
    });
    await S.full();
    return;
  }
  if (key === 'newsletter') {
    await S.view('default');
    await S.full();
    return;
  }
  await S.view('default');
  await S.full();
}

const browser = await chromium.launch();
let total = 0;
for (const mobile of [false, true]) {
  for (const [key, path] of PAGES) {
    const name = (mobile ? 'mobile-' : '') + key;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
    const vw = mobile ? 390 : 1440;
    const vh = mobile ? 844 : 900;
    const dpr = mobile ? 2 : 1;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    log('open', name, path);
    try {
      let ok = false;
      for (let attempt = 0; attempt < 3 && !ok; attempt++) {
        await p.goto(BASE + path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => log('  goto', e.message.split('\n')[0]));
        if (!(await clearChallenge(p))) break;
        await wait(p, 900);
        const bad = await p.evaluate(() => /something went wrong|^not found$/i.test((document.body?.innerText || '').trim())).catch(() => true);
        ok = !bad;
      }
      if (!ok) { log('  BLOCKED', path); await ctx.close(); continue; }
      await hideCookies(p);
      await interactions(p, S, key, mobile);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
