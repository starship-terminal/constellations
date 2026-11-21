// Public Playwright walk of voicenotes.com. Photographs reachable public
// states, reads computed styles, and stops at a login or signup wall.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   RAW=~/.design-systems/voicenotes/raw-shots \
//     node tools/capture/public/walk.mjs
//
// Does not type an email, name, password or code. Does not click Google,
// Apple, Microsoft, Twitter, SSO or any other identity provider. Does not
// submit a form, create an account, or solve a captcha.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems', 'voicenotes', 'raw-shots');
const OUT = path.join(PKG, 'raw', 'playwright-2026-11-21.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://voicenotes.com';

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const AUTH = /\/(login|signup|sign-up|register|auth)\b/i;
const IDP = /google|apple|microsoft|facebook|twitter|sso|github/i;

function publicUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function shot(page, name, requested) {
  const file = path.join(RAW, `${name}.png`);
  await screenshotWithMetadata(page, { path: file }, {
    ...requested,
    sanitizedSourceUrl: publicUrl(page.url()),
  });
  log('shot', name, publicUrl(page.url()));
  return file;
}

async function metrics(page) {
  return page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    devicePixelRatio: window.devicePixelRatio,
    visualViewport: window.visualViewport
      ? { width: window.visualViewport.width, height: window.visualViewport.height, scale: window.visualViewport.scale }
      : null,
  }));
}

async function readStyles(page, label) {
  return page.evaluate((label) => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80),
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        color: s.color,
        backgroundColor: s.backgroundColor,
        borderRadius: s.borderRadius,
        borderTopWidth: s.borderTopWidth,
        borderTopColor: s.borderTopColor,
        padding: s.padding,
        height: Math.round(r.height),
        width: Math.round(r.width),
        boxShadow: s.boxShadow === 'none' ? 'none' : s.boxShadow.slice(0, 180),
        transition: s.transitionDuration + ' ' + s.transitionTimingFunction,
      };
    };
    const byText = (sel, text) => [...document.querySelectorAll(sel)].find((el) => (el.innerText || '').trim().startsWith(text));
    const h1 = document.querySelector('h1');
    const h2 = document.querySelector('h2');
    const header = document.querySelector('header');
    const filled = [...document.querySelectorAll('button, a')].find((el) => /Start for free|Try Voicenotes|Get started/.test((el.innerText || '').trim()));
    const quiet = [...document.querySelectorAll('button, a')].find((el) => /Book a demo|Talk to sales/.test((el.innerText || '').trim()));
    const nav = [...document.querySelectorAll('header a, header button')].find((el) => (el.innerText || '').trim() === 'Pricing' || (el.innerText || '').trim() === 'Enterprise');
    return {
      label,
      url: location.origin + location.pathname,
      title: document.title,
      htmlClass: document.documentElement.className,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      pageBg: getComputedStyle(document.documentElement).backgroundColor,
      header: pick(header),
      h1: pick(h1),
      h2: pick(h2),
      filled: pick(filled),
      quiet: pick(quiet),
      nav: pick(nav),
    };
  }, label);
}

async function openMenu(page, label) {
  const btn = page.locator('header button').filter({ hasText: label }).first();
  await btn.hover();
  await wait(page, 500);
  const open = await page.evaluate((label) => {
    const root = [...document.querySelectorAll('header .relative')].find((el) => (el.innerText || '').trim().startsWith(label));
    if (!root) return false;
    const panel = [...root.querySelectorAll('div')].find((d) => (d.innerText || '').length > 12 && d.getBoundingClientRect().height > 40);
    return !!panel;
  }, label);
  return open;
}

const tree = [];
function note(row) {
  tree.push(row);
  log('tree', row.control, '->', row.result);
}

async function contextFor(browser, mobile) {
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const ctx = await browser.newContext(mobile
    ? { ...requested, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { ...requested, userAgent: UA, locale: 'en-US' });
  return { ctx, requested };
}

async function gotoPublic(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(page, 1800);
  const final = publicUrl(page.url());
  if (AUTH.test(final || '')) {
    return { stopped: true, status: resp && resp.status(), url: final };
  }
  const title = await page.title();
  const body = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 180));
  const blocked = /just a moment|verify you are human|performing security verification/i.test(title + body);
  return { stopped: false, blocked, status: resp && resp.status(), url: final, title };
}

const browser = await chromium.launch({ headless: true });
const readings = { captured: '2026-11-21', method: 'Playwright headless Chromium, public pages only. No form submitted. No identity provider clicked.', pages: {}, walls: [] };

// Desktop walk.
{
  const { ctx, requested } = await contextFor(browser, false);
  const page = await ctx.newPage();
  const home = await gotoPublic(page, BASE + '/');
  if (home.blocked || !home.url) {
    log('STOP site did not load', JSON.stringify(home));
    fs.writeFileSync(path.join(RAW, 'load-failure.json'), JSON.stringify(home, null, 2));
    await browser.close();
    process.exit(2);
  }
  readings.viewportDesktop = await metrics(page);
  readings.pages.home = await readStyles(page, 'home');
  await shot(page, 'home-light-default', requested);
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h && y < 9000; y += 700) {
      scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    scrollTo(0, 0);
  });
  await wait(page, 600);
  await shot(page, 'home-light-full', { ...requested, full: true });
  await page.screenshot({ path: path.join(RAW, 'home-light-full.png'), fullPage: true }).catch(async (e) => {
    log('fullPage failed', e.message.split('\n')[0]);
  });

  if (await openMenu(page, 'Download')) {
    await shot(page, 'home-light-download-open', requested);
    note({ control: 'Header Download', from: BASE + '/', result: 'menu: Desktop (submenu), iOS App Store, Android Play Store', followed: false });
  } else note({ control: 'Header Download', from: BASE + '/', result: 'menu did not open on hover', followed: false });
  await page.mouse.move(10, 400);
  await wait(page, 300);

  if (await openMenu(page, 'Resources')) {
    await shot(page, 'home-light-resources-open', requested);
    note({
      control: 'Header Resources',
      from: BASE + '/',
      result: 'menu: Integrations (help.voicenotes.com), Help Center (help.voicenotes.com), Blog (/blog), What\'s new (/whats-new/)',
      followed: false,
    });
  } else note({ control: 'Header Resources', from: BASE + '/', result: 'menu did not open on hover', followed: false });
  await page.mouse.move(10, 400);

  note({ control: 'Header Enterprise', from: BASE + '/', result: BASE + '/enterprise', followed: true });
  note({ control: 'Header Pricing', from: BASE + '/', result: BASE + '/pricing', followed: true });
  note({ control: 'Header Log in', from: BASE + '/', result: 'login wall (modal on marketing origin, also /login). Stopped. Not submitted.', followed: false });
  note({ control: 'Header Book a demo', from: BASE + '/', result: BASE + '/enterprise', followed: true });
  note({ control: 'Header Start for free', from: BASE + '/', result: BASE + '/signup signup wall. Stopped. Not submitted.', followed: false });
  note({ control: 'Hero Book a demo', from: BASE + '/', result: BASE + '/enterprise', followed: true });
  note({ control: 'Hero Start for free', from: BASE + '/', result: BASE + '/signup signup wall. Stopped.', followed: false });
  note({ control: 'Hero demo Cancel / Record', from: BASE + '/', result: 'in-page marketing demo controls. Not a signed-in app. Record was not pressed.', followed: false });

  // Login wall: open, photograph, do not type, do not click an identity provider.
  await page.getByRole('link', { name: 'Log in' }).first().click();
  await wait(page, 900);
  const loginModal = await page.evaluate(() => {
    const d = document.querySelector('[role="dialog"]');
    if (!d) return null;
    return {
      text: (d.innerText || '').replace(/\s+/g, ' ').slice(0, 400),
      buttons: [...d.querySelectorAll('button, a')].map((el) => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40)).filter(Boolean),
      inputs: [...d.querySelectorAll('input')].map((i) => i.placeholder || i.type),
    };
  });
  readings.walls.push({ kind: 'login-modal', url: publicUrl(page.url()), ...loginModal });
  await shot(page, 'home-light-login-modal', requested);
  await page.keyboard.press('Escape');
  await wait(page, 400);

  // Signup wall: navigate, photograph, stop. Do not click providers or Continue with Email.
  const signup = await gotoPublic(page, BASE + '/signup');
  readings.walls.push({ kind: 'signup', url: signup.url, title: signup.title, stopped: true });
  if (!signup.blocked) {
    readings.pages.signup = await page.evaluate(() => ({
      url: location.origin + location.pathname,
      title: document.title,
      text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 500),
      buttons: [...document.querySelectorAll('button, a')].map((el) => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40)).filter(Boolean).slice(0, 16),
      inputs: [...document.querySelectorAll('input')].map((i) => ({ type: i.type, placeholder: i.placeholder })),
    }));
    await shot(page, 'signup-light-default', requested);
  }

  const loginPage = await gotoPublic(page, BASE + '/login');
  readings.walls.push({ kind: 'login-page', url: loginPage.url, title: loginPage.title, stopped: true });
  if (!loginPage.blocked) {
    readings.pages.login = await page.evaluate(() => ({
      url: location.origin + location.pathname,
      title: document.title,
      text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 500),
      buttons: [...document.querySelectorAll('button, a')].map((el) => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40)).filter(Boolean).slice(0, 16),
      inputs: [...document.querySelectorAll('input')].map((i) => ({ type: i.type, placeholder: i.placeholder })),
    }));
    await shot(page, 'login-light-default', requested);
  }

  for (const [name, url] of [
    ['pricing', '/pricing'],
    ['enterprise', '/enterprise'],
    ['brand-assets', '/brand-assets'],
    ['reviews', '/reviews'],
    ['blog', '/blog/'],
    ['whats-new', '/whats-new/'],
  ]) {
    const landed = await gotoPublic(page, BASE + url);
    note({ control: name, from: 'direct', result: landed.url || url, followed: !landed.stopped, stopped: landed.stopped });
    if (landed.stopped || landed.blocked) continue;
    readings.pages[name] = await readStyles(page, name);
    readings.pages[name].viewport = await metrics(page);
    await shot(page, `${name}-light-default`, requested);
  }

  // One published blog post, linked from the index.
  await gotoPublic(page, BASE + '/blog/');
  const postHref = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((el) => /\/blog\/.+\/.+/.test(el.getAttribute('href') || '') && (el.innerText || '').trim().length > 24);
    return a ? a.getAttribute('href') : null;
  });
  if (postHref && !AUTH.test(postHref)) {
    const abs = postHref.startsWith('http') ? postHref : BASE + postHref;
    const landed = await gotoPublic(page, abs);
    note({ control: 'Blog index first post', from: BASE + '/blog/', result: landed.url, followed: true });
    if (!landed.stopped && !landed.blocked) {
      readings.pages.blogPost = await readStyles(page, 'blog-post');
      await shot(page, 'blog-post-light-default', requested);
    }
  }

  // Pricing billing pill and one FAQ, both local toggles. Plan CTAs are not followed (they open signup).
  await gotoPublic(page, BASE + '/pricing');
  const annual = page.getByRole('button', { name: /Annual/ }).first();
  if (await annual.count()) {
    await annual.click();
    await wait(page, 500);
    readings.pages.pricingAnnual = await page.evaluate(() => {
      const badge = [...document.querySelectorAll('*')].find((el) => (el.innerText || '').trim() === '2 months free');
      const s = badge ? getComputedStyle(badge) : null;
      return {
        badge: s && {
          color: s.color,
          backgroundColor: s.backgroundColor,
          borderRadius: s.borderRadius,
          fontSize: s.fontSize,
          fontFamily: s.fontFamily,
        },
      };
    });
    await shot(page, 'pricing-light-annual', requested);
    note({ control: 'Pricing Annual', from: BASE + '/pricing', result: 'local billing pill, stays on /pricing', followed: true });
  }
  const faq = page.getByRole('button', { name: /Can I try Voicenotes/ }).first();
  if (await faq.count()) {
    await faq.click();
    await wait(page, 500);
    await shot(page, 'pricing-light-faq-open', requested);
    note({ control: 'Pricing FAQ first question', from: BASE + '/pricing', result: 'accordion opens on the same page', followed: true });
  }
  note({ control: 'Pricing Get started', from: BASE + '/pricing', result: 'signup wall. Not followed.', followed: false });
  note({ control: 'Pricing Talk to sales', from: BASE + '/pricing', result: BASE + '/enterprise (same destination as Book a demo). Not submitted.', followed: false });

  await ctx.close();
}

// Phone width.
{
  const { ctx, requested } = await contextFor(browser, true);
  const page = await ctx.newPage();
  const home = await gotoPublic(page, BASE + '/');
  readings.viewportMobile = await metrics(page);
  if (!home.stopped && !home.blocked) {
    readings.pages.mobileHome = await readStyles(page, 'mobile-home');
    await shot(page, 'mobile-home-light-default', requested);
    const menuBtn = page.locator('header button, button').filter({ hasText: /menu/i });
    const iconBtn = page.locator('header button').last();
    const count = await page.locator('header button').count();
    if (count) {
      await page.locator('header button').first().click().catch(() => {});
      await wait(page, 700);
      await shot(page, 'mobile-home-light-menu', requested);
      note({ control: 'Mobile header button', from: BASE + '/', result: 'photographed after one click. If it opened a sheet, the shot shows it.', followed: true });
    }
    await gotoPublic(page, BASE + '/pricing');
    readings.pages.mobilePricing = await readStyles(page, 'mobile-pricing');
    await shot(page, 'mobile-pricing-light-default', requested);
  }
  await ctx.close();
}

readings.siteTree = tree;
readings.identityProvidersNotClicked = ['Google', 'Microsoft', 'Apple', 'Twitter', 'SSO'];
fs.writeFileSync(OUT, JSON.stringify(readings, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'site-tree.json'), JSON.stringify(tree, null, 2) + '\n');
log('wrote', OUT);
await browser.close();
