/**
 * Public signed-out capture for Pop Site.
 * Headless Chromium. Marketing pages plus the signed-out login screen.
 * Does not type credentials, does not submit, does not follow Google SSO.
 */
import { createRequire } from "node:module";
import { mkdirSync, readdirSync, unlinkSync, writeFileSync } from "node:fs";
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
  const entry = { name: spec.name, status, url, title, blocked, text: bodyText.slice(0, 180) };
  report.pages.push(entry);
  if (blocked) {
    console.log("CHALLENGE", spec.name, url);
    continue;
  }
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, sanitizedSourceUrl: spec.url };
  await screenshotWithMetadata(page, { path: join(SHOTS, `${spec.name}-light-default.png`) }, requested);
  // Bound the full-page shot the way the kit's shooter does (AGENTS.md "Bound every full-page
  // capture"): one PNG while the page fits a chunk, otherwise at most 8 chunk-high tiles, and a page
  // taller than that is truncated and recorded as a boundary instead of tiled forever.
  const fullHeight = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const chunk = Math.floor(14000 / requested.deviceScaleFactor);
  const maxHeight = 8 * chunk;
  const capped = Math.min(fullHeight, maxHeight);
  if (fullHeight > maxHeight) {
    entry.fullPageBoundary = { scrollHeight: fullHeight, capturedHeight: capped };
    console.log(`  ! ${spec.name}: page is ${fullHeight}px tall, capturing the first ${capped}px only (boundary)`);
  }
  const full = join(SHOTS, `${spec.name}-light-full`);
  // Clear this shot's tiles (and their .capture.json sidecars) from an earlier run first, so a page
  // that now needs fewer tiles, or fits one PNG, leaves no stale part for quantize.py to stitch.
  for (const old of readdirSync(SHOTS).filter((n) => n.startsWith(`${spec.name}-light-full.part`))) unlinkSync(join(SHOTS, old));
  if (capped <= chunk) await screenshotWithMetadata(page, { path: `${full}.png`, fullPage: true }, requested);
  else for (let i = 0, y = 0; y < capped; i++, y += chunk) {
    await screenshotWithMetadata(page, { path: `${full}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: requested.viewport.width, height: Math.min(chunk, capped - y) } }, requested);
  }
  console.log("shot", spec.name, status, url);
}

await browser.close();
writeFileSync(join(RAW, "capture-report.json"), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
