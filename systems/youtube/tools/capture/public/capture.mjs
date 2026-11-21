// Public signed-out capture for YouTube.
// Writes full-colour PNGs to RAW and readings to systems/youtube/raw/.
// Nothing is typed. No form is submitted. Login and signup walls are photographed empty.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
const playwrightPath = process.env.PLAYWRIGHT || `${process.env.HOME}/.design-systems/pw/node_modules/playwright/index.mjs`;
const { chromium } = await import(playwrightPath);

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW_JSON = path.join(PKG, 'raw');
const SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'youtube', 'raw-shots');
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(RAW_JSON, { recursive: true });

const PLAYWRIGHT = process.env.PLAYWRIGHT;
if (PLAYWRIGHT) {
  // playwright is imported as a package; PLAYWRIGHT is recorded for the README.
}

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideConsent(page) {
  await page.addStyleTag({
    content: `
      tp-yt-iron-overlay-backdrop.opened, ytd-consent-bump-v2-lightbox, #consent-bump { display: none !important; }
    `,
  }).catch(() => {});
}

async function shot(page, name, requested) {
  const file = path.join(SHOTS, name + '.png');
  await page.screenshot({ path: file, fullPage: false });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    vv: window.visualViewport && {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    },
    dark: document.documentElement.hasAttribute('dark') || document.documentElement.hasAttribute('system-icons'),
    theme: document.documentElement.getAttribute('dark') !== null ? 'dark-attr' : (document.body && getComputedStyle(document.body).backgroundColor),
  }));
  fs.writeFileSync(file + '.capture.json', JSON.stringify({
    capturedAt: new Date().toISOString(),
    screenshot: name + '.png',
    requested,
    actual: box,
    sanitizedSourceUrl: page.url().split('?')[0].replace(/\/watch$/, '/watch').replace(/\/shorts\/[^/]+/, '/shorts/:id'),
  }, null, 2) + '\n');
  log('  shot', name, box.innerWidth + 'x' + box.innerHeight);
}

async function readVars(page) {
  return page.evaluate(() => {
    const styles = [...document.styleSheets];
    const props = {};
    const errors = [];
    for (const sheet of styles) {
      let rules;
      try { rules = sheet.cssRules; } catch (e) { errors.push(String(e).slice(0, 120)); continue; }
      const walk = (list) => {
        for (const rule of list) {
          if (rule.cssRules) walk(rule.cssRules);
          if (!rule.style) continue;
          for (let i = 0; i < rule.style.length; i++) {
            const name = rule.style[i];
            if (name.startsWith('--')) {
              if (!props[name]) props[name] = [];
              if (props[name].length < 4) props[name].push(rule.style.getPropertyValue(name).trim().slice(0, 200));
            }
          }
        }
      };
      if (rules) walk(rules);
    }
    const cs = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const interesting = [];
    for (let i = 0; i < cs.length; i++) {
      const n = cs[i];
      if (n.startsWith('--')) interesting.push([n, cs.getPropertyValue(n).trim().slice(0, 180)]);
    }
    return {
      href: location.href.split('?')[0],
      title: document.title,
      darkAttr: document.documentElement.hasAttribute('dark'),
      bodyBg: body.backgroundColor,
      bodyColor: body.color,
      bodyFont: body.fontFamily,
      bodySize: body.fontSize,
      propCount: Object.keys(props).length,
      sampleProps: Object.fromEntries(Object.entries(props).slice(0, 80)),
      computedCustom: interesting.slice(0, 80),
      errors: errors.slice(0, 6),
    };
  });
}

async function measure(page, spec) {
  return page.evaluate((spec) => {
    const out = {};
    const pick = (el) => {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
        w: Math.round(r.width),
        h: Math.round(r.height),
        x: Math.round(r.x),
        y: Math.round(r.y),
        bg: cs.backgroundColor,
        color: cs.color,
        font: cs.fontFamily,
        size: cs.fontSize,
        weight: cs.fontWeight,
        lh: cs.lineHeight,
        radius: cs.borderRadius,
        bw: cs.borderTopWidth,
        bc: cs.borderTopColor,
        pad: cs.padding,
        shadow: cs.boxShadow,
        display: cs.display,
      };
    };
    const one = (sel) => document.querySelector(sel);
    for (const [name, sel] of Object.entries(spec)) {
      out[name] = pick(one(sel));
    }
    return out;
  }, spec);
}

const HOME_SPEC = {
  masthead: 'ytd-masthead, #masthead',
  logo: 'ytd-topbar-logo-renderer, #logo',
  search: 'input#search, input[name="search_query"]',
  searchButton: '#search-icon-legacy, button#search-icon-legacy',
  signIn: 'a[aria-label="Sign in"], ytd-button-renderer a',
  guideMini: 'ytd-mini-guide-renderer, #guide',
  emptyTitle: 'ytd-feed-nudge-renderer h2, #primary h2',
  page: 'ytd-app, body',
};

async function openFresh(browser, viewport, dpr, ua) {
  const context = await browser.newContext({
    viewport,
    deviceScaleFactor: dpr,
    userAgent: ua,
    locale: 'en-US',
    colorScheme: 'dark',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(25000);
  return { context, page };
}

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_M = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1';

async function main() {
  const browser = await chromium.launch({ headless: true });
  const readings = { capturedAt: new Date().toISOString(), pages: {}, components: {} };
  try {
    const { context, page } = await openFresh(browser, { width: 1440, height: 900 }, 1, UA);
    log('home');
    await page.goto('https://www.youtube.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2500);
    await hideConsent(page);
    await shot(page, 'home-dark-empty', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.home = await readVars(page);
    readings.components.home = await measure(page, HOME_SPEC);

    log('guide');
    const guide = page.locator('button[aria-label="Guide"]').first();
    if (await guide.count()) {
      await guide.click();
      await wait(page, 800);
      await shot(page, 'home-dark-guide', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      readings.components.guide = await measure(page, {
        drawer: '#guide-content, ytd-app #guide',
        entry: 'ytd-guide-entry-renderer a',
        signIn: '#guide-content a[href*="ServiceLogin"]',
      });
      const expanded = await page.evaluate(() => {
        const more = [...document.querySelectorAll('#guide-content a')].find((a) => (a.innerText || '').trim() === 'Show more');
        if (!more) return false;
        more.click();
        return true;
      });
      if (expanded) {
        await wait(page, 600);
        await shot(page, 'home-dark-guide-more', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      }
    }

    log('settings');
    await page.keyboard.press('Escape').catch(() => {});
    await wait(page, 300);
    const settings = page.locator('button[aria-label="Settings"]').first();
    if (await settings.count()) {
      await settings.click();
      await wait(page, 700);
      await shot(page, 'home-dark-settings-menu', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      readings.components.settingsMenu = await page.evaluate(() => {
        const items = [...document.querySelectorAll('ytd-compact-link-renderer')].map((el) => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60));
        const el = document.querySelector('ytd-multi-page-menu-renderer') || document.querySelector('tp-yt-iron-dropdown');
        if (!el) return { items };
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return { items, bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, w: Math.round(r.width), h: Math.round(r.height), font: cs.fontFamily, size: cs.fontSize };
      });
      await page.keyboard.press('Escape').catch(() => {});
    }

    log('voice');
    const mic = page.locator('button[aria-label="Search with your voice"]').first();
    if (await mic.count()) {
      await mic.click();
      await wait(page, 700);
      await shot(page, 'home-dark-voice-dialog', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      await page.keyboard.press('Escape').catch(() => {});
      await wait(page, 300);
    }

    log('search focus');
    const search = page.locator('input#search, input[name="search_query"]').first();
    if (await search.count()) {
      await search.click();
      await wait(page, 500);
      await shot(page, 'home-dark-search-focused', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    }

    log('results');
    await page.goto('https://www.youtube.com/results?search_query=design+systems', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2500);
    await shot(page, 'search-dark-results', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.components.searchResult = await measure(page, {
      title: 'a#video-title',
      renderer: 'ytd-video-renderer',
      chip: 'yt-chip-cloud-chip-renderer',
    });
    const filters = page.locator('button[aria-label="Search filters"]').first();
    if (await filters.count()) {
      await filters.click();
      await wait(page, 700);
      await shot(page, 'search-dark-filters', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      readings.components.filters = await page.evaluate(() => {
        const el = document.querySelector('ytd-search-filter-options-dialog-renderer');
        if (!el) return null;
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return { bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, w: Math.round(r.width), h: Math.round(r.height), font: cs.fontFamily, size: cs.fontSize };
      });
      const cancel = page.getByRole('button', { name: 'Cancel' }).first();
      if (await cancel.count()) await cancel.click();
      else await page.keyboard.press('Escape');
      await wait(page, 400);
    }

    log('watch');
    await page.goto('https://www.youtube.com/watch?v=jNQXAC9IVRw', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 3000);
    await shot(page, 'watch-dark-default', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.watch = await readVars(page);
    readings.components.watch = await measure(page, {
      player: '#movie_player, .html5-video-player',
      title: 'h1 yt-formatted-string, ytd-watch-metadata h1',
      subscribe: 'ytd-subscribe-button-renderer',
      like: 'like-button-view-model button, ytd-toggle-button-renderer button',
      comments: 'ytd-comments#comments, #comments',
    });
    const save = page.locator('button[aria-label*="Save"]').first();
    if (await save.count()) {
      await save.click();
      await wait(page, 800);
      await shot(page, 'watch-dark-save-signin', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
      await page.keyboard.press('Escape').catch(() => {});
    }

    log('empty states');
    for (const [name, url] of [
      ['subscriptions-dark-empty', 'https://www.youtube.com/feed/subscriptions'],
      ['library-dark-empty', 'https://www.youtube.com/feed/you'],
      ['history-dark-empty', 'https://www.youtube.com/feed/history'],
    ]) {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(page, 1800);
      await shot(page, name, { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    }
    readings.components.empty = await measure(page, { prompt: 'ytd-browse ytd-message-renderer, #contents' });

    log('premium');
    await page.goto('https://www.youtube.com/premium', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2500);
    await shot(page, 'premium-dark-default', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.premium = await readVars(page);
    readings.components.premium = await measure(page, {
      heading: 'h1, ytd-upsell-dialog-renderer h1',
      cta: 'a[href*="ServiceLogin"], ytd-button-renderer a',
    });

    log('about');
    await page.goto('https://about.youtube/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2500);
    await shot(page, 'about-dark-default', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.about = await readVars(page);

    log('login');
    await page.goto('https://accounts.google.com/ServiceLogin?service=youtube&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2F', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2000);
    await shot(page, 'login-light-empty', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.login = await readVars(page);
    readings.components.login = await measure(page, {
      card: 'form, [data-form-action-uri]',
      heading: 'h1',
      field: 'input[type="email"], input[name="identifier"]',
      next: 'button[type="submit"], #identifierNext button',
    });

    log('signup');
    await page.goto('https://accounts.google.com/lifecycle/flows/signup?service=youtube&hl=en&flowName=GlifWebSignIn&flowEntry=SignUp', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 2500);
    await shot(page, 'signup-light-empty', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    readings.pages.signup = await readVars(page);
    readings.components.signup = await measure(page, {
      heading: 'h1',
      field: 'input[name="firstName"]',
      next: 'button',
    });

    await context.close();

    log('mobile');
    const mobile = await openFresh(browser, { width: 390, height: 844 }, 2, UA_M);
    await mobile.page.goto('https://www.youtube.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(mobile.page, 2500);
    await shot(mobile.page, 'mobile-home-dark-empty', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    readings.pages.mobileHome = await readVars(mobile.page);
    await mobile.page.goto('https://www.youtube.com/watch?v=jNQXAC9IVRw', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(mobile.page, 3000);
    await shot(mobile.page, 'mobile-watch-dark-default', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await mobile.page.goto('https://accounts.google.com/ServiceLogin?service=youtube&hl=en&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2F', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(mobile.page, 2000);
    await shot(mobile.page, 'mobile-login-light-empty', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await mobile.context.close();
  } finally {
    await browser.close();
  }
  fs.writeFileSync(path.join(RAW_JSON, 'public-readings.json'), JSON.stringify(readings, null, 2) + '\n');
  log('wrote', path.join(RAW_JSON, 'public-readings.json'));
  log('shots', fs.readdirSync(SHOTS).filter((n) => n.endsWith('.png')).length);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
