// Public Reflect capture. Adapted from the kit. No form submit, no identity click.
const ADAPTED_FOR = 'reflect';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';
import { screenshotWithMetadata } from './capture/screenshot.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems/reflect/raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const READ = path.join(os.homedir(), '.design-systems/reflect');
fs.mkdirSync(READ, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

function rgb(c) {
  const m = String(c).match(/rgba?\(([^)]+)\)/);
  if (!m) return c;
  const p = m[1].split(',').map((x) => Math.round(parseFloat(x.trim())));
  const hex = (n) => n.toString(16).padStart(2, '0');
  if (p.length === 4 && p[3] === 0) return 'transparent';
  return '#' + hex(p[0]) + hex(p[1]) + hex(p[2]);
}

async function shot(page, name, requested, extra = {}) {
  const file = path.join(RAW, name + '.png');
  const actual = await page.evaluate(() => ({ w: window.innerWidth, h: window.innerHeight, dpr: window.devicePixelRatio }));
  const req = {
    viewport: { width: actual.w, height: actual.h },
    deviceScaleFactor: actual.dpr,
    sanitizedSourceUrl: page.url().split('?')[0].split('#')[0],
  };
  await screenshotWithMetadata(page, { path: file, ...extra }, req);
  console.log('shot', name, actual.w + 'x' + actual.h);
}

async function hideCookies(page) {
  await page.addStyleTag({
    content: [
      '[id*="cookie" i]', '[class*="cookie" i]', '[id*="consent" i]', '[class*="consent" i]',
      '[aria-label*="cookie" i]', '[id*="onetrust" i]', '#onetrust-banner-sdk',
    ].map((s) => `${s}{display:none !important}`).join(''),
  }).catch(() => {});
}

async function measurePage(page, label) {
  const data = await page.evaluate(() => {
    const csOf = (el) => {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 90),
        tag: el.tagName,
        rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
        color: cs.color,
        backgroundColor: cs.backgroundColor,
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        borderRadius: cs.borderRadius,
        borderTopWidth: cs.borderTopWidth,
        borderTopStyle: cs.borderTopStyle,
        borderTopColor: cs.borderTopColor,
        padding: cs.padding,
        height: cs.height,
        boxShadow: cs.boxShadow,
        textDecoration: cs.textDecorationLine,
        outline: cs.outline,
        outlineOffset: cs.outlineOffset,
      };
    };
    const byText = (sel, text) => [...document.querySelectorAll(sel)].find((n) => (n.innerText || '').replace(/\s+/g, ' ').trim().startsWith(text));
    const body = getComputedStyle(document.body);
    const links = [...document.querySelectorAll('a')].map((a) => ({
      text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      href: a.getAttribute('href'),
    }));
    const seen = new Set();
    const unique = [];
    for (const l of links) {
      const k = l.href + '|' + l.text;
      if (seen.has(k)) continue;
      seen.add(k);
      unique.push(l);
    }
    return {
      url: location.origin + location.pathname,
      title: document.title,
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize, lineHeight: body.lineHeight },
      h1: csOf(document.querySelector('h1')),
      h2: csOf(document.querySelector('h2')),
      navLinks: unique.filter((l) => l.href && !l.href.startsWith('http') || (l.href || '').includes('reflect.app')).slice(0, 40),
      allUnique: unique,
      buttons: [...document.querySelectorAll('button')].map((b) => (b.innerText || b.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 20),
      download: csOf(byText('a', 'Download for Mac') || byText('a', 'Download')),
      login: csOf(byText('a', 'Log in')),
      email: csOf(document.querySelector('input[type=email], input[placeholder*="email" i]')),
      subscribe: csOf(byText('button', 'Subscribe')),
      bodyText: document.body.innerText.slice(0, 1800),
    };
  });
  fs.writeFileSync(path.join(READ, label + '.json'), JSON.stringify(data, null, 2));
  return data;
}

const browser = await chromium.launch({ headless: true });

async function open(width, height, scheme = 'light') {
  const context = await browser.newContext({
    viewport: { width, height },
    deviceScaleFactor: 2,
    colorScheme: scheme,
    reducedMotion: 'reduce',
    userAgent: width < 500
      ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
      : UA,
    isMobile: width < 500,
    hasTouch: width < 500,
  });
  const page = await context.newPage();
  page.setDefaultTimeout(25000);
  return { context, page };
}

const desk = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 };
const phone = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };

const ONLY = (process.env.ONLY || '').split(',').filter(Boolean);
const want = (name) => !ONLY.length || ONLY.some((n) => name.startsWith(n));

if (want('desktop')) {
const { context, page } = await open(1440, 900);
await page.goto('https://reflect.app/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1800);
await hideCookies(page);
await shot(page, 'home-light-default', desk);
await measurePage(page, 'home-light');

// hover the primary download
const dl = page.getByRole('link', { name: 'Download for Mac' }).first();
if (await dl.count()) {
  await dl.hover();
  await page.waitForTimeout(250);
  await shot(page, 'home-light-download-hover', desk);
  const hover = await dl.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      color: cs.color, backgroundColor: cs.backgroundColor, boxShadow: cs.boxShadow,
      borderRadius: cs.borderRadius, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
      fontFamily: cs.fontFamily, padding: cs.padding, height: cs.height,
      border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
      rect: { w: Math.round(r.width), h: Math.round(r.height) },
    };
  });
  fs.writeFileSync(path.join(READ, 'download-hover.json'), JSON.stringify(hover, null, 2));
  await dl.focus();
  await page.waitForTimeout(200);
  const focus = await dl.evaluate((el) => {
    const cs = getComputedStyle(el);
    return { outline: cs.outline, outlineOffset: cs.outlineOffset, boxShadow: cs.boxShadow, backgroundColor: cs.backgroundColor };
  });
  fs.writeFileSync(path.join(READ, 'download-focus.json'), JSON.stringify(focus, null, 2));
  const box = await dl.boundingBox();
  if (box) {
    await shot(page, 'crop-download-hover', desk, { clip: { x: Math.max(0, box.x - 12), y: Math.max(0, box.y - 12), width: box.width + 24, height: box.height + 24 } });
  }
}

// nav product is an in-page anchor, not a menu. Photograph the pricing section and footer.
await page.locator('#pricing').scrollIntoViewIfNeeded().catch(async () => {
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('h2,h3')].find((n) => /choose your device/i.test(n.innerText || ''));
    el?.scrollIntoView();
  });
});
await page.waitForTimeout(400);
await shot(page, 'home-light-pricing', desk);

await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(500);
await shot(page, 'home-light-footer', desk);

// launch film button opens a video dialog. Open, photograph, close. Do not play past the poster if a close exists.
const play = page.getByRole('button', { name: /Play the Reflect launch film/i });
if (await play.count()) {
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(300);
  await play.click();
  await page.waitForTimeout(800);
  await shot(page, 'home-light-video-dialog', desk);
  const close = page.getByRole('button', { name: /Close video/i });
  if (await close.count()) await close.click();
  await page.waitForTimeout(300);
}

// full page, capped
await page.evaluate(async () => {
  const h = document.documentElement.scrollHeight;
  for (let y = 0; y < Math.min(h, 8000); y += 700) {
    scrollTo(0, y);
    await new Promise((r) => setTimeout(r, 80));
  }
  scrollTo(0, 0);
});
await page.waitForTimeout(400);
await shot(page, 'home-light-full', desk, { fullPage: true });

// inner pages
async function pageShot(url, name) {
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1400);
  await hideCookies(page);
  await shot(page, name, desk);
  await measurePage(page, name);
}

await pageShot('https://reflect.app/blog', 'blog-light-default');
await pageShot('https://reflect.app/download', 'download-light-default');
await pageShot('https://reflect.app/privacy', 'privacy-light-default');
await pageShot('https://reflect.app/terms', 'terms-light-default');
await pageShot('https://reflect.app/not-found', 'notfound-light-default');

// auth wall empty. Do not type. Do not click identity providers.
await page.goto('https://reflect.app/auth', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1400);
await hideCookies(page);
const authText = await page.evaluate(() => document.body.innerText.slice(0, 2000));
fs.writeFileSync(path.join(READ, 'auth-text.txt'), authText);
await shot(page, 'login-light-default', desk);
await measurePage(page, 'login-light');

// blog tag is a filter, not a form submit of personal data. Click "Articles" if present.
await page.goto('https://reflect.app/blog', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
await hideCookies(page);
const articles = page.getByRole('button', { name: /Articles/ });
if (await articles.count()) {
  await articles.first().click();
  await page.waitForTimeout(900);
  await shot(page, 'blog-light-articles', desk);
}

await context.close();
}

// mobile home + one inner page (blog)
if (want('mobile')) {
const mob = await open(390, 844);
// isMobile inflates innerWidth. Recreate without it so the CSS viewport is 390.
await mob.context.close();
const mobCtx = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  colorScheme: 'light',
  reducedMotion: 'reduce',
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
});
const mobPage = await mobCtx.newPage();
mobPage.setDefaultTimeout(25000);
const mobFixed = { context: mobCtx, page: mobPage };
await mobFixed.page.goto('https://reflect.app/', { waitUntil: 'domcontentloaded' });
await mobFixed.page.waitForTimeout(1600);
await hideCookies(mobFixed.page);
const mobileSize = await mobFixed.page.evaluate(() => ({ w: innerWidth, h: innerHeight, dpr: devicePixelRatio }));
console.log('mobile inner', mobileSize);
await shot(mobFixed.page, 'mobile-home-light-default', phone);
const menuBtn = mob.page.locator('button').filter({ hasText: /menu/i }).or(mob.page.getByRole('button', { name: /menu|open/i }));
const buttons = await mobFixed.page.evaluate(() => [...document.querySelectorAll('button, a')].slice(0, 30).map((b) => ({
  tag: b.tagName,
  text: (b.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
  aria: b.getAttribute('aria-label'),
  href: b.getAttribute('href'),
})));
fs.writeFileSync(path.join(READ, 'mobile-controls.json'), JSON.stringify({ mobileSize, buttons }, null, 2));
console.log('mobile controls', JSON.stringify(buttons));
const burgerCount = await mobFixed.page.locator('header button, nav button, button[aria-expanded], button[aria-label*="menu" i]').count();
console.log('burger candidates', burgerCount);
if (burgerCount) {
  await mobFixed.page.locator('header button, nav button, button[aria-expanded], button[aria-label*="menu" i]').first().click();
  await mobFixed.page.waitForTimeout(600);
  await shot(mobFixed.page, 'mobile-home-light-menu', phone);
}
await mobFixed.page.goto('https://reflect.app/blog', { waitUntil: 'domcontentloaded' });
await mobFixed.page.waitForTimeout(1400);
await hideCookies(mobFixed.page);
await shot(mobFixed.page, 'mobile-blog-light-default', phone);
await mobFixed.context.close();
}

await browser.close();
console.log('done', RAW);
