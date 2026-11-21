// Captures Rivian's public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile names get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full-page shots are 1x
// on desktop and 2x on phone, capped at 8 chunks.
//
// Nothing is submitted. Cookie Reject All is clicked when it is in the
// viewport; otherwise the banner shell is hidden. Sign-in is not opened.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, dismissConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'rivian', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const WALL = /\/auth\/|\/login|\/signup|\/sign-up|\/register/i;

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 14000 * 8));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.count = 0;
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: source,
    };
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    // Playwright fullPage captures the document. A clip on fullPage is still
    // checked against document size, so tall pages are stitched from viewport
    // screenshots taken while scrolled.
    if (hCap <= this.requested.viewport.height + 40) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      const vh = this.requested.viewport.height;
      for (let i = 0, y = 0; y < hCap; i++, y += vh) {
        await p.evaluate((yy) => scrollTo(0, yy), y);
        await wait(p, 200);
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png` }, this.requested);
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

async function openNav(p, name) {
  await p.keyboard.press('Escape').catch(() => {});
  const btn = p.locator('header button, nav button').filter({ hasText: new RegExp('^' + name + '$') }).first();
  await btn.click({ timeout: 5000 });
  await wait(p, 700);
}

async function openMobilePanel(p) {
  const btn = p.locator('#navbar-trigger-accordion, button[aria-label="Open"]').first();
  await btn.click({ timeout: 5000 });
  await wait(p, 800);
}

const PAGES = {
  home: '/',
  r1s: '/r1s',
  r1t: '/r1t',
  r2: '/r2',
  r3: '/r3',
  'r1s-tri': '/r1s-tri',
  'r1t-tri': '/r1t-tri',
  compare: '/compare',
  offers: '/offers',
  technology: '/technology',
  autonomy: '/autonomy',
  'connect-plus': '/connect-plus',
  charging: '/experience/charging',
  purchasing: '/experience/purchasing',
  insurance: '/experience/insurance',
  service: '/experience/service',
  'pre-owned': '/experience/pre-owned',
  fleet: '/fleet',
  spaces: '/spaces',
  // A single space page and the locations index list street addresses.
  // Those branches are recorded in site-tree.md and not captured.
  company: '/our-company',
  impact: '/scaling-responsibly',
  investors: '/investors',
  stories: '/stories',
  newsroom: '/newsroom',
  support: '/support',
  financing: '/support/financing-and-payments',
  recalls: '/support/article/recall-information',
  privacy: '/privacy',
  'privacy-notice': '/privacy/notice',
  legal: '/legal',
  terms: '/legal/terms',
  accessibility: '/accessibility',
  'gear-shop': '/gear-shop',
  'gear-wheels': '/gear-shop/c/wheels-and-tires',
  'gear-adventure': '/gear-shop/c/adventure-gear',
  'gear-charging': '/gear-shop/c/charging',
  'gear-lifestyle': '/gear-shop/c/lifestyle',
  inventory: '/configurations/list',
  'demo-drive': '/demo-drive',
  event: '/events/autonomy-and-ai-day',
  careers: '/careers',
};

const desktop = {
  ...Object.fromEntries(Object.keys(PAGES).map((k) => [k, { path: PAGES[k] }])),
};

const interactions = {
  home: async (p, S) => {
    await S.view('default');
    await step('vehicles-menu', async () => { await openNav(p, 'Vehicles'); await S.view('vehicles-menu'); await p.keyboard.press('Escape'); });
    await step('charging-menu', async () => { await openNav(p, 'Charging'); await S.view('charging-menu'); await p.keyboard.press('Escape'); });
    await step('technology-menu', async () => { await openNav(p, 'Technology'); await S.view('technology-menu'); await p.keyboard.press('Escape'); });
    await step('discover-menu', async () => { await openNav(p, 'Discover'); await S.view('discover-menu'); await p.keyboard.press('Escape'); });
    await step('gear-menu', async () => { await openNav(p, 'Gear Shop'); await S.view('gear-menu'); await p.keyboard.press('Escape'); });
    await step('question', async () => {
      await p.getByRole('button', { name: 'Have a question?' }).first().click({ timeout: 5000 });
      await wait(p, 1500);
      await S.view('question');
      await p.keyboard.press('Escape');
    });
    await step('video', async () => {
      const b = p.getByRole('button', { name: 'Watch the video' }).first();
      if (await b.count()) { await b.click({ timeout: 4000 }); await wait(p, 1200); await S.view('video'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  },
};

const mobileInteractions = {
  home: async (p, S) => {
    await S.view('default');
    await step('menu', async () => { await openMobilePanel(p); await S.view('menu'); await p.keyboard.press('Escape'); });
    await S.full();
  },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const keys = Object.keys(PAGES);
const runs = [
  ...keys.map((k) => ({ k, mob: false })),
  ...['home', 'r1s', 'r2', 'offers', 'gear-shop', 'support', 'spaces', 'inventory', 'technology'].map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const urlPath = PAGES[k];
  if (WALL.test(urlPath)) { log('skip wall', urlPath); continue; }
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const source = BASE + urlPath;
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, source);
  try {
    const resp = await p.goto(source, { waitUntil: 'domcontentloaded', timeout: 90000 });
    const status = resp ? resp.status() : 0;
    const finalUrl = p.url();
    if (WALL.test(finalUrl)) {
      log('  WALL', finalUrl, 'stopping branch');
      fs.appendFileSync(path.join(RAW, 'walls.txt'), finalUrl + '\n');
    } else {
      await wait(p, 1500);
      const consent = await dismissConsent(p);
      log('  status', status, 'consent', JSON.stringify(consent));
      if (status >= 400) log('  HTTP', status);
      const extra = mob ? mobileInteractions[k] : interactions[k];
      if (extra) await extra(p, S);
      else { await S.view('default'); await S.full(); }
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
