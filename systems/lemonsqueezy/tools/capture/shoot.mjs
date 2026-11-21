// Public screenshots for Lemon Squeezy. Desktop 1440x900 at 1x, phone 390x844 at 2x.
// Does not type, submit, click an identity provider, or open checkout.
//
//   PLAYWRIGHT=... node tools/capture/shoot.mjs

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const only = new Set((process.argv[2] || '').split(',').filter(Boolean));

const browser = await chromium.launch({ headless: true });

async function shot(page, name, requested) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, requested);
  console.log('shot', name);
}

async function desktop() {
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const context = await browser.newContext({ ...requested, locale: 'en-US' });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);

  const pages = [
    ['home', 'https://www.lemonsqueezy.com/'],
    ['pricing', 'https://www.lemonsqueezy.com/pricing'],
    ['about', 'https://www.lemonsqueezy.com/about'],
    ['help', 'https://www.lemonsqueezy.com/help'],
    ['docs', 'https://docs.lemonsqueezy.com/'],
    ['goodbye', 'https://www.lemonsqueezy.com/blog/saying-goodbye-to-lemon-squeezy'],
    ['privacy', 'https://www.lemonsqueezy.com/privacy'],
    ['charge', 'https://www.lemonsqueezy.com/why-did-lemon-squeeezy-charge-me'],
  ];
  for (const [name, url] of pages) {
    if (only.size && !only.has(name)) continue;
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1400);
    await shot(page, `${name}-light-default`, requested);
  }

  if (!only.size || only.has('pricing-faq')) {
    await page.goto('https://www.lemonsqueezy.com/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1000);
    const faq = page.locator('.accordion_item').first();
    await faq.scrollIntoViewIfNeeded();
    await page.waitForTimeout(400);
    await shot(page, 'pricing-light-faq', requested);
  }

  if (!only.size || only.has('help-dialog')) {
    await page.goto('https://www.lemonsqueezy.com/help', { waitUntil: 'load', timeout: 45000 });
    await page.waitForTimeout(1500);
    const msg = page.locator('a').filter({ hasText: 'Message us' }).first();
    await msg.scrollIntoViewIfNeeded();
    await msg.click({ force: true });
    await page.waitForTimeout(1200);
    await shot(page, 'help-light-dialog', requested);
    await page.keyboard.press('Escape');
  }

  if (!only.size || only.has('login')) {
    await page.goto('https://app.lemonsqueezy.com/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1200);
    await shot(page, 'login-light-default', requested);
  }
  if (!only.size || only.has('register')) {
    await page.goto('https://auth.lemonsqueezy.com/register', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1000);
    await shot(page, 'register-light-default', requested);
  }
  if (!only.size || only.has('reset')) {
    await page.goto('https://auth.lemonsqueezy.com/password/reset', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1000);
    await shot(page, 'reset-light-default', requested);
  }
  if (!only.size || only.has('orders')) {
    await page.goto('https://app.lemonsqueezy.com/my-orders/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1800);
    await shot(page, 'my-orders-login-light-default', requested);
  }
  await context.close();
}

async function phone() {
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
  const context = await browser.newContext({
    ...requested,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  });
  const page = await context.newPage();
  await page.goto('https://www.lemonsqueezy.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1400);
  if (!only.size || only.has('mobile-home')) await shot(page, 'mobile-home-light-default', requested);
  if (!only.size || only.has('mobile-menu')) {
    await page.locator('.nav_menu-mobile-button, .w-nav-button').first().click();
    await page.waitForTimeout(700);
    await shot(page, 'mobile-home-light-menu', requested);
  }
  if (!only.size || only.has('mobile-pricing')) {
    await page.goto('https://www.lemonsqueezy.com/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(1200);
    await shot(page, 'mobile-pricing-light-default', requested);
  }
  await context.close();
}

await desktop();
await phone();
await browser.close();
console.log('raw', RAW);
