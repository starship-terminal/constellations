// Squarespace public marketing capture.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/squarespace/tools/capture/public/capture.mjs
//
// Writes full-colour shots to ~/.design-systems/squarespace/raw-shots,
// readings to systems/squarespace/raw/, and never submits a form.
// Login, signup, Google, Apple and Facebook are recorded and not entered.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'squarespace', 'raw-shots');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const WALL = /login\.squarespace\.com|account\.squarespace\.com|\/api\/1\/login|accounts\.google\.com|appleid\.apple\.com|facebook\.com\/(login|dialog)/i;

const PAGES = [
  { id: 'home', url: BASE + '/' },
  { id: 'pricing', url: BASE + '/pricing' },
  { id: 'templates', url: BASE + '/templates' },
  { id: 'get-started', url: BASE + '/templates/get-started' },
  { id: 'website-design', url: BASE + '/website-design' },
  { id: 'ecommerce', url: BASE + '/ecommerce-website' },
  { id: 'feature-index', url: BASE + '/feature-index' },
  { id: 'blog', url: BASE + '/blog' },
  { id: 'contact', url: BASE + '/contact' },
  { id: 'about', url: BASE + '/about/company' },
  { id: 'tools', url: BASE + '/tools' },
  { id: 'domains', url: 'https://domains.squarespace.com/' },
  { id: 'login', url: 'https://login.squarespace.com/', wall: true },
];

function isWall(url, text) {
  if (WALL.test(url)) return true;
  const head = (text || '').slice(0, 600);
  return /continue with google|continue with apple|continue with facebook/i.test(head) && /password|email/i.test(head);
}

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 14; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h <= last + 40 && i > 1) break;
    last = h;
    const y = Math.min(h, (i + 1) * 700);
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
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
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
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

async function readFoundations(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
        tag: el.tagName.toLowerCase(),
        cls: (el.className || '').toString().slice(0, 90),
        w: Math.round(r.width), h: Math.round(r.height),
        color: s.color, bg: s.backgroundColor, font: s.fontFamily,
        size: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, ls: s.letterSpacing,
        radius: s.borderRadius, bw: s.borderTopWidth, bs: s.borderTopStyle, bc: s.borderTopColor,
        pad: `${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`,
        shadow: s.boxShadow, tt: s.textTransform, td: s.transitionDuration,
      };
    };
    const first = (sel) => document.querySelector(sel);
    const roles = {
      body: pick(document.body),
      h1: pick(first('h1')),
      h2: pick(first('h2')),
      eyebrow: pick(first('.text--eyebrow')),
      bodyText: pick(first('.text--body, p.text')),
      cta: pick(first('a.cta--primary, a.cta.cta--solid, a.global-navigation__cta, header a.cta')),
      navItem: pick(first('button.global-navigation__header-link-item')),
      link: pick(first('a.cta--inline')),
      promo: pick(first('.promo-banner, [class*="promo-banner"]')),
    };
    const sheets = [];
    for (const sheet of document.styleSheets) {
      let n = 0;
      try { n = sheet.cssRules ? sheet.cssRules.length : 0; } catch { n = -1; }
      sheets.push({ href: sheet.href || 'inline', rules: n });
    }
    const vars = [];
    const walk = (list) => {
      for (const rule of list) {
        if (rule.style) {
          for (let i = 0; i < rule.style.length; i++) {
            const k = rule.style[i];
            if (k.startsWith('--')) vars.push(k);
          }
        }
        if (rule.cssRules) walk(rule.cssRules);
      }
    };
    for (const sheet of document.styleSheets) {
      try { if (sheet.cssRules) walk(sheet.cssRules); } catch { /* cross-origin */ }
    }
    return {
      url: location.href,
      title: document.title,
      vw: innerWidth, vh: innerHeight, dpr: devicePixelRatio,
      roles,
      varSample: [...new Set(vars)].slice(0, 60),
      varCount: new Set(vars).size,
      sheets: sheets.slice(0, 25),
    };
  });
}

async function interact(page, S, id, mobile) {
  if (id === 'home') {
    if (!mobile) {
      const btn = page.locator('nav.global-navigation__nav button.global-navigation__header-link-item').filter({ hasText: 'Products' });
      if (await btn.count()) {
        await btn.first().click({ timeout: 6000 });
        await wait(page, 600);
        await S.view('products-menu');
        await page.keyboard.press('Escape');
        await page.mouse.move(40, 400);
        await wait(page, 300);
      }
      const sol = page.locator('nav.global-navigation__nav button.global-navigation__header-link-item').filter({ hasText: 'Solutions' });
      if (await sol.count()) {
        await sol.first().click({ timeout: 6000 });
        await wait(page, 500);
        await S.view('solutions-menu');
        await page.keyboard.press('Escape');
        await page.mouse.move(40, 400);
        await wait(page, 250);
      }
    } else {
      const ham = page.locator('button.global-navigation__hamburger');
      if (await ham.count()) {
        await ham.first().click({ timeout: 5000, force: true });
        await wait(page, 700);
        await S.view('menu');
        await page.keyboard.press('Escape').catch(() => {});
        await wait(page, 300);
      }
    }
    // FAQ accordion: click, do not submit
    const faq = page.locator('button.faq__accordion-title, .faq__accordion-title').first();
    if (await faq.count()) {
      await faq.scrollIntoViewIfNeeded().catch(() => {});
      await faq.click({ timeout: 4000 }).catch(() => {});
      await wait(page, 500);
      await S.view('faq-open');
    }
    // hover the primary CTA, no navigation
    if (!mobile) {
      const cta = page.locator('header a.cta, a.cta').filter({ hasText: /get started/i }).first();
      if (await cta.count()) {
        await cta.hover({ timeout: 4000 }).catch(() => {});
        await wait(page, 300);
        await S.view('cta-hover');
      }
    }
  }
  if (id === 'pricing') {
    // billing toggle if present, no purchase
    const toggle = page.locator('button, [role="switch"], [role="tab"]').filter({ hasText: /annual|monthly|year|month/i }).first();
    if (await toggle.count()) {
      await toggle.click({ timeout: 4000 }).catch(() => {});
      await wait(page, 500);
      await S.view('billing-toggle');
    }
  }
  if (id === 'templates') {
    const search = page.locator('input[type="search"], input[placeholder*="Search" i], input[aria-label*="Search" i]').first();
    if (await search.count()) {
      await search.click({ timeout: 4000 }).catch(() => {});
      await wait(page, 300);
      await S.view('search-focused');
    }
  }
  if (id === 'login') {
    // look only: do not type email, password, or OAuth
    await S.view('default');
  }
}

const tree = { capturedAt: new Date().toISOString(), pages: [], walls: [], failures: [] };
const foundations = [];

const browser = await chromium.launch({ headless: true });
const only = (process.env.ONLY || '').split(',').filter(Boolean);

for (const mobile of [false, true]) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  for (const spec of PAGES) {
    const name = prefix0 + spec.id;
    if (only.length && !only.includes(name) && !only.includes(spec.id)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    const page = await ctx.newPage();
    const S = new Shooter(page, `${name}-light`, vw, vh, dpr);
    log('PAGE', name, spec.url);
    try {
      const resp = await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 50000 });
      await wait(page, spec.wall ? 1800 : 2200);
      const finalUrl = page.url();
      const status = resp ? resp.status() : null;
      const title = await page.title();
      const snippet = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 500));
      const wall = isWall(finalUrl, snippet) || spec.wall && WALL.test(finalUrl);
      const row = { id: name, requested: spec.url, final: finalUrl.split('?')[0], status, title: title.slice(0, 100), wall, mobile };
      if (status === 429) {
        log('  429, backing off 25s');
        tree.failures.push({ ...row, note: '429' });
        await wait(page, 25000);
      } else if (wall && !spec.wall) {
        log('  WALL', finalUrl.slice(0, 100));
        tree.walls.push(row);
        await S.view('wall');
      } else {
        tree.pages.push(row);
        if (!spec.wall) {
          await S.view('default');
          if (!mobile || spec.id === 'home' || spec.id === 'pricing' || spec.id === 'templates') await S.full();
          await interact(page, S, spec.id, mobile);
          if (!mobile && spec.id === 'home') {
            foundations.push(await readFoundations(page));
          }
        } else {
          await S.view('default');
          tree.walls.push({ ...row, note: 'known login probe, nothing typed' });
        }
      }
    } catch (e) {
      log('  FAIL', e.message.split('\n')[0]);
      tree.failures.push({ id: name, url: spec.url, note: e.message.split('\n')[0].slice(0, 160) });
    }
    await ctx.close();
    await new Promise((r) => setTimeout(r, 1800));
  }
}

fs.writeFileSync(path.join(READ, 'capture-log.json'), JSON.stringify(tree, null, 2));
if (foundations.length) fs.writeFileSync(path.join(READ, 'foundations.json'), JSON.stringify(foundations, null, 2));
log('done shots dir', RAW);
await browser.close();
