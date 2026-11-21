// Public Preply refresh, 2026-11-21. Signed out. No form submit, no identity
// providers, no booking. Screenshots stay outside git until quantize.
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const OUT = process.env.OUT || '/tmp/preply-capture';
const SHOTS = path.join(OUT, 'screenshots');
const RAW = path.join(OUT, 'raw');
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const strip = (url) => {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.toString();
  } catch {
    return url.split('?')[0].split('#')[0];
  }
};

async function settle(page) {
  await page.waitForLoadState('domcontentloaded', { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(1200);
  const challenge = await page.evaluate(() => /just a moment|verify you are human|cf-challenge|captcha/i.test(document.body?.innerText?.slice(0, 600) || document.title));
  return challenge;
}

async function shot(page, name, extra = {}) {
  const file = path.join(SHOTS, `${name}.png`);
  const meta = await screenshotWithMetadata(page, {
    path: file,
    fullPage: Boolean(extra.fullPage),
    scale: 'device',
  }, {
    sanitizedSourceUrl: strip(page.url()),
    viewport: page.viewportSize(),
    deviceScaleFactor: extra.dpr ?? 2,
  });
  fs.writeFileSync(`${file}.capture.json`, JSON.stringify(meta, null, 2) + '\n');
  return { name, url: strip(page.url()), title: await page.title(), png: meta.png, check: meta.dimensionCheck.status };
}

async function mapPage(page) {
  return page.evaluate(() => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 160);
    const header = document.querySelector('header');
    const headerItems = header ? [...header.querySelectorAll('a, button')].filter((el) => el.offsetWidth > 0 && el.getBoundingClientRect().top < 180).map((el) => ({
      tag: el.tagName,
      text: clean(el.innerText || el.getAttribute('aria-label')),
      href: (el.getAttribute('href') || '').split('?')[0].slice(0, 180),
      aria: el.getAttribute('aria-label'),
    })) : [];
    const footer = document.querySelector('footer');
    const footerLinks = footer ? [...footer.querySelectorAll('a')].map((a) => ({
      text: clean(a.innerText),
      href: (a.getAttribute('href') || '').split('?')[0].trim().slice(0, 180),
    })) : [];
    const headings = [...document.querySelectorAll('h1, h2')].slice(0, 16).map((h) => clean(h.innerText));
    const mainLinks = [...document.querySelectorAll('main a, [role=main] a')].slice(0, 40).map((a) => ({
      text: clean(a.innerText || a.getAttribute('aria-label')),
      href: (a.getAttribute('href') || '').split('?')[0].slice(0, 180),
    })).filter((x) => x.text);
    const fields = [...document.querySelectorAll('input, textarea, select')].slice(0, 20).map((el) => ({
      tag: el.tagName,
      type: el.getAttribute('type'),
      name: el.getAttribute('name'),
      placeholder: el.getAttribute('placeholder'),
      aria: el.getAttribute('aria-label'),
      autocomplete: el.getAttribute('autocomplete'),
    }));
    const buttons = [...document.querySelectorAll('button, a[role=button], input[type=submit]')].filter((el) => el.offsetWidth > 0).slice(0, 30).map((el) => clean(el.innerText || el.getAttribute('aria-label') || el.value));
    const empty = /no results|nothing here|0 results|empty|not found|page not found|no tutors/i.test(document.body.innerText.slice(0, 2500));
    return {
      path: location.pathname,
      title: document.title,
      h1: clean(document.querySelector('h1')?.innerText),
      headings,
      headerItems,
      footerCount: footerLinks.length,
      footerHeads: footer ? [...footer.querySelectorAll('h2, h3, h4, p, span')].map((el) => clean(el.innerText)).filter((t) => t && t.length < 40).slice(0, 12) : [],
      footerLinks: footerLinks.slice(0, 80),
      mainLinks,
      fields,
      buttons,
      emptyHint: empty,
      scrollHeight: document.documentElement.scrollHeight,
    };
  });
}

async function measure(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      return {
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        color: s.color,
        backgroundColor: s.backgroundColor,
        border: s.border,
        borderRadius: s.borderRadius,
        padding: s.padding,
        height: el.offsetHeight,
        boxShadow: s.boxShadow,
        letterSpacing: s.letterSpacing,
      };
    };
    const byText = (re, sel = 'a, button') => [...document.querySelectorAll(sel)].find((el) => re.test(el.innerText || '') && el.offsetWidth > 0);
    const h1 = document.querySelector('h1');
    const header = document.querySelector('header');
    const body = document.body;
    const field = document.querySelector('input');
    const card = document.querySelector('article, [class*=Card], [class*=card]');
    return {
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      body: pick(body),
      header: pick(header),
      h1: pick(h1),
      h2: pick(document.querySelector('h2')),
      find: pick(byText(/Find your tutor|Get started|Book a lesson/i)),
      login: pick(byText(/^Log in$/i)),
      field: pick(field),
      card: pick(card),
      link: pick(document.querySelector('main a, a')),
    };
  });
}

const pages = [
  ['home', 'https://preply.com/en/'],
  ['tutors', 'https://preply.com/en/online/english-tutors'],
  ['how', 'https://preply.com/en/how-it-works'],
  ['business', 'https://preply.com/en/business-language-training'],
  ['teach', 'https://preply.com/en/teach'],
  ['progress', 'https://preply.com/en/proven-progress-platform'],
  ['ukraine', 'https://preply.com/en/stand-with-ukraine'],
  ['pricing', 'https://preply.com/en/subscription'],
  ['search-empty', 'https://preply.com/en/online/english-tutors?s=zzzznotatutor999'],
  ['notfound', 'https://preply.com/en/this-page-does-not-exist-preply'],
];

const browser = await chromium.launch({ headless: true });
const log = [];

async function runWidth(label, viewport, dpr, names) {
  const context = await browser.newContext({
    viewport,
    deviceScaleFactor: dpr,
    colorScheme: 'light',
    locale: 'en-US',
  });
  const page = await context.newPage();
  for (const [name, url] of pages) {
    if (names && !names.includes(name)) continue;
    const fileName = label === 'desktop' ? `${name}-light-default` : `mobile-${name}-light-default`;
    try {
      const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      const challenge = await settle(page);
      const status = res?.status() ?? null;
      const mapped = await mapPage(page);
      const measured = await measure(page);
      fs.writeFileSync(path.join(RAW, `${fileName}.json`), JSON.stringify({ status, challenge, url: strip(page.url()), mapped, measured }, null, 2));
      if (challenge) {
        log.push({ fileName, challenge: true, url: strip(page.url()), status });
        continue;
      }
      const shotName = label === 'desktop' && name === 'home' ? 'home-light-default' : fileName;
      const result = await shot(page, shotName, { dpr });
      if (label === 'desktop' && (name === 'home' || name === 'tutors' || name === 'how')) {
        const full = await shot(page, `${name}-light-full`, { dpr, fullPage: true });
        log.push({ ...result, full: full.png, status });
      } else {
        log.push({ ...result, status });
      }
      console.log('OK', fileName, status, strip(page.url()));
    } catch (error) {
      log.push({ fileName, error: String(error).slice(0, 400) });
      console.error('FAIL', fileName, String(error).slice(0, 300));
    }
  }
  await context.close();
}

await runWidth('desktop', { width: 1440, height: 900 }, 2, null);
await runWidth('mobile', { width: 390, height: 844 }, 2, ['home', 'tutors']);

// Menus, footer, login and signup walls. Desktop.
{
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
    colorScheme: 'light',
    locale: 'en-US',
  });
  const page = await context.newPage();
  await page.goto('https://preply.com/en/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);

  // Language / currency dropdown.
  const settings = page.locator('header button').filter({ hasText: /English/ }).first();
  if (await settings.count()) {
    await settings.click();
    await page.waitForTimeout(600);
    await shot(page, 'home-light-language-menu');
    const menu = await page.evaluate(() => {
      const wrap = document.querySelector('[class*=SettingsSelectorsDesktop_dropdownWrapper], [class*=dropdown]');
      const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
      if (!wrap) return null;
      return {
        text: clean(wrap.innerText).slice(0, 800),
        links: [...wrap.querySelectorAll('a, button')].map((el) => ({
          tag: el.tagName,
          text: clean(el.innerText).slice(0, 40),
          href: (el.getAttribute('href') || '').slice(0, 80),
        })),
      };
    });
    fs.writeFileSync(path.join(RAW, 'language-menu.json'), JSON.stringify(menu, null, 2));
    await page.keyboard.press('Escape');
    await page.waitForTimeout(300);
  }

  // Footer viewport.
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(500);
  await shot(page, 'home-light-footer');

  // Login wall. Do not type. Do not click identity providers.
  await page.goto('https://preply.com/en/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
  const loginChallenge = await settle(page);
  const loginMap = await mapPage(page);
  fs.writeFileSync(path.join(RAW, 'login-wall.json'), JSON.stringify({ challenge: loginChallenge, url: strip(page.url()), loginMap, measured: await measure(page) }, null, 2));
  if (!loginChallenge) await shot(page, 'login-light-default');
  else log.push({ fileName: 'login-light-default', challenge: true });

  // Signup wall. Stop at the empty form.
  await page.goto('https://preply.com/en/signup', { waitUntil: 'domcontentloaded', timeout: 45000 });
  let signupChallenge = await settle(page);
  let signupUrl = strip(page.url());
  if (signupUrl.endsWith('/en/') || signupUrl === 'https://preply.com/') {
    await page.goto('https://preply.com/en/get-started', { waitUntil: 'domcontentloaded', timeout: 45000 });
    signupChallenge = await settle(page);
    signupUrl = strip(page.url());
  }
  const signupMap = await mapPage(page);
  fs.writeFileSync(path.join(RAW, 'signup-wall.json'), JSON.stringify({ challenge: signupChallenge, url: signupUrl, signupMap }, null, 2));
  if (!signupChallenge) await shot(page, 'signup-light-default');

  // Messages is likely a signed-in wall. Photograph empty, do not enter.
  await page.goto('https://preply.com/en/messages', { waitUntil: 'domcontentloaded', timeout: 45000 });
  const msgChallenge = await settle(page);
  fs.writeFileSync(path.join(RAW, 'messages-wall.json'), JSON.stringify({ challenge: msgChallenge, url: strip(page.url()), mapped: await mapPage(page) }, null, 2));
  if (!msgChallenge && !/login|signup|get-started/i.test(page.url())) {
    await shot(page, 'messages-light-default');
  } else if (!msgChallenge) {
    await shot(page, 'messages-redirect-light-default');
  }

  await context.close();
}

// Mobile menu.
{
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    colorScheme: 'light',
    locale: 'en-US',
    isMobile: true,
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.goto('https://preply.com/en/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  const opener = page.locator('button[aria-label="Open menu"]').first();
  if (await opener.count()) {
    await opener.click();
    await page.waitForTimeout(700);
    await shot(page, 'mobile-home-light-menu');
    const drawer = await page.evaluate(() => {
      const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
      const links = [...document.querySelectorAll('a, button')].filter((el) => el.offsetWidth > 0 && el.getBoundingClientRect().top > 40).slice(0, 30).map((el) => ({
        tag: el.tagName,
        text: clean(el.innerText || el.getAttribute('aria-label')).slice(0, 60),
        href: (el.getAttribute('href') || '').split('?')[0].slice(0, 140),
      }));
      return links;
    });
    fs.writeFileSync(path.join(RAW, 'mobile-menu.json'), JSON.stringify(drawer, null, 2));
  }
  await context.close();
}

// Dark scheme probe.
{
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    colorScheme: 'dark',
  });
  const page = await context.newPage();
  await page.goto('https://preply.com/en/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await settle(page);
  const probe = await page.evaluate(() => {
    const header = document.querySelector('header');
    const h1 = document.querySelector('h1');
    return {
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      headerBg: header ? getComputedStyle(header).backgroundColor : null,
      h1Color: h1 ? getComputedStyle(h1).color : null,
      bodyBg: getComputedStyle(document.body).backgroundColor,
    };
  });
  fs.writeFileSync(path.join(RAW, 'dark-probe.json'), JSON.stringify(probe, null, 2));
  await context.close();
}

fs.writeFileSync(path.join(OUT, 'log.json'), JSON.stringify(log, null, 2));
await browser.close();
console.log('DONE', log.length);
