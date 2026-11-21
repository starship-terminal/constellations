// Walks the public Fourthwall marketing site and writes a control map plus
// viewport screenshots. Nothing is typed, submitted, or signed into.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/walk.mjs
//
// Writes ~/.design-systems/fourthwall/walk/ (raw shots + walk.json).
// Cookie banners are photographed, then hidden. They are never accepted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = process.env.WALK || path.join(os.homedir(), '.design-systems', 'fourthwall', 'walk');
fs.mkdirSync(OUT, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const SITEMAP = '/tmp/fw-probe/sitemap-urls.txt';

function slugify(urlPath) {
  const s = (urlPath || '/').replace(/^\//, '').replace(/\/$/, '') || 'home';
  return s.replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').slice(0, 80);
}

function pickSamples(urls) {
  const paths = urls.map((u) => u.replace(/^https?:\/\/[^/]+/, '').replace(/\/$/, '') || '/');
  const set = new Set(paths);
  const samples = [];
  const add = (p, why) => {
    if (!p) return;
    samples.push({ path: p, why });
  };
  // Unique marketing, legal, feature and audience pages: photograph all of them.
  const templates = ['/make-your-own/', '/blog/', '/design-and-sell/', '/compare/', '/apps/', '/creator-examples/', '/seasons/', '/categoryx/', '/glossary'];
  for (const p of [...set].sort()) {
    const templated = templates.some((t) => p.startsWith(t) && p !== t.replace(/\/$/, ''));
    if (templated) continue;
    if (p.split('/').length > 4 && p.startsWith('/features/apps')) continue;
    add(p, 'unique public page');
  }
  // One of each generated template, plus an index if the prefix itself is a page.
  const oneOf = {
    '/make-your-own': 'generated product landing template',
    '/blog': 'blog index plus one post',
    '/design-and-sell': 'product-category landing template',
    '/compare': 'comparison landing template',
    '/apps': 'app detail template',
    '/creator-examples': 'creator-example category template',
    '/seasons': 'seasonal campaign template',
    '/categoryx': 'blog category template',
    '/features/apps-and-integrations': 'integration detail template',
    '/glossary': 'glossary index',
    '/bespoke': 'bespoke partner template',
  };
  for (const [prefix, why] of Object.entries(oneOf)) {
    const kids = [...set].filter((p) => p.startsWith(prefix + '/') || p === prefix).sort();
    if (!kids.length) continue;
    add(kids[0], why + ' (first)');
    if (kids.length > 2) add(kids[Math.floor(kids.length / 2)], why + ' (middle)');
    if (kids.length > 1) add(kids[kids.length - 1], why + ' (last)');
  }
  // Pages linked from the homepage that the sitemap may omit.
  for (const p of ['/get-started', '/login', '/design-community/all-designers', '/admin/products/custom-shape-sterling-silver-necklace']) {
    add(p, 'linked from a public page, not necessarily in the sitemap');
  }
  const seen = new Set();
  return samples.filter((s) => (seen.has(s.path) ? false : (seen.add(s.path), true)));
}

const HIDE_CSS = `
  #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
  [id*="cookie-banner"], [class*="cookie-banner"], [id*="cookieBanner"],
  [class*="cookie-consent"], [id*="consent-banner"],
  iframe[src*="consent"], iframe[title*="cookie" i] { display: none !important; visibility: hidden !important; }
`;

async function hideBanners(page) {
  await page.addStyleTag({ content: HIDE_CSS }).catch(() => {});
  await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('div, aside, section')].filter((n) => {
      const t = (n.innerText || '').slice(0, 400);
      const r = n.getBoundingClientRect();
      return /cookie|consent|privacy choices/i.test(t) && r.height > 40 && r.height < 500 && r.width > 200
        && (n.id || '').toLowerCase().match(/cookie|consent|onetrust/) || (String(n.className).toLowerCase().match(/cookie|consent|onetrust/));
    });
    for (const n of nodes) n.style.setProperty('display', 'none', 'important');
  }).catch(() => {});
}

async function controls(page) {
  return page.evaluate(() => {
    function clean(s) {
      return (s || '').replace(/\s+/g, ' ').trim().slice(0, 140);
    }
    function row(el) {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      const visible = r.width > 1 && r.height > 1 && s.visibility !== 'hidden' && s.display !== 'none' && Number(s.opacity) > 0.05;
      const a = el.tagName === 'A' ? el : el.closest('a');
      let href = el.getAttribute('href') || (a ? a.getAttribute('href') : null);
      let abs = null;
      try { abs = a ? a.href : (el.href || null); } catch { abs = null; }
      return {
        tag: el.tagName,
        role: el.getAttribute('role'),
        text: clean(el.getAttribute('aria-label') || el.innerText || el.textContent),
        href,
        abs,
        expanded: el.getAttribute('aria-expanded'),
        haspopup: el.getAttribute('aria-haspopup'),
        controls: el.getAttribute('aria-controls'),
        type: el.getAttribute('type'),
        name: el.getAttribute('name'),
        class: String(el.className || '').slice(0, 80),
        visible,
        region: el.closest('footer') ? 'footer' : el.closest('.nav-bar, header, nav') ? 'header' : 'page',
      };
    }
    const nodes = [...document.querySelectorAll('a[href], button, [role="button"], summary, [aria-haspopup], input, select, textarea')];
    return nodes.slice(0, 800).map(row);
  });
}

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, { ...requested, sanitizedSourceUrl: null });
}

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

async function main() {
  const sitemap = fs.existsSync(SITEMAP) ? fs.readFileSync(SITEMAP, 'utf8').split('\n').filter(Boolean) : [];
  const samples = pickSamples(sitemap);
  log('samples', samples.length, 'of', sitemap.length);
  fs.writeFileSync(path.join(OUT, 'samples.json'), JSON.stringify(samples, null, 2));

  const browser = await chromium.launch({ headless: true });
  const walk = { capturedAt: new Date().toISOString(), signed_in: false, pages: [], menus: [], auth: [], blocked: [] };

  async function contextFor(mobile) {
    const context = await browser.newContext(mobile
      ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-US' }
      : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
    await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    await context.route(/onetrust|cookielaw|cookiebot|consent\.cookie/i, (route) => route.abort());
    return context;
  }

  const widths = [
    { mobile: false, prefix: '', vw: 1440, vh: 900, dpr: 1 },
    { mobile: true, prefix: 'mobile-', vw: 390, vh: 844, dpr: 2 },
  ];

  for (const w of widths) {
    const context = await contextFor(w.mobile);
    const page = await context.newPage();
    page.setDefaultTimeout(20000);
    const requested = { viewport: { width: w.vw, height: w.vh }, deviceScaleFactor: w.dpr };

    for (const sample of samples) {
      const url = sample.path.startsWith('http') ? sample.path : 'https://fourthwall.com' + (sample.path.startsWith('/') ? sample.path : '/' + sample.path);
      const name = w.prefix + slugify(sample.path);
      const row = { path: sample.path, why: sample.why, width: w.vw, url, final: null, status: null, title: null, challenge: false, authWall: false, controls: null, shots: [] };
      try {
        const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 35000 });
        await page.waitForTimeout(1400);
        row.status = resp ? resp.status() : null;
        row.final = page.url();
        row.title = await page.title();
        const body = await page.evaluate(() => (document.body?.innerText || '').slice(0, 500));
        row.challenge = /verify you are human|just a moment|cf-challenge|attention required|performing security verification/i.test(body);
        const host = (() => { try { return new URL(row.final).hostname; } catch { return ''; } })();
        row.authWall = /auth\.fourthwall\.com|accounts\.google|appleid\.apple|keycloak/i.test(row.final) || /\/login|\/register|\/get-started/.test(sample.path);
        if (row.challenge) {
          walk.blocked.push({ url, final: row.final, why: 'human-check or bot wall before paint', snippet: body.replace(/\s+/g, ' ').slice(0, 180) });
          log('BLOCKED', sample.path);
          walk.pages.push(row);
          continue;
        }
        // Photograph a cookie banner if one is actually visible, then hide it.
        const banner = await page.evaluate(() => {
          const n = document.querySelector('#onetrust-banner-sdk, [id*="cookie-banner"], [class*="cookie-banner"]');
          if (!n) return null;
          const r = n.getBoundingClientRect();
          return r.height > 20 ? (n.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 160) : null;
        });
        if (banner && !w.mobile) {
          const bfile = path.join(OUT, `${name}-cookie.png`);
          await shot(page, bfile, requested);
          row.shots.push(path.basename(bfile));
          row.cookieBanner = banner;
        }
        await hideBanners(page);
        const vfile = path.join(OUT, `${name}-default.png`);
        await shot(page, vfile, requested);
        row.shots.push(path.basename(vfile));
        row.controls = await controls(page);
        if (row.authWall || host.includes('auth.fourthwall')) {
          walk.auth.push({
            from: url,
            finalHost: host,
            finalPath: (() => { try { return new URL(row.final).pathname; } catch { return row.final; } })(),
            title: row.title,
            asks: await page.evaluate(() => {
              const fields = [...document.querySelectorAll('input, button, a')].slice(0, 40).map((el) => ({
                tag: el.tagName,
                type: el.getAttribute('type'),
                name: el.getAttribute('name'),
                id: el.id,
                text: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('value') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
                hrefHost: el.tagName === 'A' ? (() => { try { return new URL(el.href).hostname; } catch { return null; } })() : null,
              }));
              return { fields, text: (document.body?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 500) };
            }),
          });
          log('AUTH', sample.path, '->', host);
          walk.pages.push(row);
          continue;
        }
        log(row.status, w.vw, sample.path, row.title?.slice(0, 48));
      } catch (e) {
        row.error = String(e.message || e).split('\n')[0].slice(0, 180);
        log('FAIL', sample.path, row.error);
      }
      walk.pages.push(row);
      if (walk.pages.length % 8 === 0) fs.writeFileSync(path.join(OUT, 'walk.json'), JSON.stringify(walk));
    }

    // Menus, search, burger: only on the home page, after the page loop so a
    // late navigation cannot wipe the rest of the walk.
    if (!w.mobile) {
      try {
        await page.goto('https://fourthwall.com/', { waitUntil: 'domcontentloaded', timeout: 35000 });
        await page.waitForTimeout(1200);
        await hideBanners(page);
        for (const label of ['Features', 'Learn']) {
          await page.locator('.nav-link', { hasText: label }).first().hover();
          await page.waitForTimeout(500);
          const file = path.join(OUT, `home-menu-${label.toLowerCase()}.png`);
          await shot(page, file, requested);
          const items = await page.evaluate((label) => {
            const el = [...document.querySelectorAll('.nav-link')].find((a) => (a.innerText || '').trim() === label);
            const dd = el && el.closest('.nav-dropdown');
            if (!dd) return [];
            return [...dd.querySelectorAll('a')].map((a) => ({
              text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 120),
              href: a.getAttribute('href'),
            }));
          }, label);
          walk.menus.push({ label, width: 1440, shot: path.basename(file), items });
          log('menu', label, items.length);
          await page.mouse.move(10, 860);
          await page.waitForTimeout(250);
        }
        const search = page.locator('a[href="/search"], a[href="https://fourthwall.com/search"], [aria-label*="Search" i], button[aria-label*="Search" i]').first();
        if (await search.count()) {
          await search.click({ timeout: 4000 }).catch(() => {});
          await page.waitForTimeout(800);
          const file = path.join(OUT, 'home-search.png');
          await shot(page, file, requested);
          walk.menus.push({ label: 'search', width: 1440, shot: path.basename(file), final: page.url().split('?')[0] });
        }
      } catch (e) {
        log('menu fail', String(e.message || e).split('\n')[0]);
      }
    } else {
      try {
        await page.goto('https://fourthwall.com/', { waitUntil: 'domcontentloaded', timeout: 35000 });
        await page.waitForTimeout(1200);
        await hideBanners(page);
        const burger = page.locator('.nav-burger').first();
        if (await burger.count()) {
          await burger.click();
          await page.waitForTimeout(700);
          const file = path.join(OUT, 'mobile-home-menu.png');
          await shot(page, file, requested);
          const items = await page.evaluate(() => [...document.querySelectorAll('.nav-menu a, .nav-menu button')].map((el) => ({
            tag: el.tagName,
            text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100),
            href: el.getAttribute('href'),
            expanded: el.getAttribute('aria-expanded'),
          })));
          walk.menus.push({ label: 'mobile-burger', width: 390, shot: path.basename(file), items });
          log('burger', items.length);
        }
      } catch (e) {
        log('burger fail', String(e.message || e).split('\n')[0]);
      }
    }
    await context.close();
  }

  fs.writeFileSync(path.join(OUT, 'walk.json'), JSON.stringify(walk));
  log('done pages', walk.pages.length, 'auth', walk.auth.length, 'blocked', walk.blocked.length);
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
