// Public Netflix capture. Playwright only. No T3 preview browser.
//
//   RAW=~/.design-systems/netflix/raw-shots PLAYWRIGHT=... node capture.mjs
//
// Does not type an email, phone, password, or code. Does not submit a form.
// Does not click Google, Apple, or Facebook. Stops at a login or signup wall
// after one viewport. Hides the consent banner; never clicks consent POST.
import fs from 'node:fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems/netflix/raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function safeUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function hideConsent(page) {
  await page.addStyleTag({ content: '#onetrust-banner-sdk,#onetrust-consent-sdk .ot-sdk-container{display:none!important}' }).catch(() => {});
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) {
    await page.evaluate((yy) => scrollTo(0, yy), y);
    await wait(page, 180);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page;
    this.prefix = prefix;
    this.vw = vw;
    this.vh = vh;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.page);
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.page, { path: file }, {
      ...this.requested,
      sanitizedSourceUrl: safeUrl(this.page.url()),
    });
    this.count++;
    log('  shot', this.prefix + '-' + name, this.page.url().split('?')[0]);
  }
  async full(name = 'full') {
    const p = this.page;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, { ...this.requested, sanitizedSourceUrl: safeUrl(p.url()) });
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, { ...this.requested, sanitizedSourceUrl: safeUrl(p.url()) });
      }
    }
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function goto(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 }).catch((e) => {
    log('  goto fail', url, e.message.split('\n')[0]);
    return null;
  });
  await wait(page, 2800);
  await hideConsent(page);
  return resp ? resp.status() : 0;
}

async function measure(page, label) {
  const data = await page.evaluate((label) => {
    function pick(el) {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName.toLowerCase(),
        text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
        color: cs.color,
        backgroundColor: cs.backgroundColor,
        borderTopColor: cs.borderTopColor,
        borderTopWidth: cs.borderTopWidth,
        borderRadius: cs.borderRadius,
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
        boxShadow: cs.boxShadow,
        outline: `${cs.outlineWidth} ${cs.outlineStyle} ${cs.outlineColor}`,
        height: cs.height,
        width: cs.width,
      };
    }
    const q = (sel) => document.querySelector(sel);
    const body = getComputedStyle(document.body);
    const html = getComputedStyle(document.documentElement);
    return {
      label,
      path: location.pathname,
      viewport: { innerWidth, innerHeight, dpr: devicePixelRatio },
      page: {
        backgroundColor: body.backgroundColor,
        color: body.color,
        fontFamily: body.fontFamily,
        fontSize: body.fontSize,
        htmlBg: html.backgroundColor,
      },
      nodes: {
        h1: pick(q('h1')),
        signIn: pick([...document.querySelectorAll('a')].find((a) => /sign in/i.test(a.innerText || ''))),
        cta: pick(q('[data-uia="nmhp-card-cta+hero_card"], [data-uia="join-now-btn"], button')),
        email: pick(q('input[type="email"], input[name="userLoginId"]')),
        faq: pick(q('[data-uia^="nmhp-faq"]')),
        footerLink: pick([...document.querySelectorAll('footer a, a')].find((a) => /terms of use/i.test(a.innerText || ''))),
      },
    };
  }, label);
  return data;
}

const browser = await chromium.launch({ headless: true });

async function context(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  return { ctx, vw, vh, dpr };
}

const readings = [];

async function run(mobile, jobs) {
  const { ctx, vw, vh, dpr } = await context(mobile);
  const prefix0 = mobile ? 'mobile-' : '';
  for (const job of jobs) {
    const page = await ctx.newPage();
    const prefix = prefix0 + job.name + '-dark';
    const S = new Shooter(page, prefix, vw, vh, dpr);
    log('\n==', prefix);
    try {
      await goto(page, job.url);
      await job.run(page, S);
      readings.push(await measure(page, prefix));
    } catch (e) {
      log('  FAILED', job.name, e.message.split('\n')[0]);
    }
    await page.close();
  }
  await ctx.close();
}

const desktopJobs = [
  {
    name: 'home',
    url: 'https://www.netflix.com/',
    run: async (page, S) => {
      await S.view('default');
      const email = page.locator('input[type="email"], input[name="email"]').first();
      if (await email.count()) {
        await email.focus();
        await wait(page, 400);
        await S.view('email-focus');
        await page.evaluate(() => document.activeElement && document.activeElement.blur());
      }
      const faq = page.locator('[data-uia="nmhp-faq-accordion+button-0"]');
      if (await faq.count()) {
        await faq.click();
        await wait(page, 500);
        await S.view('faq-open');
      }
      const title = page.locator('[data-uia="top-10-element-1"]');
      if (await title.count()) {
        await title.click();
        await wait(page, 1500);
        await S.view('title-dialog');
        await page.keyboard.press('Escape');
        await wait(page, 400);
      }
      await S.full('full');
    },
  },
  {
    name: 'login-wall',
    url: 'https://www.netflix.com/login',
    run: async (page, S) => {
      await S.view('default');
    },
  },
  {
    name: 'signup-wall',
    url: 'https://www.netflix.com/signup',
    run: async (page, S) => {
      await S.view('default');
    },
  },
  {
    name: 'originals',
    url: 'https://www.netflix.com/browse/genre/839338',
    run: async (page, S) => {
      await S.view('default');
      await S.full('full');
    },
  },
  {
    name: 'help',
    url: 'https://help.netflix.com/',
    run: async (page, S) => {
      await S.view('default');
      const search = page.locator('input[name="q"]').first();
      if (await search.count()) {
        await search.focus();
        await wait(page, 300);
        await S.view('search-focus');
        await page.evaluate(() => document.activeElement && document.activeElement.blur());
      }
    },
  },
  {
    name: 'help-faq',
    url: 'https://help.netflix.com/support/412',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'help-devices',
    url: 'https://www.netflix.com/watch',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'terms',
    url: 'https://help.netflix.com/legal/termsofuse',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'privacy',
    url: 'https://help.netflix.com/legal/privacy',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'notices',
    url: 'https://help.netflix.com/legal/notices',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'plans',
    url: 'https://help.netflix.com/en/node/24926',
    run: async (page, S) => { await S.view('default'); },
  },
  // Media Center loads, but its headline names a place. Not screenshotted.
  {
    name: 'jobs',
    url: 'https://jobs.netflix.com/',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'investors',
    url: 'https://ir.netflix.com/',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'speed',
    url: 'https://fast.com/',
    run: async (page, S) => {
      await wait(page, 2500);
      await S.view('default');
    },
  },
];

const mobileJobs = [
  {
    name: 'home',
    url: 'https://www.netflix.com/',
    run: async (page, S) => {
      await S.view('default');
      const faq = page.locator('[data-uia="nmhp-faq-accordion+button-0"]');
      if (await faq.count()) {
        await faq.click();
        await wait(page, 400);
        await S.view('faq-open');
      }
      await S.full('full');
    },
  },
  {
    name: 'login-wall',
    url: 'https://www.netflix.com/login',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'title',
    url: 'https://www.netflix.com/title/81997887',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'help',
    url: 'https://help.netflix.com/',
    run: async (page, S) => { await S.view('default'); },
  },
  {
    name: 'originals',
    url: 'https://www.netflix.com/browse/genre/839338',
    run: async (page, S) => { await S.view('default'); },
  },
];

await run(false, desktopJobs);
await run(true, mobileJobs);

const out = path.join(process.env.HOME, '.design-systems/netflix/readings.json');
fs.writeFileSync(out, JSON.stringify({ capturedAt: new Date().toISOString(), readings }, null, 2));
log('\nreadings', readings.length, '->', out);
await browser.close();
