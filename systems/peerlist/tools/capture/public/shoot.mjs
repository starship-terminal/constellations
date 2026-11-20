// Capture Peerlist public pages. Writes full-colour PNGs under RAW (scratch),
// then the caller quantises them into systems/peerlist/screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Does not type, submit, or click Google.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { launchBrowser, newContext, open, isWall, dismissAuthDialog, BASE, REF } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'peerlist', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);

const PAGES = [
  { id: 'home', path: '/' },
  { id: 'scroll', path: '/scroll' },
  { id: 'scroll-trending', path: '/scroll/trending' },
  { id: 'jobs', path: '/jobs' },
  { id: 'jobs-role', path: '/jobs/role/software-engineer' },
  { id: 'launchpad', path: '/launchpad' },
  { id: 'launchpad-category', path: '/launchpad/category' },
  { id: 'ads', path: '/ads' },
  { id: 'blog', path: '/blog' },
  { id: 'blog-post', path: '/blog/design/designing-peerlist-darkmode' },
  { id: 'search', path: '/search' },
  { id: 'github-recap', path: '/github-recap' },
  { id: 'job-hunt-ai', path: '/job-hunt-ai' },
  { id: 'layoffs-tracker', path: '/layoffs-tracker' },
  { id: 'profile', path: '/kaiser' },
  { id: 'company', path: '/company/stripe' },
  { id: 'login-wall', path: '/login', wall: true },
  { id: 'signup-wall', path: '/signup', wall: true },
  { id: 'not-found', path: '/help' },
];

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', path.basename(file));
}

async function full(page, file, requested, dpr) {
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
  const vw = requested.viewport.width;
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log('  ! full truncated', H, '->', hCap);
  if (hCap <= chunk) {
    await screenshotWithMetadata(page, { path: file, fullPage: true }, requested);
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: file.replace(/\.png$/, `.part${i}.png`),
        fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      }, requested);
    }
  }
  log('  full', path.basename(file), 'H=' + H);
  await page.evaluate(() => scrollTo(0, 0));
}

async function setTheme(page, theme) {
  // Replace the class. Adding `dark` while `light` is still present paints black.
  await page.evaluate((theme) => {
    const root = document.documentElement;
    root.classList.remove('light', 'dark');
    root.classList.add(theme);
    root.style.colorScheme = theme;
  }, theme);
  await page.waitForTimeout(350);
  const got = await page.evaluate(() => document.documentElement.className);
  if (!got.split(/\s+/).includes(theme) || (theme === 'light' && got.split(/\s+/).includes('dark'))) {
    throw new Error('theme class not exclusive: ' + got);
  }
}

async function runWidth(browser, mobile) {
  const prefix = mobile ? 'mobile-' : '';
  const dpr = mobile ? 2 : 1;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const context = await newContext(browser, { mobile });
  const page = await context.newPage();
  const themes = mobile ? ['light'] : ['light', 'dark'];
  for (const spec of PAGES) {
    const name = prefix + spec.id;
    if (only.length && !only.some((o) => name.startsWith(o) || spec.id === o)) continue;
    log(name);
    const nav = await open(page, BASE + spec.path);
    if (!nav.ok) { log('  SKIP challenge', nav.title); continue; }
    if (!spec.wall && isWall(nav.url)) { log('  WALL redirect', nav.url); continue; }
    for (const theme of themes) {
      await setTheme(page, theme);
      const stem = `${RAW}/${name}-${theme}`;
      await shot(page, `${stem}-default.png`, { ...requested, sanitizedSourceUrl: BASE + spec.path });
      if (theme === 'light' && !mobile && ['home', 'scroll', 'jobs', 'launchpad', 'ads'].includes(spec.id)) {
        try { await full(page, `${stem}-full.png`, requested, dpr); }
        catch (e) { log('  full skipped', e.message.split('\n')[0]); }
      }
    }
    if (!mobile && spec.id === 'home') {
      await setTheme(page, 'light');
      await page.evaluate(() => {
        const b = [...document.querySelectorAll('button')].find((e) => (e.innerText || '').trim() === 'Play');
        if (b) b.click();
      });
      await page.waitForTimeout(1200);
      await shot(page, `${RAW}/${name}-light-play.png`, { ...requested, sanitizedSourceUrl: BASE + spec.path });
      await page.keyboard.press('Escape').catch(() => {});
    }
    if (!mobile && spec.id === 'scroll') {
      await setTheme(page, 'light');
      const post = page.getByRole('button', { name: 'Post', exact: true }).first();
      if (await post.count()) {
        await post.click().catch(() => {});
        await page.waitForTimeout(900);
        await shot(page, `${RAW}/${name}-light-login-dialog.png`, { ...requested, sanitizedSourceUrl: BASE + '/scroll' });
        await dismissAuthDialog(page);
      }
      const up = page.getByRole('button', { name: 'Upvote' }).first();
      if (await up.count()) {
        await up.hover().catch(() => {});
        await page.waitForTimeout(300);
        await shot(page, `${RAW}/${name}-light-upvote-hover.png`, { ...requested, sanitizedSourceUrl: BASE + '/scroll' });
      }
    }
    if (!mobile && spec.id === 'search') {
      await setTheme(page, 'light');
      const box = page.locator('input[type="search"]').first();
      if (await box.count()) {
        await box.focus();
        await page.waitForTimeout(250);
        await shot(page, `${RAW}/${name}-light-search-focus.png`, { ...requested, sanitizedSourceUrl: BASE + '/search' });
      }
    }
    if (!mobile && spec.id === 'ads') {
      await setTheme(page, 'light');
      const preview = page.getByRole('button', { name: /^Preview/ }).first();
      if (await preview.count()) {
        await preview.hover().catch(() => {});
        await page.waitForTimeout(250);
        await shot(page, `${RAW}/${name}-light-preview-hover.png`, { ...requested, sanitizedSourceUrl: BASE + '/ads' });
      }
    }
    if (!mobile && spec.id === 'jobs') {
      await setTheme(page, 'light');
      const row = page.locator('a[href*="/careers/"]').first();
      if (await row.count()) {
        await row.hover().catch(() => {});
        await page.waitForTimeout(250);
        await shot(page, `${RAW}/${name}-light-row-hover.png`, { ...requested, sanitizedSourceUrl: BASE + '/jobs' });
      }
    }
  }
  // phone menu on home
  if (mobile) {
    await open(page, BASE + '/');
    await setTheme(page, 'light');
    const burger = page.locator('button.lg\\:hidden').first();
    if (await burger.count() && await burger.isVisible().catch(() => false)) {
      await burger.click().catch(() => {});
      await page.waitForTimeout(500);
      await shot(page, `${RAW}/mobile-home-light-menu.png`, { ...requested, sanitizedSourceUrl: BASE + '/' });
    }
  }
  await context.close();
}

const browser = await launchBrowser();
try {
  await runWidth(browser, false);
  await runWidth(browser, true);
} finally {
  await browser.close();
}
log('done', RAW);
