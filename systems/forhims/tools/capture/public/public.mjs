// Captures forhims.co.uk public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. One light theme.
// Nothing is submitted, signed into, or typed into a profile, plan, survey
// or newsletter field. Login and assessment URLs are recorded and not entered.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, hideConsent, UA, UA_MOBILE, BASE, scratchDir, isWall } from './lib.mjs';

const RAW = scratchDir();
const pageArg = process.argv.slice(2).filter((a) => !a.startsWith('--')).join(',').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, 12000); y += 700) {
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
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
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
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 5000 });
  await wait(p, 700);
  await hideConsent(p);
  return true;
}

async function openHamburger(p) {
  const btn = p.locator('[class*="global-navigationstyles__Action"]').last();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 5000 });
  await wait(p, 800);
  await hideConsent(p);
  return true;
}

async function closeMenu(p) {
  await p.keyboard.press('Escape').catch(() => {});
  await wait(p, 300);
  await p.mouse.move(20, 800).catch(() => {});
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('sex-menu', async () => {
      if (await openMenu(p, 'Sex')) { await S.view('sex-menu'); await closeMenu(p); }
    });
    await step('learn-menu', async () => {
      if (await openMenu(p, 'Learn')) { await S.view('learn-menu'); await closeMenu(p); }
    });
    await step('account-menu', async () => {
      if (await openHamburger(p)) { await S.view('account-menu'); await closeMenu(p); }
    });
    await S.full();
  } },
  weight: { path: '/weight-loss', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const b = p.getByRole('button', { name: /weight loss treatment options/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await b.scrollIntoViewIfNeeded(); await S.view('faq'); }
    });
    await S.full();
  } },
  hair: { path: '/hair-loss', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  ed: { path: '/erectile-dysfunction', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pe: { path: '/premature-ejaculation', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pdp: { path: '/erectile-dysfunction/sildenafil', run: async (p, S) => {
    await S.view('default');
    await step('accordion', async () => {
      const b = p.getByRole('button', { name: /meet the generic ed pill/i }).first();
      if (await b.count()) {
        await b.scrollIntoViewIfNeeded();
        await wait(p, 400);
        const expanded = await b.getAttribute('aria-expanded');
        if (expanded !== 'true') await b.click();
        await wait(p, 700);
        await S.view('accordion');
      }
    });
    await S.full();
  } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  how: { path: '/how-it-works', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  conditions: { path: '/conditions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { path: '/hims-reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  purpose: { path: '/purpose', run: async (p, S) => { await S.view('default'); } },
  chooser: { path: '/c', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/skin', run: async (p, S) => { await S.view('default'); } },
  legal: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); } },
  migration: { path: '/migration-privacy', run: async (p, S) => { await S.view('default'); } },
  complaints: { path: '/complaints', run: async (p, S) => { await S.view('default'); } },
  sitemap: { path: '/sitemap.html', run: async (p, S) => { await S.view('default'); } },
};

const mobilePages = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('account-menu', async () => {
      if (await openHamburger(p)) {
        await S.view('account-menu');
        await p.evaluate(() => {
          const nodes = [...document.querySelectorAll('div')].filter((n) => /ACCOUNT/.test(n.innerText || '') && n.scrollHeight > n.clientHeight + 40);
          const panel = nodes.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0];
          if (panel) panel.scrollTop = panel.scrollHeight;
        });
        await wait(p, 400);
        await S.view('account-menu-scrolled');
        await closeMenu(p);
      }
    });
    await S.full();
  } },
  weight: { path: '/weight-loss', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pdp: { path: '/erectile-dysfunction/sildenafil', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  chooser: { path: '/c', run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/skin', run: async (p, S) => { await S.view('default'); } },
};

async function runSet(pages, { mobile }) {
  const browser = await chromium.launch({ headless: true });
  const width = mobile ? 390 : 1440;
  const height = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  try {
    for (const [name, spec] of Object.entries(pages)) {
      if (pageArg.length && !pageArg.includes(name) && !pageArg.includes((mobile ? 'mobile-' : '') + name)) continue;
      const context = await browser.newContext(mobile
        ? { viewport: { width, height }, deviceScaleFactor: dpr, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-GB' }
        : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-GB' });
      await patch(context);
      const p = await context.newPage();
      const prefix = (mobile ? 'mobile-' : '') + name + '-light';
      const S = new Shooter(p, prefix, width, height, dpr);
      log('page', prefix, spec.path);
      try {
        const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
        await wait(p, 1800);
        await hideConsent(p);
        const finalUrl = p.url();
        if (isWall(finalUrl)) {
          log('  WALL', finalUrl, 'stopping branch');
          continue;
        }
        log('  status', res && res.status(), 'url', finalUrl);
        const dims = await p.evaluate(() => ({
          innerWidth: window.innerWidth,
          innerHeight: window.innerHeight,
          dpr: window.devicePixelRatio,
        }));
        log('  viewport', JSON.stringify(dims));
        await spec.run(p, S);
      } catch (e) {
        log('  FAILED page', name, String(e.message).split('\n')[0]);
      } finally {
        await context.close();
      }
    }
  } finally {
    await browser.close();
  }
}

const which = process.argv.includes('--mobile') ? 'mobile' : process.argv.includes('--desktop') ? 'desktop' : 'both';
if (which !== 'mobile') await runSet(desktop, { mobile: false });
if (which !== 'desktop') await runSet(mobilePages, { mobile: true });
log('done', RAW);
