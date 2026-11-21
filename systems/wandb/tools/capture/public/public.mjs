// Public Playwright capture of wandb.ai marketing pages.
// Photographs reachable public states. Opens a login or signup wall only far
// enough to see what it asks for, photographs it, and stops that branch.
// Never types. Never clicks an identity provider. Never submits a form.
//
//   PLAYWRIGHT=... RAW=... node public.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, SITE, originPath, isAuthWall, hideOverlays } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'wandb', 'raw-shots');
const OUT = process.env.OUT || path.join(os.homedir(), '.design-systems', 'wandb');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const AUTH_CLICK = /google|github|microsoft|apple|sso|identity|continue with/i;

function safeHref(href, base) {
  try {
    const u = new URL(href, base);
    if (!['http:', 'https:'].includes(u.protocol)) return null;
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function pageFacts(page) {
  return page.evaluate(() => {
    const body = (document.body?.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 900);
    const inputs = [...document.querySelectorAll('input, textarea, select')].slice(0, 16).map((el) => ({
      tag: el.tagName.toLowerCase(),
      type: el.getAttribute('type'),
      name: el.getAttribute('name'),
      autocomplete: el.getAttribute('autocomplete'),
      placeholder: el.getAttribute('placeholder'),
      aria: el.getAttribute('aria-label'),
      required: el.required || el.getAttribute('aria-required') === 'true',
    }));
    const providers = [...document.querySelectorAll('a, button')].map((el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim())
      .filter((t) => /google|github|microsoft|apple|sso/i.test(t))
      .slice(0, 8);
    const heading = [...document.querySelectorAll('h1, h2')].map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim()).filter(Boolean).slice(0, 3);
    return {
      title: document.title,
      body,
      inputs,
      providers,
      heading,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      bg: getComputedStyle(document.body || document.documentElement).backgroundColor,
    };
  });
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.page, { path: file }, this.requested);
    this.count += 1;
    log('  shot', this.prefix, name);
    return file;
  }
  async full(name = 'full') {
    const page = this.page;
    const startH = await page.evaluate(() => document.documentElement.scrollHeight);
    const steps = Math.min(12, Math.ceil(startH / 700));
    for (let i = 0; i < steps; i++) {
      await page.evaluate((y) => scrollTo(0, y), i * 700);
      await wait(page, 180);
    }
    await page.evaluate(() => scrollTo(0, 0));
    await wait(page, 400);
    const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    if (H > MAXH) log('  ! truncated', name, H, 'to', hCap);
    if (hCap <= chunk) {
      await screenshotWithMetadata(page, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(page, {
          path: `${f}.part${i}.png`,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count += 1;
    await page.evaluate(() => scrollTo(0, 0));
    log('  shot', this.prefix, name, 'H=' + H);
  }
}

async function openPublic(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await wait(page, 2200);
  await hideOverlays(page);
  const facts = await pageFacts(page);
  const landed = originPath(page.url());
  const status = res ? res.status() : null;
  const wall = isAuthWall(page.url(), facts.body) || /just a moment|verify you are human|attention required/i.test(facts.title + facts.body);
  return { status, landed, wall, facts };
}

const tree = {
  capturedAt: new Date().toISOString(),
  product: 'Weights & Biases',
  domain: 'wandb.ai',
  method: 'public Playwright, signed out, no form submit, no identity provider click',
  roots: [],
  controls: [],
  pages: [],
  walls: [],
  notes: [],
};

const walls = [];

async function recordWall(page, from, control) {
  const facts = await pageFacts(page);
  const entry = {
    control,
    from,
    url: originPath(page.url()),
    title: facts.title,
    headings: facts.heading,
    asksFor: facts.inputs.map((i) => ({
      tag: i.tag,
      type: i.type,
      autocomplete: i.autocomplete,
      placeholder: i.placeholder,
      aria: i.aria,
      required: i.required,
    })),
    identityProvidersSeen: facts.providers,
    submitted: false,
    typed: false,
    stopped: true,
    bodyExcerpt: facts.body.slice(0, 280),
  };
  walls.push(entry);
  tree.walls.push(entry);
  return entry;
}

async function desktopPass() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
  });
  const page = await context.newPage();
  const S = new Shooter(page, 'home-dark', 1440, 900, 1);

  const root = await openPublic(page, 'https://wandb.ai/');
  tree.roots.push({ requested: 'https://wandb.ai/', ...root, facts: { title: root.facts.title, body: root.facts.body.slice(0, 200), inputs: root.facts.inputs, providers: root.facts.providers } });
  if (root.wall) {
    await S.view('login-wall');
    await recordWall(page, 'https://wandb.ai/', 'direct navigation of wandb.ai/');
    tree.notes.push('https://wandb.ai/ redirected to a login wall. That branch stopped.');
  }

  const homeReq = await openPublic(page, 'https://wandb.ai/home');
  tree.roots.push({ requested: 'https://wandb.ai/home', landed: homeReq.landed, wall: homeReq.wall, title: homeReq.facts.title, status: homeReq.status });
  if (homeReq.wall) {
    tree.notes.push('https://wandb.ai/home redirected to a login wall. Not photographed again. Branch stopped.');
    await recordWall(page, 'https://wandb.ai/home', 'direct navigation of wandb.ai/home');
  }

  const site = await openPublic(page, SITE);
  tree.pages.push({ name: 'home', requested: SITE, landed: site.landed, status: site.status, wall: site.wall, title: site.facts.title, theme: site.facts.colorScheme, bg: site.facts.bg });
  if (site.wall || /just a moment/i.test(site.facts.title)) {
    tree.notes.push('Marketing home did not load. Capture stopped. No package invented from memory.');
    fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2));
    await browser.close();
    throw new Error('site did not load: ' + site.landed + ' ' + site.facts.title);
  }
  await S.view('default');
  await S.full('full');

  // Header controls, read from the live DOM. Menus are hover panels (buttons have 0 width).
  const header = await page.evaluate(() => {
    const headerEl = document.querySelector('header') || document.body;
    return [...headerEl.querySelectorAll('a[href], button')].map((el) => {
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        href: el.getAttribute('href'),
        top: Math.round(r.top),
        left: Math.round(r.left),
        w: Math.round(r.width),
        h: Math.round(r.height),
      };
    }).filter((el) => el.top >= 40 && el.top < 180 && (el.w > 0 || el.h > 0 || el.tag === 'BUTTON'));
  });
  tree.controls.push({ surface: 'header', items: header.map((el) => ({ ...el, href: el.href ? safeHref(el.href, SITE) : null })) });

  const menus = [
    { name: 'Weave', x: 400 },
    { name: 'Solutions', x: 530 },
    { name: 'Enterprise', x: 660 },
    { name: 'Resources', x: 790 },
  ];
  for (const menu of menus) {
    await page.mouse.move(menu.x, 106);
    await wait(page, 700);
    const links = await page.evaluate(() => [...document.querySelectorAll('a[href]')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.width > 40 && r.height > 16 && r.top > 120 && r.top < 640;
    }).map((a) => ({
      text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 90),
      href: a.href,
    })));
    const unique = [];
    const seen = new Set();
    for (const link of links) {
      const href = safeHref(link.href, SITE);
      const key = link.text + href;
      if (!href || seen.has(key)) continue;
      seen.add(key);
      unique.push({ text: link.text, href });
    }
    tree.controls.push({ surface: 'menu', opens: menu.name, via: 'hover header label', links: unique });
    if (unique.length) {
      await S.view('menu-' + menu.name.toLowerCase());
    }
    await page.mouse.move(20, 400);
    await wait(page, 250);
  }

  // CTA states on the home page, no navigation.
  const cta = page.locator('a, button').filter({ hasText: /get started with weave|sign up|contact/i }).first();
  if (await cta.count()) {
    await cta.scrollIntoViewIfNeeded().catch(() => {});
    await cta.hover().catch(() => {});
    await wait(page, 400);
    await S.view('cta-hover');
    await page.keyboard.press('Escape').catch(() => {});
  }

  // Public pages the homepage and footer actually link to. One representative each.
  const pages = [
    ['pricing', 'https://wandb.ai/site/privately-hosted-pricing/'],
    ['contact', 'https://wandb.ai/site/contact/'],
    ['weave', 'https://wandb.ai/site/weave/'],
    ['about', 'https://wandb.ai/site/company/about-us/'],
    ['careers', 'https://wandb.ai/site/careers/'],
    ['brand', 'https://wandb.ai/site/brand-identity/'],
    ['security', 'https://wandb.ai/site/security'],
    ['docs', 'https://docs.wandb.ai/'],
  ];
  for (const [name, url] of pages) {
    const opened = await openPublic(page, url);
    const row = { name, requested: originPath(url), landed: opened.landed, status: opened.status, wall: opened.wall, title: opened.facts.title, theme: opened.facts.colorScheme, bg: opened.facts.bg };
    tree.pages.push(row);
    if (opened.wall) {
      const shot = new Shooter(page, name + '-wall', 1440, 900, 1);
      await shot.view('default');
      await recordWall(page, url, 'navigation from public link ' + name);
      log('  wall, stopped', name, opened.landed);
      continue;
    }
    if (/just a moment|attention required|verify you are human/i.test(opened.facts.title + opened.facts.body)) {
      row.blocked = true;
      tree.notes.push(name + ' showed a bot check. Not solved. Branch stopped.');
      const shot = new Shooter(page, name + '-blocked', 1440, 900, 1);
      await shot.view('default').catch((e) => log('  shot failed', name, e.message.split('\n')[0]));
      continue;
    }
    const shot = new Shooter(page, name + '-dark', 1440, 900, 1);
    await shot.view('default');
    if (name === 'pricing' || name === 'contact' || name === 'brand') await shot.full('full');
    log('  page', name, opened.landed, opened.status);
  }

  // Login and signup walls: open, photograph, record fields, stop. No typing.
  for (const [name, url, control] of [
    ['login', 'https://id.coreweave.com/login', 'header LOG IN'],
    ['signup', 'https://id.coreweave.com/signup', 'header SIGN UP'],
  ]) {
    const opened = await openPublic(page, url);
    const shot = new Shooter(page, name + '-light', 1440, 900, 1);
    await shot.view('default').catch((e) => log('  wall shot failed', name, e.message.split('\n')[0]));
    await recordWall(page, url, control);
    tree.pages.push({ name, requested: originPath(url), landed: opened.landed, wall: true, title: opened.facts.title, stopped: true });
    log('  wall recorded', name, opened.landed);
  }

  await browser.close();
}

async function mobilePass() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const page = await context.newPage();
  const opened = await openPublic(page, SITE);
  tree.pages.push({ name: 'home-mobile', landed: opened.landed, wall: opened.wall, title: opened.facts.title, width: 390 });
  if (!opened.wall) {
    const S = new Shooter(page, 'mobile-home-dark', 390, 844, 2);
    await S.view('default');
    const menu = page.locator('button').filter({ hasText: /menu|open/i }).first();
    const burger = page.locator('header button, button[aria-label*="menu" i], button[aria-label*="Menu" i]').first();
    let openedMenu = false;
    if (await burger.count()) {
      await burger.click({ timeout: 4000 }).catch(() => {});
      await wait(page, 800);
      openedMenu = true;
    } else if (await menu.count()) {
      await menu.click({ timeout: 4000 }).catch(() => {});
      await wait(page, 800);
      openedMenu = true;
    } else {
      // Elementor headers often use a hamburger with no accessible name. Click the right-side control.
      await page.mouse.click(350, 100);
      await wait(page, 800);
      openedMenu = true;
    }
    if (openedMenu) await S.view('menu-open');
    const links = await page.evaluate(() => [...document.querySelectorAll('a[href], button')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 20 && r.height > 16 && r.top > 40 && r.top < 800;
    }).slice(0, 40).map((el) => ({
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      href: el.getAttribute('href'),
    })));
    tree.controls.push({
      surface: 'mobile-header',
      width: 390,
      links: links.map((el) => ({ ...el, href: el.href ? safeHref(el.href, SITE) : null })),
    });
  }
  const pricing = await openPublic(page, 'https://wandb.ai/site/privately-hosted-pricing/');
  if (!pricing.wall) {
    const S = new Shooter(page, 'mobile-pricing-dark', 390, 844, 2);
    await S.view('default');
    tree.pages.push({ name: 'pricing-mobile', landed: pricing.landed, wall: false, title: pricing.facts.title, width: 390 });
  }
  await browser.close();
}

try {
  await desktopPass();
  await mobilePass();
} catch (e) {
  tree.notes.push('capture failed: ' + String(e.message || e).split('\n')[0]);
  fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2));
  console.error(e);
  process.exit(1);
}

fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2));
fs.writeFileSync(path.join(OUT, 'login-walls.json'), JSON.stringify(walls, null, 2));
log('done', 'shots in', RAW);
log('tree', path.join(OUT, 'site-tree.json'));
