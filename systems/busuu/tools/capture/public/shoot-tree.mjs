// Photographs distinct public Busuu states at 1440x900 and 390x844.
// Stops at login and signup walls. Never types, never submits, never clicks
// Apple, Facebook, Google, Microsoft or SSO. Cookie banners are hidden, never answered.
//
//   RAW=~/.design-systems/busuu/raw-shots PLAYWRIGHT=... node shoot-tree.mjs
import fs from 'node:fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW;
if (!RAW) throw new Error('RAW is required');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = [
  ['home', '/'],
  ['en', '/en'],
  ['languages', '/en/choose-your-language'],
  ['course-spanish', '/en/course/learn-spanish-online'],
  ['course-japanese', '/en/course/learn-japanese-online'],
  ['it-works', '/en/it-works/courses'],
  ['premium', '/en/premium'],
  ['mobile-app', '/en/mobile'],
  ['voucher', '/en/voucher'],
  ['about', '/en/about'],
  ['careers', '/en/careers'],
  ['press', '/en/press'],
  ['partners', '/en/partners'],
  ['covid', '/en/covid-19'],
  ['slavery', '/en/modern-slavery-statement'],
  ['terms', '/en/terms'],
  ['privacy', '/en/privacy'],
  ['grammar', '/en/spanish/spanish-numbers'],
  ['guide', '/en/languages/how-to-speak-spanish'],
  ['login', '/en/login'],
  ['blog', 'https://blog.busuu.com/'],
  ['help', 'https://help.busuu.com/hc/en-us'],
  ['business', 'https://business.busuu.com/'],
  ['education', 'https://business.busuu.com/education'],
];

function safeUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.toString();
  } catch {
    return null;
  }
}

async function shot(page, file, req, source) {
  await screenshotWithMetadata(page, { path: `${RAW}/${file}.png` }, { ...req, sanitizedSourceUrl: safeUrl(source || page.url()) });
  log('  shot', file);
}

async function openKebab(page) {
  const icon = page.locator('#js-menu-toggle, span.responsive-nav__icon').filter({ visible: true }).first();
  if (!(await icon.count())) return false;
  await icon.click({ timeout: 4000 }).catch(() => icon.evaluate((el) => (el.closest('a') || el).click()));
  await wait(page, 900);
  return true;
}

async function openFooterLang(page) {
  const sel = page.locator('footer select, select').filter({ visible: true }).first();
  if (!(await sel.count())) return false;
  await sel.focus();
  await page.keyboard.press('Alt+ArrowDown').catch(() => {});
  await sel.click({ timeout: 3000 }).catch(() => {});
  await wait(page, 600);
  return true;
}

const browser = await chromium.launch();
let n = 0;
for (const mobile of [false, true]) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix = mobile ? 'phone' : 'desktop';
  const req = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await patch(ctx);
  const page = await ctx.newPage();
  for (const [name, path] of PAGES) {
    const url = path.startsWith('http') ? path : BASE + path;
    log(prefix, name, url);
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
      const ok = await clearChallenge(page, { tries: 8, step: 1200 });
      await wait(page, 2800);
      if (!ok) { log('  BLOCKED', name); continue; }
      await closePromo(page);
      await shot(page, `${prefix}-${name}-light-default`, req, url);
      n++;
      if (name === 'home') {
        if (await openKebab(page)) {
          await shot(page, `${prefix}-home-light-menu`, req, url);
          n++;
          await page.keyboard.press('Escape').catch(() => {});
        } else log('  no kebab');
      }
      if (name === 'home' && !mobile) {
        if (await openFooterLang(page)) {
          await shot(page, `${prefix}-home-light-language`, req, url);
          n++;
          await page.keyboard.press('Escape').catch(() => {});
        }
      }
      if (name === 'premium' && !mobile) {
        const tab = page.locator('button, [role="tab"]').filter({ hasText: /^1 month$/i }).filter({ visible: true }).first();
        if (await tab.count()) {
          await tab.click({ timeout: 4000 }).catch(() => {});
          await wait(page, 900);
          await shot(page, `${prefix}-premium-light-monthly`, req, url);
          n++;
        } else log('  no 1 month tab');
      }
      if (name === 'business' && !mobile) {
        const toggle = page.locator('button.menu__child-toggle').filter({ visible: true }).first();
        if (await toggle.count()) {
          await toggle.click({ timeout: 4000 }).catch(() => {});
          await wait(page, 700);
          await shot(page, `${prefix}-business-light-submenu`, req, 'https://business.busuu.com/');
          n++;
        }
      }
      if (name === 'business' && mobile) {
        const trigger = page.locator('.mobile-trigger').filter({ visible: true }).first();
        if (await trigger.count()) {
          await trigger.click({ timeout: 4000 }).catch(() => {});
          await wait(page, 800);
          await shot(page, `${prefix}-business-light-menu`, req, 'https://business.busuu.com/');
          n++;
        }
      }
    } catch (e) {
      log('  FAILED', name, String(e.message).split('\n')[0]);
    }
  }
  await ctx.close();
}
log('done', n);
await browser.close();
