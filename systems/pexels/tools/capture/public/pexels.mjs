// Public capture of pexels.com. Adapted from tools/kit/capture/public/public.mjs.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node pexels.mjs [page,page,...]
//
// Uses the system Chrome channel. Bundled headless Chromium gets a Cloudflare
// challenge on every route after the homepage. Cookie banner is hidden, never
// clicked. No form is submitted. Login, join, Google and Apple are not clicked.
// A navigation that lands on /login/ or /join-contributor/ is recorded and the
// branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://www.pexels.com';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'pexels', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PHOTO = '/photo/icelandic-geothermal-landscape-with-mountains-32577944/';
const VIDEO = '/video/fresh-kumquats-in-wooden-bowl-indoors-39458084/';

async function hideCookies(p) {
  // Hide only. Never click Reject, Accept, Cookies Settings, or Google One Tap Continue.
  await p.evaluate(() => {
    const hide = (el) => el.style.setProperty('display', 'none', 'important');
    for (const el of document.querySelectorAll('div, section, aside, iframe, [role="dialog"]')) {
      const t = el.innerText || '';
      const s = getComputedStyle(el);
      const id = (el.id || '') + ' ' + (el.getAttribute('aria-label') || '');
      if ((s.position === 'fixed' || el.getAttribute('role') === 'dialog') && /cookie/i.test(t) && t.length < 1400) hide(el);
      if (/one.?tap|gsi|google/i.test(id) && (s.position === 'fixed' || el.tagName === 'IFRAME')) hide(el);
    }
    for (const el of document.querySelectorAll('iframe')) {
      const s = getComputedStyle(el);
      if (s.position === 'fixed') hide(el);
    }
  }).catch(() => {});
}

function isWall(url) {
  return /\/login\/|\/join-contributor\/|accounts\.google\.com|appleid\.apple\.com/i.test(url);
}

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
    const next = await p.evaluate(() => document.documentElement.scrollHeight);
    if (next > h + 400 && y > 2000) break; // infinite grid growing
    h = next;
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideCookies(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideCookies(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function openMore(p) {
  const box = await p.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => {
      const use = el.querySelector('use');
      const href = use ? (use.getAttribute('href') || use.getAttribute('xlink:href') || '') : '';
      const r = el.getBoundingClientRect();
      return href.includes('more-') && r.y < 90 && r.width < 60;
    });
    if (!b) return null;
    const r = b.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  if (!box) throw new Error('more button missing');
  await p.mouse.click(box.x, box.y);
  await wait(p, 700);
}

async function goto(p, urlPath) {
  const resp = await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 1800);
  const title = await p.title();
  if (/just a moment/i.test(title) || (resp && resp.status() === 403)) {
    throw new Error('cloudflare challenge on ' + urlPath);
  }
  if (isWall(p.url()) && !/login|join-contributor/.test(urlPath)) {
    log('  WALL', p.url());
    return 'wall';
  }
  await hideCookies(p);
  return resp && resp.status();
}

const desktop = {
  home: async (p, S) => {
    await goto(p, '/');
    await S.view('cookie');
    await hideCookies(p);
    await S.view('default');
    await step('search-focus', async () => {
      await p.locator('#search').click();
      await wait(p, 400);
      await S.view('search-focus');
      await p.locator('#search').fill('ocean');
      await wait(p, 900);
      await S.view('search-suggest');
      await p.locator('#search').fill('');
      await p.keyboard.press('Escape');
    });
    await step('type-menu', async () => {
      const b = p.getByRole('button', { name: 'Photos', exact: true }).first();
      await b.click();
      await wait(p, 500);
      await S.view('type-menu');
      await p.keyboard.press('Escape');
    });
    await step('more-menu', async () => {
      await openMore(p);
      await S.view('more-menu');
      await p.keyboard.press('Escape');
      await p.mouse.click(40, 500);
    });
    await step('join-dialog', async () => {
      await p.getByRole('button', { name: 'Join', exact: true }).first().click();
      await wait(p, 700);
      await S.view('join-dialog');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('trending-menu', async () => {
      await p.getByRole('button', { name: 'Trending', exact: true }).first().click();
      await wait(p, 500);
      await S.view('trending-menu');
      await p.keyboard.press('Escape');
    });
    await step('around-world', async () => {
      await p.getByRole('button', { name: /Around the world/ }).first().click();
      await wait(p, 700);
      await S.view('around-world');
      await p.keyboard.press('Escape');
    });
    await step('explore-hover', async () => {
      await p.getByRole('link', { name: 'Explore', exact: true }).first().hover();
      await wait(p, 600);
      await S.view('explore-hover');
      await p.mouse.move(20, 400);
    });
    await S.full();
  },
  search: async (p, S) => {
    await goto(p, '/search/ocean/');
    await S.view('default');
    await step('filters', async () => {
      const b = p.getByRole('button', { name: /Orientation|Horizontal|Filter/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('filter'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  },
  videos: async (p, S) => {
    await goto(p, '/videos/');
    await S.view('default');
    await S.full();
  },
  'search-videos': async (p, S) => {
    await goto(p, '/search/videos/ocean/');
    await S.view('default');
  },
  discover: async (p, S) => {
    await goto(p, '/discover/');
    await S.view('default');
    await S.full();
  },
  license: async (p, S) => {
    await goto(p, '/license/');
    await S.view('default');
    await S.full();
  },
  challenges: async (p, S) => {
    await goto(p, '/challenges/');
    await S.view('default');
    await S.full();
  },
  challenge: async (p, S) => {
    await goto(p, '/challenges/close-to-home/');
    await S.view('default');
  },
  leaderboard: async (p, S) => {
    await goto(p, '/leaderboard/');
    await S.view('default');
    await step('tabs', async () => {
      const tab = p.getByRole('button', { name: /Most Active/ }).first();
      if (await tab.count()) { await tab.click(); await wait(p, 600); await S.view('most-active'); }
    });
  },
  winners: async (p, S) => { await goto(p, '/winners-wall/'); await S.view('default'); },
  popular: async (p, S) => { await goto(p, '/popular-searches/'); await S.view('default'); await S.full(); },
  cookies: async (p, S) => { await goto(p, '/cookies/'); await S.view('default'); },
  api: async (p, S) => { await goto(p, '/api/'); await S.view('default'); },
  pro: async (p, S) => { await goto(p, '/pro/'); await S.view('default'); },
  imprint: async (p, S) => { await goto(p, '/imprint/'); await S.view('default'); },
  report: async (p, S) => { await goto(p, '/report/'); await S.view('default'); },
  partners: async (p, S) => { await goto(p, '/become-a-partner/'); await S.view('default'); },
  about: async (p, S) => { await goto(p, '/about/'); await S.view('default'); },
  hero: async (p, S) => { await goto(p, '/hero/'); await S.view('default'); },
  levelup: async (p, S) => { await goto(p, '/the-level-up/'); await S.view('default'); },
  photo: async (p, S) => {
    await goto(p, PHOTO);
    await S.view('default');
    await step('download-menu', async () => {
      // The Free download control is a split button. The chevron sits in the green group, not the search type menu.
      const opened = await p.evaluate(() => {
        const label = [...document.querySelectorAll('a, button, span')].find((el) => (el.innerText || '').trim() === 'Free download');
        const group = label && label.closest('div');
        const btn = group && [...group.querySelectorAll('button')].find((b) => b.getBoundingClientRect().width < 48);
        if (!btn) return null;
        const r = btn.getBoundingClientRect();
        return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
      });
      if (!opened) throw new Error('download chevron missing');
      await p.mouse.click(opened.x, opened.y);
      await wait(p, 600);
      await S.view('download-menu');
      await p.keyboard.press('Escape');
    });
  },
  video: async (p, S) => { await goto(p, VIDEO); await S.view('default'); },
  missing: async (p, S) => { await goto(p, '/this-page-does-not-exist-capture/'); await S.view('default'); },
  login: async (p, S) => {
    // Record the wall. Do not type, do not click Google.
    await goto(p, '/login/');
    await hideCookies(p);
    await S.view('wall');
  },
};

const mobile = {
  home: async (p, S) => {
    await goto(p, '/');
    await S.view('cookie');
    await hideCookies(p);
    await S.view('default');
    await step('menu', async () => {
      await openMore(p);
      await S.view('more-menu');
      await p.keyboard.press('Escape');
    });
    await S.full();
  },
  search: async (p, S) => { await goto(p, '/search/ocean/'); await S.view('default'); },
  videos: async (p, S) => { await goto(p, '/videos/'); await S.view('default'); },
  photo: async (p, S) => { await goto(p, PHOTO); await S.view('default'); },
  license: async (p, S) => { await goto(p, '/license/'); await S.view('default'); },
  discover: async (p, S) => { await goto(p, '/discover/'); await S.view('default'); },
  challenges: async (p, S) => { await goto(p, '/challenges/'); await S.view('default'); },
  login: async (p, S) => { await goto(p, '/login/'); await hideCookies(p); await S.view('wall'); },
  missing: async (p, S) => { await goto(p, '/this-page-does-not-exist-capture/'); await S.view('default'); },
};

const browser = await chromium.launch({ channel: 'chrome', headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await (mob ? mobile : desktop)[k](p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
