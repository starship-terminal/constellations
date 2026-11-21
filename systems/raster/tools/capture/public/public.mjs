// Captures Raster's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x.
// Marketing pages paint dark (html.dark). Docs paints dark on this pass.
// /design leaves html without a theme class and still paints a black body.
//
// Nothing is typed. No form is submitted. No identity provider is clicked.
// No checkout is started. Sign-in and signup are photographed empty and left.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'raster', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

async function hideCookie(page) {
  await page.evaluate(() => {
    for (const x of document.querySelectorAll('div, section, aside, [role="dialog"]')) {
      const t = x.innerText || '';
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      const overlay = (cs.position === 'fixed' || cs.position === 'sticky')
        && r.width > 80 && r.height > 40 && r.height < innerHeight * 0.7
        && /cookie|we value your privacy|consent|accept all/i.test(t)
        && !/sign in/i.test(t);
      if (overlay) x.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
  }
  async view(name, source) {
    await hideCookie(this.p);
    this.requested.sanitizedSourceUrl = source || null;
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name, source) {
    const p = this.p;
    await hideCookie(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 6 * chunk;
    const hCap = Math.min(H, MAXH);
    this.requested.sanitizedSourceUrl = source || null;
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
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
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 200);
  }
}

async function settle(page) {
  await page.waitForLoadState('domcontentloaded');
  await wait(page, 900);
  await hideCookie(page);
}

async function openResources(page) {
  const button = page.locator('button.nav-link-dropdown').first();
  await button.focus();
  await wait(page, 400);
}

async function openMobileNav(page) {
  const button = page.locator('button.mobile-nav-button').first();
  await button.click();
  await wait(page, 500);
}

async function assertEmptyAuth(page) {
  const filled = await page.evaluate(() => {
    const email = document.querySelector('input[type="email"], input[name="email"]');
    return email ? (email.value || '').length : -1;
  });
  if (filled > 0) throw new Error('auth email field is not empty; refusing to photograph');
}

const PAGES = [
  ['home', 'https://raster.app/'],
  ['product', 'https://raster.app/product'],
  ['pricing', 'https://raster.app/pricing'],
  ['blog', 'https://raster.app/blog'],
  ['design', 'https://raster.app/design'],
  ['docs', 'https://raster.app/docs'],
  ['changelog', 'https://raster.app/changelog'],
  ['privacy', 'https://raster.app/privacy'],
  ['terms', 'https://raster.app/terms'],
  ['share-missing', 'https://raster.app/s/q7Wm2xKp'],
];

async function desktop() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    colorScheme: 'dark',
  });
  const page = await context.newPage();
  const shot = new Shooter(page, 'desk', 1440, 900, 1);

  for (const [name, url] of PAGES) {
    log('desktop', name);
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await settle(page);
    const landed = new URL(page.url());
    const source = landed.origin + landed.pathname;
    await shot.view(`${name}-default`, source);
    if (name === 'home' || name === 'pricing' || name === 'product') {
      await shot.full(`${name}-full`, source);
    }
  }

  log('desktop resources menu');
  await page.goto('https://raster.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await openResources(page);
  await shot.view('home-menu', 'https://raster.app/');

  log('desktop sign-in empty');
  await page.goto('https://raster.app/sign-in', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await assertEmptyAuth(page);
  await shot.view('auth-default', 'https://raster.app/sign-in');

  log('desktop signup empty');
  await page.goto('https://raster.app/sign-up', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await assertEmptyAuth(page);
  const signupLanded = new URL(page.url());
  await shot.view('signup-default', signupLanded.origin + signupLanded.pathname);

  log('desktop missing page');
  const missing = await page.goto('https://raster.app/not-a-real-page-raster', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  log('  missing status', missing && missing.status(), 'url path', new URL(page.url()).pathname);
  const missingLanded = new URL(page.url());
  await shot.view('notfound-default', missingLanded.origin + missingLanded.pathname);

  await browser.close();
}

async function phone() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    colorScheme: 'dark',
  });
  const page = await context.newPage();
  const shot = new Shooter(page, 'phone', 390, 844, 2);

  log('phone home');
  await page.goto('https://raster.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await shot.view('home-default', 'https://raster.app/');
  await openMobileNav(page);
  await shot.view('home-menu', 'https://raster.app/');
  await page.keyboard.press('Escape').catch(() => {});
  await page.goto('https://raster.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await shot.full('home-full', 'https://raster.app/');

  log('phone pricing');
  await page.goto('https://raster.app/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await shot.view('pricing-default', 'https://raster.app/pricing');

  log('phone sign-in empty');
  await page.goto('https://raster.app/sign-in', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  await assertEmptyAuth(page);
  await shot.view('auth-default', 'https://raster.app/sign-in');

  await browser.close();
}

await desktop();
await phone();
log('done', RAW);
