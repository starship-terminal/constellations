// Captures Sketch's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/sketch/raw-shots PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Phone shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full-page shots are 1x
// on desktop and 2x on phone, tiled when taller than one GPU texture.
//
// Nothing is submitted. Sign-in is opened and left blank. Newsletter, contact,
// Apple, Google and SSO are not used. Cookie overlays are hidden, never posted.

import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) {
  console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)');
  process.exit(2);
}
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideOverlays(p) {
  await p.evaluate(() => {
    const sels = [
      '#onetrust-banner-sdk', '#onetrust-consent-sdk', '.ot-sdk-container',
      '[class*="cookie-banner"]', '[id*="cookie-banner"]', '[class*="consent-banner"]',
      'iframe[title*="chat" i]', '#hubspot-messages-iframe-container',
    ];
    for (const s of sels) document.querySelectorAll(s).forEach((el) => { el.style.setProperty('display', 'none', 'important'); });
  }).catch(() => {});
}

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
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
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

async function hoverNav(p, S, label) {
  const item = p.locator('header li.main-nav__subnav').filter({ hasText: label }).first();
  if (!(await item.count())) return;
  await item.hover();
  await wait(p, 500);
  await S.view('nav-' + label.toLowerCase());
  await p.mouse.move(8, 860);
  await wait(p, 200);
}

async function openPhoneMenu(p, S) {
  const btn = p.locator('button.main-nav__toggle').first();
  if (!(await btn.count())) return;
  await btn.click({ force: true });
  await wait(p, 600);
  await S.view('menu');
  const close = p.locator('.mobile-nav__close').first();
  if (await close.count()) await close.click({ force: true }).catch(() => {});
  await wait(p, 300);
}

const PAGES = [
  ['home', '/'],
  ['design', '/design/'],
  ['collaborate', '/collaborate/'],
  ['prototype', '/prototype/'],
  ['handoff', '/handoff/'],
  ['ai', '/ai/'],
  ['features', '/features/'],
  ['pricing', '/pricing/'],
  ['changelog', '/changelog/'],
  ['changelog-ghent', '/changelog/ghent/'],
  ['roadmap', '/roadmap/'],
  ['blog', '/blog/'],
  ['blog-smart-animate', '/blog/smart-animate/'],
  ['design-resources', '/design-resources/'],
  ['plugins', '/plugins/'],
  ['docs', '/docs/'],
  ['support', '/support/'],
  ['feature-requests', '/feature-requests/'],
  ['downloads', '/downloads/mac/'],
  ['about', '/about-us/'],
  ['beta', '/beta/'],
  ['careers', '/careers/'],
  ['education', '/education/'],
  ['legal', '/legal/'],
  ['license', '/license/'],
  ['partners', '/partners/'],
  ['privacy', '/privacy/'],
  ['security', '/security/'],
  ['vs-figma', '/vs/figma/'],
  ['contact', '/support/contact/'],
  ['signin', '/signin/'],
];

async function desktopStates(p, S, key) {
  await S.view('default');
  if (key === 'home') {
    await hoverNav(p, S, 'Product');
    await hoverNav(p, S, 'Explore');
    await hoverNav(p, S, 'Support');
    await step('hash-design', async () => {
      await p.locator('.page-nav a[href="#design"], .top-bar a[href*="#design"]').first().click();
      await wait(p, 700);
      await S.view('section-design');
    });
  }
  if (key === 'pricing') {
    await step('monthly', async () => {
      await p.locator('.billing-toggle__option--monthly').click();
      await wait(p, 500);
      await S.view('monthly');
      await p.locator('.billing-toggle__option--yearly').click().catch(() => {});
    });
    await step('tooltip', async () => {
      const tip = p.locator('.tooltip-trigger').first();
      await tip.scrollIntoViewIfNeeded();
      await tip.hover();
      await wait(p, 500);
      await S.view('tooltip');
      await p.mouse.move(8, 8);
    });
    await step('currency', async () => {
      const sel = p.locator('select.currency-selector-selector__select, select').first();
      if (await sel.count()) {
        await sel.selectOption({ index: 1 }).catch(() => {});
        await wait(p, 400);
        await S.view('currency');
      }
    });
  }
  if (key === 'signin') {
    await step('email-focus', async () => {
      const email = p.locator('input[type="email"]').first();
      await email.focus();
      await wait(p, 300);
      await S.view('email-focused');
    });
    await step('password-focus', async () => {
      const pw = p.locator('input[type="password"]').first();
      await pw.focus();
      await wait(p, 300);
      await S.view('password-focused');
    });
  }
  if (key === 'docs' || key === 'support' || key === 'plugins' || key === 'blog') {
    await step('search-focus', async () => {
      const field = p.locator('input[type="search"], input[placeholder*="Search" i], input[aria-label*="Search" i]').first();
      if (await field.count()) {
        await field.focus();
        await wait(p, 300);
        await S.view('search-focused');
      }
    });
  }
  const fullKeys = new Set(['home', 'pricing', 'design', 'features', 'docs', 'blog', 'changelog', 'signin', 'about', 'downloads']);
  if (fullKeys.has(key)) await S.full();
}

async function phoneStates(p, S, key) {
  await S.view('default');
  if (key === 'home' || key === 'pricing' || key === 'docs') await openPhoneMenu(p, S);
  if (key === 'pricing') {
    await step('monthly', async () => {
      const b = p.locator('.billing-toggle__option--monthly');
      if (await b.count()) { await b.click(); await wait(p, 400); await S.view('monthly'); }
    });
  }
  if (key === 'signin') await S.view('wall');
  const fullKeys = new Set(['home', 'pricing', 'design', 'docs', 'signin']);
  if (fullKeys.has(key)) await S.full();
}

const b = await chromium.launch({ headless: true });
let total = 0;
for (const mob of [false, true]) {
  for (const [key, urlPath] of PAGES) {
    const name = (mob ? 'mobile-' : '') + key;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
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
    const p = await ctx.newPage();
    log(name);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      const resp = await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 90000 });
      await wait(p, 2200);
      await hideOverlays(p);
      const status = resp ? resp.status() : 0;
      const landed = p.url();
      if (status >= 400) log('  HTTP', status, landed);
      if (/\/signin\/?/.test(new URL(landed).pathname) && key !== 'signin') {
        log('  WALL redirect', key, '->', landed);
        await S.view('wall');
      } else if (mob) await phoneStates(p, S, key);
      else await desktopStates(p, S, key);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await b.close();
