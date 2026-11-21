// Public Glassnode tour. Headless Chromium, signed out.
//
//   PLAYWRIGHT=... node tools/capture/tour.mjs
//
// Walks glassnode.com and the public Studio shell. Cookie banner: Deny only.
// Login and signup are opened and photographed empty. Nothing is typed or submitted.
// Auth0 state query strings are stripped before any URL is written.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'glassnode', 'raw-shots');
const OUT = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const tree = [];
const note = (row) => { tree.push(row); log('tree', row.from, '->', row.opens, row.url || ''); };

function safeUrl(u) {
  try {
    const x = new URL(u);
    for (const k of [...x.searchParams.keys()]) {
      if (/state|code|token|session|email|nonce/i.test(k)) x.searchParams.delete(k);
    }
    return x.origin + x.pathname + (x.search ? x.search : '');
  } catch {
    return '';
  }
}

async function denyCookies(page) {
  for (let i = 0; i < 8; i++) {
    const hit = await page.evaluate(() => {
      const root = document.querySelector('#usercentrics-root');
      const sr = root?.shadowRoot;
      if (!sr) return '';
      const deny = [...sr.querySelectorAll('button')].find((b) => /^deny$/i.test((b.innerText || '').trim()));
      if (deny) { deny.click(); return 'Deny'; }
      return '';
    }).catch(() => '');
    if (hit) return hit;
    await page.waitForTimeout(350);
  }
  return '';
}

async function shot(page, name, requested) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, { ...requested, sanitizedSourceUrl: safeUrl(page.url()) });
  log('shot', name);
  return file;
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await page.evaluate((yy) => scrollTo(0, yy), y);
    await page.waitForTimeout(180);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(400);
}

class Ctx {
  constructor(browser, mobile) {
    this.browser = browser;
    this.mobile = mobile;
    this.vw = mobile ? 390 : 1440;
    this.vh = mobile ? 844 : 900;
    this.dpr = mobile ? 2 : 1;
    this.prefix = mobile ? 'mobile-' : '';
    this.requested = { viewport: { width: this.vw, height: this.vh }, deviceScaleFactor: this.dpr };
  }
  async open() {
    this.context = await this.browser.newContext({
      viewport: { width: this.vw, height: this.vh },
      deviceScaleFactor: this.dpr,
      userAgent: this.mobile ? UA_MOBILE : UA,
      isMobile: this.mobile,
      hasTouch: this.mobile,
      locale: 'en-US',
    });
    this.page = await this.context.newPage();
    this.page.setDefaultTimeout(12000);
  }
  async close() { await this.context.close(); }
  async goto(url, wait = 2800) {
    const res = await this.page.goto(url, { waitUntil: 'load', timeout: 70000 });
    await this.page.waitForTimeout(wait);
    const denied = await denyCookies(this.page);
    if (denied) await this.page.waitForTimeout(500);
    const info = await this.page.evaluate(() => ({
      href: location.href,
      title: document.title,
      h1: [...document.querySelectorAll('h1')].slice(0, 2).map((e) => e.innerText.trim().replace(/\s+/g, ' ').slice(0, 80)),
      statusText: (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 180),
    }));
    return { status: res?.status() ?? null, denied, ...info, url: safeUrl(info.href) };
  }
  name(page, state) { return `${this.prefix}${page}-light-${state}`; }
}

const MARKETING = [
  ['home', 'https://glassnode.com/'],
  ['about', 'https://glassnode.com/about'],
  ['data', 'https://glassnode.com/products/data'],
  ['studio-product', 'https://glassnode.com/products/studio'],
  ['research-product', 'https://glassnode.com/products/research'],
  ['vector', 'https://glassnode.com/pricing/vector'],
  ['alpha-lab-product', 'https://glassnode.com/products/studio/alpha-lab'],
  ['contact', 'https://glassnode.com/contact'],
  ['stories', 'https://glassnode.com/customer-stories'],
  ['events', 'https://glassnode.com/events'],
  ['solutions-trading', 'https://glassnode.com/solutions/trading-and-investing'],
  ['solutions-content', 'https://glassnode.com/solutions/crypto-content-creation'],
  ['market-compass-product', 'https://glassnode.com/products/studio/market-compass'],
];

const browser = await chromium.launch({ headless: true });
const desk = new Ctx(browser, false);
await desk.open();

// --- marketing pages ---
for (const [key, url] of MARKETING) {
  try {
    const info = await desk.goto(url);
    note({ from: key === 'home' ? 'start' : 'direct', control: key, opens: 'page', url: info.url, status: info.status, title: info.title, h1: info.h1, cookies: info.denied || 'none' });
    if (/just a moment|attention required|cf-browser-verification|datadome|access denied/i.test(info.statusText + info.title)) {
      note({ from: key, control: 'load', opens: 'block', url: info.url, status: info.status, vendor: 'unknown' });
      continue;
    }
    await shot(desk.page, desk.name(key, 'default'), desk.requested);
    if (key === 'home' || key === 'about' || key === 'data' || key === 'contact') {
      await lazyScroll(desk.page);
      await shot(desk.page, desk.name(key, 'full'), { ...desk.requested });
      // full page via screenshot helper
      await screenshotWithMetadata(desk.page, { path: path.join(RAW, desk.name(key, 'full') + '.png'), fullPage: true }, { ...desk.requested, sanitizedSourceUrl: safeUrl(desk.page.url()) });
    }
  } catch (e) {
    note({ from: key, control: 'load', opens: 'error', detail: String(e.message).split('\n')[0] });
    log('FAIL', key, e.message.split('\n')[0]);
  }
}

// Products dropdown
await desk.goto('https://glassnode.com/');
await desk.page.evaluate(() => scrollTo(0, 0));
await desk.page.getByRole('button', { name: 'Products', exact: true }).click();
await desk.page.waitForTimeout(600);
const productLinks = await desk.page.evaluate(() => [...document.querySelectorAll('a')].filter((a) => {
  const r = a.getBoundingClientRect();
  return r.top > 40 && r.top < 280 && r.height > 8;
}).map((a) => ({ text: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80), href: a.getAttribute('href') })));
note({ from: 'home header', control: 'Products button', opens: 'dropdown', items: productLinks });
await shot(desk.page, desk.name('home', 'products-menu'), desk.requested);
await desk.page.keyboard.press('Escape');

// metrics carousel
await desk.page.evaluate(() => scrollTo(0, 2600));
await desk.page.waitForTimeout(400);
const next = desk.page.getByRole('button', { name: 'Next metrics' });
if (await next.count()) {
  await next.click();
  await desk.page.waitForTimeout(700);
  note({ from: 'home', control: 'Next metrics', opens: 'carousel step' });
  await shot(desk.page, desk.name('home', 'metrics-next'), desk.requested);
}

// newsletter field: focus only, type nothing, do not submit
await desk.goto('https://glassnode.com/');
const email = desk.page.locator('input[placeholder="Enter your email"]').first();
if (await email.count()) {
  await email.scrollIntoViewIfNeeded();
  await email.focus();
  await desk.page.waitForTimeout(300);
  note({ from: 'home', control: 'Send me free research email field', opens: 'focus only; not typed, not submitted' });
  await shot(desk.page, desk.name('home', 'newsletter-focused'), desk.requested);
  await email.evaluate((el) => el.blur());
}

// contact category buttons: open the chooser, do not fill the form
await desk.goto('https://glassnode.com/contact');
const cats = await desk.page.evaluate(() => [...document.querySelectorAll('button, a')].filter((e) => /contact sales|general inquiries|press|support/i.test(e.innerText || '')).map((e) => (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60)));
note({ from: 'contact', control: 'category cards', opens: 'chooser visible', items: cats });
await shot(desk.page, desk.name('contact', 'chooser'), desk.requested);

// data metric filter: type a public query word, do not submit a lead form
await desk.goto('https://glassnode.com/products/data');
const metricSearch = desk.page.getByRole('searchbox', { name: /search metrics/i }).or(desk.page.locator('input[placeholder="Search metrics"]'));
if (await metricSearch.count()) {
  await metricSearch.first().scrollIntoViewIfNeeded();
  await metricSearch.first().click();
  await metricSearch.first().fill('active');
  await desk.page.waitForTimeout(700);
  note({ from: 'data', control: 'Search metrics', opens: 'filter', query: 'active' });
  await shot(desk.page, desk.name('data', 'metrics-filtered'), desk.requested);
  await metricSearch.first().fill('');
}

// --- Studio public shell ---
const studioInfo = await desk.goto('https://studio.glassnode.com/', 3500);
note({ from: 'marketing Launch Studio', control: 'Launch Studio', opens: 'studio home', url: studioInfo.url, status: studioInfo.status, title: studioInfo.title });
await shot(desk.page, desk.name('studio-home', 'default'), desk.requested);

// search
await desk.page.getByRole('button', { name: 'search' }).click();
await desk.page.waitForTimeout(700);
note({ from: 'studio header', control: 'search button', opens: 'search overlay' });
await shot(desk.page, desk.name('studio-home', 'search'), desk.requested);
await desk.page.keyboard.press('Escape');
await desk.page.waitForTimeout(300);

// resources menu
await desk.page.getByText('Resources', { exact: true }).first().click();
await desk.page.waitForTimeout(600);
const resources = await desk.page.evaluate(() => [...document.querySelectorAll('a')].filter((a) => {
  const r = a.getBoundingClientRect();
  return r.top > 40 && r.top < 420 && r.height > 8 && r.width > 40;
}).map((a) => ({ text: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60), href: a.href })));
note({ from: 'studio header', control: 'Resources', opens: 'menu', items: resources.map((r) => ({ text: r.text, href: safeUrl(r.href) })) });
await shot(desk.page, desk.name('studio-home', 'resources'), desk.requested);
await desk.page.keyboard.press('Escape');

// changelog icon button
const iconBtn = desk.page.locator('button.ant-btn-icon-only').first();
if (await iconBtn.count()) {
  await iconBtn.click();
  await desk.page.waitForTimeout(700);
  note({ from: 'studio header', control: 'icon-only button (changelog)', opens: 'popover' });
  await shot(desk.page, desk.name('studio-home', 'changelog'), desk.requested);
  await desk.page.keyboard.press('Escape');
}

// period radios on studio home (1h / 24h / 7d) — public filter, not a form submit
const period = desk.page.getByText('7d', { exact: true }).first();
if (await period.count()) {
  await period.click();
  await desk.page.waitForTimeout(800);
  note({ from: 'studio home', control: '7d period', opens: 'filter' });
  await shot(desk.page, desk.name('studio-home', 'period-7d'), desk.requested);
}

const studioPages = [
  ['studio-pricing', 'https://studio.glassnode.com/pricing'],
  ['studio-charts', 'https://studio.glassnode.com/charts?a=BTC'],
  ['studio-dashboards', 'https://studio.glassnode.com/dashboards?a=BTC'],
  ['studio-compass', 'https://studio.glassnode.com/market-compass'],
  ['studio-catalog', 'https://studio.glassnode.com/catalog'],
  ['studio-login-404', 'https://studio.glassnode.com/login'],
];
for (const [key, url] of studioPages) {
  try {
    const info = await desk.goto(url, 3000);
    note({ from: 'studio nav or direct', control: key, opens: 'page', url: info.url, status: info.status, title: info.title, h1: info.h1 });
    await shot(desk.page, desk.name(key, 'default'), desk.requested);
    if (key === 'studio-pricing') {
      await screenshotWithMetadata(desk.page, { path: path.join(RAW, desk.name(key, 'full') + '.png'), fullPage: true }, { ...desk.requested, sanitizedSourceUrl: safeUrl(desk.page.url()) });
    }
  } catch (e) {
    note({ from: key, control: 'load', opens: 'error', detail: String(e.message).split('\n')[0] });
  }
}

// charts asset switch if a public control exists
await desk.goto('https://studio.glassnode.com/charts?a=BTC', 3000);
const asset = desk.page.getByRole('button', { name: /BTC|Bitcoin/i }).first();
if (await asset.count()) {
  await asset.click().catch(() => {});
  await desk.page.waitForTimeout(600);
  note({ from: 'studio charts', control: 'asset control', opens: 'menu or picker if it opened' });
  await shot(desk.page, desk.name('studio-charts', 'asset'), desk.requested);
  await desk.page.keyboard.press('Escape');
}

// Login wall: click Log in, photograph empty form, type nothing
await desk.goto('https://studio.glassnode.com/', 2500);
await desk.page.getByRole('button', { name: 'Log in', exact: true }).click();
await desk.page.waitForTimeout(2500);
const loginUrl = safeUrl(desk.page.url());
const loginText = await desk.page.evaluate(() => (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 500));
note({ from: 'studio header', control: 'Log in', opens: 'auth wall', url: loginUrl, offered: 'email, password, reset password, continue, sign up, continue with Google', typed: false });
await shot(desk.page, desk.name('login', 'empty'), desk.requested);
await screenshotWithMetadata(desk.page, { path: path.join(RAW, desk.name('login', 'empty-full') + '.png'), fullPage: true }, { ...desk.requested, sanitizedSourceUrl: loginUrl });

// Sign up wall: open, photograph, do not fill
await desk.goto('https://studio.glassnode.com/', 2000);
await desk.page.getByRole('button', { name: 'Sign up', exact: true }).click();
await desk.page.waitForTimeout(2500);
const signupUrl = safeUrl(desk.page.url());
const signupText = await desk.page.evaluate(() => (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 500));
note({ from: 'studio header', control: 'Sign up', opens: 'auth wall', url: signupUrl, typed: false });
await shot(desk.page, desk.name('signup', 'empty'), desk.requested);

fs.writeFileSync(path.join(OUT, 'login-walls.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  login: { url: loginUrl, text: loginText, typed: false, submitted: false },
  signup: { url: signupUrl, text: signupText, typed: false, submitted: false },
}, null, 2) + '\n');

await desk.close();

// --- phone ---
const phone = new Ctx(browser, true);
await phone.open();
for (const [key, url] of [['home', 'https://glassnode.com/'], ['studio-home', 'https://studio.glassnode.com/'], ['data', 'https://glassnode.com/products/data']]) {
  try {
    const info = await phone.goto(url, 3000);
    note({ from: 'phone', control: key, opens: 'page', url: info.url, status: info.status, width: 390 });
    await shot(phone.page, phone.name(key, 'default'), phone.requested);
  } catch (e) {
    note({ from: 'phone ' + key, control: 'load', opens: 'error', detail: String(e.message).split('\n')[0] });
  }
}
// mobile menu if a hamburger exists
const burger = phone.page.locator('button').filter({ hasText: /menu/i }).or(phone.page.getByRole('button', { name: /menu|open/i }));
const headerBtns = await phone.page.evaluate(() => [...document.querySelectorAll('button')].filter((e) => e.getBoundingClientRect().top < 80 && e.getBoundingClientRect().height > 8).map((e) => ({
  text: (e.innerText || e.getAttribute('aria-label') || '').trim().slice(0, 40),
  x: Math.round(e.getBoundingClientRect().x),
})));
note({ from: 'phone studio or last page', control: 'header buttons', opens: 'inventory', items: headerBtns });
if (headerBtns.length) {
  const last = headerBtns[headerBtns.length - 1];
  await phone.page.mouse.click(last.x + 8, 36);
  await phone.page.waitForTimeout(700);
  note({ from: 'phone', control: 'last header button', opens: 'possible menu' });
  await shot(phone.page, phone.name('nav', 'open'), phone.requested);
}
await phone.goto('https://glassnode.com/', 2500);
const mBtns = await phone.page.evaluate(() => [...document.querySelectorAll('button, a')].filter((e) => {
  const r = e.getBoundingClientRect();
  return r.top < 80 && r.height > 8;
}).map((e) => ({ text: (e.innerText || e.getAttribute('aria-label') || '').trim().slice(0, 40), x: Math.round(e.getBoundingClientRect().x), tag: e.tagName })));
note({ from: 'phone marketing', control: 'header', opens: 'inventory', items: mBtns });
await shot(phone.page, phone.name('home', 'header'), phone.requested);
await phone.close();
await browser.close();

fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2) + '\n');
log('done', tree.length, 'tree rows');
