// Captures Typeform's public pages into RAW (full-colour PNGs); quantize.py
// turns them into screenshots/.
//
//   RAW=/tmp/typeform-raw PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; phone shots get a mobile- prefix.
// Desktop is 1440x900 at 1x, phone is 390x844 at 2x. Full pages tile at most
// 8 chunks. Nothing is submitted, and login, signup, Google, Microsoft and
// SSO are never clicked. The OneTrust banner is hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, hoverMenu, dismissAnnouncement } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'typeform', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
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
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const AUTH = /admin\.typeform\.com|\/login|\/signup|accounts\.google|login\.microsoftonline|appleid\.apple|facebook\.com\/login/i;

async function shotPage(p, S, { full = true, menus = false, extra } = {}) {
  await S.view('banner');
  await dismissAnnouncement(p);
  await hideConsent(p);
  await S.view('default');
  if (full) await S.full();
  if (menus) {
    await step('platform-menu', async () => {
      if (await hoverMenu(p, 'open products dropdown menu')) await S.view('platform-menu');
      await p.mouse.move(8, 400);
      await wait(p, 250);
    });
    await step('solutions-menu', async () => {
      if (await hoverMenu(p, 'open solutions dropdown menu')) await S.view('solutions-menu');
      await p.mouse.move(8, 400);
      await wait(p, 250);
    });
    await step('resources-menu', async () => {
      if (await hoverMenu(p, 'open resource dropdown menu')) await S.view('resources-menu');
      await p.mouse.move(8, 400);
      await wait(p, 250);
    });
  }
  if (extra) await extra(p, S);
}

const PAGES = [
  { name: 'home', url: BASE + '/', menus: true },
  { name: 'pricing', url: BASE + '/pricing', extra: async (p, S) => {
    await step('yearly', async () => {
      const y = p.getByRole('button', { name: /Yearly/i }).first();
      if (await y.count()) { await y.click(); await wait(p, 2800); await S.view('yearly'); }
    });
    await step('monthly', async () => {
      const m = p.getByRole('button', { name: /^Monthly/i }).first();
      if (await m.count()) { await m.click(); await wait(p, 2800); await S.view('monthly'); }
    });
  } },
  { name: 'forms', url: BASE + '/forms' },
  { name: 'ai', url: BASE + '/ai' },
  { name: 'mcp', url: BASE + '/mcp' },
  { name: 'growth', url: BASE + '/growth' },
  { name: 'research', url: BASE + '/research-flow' },
  { name: 'templates', url: BASE + '/templates', extra: async (p, S) => {
    await step('search-focus', async () => {
      const s = p.locator('input[type="search"], input[placeholder*="earch" i], input[aria-label*="earch" i]').first();
      if (await s.count()) {
        await s.click();
        await wait(p, 300);
        await S.view('search-focus');
        await p.keyboard.press('Escape');
      }
    });
  } },
  { name: 'template', url: BASE + '/templates/nps-survey-template', extra: async (p, S) => {
    await step('preview', async () => {
      const b = p.locator('[aria-label="open template preview"], button:has-text("Preview")').first();
      if (await b.count()) {
        await b.click();
        await wait(p, 900);
        await S.view('preview');
        const close = p.locator('[aria-label="Close template preview modal"]').first();
        if (await close.count()) await close.click().catch(() => {});
      }
    });
  } },
  { name: 'connect', url: BASE + '/connect' },
  { name: 'enterprise', url: BASE + '/enterprise' },
  { name: 'blog', url: BASE + '/blog', full: false },
  { name: 'blog-post', url: BASE + '/blog/typeform-vs-jotform', full: false },
  { name: 'legal', url: BASE + '/legal', full: false },
  { name: 'about', url: BASE + '/about-us', full: false },
  { name: 'developers', url: BASE + '/developers/', full: false },
  { name: 'help', url: 'https://help.typeform.com/hc/en-us', full: false },
  { name: 'status', url: 'https://status.typeform.com/', full: false },
  { name: 'login', url: 'https://admin.typeform.com/login', full: false, wall: true },
  { name: 'signup', url: 'https://admin.typeform.com/signup', full: false, wall: true },
];

const b = await chromium.launch({ headless: true });
let total = 0;

async function runSet(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  for (const spec of PAGES) {
    const name = (mobile ? 'mobile-' : '') + spec.name;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(spec.name)) continue;
    const ctx = await b.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
      reducedMotion: 'reduce',
    });
    const p = await ctx.newPage();
    log(name, spec.url);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      const resp = await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 70000 });
      await wait(p, spec.wall ? 2500 : 3200);
      await hideConsent(p);
      const landed = p.url();
      if (AUTH.test(landed) && !spec.wall) {
        log('  STOP auth wall', landed);
        await S.view('auth-wall');
      } else {
        if (mobile) {
          await S.view('default');
          if (spec.name === 'home') {
            await step('mobile-menu', async () => {
              const btn = p.locator('[aria-label="open mobile navigation menu"]').first();
              if (await btn.count()) {
                await btn.click();
                await wait(p, 700);
                await S.view('menu');
              }
            });
          }
          if (spec.full !== false && spec.name === 'home') await S.full();
        } else {
          await shotPage(p, S, { full: spec.full !== false && !spec.wall, menus: spec.menus, extra: spec.extra });
        }
        if (resp) log('  status', resp.status(), 'landed', landed.slice(0, 90));
      }
    } catch (e) {
      log('  PAGE FAILED', name, e.message.split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}

await runSet(false);
await runSet(true);
log('done', total, 'screenshots ->', RAW);
await b.close();
