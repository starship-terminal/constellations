// Public capture for scape.com. Headless Playwright. CookieYes is hidden, never clicked.
// No form is submitted. No booking, account, newsletter, or identity provider is used.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'scape', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const BASE = 'https://www.scape.com';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(...a);

const CONSENT_SEL = '.cky-consent-container,.cky-modal,.cky-overlay,.cky-btn-revisit';

async function hideConsent(page) {
  await page.addStyleTag({
    content: `${CONSENT_SEL}{display:none!important;visibility:hidden!important;pointer-events:none!important}`,
  }).catch(() => {});
  await page.evaluate((sel) => {
    document.querySelectorAll(sel).forEach((el) => el.remove());
    // Third-party embed gate ("Please accept cookies to access this content").
    // Hide the overlay. Do not click Accept, Reject, or any consent control.
    const needle = 'please accept cookies';
    for (const el of document.querySelectorAll('div,section,aside')) {
      const text = (el.innerText || '').replace(/\s+/g, ' ').trim().toLowerCase();
      if (!text.includes(needle)) continue;
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.width < 280 && r.height > 0 && r.height < 280) el.remove();
    }
  }, CONSENT_SEL).catch(() => {});
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await page.evaluate((yy) => scrollTo(0, yy), y);
    await page.waitForTimeout(180);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.page, { path: file }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    await lazyScroll(this.page);
    const H = await this.page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(this.page, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.page, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await this.page.evaluate(() => scrollTo(0, 0));
  }
}

const pages = [
  { id: 'home', path: '/' },
  { id: 'rooms', path: '/rooms/' },
  { id: 'favourites', path: '/favourites/' },
  { id: 'booking', path: '/booking/' },
  { id: 'contact', path: '/contact-us/' },
  { id: 'blog', path: '/blog/' },
  { id: 'blog-post', path: '/blog/5-benefits-living-with-friends/' },
  { id: 'faq', path: '/about/faq/' },
  { id: 'life', path: '/life-at-scape/' },
  { id: 'company', path: '/company/' },
  { id: 'offers', path: '/about/offers/' },
  { id: 'privacy', path: '/about/privacy-policy/' },
  { id: 'london', path: '/student-accommodation-london/' },
  { id: 'shoreditch', path: '/student-accommodation-shoreditch/' },
  { id: 'room', path: '/student-accommodation-wembley/en-suite/standard/' },
  { id: 'compare', path: '/university-halls-vs-private-student-accommodation/' },
  { id: 'notfound', path: '/login/' },
];

const browser = await chromium.launch({ headless: true });
let total = 0;
for (const mob of [false, true]) {
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const prefixBase = mob ? 'mobile' : 'desktop';
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-GB',
  });
  await ctx.addInitScript(() => {
    const hide = () => {
      document.querySelectorAll('.cky-consent-container,.cky-modal,.cky-overlay,.cky-btn-revisit').forEach((el) => el.remove());
    };
    const obs = () => new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    if (document.documentElement) { hide(); obs(); }
    else document.addEventListener('DOMContentLoaded', () => { hide(); obs(); });
  });
  const page = await ctx.newPage();
  for (const spec of pages) {
    const name = `${prefixBase}-${spec.id}`;
    if (only.size && !only.has(name) && !only.has(spec.id)) continue;
    const S = new Shooter(page, `${spec.id}-light${mob ? '-mobile' : ''}`, vw, vh, dpr);
    log(name, spec.path);
    try {
      const resp = await page.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 50000 });
      await page.waitForTimeout(2200);
      await hideConsent(page);
      await page.waitForTimeout(400);
      const status = resp ? resp.status() : 0;
      fs.writeFileSync(path.join(RAW, `${S.prefix}.status.json`), JSON.stringify({
        path: spec.path, status, title: await page.title(), measured: await page.evaluate(() => ({
          innerWidth: window.innerWidth, innerHeight: window.innerHeight, dpr: window.devicePixelRatio,
        })),
      }, null, 2));
      await S.view('default');
      if (!mob && spec.id === 'home') {
        await page.getByRole('button', { name: 'Our locations' }).first().click().catch(() => {});
        await page.waitForTimeout(700);
        await S.view('locations-menu');
        await page.keyboard.press('Escape').catch(() => {});
        await page.mouse.click(20, 400).catch(() => {});
        await page.waitForTimeout(300);
        const faq = page.getByRole('button', { name: 'Who is Scape?' }).first();
        if (await faq.count()) {
          await faq.click().catch(() => {});
          await page.waitForTimeout(500);
          await S.view('faq-open');
        }
      }
      if (!mob && spec.id === 'rooms') {
        await page.getByRole('button', { name: 'LOCATION' }).first().click().catch(() => {});
        await page.waitForTimeout(600);
        await S.view('filter-location');
        await page.keyboard.press('Escape').catch(() => {});
      }
      if (!mob && spec.id === 'contact') {
        await page.getByRole('button', { name: 'OPEN FORM' }).first().click().catch(() => {});
        await page.waitForTimeout(800);
        await S.view('enquiry-dialog');
        await page.keyboard.press('Escape').catch(() => {});
        await page.waitForTimeout(300);
      }
      if (!mob && spec.id === 'faq') {
        const chip = page.getByRole('button', { name: 'BOOKINGS' }).first();
        if (await chip.count()) {
          await chip.click().catch(() => {});
          await page.waitForTimeout(500);
          await S.view('bookings-filter');
        }
      }
      if (mob && spec.id === 'home') {
        const burger = page.getByRole('button', { name: /menu/i }).first();
        if (await burger.count()) {
          await burger.click().catch(() => {});
          await page.waitForTimeout(700);
          await S.view('menu');
        }
      }
      // Full-page dumps are not stored. They include building phone numbers and map pins.
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
  }
  await ctx.close();
}
log('done', total, '->', RAW);
await browser.close();
