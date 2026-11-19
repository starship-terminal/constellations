// Unit tests for the small display helpers. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { themeLabel, tintOf } from "./style-labels.ts";

describe("tintOf", () => {
  it("picks the first accent, primary, brand or face colour across themes", () => {
    const swatches = {
      light: [
        { role: "background", value: "#fff" },
        { role: "Brand-500", value: "#5e6ad2" },
      ],
      dark: [{ role: "accent", value: "#000" }],
    };
    assert.equal(tintOf(swatches), "#5e6ad2");
  });

  it("is empty when nothing matches or the match has no value", () => {
    assert.equal(tintOf({ light: [{ role: "background", value: "#fff" }] }), "");
    assert.equal(tintOf({ light: [{ role: "primary", value: null }] }), "");
    assert.equal(tintOf({}), "");
  });
});

describe("themeLabel", () => {
  it("shortens the known theme ids", () => {
    assert.equal(themeLabel("light-mobile"), "mobile");
    assert.equal(themeLabel("light-high-contrast"), "high contrast");
    assert.equal(themeLabel("dark-experimental"), "dark (exp.)");
    // Polaris ships this id; both replacements apply.
    assert.equal(themeLabel("light-high-contrast-experimental"), "high contrast (exp.)");
  });

  it("leaves other ids alone", () => {
    assert.equal(themeLabel("dark"), "dark");
  });
});
