// Map polar.sh controls. Read-only: no typing, no form submit, no OAuth click.
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node probe.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = process.env.OUT || path.join(os.homedir(), '.design-systems', 'polar', 'probe.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(20000);

function clean(u) {
  try {
    const x = new URL(u);
    x.hash = '';
    for (const k of ['code', 'token', 'session', 'state', 'oauth', 'access_token', 'id_token']) x.searchParams.delete(k);
    return x.origin + x.pathname + (x.search ? x.search : '');
  } catch {
    return String(u).slice(0, 180);
  }
}

async function dump(label) {
  return page.evaluate((label) => {
    const txt = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 90);
    const hrefOf = (a) => {
      try {
        const u = new URL(a.href);
        return u.origin + u.pathname + (u.search ? u.search : '');
      } catch { return a.getAttribute('href'); }
    };
    const nav = document.querySelector('header, nav');
    const footer = document.querySelector('footer');
    const visible = (el) => {
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < innerHeight + 40;
    };
    const items = (root) => root ? [...root.querySelectorAll('a, button')].filter(visible).map((el) => ({
      tag: el.tagName,
      text: txt(el),
      href: el.tagName === 'A' ? hrefOf(el) : null,
      expanded: el.getAttribute('aria-expanded'),
      popup: el.getAttribute('aria-haspopup'),
    })).filter((x) => x.text || x.href) : [];
    const overlays = [...document.querySelectorAll('[role=menu], [role=dialog], [data-state=open], [data-radix-popper-content-wrapper]')].map((el) => ({
      role: el.getAttribute('role'),
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400),
    }));
    return {
      label,
      url: location.origin + location.pathname,
      title: document.title,
      htmlClass: document.documentElement.className,
      bg: getComputedStyle(document.body).backgroundColor,
      h1: (document.querySelector('h1') || {}).innerText || '',
      nav: items(nav).slice(0, 30),
      footer: items(footer).slice(0, 40),
      overlays,
      buttons: [...document.querySelectorAll('button')].filter(visible).slice(0, 20).map((b) => txt(b)),
    };
  }, label);
}

const report = { captured: new Date().toISOString(), pages: [], menus: [] };
await page.goto('https://polar.sh/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2500);
report.pages.push(await dump('home'));

// Click header controls that are buttons (Features, Docs, Sign in, Get Started)
// and record what opens. Stop if the URL leaves polar.sh or lands on /auth.
const clicks = ['Features', 'Docs', 'Sign in'];
for (const name of clicks) {
  await page.goto('https://polar.sh/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1200);
  const btn = page.locator('nav button, header button').filter({ hasText: name }).first();
  const before = page.url();
  let opened = null;
  try {
    if (await btn.count()) {
      await btn.click({ timeout: 5000 });
      await page.waitForTimeout(900);
      opened = await dump('click-' + name);
    } else {
      opened = { missing: true };
    }
  } catch (e) {
    opened = { error: String(e.message).split('\n')[0] };
  }
  report.menus.push({ name, before: clean(before), after: clean(page.url()), opened });
  if (/auth|login|signup|checkout/i.test(page.url()) && name !== 'Sign in') break;
}

// Features menu links if a menu opened
const featureMenu = report.menus.find((m) => m.name === 'Features');
if (featureMenu?.opened?.overlays?.length) {
  report.featureMenuText = featureMenu.opened.overlays;
}

await page.goto('https://polar.sh/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(800);
const featureLinks = await page.evaluate(() => {
  const nav = document.querySelector('nav, header');
  if (!nav) return [];
  return [...nav.querySelectorAll('a')].map((a) => ({
    text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    href: a.getAttribute('href'),
  }));
});
report.navAnchors = featureLinks;

fs.writeFileSync(OUT, JSON.stringify(report, null, 2));
console.log('wrote', OUT);
console.log(JSON.stringify({
  homeTitle: report.pages[0]?.title,
  homeBg: report.pages[0]?.bg,
  nav: report.pages[0]?.nav,
  menus: report.menus.map((m) => ({ name: m.name, after: m.after, overlays: m.opened?.overlays?.length, nav: m.opened?.nav, error: m.opened?.error, missing: m.opened?.missing })),
}, null, 2));
await browser.close();
