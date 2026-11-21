// Walk the public MSCHF index and the store pages the index opens.
// Does not type, submit, sign in, or click Log in / Continue / Submit.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node walk.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const SHOTS = path.join(PKG, 'screenshots');
const RAW = path.join(PKG, 'raw');
const SCRATCH = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mschf', 'raw-shots');
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SCRATCH, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function wall(text, url) {
  const t = `${text || ''}\n${url || ''}`;
  if (/shopify\.com\/authentication/i.test(url || '')) return true;
  if (/sign in or create an account/i.test(t)) return true;
  if (/verify you are human|just a moment|cf-challenge|captcha/i.test(t)) return true;
  return false;
}

async function shot(page, name, requested, extra = {}) {
  const dest = path.join(SHOTS, `${name}.png`);
  await screenshotWithMetadata(page, { path: dest }, {
    ...requested,
    sanitizedSourceUrl: extra.sourceUrl || null,
  });
  const side = JSON.parse(fs.readFileSync(`${dest}.capture.json`, 'utf8'));
  side.theme = extra.theme || 'store-light';
  side.note = extra.note || 'live headless Chromium; no form submitted';
  side.sourceUrl = extra.sourceUrl || null;
  fs.writeFileSync(`${dest}.capture.json`, JSON.stringify(side, null, 2) + '\n');
  fs.copyFileSync(dest, path.join(SCRATCH, `${name}.png`));
  log('  shot', name, side.actual?.innerWidth, side.png);
}

async function readStyles(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const c = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
        color: c.color,
        backgroundColor: c.backgroundColor,
        fontFamily: c.fontFamily,
        fontSize: c.fontSize,
        fontWeight: c.fontWeight,
        lineHeight: c.lineHeight,
        letterSpacing: c.letterSpacing,
        textTransform: c.textTransform,
        padding: c.padding,
        margin: c.margin,
        borderRadius: c.borderRadius,
        border: c.border,
        boxShadow: c.boxShadow,
        outline: c.outline,
        height: Math.round(r.height),
        width: Math.round(r.width),
      };
    };
    const q = (s) => document.querySelector(s);
    const vars = [];
    for (const sheet of [...document.styleSheets]) {
      let rules;
      try { rules = [...sheet.cssRules]; } catch { continue; }
      const walk = (list) => {
        for (const rule of list) {
          if (rule.style) {
            for (const prop of rule.style) {
              if (prop.startsWith('--')) vars.push({ sel: (rule.selectorText || '').slice(0, 80), prop, val: rule.style.getPropertyValue(prop).trim().slice(0, 80) });
            }
          }
          if (rule.cssRules) walk([...rule.cssRules]);
        }
      };
      walk(rules);
    }
    const counts = {};
    const tally = (el) => {
      const c = getComputedStyle(el);
      for (const key of ['color', 'backgroundColor', 'fontSize', 'borderRadius']) {
        const v = c[key];
        if (!v || v === 'rgba(0, 0, 0, 0)' || v === '0px') continue;
        const k = key + ':' + v;
        counts[k] = (counts[k] || 0) + 1;
      }
    };
    document.querySelectorAll('body, a, button, h1, h2, p, input, label').forEach(tally);
    return {
      href: location.href.split('?')[0],
      title: document.title,
      themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      body: pick(document.body),
      header: pick(q('header')),
      footer: pick(q('footer')),
      h1: pick(q('h1')),
      button: pick(q('button')),
      link: pick(q('a')),
      search: pick(q('input[type="search"]')),
      productTitle: pick(q('.product__title, h1')),
      varCount: vars.length,
      vars: vars.slice(0, 80),
      counts,
      viewport: { innerWidth, innerHeight, dpr: devicePixelRatio },
    };
  });
}

const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  return browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
}

const readings = {};
const stops = [];

async function open(ctx, url, name, requested, { interact, mobile } = {}) {
  const page = await ctx.newPage();
  page.setDefaultTimeout(20000);
  log('open', name, url);
  let resp;
  try {
    resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 40000 });
  } catch (e) {
    stops.push({ name, url, error: String(e.message || e).split('\n')[0] });
    await page.close();
    return;
  }
  await wait(page, 1600);
  const finalUrl = page.url();
  const text = await page.evaluate(() => (document.body?.innerText || '').slice(0, 1500));
  if (wall(text, finalUrl)) {
    stops.push({ name, url, finalUrl, wall: true, title: await page.title(), text: text.slice(0, 400) });
    log('  WALL', finalUrl);
    await page.close();
    return;
  }
  readings[name] = {
    status: resp && resp.status(),
    finalUrl: finalUrl.split('?')[0],
    styles: await readStyles(page),
  };
  await shot(page, name, requested, { sourceUrl: url.split('?')[0], theme: name.includes('home') || name.includes('not-found') ? 'dark' : 'store-light', note: mobile ? 'phone 390' : 'desktop 1440' });
  if (interact) {
    try { await interact(page, name, requested); } catch (e) { log('  interact fail', name, String(e.message || e).split('\n')[0]); }
  }
  await page.close();
}

const desktopReq = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const phoneReq = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };

const desk = await contextFor(false);

await open(desk, 'https://mschf.com/', 'home-dark-default-2026-11-21', desktopReq, {
  interact: async (page, _name, requested) => {
    const shop = page.locator('header a, a').filter({ hasText: /SHOP/i }).first();
    if (await shop.count()) {
      await shop.hover();
      await wait(page, 400);
      await shot(page, 'home-dark-shop-hover-2026-11-21', requested, { sourceUrl: 'https://mschf.com/', theme: 'dark', note: 'SHOP link hover' });
    }
  },
});

await open(desk, 'https://mschf.com/missing-page', 'not-found-dark-default-2026-11-21', desktopReq);

await open(desk, 'https://store.mschf.com/', 'store-light-default', desktopReq, {
  interact: async (page, _name, requested) => {
    const search = page.getByRole('button', { name: 'Search' }).first();
    if (await search.count()) {
      await search.click();
      await wait(page, 600);
      const field = page.locator('input[type="search"][name="q"]').first();
      if (await field.count()) {
        await field.focus();
        await wait(page, 300);
        await shot(page, 'store-light-search-focus', requested, { sourceUrl: 'https://store.mschf.com/', theme: 'store-light', note: 'search field focused, nothing typed' });
      }
      await page.keyboard.press('Escape');
      await wait(page, 300);
    }
    const country = page.getByRole('button', { name: /Singapore/i }).first();
    if (await country.count()) {
      await country.click();
      await wait(page, 700);
      await shot(page, 'store-light-country', requested, { sourceUrl: 'https://store.mschf.com/', theme: 'store-light', note: 'country picker open, no country chosen' });
      await page.keyboard.press('Escape');
      await wait(page, 300);
    }
  },
});

await open(desk, 'https://store.mschf.com/products/super-normal-2', 'store-product-light-default', desktopReq, {
  interact: async (page, _name, requested) => {
    const size = page.locator('input[type="radio"], fieldset label, [name="options"]').first();
    const sold = page.getByRole('button', { name: /Sold out/i }).first();
    if (await sold.count()) {
      await sold.scrollIntoViewIfNeeded().catch(() => {});
      await wait(page, 300);
      await shot(page, 'store-product-light-soldout', requested, { sourceUrl: 'https://store.mschf.com/products/super-normal-2', theme: 'store-light', note: 'sold out control in view; not clicked' });
    }
    const notify = page.getByRole('button', { name: /Get notified/i }).first();
    if (await notify.count()) {
      await notify.click();
      await wait(page, 800);
      const after = await page.evaluate(() => location.href);
      const text = await page.evaluate(() => (document.body?.innerText || '').slice(0, 400));
      if (wall(text, after)) {
        stops.push({ name: 'notify', url: after, wall: true, text: text.slice(0, 200) });
        log('  WALL after notify');
        return;
      }
      await shot(page, 'store-product-light-notify', requested, { sourceUrl: 'https://store.mschf.com/products/super-normal-2', theme: 'store-light', note: 'notify disclosure opened; email not filled' });
      await page.keyboard.press('Escape');
    }
    void size;
  },
});

await open(desk, 'https://store.mschf.com/cart', 'store-cart-light-empty', desktopReq);
await open(desk, 'https://store.mschf.com/search?q=boot', 'store-search-light-results', desktopReq, {
  interact: async (page, _name, requested) => {
    const filter = page.getByRole('button', { name: 'Availability' }).first();
    if (await filter.count()) {
      await filter.click();
      await wait(page, 500);
      await shot(page, 'store-search-light-filter', requested, { sourceUrl: 'https://store.mschf.com/search', theme: 'store-light', note: 'availability filter open; apply not clicked' });
    }
  },
});
await open(desk, 'https://store.mschf.com/policies/contact-information', 'store-contact-light-default', desktopReq);
await open(desk, 'https://store.mschf.com/policies/privacy-policy', 'store-privacy-light-default', desktopReq);

await desk.close();

const phone = await contextFor(true);
await open(phone, 'https://mschf.com/', 'mobile-home-dark-default-2026-11-21', phoneReq, { mobile: true });
await open(phone, 'https://store.mschf.com/', 'mobile-store-light-default', phoneReq, { mobile: true, interact: async (page, _name, requested) => {
  const menu = page.locator('button').filter({ hasText: /menu|search/i }).first();
  const search = page.getByRole('button', { name: 'Search' }).first();
  if (await search.count()) {
    await search.click();
    await wait(page, 500);
    await shot(page, 'mobile-store-light-search', requested, { sourceUrl: 'https://store.mschf.com/', theme: 'store-light', note: 'phone search open; nothing typed' });
  } else if (await menu.count()) {
    await menu.click();
    await wait(page, 500);
    await shot(page, 'mobile-store-light-menu', requested, { sourceUrl: 'https://store.mschf.com/', theme: 'store-light', note: 'phone menu' });
  }
} });
await open(phone, 'https://store.mschf.com/products/super-normal-2', 'mobile-store-product-light-default', phoneReq, { mobile: true });
await open(phone, 'https://store.mschf.com/cart', 'mobile-store-cart-light-empty', phoneReq, { mobile: true });
await phone.close();
await browser.close();

fs.writeFileSync(path.join(RAW, 'store-computed.json'), JSON.stringify({ capturedAt: new Date().toISOString(), readings, stops }, null, 2) + '\n');
log('stops', JSON.stringify(stops, null, 2));
log('done', Object.keys(readings).length, 'pages');
