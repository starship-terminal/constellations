// Capture Resend's public site. Screenshots plus computed styles.
// Never types, never submits, never clicks Google or GitHub, never follows an auth wall.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node capture.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, launch, open, isAuthUrl, styleOf, quantizePng, REF, RAW } from './lib.mjs';

const RAW_SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'resend', 'raw-shots');
fs.mkdirSync(RAW_SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(REF, 'screenshots'), { recursive: true });
fs.mkdirSync(path.join(REF, 'components', 'crops'), { recursive: true });

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const SKIP = new Set((process.env.SKIP || '').split(',').filter(Boolean));
const ONLY = new Set((process.env.ONLY || '').split(',').filter(Boolean));
const PAGES = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['enterprise', '/enterprise'],
  ['features-email-api', '/features/email-api'],
  ['features-smtp', '/features/smtp-service'],
  ['features-inbound', '/features/inbound'],
  ['features-audiences', '/features/audiences'],
  ['features-broadcasts', '/features/broadcasts'],
  ['features-automations', '/features/automations'],
  ['features-templates', '/features/templates'],
  ['features-cli', '/features/cli'],
  ['features-webhooks', '/features/webhooks'],
  ['features-dedicated-ips', '/features/dedicated-ips'],
  ['product-inboxes', '/products/inboxes'],
  ['product-transactional', '/products/transactional-emails'],
  ['product-marketing', '/products/marketing-emails'],
  ['about', '/about'],
  ['blog', '/blog'],
  ['careers', '/careers'],
  ['customers', '/customers'],
  ['humans', '/humans'],
  ['handbook', '/handbook'],
  ['philosophy', '/philosophy'],
  ['security', '/security'],
  ['security-soc2', '/security/soc-2'],
  ['security-gdpr', '/security/gdpr'],
  ['support', '/support'],
  ['migrate', '/migrate'],
  ['changelog', '/changelog'],
  ['brand', '/brand'],
  ['clubs', '/clubs'],
  ['events', '/events'],
  ['insiders', '/insiders'],
  ['open-source', '/open-source'],
  ['wallpapers', '/wallpapers'],
  ['legal', '/legal'],
  ['forward', '/forward'],
  ['docs', '/docs/introduction'],
  ['docs-api', '/docs/api-reference'],
  ['docs-sdks', '/docs/sdks'],
  ['docs-webhooks', '/docs/webhooks/introduction'],
  ['docs-knowledge', '/docs/knowledge-base/introduction'],
  ['login', '/login'],
];

const PHONE_PAGES = ['home', 'pricing', 'docs', 'enterprise', 'blog', 'login'];

const walls = [];
const shots = [];

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 300);
}

async function shoot(page, name, vw, vh, dpr, { full = false } = {}) {
  const raw = path.join(RAW_SHOTS, name + '.png');
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  if (full) await lazyScroll(page);
  // Viewport captures only. fullPage height disagrees with documentSize on this
  // site, and the kit's dimension check rejects that mismatch. A "full" shot is
  // the viewport after a lazy scroll back to the top, so below-the-fold images
  // have loaded. The page's scrollHeight is recorded in the sidecar.
  await screenshotWithMetadata(page, { path: raw }, requested);
  const dest = path.join(REF, 'screenshots', name + '.png');
  quantizePng(raw, dest);
  shots.push(name);
  log('shot', name, full ? '(scrolled)' : '');
}

async function hoverMenu(page, name) {
  const btn = page.locator('header button').filter({ hasText: new RegExp('^' + name + '$') }).first();
  const box = await btn.boundingBox();
  if (!box) return false;
  await page.mouse.move(box.x + box.width / 2, box.y + 20);
  await wait(page, 450);
  return true;
}

async function readVars(page) {
  return page.evaluate(() => {
    const decls = [];
    const fonts = [];
    const errors = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        try {
          if (r.type === CSSRule.FONT_FACE_RULE) {
            const o = { file };
            for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();
            fonts.push(o);
            continue;
          }
          if (r.cssRules && !r.style) {
            const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
              : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
              : r.cssText.split('{')[0].trim().slice(0, 120);
            walk(r.cssRules, [...ctx, head], file);
            continue;
          }
          if (!r.style) continue;
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim().slice(0, 400);
          }
          if (Object.keys(props).length) decls.push({ file, selector: (r.selectorText || '').slice(0, 200), context: ctx, properties: props });
        } catch (e) { errors.push(String(e).slice(0, 120)); }
      }
    };
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch (e) { errors.push('unreadable ' + (sheet.href || 'inline')); continue; }
      walk(rules, [], sheet.href || 'inline');
    }
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const d of decls) for (const k of Object.keys(d.properties)) names.add(k);
    const resolved = {};
    for (const n of names) {
      const v = root.getPropertyValue(n).trim();
      if (v) resolved[n] = v.slice(0, 400);
    }
    return {
      decls, fonts, errors, resolved,
      htmlClass: document.documentElement.className.slice(0, 200),
      colorScheme: root.colorScheme,
    };
  });
}

async function measureComponents(page, theme) {
  const specs = [
    ['button-primary', 'header a', /get started/i],
    ['button-secondary', 'header a', /log in/i],
    ['link-nav', 'header a', /pricing/i],
    ['nav-trigger', 'header button', /^Features$/],
  ];
  const out = {};
  for (const [key, sel, re] of specs) {
    const loc = page.locator(sel).filter({ hasText: re }).first();
    if (!(await loc.count())) { out[key] = { missing: true }; continue; }
    try {
      const box = await loc.boundingBox();
      if (!box || box.width < 2) { out[key] = { missing: true }; continue; }
      out[key] = { default: await styleOf(loc), theme };
      await loc.hover({ timeout: 2000 }).catch(() => {});
      await wait(page, 250);
      out[key].hover = await styleOf(loc);
      await page.mouse.move(2, 2);
    } catch (e) {
      out[key] = { error: String(e.message).split('\n')[0] };
    }
  }
  // text field on login is observed, never typed
  return out;
}

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 1 });
const page = await context.newPage();

const varPages = {};
for (const [name, pathn] of PAGES) {
  if (SKIP.has(name) || (ONLY.size && !ONLY.has(name))) continue;
  log('page', name, pathn);
  let landed;
  try {
    landed = await open(page, BASE + pathn, { wait: 1600 });
  } catch (e) {
    log('  FAIL', e.message.split('\n')[0]);
    walls.push({ name, path: pathn, error: e.message.split('\n')[0] });
    continue;
  }
  if (landed.authWall && name !== 'login') {
    walls.push({ name, path: pathn, url: landed.url, action: 'stopped, auth wall' });
    log('  AUTH', landed.url);
    continue;
  }
  if (name === 'login') {
    walls.push({ name, path: pathn, url: landed.url, action: 'observed only; did not type; did not click Google or GitHub' });
  }
  const theme = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  await shoot(page, `${name}-${theme}-default`, 1440, 900, 1);
  if (['home', 'pricing', 'docs', 'enterprise', 'blog', 'features-email-api', 'customers', 'changelog'].includes(name)) {
    await shoot(page, `${name}-${theme}-full`, 1440, 900, 1, { full: true });
  }
  if (name === 'home' || name === 'docs' || name === 'pricing') {
    varPages[name] = await readVars(page);
    log('  vars', Object.keys(varPages[name].resolved).length, 'decls', varPages[name].decls.length);
  }
}

// home interactions
await open(page, BASE + '/');
const homeTheme = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
const homeComps = await measureComponents(page, homeTheme);
if (await hoverMenu(page, 'Features')) {
  await shoot(page, `home-${homeTheme}-features-menu`, 1440, 900, 1);
}
await page.mouse.move(8, 700);
await wait(page, 200);
if (await hoverMenu(page, 'Company')) {
  await shoot(page, `home-${homeTheme}-company-menu`, 1440, 900, 1);
}
await page.mouse.move(8, 700);
await wait(page, 200);
if (await hoverMenu(page, 'AI')) {
  await shoot(page, `home-${homeTheme}-ai-menu`, 1440, 900, 1);
}
await page.mouse.move(8, 700);
await wait(page, 200);
if (await hoverMenu(page, 'Docs')) {
  await shoot(page, `home-${homeTheme}-docs-menu`, 1440, 900, 1);
}
await page.mouse.move(8, 700);

// pricing marketing tab
await open(page, BASE + '/pricing');
const pTheme = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
const tab = page.getByRole('tab', { name: 'Marketing emails' });
if (await tab.count()) {
  await tab.click();
  await wait(page, 500);
  await shoot(page, `pricing-${pTheme}-marketing-tab`, 1440, 900, 1);
}

// docs theme switch + search, no submit
await open(page, BASE + '/docs/introduction');
const lightBtn = page.getByRole('button', { name: 'Switch to light theme' });
if (await lightBtn.count()) {
  await lightBtn.click();
  await wait(page, 600);
  const t = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  await shoot(page, `docs-${t}-theme`, 1440, 900, 1);
  varPages.docsLight = await readVars(page);
  log('  docs light vars', Object.keys(varPages.docsLight.resolved).length);
}
const search = page.getByRole('button', { name: /search/i }).first();
if (await search.count()) {
  await search.click();
  await wait(page, 500);
  const t = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  await shoot(page, `docs-${t}-search`, 1440, 900, 1);
  await page.keyboard.press('Escape');
}

// sidebar group
const sending = page.getByRole('button', { name: 'Sending', exact: true }).first();
if (await sending.count()) {
  await sending.click().catch(() => {});
  await wait(page, 400);
  const t = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  await shoot(page, `docs-${t}-sidebar-sending`, 1440, 900, 1);
}

await context.close();

// phone
const mob = await launch({ mobile: true, dpr: 2 });
const mp = await mob.context.newPage();
for (const name of PHONE_PAGES) {
  const pathn = PAGES.find((p) => p[0] === name)[1];
  log('phone', name);
  let landed;
  try { landed = await open(mp, BASE + pathn, { wait: 1400 }); }
  catch (e) { log('  FAIL', e.message.split('\n')[0]); continue; }
  if (landed.authWall && name !== 'login') {
    walls.push({ name: 'mobile-' + name, path: pathn, url: landed.url, action: 'stopped, auth wall' });
    continue;
  }
  const theme = await mp.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  await shoot(mp, `mobile-${name}-${theme}-default`, 390, 844, 2);
  if (name === 'home' || name === 'pricing') await shoot(mp, `mobile-${name}-${theme}-full`, 390, 844, 2, { full: true });
}
await open(mp, BASE + '/');
const mTheme = await mp.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
const menu = mp.locator('button[aria-label="menu"]');
if (await menu.count()) {
  await menu.click();
  await wait(mp, 600);
  await shoot(mp, `mobile-home-${mTheme}-menu`, 390, 844, 2);
}
await mob.context.close();
await browser.close();
await mob.browser.close();

const evidence = {
  capturedAt: new Date().toISOString(),
  viewport: { desktop: { width: 1440, height: 900, dpr: 1 }, phone: { width: 390, height: 844, dpr: 2 } },
  walls,
  shots,
  varCounts: Object.fromEntries(Object.entries(varPages).map(([k, v]) => [k, { resolved: Object.keys(v.resolved).length, decls: v.decls.length, htmlClass: v.htmlClass, colorScheme: v.colorScheme }])),
  homeComponents: homeComps,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  source: 'live CSSOM on resend.com, 2026-11-21, signed out',
  pages: Object.fromEntries(Object.entries(varPages).map(([k, v]) => [k, { resolved: v.resolved, htmlClass: v.htmlClass, colorScheme: v.colorScheme, declCount: v.decls.length, errors: v.errors }])),
  decls: varPages.home?.decls || varPages.docs?.decls || [],
  docsDecls: varPages.docs?.decls || [],
  docsLightDecls: varPages.docsLight?.decls || [],
  fonts: varPages.home?.fonts || [],
}, null, 1));
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(homeComps, null, 1));
fs.writeFileSync(path.join(RAW, 'capture-manifest.json'), JSON.stringify(evidence, null, 1));
log('done', shots.length, 'shots', walls.length, 'walls');
