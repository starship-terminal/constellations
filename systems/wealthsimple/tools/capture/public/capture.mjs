// Public Wealthsimple capture. Headless Playwright. No form submits, no login typing.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/wealthsimple/tools/capture/public/capture.mjs [names...]
//
// Writes full-colour PNGs to ~/.design-systems/wealthsimple/raw-shots
// and a JSON sidecar of measurements beside each interactive shot.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'wealthsimple', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://www.wealthsimple.com';

const PAGES = [
  ['home', '/en-ca'],
  ['presents', '/en-ca/presents/something-good'],
  ['chequing', '/en-ca/chequing'],
  ['kids', '/en-ca/chequing/kids-teens'],
  ['savings', '/en-ca/savings'],
  ['usd', '/en-ca/accounts/usd'],
  ['credit-card', '/en-ca/credit-card'],
  ['visa-infinite', '/en-ca/wealthsimple-visa-infinite-card'],
  ['visa-privilege', '/en-ca/wealthsimple-visa-infinite-privilege-card'],
  ['trade', '/en-ca/trade'],
  ['pro', '/en-ca/trade/pro'],
  ['options', '/en-ca/trade/options'],
  ['margin', '/en-ca/trade/margin'],
  ['futures', '/en-ca/trade/futures'],
  ['ipo', '/en-ca/trade/ipo-access'],
  ['predict', '/en-ca/predict'],
  ['gold', '/en-ca/trade/gold'],
  ['crypto', '/en-ca/trade/crypto'],
  ['auto-invest', '/en-ca/automated-investing'],
  ['classic', '/en-ca/invest/classic-portfolios'],
  ['summit', '/en-ca/invest/summit-portfolios'],
  ['income', '/en-ca/invest/income-portfolios'],
  ['private-markets', '/en-ca/invest/private-market-fund'],
  ['advice', '/en-ca/invest/advice'],
  ['invest', '/en-ca/invest'],
  ['loc', '/en-ca/portfolio-line-of-credit'],
  ['mortgages', '/en-ca/mortgages'],
  ['tfsa', '/en-ca/accounts/tfsa'],
  ['rrsp', '/en-ca/accounts/rrsp'],
  ['spousal-rrsp', '/en-ca/accounts/spousal-rrsp'],
  ['non-registered', '/en-ca/accounts/non-registered'],
  ['fhsa', '/en-ca/accounts/fhsa'],
  ['resp', '/en-ca/accounts/resp'],
  ['rrif', '/en-ca/accounts/rrif'],
  ['lira', '/en-ca/accounts/lira'],
  ['accounts', '/en-ca/accounts'],
  ['biz-chequing', '/en-ca/business/chequing'],
  ['biz-investing', '/en-ca/business/investing'],
  ['biz-group', '/en-ca/business/group-savings'],
  ['business', '/en-ca/business'],
  ['millionaire', '/en-ca/monthly-millionaire'],
  ['match', '/en-ca/one-percent-match'],
  ['welcome', '/en-ca/5-percent-welcome-offer'],
  ['promotions', '/en-ca/promotions'],
  ['terms', '/en-ca/legal/terms'],
  ['privacy', '/en-ca/legal/privacy'],
  ['accessibility', '/en-ca/legal/accessibility/statement'],
  ['disclaimers', '/en-ca/legal/legal-disclaimers'],
  ['complaint', '/en-ca/legal/file-complaint'],
  ['active-trading', '/en-ca/trade/active-trading'],
  ['tldr', '/en-ca/learn/tldr-newsletter-signup'],
  ['about', '/en-ca/about'],
  ['culture', '/en-ca/culture'],
  ['careers', '/en-ca/careers'],
  ['security', '/en-ca/security'],
  ['tax', '/en-ca/tax'],
  ['households', '/en-ca/households'],
  ['changelog', '/en-ca/changelog'],
  ['contact', '/en-ca/contact'],
  ['get-in-touch', '/en-ca/get-in-touch'],
  ['referrals', '/en-ca/referrals'],
  ['pricing', '/en-ca/pricing'],
  ['learn', '/en-ca/learn'],
  ['learn-article', '/en-ca/learn/what-is-a-covered-call'],
  ['direct-deposit', '/en-ca/direct-deposit'],
  ['teaching-kids', '/en-ca/teaching-kids-about-money'],
  ['tech-analysis', '/en-ca/technical-analysis'],
  ['trade-show', '/en-ca/the-trade-show'],
  ['options-edu', '/en-ca/options-trading-education'],
  ['margin-resources', '/en-ca/margin-trading-resources'],
  ['futures-guide', '/en-ca/futures-trading-resource-guide'],
  ['notify-futures', '/en-ca/trade/futures/perpetuals-notify-me'],
  ['notify-assistant', '/en-ca/financial-assistant-notify-me'],
  ['notify-biz-card', '/en-ca/business/credit-card-notify-me'],
  ['presents-live', '/en-ca/presents/something-good/live'],
  ['buying-house', '/en-ca/buying-a-house'],
  ['benefits', '/en-ca/benefits'],
  ['retirement', '/en-ca/retirement-planning'],
  ['tax-info', '/en-ca/tax-information-canada'],
  ['transfer-bonus', '/en-ca/transfer-bonus'],
  ['dex', '/en-ca/dex-trading'],
  ['not-found', '/en-ca/this-page-does-not-exist'],
];

const EXTERNAL = [
  ['help', 'https://help.wealthsimple.com/hc/en-ca'],
  ['newsroom', 'https://newsroom.wealthsimple.com/'],
  ['shop', 'https://wealthsimple.com/shop'],
  ['login-wall', 'https://my.wealthsimple.com/app/login?locale=en-ca'],
];

async function hideConsent(page) {
  await page.addStyleTag({ content: `
    #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
    [id*="cookie-banner"], [class*="cookie-banner"], [class*="CookieBanner"],
    [aria-label*="cookie" i], [id*="consent"] { display: none !important; visibility: hidden !important; }
  ` }).catch(() => {});
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter')) {
      el.remove();
    }
  }).catch(() => {});
}

async function settle(page) {
  await page.waitForTimeout(1600);
  await hideConsent(page);
  await page.evaluate(async () => {
    const h = Math.min(document.documentElement.scrollHeight || 0, 12000);
    for (let y = 0; y < h; y += 700) {
      scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 80));
    }
    scrollTo(0, 0);
  }).catch(() => {});
  await page.waitForTimeout(500);
  await hideConsent(page);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr; this.count = 0;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(path.join(RAW, old));
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  full', this.prefix, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)).catch(() => {});
  }
}

async function openPage(browser, url, mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-CA',
    reducedMotion: 'reduce',
  });
  const page = await ctx.newPage();
  let status = null;
  let finalUrl = url;
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    status = resp && resp.status();
    finalUrl = page.url();
    await settle(page);
  } catch (e) {
    log('  OPEN FAIL', url, String(e.message).split('\n')[0]);
    await ctx.close();
    return null;
  }
  const host = new URL(finalUrl).hostname;
  const wall = host.startsWith('my.') || host.startsWith('app.') || /\/app\/(login|signup)/.test(finalUrl);
  return { ctx, page, vw, vh, dpr, status, finalUrl, wall };
}

const browser = await chromium.launch({ headless: true });
const manifest = [];

async function shootPair(name, url, { interactions = false } = {}) {
  for (const mobile of [false, true]) {
    const key = (mobile ? 'mobile-' : '') + name;
    if (only.size && !only.has(key) && !only.has(name)) continue;
    if (only.size && only.has(name) === false && only.has(key) === false) continue;
    log(key, url);
    const opened = await openPage(browser, url, mobile);
    if (!opened) {
      manifest.push({ name: key, url, error: 'open failed' });
      continue;
    }
    const { ctx, page, vw, vh, dpr, status, finalUrl, wall } = opened;
    const S = new Shooter(page, `${key}-light`, vw, vh, dpr);
    try {
      if (wall && !name.includes('login')) {
        log('  WALL', finalUrl);
        await S.view('wall');
        manifest.push({ name: key, url, finalUrl, status, wall: true, shots: S.count });
        await ctx.close();
        continue;
      }
      await S.view('default');
      if (name === 'home' && !mobile) await S.view('banner');
      await S.full();
      if (interactions) await runInteractions(page, S, mobile, name);
      if (name === 'login-wall') {
        const probe = await page.evaluate(() => {
          const inputs = [...document.querySelectorAll('input')].map((i) => ({ type: i.type, name: i.name, autocomplete: i.autocomplete, placeholder: i.placeholder }));
          const buttons = [...document.querySelectorAll('button, a')].map((b) => (b.innerText || b.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 30);
          return { inputs, buttons, title: document.title, url: location.href };
        });
        fs.writeFileSync(path.join(RAW, 'login-probe.json'), JSON.stringify(probe, null, 2));
        log('  login probe', JSON.stringify(probe.inputs), 'buttons', probe.buttons.slice(0, 12).join(' | '));
      }
      manifest.push({ name: key, url, finalUrl, status, wall, shots: S.count, inner: await page.evaluate(() => [innerWidth, innerHeight, devicePixelRatio]).catch(() => null) });
    } catch (e) {
      log('  FAIL', key, String(e.message).split('\n')[0]);
      manifest.push({ name: key, url, error: String(e.message).split('\n')[0], shots: S.count });
    }
    await ctx.close();
  }
}

async function runInteractions(page, S, mobile, name) {
  const step = async (label, fn) => {
    try { await fn(); } catch (e) { log('  skip', label, String(e.message).split('\n')[0]); }
  };
  if (name === 'home') {
    await step('banner-closed', async () => {
      const b = page.getByRole('button', { name: 'Close banner' });
      if (await b.count()) { await b.first().click({ timeout: 3000 }); await page.waitForTimeout(400); await S.view('banner-closed'); }
    });
    if (!mobile) {
      for (const label of ['Chequing', 'Trade', 'Borrow', 'Accounts', 'Business', 'Offers']) {
        await step('menu-' + label, async () => {
          const b = page.locator('header button, nav button').filter({ hasText: new RegExp('^' + label + '$') }).first();
          await b.click({ timeout: 3000 });
          await page.waitForTimeout(500);
          await S.view('menu-' + label.toLowerCase());
          await page.keyboard.press('Escape');
          await page.mouse.move(8, 860);
          await page.waitForTimeout(200);
        });
      }
      await step('search', async () => {
        await page.getByRole('button', { name: 'Open search' }).click({ timeout: 3000 });
        await page.waitForTimeout(400);
        await S.view('search-open');
        const field = page.getByPlaceholder("I'm looking for...");
        await field.click({ timeout: 2000 });
        await field.fill('TFSA');
        await page.waitForTimeout(700);
        await S.view('search-typed');
        await page.keyboard.press('Escape');
      });
      await step('button-states', async () => {
        const cta = page.getByRole('link', { name: 'Get started' }).first();
        await cta.hover();
        await page.waitForTimeout(250);
        await S.view('cta-hover');
        await cta.focus();
        await page.waitForTimeout(200);
        await S.view('cta-focus');
      });
    } else {
      await step('menu', async () => {
        const b = page.getByRole('button', { name: 'Menu' });
        if (await b.count()) {
          await b.first().click({ timeout: 3000 });
          await page.waitForTimeout(600);
          await S.view('menu');
          const group = page.getByRole('button', { name: 'Trade' }).last();
          if (await group.count()) {
            await group.click({ timeout: 2000 }).catch(() => {});
            await page.waitForTimeout(400);
            await S.view('menu-trade');
          }
        }
      });
      await step('search', async () => {
        const b = page.getByRole('button', { name: 'Open search' });
        if (await b.count()) {
          await b.first().click({ timeout: 3000 });
          await page.waitForTimeout(500);
          await S.view('search-open');
        }
      });
    }
  }
  if (name === 'pricing' && !mobile) {
    await step('tier', async () => {
      const tabs = page.getByRole('tab');
      const n = await tabs.count();
      if (n > 1) {
        await tabs.nth(1).click();
        await page.waitForTimeout(400);
        await S.view('tier-selected');
      }
    });
  }
  if (['chequing', 'pricing', 'credit-card', 'trade'].includes(name)) {
    await step('accordion', async () => {
      const btn = page.locator('button[aria-expanded="false"]').first();
      if (await btn.count()) {
        await btn.scrollIntoViewIfNeeded();
        await btn.click({ timeout: 3000 });
        await page.waitForTimeout(400);
        await S.view('accordion-open');
      }
    });
  }
  if (name === 'contact' || name === 'get-in-touch') {
    await step('field-focus', async () => {
      const field = page.locator('input[type="text"], input[type="email"], textarea').first();
      if (await field.count()) {
        await field.scrollIntoViewIfNeeded();
        await field.focus();
        await page.waitForTimeout(200);
        await S.view('field-focused');
      }
    });
  }
}

// Phase filter: CAPTURE_PHASE=pages|external|home
const phase = process.env.CAPTURE_PHASE || 'all';

if (phase === 'all' || phase === 'pages') {
  for (const [name, pathName] of PAGES) {
    const interactions = ['home', 'pricing', 'chequing', 'credit-card', 'trade', 'contact', 'get-in-touch'].includes(name);
    if (only.size && ![name, 'mobile-' + name].some((k) => only.has(k))) continue;
    await shootPair(name, BASE + pathName, { interactions });
  }
}
if (phase === 'all' || phase === 'external') {
  for (const [name, url] of EXTERNAL) {
    if (only.size && ![name, 'mobile-' + name].some((k) => only.has(k))) continue;
    await shootPair(name, url, { interactions: false });
  }
}

fs.writeFileSync(path.join(RAW, 'manifest.json'), JSON.stringify(manifest, null, 2));
log('done shots', manifest.reduce((n, m) => n + (m.shots || 0), 0), 'pages', manifest.length);
await browser.close();
