// Unit tests for the refero media URL helpers shared by the index and detail
// pages. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { cardFav, cardImg, cardVideo, cdnUrl, host, localMedia } from "./refero-media.ts";
import type { ReferoCard, ReferoIndex } from "@/lib/refero";

const index: ReferoIndex = { version: 1, cdn: "https://cdn.example/", mediaBase: "https://media.example", styles: [] };
const card: ReferoCard = {
  slug: "acme corp",
  name: "Acme",
  tagline: null,
  theme: "light",
  industry: null,
  type: null,
  style: null,
  tags: [],
  src: "https://www.acme.example/pricing",
  card: "s",
  cardRemote: "shots/acme.jpg",
  video: true,
  videoRemote: "https://other.example/v.mp4",
};

describe("host", () => {
  it("drops scheme, www and path", () => {
    assert.equal(host("https://www.acme.example/pricing?x=1"), "acme.example");
    assert.equal(host("http://sub.acme.example"), "sub.acme.example");
  });

  it("drops a query or fragment that has no path before it", () => {
    assert.equal(host("https://acme.example?ref=x"), "acme.example");
    assert.equal(host("https://www.acme.example#top"), "acme.example");
    assert.equal(host("acme.example/pricing"), "acme.example");
  });

  it("is empty for null", () => {
    assert.equal(host(null), "");
  });
});

describe("localMedia", () => {
  it("builds the /refero-media path under the media base", () => {
    const slug = "acme";
    assert.equal(localMedia("https://m.example", "shots", slug, "jpg"), "https://m.example/refero-media/shots/acme.jpg");
  });

  it("falls back to the app's own /media route when the base is empty", () => {
    assert.equal(localMedia("", "videos", "a b", "mp4"), "/media/refero-media/videos/a%20b.mp4");
  });
});

describe("cdnUrl", () => {
  it("prefixes relative paths and keeps absolute URLs", () => {
    assert.equal(cdnUrl("https://cdn.example/", "v/a.mp4"), "https://cdn.example/v/a.mp4");
    assert.equal(cdnUrl("https://cdn.example/", "https://x.example/a.mp4"), "https://x.example/a.mp4");
  });

  it("is null without a URL", () => {
    assert.equal(cdnUrl("https://cdn.example/", null), null);
    assert.equal(cdnUrl("https://cdn.example/", ""), null);
  });
});

describe("card media pairs", () => {
  it("cardImg uses shots for an s card and posters for a p card", () => {
    assert.equal(cardImg(index, card).local, "https://media.example/refero-media/shots/acme%20corp.jpg");
    assert.equal(cardImg(index, { ...card, card: "p" }).local, "https://media.example/refero-media/posters/acme%20corp.jpg");
    assert.equal(cardImg(index, card).remote, "https://cdn.example/shots/acme.jpg");
  });

  it("cardImg has no local file for a card without an image", () => {
    assert.deepEqual(cardImg(index, { ...card, card: null, cardRemote: null }), { local: null, remote: null });
  });

  it("cardFav and cardVideo point at their own folders", () => {
    assert.equal(cardFav(index, card).local, "https://media.example/refero-media/favicons/acme%20corp.png");
    assert.equal(cardFav(index, card).remote, null);
    assert.equal(cardVideo(index, card).local, "https://media.example/refero-media/videos/acme%20corp.mp4");
    assert.equal(cardVideo(index, card).remote, "https://other.example/v.mp4");
  });
});

describe("favicons", () => {
  it("never name a favicon service, so browsing a style tells no third party", () => {
    const pair = cardFav(index, { ...card, src: "acme.example" });
    assert.equal(pair.remote, null);
    assert.ok(!JSON.stringify(pair).includes("gstatic"));
  });
});
