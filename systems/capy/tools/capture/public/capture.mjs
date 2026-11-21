// Public marketing capture for capy.ai. Signed out. Never types, never
// submits, never clicks an identity provider, never follows a download file.
import { chromium } from "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs";
import { writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "../../..");
const shots = join(root, "screenshots");
const raw = join(root, "raw");
mkdirSync(shots, { recursive: true });
mkdirSync(raw, { recursive: true });

const browser = await chromium.launch({ headless: true });

async function shot(page, name, extra = {}) {
  const path = join(shots, name);
  await page.screenshot({ path, fullPage: false });
  const meta = await page.evaluate(() => ({
    url: location.href,
    title: document.title,
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    devicePixelRatio: window.devicePixelRatio,
    visualViewport: window.visualViewport && {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    },
  }));
  writeFileSync(path + ".capture.json", JSON.stringify({ ...meta, ...extra, file: "screenshots/" + name }, null, 2) + "\n");
  console.log("shot", name, meta.url, meta.innerWidth);
  return meta;
}

async function readPage(page) {
  return page.evaluate(() => {
    const cs = getComputedStyle(document.documentElement);
    const pick = [
      "--color-orange-red", "--color-black", "--color-black-50", "--color-black-100",
      "--color-black-200", "--color-black-300", "--color-black-400", "--color-black-500",
      "--color-black-600", "--color-black-700", "--color-black-800", "--color-black-900",
      "--color-white", "--color-capy-blue-200", "--color-capy-blue-300", "--color-capy-blue-500",
      "--color-capy-blue-600", "--color-capy-blue-800", "--color-primary", "--color-primary-dark",
      "--color-link", "--color-border", "--color-card-foreground", "--color-secondary-foreground",
      "--color-yuzu-yellow-400", "--color-pelican-orange-500", "--color-godmode-red-500",
      "--color-orange-dark", "--color-sapphire-blue-100", "--color-grass-green-400",
      "--color-envious-emerald-400", "--color-galaxy-purple-500", "--color-cool-teal-400",
      "--font-sans", "--font-heading", "--font-mono", "--font-inter", "--font-bebas-neue",
      "--font-abc-social-mono", "--font-dm-mono", "--header-height",
      "--radius-xs", "--radius-sm", "--radius-md", "--radius-lg", "--radius-xl", "--radius-2xl", "--radius-3xl",
      "--ease-out-quart", "--ease-out", "--ease-in-out",
    ];
    const vars = {};
    for (const name of pick) vars[name] = cs.getPropertyValue(name).trim();
    const measure = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || "").trim().slice(0, 80),
        font: s.fontFamily,
        size: s.fontSize,
        weight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        color: s.color,
        background: s.backgroundColor,
        radius: s.borderRadius,
        padding: s.padding,
        height: s.height,
        border: s.border,
        boxShadow: s.boxShadow.slice(0, 220),
        width: Math.round(r.width),
        top: Math.round(r.top),
      };
    };
    const h1 = document.querySelector("h1");
    const buttons = [...document.querySelectorAll("a, button")].slice(0, 12).map(measure);
    const inputs = [...document.querySelectorAll("input, textarea, select")].map((el) => ({
      type: el.type,
      name: el.name,
      placeholder: el.placeholder,
      valueLength: (el.value || "").length,
      ...measure(el),
    }));
    return {
      title: document.title,
      url: location.href,
      h1: h1 && h1.innerText.slice(0, 180),
      bodyStart: document.body.innerText.slice(0, 600),
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily,
      vars,
      h1Style: measure(h1),
      buttons,
      inputs,
      linkCount: document.querySelectorAll("a").length,
    };
  });
}

const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  reducedMotion: "reduce",
});
const page = await context.newPage();

const pages = [
  ["https://capy.ai/", "home-light-default.png"],
  ["https://capy.ai/pricing", "pricing-light-default.png"],
  ["https://capy.ai/enterprise", "enterprise-light-default.png"],
  ["https://capy.ai/download", "download-light-default.png"],
  ["https://capy.ai/features/captains", "captains-light-default.png"],
  ["https://capy.ai/features/review", "review-light-default.png"],
  ["https://capy.ai/integrations", "integrations-light-default.png"],
  ["https://capy.ai/customers", "customers-light-default.png"],
  ["https://capy.ai/security", "security-light-default.png"],
  ["https://capy.ai/about", "about-light-default.png"],
  ["https://capy.ai/blog", "blog-light-default.png"],
  ["https://capy.ai/changelog", "changelog-light-default.png"],
  ["https://capy.ai/demo", "demo-light-default.png"],
  ["https://capy.ai/this-page-does-not-exist-capture-2026", "notfound-light-default.png"],
  ["https://capy.ai/sign-in", "login-light-default.png"],
  ["https://capy.ai/sign-up", "signup-light-default.png"],
];

const readings = {};
for (const [url, name] of pages) {
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(1200);
    const reading = await readPage(page);
    readings[name] = reading;
    const wall = /captcha|verify you are human|just a moment/i.test(reading.bodyStart || "");
    if (wall) {
      console.log("SKIP wall", url);
      continue;
    }
    await shot(page, name);
    if (name === "home-light-default.png") {
      await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await page.waitForTimeout(600);
      await shot(page, "home-light-footer.png");
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(300);
      // Open Product with keyboard, matching the live menu.
      const product = page.locator("button", { hasText: /^Product$/i }).first();
      await product.focus();
      await page.keyboard.press("Enter");
      await page.waitForTimeout(400);
      await shot(page, "home-light-product-menu.png");
      await page.keyboard.press("Escape");
      await page.waitForTimeout(200);
      const resources = page.locator("button", { hasText: /^Resources$/i }).first();
      await resources.focus();
      await page.keyboard.press("Enter");
      await page.waitForTimeout(400);
      await shot(page, "home-light-resources-menu.png");
      await page.keyboard.press("Escape");
    }
    if (name === "pricing-light-default.png") {
      const monthly = page.locator("button", { hasText: /^Monthly$/ }).first();
      if (await monthly.count()) {
        await monthly.click();
        await page.waitForTimeout(400);
        await shot(page, "pricing-light-monthly.png");
      }
    }
  } catch (err) {
    console.log("FAIL", url, err.message);
    readings[name] = { error: err.message, url };
  }
}

await context.close();

const phone = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  reducedMotion: "reduce",
});
const mobile = await phone.newPage();
for (const [url, name] of [
  ["https://capy.ai/", "mobile-home-light-default.png"],
  ["https://capy.ai/pricing", "mobile-pricing-light-default.png"],
]) {
  await mobile.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await mobile.waitForTimeout(1200);
  const reading = await readPage(mobile);
  readings[name] = reading;
  await shot(mobile, name);
  if (name.startsWith("mobile-home")) {
    const opener = mobile.locator("header button").first();
    await opener.click({ timeout: 8000 });
    await mobile.waitForTimeout(600);
    await shot(mobile, "mobile-home-light-menu.png");
  }
}
await phone.close();
await browser.close();

writeFileSync(join(raw, "public-readings.json"), JSON.stringify(readings, null, 2) + "\n");
console.log("done", Object.keys(readings).length);
