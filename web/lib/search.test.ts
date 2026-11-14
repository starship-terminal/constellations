// Unit tests for the listings' shared search scoring. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { scoreRow, terms, type Facet } from "./search.ts";

describe("terms", () => {
  it("lowercases, splits on whitespace and drops stop words", () => {
    assert.deepEqual(terms("  The Dark   Dashboard  "), ["dark", "dashboard"]);
  });

  it("returns nothing for an empty or all-stop-word query", () => {
    assert.deepEqual(terms(""), []);
    assert.deepEqual(terms("a design for the web"), []);
  });
});

describe("scoreRow", () => {
  const row = { tags: new Set(["dark"]) };
  const facets: Facet<typeof row>[] = [[new Set(["dark", "light"]), (r, t) => r.tags.has(t)]];

  it("scores every row 1 when there are no terms", () => {
    assert.equal(scoreRow(row, "anything", [], facets), 1);
  });

  it("counts a text hit once and a facet value the row holds twice", () => {
    assert.equal(scoreRow(row, "a dark theme", ["theme"], facets), 1);
    assert.equal(scoreRow(row, "a dark theme", ["dark"], facets), 2);
  });

  it("a facet value the row lacks falls back to a text hit", () => {
    assert.equal(scoreRow({ tags: new Set<string>() }, "dark mode", ["dark"], facets), 1);
  });

  it("hides rows that miss a term of a short query", () => {
    assert.equal(scoreRow(row, "dark theme", ["dark", "missing"], facets), 0);
    assert.equal(scoreRow(row, "dark theme", ["missing"], facets), 0);
  });

  it("lets a query of three or more terms miss once", () => {
    assert.ok(scoreRow(row, "dark dense grid", ["dark", "dense", "nope"], facets) > 0);
    assert.equal(scoreRow(row, "dark dense grid", ["dark", "nope", "nada"], facets), 0);
  });

  it("adds a bonus when adjacent terms appear as a phrase", () => {
    const together = scoreRow(row, "dense grid layout", ["dense", "grid"], []);
    const apart = scoreRow(row, "dense layout grid", ["dense", "grid"], []);
    assert.equal(together - apart, 1.5);
  });
});
