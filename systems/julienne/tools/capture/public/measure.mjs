// Measures withjulienne.com's signed-out components at 1440 and writes
// raw/components-computed.json plus components/crops/.
//
//   PLAYWRIGHT=... node measure.mjs [name,name]
//
// Auth, Save, Cook, Buy and search submit are never pressed. Dark readings
// use the header's own Toggle theme control.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, RECIPE, COLLECTION, launch, open as openPage, styleOf, crop, setTheme, RAW } from './lib.mjs';
// open() returns false on a blocked load and leaves the tab on about:blank;
// every reading here runs inside run(), so throwing records it as failed
// instead of measuring the blank tab as the product (2026-11 audit, 20-4)
const open = async (page, url, opts) => { if (!(await openPage(page, url, opts))) throw new Error(`BLOCKED ${url}: the page never loaded, nothing measured`); };

const only = (process.argv[2] || '').split(',').filter(Boolean);
const priorPath = path.join(RAW, 'components-computed.json');
const prior = fs.existsSync(priorPath) ? JSON.parse(fs.readFileSync(priorPath, 'utf8')) : {};
const out = { readAt: new Date().toLocaleDateString('en-CA'), source: 'computed styles on live signed-out withjulienne.com, 1440x900, light (boot) and dark (Toggle theme)', components: { ...(prior.components || {}) } };
fs.mkdirSync(RAW, { recursive: true });
const { browser, context } = await launch();
const p = await context.newPage();

async function run(name, fn) {
  if (only.length && !only.includes(name)) return;
  try {
    out.components[name] = await fn();
    console.log('ok', name);
  } catch (e) {
    out.components[name] = { error: String(e).split('\n')[0] };
    console.log('FAIL', name, out.components[name].error);
  }
}

function pack(reading, cropPath) {
  if (!reading || reading.missing) return { missing: true };
  return { style: reading.style, rect: reading.rect, classes: reading.classes, text: reading.text, tag: reading.tag, htmlClass: reading.htmlClass, placeholder: reading.placeholder, icon: reading.icon, crop: cropPath || null };
}

await run('header', async () => {
  await open(p, BASE + '/');
  const header = p.locator('header.site-header').first();
  const logo = p.locator('header a[href="/"]').first();
  const discover = p.locator('header a[href="/discover"]').first();
  const login = p.getByRole('button', { name: 'Log in', exact: true }).first();
  const toggle = p.getByRole('button', { name: 'Toggle theme' }).first();
  const search = p.locator('input[placeholder="Search all recipes"]').first();
  const glass = p.locator('header .glass').first();
  return {
    states: {
      header: pack(await styleOf(header), await crop(p, header, 'header-default')),
      logo: pack(await styleOf(logo), await crop(p, logo, 'logo-default')),
      navLink: pack(await styleOf(discover), await crop(p, discover, 'nav-link-default')),
      login: pack(await styleOf(login), await crop(p, login, 'login-button-default')),
      themeToggle: pack(await styleOf(toggle), await crop(p, toggle, 'theme-toggle-default')),
      search: pack(await styleOf(search), await crop(p, search, 'search-field-default')),
      searchGlass: pack(await styleOf(glass), await crop(p, glass, 'search-glass-default')),
    },
  };
});

await run('header-dark', async () => {
  await open(p, BASE + '/', { theme: 'dark' });
  const header = p.locator('header.site-header').first();
  const login = p.getByRole('button', { name: 'Log in', exact: true }).first();
  const glass = p.locator('header .glass').first();
  const h1 = p.locator('h1').first();
  return {
    states: {
      header: pack(await styleOf(header)),
      login: pack(await styleOf(login), await crop(p, login, 'login-button-dark')),
      searchGlass: pack(await styleOf(glass), await crop(p, glass, 'search-glass-dark')),
      h1: pack(await styleOf(h1)),
      page: pack(await styleOf(p.locator('body'))),
    },
  };
});

await run('hero', async () => {
  await open(p, BASE + '/');
  const h1 = p.locator('h1').first();
  const cta = p.getByRole('link', { name: /Get the app/i }).first();
  const more = p.getByRole('button', { name: /See more recipes/i }).first();
  return {
    states: {
      h1: pack(await styleOf(h1), await crop(p, h1, 'hero-title-default')),
      cta: pack(await styleOf(cta), await crop(p, cta, 'hero-cta-default')),
      more: pack(await styleOf(more), await crop(p, more, 'see-more-default')),
    },
  };
});

await run('recipe-card', async () => {
  await open(p, BASE + '/');
  const card = p.locator('a[href*="/recipes/"]').first();
  const save = p.getByRole('button', { name: /^Save / }).first();
  const time = card.locator('text=/Total Time/').first();
  return {
    states: {
      card: pack(await styleOf(card), await crop(p, card, 'recipe-card-default')),
      title: pack(await styleOf(card.locator('h2, h3, p').first())),
      save: pack(await styleOf(save), await crop(p, save, 'save-button-default')),
      meta: pack(await styleOf(time)),
    },
  };
});

await run('discover-chips', async () => {
  await open(p, BASE + '/discover');
  const breakfast = p.locator('button.rounded-full, a.rounded-full').filter({ hasText: /^Breakfast$/ }).first();
  const resting = await styleOf(breakfast);
  const restCrop = await crop(p, breakfast, 'chip-default');
  await breakfast.click();
  await p.waitForTimeout(700);
  const after = await styleOf(breakfast);
  return {
    states: {
      chip: { ...pack(resting, restCrop), note: 'Breakfast filter at rest, before it is selected' },
      chipSelected: { ...pack(after, await crop(p, breakfast, 'chip-selected-default')), note: 'Breakfast after its own click; a local filter toggle, not a search submit' },
      browseAll: pack(await styleOf(p.locator('button').filter({ hasText: /^Browse all$/ }).first())),
    },
  };
});

await run('search-focus', async () => {
  await open(p, BASE + '/');
  const input = p.locator('input[placeholder="Search all recipes"]').first();
  await input.focus();
  await p.waitForTimeout(200);
  const glass = p.locator('header .glass').first();
  const focused = await styleOf(input);
  const glassFocus = await styleOf(glass);
  // outline on the focused node and its glass shell
  const ring = await p.evaluate(() => {
    const el = document.activeElement;
    const chain = [];
    for (let n = el, i = 0; n && i < 5; n = n.parentElement, i++) {
      const s = getComputedStyle(n);
      chain.push({
        tag: n.tagName, cls: String(n.className).slice(0, 80),
        outline: `${s.outlineWidth} ${s.outlineStyle} ${s.outlineColor} offset ${s.outlineOffset}`,
        shadow: s.boxShadow === 'none' ? '' : s.boxShadow.slice(0, 180),
        border: s.borderTopColor,
      });
    }
    return { active: document.activeElement?.tagName, chain };
  });
  return { states: { input: pack(focused, await crop(p, glass, 'search-field-focus')), glass: pack(glassFocus) }, ring };
});

await run('auth-rest', async () => {
  // Open the signup page and read the form at rest. Do not type or submit.
  await open(p, BASE + '/signup', { wait: 3500 });
  const email = p.locator('input[type="email"]').first();
  const password = p.locator('input[type="password"]').first();
  const create = p.getByRole('button', { name: /Create account/i }).first();
  const google = p.getByRole('button', { name: 'Google' }).first();
  const apple = p.getByRole('button', { name: 'Apple' }).first();
  const terms = p.getByRole('link', { name: /Terms of Service/i }).first();
  const signin = p.getByRole('link', { name: /Sign in/i }).first();
  const card = p.locator('form').filter({ hasText: /password/i }).first();
  return {
    boundary: 'signup form at rest; nothing typed or submitted; Google, Apple and Turnstile never used',
    states: {
      email: pack(await styleOf(email), await crop(p, email, 'auth-email-default')),
      password: pack(await styleOf(password), await crop(p, password, 'auth-password-default')),
      create: pack(await styleOf(create), await crop(p, create, 'auth-create-default')),
      google: pack(await styleOf(google), await crop(p, google, 'auth-google-default')),
      apple: pack(await styleOf(apple)),
      termsLink: pack(await styleOf(terms)),
      signInLink: pack(await styleOf(signin)),
      form: pack(await styleOf(card), await crop(p, card, 'auth-form-default')),
    },
  };
});

await run('login-dialog', async () => {
  await open(p, BASE + '/');
  const login = p.getByRole('button', { name: 'Log in', exact: true }).first();
  await login.click();
  await p.waitForTimeout(900);
  const email = p.locator('input[aria-label="Email"], input[placeholder="Email"]').first();
  const dialogish = p.locator('form').filter({ hasText: /password/i }).first();
  const reading = await styleOf(dialogish);
  const shot = await crop(p, dialogish, 'login-dialog-default');
  await p.keyboard.press('Escape');
  return {
    boundary: 'Log in dialog opened and read at rest; fields never typed, submit never pressed',
    states: { form: { ...pack(reading, shot) }, email: pack(await styleOf(email)) },
  };
});

await run('recipe', async () => {
  await open(p, BASE + RECIPE, { wait: 2500 });
  const h1 = p.locator('h1').first();
  const cook = p.getByRole('button', { name: 'Cook', exact: true }).first();
  const save = p.getByRole('button', { name: 'Save', exact: true }).first();
  const ingredient = p.locator('text=/Olive Oil|Mushrooms|Leeks/').first();
  const body = p.locator('main p, article p, p').filter({ hasText: /French-inspired|creamy/i }).first();
  return {
    states: {
      title: pack(await styleOf(h1), await crop(p, h1, 'recipe-title-default')),
      cook: pack(await styleOf(cook), await crop(p, cook, 'cook-button-default')),
      save: pack(await styleOf(save), await crop(p, save, 'recipe-save-default')),
      ingredient: pack(await styleOf(ingredient)),
      body: pack(await styleOf(body)),
    },
  };
});

await run('ingredient-chip', async () => {
  await open(p, BASE + '/');
  const chip = p.locator('a[href*="/search?ingredients="]').first();
  await chip.scrollIntoViewIfNeeded();
  return { states: { chip: pack(await styleOf(chip), await crop(p, chip, 'ingredient-chip-default')) } };
});

await run('collection', async () => {
  await open(p, BASE + COLLECTION, { wait: 2500 });
  const h1 = p.locator('h1').first();
  const card = p.locator('a[href*="/recipes/"]').first();
  return { states: { title: pack(await styleOf(h1)), card: pack(await styleOf(card), await crop(p, card, 'collection-card-default')) } };
});

await run('search-results', async () => {
  await open(p, BASE + '/search?ingredients=apple', { wait: 2200 });
  const heading = p.locator('h1, h2, p').filter({ hasText: /apple/i }).first();
  const card = p.locator('a[href*="/recipes/"]').first();
  return { states: { heading: pack(await styleOf(heading)), card: pack(await styleOf(card)) } };
});

await run('footer', async () => {
  await open(p, BASE + '/');
  const footer = p.locator('footer').first();
  await footer.scrollIntoViewIfNeeded();
  const link = footer.locator('a').first();
  return { states: { footer: pack(await styleOf(footer), await crop(p, footer, 'footer-default')), link: pack(await styleOf(link), await crop(p, link, 'footer-link-default')) } };
});

await run('team', async () => {
  await open(p, BASE + '/team', { wait: 1800 });
  const h1 = p.locator('h1').first();
  const menu = p.getByRole('button', { name: 'Menu' });
  const menuStyle = await styleOf(menu);
  let openMenu = null;
  if (await menu.count()) {
    await menu.click();
    await p.waitForTimeout(500);
    const panel = p.locator('nav, [role="navigation"], header').filter({ hasText: /Roadmap/ }).last();
    openMenu = pack(await styleOf(panel), await crop(p, panel, 'team-menu-default'));
    await p.keyboard.press('Escape').catch(() => {});
  }
  return { states: { h1: pack(await styleOf(h1), await crop(p, h1, 'team-title-default')), menuButton: pack(menuStyle, await crop(p, menu, 'menu-button-default')), menu: openMenu } };
});

await run('legal', async () => {
  await open(p, BASE + '/privacy-policy', { wait: 1800 });
  const h1 = p.locator('h1').first();
  const h2 = p.locator('h2').first();
  const p1 = p.locator('main p, article p, p').nth(1);
  return { states: { h1: pack(await styleOf(h1)), h2: pack(await styleOf(h2)), body: pack(await styleOf(p1)) } };
});

await run('cookbook-boundary', async () => {
  await open(p, BASE + '/cookbook', { wait: 1800 });
  const body = p.locator('body');
  return { boundary: 'https://withjulienne.com/cookbook shows "Come back soon." signed out', states: { body: pack(await styleOf(body)) } };
});

await run('buy-boundary', async () => {
  await open(p, BASE + '/');
  const buy = p.getByRole('link', { name: 'Buy' }).first();
  await buy.scrollIntoViewIfNeeded().catch(() => {});
  const href = await buy.getAttribute('href').catch(() => null);
  return { boundary: 'Buy links leave the site (affiliate/shop). Never followed.', href: (href || '').split('?')[0].slice(0, 80), states: { buy: pack(await styleOf(buy), await crop(p, buy, 'buy-link-default')) } };
});

await run('hover-pressed', async () => {
  await open(p, BASE + '/');
  const login = p.getByRole('button', { name: 'Log in', exact: true }).first();
  const before = await styleOf(login);
  await login.hover();
  await p.waitForTimeout(180);
  const hover = await styleOf(login);
  const hoverCrop = await crop(p, login, 'login-button-hover');
  const box = await login.boundingBox();
  await p.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  await p.mouse.down();
  await p.waitForTimeout(120);
  const pressed = await styleOf(login);
  const pressedCrop = await crop(p, login, 'login-button-pressed');
  await p.mouse.move(8, 8);
  await p.mouse.up();
  await login.focus();
  await p.waitForTimeout(120);
  const focus = await styleOf(login);
  return {
    note: 'hover is a real pointer hover; pressed is mousedown held, then the pointer leaves before mouseup so Log in never opens; focus is element.focus() on the same button',
    states: {
      default: pack(before),
      hover: pack(hover, hoverCrop),
      pressed: pack(pressed, pressedCrop),
      focus: pack(focus, await crop(p, login, 'login-button-focus')),
    },
  };
});

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
