/**
 * Public signed-out capture for Pop Site.
 * Headless Chromium. Marketing pages plus the signed-out login screen.
 * Does not type credentials, does not submit, does not follow Google SSO.
 */
import { createRequire } from "node:module";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { screenshotWithMetadata } from "../screenshot.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT);

const here = dirname(fileURLToPath(import.meta.url));
const RAW = process.env.RAW || join(here, "..", "..", "..", "raw");
const SHOTS = process.env.SHOTS || join(here, "..", "..", "..", "screenshots");
mkdirSync(RAW, { recursive: true });
mkdirSync(SHOTS, { recursive: true });

const PAGES = [
  { name: "home", url: "https://pop.site/" },
  { name: "pricing", url: "https://pop.site/pricing" },
  { name: "blog", url: "https://pop.site/blog" },
  { name: "signin", url: "https://app.pop.site/?signin" },
];

function challenge(page) {
  const title = page.url();
  return title.includes("challenges.cloudflare.com");
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  colorScheme: "light",
});
const page = await context.newPage();

const report = { pages: [] };

for (const spec of PAGES) {
  const response = await page.goto(spec.url, { waitUntil: "networkidle", timeout: 45000 });
  await page.waitForTimeout(800);
  const status = response ? response.status() : null;
  const url = page.url();
  const title = await page.title();
  const bodyText = await page.evaluate(() => (document.body.innerText || "").slice(0, 400));
  const blocked = /just a moment|cf-challenge|checking your browser/i.test(bodyText) || url.includes("challenges.cloudflare");
  report.pages.push({ name: spec.name, status, url, title, blocked, text: bodyText.slice(0, 180) });
  if (blocked) {
    console.log("CHALLENGE", spec.name, url);
    continue;
  }
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, sanitizedSourceUrl: spec.url };
  await screenshotWithMetadata(page, { path: join(SHOTS, `${spec.name}-light-default.png`) }, requested);
  await screenshotWithMetadata(page, { path: join(SHOTS, `${spec.name}-light-full.png`), fullPage: true }, requested);
  console.log("shot", spec.name, status, url);
}

await browser.close();
writeFileSync(join(RAW, "capture-report.json"), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
