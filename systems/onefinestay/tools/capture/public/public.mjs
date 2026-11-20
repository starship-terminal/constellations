// Captures onefinestay.com public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// Desktop 1440x900 at 1x. Phone 390x844 at 2x.
// Cookie banner is not accepted. Login, signup, and forgot-password are
// recorded as walls and not filled. No form is submitted. No email, phone,
// or location is typed. A fresh browser context per route avoids the
// security-verification interstitial that same-context navigation hits.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { launch, isChallenge, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'onefinestay', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

// Remove-only. Hides the OneTrust banner so menus and pickers can be shot.
// Does not click Accept, Continue, or Confirm. Call only after the cookie shot.
async function hideCookie(p) {
  await p.evaluate(() => {
    const sdk = document.getElementById('onetrust-consent-sdk');
    if (sdk) sdk.style.setProperty('display', 'none', 'important');
    document.body.style.overflow = 'auto';
    document.documentElement.style.overflow = 'auto';
  });
}

async function openMenu(p, label) {
  const loc = p.locator(`a[aria-label="${label}"]`).first();
  await loc.click({ force: true, timeout: 8000 });
  await wait(p, 700);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('cookie');
    await hideCookie(p);
    await S.view('default');
    await step('destinations', async () => {
      await openMenu(p, 'Destinations');
      await S.view('destinations');
      await p.keyboard.press('Escape');
      await p.mouse.click(40, 800);
      await wait(p, 400);
    });
    await step('inspiration', async () => {
      await openMenu(p, 'Inspiration');
      await S.view('inspiration');
      await p.keyboard.press('Escape');
      await p.mouse.click(40, 800);
      await wait(p, 400);
    });
    await step('account', async () => {
      await p.locator('button[aria-label="Login or Sign up menu"]').first().click({ force: true });
      await wait(p, 700);
      await S.view('account-wall');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('dates', async () => {
      await p.getByText('Dates', { exact: true }).first().click({ force: true });
      await wait(p, 700);
      await S.view('dates');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('guests', async () => {
      await p.getByText('Guests', { exact: true }).first().click({ force: true });
      await wait(p, 600);
      await S.view('guests');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  destination: { path: '/destination/london', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /Can I cancel/i }).first();
      if (await b.count()) { await b.click({ force: true }); await wait(p, 500); await S.view('faq'); }
    });
    await S.full();
  } },
  search: { path: '/search/london/500', run: async (p, S) => {
    await S.view('default');
    await step('filters', async () => {
      const b = p.getByRole('button', { name: 'Filters' }).first();
      if (await b.count()) { await b.click({ force: true }); await wait(p, 700); await S.view('filters'); await p.keyboard.press('Escape'); }
    });
    await step('sort', async () => {
      const b = p.getByRole('button', { name: /Sort by/i }).first();
      if (await b.count()) { await b.click({ force: true }); await wait(p, 500); await S.view('sort'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  listing: { path: '/home-listing/cadogan-street-iv-cad126', run: async (p, S) => {
    await S.view('default');
    await step('gallery', async () => {
      const b = p.getByRole('button', { name: /View all/i }).first();
      if (await b.count()) { await b.click({ force: true }); await wait(p, 900); await S.view('gallery'); await p.keyboard.press('Escape'); await wait(p, 400); }
    });
    await S.full();
  } },
  enquire: { path: '/enquire', run: async (p, S) => { await S.view('default'); await S.full(); } },
  wishlist: { path: '/wishlist', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'list-your-home': { path: '/list-your-home', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /What happens when there is a guest booking/i }).first();
      if (await b.count()) { await b.click({ force: true }); await wait(p, 500); await S.view('faq'); }
    });
    await S.full();
  } },
  journal: { path: '/journal', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  services: { path: '/onefinestay-services', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { path: '/reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact-us', run: async (p, S) => { await S.view('default'); await S.full(); } },
  promo: { path: '/black-friday-weekend', run: async (p, S) => { await S.view('default'); await S.full(); } },
  collection: { path: '/villa-collection', run: async (p, S) => { await S.view('default'); await S.full(); } },
  category: { path: '/c/beachfront-vacation-rentals', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  team: { path: '/team', run: async (p, S) => { await S.view('default'); } },
  accessibility: { path: '/website-accessibility', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('wall'); } },
  signup: { path: '/signup', run: async (p, S) => { await S.view('wall'); } },
  'forgot-password': { path: '/forgot-password', run: async (p, S) => { await S.view('wall'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('cookie');
    await hideCookie(p);
    await S.view('default');
    await step('menu', async () => {
      await p.locator('button[aria-label="Open menu"]').first().click({ force: true });
      await wait(p, 700);
      await S.view('menu');
      await p.locator('button[aria-label="Close menu"]').first().click({ force: true }).catch(() => {});
      await wait(p, 300);
    });
    await S.full();
  } },
  destination: { path: '/destination/london', run: async (p, S) => { await S.view('default'); await S.full(); } },
  search: { path: '/search/london/500', run: async (p, S) => { await S.view('default'); await S.full(); } },
  listing: { path: '/home-listing/cadogan-street-iv-cad126', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enquire: { path: '/enquire', run: async (p, S) => { await S.view('default'); } },
  wishlist: { path: '/wishlist', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  journal: { path: '/journal', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('wall'); } },
};

const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];

let total = 0;
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  log(name, spec.path);
  const { browser, context } = await launch({ width: vw, height: vh, mobile: mob });
  const p = await context.newPage();
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 2800);
    const blocked = await isChallenge(p);
    log('  status', res && res.status(), blocked ? 'CHALLENGE' : 'ok', await p.title());
    if (!blocked) {
      // Homepage shots the banner first, then hides it inside the page run.
      // Every other page hides the banner before the default shot. The banner
      // itself is recorded on home-light-cookie and mobile-home-light-cookie.
      // Hiding is remove-only: Accept, Continue, and Confirm are never clicked.
      // Homepage runs shoot the banner, then hide it. Other pages hide first.
      if (spec.path !== '/') await hideCookie(p);
      await spec.run(p, S);
    }
    else log('  skipped: security verification');
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await context.close();
  await browser.close();
}
log('done', total, 'screenshots ->', RAW);
log('package', PKG);
