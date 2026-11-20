// Captures macawhq.com public pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/macaw/raw-shots PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, named mobile-*. Nothing is
// submitted. Login and sign-up links are recorded and not followed: the app
// host does not resolve (see site-tree.md).
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, closePromo } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'macaw', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
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
  async view(name, source) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, { ...this.requested, sanitizedSourceUrl: source || null });
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full', source) {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const req = { ...this.requested, sanitizedSourceUrl: source || null };
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, req);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, req);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function pauseMotion(p) {
  await p.addStyleTag({ content: '.splide__list, .splide__slide { animation: none !important; transition: none !important; }' }).catch(() => {});
}

async function openResources(p) {
  const toggle = p.locator('.navbar_dropdown-toggle').first();
  const box = await toggle.boundingBox();
  if (!box) return false;
  await p.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  await wait(p, 500);
  const open = await p.evaluate(() => {
    const list = document.querySelector('.navbar_dropdown-list');
    if (!list) return false;
    return getComputedStyle(list).display !== 'none' && list.getBoundingClientRect().height > 20;
  });
  return open;
}

async function openExample(p) {
  await pauseMotion(p);
  await p.evaluate(() => document.querySelector('#examples')?.scrollIntoView({ block: 'center' }));
  await wait(p, 300);
  const opened = await p.evaluate(() => {
    const el = [...document.querySelectorAll('.div-block-46')].find((e) => /Gong|Ultimate Sales Coaching/.test(e.innerText || ''));
    if (!el) return false;
    el.click();
    const modal = [...document.querySelectorAll('.tingle-modal')].find((m) => getComputedStyle(m).display !== 'none' && m.getBoundingClientRect().height > 100);
    return !!modal;
  });
  await wait(p, 600);
  return opened;
}

async function openMenu(p) {
  const btn = p.locator('.navbar_menu-button').first();
  if (!(await btn.count())) return false;
  await btn.click({ force: true });
  await wait(p, 500);
  return p.evaluate(() => {
    const menu = document.querySelector('.w-nav-menu');
    return !!menu && getComputedStyle(menu).display !== 'none';
  });
}

const desktop = {
  home: { path: '/', source: 'https://macawhq.com/', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/');
    await S.full('full', 'https://macawhq.com/');
    if (await openResources(p)) {
      await S.view('resources', 'https://macawhq.com/');
      await p.mouse.move(8, 8);
      await wait(p, 300);
    } else log('  resources dropdown did not open');
    if (await openExample(p)) {
      await S.view('example-dialog', 'https://macawhq.com/#examples');
      await p.evaluate(() => document.querySelector('.tingle-modal--visible .tingle-modal__close')?.click());
      await wait(p, 400);
    } else log('  example dialog did not open');
    await p.evaluate(() => document.querySelector('#prod')?.scrollIntoView({ block: 'start' }));
    await wait(p, 400);
    await S.view('product-anchor', 'https://macawhq.com/#prod');
  } },
  pricing: { path: '/pricing', source: 'https://macawhq.com/pricing', run: async (p, S) => {
    await S.view('yearly', 'https://macawhq.com/pricing');
    await S.full('full', 'https://macawhq.com/pricing');
    const monthly = p.locator('.pricing-toggle-button').filter({ hasText: 'Monthly' }).first();
    if (await monthly.count()) {
      await monthly.click();
      await wait(p, 500);
      await S.view('monthly', 'https://macawhq.com/pricing');
    }
  } },
  contact: { path: '/contact-us', source: 'https://macawhq.com/contact-us', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/contact-us');
    await S.full('full', 'https://macawhq.com/contact-us');
    const field = p.locator('input[name="Contact-1-Name-1"]').first();
    if (await field.count()) {
      await field.focus();
      await wait(p, 300);
      await S.view('field-focused', 'https://macawhq.com/contact-us');
    }
  } },
  terms: { path: '/terms-and-conditions', source: 'https://macawhq.com/terms-and-conditions', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/terms-and-conditions');
    await S.full('full', 'https://macawhq.com/terms-and-conditions');
  } },
  privacy: { path: '/privacy-policy', source: 'https://macawhq.com/privacy-policy', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/privacy-policy');
    await S.full('full', 'https://macawhq.com/privacy-policy');
  } },
  'tool-title': { path: '/free-tools/blog-title-generator', source: 'https://macawhq.com/free-tools/blog-title-generator', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/free-tools/blog-title-generator');
    await S.full('full', 'https://macawhq.com/free-tools/blog-title-generator');
  } },
  'tool-ideas': { path: '/free-tools/blog-post-ideas-generator', source: 'https://macawhq.com/free-tools/blog-post-ideas-generator', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/free-tools/blog-post-ideas-generator');
  } },
  'tool-content': { path: '/free-tools/ai-content-idea-generator', source: 'https://macawhq.com/free-tools/ai-content-idea-generator', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/free-tools/ai-content-idea-generator');
  } },
  'tool-outline': { path: '/free-tools/ai-blog-outline-generator', source: 'https://macawhq.com/free-tools/ai-blog-outline-generator', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/free-tools/ai-blog-outline-generator');
  } },
};

const mobile = {
  home: { path: '/', source: 'https://macawhq.com/', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/');
    await S.full('full', 'https://macawhq.com/');
    if (await openMenu(p)) await S.view('menu', 'https://macawhq.com/');
    else log('  mobile menu did not open');
  } },
  pricing: { path: '/pricing', source: 'https://macawhq.com/pricing', run: async (p, S) => {
    await S.view('yearly', 'https://macawhq.com/pricing');
    const monthly = p.locator('.pricing-toggle-button').filter({ hasText: 'Monthly' }).first();
    if (await monthly.count()) {
      await monthly.click();
      await wait(p, 400);
      await S.view('monthly', 'https://macawhq.com/pricing');
    }
  } },
  contact: { path: '/contact-us', source: 'https://macawhq.com/contact-us', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/contact-us');
  } },
  terms: { path: '/terms-and-conditions', source: 'https://macawhq.com/terms-and-conditions', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/terms-and-conditions');
  } },
  privacy: { path: '/privacy-policy', source: 'https://macawhq.com/privacy-policy', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/privacy-policy');
  } },
  'tool-title': { path: '/free-tools/blog-title-generator', source: 'https://macawhq.com/free-tools/blog-title-generator', run: async (p, S) => {
    await S.view('default', 'https://macawhq.com/free-tools/blog-title-generator');
  } },
};

const browser = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
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
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, 2200);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
