// Photographs the public states named in systems/mailchimp/site-tree.md.
// Written after the tree, from the homepage map. Does not type, submit, or
// click an identity provider. Cookie and survey buttons are not pressed.
// Login and signup are opened only far enough to see the empty wall.
//
//   PLAYWRIGHT=... node site-tree.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, LOGIN_URL, SIGNUP_URL, patch, clearChallenge, closePromo } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const OUT = path.join(PKG, 'screenshots', 'site-tree');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mailchimp', 'site-tree-raw');
fs.mkdirSync(OUT, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function shot(page, name, requested) {
  const raw = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: raw }, requested);
  const dest = path.join(OUT, name + '.png');
  fs.copyFileSync(raw, dest);
  fs.copyFileSync(raw + '.capture.json', dest + '.capture.json');
  log('  shot', name);
}

async function openMenu(page, label) {
  const btn = page.locator('header button.iaNav__cta[aria-haspopup]').filter({ hasText: new RegExp(`^${label}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) { log('  ! no trigger', label); return false; }
  await btn.click({ timeout: 8000, force: true });
  await wait(page, 700);
  const expanded = await btn.getAttribute('aria-expanded');
  if (expanded !== 'true') { log('  ! not expanded', label, expanded); return false; }
  return true;
}

async function closeMenu(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await wait(page, 400);
}

const browser = await chromium.launch();

async function contextFor(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await patch(ctx);
  return { ctx, vw, vh, dpr };
}

// Desktop homepage: consent and survey still up, then each header menu.
{
  const { ctx, vw, vh, dpr } = await contextFor(false);
  const page = await ctx.newPage();
  const req = (url) => ({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: url });
  log('desktop home');
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) log('  BLOCKED home');
  else {
    await wait(page, 4000);
    await shot(page, 'desktop-home-consent', req(BASE + '/'));
    await shot(page, 'desktop-home-survey', req(BASE + '/'));
    // Hide the survey and the cookie banner so the menus can open. Hiding
    // never accepts, rejects, or submits. The shots above keep both visible.
    await closePromo(page);
    for (const [label, file] of [
      ['Industries and Solutions', 'desktop-menu-industries'],
      ['Integrations', 'desktop-menu-integrations'],
      ['Resources', 'desktop-menu-resources'],
    ]) {
      if (await openMenu(page, label)) {
        await shot(page, file, req(BASE + '/'));
        await closeMenu(page);
      }
    }
  }
  await ctx.close();
}

// Phone drawer. Main Menu only. Nested drawers are not walked into login.
{
  const { ctx, vw, vh, dpr } = await contextFor(true);
  const page = await ctx.newPage();
  const req = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: BASE + '/' };
  log('phone home');
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) log('  BLOCKED phone home');
  else {
    await wait(page, 4000);
    const ham = page.locator('button.iaNav__menuOpen, button[aria-label="Main Menu"]').filter({ visible: true }).first();
    await closePromo(page);
    if (await ham.count()) {
      await ham.click({ timeout: 8000, force: true });
      await wait(page, 900);
      await shot(page, 'phone-nav-drawer', req);
    } else log('  ! no Main Menu');
  }
  await ctx.close();
}

// Empty login and signup walls. Fields are cleared, never filled. No submit.
async function wall(url, name) {
  const { ctx, vw, vh, dpr } = await contextFor(false);
  const page = await ctx.newPage();
  const req = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: url.split('?')[0] };
  log(name);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) { log('  BLOCKED', name); await ctx.close(); return; }
  await wait(page, 4000);
  const body = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 500)).catch(() => '');
  const title = await page.title();
  log('  title', title);
  log('  body', body.replace(/\s+/g, ' ').slice(0, 240));
  const idp = /google|apple|facebook|microsoft|sso|identity/i.test(body);
  log('  identity-provider-text', idp);
  await page.locator('input').evaluateAll((els) => {
    for (const el of els) {
      if (el instanceof HTMLInputElement && (el.type === 'email' || el.type === 'text' || el.type === 'password' || el.type === 'tel')) el.value = '';
    }
  }).catch(() => {});
  await shot(page, name, req);
  await ctx.close();
}

await wall(LOGIN_URL, 'desktop-login-wall');
await wall(SIGNUP_URL, 'desktop-signup-wall');

{
  const { ctx, vw, vh, dpr } = await contextFor(true);
  const page = await ctx.newPage();
  const req = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: LOGIN_URL };
  log('phone-login-wall');
  await page.goto(LOGIN_URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) log('  BLOCKED phone login');
  else {
    await wait(page, 3000);
    await page.locator('input').evaluateAll((els) => {
      for (const el of els) {
        if (el instanceof HTMLInputElement) el.value = '';
      }
    }).catch(() => {});
    await shot(page, 'phone-login-wall', req);
  }
  await ctx.close();
}

await browser.close();
log('done', OUT);
