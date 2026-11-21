// Captures Understory's public marketing pages. Nothing is submitted.
// Login, signup, preview URL entry, newsletter, and demo forms are not filled.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node capture.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { launch, settle, hideConsent, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'understory', 'raw-shots');
const OUT = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: path.join(RAW, file) }, {
    ...requested,
    sanitizedSourceUrl: new URL(page.url()).origin + new URL(page.url()).pathname,
  });
  log('  shot', file);
}

async function full(page, file, requested) {
  const h0 = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h0, 8000); y += 700) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await wait(page, 150);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 400);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const dpr = requested.deviceScaleFactor;
  const vw = requested.viewport.width;
  const chunk = Math.floor(12000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log('  ! truncated', file, H, '->', hCap);
  const stem = path.join(RAW, file.replace(/\.png$/, ''));
  if (hCap <= chunk) {
    await screenshotWithMetadata(page, { path: stem + '.png', fullPage: true }, { ...requested, sanitizedSourceUrl: null });
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: `${stem}.part${i}.png`, fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      }, { ...requested, sanitizedSourceUrl: null });
    }
  }
  log('  full', file, 'H=' + H);
  await page.evaluate(() => scrollTo(0, 0));
}

function box(el) {
  if (!el) return null;
  const c = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return {
    text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
    cls: String(el.className || '').slice(0, 100),
    tag: el.tagName.toLowerCase(),
    font: c.fontFamily,
    size: c.fontSize,
    weight: c.fontWeight,
    lh: c.lineHeight,
    ls: c.letterSpacing,
    tt: c.textTransform,
    color: c.color,
    bg: c.backgroundColor,
    radius: c.borderRadius,
    bw: c.borderTopWidth,
    bc: c.borderTopColor,
    pad: c.padding,
    shadow: c.boxShadow === 'none' ? 'none' : c.boxShadow.slice(0, 140),
    h: Math.round(r.height),
    w: Math.round(r.width),
    x: Math.round(r.x),
    y: Math.round(r.y),
  };
}

async function readVars(page) {
  return page.evaluate(() => {
    const rows = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        for (const r of list) {
          if (r.type === CSSRule.STYLE_RULE) {
            for (const name of r.style) {
              if (name.startsWith('--')) rows.push({ selector: r.selectorText.slice(0, 140), name, value: r.style.getPropertyValue(name).trim() });
            }
          }
          if (r.cssRules) walk(r.cssRules);
        }
      };
      try { walk(rules); } catch { /* cross-origin */ }
    }
    const cs = getComputedStyle(document.documentElement);
    const resolved = {};
    for (const row of rows) if (!(row.name in resolved)) resolved[row.name] = cs.getPropertyValue(row.name).trim();
    const faces = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      for (const r of rules) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          faces.push({ family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style') });
        }
      }
    }
    return { rows, resolved, faces, bodyBg: getComputedStyle(document.body).backgroundColor, bodyColor: getComputedStyle(document.body).color, bodyFont: getComputedStyle(document.body).fontFamily };
  });
}

async function measure(page, label) {
  return page.evaluate((label) => {
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const c = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 1 && r.height < 1) return { sel, miss: 'zero box', text: (el.innerText || '').slice(0, 40) };
      return {
        sel,
        text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 50),
        cls: String(el.className || '').slice(0, 80),
        font: c.fontFamily, size: c.fontSize, weight: c.fontWeight, lh: c.lineHeight, ls: c.letterSpacing, tt: c.textTransform,
        color: c.color, bg: c.backgroundColor, radius: c.borderRadius, bw: c.borderTopWidth, bc: c.borderTopColor,
        pad: c.padding, shadow: c.boxShadow === 'none' ? 'none' : c.boxShadow.slice(0, 120),
        h: Math.round(r.height), w: Math.round(r.width),
      };
    };
    const byText = (sel, re) => {
      const el = [...document.querySelectorAll(sel)].find((e) => re.test((e.innerText || '').replace(/\s+/g, ' ').trim()) && e.getBoundingClientRect().width > 2);
      if (!el) return null;
      el.setAttribute('data-m-mark', '1');
      const out = pick('[data-m-mark="1"]');
      el.removeAttribute('data-m-mark');
      return out;
    };
    return {
      label,
      url: location.pathname,
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      h1: pick('h1'),
      h2: pick('h2'),
      body: pick('body'),
      primary: byText('a.button-n', /^Try for free$|^Get started$/),
      secondary: byText('a.button-n.is-lightgreen', /Book a demo|Login/),
      ghost: byText('a.button-n.is-transparent', /Login/),
      navToggle: pick('.dropdown-toggle_nav'),
      tab: pick('.w-tab-link.w--current'),
      tabIdle: pick('.w-tab-link:not(.w--current)'),
      field: pick('input.w-input'),
      faq: pick('.faq_accordion, .accordion, .w-dropdown.faq'),
      menu: pick('.w-dropdown-list.w--open'),
      nav: pick('.nav_component'),
      footer: pick('.section_footer, footer'),
      card: pick('.dropdown-nav_link, .feature-card, .blog_card, .w-dyn-item a'),
    };
  }, label);
}

const readings = [];
const walls = [];

async function runDesktop() {
  const vw = 1440, vh = 900, dpr = 1;
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const { browser, context } = await launch({ width: vw, height: vh, dpr });
  const page = await context.newPage();
  try {
    await page.goto(BASE + '/', { waitUntil: 'load', timeout: 90000 });
    const s = await settle(page);
    await hideConsent(page);
    log('home', s.title, 'blocked', s.blocked);
    if (s.blocked) throw new Error('homepage blocked');
    const vars = await readVars(page);
    fs.writeFileSync(path.join(OUT, 'css-vars.json'), JSON.stringify({ capturedAt: new Date().toISOString(), page: '/', ...vars }, null, 2));
    await shot(page, 'home-light-default.png', requested);
    readings.push(await measure(page, 'home-default'));

    await page.locator('.dropdown-toggle_nav').filter({ hasText: 'Booking system' }).first().hover();
    await wait(page, 700);
    await shot(page, 'home-light-menu-booking.png', requested);
    readings.push(await measure(page, 'menu-booking'));
    await page.mouse.move(10, 400);
    await wait(page, 300);

    await page.locator('.dropdown-toggle_nav').filter({ hasText: 'Marketing' }).first().hover();
    await wait(page, 700);
    await shot(page, 'home-light-menu-marketing.png', requested);
    await page.mouse.move(10, 400);
    await wait(page, 200);

    const tab = page.locator('.w-tab-link').filter({ hasText: 'More bookings' }).first();
    if (await tab.count()) {
      await tab.click({ force: true });
      await wait(page, 600);
      await shot(page, 'home-light-tab.png', requested);
      readings.push(await measure(page, 'home-tab'));
    }

    const faq = page.locator('button, .w-dropdown-toggle, [role="button"]').filter({ hasText: 'What exactly does Understory do?' }).first();
    if (await faq.count()) {
      await faq.scrollIntoViewIfNeeded();
      await faq.click({ force: true });
      await wait(page, 500);
      await shot(page, 'home-light-faq.png', requested);
      readings.push(await measure(page, 'home-faq'));
    }

    await page.evaluate(() => scrollTo(0, 0));
    await full(page, 'home-light-full.png', requested);

    const primary = page.locator('a.button-n').filter({ hasText: /^Try for free$/ }).first();
    if (await primary.count()) {
      await primary.hover();
      await wait(page, 400);
      await shot(page, 'home-light-button-hover.png', requested);
      readings.push(await measure(page, 'button-hover'));
      await primary.focus();
      await wait(page, 250);
      await shot(page, 'home-light-button-focus.png', requested);
    }

    const field = page.locator('input.w-input').first();
    if (await field.count()) {
      await field.scrollIntoViewIfNeeded();
      await field.focus();
      await wait(page, 300);
      await shot(page, 'home-light-field-focus.png', requested);
      readings.push(await measure(page, 'field-focus'));
    }

    await page.goto(BASE + '/pricing', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'pricing-light-default.png', requested);
    readings.push(await measure(page, 'pricing'));
    await full(page, 'pricing-light-full.png', requested);

    await page.goto(BASE + '/blog', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'blog-light-default.png', requested);
    const radio = page.locator('input[type="radio"][name="filters"]').nth(1);
    if (await radio.count()) {
      await radio.click({ force: true });
      await wait(page, 500);
      await shot(page, 'blog-light-filter.png', requested);
    }

    await page.goto(BASE + '/ticketing', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'ticketing-light-default.png', requested);
    readings.push(await measure(page, 'ticketing'));

    await page.goto(BASE + '/tours', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'tours-light-default.png', requested);

    await page.goto(BASE + '/support', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'support-light-default.png', requested);
    const sfaq = page.getByText('How long does it take to set up and go live?').first();
    if (await sfaq.count()) {
      await sfaq.click({ force: true });
      await wait(page, 500);
      await shot(page, 'support-light-faq.png', requested);
    }

    await page.goto('https://help.understory.io/en', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1500);
    await shot(page, 'help-light-default.png', requested);

    await page.goto('https://developer.understory.io/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1500);
    await shot(page, 'docs-light-default.png', requested);
    const theme = page.getByRole('button', { name: /light|dark/i }).first();
    if (await theme.count()) {
      await theme.click();
      await wait(page, 600);
      await shot(page, 'docs-dark-default.png', requested);
    }

    // Login wall: record URL and visible fields. Do not type. Do not submit.
    await page.goto('https://backoffice.understory.io/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1500);
    const wall = await page.evaluate(() => ({
      url: location.href.split('?')[0],
      title: document.title,
      hasPassword: !!document.querySelector('input[type="password"]'),
      hasEmail: !!document.querySelector('input[type="email"], input[name="email"]'),
      google: [...document.querySelectorAll('button, a')].some((el) => /google/i.test(el.innerText || '')),
      apple: [...document.querySelectorAll('button, a')].some((el) => /apple/i.test(el.innerText || '')),
      labels: [...document.querySelectorAll('button, a, label')].map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 16),
    }));
    walls.push(wall);
    log('WALL', JSON.stringify(wall));
    // Do not screenshot the login form: it is an auth wall and the task says stop that branch.
  } finally {
    await context.close();
    await browser.close();
  }
}

async function runPhone() {
  const vw = 390, vh = 844, dpr = 2;
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const { browser, context } = await launch({ width: vw, height: vh, mobile: true, dpr });
  const page = await context.newPage();
  try {
    await page.goto(BASE + '/', { waitUntil: 'load', timeout: 90000 });
    const s = await settle(page);
    await hideConsent(page);
    log('mobile home', s.title, 'blocked', s.blocked);
    await shot(page, 'mobile-home-light-default.png', requested);
    readings.push(await measure(page, 'mobile-home'));
    const burger = page.locator('.w-nav-button').first();
    if (await burger.count()) {
      await burger.click({ force: true });
      await wait(page, 700);
      await shot(page, 'mobile-home-light-menu.png', requested);
      readings.push(await measure(page, 'mobile-menu'));
    }
    await page.keyboard.press('Escape').catch(() => {});
    await page.evaluate(() => scrollTo(0, 0));
    await full(page, 'mobile-home-light-full.png', requested);

    await page.goto(BASE + '/pricing', { waitUntil: 'load', timeout: 60000 });
    await settle(page);
    await hideConsent(page);
    await shot(page, 'mobile-pricing-light-default.png', requested);
    await full(page, 'mobile-pricing-light-full.png', requested);
  } finally {
    await context.close();
    await browser.close();
  }
}

await runDesktop();
await runPhone();
fs.writeFileSync(path.join(OUT, 'components-computed.json'), JSON.stringify({ capturedAt: new Date().toISOString(), readings }, null, 2));
fs.writeFileSync(path.join(OUT, 'walls.json'), JSON.stringify({ capturedAt: new Date().toISOString(), walls }, null, 2));
log('done readings', readings.length, 'walls', walls.length);
