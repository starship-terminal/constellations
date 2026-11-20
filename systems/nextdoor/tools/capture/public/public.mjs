// Captures Nextdoor's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Nothing is typed or
// submitted. Google, Facebook and Apple are not clicked. A page that lands
// on a login or signup wall is recorded and skipped.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'nextdoor', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = {
  home: 'https://nextdoor.com/',
  about: 'https://about.nextdoor.com/',
  press: 'https://about.nextdoor.com/press-releases',
  careers: 'https://about.nextdoor.com/careers/',
  help: 'https://help.nextdoor.com/s/topic-page?topicName=Neighbor&language=en_US',
  privacy: 'https://help.nextdoor.com/s/article/Privacy-Policy-2026?language=en_US',
  smallbiz: 'https://business.nextdoor.com/en-us/small-business',
  enterprise: 'https://business.nextdoor.com/en-us/enterprise',
  agency: 'https://about.nextdoor.com/public-agency',
  developers: 'https://developer.nextdoor.com/',
  directories: 'https://nextdoor.com/directories/',
  agencies: 'https://nextdoor.com/agencies/',
  neighborhoods: 'https://nextdoor.com/find-neighborhood/',
  industry: 'https://business.nextdoor.com/en-us/resources/industry/home-garden',
  blog: 'https://blog.nextdoor.com/',
  guidelines: 'https://help.nextdoor.com/s/article/community-guidelines?language=en_US',
};

const WALL = /\/login\/|\/join\/?$|\/choose_address|\/create-business|accounts\.google|appleid\.apple|facebook\.com|ads\.nextdoor\.com\/v2\/signup/i;

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 6000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
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

async function openMenu(p, S, label) {
  const btn = p.getByRole('button', { name: label, exact: true });
  if (!(await btn.count())) return;
  await btn.first().click({ timeout: 4000 });
  await wait(p, 700);
  await S.view('menu-' + label.toLowerCase());
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 250);
}

function spec(key, extra) {
  return { url: PAGES[key], run: async (p, S) => { await S.view('default'); await S.full(); if (extra) await extra(p, S); } };
}

const desktop = {
  home: { url: PAGES.home, run: async (p, S) => {
    await S.view('default');
    await step('partners-menu', () => openMenu(p, S, 'Partners'));
    await step('businesses-menu', () => openMenu(p, S, 'Businesses'));
    await S.full();
  } },
  about: spec('about'),
  press: spec('press'),
  careers: spec('careers'),
  help: spec('help'),
  privacy: spec('privacy'),
  smallbiz: spec('smallbiz'),
  enterprise: spec('enterprise'),
  agency: spec('agency'),
  developers: spec('developers'),
  directories: spec('directories'),
  agencies: spec('agencies'),
  neighborhoods: spec('neighborhoods'),
  industry: spec('industry'),
  blog: spec('blog'),
  guidelines: spec('guidelines'),
};

const mobileKeys = ['home', 'about', 'smallbiz', 'help', 'directories', 'neighborhoods'];
const mobile = Object.fromEntries(mobileKeys.map((k) => [k, { url: PAGES[k], run: async (p, S) => { await S.view('default'); await S.full(); } }]));

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const specRow = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(specRow.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(p, 2500);
    await closePromo(p);
    if (WALL.test(p.url())) {
      log('  WALL', p.url(), 'status', resp && resp.status());
    } else {
      await specRow.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
