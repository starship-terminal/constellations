// Unit tests for the client-safe URL helpers. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { mediaUrl } from "./url.ts";

describe("mediaUrl", () => {
  it("prefixes /media/ and keeps the path separators", () => {
    assert.equal(mediaUrl("systems/linear/screenshots/home.png"), "/media/systems/linear/screenshots/home.png");
  });

  it("encodes each segment, not the slashes", () => {
    assert.equal(mediaUrl("systems/a b/c#d?.png"), "/media/systems/a%20b/c%23d%3F.png");
  });
});
