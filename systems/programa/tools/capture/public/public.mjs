// Captures Programa's public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/programa/raw-shots PLAYWRIGHT=... node public.mjs [page,page]
//
// Names are {page}-light-{state}.png. Mobile names get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full pages tile at 8 chunks.
//
// Nothing is submitted. Email is never typed. Login, register, Google, Trimble
// and Xero are never opened. A control that would leave the public site is recorded
// in site-tree.md and skipped here.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'programa', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 8 * 7000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
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
    await this.p.evaluate(() => scrollTo(0, 0)).catch(() => {});
    const source = this.p.url().split('?')[0];
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, { ...this.requested, sanitizedSourceUrl: source });
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const source = p.url().split('?')[0];
    const req = { ...this.requested, sanitizedSourceUrl: source };
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, req);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, req);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function hoverNav(p, name) {
  const loc = p.locator('header a, nav a').filter({ hasText: new RegExp('^' + name + '$') }).first();
  await loc.hover();
  await wait(p, 700);
}

async function openMobileMenu(p) {
  const b = p.getByRole('button', { name: 'Open menu' }).first();
  await b.click();
  await wait(p, 700);
}

const pages = {
  home: { path: '/' },
  features: { path: '/features' },
  pricing: { path: '/pricing' },
  about: { path: '/about' },
  blog: { path: '/blog' },
  editorial: { path: '/editorial' },
  'made-with': { path: '/made-with-programa' },
  contact: { path: '/contact-us' },
  changelog: { path: '/changelog' },
  faq: { path: '/frequently-asked-questions' },
  testimonials: { path: '/testimonials' },
  solo: { path: '/solo-designers' },
  small: { path: '/small-studios' },
  large: { path: '/large-studios' },
  demo: { path: '/designer-demo-on-demand' },
  suppliers: { path: '/suppliers' },
  'trade-portal': { path: '/trade-portal' },
  team: { path: '/team' },
  reviews: { path: '/reviews' },
  guide: { path: '/guide-to-getting-started' },
  privacy: { path: '/privacy-policy' },
  terms: { path: '/terms-and-conditions' },
  cookies: { path: '/cookie-policy' },
  schedules: { path: '/features/schedules-for-interior-designers' },
  presentations: { path: '/features/presentations-for-interior-designers' },
  library: { path: '/features/product-libraries' },
  invoicing: { path: '/features/invoicing-and-payments-for-interior-designers' },
  article: { path: '/blog/what-is-programa' },
};

const desktop = {};
const mobile = {};
for (const [k, spec] of Object.entries(pages)) {
  desktop[k] = {
    path: spec.path,
    run: async (p, S) => {
      await S.view('default');
      await S.full();
      if (k === 'home') {
        await step('features-menu', async () => { await hoverNav(p, 'Features'); await S.view('features-menu'); await p.mouse.move(700, 800); await wait(p, 300); });
        await step('solutions-menu', async () => { await hoverNav(p, 'Solutions'); await S.view('solutions-menu'); await p.mouse.move(700, 800); await wait(p, 300); });
        await step('learn-menu', async () => { await hoverNav(p, 'Learn'); await S.view('learn-menu'); await p.mouse.move(700, 800); await wait(p, 300); });
        await step('login-hover', async () => {
          const loc = p.getByRole('link', { name: 'Log in' }).first();
          await loc.hover();
          await wait(p, 400);
          await S.view('login-hover');
        });
        await step('cta-focus', async () => {
          const loc = p.getByRole('link', { name: 'Get started' }).first();
          await loc.focus();
          await wait(p, 300);
          await S.view('cta-focus');
        });
      }
      if (k === 'pricing') {
        await step('annual-toggle', async () => {
          const t = p.getByRole('button', { name: /annual/i }).first();
          if (await t.count()) { await t.click(); await wait(p, 500); await S.view('annual'); }
        });
        await step('faq-open', async () => {
          const q = p.getByRole('button', { name: /How will I be billed/i }).first();
          if (await q.count()) { await q.click(); await wait(p, 400); await S.view('faq-open'); }
        });
      }
      if (k === 'faq') {
        await step('accordion', async () => {
          const q = p.getByRole('button', { name: 'What is Programa?' }).first();
          if (await q.count()) { await q.click(); await wait(p, 400); await S.view('accordion'); }
        });
      }
      if (k === 'blog') {
        await step('search-focus', async () => {
          const s = p.locator('input[type="search"], input[name="query"]').first();
          if (await s.count()) { await s.focus(); await wait(p, 300); await S.view('search-focus'); }
        });
      }
      if (k === 'contact') {
        await step('email-focus', async () => {
          const s = p.locator('input[type="email"]').first();
          if (await s.count()) { await s.focus(); await wait(p, 300); await S.view('email-focus'); }
        });
      }
    },
  };
  mobile[k] = {
    path: spec.path,
    run: async (p, S) => {
      await S.view('default');
      if (['home', 'features', 'pricing', 'blog', 'contact', 'faq'].includes(k)) await S.full();
      if (k === 'home') {
        await step('menu', async () => {
          await openMobileMenu(p);
          await S.view('menu');
          const feat = p.getByRole('button', { name: 'Features', exact: true }).first();
          if (await feat.count()) { await feat.click(); await wait(p, 400); await S.view('menu-features'); }
        });
      }
    },
  };
}

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1600);
    await closePromo(p);
    const title = await p.title();
    if (/just a moment|access denied|verify/i.test(title)) throw new Error('blocked: ' + title);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
