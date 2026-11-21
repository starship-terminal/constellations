// Skillshare public capture. Adapted from tools/kit/capture.
// Screenshots and computed styles from signed-out pages only.
// Never types an email, never submits a form, never clicks Google, Facebook,
// Apple, Sign In, or Sign Up.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/skillshare/tools/capture/public/shoot.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'skillshare', 'raw-shots');
const READ = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = {
  home: 'https://www.skillshare.com/en/',
  browse: 'https://www.skillshare.com/en/browse?via=header',
  illustration: 'https://www.skillshare.com/en/browse/illustration?via=footer',
  paths: 'https://www.skillshare.com/en/paths?via=header',
  projects: 'https://www.skillshare.com/en/projects?via=header',
  shop: 'https://www.skillshare.com/en/shop/digital-products?via=header',
  sessions: 'https://www.skillshare.com/en/one-on-one-sessions?via=header',
  about: 'https://www.skillshare.com/en/about',
  press: 'https://www.skillshare.com/en/press',
  blog: 'https://www.skillshare.com/en/blog/',
  affiliates: 'https://www.skillshare.com/en/affiliates',
  teach: 'https://www.skillshare.com/en/teach',
  gift: 'https://www.skillshare.com/gift/membership',
  teams: 'https://www.skillshare.com/en/for-teams/home',
  help: 'https://help.skillshare.com/hc/en-us',
  terms: 'https://www.skillshare.com/en/terms',
  privacy: 'https://www.skillshare.com/en/privacy',
  search: 'https://www.skillshare.com/en/search?query=watercolor',
  login: 'https://www.skillshare.com/en/login',
  careers: 'https://www.skillshare.com/en/careers',
};

const arg = (process.argv[2] || '').split(',').filter(Boolean);

async function hideConsent(page) {
  await page.addStyleTag({
    content: `
      .dg-consent-banner, [class*="dg-consent"], #onetrust-banner-sdk, [id*="onetrust"],
      [class*="onetrust"], [id*="cookieBanner"], iframe[src*="datagrail"],
      [class*="cookie-banner"], [id*="iubenda"], .ot-fade-in, .onetrust-pc-dark-filter,
      [role="dialog"][class*="cookie"], #cookiescript_injected { display: none !important; visibility: hidden !important; pointer-events: none !important; }
    `,
  }).catch(() => {});
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('div, aside, section')) {
      const t = (el.innerText || '').slice(0, 400);
      const cs = getComputedStyle(el);
      if ((cs.position === 'fixed' || cs.position === 'sticky') && /cookie|privacy choices|we value your privacy|consent/i.test(t) && t.length < 800) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
    document.documentElement.style.removeProperty('overflow');
    document.body && document.body.style.removeProperty('overflow');
  }).catch(() => {});
}

async function challenged(page) {
  const s = await page.evaluate(() => ({
    title: document.title,
    body: (document.body && document.body.innerText || '').slice(0, 300),
  })).catch(() => ({ title: '', body: '' }));
  return /just a moment|attention required/i.test(s.title)
    || /performing security verification|verify you are not a bot/i.test(s.body);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
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
    const h0 = await p.evaluate(() => document.documentElement.scrollHeight);
    const steps = Math.min(12, Math.ceil(h0 / 700));
    for (let i = 0; i < steps; i++) {
      await p.evaluate((y) => scrollTo(0, y), i * 700);
      await wait(p, 180);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
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
  }
}

async function openPage(browser, url, mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    locale: 'en-US',
    hasTouch: !!mobile,
  });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await wait(page, 2800);
  await hideConsent(page);
  const bad = await challenged(page);
  const metrics = await page.evaluate(() => ({
    url: location.href.split('?')[0],
    title: document.title,
    innerWidth, innerHeight, devicePixelRatio,
    scrollH: document.documentElement.scrollHeight,
  }));
  return { context, page, resp, bad, metrics, vw, vh, dpr };
}

const readings = { capturedAt: new Date().toISOString(), pages: {}, components: {} };

async function readBox(page, spec) {
  return page.evaluate((spec) => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
    function pick(spec) {
      if (spec.aria) {
        const el = [...document.querySelectorAll(spec.sel || 'a, button, [role="button"]')].find((n) => n.getAttribute('aria-label') === spec.aria);
        if (el) return el;
      }
      if (spec.text) {
        const re = new RegExp('^' + spec.text + '$', 'i');
        const els = [...document.querySelectorAll(spec.sel || 'a, button, [role="button"], h1, input')].filter((n) => {
          const r = n.getBoundingClientRect();
          const t = clean(n.innerText || n.getAttribute('aria-label') || n.getAttribute('placeholder') || '');
          return r.width > 0 && r.height > 0 && re.test(t);
        });
        const leaf = els.filter((n) => !els.some((o) => o !== n && n.contains(o)));
        return (leaf[0] || els[0]) || null;
      }
      if (spec.sel) return document.querySelector(spec.sel);
      return null;
    }
    const el = pick(spec);
    if (!el) return { missing: true };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return { missing: true, reason: 'zero box' };
    const pickProps = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle', 'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'boxShadow', 'outline', 'outlineOffset', 'height', 'width', 'textDecorationLine', 'opacity'];
    const style = {};
    for (const k of pickProps) style[k] = cs[k];
    return {
      tag: el.tagName,
      text: clean(el.innerText || el.getAttribute('aria-label') || '').slice(0, 80),
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      style,
    };
  }, spec);
}

async function cropEl(page, spec, file) {
  const box = await page.evaluate((spec) => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
    let el = null;
    if (spec.aria) {
      el = [...document.querySelectorAll(spec.sel || 'a, button')].find((n) => n.getAttribute('aria-label') === spec.aria);
    } else if (spec.text) {
      const re = new RegExp('^' + spec.text + '$', 'i');
      const els = [...document.querySelectorAll(spec.sel || 'a, button, [role="button"], h1, input')].filter((n) => {
        const r = n.getBoundingClientRect();
        const t = clean(n.innerText || n.getAttribute('aria-label') || n.getAttribute('placeholder') || '');
        return r.width > 8 && r.height > 8 && re.test(t);
      });
      const leaf = els.filter((n) => !els.some((o) => o !== n && n.contains(o)));
      el = leaf[0] || els[0];
    } else if (spec.sel) el = document.querySelector(spec.sel);
    if (!el) return null;
    el.scrollIntoView({ block: 'center', inline: 'nearest' });
    const r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  }, spec);
  if (!box || box.width < 2) return null;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 400),
  };
  const dest = path.join(CROPS, file);
  await page.screenshot({ path: dest, clip });
  return file;
}

const DESKTOP_SHOTS = ['home', 'browse', 'illustration', 'paths', 'projects', 'shop', 'sessions', 'about', 'press', 'blog', 'affiliates', 'teach', 'gift', 'teams', 'help', 'terms', 'privacy', 'search', 'login', 'careers'];
const MOBILE_SHOTS = ['home', 'browse', 'about', 'teach', 'blog', 'search', 'login'];

const browser = await chromium.launch({ headless: true, args: ['--disable-blink-features=AutomationControlled'] });

for (const name of DESKTOP_SHOTS) {
  if (arg.length && !arg.includes(name) && !arg.includes('desktop')) continue;
  log('desktop', name);
  let opened;
  try {
    opened = await openPage(browser, PAGES[name], false);
  } catch (e) {
    log('  FAIL open', name, String(e.message).split('\n')[0]);
    readings.pages[name] = { error: String(e.message).split('\n')[0] };
    continue;
  }
  const { context, page, bad, metrics } = opened;
  readings.pages[name] = { ...metrics, challenged: bad, status: opened.resp && opened.resp.status() };
  if (bad) {
    log('  CHALLENGE', name, metrics.title);
    await context.close();
    continue;
  }
  const S = new Shooter(page, `${name}-light`, opened.vw, opened.vh, opened.dpr);
  try {
    await S.view('default');
    if (name !== 'login') await S.full();
  } catch (e) {
    log('  shot fail', name, String(e.message).split('\n')[0]);
  }
  if (name === 'home') {
    try {
      const browse = page.locator('a').filter({ hasText: /^Browse$/ }).first();
      await browse.click({ timeout: 5000 });
      await wait(page, 900);
      await S.view('menu');
      await page.keyboard.press('Escape');
      await wait(page, 300);
    } catch (e) { log('  menu fail', String(e.message).split('\n')[0]); }
    try {
      const box = page.locator('[aria-label="Search box"]').first();
      await box.click({ timeout: 5000 });
      await wait(page, 500);
      await S.view('search-focus');
      await box.fill('watercolor');
      await wait(page, 900);
      await S.view('search-typed');
    } catch (e) { log('  search fail', String(e.message).split('\n')[0]); }
  }
  if (name === 'illustration') {
    try {
      const filters = page.getByRole('button', { name: 'Filters' });
      if (await filters.count()) {
        await filters.first().click({ timeout: 5000 });
        await wait(page, 900);
        await S.view('filters');
        await page.keyboard.press('Escape');
      }
    } catch (e) { log('  filters fail', String(e.message).split('\n')[0]); }
  }
  if (name === 'about') {
    try {
      const watch = page.getByRole('button', { name: /Watch Mimi/i });
      if (await watch.count()) {
        await watch.first().click({ timeout: 5000 });
        await wait(page, 1500);
        const u = page.url();
        if (!/auth\.skillshare|login|signup/i.test(u)) await S.view('video');
        else log('  video went to auth, stopped', u.split('?')[0]);
        await page.keyboard.press('Escape');
      }
    } catch (e) { log('  video fail', String(e.message).split('\n')[0]); }
  }
  await context.close();
}

for (const name of MOBILE_SHOTS) {
  const key = 'mobile-' + name;
  if (arg.length && !arg.includes(key) && !arg.includes('mobile')) continue;
  log('mobile', name);
  let opened;
  try {
    opened = await openPage(browser, PAGES[name], true);
  } catch (e) {
    log('  FAIL open', key, String(e.message).split('\n')[0]);
    continue;
  }
  const { context, page, bad, metrics } = opened;
  readings.pages[key] = { ...metrics, challenged: bad };
  if (bad) {
    log('  CHALLENGE', key);
    await context.close();
    continue;
  }
  if (metrics.innerWidth !== 390) log('  viewport width', metrics.innerWidth, 'expected 390');
  const S = new Shooter(page, `${key}-light`, opened.vw, opened.vh, opened.dpr);
  try {
    await S.view('default');
    if (name !== 'login') await S.full();
  } catch (e) {
    log('  shot fail', key, String(e.message).split('\n')[0]);
  }
  if (name === 'home') {
    try {
      await page.locator('svg.ss-icon-hamburger, [class*="hamburger"]').first().click({ timeout: 5000 });
      await wait(page, 900);
      await S.view('menu');
    } catch (e) { log('  drawer fail', String(e.message).split('\n')[0]); }
  }
  await context.close();
}

// Component readings on desktop home + browse + login (fields only, not filled).
{
  log('measure');
  const opened = await openPage(browser, PAGES.home, false);
  const { page, context } = opened;
  const specs = {
    'logo': { aria: 'Home', sel: 'a' },
    'nav-browse': { text: 'Browse', sel: 'a, button' },
    'nav-signin': { text: 'Sign In', sel: 'a, button' },
    'btn-signup': { text: 'Sign Up', sel: 'button' },
    'search': { aria: 'Search box', sel: 'input' },
    'hero-title': { sel: 'h1' },
    'btn-google': { text: 'Continue with Google', sel: 'button' },
    'btn-email': { text: 'Continue with email', sel: 'button' },
    'link-terms': { text: 'Terms of Service', sel: 'a' },
  };
  for (const [key, spec] of Object.entries(specs)) {
    const reading = await readBox(page, spec);
    readings.components[key] = { page: 'home', ...reading };
    if (!reading.missing) {
      try { await cropEl(page, spec, `${key}-default.png`); } catch (e) { log('  crop fail', key, e.message); }
    } else log('  miss', key);
  }
  // hover signup
  try {
    const btn = page.locator('button').filter({ hasText: /^Sign Up$/ }).first();
    await btn.hover();
    await wait(page, 300);
    const reading = await readBox(page, { text: 'Sign Up', sel: 'button' });
    readings.components['btn-signup-hover'] = reading;
    await cropEl(page, { text: 'Sign Up', sel: 'button' }, 'btn-signup-hover.png');
  } catch (e) { log('  hover fail', e.message); }
  await context.close();
}

{
  const opened = await openPage(browser, PAGES.login, false);
  const { page, context, bad } = opened;
  if (!bad) {
    const spec = { sel: 'input[type="email"]' };
    readings.components['field-email'] = { page: 'login', ...(await readBox(page, spec)) };
    try { await cropEl(page, spec, 'field-email-default.png'); } catch (e) { log('  email crop', e.message); }
  }
  await context.close();
}

fs.writeFileSync(path.join(READ, 'capture-readings.json'), JSON.stringify(readings, null, 2));
log('readings', Object.keys(readings.components).length, 'components', Object.keys(readings.pages).length, 'pages');
await browser.close();
