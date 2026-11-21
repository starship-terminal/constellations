// Capture Threads' public signed-out surface.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/threads/tools/capture/public/capture.mjs
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Light is the default class.
// Dark is the same pages with prefers-color-scheme: dark, which Threads
// paints as __fb-dark-mode. Nothing is typed. Nothing is submitted.
// Instagram, Google, Apple and Facebook controls are never clicked.
// A control that opens /login or a Continue-with-Instagram dialog is recorded
// and that branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'threads', 'raw-shots');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_M = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', path.basename(file));
}

async function hideSplash(page) {
  await page.evaluate(() => {
    const s = document.getElementById('barcelona-splash-screen');
    if (s) s.style.display = 'none';
  }).catch(() => {});
}

async function dismissJoin(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(350);
}

async function open(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2200);
  await hideSplash(page);
  await page.waitForTimeout(400);
  return res ? res.status() : null;
}

async function clickNav(page, label) {
  return page.evaluate((label) => {
    const hit = [...document.querySelectorAll('[role="button"], a, button')].find((el) => {
      const t = (el.innerText || '').replace(/\s+/g, ' ').trim();
      const r = el.getBoundingClientRect();
      return t === label && r.x < 280 && r.width > 16 && r.height > 8;
    });
    if (!hit) return false;
    hit.click();
    return true;
  }, label);
}

async function readSurface(page) {
  return page.evaluate(() => {
    const body = getComputedStyle(document.body);
    const html = document.documentElement;
    const names = [
      '--barcelona-splash-screen-logo-color',
      '--background-primary',
      '--text-primary',
    ];
    const picked = {};
    const cs = getComputedStyle(html);
    for (let i = 0; i < cs.length; i++) {
      const n = cs[i];
      if (n.startsWith('--') && /barcelona|ig-|fds-|primary|secondary|background|text|border|accent/.test(n)) {
        picked[n] = cs.getPropertyValue(n).trim();
      }
    }
    // also walk a few painted nodes
    const sample = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        sel, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        color: s.color, bg: s.backgroundColor, font: s.fontFamily, size: s.fontSize,
        weight: s.fontWeight, lh: s.lineHeight, radius: s.borderRadius, pad: s.padding,
        h: Math.round(r.height), w: Math.round(r.width),
      };
    };
    return {
      href: location.href,
      title: document.title,
      htmlClass: html.className,
      vw: innerWidth, vh: innerHeight, dpr: devicePixelRatio,
      bodyBg: body.backgroundColor, bodyColor: body.color, bodyFont: body.fontFamily,
      bodySize: body.fontSize, bodyWeight: body.fontWeight, bodyLh: body.lineHeight,
      pickedCount: Object.keys(picked).length,
      picked,
      samples: {
        login: sample('a[href*="/login"]'),
      },
    };
  });
}

const SEMANTIC = [
  '--ig-primary-background', '--ig-secondary-background', '--ig-tertiary-background',
  '--ig-elevated-background', '--ig-primary-text', '--ig-secondary-text', '--ig-tertiary-text',
  '--ig-primary-button', '--ig-primary-button-hover', '--ig-link', '--ig-stroke',
  '--ig-separator', '--ig-highlight-background', '--ig-error-or-destructive',
  '--ig-success', '--ig-focus-ring',
];

async function dumpVars(page, label) {
  return page.evaluate((label) => {
    const html = document.documentElement;
    const cs = getComputedStyle(html);
    const resolved = {};
    for (let i = 0; i < cs.length; i++) {
      const n = cs[i];
      if (!n.startsWith('--')) continue;
      const v = cs.getPropertyValue(n).trim();
      if (!v || v.length > 180) continue;
      if (/url\(|token|session|bearer/i.test(v)) continue;
      resolved[n] = v;
    }
    return {
      label,
      href: location.href,
      htmlClass: html.className,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily,
      count: Object.keys(resolved).length,
      resolved,
    };
  }, label);
}

const browser = await chromium.launch({ headless: true });
const readings = { capturedAt: new Date().toISOString(), themes: {}, components: [], pages: [] };

async function contextFor(theme, mobile) {
  const opts = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_M, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: theme }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: theme };
  const context = await browser.newContext(opts);
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return context;
}

for (const theme of ['light', 'dark']) {
  const context = await contextFor(theme, false);
  const page = await context.newPage();
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const prefix = `home-${theme}`;

  log('home', theme);
  await open(page, 'https://www.threads.com/');
  await shot(page, `${RAW}/${prefix}-join-dialog.png`, requested);
  await dismissJoin(page);
  await page.waitForTimeout(400);
  await shot(page, `${RAW}/${prefix}-default.png`, requested);
  readings.pages.push({ name: prefix + '-default', ...(await readSurface(page)) });
  if (!readings.themes[theme]) readings.themes[theme] = await dumpVars(page, theme);

  // More menu
  await clickNav(page, 'More');
  await page.waitForTimeout(600);
  await shot(page, `${RAW}/${prefix}-more-menu.png`, requested);

  // Appearance
  await page.evaluate(() => {
    const menu = document.querySelector('[role="menu"]');
    if (!menu) return;
    [...menu.querySelectorAll('div')].find((el) => (el.innerText || '').trim() === 'Appearance')?.click();
  });
  await page.waitForTimeout(500);
  await shot(page, `${RAW}/${prefix}-appearance.png`, requested);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  // Sounds (public, no toggle)
  await clickNav(page, 'More');
  await page.waitForTimeout(400);
  await page.evaluate(() => {
    const menu = document.querySelector('[role="menu"]');
    if (!menu) return;
    [...menu.querySelectorAll('div')].find((el) => (el.innerText || '').trim() === 'Sounds')?.click();
  });
  await page.waitForTimeout(500);
  await shot(page, `${RAW}/${prefix}-sounds.png`, requested);
  await page.keyboard.press('Escape');
  await dismissJoin(page);

  // New thread wall, then stop
  await clickNav(page, 'New thread');
  await page.waitForTimeout(800);
  await shot(page, `${RAW}/${prefix}-new-thread-wall.png`, requested);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  // Search
  log('search', theme);
  await open(page, 'https://www.threads.com/search');
  await dismissJoin(page);
  await shot(page, `${RAW}/search-${theme}-default.png`, requested);
  const field = page.locator('input[type="search"]').first();
  if (await field.count()) {
    await field.focus();
    await page.waitForTimeout(400);
    await shot(page, `${RAW}/search-${theme}-focused.png`, requested);
  }

  // Official profile
  log('profile', theme);
  await open(page, 'https://www.threads.com/@threads');
  await dismissJoin(page);
  await shot(page, `${RAW}/profile-${theme}-default.png`, requested);
  for (const tab of ['Replies', 'Media', 'Reposts', 'Threads']) {
    await page.evaluate((tab) => {
      const hit = [...document.querySelectorAll('div, a, [role="tab"]')].find((el) => {
        const t = (el.innerText || '').replace(/\s+/g, ' ').trim();
        const r = el.getBoundingClientRect();
        return t === tab && r.y > 180 && r.y < 800 && r.width < 220 && r.width > 20;
      });
      hit && hit.click();
    }, tab);
    await page.waitForTimeout(900);
    await shot(page, `${RAW}/profile-${theme}-tab-${tab.toLowerCase()}.png`, requested);
  }
  // Follow wall, then stop
  await page.evaluate(() => {
    const hit = [...document.querySelectorAll('[role="button"]')].find((el) => (el.innerText || '').trim() === 'Follow');
    hit && hit.click();
  });
  await page.waitForTimeout(800);
  await shot(page, `${RAW}/profile-${theme}-follow-wall.png`, requested);
  await page.keyboard.press('Escape');

  // Login boundary, no typing
  if (theme === 'light') {
    log('login boundary');
    await open(page, 'https://www.threads.com/login');
    await shot(page, `${RAW}/login-light-default.png`, requested);
    readings.pages.push({ name: 'login-light-default', note: 'boundary, not submitted', ...(await readSurface(page)) });
  }

  await context.close();
}

// Phone, light and dark
for (const theme of ['light', 'dark']) {
  const context = await contextFor(theme, true);
  const page = await context.newPage();
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
  log('mobile home', theme);
  await open(page, 'https://www.threads.com/');
  await hideSplash(page);
  await page.waitForTimeout(600);
  await shot(page, `${RAW}/mobile-home-${theme}-default.png`, requested);
  readings.pages.push({ name: `mobile-home-${theme}-default`, ...(await readSurface(page)) });

  // search tab
  await page.evaluate(() => {
    const hit = [...document.querySelectorAll('a')].find((el) => el.querySelector('svg title')?.textContent === 'Search' || (el.href || '').endsWith('/search'));
    const tabs = [...document.querySelectorAll('a')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.y > 740 && (el.href || '').includes('/search');
    });
    (tabs[0] || hit)?.click();
  });
  await page.waitForTimeout(1500);
  await hideSplash(page);
  await shot(page, `${RAW}/mobile-search-${theme}-default.png`, requested);

  await context.close();
}

fs.writeFileSync(path.join(READ, 'css-vars.json'), JSON.stringify({
  source: 'computed custom properties on html, threads.com, 2026-11-21',
  themes: readings.themes,
}, null, 1));
fs.writeFileSync(path.join(READ, 'pages.json'), JSON.stringify(readings.pages, null, 1));
log('vars', Object.keys(readings.themes.light?.resolved || {}).length, 'light names');
log('done shots in', RAW);
await browser.close();
