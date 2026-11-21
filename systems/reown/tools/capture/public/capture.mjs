// Reown public capture. Adapted from the kit's public route.
// No form submits, no auth, no newsletter, no Google/Apple.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/reown/tools/capture/public/capture.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'reown', 'raw-shots');
const OUT = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const AUTH = /sign-in|sign-up|signin|signup|\/login|accounts\.google|appleid\.apple|oauth/i;

function sanitizeUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.toString();
  } catch {
    return null;
  }
}

async function launch(mobile) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { browser, context };
}

async function hideOverlays(page) {
  // Hide, never click. Cookie banners and announcement bars stay recorded in their own shots.
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('[class*="cookie" i], [id*="cookie" i], [class*="consent" i]')) {
      const t = (el.innerText || '').slice(0, 200);
      if (/cookie|consent/i.test(t) && el.getBoundingClientRect().height > 40) el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function shot(page, name, requested, opts = {}) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file, ...opts }, { ...requested, sanitizedSourceUrl: sanitizeUrl(page.url()) });
  log('shot', name);
  return file;
}

async function full(page, name, requested) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * Math.floor(14000 / (requested.deviceScaleFactor || 1)));
  for (let y = 0; y < Math.min(h, 6000); y += 700) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await wait(page, 120);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 400);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const dpr = requested.deviceScaleFactor || 1;
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log('  truncated', name, H, '->', hCap);
  if (hCap <= chunk) await shot(page, name, requested, { fullPage: true });
  else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await shot(page, `${name}.part${i}`, requested, { fullPage: true, clip: { x: 0, y, width: requested.viewport.width, height: Math.min(chunk, hCap - y) } });
    }
  }
}

async function goto(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await wait(page, 1600);
  const finalUrl = page.url();
  if (AUTH.test(finalUrl) && !AUTH.test(url)) {
    log('AUTH WALL', url, '->', sanitizeUrl(finalUrl));
    return { wall: true, status: resp && resp.status(), finalUrl: sanitizeUrl(finalUrl) };
  }
  return { wall: false, status: resp && resp.status(), finalUrl: sanitizeUrl(finalUrl) };
}

async function openNav(page) {
  const btn = page.getByRole('button', { name: 'Navigation Toggle' });
  if (await btn.count()) {
    await btn.click();
    await wait(page, 600);
    return true;
  }
  return false;
}

async function openMenu(page, name) {
  const btn = page.getByRole('button', { name, exact: true });
  if (await btn.count()) {
    await btn.first().click();
    await wait(page, 400);
    return true;
  }
  return false;
}

const MARKETING = [
  ['home', 'https://reown.com/'],
  ['pricing', 'https://reown.com/pricing'],
  ['learn', 'https://reown.com/learn'],
  ['solutions-analytics', 'https://reown.com/solutions/analytics'],
  ['solutions-authentication', 'https://reown.com/solutions/authentication'],
  ['solutions-transactions', 'https://reown.com/solutions/transactions'],
  ['solutions-compliance', 'https://reown.com/solutions/compliance'],
  ['use-cases-defi', 'https://reown.com/use-cases/defi'],
  ['use-cases-marketplaces', 'https://reown.com/use-cases/marketplaces'],
  ['use-cases-gaming', 'https://reown.com/use-cases/gaming'],
  ['use-cases-social', 'https://reown.com/use-cases/social'],
  ['about', 'https://reown.com/about-reown'],
  ['blog', 'https://reown.com/blog'],
  ['careers', 'https://reown.com/careers'],
  ['contact', 'https://reown.com/contact'],
  ['faq', 'https://reown.com/faq'],
  ['security', 'https://reown.com/security'],
  ['sdk', 'https://reown.com/reown-sdk'],
  ['state-of-defi', 'https://reown.com/state-of-defi-2026'],
  ['privacy', 'https://reown.com/privacy-policy'],
  ['terms', 'https://reown.com/terms-of-service'],
  ['cookies', 'https://reown.com/cookie-policy'],
  ['login-404', 'https://reown.com/login'],
];

const only = (process.env.ONLY || '').split(',').filter(Boolean);

function want(name) {
  return !only.length || only.some((o) => name.includes(o));
}

async function captureMarketing(mobile) {
  const prefix = mobile ? 'mobile-' : '';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const { browser, context } = await launch(mobile);
  const page = await context.newPage();
  const pages = [];
  try {
    for (const [name, url] of MARKETING) {
      const shotName = prefix + name;
      if (!want(shotName)) continue;
      log('page', shotName);
      const nav = await goto(page, url);
      pages.push({ name: shotName, url, ...nav, title: await page.title() });
      if (nav.wall) {
        await shot(page, shotName + '-light-auth-wall', requested);
        continue;
      }
      if (name === 'home') {
        await shot(page, shotName + '-light-announcement', requested);
        const close = page.getByRole('button', { name: 'Close announcement' });
        if (await close.count()) { await close.click().catch(() => {}); await wait(page, 400); }
      }
      await hideOverlays(page);
      await shot(page, shotName + '-light-default', requested);
      if (['home', 'pricing', 'learn', 'blog', 'about', 'faq', 'solutions-authentication'].includes(name)) {
        await full(page, shotName + '-light-full', requested);
      }
      if (name === 'home') {
        if (await openNav(page)) {
          await shot(page, shotName + '-light-nav', requested);
          if (await openMenu(page, 'Solutions')) await shot(page, shotName + '-light-nav-solutions', requested);
          if (await openMenu(page, 'Use Cases')) await shot(page, shotName + '-light-nav-usecases', requested);
          if (await openMenu(page, 'Company')) await shot(page, shotName + '-light-nav-company', requested);
          await page.keyboard.press('Escape').catch(() => {});
          await wait(page, 300);
        }
        // Contact sales dialog: open, screenshot, close. Do not fill or submit.
        const sales = page.getByRole('button', { name: /contact sales/i }).first();
        if (await sales.count()) {
          await sales.click().catch(() => {});
          await wait(page, 1200);
          await shot(page, shotName + '-light-contact-dialog', requested);
          await page.keyboard.press('Escape').catch(() => {});
          await wait(page, 300);
        }
      }
      if (name === 'pricing' || name === 'faq' || name === 'solutions-authentication') {
        const acc = page.locator('button').filter({ hasText: /\?$/ }).first();
        if (await acc.count()) {
          await acc.click().catch(() => {});
          await wait(page, 500);
          await shot(page, shotName + '-light-accordion', requested);
        }
      }
      if (name === 'learn' || name === 'blog') {
        const chip = page.getByRole('button', { name: name === 'learn' ? 'Solana Ecosystem' : 'Product Updates' });
        if (await chip.count()) {
          await chip.click().catch(() => {});
          await wait(page, 600);
          await shot(page, shotName + '-light-filter', requested);
        }
      }
    }
  } finally {
    await browser.close();
  }
  return pages;
}

async function captureDocs(mobile) {
  const prefix = mobile ? 'mobile-' : '';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  if (!want(prefix + 'docs') && !want(prefix + 'docs-dark')) return [];
  const { browser, context } = await launch(mobile);
  const page = await context.newPage();
  const pages = [];
  try {
    log('docs', prefix);
    await goto(page, 'https://docs.reown.com/');
    await wait(page, 800);
    await shot(page, prefix + 'docs-light-default', requested);
    if (!mobile) await full(page, prefix + 'docs-light-full', requested);
    const search = page.getByRole('button', { name: /Search/ });
    if (await search.count()) {
      await search.first().click().catch(() => {});
      await wait(page, 700);
      await shot(page, prefix + 'docs-light-search', requested);
      await page.keyboard.press('Escape').catch(() => {});
      await wait(page, 300);
    }
    if (!mobile) {
      const theme = page.getByRole('button', { name: 'Change theme preference' });
      if (await theme.count()) {
        await theme.click();
        await wait(page, 400);
        await shot(page, prefix + 'docs-light-theme-menu', requested);
        const dark = page.getByRole('menuitem', { name: /Dark/ });
        if (await dark.count()) await dark.first().click({ force: true }).catch(() => {});
        await wait(page, 800);
        await shot(page, prefix + 'docs-dark-default', requested);
      }
    } else {
      const menu = page.getByRole('button', { name: /menu|open navigation|sidebar/i });
      if (await menu.count()) {
        await menu.first().click().catch(() => {});
        await wait(page, 600);
        await shot(page, prefix + 'docs-light-nav', requested);
      }
    }
    await goto(page, 'https://docs.reown.com/appkit/overview');
    await wait(page, 600);
    await shot(page, prefix + 'docs-appkit-light-default', requested);
    pages.push({ name: prefix + 'docs', url: 'https://docs.reown.com/' });
  } finally {
    await browser.close();
  }
  return pages;
}

async function captureDemo(mobile) {
  const prefix = mobile ? 'mobile-' : '';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  if (!want(prefix + 'demo')) return [];
  const { browser, context } = await launch(mobile);
  const page = await context.newPage();
  try {
    log('demo', prefix);
    await goto(page, 'https://demo.reown.com/');
    await wait(page, 1200);
    await shot(page, prefix + 'demo-dark-auth', requested);
    const features = page.getByRole('tab', { name: 'Features' });
    if (await features.count()) {
      await features.click();
      await wait(page, 500);
      await shot(page, prefix + 'demo-dark-features', requested);
    }
    const design = page.getByRole('tab', { name: 'Design' });
    if (await design.count()) {
      await design.click();
      await wait(page, 500);
      await shot(page, prefix + 'demo-dark-design', requested);
      const light = page.getByRole('button', { name: 'Light', exact: true }).or(page.getByText('Light', { exact: true }));
      if (await light.count()) {
        await light.first().click().catch(() => {});
        await wait(page, 500);
        await shot(page, prefix + 'demo-dark-design-light-mode', requested);
      }
    }
    await page.getByRole('tab', { name: 'Auth' }).click().catch(() => {});
    await wait(page, 300);
    const gs = page.getByRole('button', { name: 'Get started' }).or(page.getByRole('link', { name: 'Get started' }));
    if (await gs.count()) {
      await gs.first().click().catch(() => {});
      await wait(page, 1500);
      const url = page.url();
      if (AUTH.test(url)) log('AUTH WALL from Get started', sanitizeUrl(url));
      await shot(page, prefix + 'demo-dark-connect-modal', requested);
      await page.keyboard.press('Escape').catch(() => {});
    }
    const networks = page.getByRole('button', { name: 'Open networks' });
    if (await networks.count()) {
      await networks.click().catch(() => {});
      await wait(page, 500);
      await shot(page, prefix + 'demo-dark-networks', requested);
    }
  } finally {
    await browser.close();
  }
  return [{ name: prefix + 'demo', url: 'https://demo.reown.com/' }];
}

async function captureStatus() {
  if (!want('status')) return [];
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const { browser, context } = await launch(false);
  const page = await context.newPage();
  try {
    await goto(page, 'https://status.reown.com/');
    await wait(page, 1200);
    await shot(page, 'status-light-default', requested);
    const sub = page.getByRole('button', { name: /subscribe/i });
    if (await sub.count()) {
      await sub.first().click().catch(() => {});
      await wait(page, 700);
      await shot(page, 'status-light-subscribe-dialog', requested);
      await page.keyboard.press('Escape').catch(() => {});
    }
  } finally {
    await browser.close();
  }
  return [{ name: 'status', url: 'https://status.reown.com/' }];
}

async function captureAuthWall() {
  if (!want('auth-wall')) return [];
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const { browser, context } = await launch(false);
  const page = await context.newPage();
  try {
    const nav = await goto(page, 'https://cloud.reown.com/sign-in');
    log('auth wall', nav);
    await shot(page, 'dashboard-signin-light-wall', requested);
    return [{ name: 'dashboard-signin', ...nav }];
  } finally {
    await browser.close();
  }
}

const index = { capturedAt: new Date().toISOString(), pages: [] };
index.pages.push(...await captureMarketing(false));
index.pages.push(...await captureMarketing(true));
index.pages.push(...await captureDocs(false));
index.pages.push(...await captureDocs(true));
index.pages.push(...await captureDemo(false));
index.pages.push(...await captureDemo(true));
index.pages.push(...await captureStatus());
index.pages.push(...await captureAuthWall());
fs.writeFileSync(path.join(OUT, 'capture-index.json'), JSON.stringify(index, null, 2));
log('done', index.pages.length, 'pages');
