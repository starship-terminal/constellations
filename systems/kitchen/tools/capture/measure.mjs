// Measures Kitchen.co components on public pages. Nothing is submitted or signed into.
// Hover is a real pointer. focus-visible is keyboard focus. pressed is CDP :active:hover.
// Filled types sample text and deletes it. Enter is never pressed.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, PAGES, RAW, chromium, UA, UA_MOBILE, hideConsent, styleOf, crop } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = {
  _meta: {
    product: 'Kitchen.co',
    read: new Date().toLocaleDateString('en-CA'),   // the local run date
    url: BASE,
    note: 'Public marketing surface. Login, signup, demo and Stripe checkout were not submitted.',
  },
  components: {},
};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

let page, cdp, current;

const browser = await chromium.launch();

async function withPage(key, fn, { mobile = false } = {}) {
  current = key;
  const vw = mobile ? 390 : 1440, vh = mobile ? 844 : 900;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: mobile ? 2 : 1,
    userAgent: mobile ? UA_MOBILE : UA,
    locale: 'en-US',
    isMobile: mobile,
    hasTouch: mobile,
  });
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = BASE + PAGES[key];
  log('open', key, url);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(1600);
  await hideConsent(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  try { await fn(); } catch (e) { log('  PAGE ERR', key, e.message.split('\n')[0]); }
  await ctx.close();
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4);
  await page.waitForTimeout(180);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
  }
  await page.waitForTimeout(250);
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(280);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, url: BASE + PAGES[current] }, meta);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.first();
  const c = out.components[key];
  try {
    if (!(await loc.count())) throw new Error('missing');
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 100));
  }
}

async function S(key, target, list, meta) {
  comp(key, meta);
  const loc = target.first();
  if (!(await loc.count())) {
    out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(150);
  for (const st of list) {
    // One failed state (a hover that times out, a click that misses) is recorded and the
    // rest of the component and page still run.
    try {
      await reset();
      if (st === 'default') await measure(key, st, loc, { via: 'rest' });
      else if (st === 'hover') {
        await loc.hover();
        await page.waitForTimeout(280);
        await measure(key, st, loc, { via: 'pointer hover' });
      } else if (st === 'focus-visible') {
        const how = await kbFocus(loc);
        await measure(key, st, loc, { via: how });
      } else if (st === 'pressed') {
        const undo = await forcePseudo(loc, ['hover', 'active']);
        await measure(key, st, loc, { via: 'CDP :hover:active' });
        await undo();
      } else if (st === 'focused') {
        await loc.click();
        await page.waitForTimeout(200);
        await measure(key, st, loc, { via: 'click into field, nothing submitted' });
      } else if (st === 'filled') {
        await loc.click();
        await loc.fill('studio@example.com');
        await page.waitForTimeout(150);
        await measure(key, st, loc, { via: 'sample text typed, then cleared' });
        await loc.fill('');
      }
    } catch (e) {
      log('  ! state failed', key, st, String(e.message || e).split('\n')[0]);
      const c = out.components[key] ??= { states: {} };
      (c.states ??= {})[st] = { error: String(e.message || e).split('\n')[0].slice(0, 180) };
    }
  }
}

const states = ['default', 'hover', 'focus-visible', 'pressed'];

await withPage('home', async () => {
  await S('promo-bar', page.locator('a.bar'), ['default', 'hover'], {
    title: 'Promo bar', group: 'Chrome', desc: 'The black campaign strip above the header.', sel: 'a.bar',
  });
  await S('logo', page.locator('a.logo.header__logo'), ['default'], {
    title: 'Wordmark', group: 'Chrome', desc: 'The Kitchen.co wordmark in the header.', sel: 'a.logo',
  });
  await S('nav-link', page.locator('nav.nav a[href*="/features"]'), states, {
    title: 'Nav link', group: 'Chrome', desc: 'A primary nav link.', sel: 'nav.nav a',
  });
  await S('nav-login', page.locator('a.btn.btn--small.is-outline'), states, {
    title: 'Log in button', group: 'Buttons', desc: 'The outline Log in control in the header.', sel: 'a.btn.is-outline',
  });
  await S('nav-try', page.locator('header a.btn.btn--small.btn--dark:not(.is-outline)'), states, {
    title: 'Try it free button', group: 'Buttons', desc: 'The filled ink button in the header.', sel: 'a.btn.btn--dark',
  });
  await S('hero-kicker', page.locator('section.hero h6').first(), ['default'], {
    title: 'Hero kicker', group: 'Type', desc: 'The small label above the home headline.', sel: 'section.hero h6',
  });
  await S('hero-title', page.locator('h1.hero__title').first(), ['default'], {
    title: 'Hero title', group: 'Type', desc: 'The home page headline.', sel: 'h1.hero__title',
  });
  await S('hero-body', page.locator('.hero__entry p').first(), ['default'], {
    title: 'Hero body', group: 'Type', desc: 'The paragraph under the home headline.', sel: '.hero__entry p',
  });
  await S('cta-coral', page.locator('a.btn').filter({ hasText: "Get Started" }).first(), states, {
    title: 'Coral call to action', group: 'Buttons', desc: 'The coral Get Started link on the home hero.', sel: 'a.btn (coral)',
  });
  await S('feature-card', page.locator('.card, .card-feature, .feature').first(), ['default'], {
    title: 'Feature card', group: 'Cards', desc: 'A feature card on the home page.', sel: '.card, .feature',
  });
  await S('footer', page.locator('footer.footer, .footer').first(), ['default'], {
    title: 'Footer', group: 'Chrome', desc: 'The site footer.', sel: 'footer.footer',
  });
  await S('footer-link', page.locator('footer a, .footer a').filter({ hasText: /Privacy|Terms|Blog/ }).first(), ['default', 'hover'], {
    title: 'Footer link', group: 'Links', desc: 'A link in the footer.', sel: 'footer a',
  });
  // solutions dropdown, hover only, no navigation
  const item = page.locator('li.has-dropdown').first();
  await item.hover();
  await page.waitForTimeout(400);
  await S('solutions-menu', page.locator('.dropdown').first(), ['default'], {
    title: 'Solutions menu', group: 'Menus', desc: 'The Solutions dropdown, opened by hover.', sel: '.dropdown',
  });
  await S('solutions-item', page.locator('.dropdown a').first(), ['default', 'hover'], {
    title: 'Solutions menu item', group: 'Menus', desc: 'One row in the Solutions dropdown.', sel: '.dropdown a',
  });
});

await withPage('pricing', async () => {
  await S('plan-card', page.locator('.plan').first(), ['default'], {
    title: 'Plan card', group: 'Cards', desc: 'A pricing plan card.', sel: '.plan',
  });
  await S('plan-price', page.locator('.plan__price').first(), ['default'], {
    title: 'Plan price', group: 'Type', desc: 'The price figure on a plan card.', sel: '.plan__price',
  });
  await S('plan-cta', page.locator('.plan a.btn').first(), states, {
    title: 'Plan call to action', group: 'Buttons', desc: 'The action on a plan card. The href was not followed.', sel: '.plan a.btn',
  });
  await S('plans-tab', page.locator('.plans-tabs__button').first(), ['default', 'hover', 'pressed'], {
    title: 'Plans tab', group: 'Tabs', desc: 'A billing-period tab on pricing.', sel: '.plans-tabs__button',
  });
  const head = page.locator('button.accordion__head').first();
  await S('faq-row', head, ['default', 'hover', 'focus-visible'], {
    title: 'FAQ row', group: 'Lists', desc: 'A closed pricing FAQ accordion row.', sel: 'button.accordion__head',
  });
  await head.click().catch(() => {});
  await page.waitForTimeout(400);
  await S('faq-row-open', page.locator('.accordion__section.is-open, .accordion__section').first(), ['default'], {
    title: 'FAQ row open', group: 'Lists', desc: 'A pricing FAQ row after its head was clicked. No form was submitted.', sel: '.accordion__section',
  });
  await S('badge', page.locator('.badge').first(), ['default'], {
    title: 'Badge', group: 'Badges', desc: 'A badge on the pricing page, when one paints.', sel: '.badge',
  });
});

await withPage('login', async () => {
  await S('login-field', page.locator('form input').first(), ['default', 'hover', 'focused', 'filled'], {
    title: 'Workspace field', group: 'Fields', desc: 'The login workspace field. Sample text was typed and cleared. Nothing was submitted.', sel: 'form input',
  });
  await S('login-submit', page.locator('form button, form a.btn, form .btn').first(), ['default', 'hover', 'focus-visible'], {
    title: 'Login continue', group: 'Buttons', desc: 'The login form action. It was not pressed.', sel: 'form .btn',
  });
  await S('login-label', page.locator('form label, .form__label').first(), ['default'], {
    title: 'Field label', group: 'Fields', desc: 'The label on the login form.', sel: 'form label',
  });
});

await withPage('get-started', async () => {
  await S('signup-field', page.locator('form input').first(), ['default', 'focused'], {
    title: 'Get started field', group: 'Fields', desc: 'The first field on Get started. Nothing was submitted.', sel: 'form input',
  });
});

await withPage('blog', async () => {
  await S('search-field', page.locator('.form-search__field, form input[type=search], form input').first(), ['default', 'focused'], {
    title: 'Blog search field', group: 'Fields', desc: 'The blog search field. Nothing was submitted.', sel: '.form-search__field',
  });
  await S('article-card', page.locator('article, .card').first(), ['default'], {
    title: 'Article card', group: 'Cards', desc: 'A blog article card.', sel: 'article',
  });
});

await withPage('reviews', async () => {
  await S('review-card', page.locator('.review').first(), ['default'], {
    title: 'Review card', group: 'Cards', desc: 'A customer review card.', sel: '.review',
  });
  await S('avatar', page.locator('.review__author-avatar, .review__author-avatar img').first(), ['default'], {
    title: 'Review avatar', group: 'Media', desc: 'The avatar on a review.', sel: '.review__author-avatar',
  });
});

await withPage('home', async () => {
  current = 'home';
  const btn = page.locator('a.header__nav-mobile').first();
  await S('menu-button', btn, ['default'], {
    title: 'Menu button', group: 'Mobile', desc: 'The phone Menu control.', sel: 'a.header__nav-mobile',
  });
  await btn.click().catch(() => {});
  await page.waitForTimeout(400);
  await S('mobile-drawer', page.locator('.header__content, .nav').first(), ['default'], {
    title: 'Mobile drawer', group: 'Mobile', desc: 'The phone nav after Menu is pressed. No destination was followed.', sel: '.header__content',
  });
  await S('mobile-nav-link', page.locator('.header__content a, .nav a').filter({ hasText: 'Pricing' }).first(), ['default'], {
    title: 'Mobile nav link', group: 'Mobile', desc: 'A link inside the opened phone nav.', sel: '.nav a',
  });
}, { mobile: true });

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
