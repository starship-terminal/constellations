import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { expect, test } from "vitest";

// A white wash (#ffffff0c) or near-white text (#f7f8fb) written straight into
// a rule renders in dark and disappears on the light theme's white surfaces.
// Washes are a share of var(--ink) and text uses the theme roles instead.
// Shadows, filters and decorative gradients may stay literal: they paint over
// a fixed backdrop (or are dark), so they read the same on both themes.
const SRC = path.join(__dirname, "..", "src");

function cssFiles(dir: string): string[] {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) return cssFiles(full);
    return entry.name.endsWith(".css") ? [full] : [];
  });
}

// White in any form (#fff, #ffffff, white, with or without alpha), or an
// opaque colour whose channels are all at least 0xd0.
const PALE =
  /#(?:fff[0-9a-f]?|ffffff(?:[0-9a-f]{2})?|(?:[d-f][0-9a-f]){3})(?![0-9a-f])|:\s*white\b(?!-)/i;

// Fixed pairs: these surfaces are white in both themes on purpose and set
// their own dark text, or frame a page that paints its own content.
const FIXED_PAIRS = new Set([
  "app/globals.css .skip-link",
  "app/globals.css .icon-button.selected",
  "features/package-detail.module.css .guide",
  "features/research-home.module.css .session :global(.user-message .message-body)",
  "features/style-reference.module.css .componentFrame",
]);

test("app stylesheets keep pale literals out of colour declarations", () => {
  const offenders: string[] = [];
  for (const file of cssFiles(SRC)) {
    if (file.endsWith(`${path.sep}tokens.css`)) continue;
    // The declaration a line belongs to, so a multi-line value is judged by
    // the property it started under.
    let declaration = "";
    let selector = "";
    readFileSync(file, "utf8")
      .split("\n")
      .forEach((line, index) => {
        if (/\{\s*$/.test(line))
          selector = line.replace(/\s*\{\s*$/, "").trim();
        if (/^\s*[\w-]+\s*:/.test(line) || /[{}]/.test(line))
          declaration = line;
        if (!PALE.test(line)) return;
        if (/^\s*(box-shadow|filter|--)/.test(declaration)) return;
        if (/gradient\(/.test(declaration + line)) return;
        const rel = path.relative(SRC, file).split(path.sep).join("/");
        if (FIXED_PAIRS.has(`${rel} ${selector}`)) return;
        offenders.push(`${rel}:${index + 1}: ${line.trim()}`);
      });
  }
  expect(offenders).toEqual([]);
});
