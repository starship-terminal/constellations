// Captures ClassPass public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [name,name,...]
//
// Names are {page}-light-{state}.png. Mobile ones get a mobile- prefix.
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Full pages are 1x relative to
// that viewport. A page taller than one GPU texture is saved as part tiles.
//
// Nothing is submitted. Cookie banners are hidden, never accepted. Login,
// signup, reset-password and SSO are not clicked. A fresh browser is used
// per page because ClassPass 403s a reused session.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, closePromo } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'classpass', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 14; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h === last && i > 1) break;
    last = h;
    const y = Math.min(h, (i + 1) * 700);
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 250);
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
  async view(name) {
    await hideConsent(this.p);
    // Phone contexts are launched at deviceScaleFactor 2, but some pages
    // report devicePixelRatio 1 while Playwright still writes a 2x PNG.
    // CSS scale keeps the PNG at the CSS viewport the sidecar expects.
    const scale = this.dpr > 1 ? 'css' : 'device';
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, scale }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) {
      // Viewport-sized pages use a normal screenshot. fullPage on a short phone
      // page came back at 2x CSS pixels and failed the dimension check.
      const scale = this.dpr > 1 ? 'css' : 'device';
      if (hCap <= this.requested.viewport.height + 2) await screenshotWithMetadata(p, { path: f + '.png', scale }, this.requested);
      else await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, scale }, this.requested);
    }
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, scale: 'css', clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
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

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('banner');
    await S.view('default');
    await step('how-menu', async () => {
      await p.getByRole('button', { name: 'How it works' }).first().click();
      await wait(p, 700);
      await S.view('how-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await S.full();
    await step('language', async () => {
      await p.evaluate(() => scrollTo(0, document.body.scrollHeight));
      await wait(p, 500);
      await hideConsent(p);
      const lang = p.getByRole('button', { name: /select site language|English/i }).first();
      if (await lang.count()) {
        await lang.click();
        await wait(p, 700);
        await S.view('language');
        await p.keyboard.press('Escape');
      }
    });
  } },
  search: { path: '/search', run: async (p, S) => {
    await S.view('default');
    await step('fitness-filter', async () => {
      const b = p.getByRole('button', { name: 'Fitness' }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('fitness-filter'); await p.keyboard.press('Escape'); await wait(p, 300); }
    });
    await step('activities-filter', async () => {
      const b = p.getByRole('button', { name: 'Activities' }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('activities-filter'); await p.keyboard.press('Escape'); await wait(p, 300); }
    });
    await step('distance-filter', async () => {
      const b = p.getByRole('button', { name: 'Distance' }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('distance-filter'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  plans: { path: '/plans', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gifts: { path: '/gifts', run: async (p, S) => { await S.view('default'); await S.full(); } },
  partners: { path: '/partners', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-how': { path: '/partners/how-it-works', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-calculator': { path: '/partners/revenue-calculator', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-integrations': { path: '/partners/classpass-booking-integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-resources': { path: '/partners/resources', run: async (p, S) => { await S.view('default'); } },
  'partners-blog': { path: '/partners/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-faqs': { path: '/partners/faqs', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'partners-contact': { path: '/partners/contact', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/about/careers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  fitness: { path: '/fitness', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'how-it-works': { path: '/how-classpass-works', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { path: '/try/reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  activities: { path: '/search-index', run: async (p, S) => { await S.view('default'); await S.full(); } },
  brands: { path: '/brands', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gym: { path: '/gym', run: async (p, S) => { await S.view('default'); await S.full(); } },
  press: { path: '/press-room', run: async (p, S) => { await S.view('default'); await S.full(); } },
  referral: { path: '/try/referral-program', run: async (p, S) => { await S.view('default'); await S.full(); } },
  affiliate: { path: '/try/affiliate-program', run: async (p, S) => { await S.view('default'); await S.full(); } },
  partnerships: { path: '/try/brand-partnerships', run: async (p, S) => { await S.view('default'); await S.full(); } },
  location: { path: '/location', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  accessibility: { path: '/about/accessibility', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  'reset-password': { path: '/reset-password', run: async (p, S) => { await S.view('default'); } },
  walkthrough: { path: '/walkthrough', run: async (p, S) => {
    await S.view('default');
    await step('next', async () => {
      const n = p.getByRole('button', { name: /Next/ }).first();
      if (await n.count()) { await n.click(); await wait(p, 800); await S.view('slide-2'); }
    });
  } },
  'walkthrough-edu': { path: '/walkthrough/edusignup', run: async (p, S) => { await S.view('default'); } },
  signup: { path: '/member-signup/getclasspass', run: async (p, S) => { await S.view('default'); } },
  studio: { path: '/studios/dopamine-movement-serangoon-garden-singapore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  brand: { path: '/brands/soulcycle', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/what-is-somatic-yoga/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'activity-city': { path: '/search-index/amsterdam', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.locator('button').filter({ has: p.locator('svg') }).first();
      const named = p.getByRole('button', { name: /menu|open/i });
      const target = (await named.count()) ? named.first() : p.locator('header button, nav button, [aria-label*="menu" i]').first();
      if (await target.count()) {
        await target.click();
        await wait(p, 800);
        await S.view('menu');
      } else {
        log('  no mobile menu button');
      }
    });
    await S.full();
  } },
  search: { path: '/search', run: async (p, S) => { await S.view('default'); await S.full(); } },
  plans: { path: '/plans', run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  gifts: { path: '/gifts', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  features: { path: '/features', run: async (p, S) => { await S.view('default'); } },
  walkthrough: { path: '/walkthrough', run: async (p, S) => { await S.view('default'); } },
  signup: { path: '/member-signup/getclasspass', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  partners: { path: '/partners', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
};

async function shoot(name, spec, mob) {
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  const prefix = `${mob ? 'mobile-' : ''}${name}-light`;
  const S = new Shooter(p, prefix, vw, vh, dpr);
  log(prefix);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2800);
    const statusish = p.url();
    const title = await p.title();
    log('  url', statusish, 'title', title.slice(0, 70));
    if (/access denied|just a moment|attention required/i.test(title)) {
      log('  BLOCKED', name);
    } else {
      await hideConsent(p);
      await spec.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  await ctx.close();
  await browser.close();
  return S.count;
}

const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false, spec: desktop[k] })), ...Object.keys(mobile).map((k) => ({ k, mob: true, spec: mobile[k] }))];
let total = 0;
for (const { k, mob, spec } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  total += await shoot(k, spec, mob);
}
log('done', total, 'screenshots ->', RAW);
