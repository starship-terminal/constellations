#!/usr/bin/env node
/**
 * Public Zoom capture. Does not type, submit, click identity providers,
 * join a meeting, or follow a signed-in app.
 *
 * PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
 *   node systems/zoom/tools/capture/public/capture.mjs
 *
 * Writes screenshots to $SHOTS (default /tmp/zoom-capture/shots) so a
 * skip-smudge checkout is not required to re-run it. Copy the shots you
 * keep into screenshots/ and quantize before commit.
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath = process.env.PLAYWRIGHT || path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.mjs");
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const pkg = path.resolve(here, "../../..");
const outDir = process.env.SHOTS || "/tmp/zoom-capture/shots";
const rawDir = process.env.RAW || path.join(pkg, "raw");
const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

async function dismissCookies(page) {
  const accept = page.locator("#onetrust-accept-btn-handler").first();
  if (await accept.count()) {
    await accept.click({ timeout: 2500 }).catch(() => {});
    await page.waitForTimeout(400);
  }
}

async function shoot(page, name) {
  const file = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: file });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
  }));
  return { name, ...box, url: page.url().split("?")[0].split("#")[0] };
}

async function goto(page, url) {
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.waitForTimeout(1400);
  await dismissCookies(page);
}

async function main() {
  await mkdir(outDir, { recursive: true });
  await mkdir(rawDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({
    viewport: DESKTOP,
    deviceScaleFactor: 1,
    locale: "en-US",
  })).newPage();
  const log = [];

  await goto(page, "https://www.zoom.com/");
  log.push(await shoot(page, "home-dark-default"));

  const headerButton = (name) => page.locator("header button, .nav-primary button").filter({ hasText: name }).first();
  for (const [label, file] of [
    [/^Products$/, "home-dark-products-menu"],
    [/^AI$/, "home-dark-ai-menu"],
    [/^Solutions$/, "home-dark-solutions-menu"],
  ]) {
    await headerButton(label).click();
    await page.waitForTimeout(500);
    log.push(await shoot(page, file));
    await page.keyboard.press("Escape");
    await page.waitForTimeout(200);
  }

  await page.getByRole("button", { name: "Meet" }).first().click();
  await page.waitForTimeout(400);
  log.push(await shoot(page, "home-dark-meet-menu"));
  await page.keyboard.press("Escape");

  await page.getByRole("button", { name: /Open search|Search/i }).first().click();
  await page.waitForTimeout(400);
  log.push(await shoot(page, "home-dark-search"));
  await page.keyboard.press("Escape");

  await page.getByRole("button", { name: /More products/i }).click();
  await page.waitForTimeout(400);
  log.push(await shoot(page, "home-dark-more-drawer"));
  await page.keyboard.press("Escape");

  await page.locator("footer").first().scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);
  log.push(await shoot(page, "home-dark-footer"));

  for (const [name, url] of [
    ["pricing-light-default", "https://zoom.us/pricing"],
    ["products-light-default", "https://www.zoom.com/en/products/"],
    ["meetings-light-default", "https://www.zoom.com/en/products/virtual-meetings/"],
    ["download-light-default", "https://zoom.us/download"],
    ["about-light-default", "https://www.zoom.com/en/about/"],
    ["privacy-light-default", "https://www.zoom.com/en/trust/privacy/privacy-statement/"],
    ["trust-light-default", "https://www.zoom.com/en/trust/"],
    ["notfound-light-default", "https://www.zoom.com/en/this-page-does-not-exist-capture-2026/"],
    ["login-light-default", "https://zoom.us/signin"],
    ["signup-light-default", "https://zoom.us/signup"],
  ]) {
    await goto(page, url);
    log.push(await shoot(page, name));
  }

  await page.setViewportSize(PHONE);
  await goto(page, "https://www.zoom.com/");
  log.push(await shoot(page, "mobile-home-dark-default"));
  const menu = page.getByRole("button", { name: /menu/i }).first();
  if (await menu.count()) {
    await menu.click().catch(() => {});
    await page.waitForTimeout(400);
    log.push(await shoot(page, "mobile-home-dark-menu"));
  }
  await goto(page, "https://zoom.us/pricing");
  log.push(await shoot(page, "mobile-pricing-light-default"));

  await writeFile(path.join(rawDir, "shots.json"), JSON.stringify(log, null, 2));
  console.log(JSON.stringify(log.map((s) => s.name), null, 2));
  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
