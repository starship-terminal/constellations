// Photographs every public bezi.com page and overlay named in site-tree.md.
//
//   RAW=~/.design-systems/bezi/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/site-tree.mjs
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Viewport shots only, so a
// tall page never tiles without bound. Nothing is typed, submitted, or
// downloaded. A control that opens app.bezi.com is recorded and not clicked.
import fs from 'node:fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems/bezi/raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const MARKETING = [
  ['home', '/'],
  ['studios', '/studios'],
  ['product', '/product'],
  ['pricing', '/pricing'],
  ['pricing-studio', '/pricing/studio'],
  ['blog', '/blog'],
  ['unreal', '/unreal'],
  ['book-demo', '/book-demo'],
  ['careers', '/careers'],
  ['careers-product-design-lead', '/careers/product-design-lead'],
  ['careers-opportunistic', '/careers/opportunistic'],
  ['security', '/security'],
  ['privacy-policy', '/privacy-policy'],
  ['copyright-policy', '/copyright-policy'],
  ['terms-of-service', '/terms-of-service'],
  ['subprocessors', '/subprocessors'],
  ['proofs', '/proofs'],
  ['partnerships-thomasbrush', '/partnerships/thomasbrush'],
  ['partnerships-sonderingemily', '/partnerships/sonderingemily'],
  ['partnerships-bitemegames', '/partnerships/bitemegames'],
  ['partnerships-lazyteastudios', '/partnerships/lazyteastudios'],
];

const SITEMAP_ONLY = [
  'the-indie-renaissance-how-small-teams-are-reinventing-player-interaction',
  'secure-design-journey',
  'bezi-raises-13m-led-by-benchmark-to-empower-3d-designers',
  'introducing-bezi-ai',
  '3d-performance',
  'rtfkt-x-bezi-design-challenge-winner-an-interview-with-marcus-graber',
  'designing-for-new-realities-in-the-age-of-spatial-computing-and-ai',
  'bezel-is-now-bezi',
  'designer-3d-project-workflow',
  'human-centered-design-bezel',
  'how-to-design-for-reality',
  'designing-for-ar-google-lens',
  'real-time-collaboration-in-a-3d-design-tool',
  'why-we-built-the-command-center',
  'introducing-bezel',
];

const tree = {
  capturedAt: new Date().toISOString(),
  start: 'https://www.bezi.com/',
  widths: { desktop: { width: 1440, height: 900, dpr: 1 }, phone: { width: 390, height: 844, dpr: 2 } },
  stopped: [],
  shots: [],
};

async function shot(page, name, requested) {
  const file = path.join(RAW, `${name}.png`);
  await screenshotWithMetadata(page, { path: file }, {
    ...requested,
    sanitizedSourceUrl: new URL(page.url()).origin + new URL(page.url()).pathname,
  });
  const dims = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
  }));
  tree.shots.push({ name, url: new URL(page.url()).origin + new URL(page.url()).pathname, ...dims });
  log('shot', name, dims.innerWidth + 'x' + dims.innerHeight);
}

async function settle(page) {
  await page.waitForTimeout(3500);
  const title = await page.title();
  const body = await page.evaluate(() => (document.body?.innerText || '').slice(0, 180));
  const blocked = /just a moment|verify you are human|performing security verification/i.test(title + body);
  return { title, blocked, url: page.url() };
}

async function openMobileMenu(page) {
  return page.evaluate(() => {
    const nodes = [...document.querySelectorAll('div')].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.x > 280 && r.y < 80 && r.width >= 12 && r.width <= 20 && r.height >= 12 && r.height <= 20
        && getComputedStyle(n).cursor === 'pointer';
    });
    const el = nodes.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0];
    if (!el) return false;
    el.click();
    return true;
  });
}

async function clickText(page, label, { tag = '*' } = {}) {
  return page.evaluate(([label, tag]) => {
    const nodes = [...document.querySelectorAll(tag)].filter((n) => {
      const t = (n.innerText || n.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim();
      const r = n.getBoundingClientRect();
      return t === label && r.width > 8 && r.height > 8 && r.y > -20 && r.y < 900;
    });
    const el = nodes.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0];
    if (!el) return false;
    el.scrollIntoView({ block: 'center' });
    el.click();
    return true;
  }, [label, tag]);
}

const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  return ctx;
}

for (const mobile of [false, true]) {
  const prefix = mobile ? 'mobile-' : '';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const ctx = await contextFor(mobile);
  const page = await ctx.newPage();

  for (const [name, route] of MARKETING) {
    try {
      await page.goto('https://www.bezi.com' + route, { waitUntil: 'domcontentloaded', timeout: 90000 });
      const s = await settle(page);
      if (s.blocked) { log('BLOCKED', route); tree.stopped.push({ route, reason: 'challenge' }); continue; }
      if (new URL(s.url).hostname === 'app.bezi.com') {
        tree.stopped.push({ route, url: s.url, reason: 'login wall' });
        continue;
      }
      await shot(page, `${prefix}${name}-dark-default`, requested);
    } catch (e) {
      log('FAIL', name, e.message.split('\n')[0]);
    }
  }

  // Blog articles linked from the index, then sitemap-only paths.
  try {
    await page.goto('https://www.bezi.com/blog', { waitUntil: 'domcontentloaded', timeout: 90000 });
    await settle(page);
    const slugs = await page.evaluate(() => [...new Set([...document.querySelectorAll('a')].map((a) => a.pathname).filter((p) => p.startsWith('/blog/') && p.length > 6))]);
    log('blog slugs', slugs.length);
    for (const slug of slugs) {
      const name = 'blog-' + slug.replace('/blog/', '').slice(0, 48);
      await page.goto('https://www.bezi.com' + slug, { waitUntil: 'domcontentloaded', timeout: 90000 });
      const s = await settle(page);
      if (s.blocked || new URL(s.url).hostname === 'app.bezi.com') continue;
      await shot(page, `${prefix}${name}-dark-default`, requested);
    }
  } catch (e) { log('FAIL blog index', e.message.split('\n')[0]); }

  for (const slug of SITEMAP_ONLY) {
    try {
      await page.goto('https://www.bezi.com/blog/' + slug, { waitUntil: 'domcontentloaded', timeout: 90000 });
      const s = await settle(page);
      if (s.blocked) continue;
      await shot(page, `${prefix}blog-${slug.slice(0, 48)}-dark-default`, requested);
    } catch (e) { log('FAIL', slug, e.message.split('\n')[0]); }
  }

  // Interactions that stay on the marketing site.
  try {
    await page.goto('https://www.bezi.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
    await settle(page);
    if (mobile) {
      if (await openMobileMenu(page)) {
        await page.waitForTimeout(900);
        await shot(page, 'mobile-home-dark-menu-open', requested);
      } else log('mobile menu trigger missing');
    } else {
      await page.evaluate(() => document.querySelector('button')?.scrollIntoView({ block: 'center' }));
      if (await clickText(page, '02CONNECTED TOOLS', { tag: 'button' }) || await page.evaluate(() => {
        const b = [...document.querySelectorAll('button')].find((n) => (n.innerText || '').includes('02'));
        if (!b) return false;
        b.scrollIntoView({ block: 'center' });
        b.click();
        return true;
      })) {
        await page.waitForTimeout(700);
        await shot(page, 'home-dark-chip-02', requested);
      }
      await page.evaluate(() => document.getElementById('download-bezi')?.scrollIntoView({ block: 'center' }));
      await page.waitForTimeout(600);
      await shot(page, 'home-dark-download-anchor', requested);
    }
  } catch (e) { log('FAIL home interactions', e.message.split('\n')[0]); }

  if (!mobile) {
    try {
      await page.goto('https://www.bezi.com/product', { waitUntil: 'domcontentloaded', timeout: 90000 });
      await settle(page);
      await page.evaluate(() => {
        const el = [...document.querySelectorAll('[role="button"]')].find((n) => (n.innerText || '').includes('Knowledge Base'));
        if (el) { el.scrollIntoView({ block: 'center' }); el.click(); }
      });
      await page.waitForTimeout(700);
      await shot(page, 'product-dark-knowledge-base', requested);
      await page.evaluate(() => {
        const el = [...document.querySelectorAll('button')].find((n) => (n.innerText || '').trim() === 'Animation');
        if (el) { el.scrollIntoView({ block: 'center' }); el.click(); }
      });
      await page.waitForTimeout(700);
      await shot(page, 'product-dark-tab-animation', requested);
    } catch (e) { log('FAIL product', e.message.split('\n')[0]); }

    try {
      await page.goto('https://www.bezi.com/pricing', { waitUntil: 'domcontentloaded', timeout: 90000 });
      await settle(page);
      await page.evaluate(() => {
        const a = [...document.querySelectorAll('a')].find((n) => /TRY FOR FREE/i.test(n.getAttribute('aria-label') || n.innerText || '') && !n.getAttribute('href'));
        if (a) { a.scrollIntoView({ block: 'center' }); a.click(); }
      });
      await page.waitForTimeout(800);
      await shot(page, 'pricing-dark-download-menu', requested);
      tree.stopped.push({
        control: 'pricing download menu items',
        reason: 'desktop app download; menu photographed, items not activated',
      });
    } catch (e) { log('FAIL pricing menu', e.message.split('\n')[0]); }

    try {
      await page.goto('https://www.bezi.com/blog', { waitUntil: 'domcontentloaded', timeout: 90000 });
      await settle(page);
      await page.evaluate(() => {
        const b = [...document.querySelectorAll('button')].find((n) => (n.innerText || '').trim() === 'Editorial');
        if (b) b.click();
      });
      await page.waitForTimeout(700);
      await shot(page, 'blog-dark-filter-editorial', requested);
    } catch (e) { log('FAIL blog filter', e.message.split('\n')[0]); }

    try {
      await page.goto('https://www.bezi.com/unreal', { waitUntil: 'domcontentloaded', timeout: 90000 });
      await settle(page);
      await page.evaluate(() => {
        const el = [...document.querySelectorAll('div')].find((n) => (n.innerText || '').trim() === 'Which Unreal versions does it support?' && getComputedStyle(n).cursor === 'pointer');
        if (el) { el.scrollIntoView({ block: 'center' }); el.click(); }
      });
      await page.waitForTimeout(700);
      await shot(page, 'unreal-dark-faq-open', requested);
    } catch (e) { log('FAIL faq', e.message.split('\n')[0]); }
  }

  await ctx.close();
}

tree.stopped.push({
  control: 'Sign up / Select plan',
  url: 'https://app.bezi.com/start',
  reason: 'login wall recorded from a prior probe; not clicked in this run',
});
tree.stopped.push({
  control: 'Book a demo form',
  url: 'https://www.bezi.com/book-demo',
  reason: 'form photographed empty; not filled, not submitted',
});

fs.writeFileSync(path.join(RAW, 'site-tree-capture.json'), JSON.stringify(tree, null, 2) + '\n');
log('done', tree.shots.length, 'shots');
await browser.close();
