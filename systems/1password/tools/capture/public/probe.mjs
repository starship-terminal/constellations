// One-off selector probe for measure.mjs: prints the visible candidates for
// each component slot on the pages that file measures.
import { BASE, launch, open, closePromo, openFirstProduct } from './lib.mjs';

const { context, browser } = await launch();
const page = await context.newPage();
page.setDefaultTimeout(8000);

const dump = async (label, loc) => {
  const els = await loc.all();
  console.log(`--- ${label} (${els.length})`);
  for (const el of els.slice(0, 8)) {
    const i = await el.evaluate((n) => ({
      tag: n.tagName.toLowerCase(), cls: n.className.toString().slice(0, 90),
      id: n.id || '', text: (n.innerText || n.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
      vis: !!(n.offsetWidth && n.offsetHeight),
    })).catch(() => null);
    if (i) console.log('   ', JSON.stringify(i));
  }
};

// ---- home ----
await open(page, BASE + '/', { wait: 8000 });
await dump('promo bar', page.locator('[class*="announcement" i], [class*="promo-bar" i], [class*="top-bar" i], header [class*="marquee" i]').filter({ visible: true }));
await dump('header', page.locator('header').filter({ visible: true }));
await dump('nav buttons', page.locator('header a, header button').filter({ visible: true }));
await dump('hero CTAs', page.locator('a.btn, a.btn-primary, .btn-primary').filter({ visible: true }));
await dump('sections h2', page.locator('h1, h2').filter({ visible: true }));
await dump('cards', page.locator('[class*="card" i]').filter({ visible: true }));
await dump('footer', page.locator('footer').filter({ visible: true }));
await dump('chat chip', page.locator('[class*="chat" i], [id*="chat" i], [class*="ai-" i]').filter({ visible: true }));
await dump('geo dialog', page.locator('[id*="geofencing"]').filter({ visible: true }));
// search overlay
await page.getByRole('button', { name: /search/i }).filter({ visible: true }).first().click().catch(() => {});
await page.waitForTimeout(2000);
await dump('search overlay', page.locator('[role="dialog"], [class*="search" i]').filter({ visible: true }));
await page.keyboard.press('Escape');
await page.waitForTimeout(800);

// ---- pricing ----
await open(page, BASE + '/pricing', { wait: 6000 });
await dump('plan selector', page.locator('[class*="segment" i], [role="tab"]').filter({ visible: true }));
await dump('faq toggles', page.locator('button[aria-label^="Answer to"], button[aria-expanded]').filter({ visible: true }));
await page.evaluate(() => scrollTo(0, 1200));
await page.waitForTimeout(2500);
await dump('pricing ctas', page.locator('a, button').filter({ hasText: /get started|quote|try/i }).filter({ visible: true }));
await dump('price cards', page.locator('[class*="card" i], [class*="price" i]').filter({ visible: true }));

// ---- product ----
await open(page, BASE + '/product/enterprise-password-manager', { wait: 8000 });
await closePromo(page);
await dump('product title', page.locator('h1').filter({ visible: true }));
await dump('primary ctas', page.locator('a, button').filter({ hasText: /get started|free/i }).filter({ visible: true }));
await dump('accordion', page.locator('button[aria-expanded], details, summary, [class*="accordion" i]').filter({ visible: true }));
await dump('marketplace link', page.locator('a[href*="marketplace"]').filter({ visible: true }));
// feature cards on the product page
await dump('feature cards', page.locator('[class*="card" i], article, li:has(h3), section [class*="rounded"]').filter({ visible: true }));
await page.close();

await browser.close();
