// Captures Patreon's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x, phone shots 390x844 at 2x. Names are {page}-light-{state}.png.
// A logged-out app page that exposes Appearance can also write {page}-dark-{state}.png after the
// Account menu Dark control, then System is restored. Nothing is submitted. Login, signup, Apple,
// Facebook, Google, Join, Chats and Notifications are never clicked. A password field aborts that page.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const WALL = /\/(login|signup|sign-up)(\b|\/|\?)/i;

async function hideConsent(p) {
  // Never click a consent control. Hide a banner if one is covering the page.
  await p.evaluate(() => {
    const words = /cookie|consent|privacy choices/i;
    for (const el of document.querySelectorAll('[role="dialog"], [aria-modal="true"], [class*="cookie" i], [id*="cookie" i], [class*="consent" i]')) {
      const text = (el.innerText || '').slice(0, 400);
      if (!words.test(text) && !words.test(el.id || '') && !words.test(el.className || '')) continue;
      if ((el.innerText || '').length > 800) continue;
      el.setAttribute('data-patreon-hidden-consent', '1');
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function isWall(p) {
  const url = p.url();
  if (WALL.test(url)) return url;
  const pwd = await p.locator('input[type="password"]').count().catch(() => 0);
  if (pwd) return url + ' (password field)';
  return '';
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 7200));
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    const wall = await isWall(this.p);
    if (wall) { log('  skip shot', name, 'wall', wall); return; }
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    const wall = await isWall(p);
    if (wall) { log('  skip full', name, 'wall', wall); return; }
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function openPage(p, url) {
  const resp = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await wait(p, 2800);
  await hideConsent(p);
  const wall = await isWall(p);
  return { status: resp ? resp.status() : null, url: p.url(), title: await p.title(), wall };
}

async function accountMenu(p, S, theme) {
  const btn = p.getByRole('button', { name: 'Account menu' });
  if (!(await btn.count())) { log('  no account menu'); return; }
  await btn.first().click();
  await wait(p, 700);
  await S.view('account-menu');
  if (theme === 'dark') {
    const dark = p.getByRole('button', { name: 'Dark', exact: true });
    if (await dark.count()) {
      await dark.first().click();
      await wait(p, 700);
    }
  }
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 300);
}

async function restoreSystem(p) {
  const btn = p.getByRole('button', { name: 'Account menu' });
  if (!(await btn.count())) return;
  await btn.first().click();
  await wait(p, 500);
  const system = p.getByRole('button', { name: 'System', exact: true });
  if (await system.count()) await system.first().click();
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 300);
}

const desktop = {
  'home-app': { url: 'https://www.patreon.com/?patreon_source=internal', expect: /Home \| Patreon/, run: async (p, S) => {
    if (!/Home \| Patreon/.test(await p.title())) { log('  not the logged-out app home, title=', await p.title()); return; }
    await S.view('default');
    const share = p.getByRole('button', { name: 'Share', exact: true });
    if (await share.count()) { await share.first().click(); await wait(p, 600); await S.view('share-menu'); await p.keyboard.press('Escape'); }
    await accountMenu(p, S, 'light');
  } },
  'home-app-dark': { url: 'https://www.patreon.com/?patreon_source=internal', theme: 'dark', expect: /Home \| Patreon/, run: async (p, S) => {
    if (!/Home \| Patreon/.test(await p.title())) { log('  not the logged-out app home'); return; }
    await accountMenu(p, S, 'dark');
    await S.view('default');
    await restoreSystem(p);
  } },
  explore: { url: 'https://www.patreon.com/explore', run: async (p, S) => {
    await S.view('default');
    const search = p.getByRole('searchbox').or(p.locator('input[type="search"], input[placeholder*="Search" i]'));
    if (await search.count()) {
      await search.first().click();
      await search.first().fill('podcast');
      await wait(p, 900);
      await S.view('search-typed');
      await search.first().fill('');
    }
    const chip = p.getByRole('button', { name: 'Art tutorials' });
    if (await chip.count()) {
      await chip.first().click({ timeout: 8000 }).catch((e) => log('  topic click skipped', String(e.message || e).split('\n')[0]));
      await wait(p, 800);
      await S.view('topic');
    }
  } },
  creator: { url: 'https://www.patreon.com/cw/GlamorousTrash', run: async (p, S) => { await S.view('default'); } },
  'creator-posts': { url: 'https://www.patreon.com/cw/GlamorousTrash/posts', run: async (p, S) => { await S.view('default'); } },
  'creator-membership': { url: 'https://www.patreon.com/cw/GlamorousTrash/membership', run: async (p, S) => { await S.view('default'); } },
  'creator-shop': { url: 'https://www.patreon.com/cw/GlamorousTrash/shop', run: async (p, S) => { await S.view('default'); } },
  'creator-collections': { url: 'https://www.patreon.com/cw/GlamorousTrash/collections', run: async (p, S) => { await S.view('default'); } },
  post: { url: 'https://www.patreon.com/GlamorousTrash/posts/175733850', run: async (p, S) => { await S.view('default'); } },
  marketing: { url: 'https://www.patreon.com/', expect: /Where Creator Communities Thrive/, run: async (p, S) => {
    if (!/Where Creator Communities Thrive/.test(await p.title())) { log('  marketing home not served, title=', await p.title()); return; }
    await S.view('default');
    await S.full();
    const creators = p.locator('header').getByRole('button', { name: 'Creators', exact: true });
    if (await creators.count()) { await creators.first().hover(); await wait(p, 600); await S.view('creators-menu'); }
  } },
  pricing: { url: 'https://www.patreon.com/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-create': { url: 'https://www.patreon.com/product/create', run: async (p, S) => { await S.view('default'); } },
  'product-membership': { url: 'https://www.patreon.com/product/paid-membership', run: async (p, S) => { await S.view('default'); } },
  'creators-podcasts': { url: 'https://www.patreon.com/creators/podcasts', run: async (p, S) => { await S.view('default'); } },
  about: { url: 'https://www.patreon.com/about', run: async (p, S) => { await S.view('default'); } },
  press: { url: 'https://www.patreon.com/press', run: async (p, S) => { await S.view('default'); } },
  careers: { url: 'https://www.patreon.com/careers', run: async (p, S) => { await S.view('default'); } },
  apps: { url: 'https://www.patreon.com/apps', run: async (p, S) => { await S.view('default'); } },
  policy: { url: 'https://www.patreon.com/policy', run: async (p, S) => { await S.view('default'); } },
  help: { url: 'https://support.patreon.com/hc/en-us', run: async (p, S) => {
    await S.view('default');
    const search = p.locator('input[type="search"], input[name="query"]').first();
    if (await search.count()) { await search.click(); await wait(p, 400); await S.view('search-focused'); }
  } },
  news: { url: 'https://news.patreon.com/', run: async (p, S) => { await S.view('default'); } },
  updates: { url: 'https://www.patreon.com/collection/700928?view=condensed', run: async (p, S) => { await S.view('default'); } },
  'p4c': { url: 'https://www.patreon.com/cw/PatreonforCreators', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  'home-app': { url: 'https://www.patreon.com/?patreon_source=internal', expect: /Home \| Patreon/, run: async (p, S) => {
    if (!/Home \| Patreon/.test(await p.title())) { log('  phone home is not the app, title=', await p.title()); return; }
    await S.view('default');
    const nav = p.getByRole('button', { name: /open navigation/i });
    if (await nav.count()) { await nav.first().click(); await wait(p, 700); await S.view('nav-sheet'); }
  } },
  explore: { url: 'https://www.patreon.com/explore', run: async (p, S) => { await S.view('default'); } },
  creator: { url: 'https://www.patreon.com/cw/GlamorousTrash', run: async (p, S) => { await S.view('default'); } },
  pricing: { url: 'https://www.patreon.com/pricing', run: async (p, S) => { await S.view('default'); } },
  marketing: { url: 'https://www.patreon.com/', expect: /Where Creator Communities Thrive/, run: async (p, S) => {
    if (!/Where Creator Communities Thrive/.test(await p.title())) { log('  phone marketing home not served, title=', await p.title()); return; }
    await S.view('default');
    const menu = p.getByRole('button', { name: /open menu/i });
    if (await menu.count()) { await menu.first().click(); await wait(p, 700); await S.view('nav-sheet'); }
  } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const theme = spec.theme === 'dark' ? 'dark' : 'light';
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, spec.url.split('?')[0]);
  try {
    const opened = await openPage(p, spec.url);
    log('  ', opened.status, opened.title, opened.wall ? 'WALL ' + opened.wall : opened.url);
    if (opened.wall) { log('  branch stopped'); }
    else if (spec.expect && !spec.expect.test(opened.title)) log('  title mismatch, runner decides');
    if (!opened.wall) await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
