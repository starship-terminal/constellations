// Captures IFTTT's public pages (ifttt.ai) into RAW. quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Phone shots get a mobile- prefix. The site paints one light
// theme. Desktop is 1440x900 at 1x, phone 390x844 at 2x. A page taller than one GPU texture is
// saved as name.partN.png. Nothing is submitted, and no password, email, code, or identity
// provider is used. A control that opens /login or /join is recorded and that branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'ifttt', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const BASE = 'https://ifttt.ai';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const WALL = /\/(login|join|passwords\/forgot)(\?|$)/;

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
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
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function goto(p, urlPath) {
  const resp = await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 1800);
  return { status: resp?.status() ?? null, url: p.url() };
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const input = p.locator('#universal-search-input');
      await input.click({ timeout: 5000 });
      await input.fill('hue');
      await wait(p, 900);
      await S.view('search');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('tab-business', async () => {
      await p.locator('button.featured-tab', { hasText: 'Business' }).click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('tab-business');
    });
    await S.full();
  } },
  explore: { path: '/explore', run: async (p, S) => {
    await S.view('default');
    await step('chip', async () => {
      const chip = p.getByRole('button', { name: 'Popular', exact: true }).first();
      if (await chip.count()) { await chip.click({ timeout: 5000 }); await wait(p, 700); await S.view('chip-popular'); }
    });
    await S.full();
  } },
  'explore-services': { path: '/explore/services', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'explore-applets': { path: '/explore/applets', run: async (p, S) => { await S.view('default'); } },
  'explore-stories': { path: '/explore/stories', run: async (p, S) => { await S.view('default'); } },
  plans: { path: '/plans', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      const sw = p.getByRole('switch', { name: 'Show yearly prices' });
      if (await sw.count()) { await sw.click({ timeout: 5000 }); await wait(p, 500); await S.view('monthly'); }
    });
    await step('tooltip', async () => {
      const b = p.getByRole('button', { name: 'About Credits' });
      if (await b.count()) { await b.click({ timeout: 5000 }); await wait(p, 500); await S.view('tooltip'); await p.keyboard.press('Escape'); }
    });
    await step('faq', async () => {
      const s = p.locator('summary').filter({ hasText: 'Which payment methods' });
      if (await s.count()) {
        await s.click({ timeout: 5000 });
        await wait(p, 400);
        const open = await p.evaluate(() => [...document.querySelectorAll('details')].some((d) => d.open && /payment methods/i.test(d.innerText || '')));
        if (!open) await p.evaluate(() => { const d = [...document.querySelectorAll('details')].find((el) => /payment methods/i.test(el.innerText || '')); if (d) d.open = true; });
        await wait(p, 300);
        await S.view('faq');
      }
    });
    await S.full();
  } },
  service: { path: '/hue', run: async (p, S) => {
    await S.view('default');
    await step('share', async () => {
      await p.locator('button[aria-label="share"]').click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('share');
      await p.locator('.modal-close').first().click({ timeout: 3000 }).catch(() => p.keyboard.press('Escape'));
      await wait(p, 300);
    });
    await step('show-more', async () => {
      const b = p.locator('button.clamp-toggle').first();
      if (await b.count()) { await b.click({ timeout: 5000 }); await wait(p, 400); await S.view('show-more'); }
    });
    await S.full();
  } },
  connect: { path: '/connect/google_calendar/slack', run: async (p, S) => { await S.view('default'); await S.full(); } },
  applet: { path: '/applets/yNvHX9VQ-set-your-android-wallpaper-to-nasa-s-image-of-the-day', run: async (p, S) => { await S.view('default'); await S.full(); } },
  story: { path: '/explore/welcome_to_ifttt', run: async (p, S) => { await S.view('default'); await S.full(); } },
  mcp: { path: '/mcp', run: async (p, S) => {
    await S.view('default');
    await step('tab-cursor', async () => {
      const t = p.getByRole('tab', { name: 'Cursor', exact: true });
      if (await t.count()) { await t.click({ timeout: 5000 }); await wait(p, 500); await S.view('tab-cursor'); }
    });
    await S.full();
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: '/careers', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  help: { path: '/help', run: async (p, S) => { await S.view('default'); } },
  developers: { path: '/developers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  partners: { path: '/partners', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'docs-api': { path: '/docs/api_reference', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: 'Open the menu' });
      if (await b.count()) { await b.click({ timeout: 5000 }); await wait(p, 500); await S.view('menu'); }
    });
  } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  'content-map': { path: '/content_map', run: async (p, S) => { await S.view('default'); } },
  'contact-sales': { path: '/contact_sales', run: async (p, S) => { await S.view('default'); } },
  solutions: { path: '/solutions/productivity', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'solutions-home': { path: '/solutions/smart-home', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  join: { path: '/join', run: async (p, S) => { await S.view('default'); } },
  forgot: { path: '/passwords/forgot', run: async (p, S) => { await S.view('default'); } },
  missing: { path: '/not-a-real-page-xyz', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      await p.locator('button.closed').click({ timeout: 5000 });
      await wait(p, 600);
      await S.view('menu');
      await p.locator('button.open').click({ timeout: 4000 }).catch(() => {});
      await wait(p, 300);
    });
    await step('search', async () => {
      await p.locator('button.mobile-icon-search').click({ force: true, timeout: 5000 });
      await wait(p, 500);
      await S.view('search');
    });
    await S.full();
  } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  plans: { path: '/plans', run: async (p, S) => { await S.view('default'); await S.full(); } },
  service: { path: '/hue', run: async (p, S) => { await S.view('default'); } },
  applet: { path: '/applets/yNvHX9VQ-set-your-android-wallpaper-to-nasa-s-image-of-the-day', run: async (p, S) => { await S.view('default'); } },
  mcp: { path: '/mcp', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
const walls = [];
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
  const p = await ctx.newPage();
  log(name, spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const landed = await goto(p, spec.path);
    log('  landed', landed.status, landed.url.replace(BASE, ''));
    if (WALL.test(landed.url) && !WALL.test(BASE + spec.path)) {
      walls.push({ name, from: spec.path, to: landed.url });
      log('  WALL', landed.url);
    }
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
fs.mkdirSync(path.join(PKG, 'raw'), { recursive: true });
fs.writeFileSync(path.join(PKG, 'raw', 'walls.json'), JSON.stringify({ capturedAt: new Date().toISOString(), walls }, null, 2));
log('done', total, 'screenshots ->', RAW);
await browser.close();
