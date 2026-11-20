// Signed-in Kitchen.co workspace capture.
// Uses the persistent Chromium profile. Does not invite, create, pay or change settings.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/app.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'kitchen', 'raw-shots');
const PROFILE = process.env.PROFILE || path.join(os.homedir(), '.design-systems', 'kitchen', 'chrome-profile');
const originFile = path.join(os.homedir(), '.design-systems', 'kitchen', 'app-origin');
const APP = process.env.APP_ORIGIN || (fs.existsSync(originFile) ? fs.readFileSync(originFile, 'utf8').trim() : '');
if (!APP) throw new Error('Set APP_ORIGIN or ~/.design-systems/kitchen/app-origin');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

function stopReason(url, text, frames) {
  const blob = `${url}\n${text}\n${frames}`;
  if (/checkout\.stripe\.com|js\.stripe\.com\/v3\/elements|billing\.stripe/i.test(blob)) return 'STRIPE';
  if (/recaptcha|hcaptcha|challenges\.cloudflare\.com\/turnstile|gstatic\.com\/recaptcha/i.test(blob)) return 'CAPTCHA';
  if (/verify your (phone|mobile)|enter (your )?(phone|mobile) number/i.test(text) && /tel/i.test(blob)) return 'PHONE';
  if (/\b(card number|cvc|expiry date|add a payment method)\b/i.test(text) && /stripe/i.test(blob)) return 'STRIPE';
  return null;
}

async function hideConsent(page) {
  await page.addStyleTag({
    content: [
      '#cookie-banner, #cookie-consent, .cookie-banner, .cookie-consent, .cookie-notice,',
      '.cc-window, .cc-banner, #onetrust-banner-sdk, [class*="cookie-bar"],',
      '[id*="cookie-consent"], [aria-label*="cookie" i], [class*="consent-banner"],',
      '.legal-docs-banner, [class*="Cookie"]',
      '{ display: none !important; visibility: hidden !important; pointer-events: none !important; }',
    ].join(''),
  }).catch(() => {});
  await page.evaluate(() => {
    const words = /cookie|consent|gdpr/i;
    for (const el of document.querySelectorAll('div, aside, section, dialog, footer')) {
      const t = (el.innerText || '').slice(0, 280);
      const r = el.getBoundingClientRect();
      if (words.test(t) && /accept|reject|allow/i.test(t) && r.height > 24 && r.height < 220) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

async function redactLive(page) {
  const redactPath = path.join(os.homedir(), '.design-systems', 'kitchen', 'live-redact.json');
  const pairs = fs.existsSync(redactPath) ? JSON.parse(fs.readFileSync(redactPath, 'utf8')) : [];
  await page.evaluate((pairs) => {
    const walk = (node) => {
      if (node.nodeType === 3) {
        let v = node.nodeValue;
        for (const [a, b] of pairs) v = v.split(a).join(b);
        if (v !== node.nodeValue) node.nodeValue = v;
      } else if (node.nodeType === 1 && node.tagName !== 'SCRIPT' && node.tagName !== 'STYLE') {
        for (const attr of ['placeholder', 'title', 'aria-label', 'alt']) {
          const cur = node.getAttribute?.(attr);
          if (!cur) continue;
          let next = cur;
          for (const [a, b] of pairs) next = next.split(a).join(b);
          if (next !== cur) node.setAttribute(attr, next);
        }
        if (node.placeholder) {
          let p = node.placeholder;
          for (const [a, b] of pairs) p = p.split(a).join(b);
          node.placeholder = p;
        }
        for (const c of node.childNodes) walk(c);
      }
    };
    walk(document.body);
    let title = document.title;
    for (const [a, b] of pairs) title = title.split(a).join(b);
    if (title !== document.title) document.title = title;
  }, pairs);
}

async function settle(page) {
  await wait(page, 1800);
  await hideConsent(page);
  await redactLive(page);
  await wait(page, 200);
}

function shooter(page, prefix, vw, vh, dpr) {
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  return {
    async view(name) {
      await redactLive(page);
      await screenshotWithMetadata(page, { path: `${RAW}/${prefix}-${name}.png` }, requested);
      log('  shot', prefix, name, page.url().replace(/https?:\/\//, ''));
    },
  };
}

async function pageInfo(page) {
  return page.evaluate(() => ({
    url: location.href,
    title: document.title,
    text: (document.body?.innerText || '').replace(/\s+/g, ' ').slice(0, 900),
    frames: [...document.querySelectorAll('iframe')].map((f) => f.src?.slice(0, 120)),
  }));
}

async function dismiss(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await wait(page, 250);
}

async function clickNav(page, text) {
  await dismiss(page);
  const rail = page.locator('button.nav__button', { hasText: new RegExp(`^${text}$`) }).first();
  if (await rail.count()) {
    await rail.click({ timeout: 8000 });
    return true;
  }
  const loc = page.getByRole('button', { name: text, exact: true }).first();
  if (await loc.count()) {
    await loc.click({ timeout: 8000 });
    return true;
  }
  return false;
}

async function clickText(page, text) {
  return clickNav(page, text);
}

const notes = [];
const ctx = await chromium.launchPersistentContext(PROFILE, {
  headless: true,
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = ctx.pages()[0] || await ctx.newPage();
page.setDefaultTimeout(12000);

try {
  await page.goto(APP + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await settle(page);
  let info = await pageInfo(page);
  let stop = stopReason(info.url, info.text, info.frames.join(' '));
  if (stop) {
    log('STOP', stop, info.url);
    const S = shooter(page, 'app-blocked-light', 1440, 900, 1);
    await S.view('default');
    fs.writeFileSync(path.join(RAW, 'app-stop.json'), JSON.stringify({ stop, info }, null, 2));
    process.exit(2);
  }
  if (!/kitchen\.co/i.test(info.url) || /login|get-started/i.test(info.url)) {
    log('NOT SIGNED IN', info.url, info.title);
    fs.writeFileSync(path.join(RAW, 'app-stop.json'), JSON.stringify({ stop: 'NOT_SIGNED_IN', info }, null, 2));
    process.exit(3);
  }
  log('in', info.url, info.title);

  const desk = shooter(page, 'app-home-light', 1440, 900, 1);
  await desk.view('default');

  const nav = [
    ['Inbox', 'app-inbox-light'],
    ['Proposals', 'app-proposals-light'],
    ['Clients', 'app-clients-light'],
    ['Tasks', 'app-tasks-light'],
  ];
  for (const [label, prefix] of nav) {
    try {
      const ok = await clickNav(page, label);
      await settle(page);
      info = await pageInfo(page);
      stop = stopReason(info.url, info.text, (info.frames || []).join(' '));
      log('nav', label, ok, info.url, stop || '');
      notes.push({ label, ok, url: info.url, title: info.title, stop, text: info.text.slice(0, 240) });
      if (stop) {
        await shooter(page, prefix, 1440, 900, 1).view('blocked');
        await dismiss(page);
        continue;
      }
      await shooter(page, prefix, 1440, 900, 1).view('default');
      if (label === 'Inbox') {
        for (const tab of ['Tasks', 'Files', 'Updates']) {
          const t = page.locator('.tree-view, [class*="inbox"], [class*="panel"]').locator(`text=${tab}`).first();
          try {
            if (await t.count()) {
              await t.click({ timeout: 4000 });
              await settle(page);
              await shooter(page, prefix, 1440, 900, 1).view('tab-' + tab.toLowerCase());
            }
          } catch (e) { log('  tab fail', tab, e.message.split('\n')[0]); }
        }
      }
      await dismiss(page);
    } catch (e) {
      log('nav fail', label, e.message.split('\n')[0]);
      notes.push({ label, error: e.message.split('\n')[0] });
      await dismiss(page);
    }
  }

  await clickNav(page, 'Home').catch(() => {});
  await settle(page);
  await shooter(page, 'app-home-light', 1440, 900, 1).view('default');

  try {
    const lib = page.locator('button.tree-view__button', { hasText: 'Library' }).first();
    if (await lib.count()) {
      await lib.click();
      await settle(page);
      await shooter(page, 'app-library-light', 1440, 900, 1).view('default');
      notes.push({ label: 'Library', url: page.url(), title: await page.title() });
    }
  } catch (e) { log('library fail', e.message.split('\n')[0]); }

  const more = await clickNav(page, 'More').catch(() => false);
  await wait(page, 800);
  await redactLive(page);
  await shooter(page, 'app-more-light', 1440, 900, 1).view('open');
  notes.push({ label: 'More', ok: more, url: page.url() });
  await dismiss(page);

  const settings = await clickNav(page, 'Settings').catch(() => false);
  await settle(page);
  info = await pageInfo(page);
  notes.push({ label: 'Settings', ok: settings, url: info.url, title: info.title, text: info.text.slice(0, 300) });
  await shooter(page, 'app-settings-light', 1440, 900, 1).view('default');

  await page.goto(APP + '/tasks/me', { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  await settle(page);
  await shooter(page, 'app-my-tasks-light', 1440, 900, 1).view('default');
  notes.push({ label: 'My Tasks', url: page.url(), title: await page.title() });

  await page.goto(APP + '/settings/branding/theme-and-colors', { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  await settle(page);
  info = await pageInfo(page);
  notes.push({ label: 'Theme', url: info.url, title: info.title, text: info.text.slice(0, 400) });
  await shooter(page, 'app-theme-light', 1440, 900, 1).view('default');

  await page.goto(APP + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await settle(page);
  const search = page.locator('input[placeholder*="Search" i], input[type="search"]').first();
  if (await search.count()) {
    await search.click();
    await wait(page, 400);
    await redactLive(page);
    await shooter(page, 'app-home-light', 1440, 900, 1).view('search-focus');
    await page.keyboard.press('Escape').catch(() => {});
  }
  const avatar = page.locator('button').filter({ hasText: /^AR$/ }).first();
  if (await avatar.count()) {
    await avatar.click();
    await wait(page, 700);
    await redactLive(page);
    await shooter(page, 'app-account-light', 1440, 900, 1).view('menu');
    await page.keyboard.press('Escape').catch(() => {});
  }

  const vars = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      for (const rule of rules) {
        if (!(rule instanceof CSSStyleRule)) continue;
        for (const n of rule.style) if (n.startsWith('--')) names.push(n);
      }
    }
    const uniq = [...new Set(names)];
    const declared = {};
    for (const n of uniq.slice(0, 400)) declared[n] = root.getPropertyValue(n).trim();
    return {
      colorScheme: root.colorScheme,
      rootBg: root.backgroundColor,
      bodyBg: body.backgroundColor,
      bodyColor: body.color,
      bodyFont: body.fontFamily,
      bodySize: body.fontSize,
      customPropertyCount: uniq.length,
      declared,
    };
  });
  fs.writeFileSync(path.join(os.homedir(), '.design-systems/kitchen/app-vars.json'), JSON.stringify(vars, null, 2));
  fs.writeFileSync(path.join(os.homedir(), '.design-systems/kitchen/app-notes.json'), JSON.stringify({ app: APP, notes, vars: { colorScheme: vars.colorScheme, customPropertyCount: vars.customPropertyCount, bodyBg: vars.bodyBg, bodyColor: vars.bodyColor, bodyFont: vars.bodyFont } }, null, 2));
  log('vars', vars.customPropertyCount, vars.bodyBg, vars.bodyFont);

  // The session's cookies and localStorage seed the mobile context in memory only: they are
  // never written to disk (an earlier run left them in ~/.design-systems/kitchen/storage-state.json,
  // which can be deleted).
  const state = await ctx.storageState();
  await ctx.close();

  const browser = await chromium.launch({ headless: true });
  const mctx = await browser.newContext({
    storageState: state,
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const mpage = await mctx.newPage();
  await mpage.goto(APP + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await settle(mpage);
  const mobile = shooter(mpage, 'mobile-app-home-light', 390, 844, 2);
  await mobile.view('default');
  for (const [label, prefix] of [['Inbox', 'mobile-app-inbox-light'], ['Tasks', 'mobile-app-tasks-light'], ['Settings', 'mobile-app-settings-light']]) {
    const ok = await clickText(mpage, label);
    await settle(mpage);
    log('mobile', label, ok, mpage.url());
    await shooter(mpage, prefix, 390, 844, 2).view('default');
  }
  await mctx.close();
  await browser.close();
  log('done');
} catch (e) {
  log('FAILED', e.message.split('\n')[0]);
  try { await ctx.close(); } catch {}
  process.exit(1);
}
