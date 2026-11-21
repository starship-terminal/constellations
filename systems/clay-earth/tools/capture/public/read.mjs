// Live public capture for Clay (clay.earth), which 301s to me.sh (Mesh).
// Reads custom properties, computed controls, and screenshots. Does not submit
// forms, follow identity providers, or start installer downloads.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node read.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..', '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(PKG, 'screenshots');
const CROPS = path.join(PKG, 'components', 'crops');
const SCRATCH = path.join(os.homedir(), '.design-systems', 'clay-earth', 'raw-shots');
for (const d of [RAW, SHOTS, CROPS, SCRATCH]) fs.mkdirSync(d, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PAGES = [
  ['home', 'https://me.sh/'],
  ['pricing', 'https://me.sh/pricing'],
  ['integrations', 'https://me.sh/integrations'],
  ['nexus', 'https://me.sh/nexus'],
  ['teams', 'https://me.sh/teams'],
  ['stories', 'https://me.sh/stories'],
  ['start', 'https://me.sh/start'],
  ['about', 'https://me.sh/about'],
  ['contact', 'https://me.sh/contact'],
  ['login-wall', 'https://app.me.sh/login?signin'],
];

function styleOf(cs, extra = {}) {
  const pick = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
    'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
    'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width',
    'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
    'textDecorationLine', 'opacity', 'gap'];
  const out = {};
  for (const k of pick) out[k] = cs[k];
  return { ...out, ...extra };
}

async function readVars(page) {
  return page.evaluate(async () => {
    const sheets = [];
    for (const sh of document.styleSheets) {
      let rules = 0;
      let blocked = false;
      try { rules = sh.cssRules ? sh.cssRules.length : 0; } catch { blocked = true; }
      sheets.push({ href: sh.href, rules, blocked });
    }
    const names = new Set();
    const walk = (list) => {
      for (const r of list) {
        if (r.style) {
          for (const prop of r.style) if (prop.startsWith('--')) names.add(prop);
        }
        if (r.cssRules) walk(r.cssRules);
      }
    };
    for (const sh of document.styleSheets) {
      try { walk(sh.cssRules); } catch { /* cross-origin */ }
    }
    const cs = getComputedStyle(document.documentElement);
    const resolved = {};
    for (const n of [...names].sort()) {
      const v = cs.getPropertyValue(n).trim();
      if (v) resolved[n] = v.slice(0, 240);
    }
    const theme = document.querySelector('meta[name="theme-color"]')?.content || null;
    const mask = document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null;
    return {
      url: location.href,
      title: document.title,
      themeColor: theme,
      maskIconColor: mask,
      htmlClass: document.documentElement.className,
      colorScheme: cs.colorScheme,
      background: cs.backgroundColor,
      color: cs.color,
      fontFamily: cs.fontFamily,
      sheets,
      varCount: Object.keys(resolved).length,
      vars: resolved,
    };
  });
}

async function measureEl(page, handle, label) {
  if (!handle) return { label, missing: true };
  const box = await handle.boundingBox();
  const data = await handle.evaluate((el) => {
    const cs = getComputedStyle(el);
    const pick = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderRadius',
      'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop',
      'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'boxShadow', 'outline',
      'textTransform', 'opacity'];
    const style = {};
    for (const k of pick) style[k] = cs[k];
    return {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      style,
    };
  });
  return { label, box, ...data };
}

async function cropEl(page, handle, file) {
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  await page.screenshot({ path: file, clip });
  return clip;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  userAgent: UA,
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(12000);

const readings = { capturedAt: new Date().toISOString(), pages: {}, components: {} };

async function openPage(url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1400);
  return res ? res.status() : null;
}

async function shoot(name, opts = {}) {
  const dest = path.join(SHOTS, name + '.png');
  await screenshotWithMetadata(page, { path: dest, ...opts }, {
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    sanitizedSourceUrl: page.url().split('?')[0],
  });
  log('shot', name);
}

// Home
let status = await openPage('https://me.sh/');
readings.pages.home = { status, url: page.url(), ...(await readVars(page)) };
await shoot('home-light-default');
await page.evaluate(() => window.scrollTo(0, 0));

const logo = page.locator('a.y0DxmG_logo').first();
const signIn = page.locator('a[href*="login?signin"]').first();
const getStarted = page.locator('a[href="https://app.me.sh/login"]').first();
readings.components.logo = await measureEl(page, logo, 'logo');
await cropEl(page, logo, path.join(CROPS, 'logo-default.png'));
readings.components.signIn = await measureEl(page, signIn, 'sign-in');
await cropEl(page, signIn, path.join(CROPS, 'sign-in-link-default.png'));
readings.components.getStarted = await measureEl(page, getStarted, 'get-started');
await cropEl(page, getStarted, path.join(CROPS, 'get-started-default.png'));

await signIn.hover();
await page.waitForTimeout(400);
readings.components.signInHover = await measureEl(page, signIn, 'sign-in-hover');
await cropEl(page, signIn, path.join(CROPS, 'sign-in-link-hover.png'));
await page.mouse.move(2, 2);

await page.locator('#Releases_Button').click();
await page.waitForTimeout(450);
readings.components.releasesMenu = await measureEl(page, page.locator('#Releases_Panel'), 'releases-menu');
await shoot('home-light-releases-menu');
await page.keyboard.press('Escape');
await page.mouse.click(8, 860);
await page.waitForTimeout(250);

await page.locator('#Resources_Button').click();
await page.waitForTimeout(400);
await shoot('home-light-resources-menu');
await page.keyboard.press('Escape');
await page.mouse.click(8, 860);
await page.waitForTimeout(200);

await page.locator('#Company_Button').click();
await page.waitForTimeout(400);
await shoot('home-light-company-menu');
await page.keyboard.press('Escape');
await page.mouse.click(8, 860);

const birthdays = page.locator('button', { hasText: /^Birthdays$/ }).first();
await birthdays.scrollIntoViewIfNeeded();
await birthdays.click();
await page.waitForTimeout(500);
readings.components.filterBirthdays = await measureEl(page, birthdays, 'filter-birthdays-selected');
await cropEl(page, birthdays, path.join(CROPS, 'filter-chip-selected.png'));
await shoot('home-light-filter-birthdays');

// Pricing
status = await openPage('https://me.sh/pricing');
readings.pages.pricing = { status, url: page.url(), vars: (await readVars(page)).vars, themeColor: (await readVars(page)).themeColor };
await shoot('pricing-light-default');
const monthly = page.getByRole('button', { name: /pay monthly/i });
const annual = page.getByRole('button', { name: /pay annually/i });
readings.components.payAnnual = await measureEl(page, annual, 'pay-annually');
await cropEl(page, annual, path.join(CROPS, 'billing-toggle-selected.png'));
await monthly.click();
await page.waitForTimeout(400);
readings.components.payMonthly = await measureEl(page, monthly, 'pay-monthly-selected');
await cropEl(page, monthly, path.join(CROPS, 'billing-toggle-monthly.png'));
await shoot('pricing-light-monthly');
const personal = page.locator('#CTA_Personal');
readings.components.planCta = await measureEl(page, personal, 'plan-cta');
await cropEl(page, personal, path.join(CROPS, 'plan-cta-default.png'));

// Integrations search (type, do not submit)
status = await openPage('https://me.sh/integrations');
readings.pages.integrations = { status, url: page.url() };
await shoot('integrations-light-default');
const search = page.locator('input').first();
readings.components.search = await measureEl(page, search, 'search-default');
await cropEl(page, search, path.join(CROPS, 'search-field-default.png'));
await search.click();
await page.waitForTimeout(200);
readings.components.searchFocused = await measureEl(page, search, 'search-focused');
await cropEl(page, search, path.join(CROPS, 'search-field-focused.png'));
await search.fill('gmail');
await page.waitForTimeout(500);
readings.components.searchFilled = await measureEl(page, search, 'search-filled');
await cropEl(page, search, path.join(CROPS, 'search-field-filled.png'));
await shoot('integrations-light-search');
await search.fill('');

// A few more pages, viewport only
for (const [name, url] of [['nexus', 'https://me.sh/nexus'], ['teams', 'https://me.sh/teams'], ['start', 'https://me.sh/start'], ['stories', 'https://me.sh/stories'], ['about', 'https://me.sh/about'], ['contact', 'https://me.sh/contact'], ['notfound', 'https://me.sh/login']]) {
  status = await openPage(url);
  readings.pages[name] = { status, url: page.url(), title: await page.title() };
  await shoot(name + '-light-default');
}

// Login wall. Photograph only. Do not type, do not click Apple/Google/SSO.
status = await openPage('https://app.me.sh/login?signin');
const wall = await page.evaluate(() => ({
  url: location.href,
  title: document.title,
  text: (document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 900),
  controls: [...document.querySelectorAll('button, a, input')].map((el) => ({
    tag: el.tagName,
    type: el.getAttribute('type'),
    text: (el.innerText || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    href: el.tagName === 'A' ? el.href : null,
    disabled: !!el.disabled,
  })),
}));
readings.pages.loginWall = { status, ...wall };
await shoot('login-light-signin');
const email = page.locator('input[placeholder="Enter your email"]');
if (await email.count()) {
  readings.components.loginEmail = await measureEl(page, email, 'login-email');
  await cropEl(page, email, path.join(CROPS, 'login-email-default.png'));
}
const apple = page.getByRole('button', { name: /apple/i });
if (await apple.count()) {
  readings.components.idpApple = await measureEl(page, apple.first(), 'idp-apple');
  await cropEl(page, apple.first(), path.join(CROPS, 'idp-apple-default.png'));
}

// Mobile home
const mctx = await browser.newContext({
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  locale: 'en-US',
});
const mp = await mctx.newPage();
await mp.goto('https://me.sh/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await mp.waitForTimeout(1200);
const mdest = path.join(SHOTS, 'mobile-home-light-default.png');
await screenshotWithMetadata(mp, { path: mdest, sanitizedSourceUrl: 'https://me.sh/' }, {
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
});
const mobileHeader = await mp.evaluate(() => [...document.querySelectorAll('a, button')].filter((el) => {
  const r = el.getBoundingClientRect();
  return r.top < 90 && r.height > 0 && r.width > 0;
}).map((el) => ({
  tag: el.tagName,
  text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
  href: el.getAttribute('href'),
})));
readings.pages.mobileHome = { url: mp.url(), header: mobileHeader, innerWidth: await mp.evaluate(() => window.innerWidth) };
log('mobile shot');

fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
log('wrote readings', Object.keys(readings.pages).length, 'pages');
await browser.close();
