// Captures IKEA Singapore public pages. Nothing is submitted. Login branches stop.
// Country and store dialogs are opened and closed without a selection.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   RAW=~/.design-systems/ikea/raw-shots node tools/capture/public/public.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { launch, hideConsent, isLoginWall, openPublic, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'ikea', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = [
  { name: 'home', path: '/sg/en/' },
  { name: 'products', path: '/sg/en/cat/products-products/' },
  { name: 'rooms', path: '/sg/en/rooms/' },
  { name: 'offers', path: '/sg/en/offers/' },
  { name: 'ideas', path: '/sg/en/ideas/' },
  { name: 'services', path: '/sg/en/customer-service/services/' },
  { name: 'search', path: '/sg/en/search/?q=sofa' },
  { name: 'plp', path: '/sg/en/cat/sofas-armchairs-700640/' },
  { name: 'pdp', path: '/sg/en/p/vinterfint-artificial-christmas-tree-in-outdoor-green-60636381/' },
  { name: 'cart', path: '/sg/en/cart/' },
  { name: 'favourites', path: '/sg/en/favourites/' },
  { name: 'stores', path: '/sg/en/stores/' },
  { name: 'customer-service', path: '/sg/en/customer-service/faq/' },
  { name: 'family', path: '/sg/en/ikea-family/' },
  { name: 'new', path: '/sg/en/new/' },
  { name: 'planners', path: '/sg/en/planners/' },
  { name: 'about', path: '/sg/en/this-is-ikea/about-us/' },
  { name: 'delivery', path: '/sg/en/customer-service/services/delivery/' },
  { name: 'christmas', path: '/sg/en/campaigns/christmas/' },
  { name: 'login', path: '/sg/en/profile/login/', wall: true },
];

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log('  !', name, 'page is', H, 'px, capturing first', hCap);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) {
      await screenshotWithMetadata(this.p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.p, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    log('  shot', this.prefix, name, 'H=' + H);
    await this.p.evaluate(() => scrollTo(0, 0));
  }
}

async function dismissOverlays(page) {
  await hideConsent(page);
  await page.keyboard.press('Escape').catch(() => {});
  await wait(page, 200);
}

async function shotPage(context, spec, { mobile }) {
  const prefix = (mobile ? 'mobile-' : '') + spec.name + '-light';
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const S = new Shooter(page, prefix, vw, vh, dpr);
  try {
    const opened = await openPublic(page, BASE + spec.path, { wait: 2800 });
    log('open', spec.name, opened.status, opened.url);
    if (isLoginWall(opened.url) || spec.wall) {
      await S.view('login-wall');
      log('  STOP login wall', opened.url);
      return { name: spec.name, url: opened.url, stopped: 'login-wall' };
    }
    await S.view('default');
    if (!mobile) await S.full();
    else await S.full();
    return { name: spec.name, url: opened.url, status: opened.status };
  } catch (e) {
    log('  FAILED', spec.name, String(e.message).split('\n')[0]);
    return { name: spec.name, error: String(e.message).split('\n')[0] };
  } finally {
    await page.close().catch(() => {});
  }
}

async function interactions(context) {
  const page = await context.newPage();
  page.setDefaultTimeout(15000);
  const S = new Shooter(page, 'home-light', 1440, 900, 1);
  const notes = [];
  try {
    await openPublic(page, BASE + '/sg/en/', { wait: 2500 });
    await dismissOverlays(page);
    // Products mega menu
    await page.locator('a.hnf-menu__entrypoint', { hasText: 'Products' }).first().click();
    await wait(page, 900);
    await S.view('products-menu');
    await page.keyboard.press('Escape');
    await wait(page, 400);
    // Search suggestions, typed, not submitted with a password and not a form POST beyond the public search page
    await page.locator('#ikea-search-input').click();
    await wait(page, 600);
    await S.view('search-focus');
    await page.keyboard.type('sofa', { delay: 20 });
    await wait(page, 1200);
    await S.view('search-suggest');
    await page.keyboard.press('Escape');
    await wait(page, 300);
    // Store dialog: open and close. Do not pick a store.
    // A saved store preference turns this button into a store sheet with an address.
    // Skip the shot when the button is no longer the generic "Select store" control.
    const storeBtn = page.getByRole('button', { name: 'Select store' }).first();
    const storeLabel = await storeBtn.innerText().catch(() => '');
    if (/^select store$/i.test(storeLabel.trim())) {
      await storeBtn.click();
      await wait(page, 1000);
      const sheetText = await page.locator('[role="dialog"]').innerText().catch(() => '');
      if (!/\d{2,}/.test(sheetText)) await S.view('store-dialog');
      else log('  skip store-dialog: sheet shows a saved store');
      await page.keyboard.press('Escape');
      await wait(page, 400);
    } else {
      log('  skip store-dialog: button is not Select store');
    }
    // Language dialog: open and close. Do not change country.
    await page.getByRole('button', { name: /Change language or country/ }).first().click();
    await wait(page, 900);
    await S.view('country-dialog');
    await page.keyboard.press('Escape');
    notes.push('menus and dialogs captured on home');
  } catch (e) {
    notes.push('interaction failed: ' + String(e.message).split('\n')[0]);
    log('  interaction', notes.at(-1));
  } finally {
    await page.close().catch(() => {});
  }
  return notes;
}

async function mobileMenu(context) {
  const page = await context.newPage();
  const S = new Shooter(page, 'mobile-home-light', 390, 844, 2);
  try {
    await openPublic(page, BASE + '/sg/en/', { wait: 2500 });
    await hideConsent(page);
    const menu = page.getByRole('button', { name: 'Menu' }).first();
    if (await menu.count()) {
      await menu.click();
      await wait(page, 900);
      await S.view('menu');
      await page.keyboard.press('Escape');
    } else {
      log('  no mobile Menu button');
    }
  } catch (e) {
    log('  mobile menu failed', String(e.message).split('\n')[0]);
  } finally {
    await page.close().catch(() => {});
  }
}

const report = { desktop: [], mobile: [], notes: [] };
const desk = await launch({ width: 1440, height: 900 });
try {
  for (const spec of PAGES) {
    if (only.size && !only.has(spec.name) && !only.has('desktop')) continue;
    report.desktop.push(await shotPage(desk.context, spec, { mobile: false }));
  }
  if (!only.size || only.has('interactions')) report.notes.push(...await interactions(desk.context));
} finally {
  await desk.browser.close();
}

const phonePages = PAGES.filter((p) => ['home', 'plp', 'pdp', 'search', 'cart', 'login', 'products'].includes(p.name));
const mob = await launch({ mobile: true });
try {
  for (const spec of phonePages) {
    if (only.size && !only.has(spec.name) && !only.has('mobile')) continue;
    report.mobile.push(await shotPage(mob.context, spec, { mobile: true }));
  }
  if (!only.size || only.has('mobile')) await mobileMenu(mob.context);
} finally {
  await mob.browser.close();
}

fs.writeFileSync(path.join(RAW, 'capture-report.json'), JSON.stringify(report, null, 2));
log('done', RAW);
