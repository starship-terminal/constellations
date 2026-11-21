// Captures Gumroad's public pages. Full-colour PNGs go to RAW; quantize.py
// writes screenshots/. Nothing is submitted. Login and signup are photographed
// and not filled. Apple, Google, X, Stripe and passkey are not clicked.
//
//   PLAYWRIGHT=... node public.mjs [page,page]
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'gumroad', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideOverlays(p) {
  await p.addStyleTag({ content: '#onetrust-banner-sdk,[id*="onetrust" i],[class*="onetrust" i],[id*="cookie-banner" i]{display:none!important}' }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
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
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    // Playwright's clip is viewport-relative here, so a tall page is captured
    // by scrolling the viewport and stitching the tiles afterwards.
    if (hCap <= this.requested.viewport.height + 40) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      const tile = this.requested.viewport.height;
      for (let i = 0, y = 0; y < hCap; i++, y += tile) {
        await p.evaluate((yy) => scrollTo(0, yy), y);
        await wait(p, 200);
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png` }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const PAGES = {
  home: '/',
  discover: '/discover',
  blog: '/blog',
  pricing: '/pricing',
  features: '/features',
  about: '/about',
  gumclaw: '/gumclaw',
  'small-bets': '/small-bets',
  mcp: '/mcp',
  help: '/help',
  terms: '/terms',
  privacy: '/privacy',
  prohibited: '/prohibited',
  login: '/login',
  signup: '/signup',
  category: '/drawing-and-painting',
  'blog-post': '/blog/p/gumroad-is-now-open-source',
  product: 'https://tejujangid.gumroad.com/l/Thickimpastobrushes',
};

const EXTRA = {
  home: async (p, S) => {
    const search = p.locator('input[name="query"], input[placeholder*="Search marketplace"]').first();
    if (await search.count()) {
      await search.click();
      await wait(p, 300);
      await S.view('search-focused');
      await p.keyboard.press('Escape').catch(() => {});
    }
  },
  discover: async (p, S, mob) => {
    if (!mob) {
      const box = await p.evaluate(() => {
        const span = [...document.querySelectorAll('[aria-haspopup="dialog"]')].find((el) => /Drawing/.test(el.innerText || ''));
        if (!span) return null;
        const r = span.getBoundingClientRect();
        return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
      });
      if (box) {
        await p.mouse.move(box.x, box.y);
        await wait(p, 700);
        await S.view('category-dialog');
        await p.mouse.move(10, 400);
        await wait(p, 300);
      }
      const more = await p.evaluate(() => {
        const span = [...document.querySelectorAll('[aria-haspopup="dialog"]')].find((el) => (el.innerText || '').trim() === 'More');
        if (!span) return null;
        const r = span.getBoundingClientRect();
        return { x: r.x + 10, y: r.y + r.height / 2 };
      });
      if (more) {
        await p.mouse.click(more.x, more.y);
        await wait(p, 600);
        await S.view('more-dialog');
        await p.keyboard.press('Escape').catch(() => {});
      }
    }
    const sellers = p.getByRole('tab', { name: 'Best Sellers' }).or(p.getByRole('link', { name: 'Best Sellers' })).first();
    if (await sellers.count()) {
      await sellers.click();
      await wait(p, 900);
      await S.view('best-sellers');
    }
  },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const themes = ['light', 'dark'];
const widths = [
  { mob: false, vw: 1440, vh: 900, dpr: 1 },
  { mob: true, vw: 390, vh: 844, dpr: 2 },
];

for (const theme of themes) {
  for (const { mob, vw, vh, dpr } of widths) {
    for (const [key, urlPath] of Object.entries(PAGES)) {
      const name = (mob ? 'mobile-' : '') + key + '-' + theme;
      if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
      // Login and signup do not follow the color scheme. Capture them once, in light.
      if ((key === 'login' || key === 'signup') && (theme === 'dark' || mob)) continue;
      const ctx = await b.newContext({
        viewport: { width: vw, height: vh },
        deviceScaleFactor: dpr,
        userAgent: mob ? UA_MOBILE : UA,
        isMobile: mob,
        hasTouch: mob,
        locale: 'en-US',
        colorScheme: theme,
      });
      await ctx.addInitScript(() => {
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
      });
      const p = await ctx.newPage();
      const S = new Shooter(p, name, vw, vh, dpr);
      log(name);
      try {
        const url = urlPath.startsWith('http') ? urlPath : BASE + urlPath;
        await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
        await wait(p, 1800);
        await hideOverlays(p);
        const title = await p.title();
        if (/just a moment|attention required/i.test(title)) {
          log('  CHALLENGE', name);
        } else {
          await S.view('default');
          if (!mob && ['home', 'discover', 'pricing', 'features', 'blog', 'help'].includes(key)) await S.full();
          if (mob && key === 'home') {
            const menu = p.locator('button[data-toggle="mobile-menu"]').first();
            if (await menu.count()) {
              await menu.click();
              await wait(p, 600);
              await S.view('menu');
              await p.keyboard.press('Escape').catch(() => {});
            }
            await S.full();
          }
          if (EXTRA[key]) await EXTRA[key](p, S, mob);
        }
      } catch (e) {
        log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
      }
      total += S.count;
      await ctx.close();
    }
  }
}
log('done', total, '->', RAW);
await b.close();
