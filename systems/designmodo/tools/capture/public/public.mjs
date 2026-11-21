// Photographs Designmodo's public signed-out pages and opened menus.
// Desktop 1440x900 and phone 390x844. Does not submit forms, type a password,
// click an identity provider, or enter a builder canvas.
//
//   PLAYWRIGHT=... RAW=~/.design-systems/designmodo/raw-shots node public.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, hideConsent } from './lib.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'designmodo', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const DESKTOP = { width: 1440, height: 900, dpr: 1 };
const PHONE = { width: 390, height: 844, dpr: 2 };

function slug(p) {
  return (p === '/' ? 'home' : p.replace(/^\//, '').replace(/\/$/, '').replace(/\//g, '-')).slice(0, 70);
}

async function settle(page) {
  await page.waitForFunction(() => {
    const text = (document.body && document.body.innerText) || '';
    return text.trim().length > 40 && document.documentElement.scrollHeight > 200;
  }, { timeout: 20000 }).catch(() => {});
  await page.evaluate(() => document.fonts && document.fonts.ready).catch(() => {});
  await page.waitForTimeout(700);
  await hideConsent(page);
  await page.waitForTimeout(250);
}

async function goto(page, url) {
  const resp = await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await settle(page);
  return resp?.status() || 0;
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
  }
  async view(name) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const steps = Math.min(12, Math.ceil(H0 / 700));
    for (let i = 0; i < steps; i++) {
      await p.evaluate((y) => scrollTo(0, y), i * 700);
      await p.waitForTimeout(180);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await p.waitForTimeout(400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(path.join(RAW, old));
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openDropdown(page, id) {
  await page.evaluate((id) => {
    document.querySelectorAll('.dropdown.show').forEach((d) => d.classList.remove('show'));
    const trigger = document.querySelector(`a.dropdownTrigger[data-dropdown-id="${id}"]`);
    const panel = document.querySelector(`div.dropdown[data-dropdown-id="${id}"]`);
    if (trigger) trigger.classList.add('triggered');
    if (panel) panel.classList.add('show');
  }, id);
  await page.waitForTimeout(450);
}

async function closeDropdowns(page) {
  await page.evaluate(() => {
    document.querySelectorAll('.dropdown.show').forEach((d) => d.classList.remove('show'));
    document.querySelectorAll('.dropdownTrigger.triggered').forEach((d) => d.classList.remove('triggered'));
  });
}

async function openSearch(page) {
  await page.evaluate(() => {
    const form = document.querySelector('form.searchForm');
    if (!form) return;
    form.classList.add('show', 'open', 'active');
    form.style.setProperty('display', 'block', 'important');
    form.style.setProperty('visibility', 'visible', 'important');
    form.style.setProperty('opacity', '1', 'important');
    const wrap = form.closest('.popup, .search, [class*="searchPopup"], .popupContent');
    if (wrap && wrap !== form) {
      wrap.classList.add('show', 'open');
      wrap.style.setProperty('display', 'block', 'important');
    }
  });
  await page.waitForTimeout(300);
}

async function openMobileMenu(page) {
  await page.evaluate(() => {
    const side = document.querySelector('[data-sidebar-id="mobile-menu"].sidebar, nav.sidebar');
    if (side) {
      side.classList.add('show', 'open', 'active');
      side.style.setProperty('display', 'block', 'important');
      side.style.setProperty('transform', 'none', 'important');
      side.style.setProperty('visibility', 'visible', 'important');
    }
    document.body.classList.add('sidebar-open');
  });
  await page.waitForTimeout(400);
}

const PAGES = [
  { id: 'home', url: 'https://designmodo.com/' },
  { id: 'postcards', url: 'https://designmodo.com/postcards/' },
  { id: 'postcards-pricing', url: 'https://designmodo.com/postcards/pricing/' },
  { id: 'slides', url: 'https://designmodo.com/slides/' },
  { id: 'slides-pricing', url: 'https://designmodo.com/slides/pricing/' },
  { id: 'startup', url: 'https://designmodo.com/startup/' },
  { id: 'email-templates', url: 'https://designmodo.com/email-templates/' },
  { id: 'website-templates', url: 'https://designmodo.com/website-templates/' },
  { id: 'articles', url: 'https://designmodo.com/articles/' },
  { id: 'article', url: 'https://designmodo.com/how-to-add-a-countdown-timer-to-email/' },
  { id: 'products', url: 'https://designmodo.com/products/' },
  { id: 'about', url: 'https://designmodo.com/about/' },
  { id: 'contacts', url: 'https://designmodo.com/contacts/' },
  { id: 'subscribe', url: 'https://designmodo.com/subscribe/' },
  { id: 'black-friday', url: 'https://designmodo.com/black-friday/' },
  { id: 'privacy', url: 'https://designmodo.com/privacy-statement/' },
  { id: 'terms', url: 'https://designmodo.com/terms-and-conditions/' },
  { id: 'cookies', url: 'https://designmodo.com/cookies-policy/' },
  { id: 'resources', url: 'https://designmodo.com/resources/' },
  { id: 'sign-in', url: 'https://designmodo.com/my-account/sign-in/' },
  { id: 'sign-up', url: 'https://designmodo.com/my-account/sign-up/' },
  { id: 'lost-password', url: 'https://designmodo.com/my-account/lost-password/' },
  { id: 'help', url: 'https://help.designmodo.com/' },
];

async function runWidth(mobile) {
  const spec = mobile ? PHONE : DESKTOP;
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: spec.width, height: spec.height },
    deviceScaleFactor: spec.dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  const prefix0 = mobile ? 'mobile' : 'desktop';

  for (const item of PAGES) {
    const name = (mobile ? 'mobile-' : '') + item.id;
    log('open', name);
    try {
      await goto(page, item.url);
    } catch (e) {
      log('  FAIL', name, String(e.message).split('\n')[0]);
      continue;
    }
    const S = new Shooter(page, name, spec.width, spec.height, spec.dpr);
    S.requested.sanitizedSourceUrl = item.url;
    await S.view('default');
    if (['home', 'postcards', 'postcards-pricing', 'email-templates', 'slides', 'startup', 'articles', 'sign-in', 'about', 'products'].includes(item.id)) {
      await S.full('full').catch((e) => log('  full fail', e.message.split('\n')[0]));
    }
    if (!mobile && item.id === 'home') {
      await openDropdown(page, 'apps');
      await S.view('apps-menu');
      await closeDropdowns(page);
      await openDropdown(page, 'articles');
      await S.view('articles-menu');
      await closeDropdowns(page);
      await page.evaluate(() => {
        const cart = document.querySelector('#cart.dropdown, [data-dropdown-id="cart"]');
        if (cart) cart.classList.add('show');
      });
      await page.waitForTimeout(300);
      await S.view('cart');
      await closeDropdowns(page);
      await page.evaluate(() => {
        const a = document.querySelector('#account.dropdown, [data-dropdown-id="account"]');
        if (a) a.classList.add('show');
      });
      await page.waitForTimeout(300);
      await S.view('account-menu');
      await closeDropdowns(page);
    }
    if (mobile && item.id === 'home') {
      await openMobileMenu(page);
      await S.view('menu');
    }
  }

  // Postcards gallery: dismiss Welcome-back locally, do not log in.
  log('open gallery');
  try {
    await goto(page, 'https://designmodo.com/postcards/app/');
    const G = new Shooter(page, (mobile ? 'mobile-' : '') + 'postcards-gallery', spec.width, spec.height, spec.dpr);
    G.requested.sanitizedSourceUrl = 'https://designmodo.com/postcards/app/';
    await G.view('welcome');
    const closed = await page.evaluate(() => {
      const buttons = [...document.querySelectorAll('button')];
      const x = buttons.find((b) => {
        const a = (b.getAttribute('aria-label') || '') + ' ' + (b.className || '');
        const r = b.getBoundingClientRect();
        return /close/i.test(a) || (r.width < 48 && r.height < 48 && r.width > 8 && b.closest('[role="dialog"], [class*="modal"], [class*="Modal"]'));
      });
      if (x) { x.click(); return 'clicked-close'; }
      // local dismiss only: hide the welcome dialog node, do not navigate
      const dialog = [...document.querySelectorAll('div, section')].find((e) => /welcome back/i.test(e.innerText || '') && e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().width < 700);
      if (dialog) { dialog.style.setProperty('display', 'none', 'important'); return 'hid-dialog'; }
      return 'none';
    });
    log('  gallery dismiss', closed);
    await page.waitForTimeout(600);
    // also hide leftover scrim if the local hide left one
    await page.evaluate(() => {
      document.querySelectorAll('[class*="overlay"], [class*="backdrop"], [class*="Overlay"]').forEach((n) => {
        const t = n.innerText || '';
        if (/welcome back|continue with google/i.test(t) || getComputedStyle(n).position === 'fixed') {
          if (/welcome back/i.test(t)) n.style.setProperty('display', 'none', 'important');
        }
      });
    });
    await G.view('default');
  } catch (e) {
    log('  gallery FAIL', e.message.split('\n')[0]);
  }

  await browser.close();
}

const only = (process.argv[2] || '').split(',').filter(Boolean);
if (!only.length || only.includes('desktop')) await runWidth(false);
if (!only.length || only.includes('phone')) await runWidth(true);
log('done');
