// Capture the public Microsoft homepage and same-host pages. No sign-in.
// Stops at login, signup, identity-provider, and captcha walls.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture_public.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(PKG, 'screenshots');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HOME = 'https://www.microsoft.com/en-sg';
const ALLOWED = new Set(['www.microsoft.com', 'microsoft.com']);

function hostOf(url) {
  try { return new URL(url).hostname; } catch { return ''; }
}

function wallReason(info) {
  const blob = `${info.title}\n${info.body}`.slice(0, 1600);
  if (/just a moment|cf-browser-verification|challenge-platform|Attention Required|Checking your browser|verify you are human|captcha/i.test(blob)) {
    return 'captcha';
  }
  if (/sign in|sign-in|create an account|enter (your )?(email|phone)|password/i.test(blob) && /login\.live\.com|account\.microsoft\.com|login\.microsoftonline\.com/i.test(info.href)) {
    return 'login-wall';
  }
  if (hostOf(info.href) && !ALLOWED.has(hostOf(info.href))) return 'off-host';
  return null;
}

async function meta(page) {
  return page.evaluate(() => ({
    href: location.href,
    title: document.title,
    body: (document.body?.innerText || '').slice(0, 700),
    innerWidth, innerHeight, devicePixelRatio,
    vv: visualViewport ? { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale } : null,
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
    scrollHeight: document.documentElement.scrollHeight,
  }));
}

function rgbToHex(value) {
  const m = String(value).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
  if (!m) return value;
  const hex = (n) => Number(n).toString(16).padStart(2, '0');
  return `#${hex(m[1])}${hex(m[2])}${hex(m[3])}`;
}

async function readPage(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100),
        tag: el.tagName,
        cls: String(el.className || '').slice(0, 140),
        href: el.href || null,
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
        backgroundColor: s.backgroundColor,
        color: s.color,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        padding: s.padding,
        border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
        boxShadow: s.boxShadow,
        outline: s.outline,
        height: s.height,
      };
    };
    const first = (sel) => document.querySelector(sel);
    const links = [...document.querySelectorAll('a, button')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 40 && r.height > 24 && r.top > 60 && r.top < 1100;
    });
    const cta = links.find((el) => /shop|download|join|learn|explore|get /i.test(el.innerText || '')) || links[0];
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const rule of list) {
          if (rule.cssRules && !rule.style) { walk(rule.cssRules); continue; }
          if (!rule.style) continue;
          for (let i = 0; i < rule.style.length; i++) {
            const name = rule.style[i];
            if (name.startsWith('--') && vars[name] == null) vars[name] = root.getPropertyValue(name).trim();
          }
        }
      };
      walk(rules);
      if (Object.keys(vars).length > 400) break;
    }
    const themeColor = document.querySelector('meta[name="theme-color"]')?.content || null;
    const nav = [...document.querySelectorAll('#uhf-g-nav a, #uhf-g-nav button, header a, header button')].map((el) => {
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        label: (el.getAttribute('aria-label') || el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 100),
        href: el.href || el.getAttribute('href') || '',
        ariaExpanded: el.getAttribute('aria-expanded'),
        visible: r.width > 0 && r.height > 0,
      };
    }).filter((x) => x.label);
    return {
      themeColor,
      colorScheme: root.colorScheme,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily,
      h1: pick(first('h1')),
      header: pick(first('header, #uhf-header, .c-uhfh')),
      cta: pick(cta),
      signIn: pick([...document.querySelectorAll('button, a')].find((el) => /sign in/i.test((el.getAttribute('aria-label') || '') + el.innerText))),
      vars,
      nav,
    };
  });
}

async function shot(page, name, requested) {
  const file = path.join(SHOTS, name);
  await page.screenshot({ path: file, fullPage: false });
  const info = await meta(page);
  const png = fs.readFileSync(file);
  const w = png.readUInt32BE(16);
  const h = png.readUInt32BE(20);
  fs.writeFileSync(file + '.capture.json', JSON.stringify({
    requested,
    measured: {
      innerWidth: info.innerWidth,
      innerHeight: info.innerHeight,
      devicePixelRatio: info.devicePixelRatio,
      visualViewport: info.vv,
    },
    png: { pixelWidth: w, pixelHeight: h },
    href: info.href,
    title: info.title,
  }, null, 2) + '\n');
  return info;
}

async function crop(page, selectorText, file) {
  const box = await page.evaluate((text) => {
    const els = [...document.querySelectorAll('a, button')];
    const el = els.find((node) => (node.innerText || '').replace(/\s+/g, ' ').trim().includes(text));
    if (!el) return null;
    const r = el.getBoundingClientRect();
    if (r.width < 8 || r.height < 8) return null;
    return { x: Math.max(0, r.x - 8), y: Math.max(0, r.y - 8), width: r.width + 16, height: r.height + 16 };
  }, selectorText);
  if (!box) return false;
  await page.screenshot({ path: path.join(CROPS, file), clip: box });
  return true;
}

const browser = await chromium.launch({ headless: true });
const readings = { captured: '2026-11-21', home: HOME, pages: {}, walls: [] };

async function openContext(viewport, dpr, mobile) {
  return browser.newContext({
    viewport,
    deviceScaleFactor: dpr,
    isMobile: mobile,
    hasTouch: mobile,
    userAgent: mobile
      ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
      : undefined,
  });
}

const desktop = await openContext({ width: 1440, height: 900 }, 1, false);
const page = await desktop.newPage();
page.setDefaultTimeout(25000);

await page.goto(HOME, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2500);
let info = await meta(page);
console.log('home', info.href, info.title, info.innerWidth);
if (wallReason(info)) {
  readings.walls.push({ url: info.href, reason: wallReason(info), title: info.title });
  fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
  await browser.close();
  process.exit(3);
}

const requestedDesktop = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
await shot(page, 'home-light-default.png', requestedDesktop);
const homeRead = await readPage(page);
readings.pages.home = { meta: info, styles: { ...homeRead, nav: undefined }, navCount: homeRead.nav.length };
fs.writeFileSync(path.join(RAW, 'nav.json'), JSON.stringify(homeRead.nav, null, 2));

await page.locator('button', { hasText: 'All Microsoft' }).first().click({ timeout: 8000 }).catch((e) => console.log('menu fail', e.message));
await page.waitForTimeout(800);
await shot(page, 'home-light-menu-all-microsoft.png', requestedDesktop);
await page.keyboard.press('Escape').catch(() => {});
await page.waitForTimeout(300);

const searchBtn = page.locator('button[aria-label="Search Microsoft.com"], button:has-text("Search Microsoft.com")').first();
await searchBtn.click({ timeout: 8000 }).catch((e) => console.log('search fail', e.message));
await page.waitForTimeout(600);
await shot(page, 'home-light-search.png', requestedDesktop);
await page.keyboard.press('Escape').catch(() => {});

const ctaText = homeRead.cta?.text || '';
if (ctaText) {
  const loc = page.getByRole('link', { name: ctaText }).first();
  await loc.hover({ timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(250);
  await shot(page, 'home-light-cta-hover.png', requestedDesktop);
  await crop(page, ctaText.slice(0, 24), 'button-primary-default.png');
  await loc.focus().catch(() => {});
  await page.waitForTimeout(200);
  await crop(page, ctaText.slice(0, 24), 'button-primary-focus.png');
}
await crop(page, 'Sign in', 'button-signin-default.png');

await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(600);
await shot(page, 'home-light-footer.png', requestedDesktop);
await page.evaluate(() => scrollTo(0, 0));

const sameHost = [
  { name: 'products', url: 'https://www.microsoft.com/en-sg/microsoft-products-and-apps' },
  { name: 'microsoft-365', url: 'https://www.microsoft.com/en-sg/microsoft-365' },
  { name: 'windows', url: 'https://www.microsoft.com/en-sg/windows/' },
  { name: 'surface', url: 'https://www.microsoft.com/en-sg/surface' },
  { name: 'sale', url: 'https://www.microsoft.com/en-sg/store/b/sale' },
  { name: 'sitemap', url: 'https://www.microsoft.com/en-sg/sitemap' },
];

for (const item of sameHost) {
  if (!ALLOWED.has(hostOf(item.url))) continue;
  const p = await desktop.newPage();
  try {
    await p.goto(item.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await p.waitForTimeout(1800);
    const m = await meta(p);
    const reason = wallReason(m);
    console.log(item.name, m.href, reason || 'ok');
    if (reason) {
      readings.walls.push({ name: item.name, url: m.href, reason, title: m.title });
      if (reason === 'login-wall' || reason === 'captcha') {
        await p.screenshot({ path: path.join(SHOTS, `${item.name}-light-wall.png`) }).catch(() => {});
      }
      continue;
    }
    await shot(p, `${item.name}-light-default.png`, requestedDesktop);
    readings.pages[item.name] = { href: m.href, title: m.title, styles: await readPage(p).then((r) => ({ h1: r.h1, cta: r.cta, bodyBg: r.bodyBg, bodyFont: r.bodyFont, themeColor: r.themeColor })) };
  } catch (e) {
    console.log('FAILED', item.name, e.message.split('\n')[0]);
    readings.walls.push({ name: item.name, reason: 'error', message: e.message.split('\n')[0] });
  } finally {
    await p.close();
  }
}

const signin = await desktop.newPage();
await page.goto(HOME, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
const popupPromise = desktop.waitForEvent('page', { timeout: 8000 }).catch(() => null);
await page.locator('button', { hasText: /^Sign in$/ }).first().click({ timeout: 8000 }).catch((e) => console.log('signin click', e.message));
const popup = await popupPromise;
const signinPage = popup || page;
await signinPage.waitForTimeout(2000);
const signinMeta = await meta(signinPage);
const signinReason = wallReason(signinMeta) || (ALLOWED.has(hostOf(signinMeta.href)) ? null : 'off-host');
console.log('signin', signinMeta.href, signinReason);
readings.signin = { href: signinMeta.href, title: signinMeta.title, reason: signinReason, body: signinMeta.body.slice(0, 280) };
if (signinReason === 'login-wall' || /sign in/i.test(signinMeta.title)) {
  await signinPage.screenshot({ path: path.join(SHOTS, 'login-light-wall.png') });
}
await signin.close().catch(() => {});

const phone = await openContext({ width: 390, height: 844 }, 2, true);
const mp = await phone.newPage();
await mp.goto(HOME, { waitUntil: 'domcontentloaded' });
await mp.waitForTimeout(2000);
const phoneMeta = await meta(mp);
console.log('phone', phoneMeta.href, phoneMeta.innerWidth, phoneMeta.devicePixelRatio);
const requestedPhone = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
if (!wallReason(phoneMeta)) {
  await shot(mp, 'mobile-home-light-default.png', requestedPhone);
  const menu = mp.locator('button[aria-label="More"], button:has-text("More")').first();
  await menu.click({ timeout: 6000 }).catch((e) => console.log('phone menu', e.message));
  await mp.waitForTimeout(700);
  await shot(mp, 'mobile-home-light-menu.png', requestedPhone);
}

fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
await browser.close();
console.log('done', Object.keys(readings.pages));
