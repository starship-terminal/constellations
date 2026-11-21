#!/usr/bin/env node
/**
 * Public 37signals capture. Does not type, submit, click identity providers,
 * or follow Basecamp, HEY, Fizzy, ONCE, or a signed-in app.
 *
 * PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.js \
 *   node systems/37signals/tools/capture/public/capture.mjs
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath = process.env.PLAYWRIGHT || path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.js");
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const pkg = path.resolve(here, "../../..");
const shots = path.join(pkg, "screenshots");

const THEME = "--rgb-theme-3";
const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

const PAGES = [
  ["home-light-default", "https://37signals.com/"],
  ["signal-00-light-default", "https://37signals.com/00"],
  ["books-light-default", "https://37signals.com/books"],
  ["thoughts-light-default", "https://37signals.com/thoughts"],
  ["jobs-light-default", "https://37signals.com/jobs"],
  ["policies-light-default", "https://37signals.com/policies"],
  ["not-found-light-default", "https://37signals.com/signup"],
];

async function pin(page) {
  await page.evaluate((name) => {
    const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    document.documentElement.style.setProperty("--rgb-theme", v);
    document.body.classList.add("is-ready");
  }, THEME);
}

async function shot(page, name) {
  const file = path.join(shots, name + ".png");
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    scrollH: document.documentElement.scrollHeight,
    theme: document.documentElement.style.getPropertyValue("--rgb-theme").trim(),
    url: location.href,
  }));
  await page.screenshot({ path: file, fullPage: true, animations: "disabled" });
  await writeFile(file + ".capture.json", JSON.stringify({ name, ...box, capturedAt: new Date().toISOString() }, null, 2));
  return box;
}

const browser = await chromium.launch({ headless: true });
const desktop = await browser.newContext({ viewport: DESKTOP, deviceScaleFactor: 1 });
const page = await desktop.newPage();
await mkdir(shots, { recursive: true });

for (const [name, url] of PAGES) {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.waitForTimeout(250);
  await pin(page);
  const box = await shot(page, name);
  console.log(name, box.theme, box.url);
}

const phone = await browser.newContext({ viewport: PHONE, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
const mp = await phone.newPage();
await mp.goto("https://37signals.com/", { waitUntil: "domcontentloaded" });
await mp.waitForTimeout(250);
await pin(mp);
await shot(mp, "mobile-home-light-default");
await mp.locator(".nav__toggle label").first().click();
await mp.waitForTimeout(200);
await shot(mp, "mobile-home-light-menu");
await mp.goto("https://37signals.com/00", { waitUntil: "domcontentloaded" });
await mp.waitForTimeout(250);
await pin(mp);
await shot(mp, "mobile-signal-00-light-default");

await browser.close();
console.log("done");
