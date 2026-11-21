// Public marketing capture for cursor.com. Signed out. No typing, no identity
// providers, no form submit, no captcha. Cookie banner is hidden, not accepted.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { screenshotWithMetadata } from "./screenshot.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, "../..");
const SHOTS = path.join(PKG, "screenshots");
const RAW = path.join(PKG, "raw");
const PLAYWRIGHT = process.env.PLAYWRIGHT;
if (!PLAYWRIGHT) throw new Error("Set PLAYWRIGHT to playwright/index.mjs");
const { chromium } = await import(PLAYWRIGHT);

const PAGES = [
  ["home", "https://cursor.com/"],
  ["pricing", "https://cursor.com/pricing"],
  ["download", "https://cursor.com/download"],
  ["product", "https://cursor.com/product"],
  ["enterprise", "https://cursor.com/enterprise"],
  ["changelog", "https://cursor.com/changelog"],
  ["blog", "https://cursor.com/blog"],
  ["not-found", "https://cursor.com/this-page-does-not-exist"],
];

function hideConsent(page) {
  return page.addInitScript(() => {
    const hide = () => {
      for (const sel of ["#onetrust-consent-sdk", "#onetrust-banner-sdk", ".onetrust-pc-dark-filter", "#onetrust-pc-sdk"]) {
        document.querySelectorAll(sel).forEach((el) => el.style.setProperty("display", "none", "important"));
      }
    };
    new MutationObserver(hide).observe(document.documentElement, { childList: true, subtree: true });
    document.addEventListener("DOMContentLoaded", hide);
  });
}

async function settle(page) {
  await page.waitForTimeout(800);
  await page.evaluate(async () => {
    const h = Math.min(document.documentElement.scrollHeight, 8000);
    for (let y = 0; y < h; y += 700) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 80));
    }
    window.scrollTo(0, 0);
  });
  await page.waitForTimeout(400);
}

async function shoot(page, name, url) {
  const file = path.join(SHOTS, name);
  const meta = await screenshotWithMetadata(page, { path: file, fullPage: true }, {
    sanitizedSourceUrl: url.split("?")[0],
    viewport: page.viewportSize(),
    deviceScaleFactor: 1,
  });
  meta.visualReview = { status: "pending", note: "Public marketing page. Cookie banner hidden, not accepted." };
  fs.writeFileSync(`${file}.capture.json`, JSON.stringify(meta, null, 2) + "\n");
  return meta.png;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  colorScheme: "dark",
  locale: "en-US",
});
await hideConsent(context);
const page = await context.newPage();

const readings = [];
for (const [slug, url] of PAGES) {
  const response = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.waitForTimeout(1200);
  await settle(page);
  const status = response ? response.status() : null;
  const finalUrl = page.url().split("?")[0];
  const png = await shoot(page, `${slug}-dark-default.png`, finalUrl);
  const sample = await page.evaluate(() => {
    const h1 = document.querySelector("h1");
    const body = getComputedStyle(document.body);
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of [...document.styleSheets]) {
      let rules;
      try { rules = [...sheet.cssRules]; } catch { continue; }
      const walk = (list) => {
        for (const rule of list) {
          if (rule.style) {
            for (const name of rule.style) {
              if (name.startsWith("--")) vars[name] = rule.style.getPropertyValue(name).trim();
            }
          }
          if (rule.cssRules) walk([...rule.cssRules]);
        }
      };
      walk(rules);
    }
    const btn = document.querySelector("a.btn--primary, a.btn.btn--primary, .btn--primary");
    const ghost = document.querySelector("a.btn--ghost, .btn--ghost");
    const cs = (el) => el ? {
      text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 60),
      bg: getComputedStyle(el).backgroundColor,
      color: getComputedStyle(el).color,
      radius: getComputedStyle(el).borderRadius,
      font: getComputedStyle(el).fontFamily,
      size: getComputedStyle(el).fontSize,
      weight: getComputedStyle(el).fontWeight,
      pad: getComputedStyle(el).padding,
      height: getComputedStyle(el).height,
    } : null;
    return {
      title: document.title,
      h1: h1 ? h1.innerText.replace(/\s+/g, " ").trim().slice(0, 160) : null,
      h1Style: h1 ? { font: getComputedStyle(h1).fontFamily, size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, lh: getComputedStyle(h1).lineHeight, color: getComputedStyle(h1).color } : null,
      body: { bg: body.backgroundColor, color: body.color, font: body.fontFamily, size: body.fontSize, weight: body.fontWeight, lh: body.lineHeight },
      scheme: root.colorScheme,
      themeClass: document.documentElement.className,
      varCount: Object.keys(vars).length,
      vars,
      primary: cs(btn),
      ghost: cs(ghost),
      inner: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
    };
  });
  readings.push({ slug, url, status, finalUrl, png, sample: { ...sample, vars: undefined }, varCount: sample.varCount });
  if (slug === "home") {
    fs.writeFileSync(path.join(RAW, "css-vars.json"), JSON.stringify({ capturedAt: new Date().toISOString(), url: "https://cursor.com/", vars: sample.vars, count: sample.varCount }, null, 2) + "\n");
    fs.writeFileSync(path.join(RAW, "home-computed.json"), JSON.stringify(sample, null, 2) + "\n");
  }
  console.log(slug, status, finalUrl, png.width + "x" + png.height, "vars", sample.varCount);
}

await context.close();

const phone = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  colorScheme: "dark",
  locale: "en-US",
  userAgent: "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
});
await hideConsent(phone);
const mobile = await phone.newPage();
await mobile.goto("https://cursor.com/", { waitUntil: "domcontentloaded", timeout: 45000 });
await mobile.waitForTimeout(1200);
await settle(mobile);
const mobilePng = await shoot(mobile, "mobile-home-dark-default.png", "https://cursor.com/");
const mobileMeta = await mobile.evaluate(() => ({
  inner: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
  title: document.title,
  menu: !!document.querySelector('button[aria-label="Open navigation"]'),
}));
console.log("mobile-home", mobilePng.width + "x" + mobilePng.height, JSON.stringify(mobileMeta));
await phone.close();
await browser.close();
fs.writeFileSync(path.join(RAW, "pages.json"), JSON.stringify({ readings, mobileMeta, capturedAt: new Date().toISOString() }, null, 2) + "\n");
