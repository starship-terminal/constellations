// Photograph Digg's public signed-out pages. Cookie notice is hidden, never accepted.
// Does not type credentials, submit forms, or click Google / X.
//
//   PLAYWRIGHT=... node shoot.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'digg', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const only = (process.argv[2] || '').split(',').filter(Boolean);

const browser = await chromium.launch({ headless: true });
const tree = [];

async function hideConsent(page) {
  await page.addStyleTag({ content: 'section.cookie-notice, .cookie-notice { display: none !important; visibility: hidden !important; pointer-events: none !important; }' }).catch(() => {});
}

async function hideSampleAddresses(page) {
  // The newsletter card paints a sample address. Clear it before the shot. Do not type in the field.
  await page.evaluate(() => {
    const walk = (node) => {
      if (node.nodeType === Node.TEXT_NODE) {
        if (node.nodeValue && /@example\.com/i.test(node.nodeValue)) {
          node.nodeValue = node.nodeValue.replace(/\S+@example\.com/gi, '');
        }
        return;
      }
      for (const child of node.childNodes) walk(child);
    };
    walk(document.body);
    for (const el of document.querySelectorAll('input, [placeholder]')) {
      const ph = el.getAttribute('placeholder') || '';
      if (/@example\.com/i.test(ph)) el.setAttribute('placeholder', '');
      if (el.value && /@example\.com/i.test(el.value)) el.value = '';
    }
  }).catch(() => {});
}

async function setTheme(page, theme) {
  // Desktop: the cycle button sits in the sidebar. Phone: it sits in the nav sheet.
  const button = () => page.locator('button[aria-label*="Switch theme"]');
  const openSheet = async () => {
    if (await button().count()) return;
    const opener = page.getByRole('button', { name: 'Open navigation menu' });
    if (await opener.count()) {
      await opener.click();
      await page.waitForTimeout(400);
    }
  };
  for (let i = 0; i < 4; i++) {
    const cls = await page.evaluate(() => document.documentElement.className);
    const has = (name) => cls.split(/\s+/).includes(name);
    if (theme === 'dark' && has('dark')) return cls;
    if (theme === 'light' && has('light')) return cls;
    await openSheet();
    await button().click();
    await page.waitForTimeout(350);
  }
  return page.evaluate(() => document.documentElement.className);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name, extra = {}) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.page, { path: file }, { ...this.requested, sanitizedSourceUrl: extra.url });
    console.log('  shot', path.basename(file));
  }
  async full(name = 'full') {
    const page = this.page;
    const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    if (hCap <= chunk) await screenshotWithMetadata(page, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(page, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    console.log('  shot', name, 'H=' + H);
    await page.evaluate(() => scrollTo(0, 0));
  }
}

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);

  async function visit(slug, url, theme, fn) {
    const name = `${prefix0}${slug}-${theme}`;
    if (only.length && !only.some((o) => name.startsWith(o) || slug === o)) return;
    console.log(name, url);
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(1600);
    await hideConsent(page);
    await hideSampleAddresses(page);
    const cls = await setTheme(page, theme);
    await page.waitForTimeout(400);
    const S = new Shooter(page, name, vw, vh, dpr);
    const finalUrl = page.url();
    tree.push({ slug, url, finalUrl, theme, mobile, status: resp && resp.status(), htmlClass: cls, viewport: { width: vw, height: vh, dpr } });
    await fn(page, S, finalUrl);
  }

  const feeds = [
    ['home', 'https://digg.com/'],
    ['tech', 'https://digg.com/tech'],
    ['gaming', 'https://digg.com/gaming'],
    ['entertainment', 'https://digg.com/entertainment'],
    ['world-business', 'https://digg.com/world-business'],
    ['science', 'https://digg.com/science'],
    ['sports', 'https://digg.com/sports'],
    ['ai', 'https://digg.com/ai'],
  ];
  // Desktop: every feed in light (default) and home+ai in dark. Phone: home, ai, one category.
  const feedList = mobile
    ? [['home', 'https://digg.com/'], ['ai', 'https://digg.com/ai'], ['tech', 'https://digg.com/tech']]
    : feeds;

  for (const [slug, url] of feedList) {
    await visit(slug, url, 'light', async (page, S) => {
      await S.view('default', { url });
      if (slug === 'home' || slug === 'about') await S.full('full');
    });
  }
  await visit('home', 'https://digg.com/', 'dark', async (page, S) => {
    await S.view('default', { url: page.url() });
  });

  if (!mobile) {
    await visit('home', 'https://digg.com/', 'light', async (page, S) => {
      await page.locator('button[aria-label="Feed View"]').click();
      await page.waitForTimeout(400);
      await S.view('feed-view-open', { url: page.url() });
      await page.keyboard.press('Escape');
      await page.locator('button[aria-label^="Feed display"]').click();
      await page.waitForTimeout(400);
      await S.view('feed-display-open', { url: page.url() });
      await page.keyboard.press('Escape');
      // sidebar folded
      await page.locator('button[aria-label="Toggle Sidebar"]').first().click();
      await page.waitForTimeout(500);
      await S.view('sidebar-folded', { url: page.url() });
      await page.locator('button[aria-label="Toggle Sidebar"]').first().click().catch(() => {});
    });
    await visit('story', 'https://digg.com/ai/f7vysbah', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
      await S.full('full');
    });
    await visit('story', 'https://digg.com/ai/f7vysbah', 'dark', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('profile', 'https://digg.com/u/justinmezzell', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('about', 'https://digg.com/about', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
      await S.full('full');
    });
    await visit('contact', 'https://digg.com/contact', 'light', async (page, S) => {
      // Wait for the address links, then clear them. The sentences stay; the addresses do not enter the package.
      await page.waitForFunction(() => document.body.innerText.includes('@digg.com'), { timeout: 15000 }).catch(() => {});
      const n = await page.evaluate(() => {
        let n = 0;
        const walk = (node) => {
          if (node.nodeType === Node.TEXT_NODE) {
            if (node.nodeValue && node.nodeValue.includes('@digg.com')) {
              node.nodeValue = node.nodeValue.replace(/\S+@digg\.com/g, '');
              n += 1;
            }
            return;
          }
          for (const child of node.childNodes) walk(child);
        };
        walk(document.body);
        for (const a of document.querySelectorAll('a[href^="mailto:"]')) {
          a.textContent = '';
          a.removeAttribute('href');
          n += 1;
        }
        return n;
      });
      console.log('  cleared address nodes', n);
      await S.view('default', { url: page.url() });
      await S.full('full');
    });
    await visit('privacy', 'https://digg.com/privacy', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('tos', 'https://digg.com/tos', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('guidelines', 'https://digg.com/community-guidelines', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('not-found', 'https://digg.com/this-page-does-not-exist-capture', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    // Login and signup walls: photograph, do not type, do not click Google or X.
    await visit('login', 'https://digg.com/login?redirect_url=%2F', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
      await page.locator('#identifier-field').focus();
      await page.waitForTimeout(200);
      await S.view('email-focused', { url: page.url() });
    });
    await visit('signup', 'https://digg.com/sign-up?redirect_url=%2F', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
  } else {
    await visit('home', 'https://digg.com/', 'light', async (page, S) => {
      await page.getByRole('button', { name: 'Open navigation menu' }).click();
      await page.waitForTimeout(600);
      await S.view('nav-open', { url: page.url() });
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300);
      await S.full('full');
    });
    await visit('home', 'https://digg.com/', 'dark', async (page, S) => {
      await page.getByRole('button', { name: 'Open navigation menu' }).click();
      await page.waitForTimeout(500);
      await S.view('nav-open', { url: page.url() });
    });
    await visit('story', 'https://digg.com/ai/f7vysbah', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('login', 'https://digg.com/login?redirect_url=%2F', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
    await visit('about', 'https://digg.com/about', 'light', async (page, S) => {
      await S.view('default', { url: page.url() });
    });
  }
  await context.close();
}

await runWidth(false);
await runWidth(true);
fs.writeFileSync(path.join(os.homedir(), '.design-systems', 'digg', 'readings', 'shot-tree.json'), JSON.stringify(tree, null, 2));
console.log('done', tree.length, 'visits');
await browser.close();
