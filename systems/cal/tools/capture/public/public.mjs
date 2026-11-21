// Captures Cal.com's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x, phone shots 390x844 at 2x. Nothing is
// signed into, submitted, or sent. Auth and SSO controls are never clicked.
// A control that navigates to app.cal.com/auth or /signup is recorded and
// that branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, contextFor, hideBanners, isAuth } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'cal', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const walls = [];

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name, source) {
    this.requested.sanitizedSourceUrl = source || null;
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full', source) {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px`);
    this.requested.sanitizedSourceUrl = source || null;
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

async function gotoPublic(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(page, 1600);
  await hideBanners(page);
  const final = page.url();
  if (isAuth(final)) {
    walls.push({ from: url, to: final.split('?')[0] });
    log('  AUTH WALL', url, '->', final.split('?')[0]);
    return { ok: false, status: res?.status() || 0, final };
  }
  return { ok: true, status: res?.status() || 0, final };
}

async function openMenu(page, name) {
  const b = page.locator('nav button').filter({ hasText: new RegExp('^' + name + '$') }).first();
  if (!(await b.count())) return false;
  await b.click({ force: true });
  await wait(page, 700);
  return (await b.getAttribute('aria-expanded')) === 'true';
}

const PAGES = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['enterprise', '/enterprise'],
  ['scheduling', '/scheduling'],
  ['events', '/events'],
  ['discover', '/discover'],
  ['ai', '/ai'],
  ['assistant', '/assistant'],
  ['desktop', '/desktop'],
  ['apps', '/apps'],
  ['customers', '/customers'],
  ['blog', '/blog'],
  ['docs', '/docs'],
  ['help', '/help'],
  ['faq', '/faq'],
  ['about', '/about'],
  ['security', '/security'],
  ['compliance', '/compliance'],
  ['contact', '/contact'],
  ['talk-to-sales', '/talk-to-sales'],
  ['download', '/download'],
  ['changelog', '/changelog'],
  ['font', '/font'],
  ['brand', '/brand'],
  ['jobs', '/jobs'],
  ['open', '/open'],
  ['privacy', '/privacy'],
  ['terms', '/terms'],
  ['cal-video', '/features/cal-video'],
  ['workflows', '/workflows'],
  ['routing', '/routing'],
  ['teams', '/teams'],
  ['embed', '/embed'],
  ['app', '/app'],
  ['notes', '/notes'],
  ['calendar', '/calendar'],
  ['payments', '/payments'],
  ['organizations', '/organizations'],
  ['mcp', '/mcp'],
  ['agent', '/agent'],
  ['grok-bot', '/grok-bot'],
  ['compare', '/compare'],
  ['vs-calendly', '/calcom-vs-calendly'],
  ['migrate', '/migrate'],
  ['atoms', '/atoms'],
  ['integrate', '/integrate'],
  ['world-clock', '/world-clock'],
  ['calendar-tools', '/calendar-tools'],
  ['customer-deel', '/customers/deel'],
  ['healthcare', '/scheduling/healthcare'],
  ['sales', '/scheduling/sales-teams'],
  ['round-robin', '/features/round-robin'],
  ['signup-wall', 'https://app.cal.com/signup'],
  ['login-wall', 'https://app.cal.com/auth/login'],
];

const MOBILE = ['home', 'pricing', 'enterprise', 'scheduling', 'ai', 'docs', 'blog', 'apps', 'customers', 'signup-wall'];

const browser = await chromium.launch({ headless: true });
let total = 0;

async function shoot(name, url, mobile) {
  const prefix = (mobile ? 'mobile-' : '') + name + '-light';
  if (pageArg.length && !pageArg.includes(prefix) && !pageArg.includes(name) && !pageArg.includes((mobile ? 'mobile-' : '') + name)) return;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const ctx = await contextFor(browser, { mobile });
  const page = await ctx.newPage();
  const S = new Shooter(page, prefix, vw, vh, dpr);
  const abs = url.startsWith('http') ? url : BASE + url;
  log(prefix, abs);
  try {
    const landed = await gotoPublic(page, abs);
    if (!landed.ok) {
      await S.view('auth-wall', abs.split('?')[0]);
      total += S.count;
      await ctx.close();
      return;
    }
    const source = abs.split('?')[0];
    await S.view('default', source);
    if (!mobile) await S.full('full', source);
    else if (['home', 'pricing', 'scheduling'].includes(name)) await S.full('full', source);

    if (!mobile && name === 'home') {
      for (const menu of ['Products', 'Use cases', 'AI', 'Features', 'Resources']) {
        if (await openMenu(page, menu)) {
          await S.view('menu-' + menu.toLowerCase().replace(/\s+/g, '-'), source);
          await page.keyboard.press('Escape');
          await page.mouse.click(700, 820);
          await wait(page, 250);
        }
      }
      const faq = page.getByRole('button', { name: /What is Cal\.com and how does it work/i }).first();
      if (await faq.count()) {
        await faq.scrollIntoViewIfNeeded().catch(() => {});
        await faq.click({ force: true }).catch(() => {});
        await wait(page, 500);
        await S.view('faq-open', source);
      }
      const tab = page.getByRole('tab', { name: 'Cal Desktop' }).first();
      if (await tab.count()) {
        await tab.scrollIntoViewIfNeeded().catch(() => {});
        await tab.click({ force: true }).catch(() => {});
        await wait(page, 500);
        await S.view('tab-desktop', source);
      }
    }
    if (mobile && name === 'home') {
      const open = page.getByRole('button', { name: /open menu/i }).first();
      if (await open.count()) {
        await open.click({ force: true });
        await wait(page, 700);
        await S.view('menu', source);
      }
    }
    if (name === 'pricing') {
      const monthly = page.getByRole('button', { name: /month/i }).first();
      const yearly = page.getByRole('tab', { name: /year|annual/i }).first();
      const toggle = (await yearly.count()) ? yearly : monthly;
      if (await toggle.count()) {
        await toggle.click({ force: true }).catch(() => {});
        await wait(page, 400);
        await S.view('billing-toggle', source);
      }
    }
    if (name === 'talk-to-sales' || name === 'contact') {
      // Photograph the empty form. Do not type or submit.
      await S.view('form-empty', source);
    }
  } catch (e) {
    log('  PAGE FAILED', prefix, String(e.message).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}

for (const [name, url] of PAGES) await shoot(name, url, false);
for (const name of MOBILE) {
  const found = PAGES.find((p) => p[0] === name);
  if (found) await shoot(name, found[1], true);
}

fs.writeFileSync(path.join(RAW, 'auth-walls.json'), JSON.stringify(walls, null, 2) + '\n');
log('done', total, 'screenshots ->', RAW, 'walls', walls.length);
await browser.close();
