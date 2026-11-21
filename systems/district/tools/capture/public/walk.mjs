// Map the public District site and photograph distinct pages and interactions.
// Signed-out only. Never submits a form, never types a phone number or code,
// never clicks an app-download control, never follows SSO.
//
//   PLAYWRIGHT=... node walk.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const BASE = 'https://www.district.in';
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'district', 'raw-shots');
const OUT = process.env.OUT || path.join(os.homedir(), '.design-systems', 'district');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const tree = [];
const notes = [];

function note(s) { notes.push(s); log('  note', s); }

function safePath(url) {
  try {
    const u = new URL(url, BASE);
    u.search = '';
    u.hash = '';
    return u.pathname.replace(/\/$/, '') || '/';
  } catch {
    return url;
  }
}

async function shot(page, name, requested) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', name);
  return name;
}

async function dismissOverlay(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(250);
}

async function pageMeta(page) {
  return page.evaluate(() => {
    const text = (el) => (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 100);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 1 && r.height > 1 && s.visibility !== 'hidden' && s.display !== 'none';
    };
    const controls = [...document.querySelectorAll('a, button, [role="tab"], summary, input, select')].filter(vis).slice(0, 80).map((el) => ({
      tag: el.tagName,
      role: el.getAttribute('role'),
      href: el.getAttribute('href'),
      text: text(el),
      aria: el.getAttribute('aria-label'),
      expanded: el.getAttribute('aria-expanded'),
      type: el.getAttribute('type') || el.type || null,
    }));
    const headings = [...document.querySelectorAll('h1,h2')].slice(0, 8).map((h) => (h.innerText || '').trim().slice(0, 80));
    return {
      title: document.title,
      headings,
      controls,
      body: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 280),
    };
  });
}

const PAGES = [
  { id: 'home', path: '/' },
  { id: 'events', path: '/events/' },
  { id: 'movies', path: '/movies/' },
  { id: 'dining', path: '/dining/' },
  { id: 'play', path: '/play/' },
  { id: 'activities', path: '/activities/' },
  { id: 'stores', path: '/stores/' },
  { id: 'events-comedy', path: '/events/comedy' },
  { id: 'artist', path: '/events/sonu-nigam/artist' },
  { id: 'event', path: '/events/unifyd-music-festival-buy-tickets' },
  { id: 'movie', path: '/movies/ramayana-movie-tickets-MV176276' },
  { id: 'restaurant', path: '/dining/singapore/the-palace-korean-restaurant-downtown-core' },
  { id: 'venue', path: '/venue/metcalfe-hall' },
  { id: 'contact', path: '/contact' },
  { id: 'corporate', path: '/corporate-announcements' },
  { id: 'list-event', path: '/events/list-your-event' },
  { id: 'policies', path: '/policies/' },
  { id: 'terms', path: '/policies/terms-of-service' },
  { id: 'privacy', path: '/policies/privacy' },
  { id: 'login-url', path: '/login', expectMissing: true },
];

async function captureWidth(label, mobile) {
  const browser = await chromium.launch({ headless: true });
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const context = await browser.newContext(mobile
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-IN' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-IN' });
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const prefix = mobile ? 'mobile-' : '';

  for (const spec of PAGES) {
    const url = BASE + spec.path;
    log('\n==', prefix + spec.id, url);
    let status = null;
    try {
      const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      status = resp && resp.status();
      await page.waitForTimeout(2200);
    } catch (e) {
      note(`${prefix}${spec.id} failed to load: ${String(e.message).split('\n')[0]}`);
      tree.push({ id: spec.id, path: spec.path, width: vw, status: 'load-failed', error: String(e.message).split('\n')[0] });
      continue;
    }
    const final = page.url();
    const meta = await pageMeta(page).catch(() => ({}));
    const missing = /couldn't find|page was not found|not found/i.test(meta.body || '') || status === 404;
    const row = {
      id: spec.id,
      path: spec.path,
      width: vw,
      status,
      final: safePath(final),
      title: meta.title,
      headings: meta.headings,
      missing,
      shot: null,
    };
    if (!missing) {
      row.shot = await shot(page, `${prefix}${spec.id}-light-default`, requested);
    } else {
      if (vw === 1440) row.shot = await shot(page, `${prefix}${spec.id}-light-missing`, requested);
      note(`${spec.path} is a missing page (${status}) at ${vw}`);
    }
    if (vw === 1440) {
      row.controls = (meta.controls || []).map((c) => ({
        tag: c.tag,
        text: c.text,
        aria: c.aria,
        href: c.href,
        expanded: c.expanded,
        type: c.type,
      }));
    }
    tree.push(row);
    if (missing) continue;

    // Interactions only on desktop, and only the ones that do not submit or download.
    if (!mobile && spec.id === 'home') {
      await page.getByRole('button').filter({ hasText: /Singapore|location/i }).first().click().catch(() => {});
      await page.waitForTimeout(900);
      const locOpen = await page.locator('[role="dialog"]').count();
      if (locOpen) {
        await shot(page, 'home-light-location', requested);
        tree.push({ id: 'home-location', from: 'home location button', opens: 'in-page dialog Select Location', shot: 'home-light-location', width: vw });
      }
      await dismissOverlay(page);

      await page.getByRole('button', { name: 'All', exact: true }).click().catch(() => {});
      await page.waitForTimeout(500);
      if (await page.locator('[role="listbox"]').count()) {
        await shot(page, 'home-light-search-scope', requested);
        tree.push({ id: 'home-search-scope', from: 'search scope button All', opens: 'listbox Select tab: All, Events', shot: 'home-light-search-scope', width: vw });
      }
      await dismissOverlay(page);

      await page.getByRole('button', { name: 'Open search' }).click().catch(() => {});
      await page.waitForTimeout(800);
      if (await page.locator('#search-results-panel, [role="listbox"]').count()) {
        await shot(page, 'home-light-search', requested);
        tree.push({ id: 'home-search', from: 'Open search', opens: 'search results listbox (trending). Typed query not submitted.', shot: 'home-light-search', width: vw });
      }
      await dismissOverlay(page);

      await page.getByRole('button', { name: 'Login' }).click().catch(() => {});
      await page.waitForTimeout(1200);
      const loginText = await page.evaluate(() => {
        const d = document.querySelector('[role="dialog"]');
        return d ? (d.innerText || '').replace(/\s+/g, ' ').slice(0, 180) : '';
      });
      if (/log in|sign up|otp|mobile/i.test(loginText)) {
        await shot(page, 'home-light-login-wall', requested);
        tree.push({
          id: 'login-wall',
          from: 'header Login button',
          opens: 'in-page dialog: Log in or sign up (phone OTP). Branch stopped. Form not filled.',
          url: page.url(),
          shot: 'home-light-login-wall',
          width: vw,
        });
        note('login wall is an in-page dialog, not /login. Stopped that branch.');
      }
      await dismissOverlay(page);
    }

    if (!mobile && spec.id === 'events') {
      await page.getByRole('button', { name: 'Filters', exact: true }).click().catch(() => {});
      await page.waitForTimeout(800);
      if (await page.locator('[role="dialog"]').count()) {
        await shot(page, 'events-light-filters', requested);
        tree.push({ id: 'events-filters', from: 'Events Filters button', opens: 'Filter by dialog (sort, genre). Apply not pressed.', shot: 'events-light-filters', width: vw });
      }
      await dismissOverlay(page);
    }

    if (!mobile && spec.id === 'event') {
      const gallery = page.getByRole('button', { name: 'View image' }).first();
      if (await gallery.count()) {
        await gallery.click().catch(() => {});
        await page.waitForTimeout(800);
        await shot(page, 'event-light-gallery', requested);
        tree.push({ id: 'event-gallery', from: 'View image', opens: 'image viewer. Closed without booking.', shot: 'event-light-gallery', width: vw });
        await dismissOverlay(page);
      }
    }

    if (!mobile && spec.id === 'movie') {
      const faq = page.getByRole('button', { name: /When was/ }).first();
      if (await faq.count()) {
        await faq.scrollIntoViewIfNeeded().catch(() => {});
        await faq.click().catch(() => {});
        await page.waitForTimeout(600);
        await shot(page, 'movie-light-faq', requested);
        tree.push({ id: 'movie-faq', from: 'movie FAQ button', opens: 'accordion answer in page', shot: 'movie-light-faq', width: vw });
      }
    }

    if (!mobile && spec.id === 'policies') {
      const movies = page.getByRole('button', { name: 'Movies', exact: true }).first();
      if (await movies.count()) {
        await movies.click().catch(() => {});
        await page.waitForTimeout(500);
        await shot(page, 'policies-light-nav-open', requested);
        tree.push({ id: 'policies-nav', from: 'policies sidebar Movies', opens: 'expanded nav group', shot: 'policies-light-nav-open', width: vw });
      }
    }
  }

  if (mobile) {
    await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(2000);
    const menu = page.getByRole('button', { name: /menu|open navigation/i }).first();
    if (await menu.count()) {
      await menu.click().catch(() => {});
      await page.waitForTimeout(700);
      await shot(page, 'mobile-home-light-menu', requested);
      tree.push({ id: 'mobile-menu', from: 'phone menu button', opens: 'navigation drawer', shot: 'mobile-home-light-menu', width: 390 });
    } else {
      note('phone home has no separate menu button; primary nav stays in the header');
    }
    await page.getByRole('button', { name: 'Login' }).click().catch(() => {});
    await page.waitForTimeout(1000);
    const loginText = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]');
      return d ? (d.innerText || '').replace(/\s+/g, ' ').slice(0, 120) : '';
    });
    if (/log in|sign up|otp|mobile/i.test(loginText)) {
      await shot(page, 'mobile-home-light-login-wall', requested);
      tree.push({ id: 'mobile-login-wall', from: 'phone Login', opens: 'same OTP dialog. Branch stopped.', shot: 'mobile-home-light-login-wall', width: 390 });
    }
  }

  await browser.close();
}

await captureWidth('desktop', false);
await captureWidth('phone', true);

fs.writeFileSync(path.join(OUT, 'tree.json'), JSON.stringify({ tree, notes, capturedAt: new Date().toISOString() }, null, 2));
log('\nwrote', path.join(OUT, 'tree.json'), 'rows', tree.length);
