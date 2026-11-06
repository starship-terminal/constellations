import { expect, test } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import type { LibraryItem, ReferenceMedia } from "@/contracts/library";
import { captureViewerLinks } from "@/features/package-detail";
import {
  CollectionScreens,
  resolveCollectionSelection,
  type CollectionMediaEntry,
} from "@/features/collection-media";
import { MediaCollectionButton } from "@/components/media-collection";
const reference = {
  id: "systems:demo",
  source: "systems",
  slug: "demo",
  name: "Demo",
  platform: "web",
} as LibraryItem;
const media = {
  id: "same-name",
  name: "Home",
  url: "/media/demo.png",
  type: "image",
  tags: [],
} as ReferenceMedia;
const entry = {
  id: "board:systems:demo:same-name",
  collectionId: "board",
  referenceId: reference.id,
  mediaId: media.id,
  reference,
  media,
  name: "Demo",
  addedAt: 1,
} as CollectionMediaEntry;
test("board selection resolves current hydrated objects after an independent row refresh", () => {
  const refreshed = structuredClone([entry]);
  const selected = resolveCollectionSelection(refreshed, entry.id);
  expect(selected).toBe(refreshed[0]);
  expect(selected?.media).not.toBe(entry.media);
  expect(refreshed.map((row) => row.media).indexOf(selected!.media)).toBe(0);
  expect(resolveCollectionSelection([], entry.id)).toBeUndefined();
});
test("missing capture remains removable from its board", () => {
  const html = renderToStaticMarkup(
    createElement(CollectionScreens, {
      id: "board",
      items: [{ ...entry, reference: null, media: null }],
      onChanged: () => {},
    }),
  );
  expect(html).toContain("Capture unavailable");
  expect(html).toContain('aria-label="Remove same-name from board"');
  expect(html).not.toContain('aria-label="Open');
});
test("picker state remounts for both package and media identities", () => {
  const first = MediaCollectionButton({
    referenceId: "systems:a",
    mediaId: "shared",
  });
  const otherReference = MediaCollectionButton({
    referenceId: "systems:b",
    mediaId: "shared",
  });
  const otherMedia = MediaCollectionButton({
    referenceId: "systems:a",
    mediaId: "other",
  });
  expect(first.key).not.toBe(otherReference.key);
  expect(first.key).not.toBe(otherMedia.key);
});
test("viewer links preserve source and exact media without routing styles into measured packages", () => {
  const measured = captureViewerLinks(reference, media);
  expect(measured.documentation).toBe("/library/demo");
  for (const platform of ["mobile", "desktop"] as const) {
    const links = captureViewerLinks({ ...reference, platform }, media);
    expect(
      new URL(links.browse, "http://localhost").searchParams.get("platform"),
    ).toBe(platform);
    expect(
      new URL(links.tag("dense"), "http://localhost").searchParams.get(
        "platform",
      ),
    ).toBe(platform);
  }
  expect(measured.copy).toBe("/library/demo?tab=screenshots&media=same-name");
  const interpreted = captureViewerLinks(
    { ...reference, id: "refero:demo", source: "refero" },
    media,
  );
  expect(interpreted.documentation).toBe("/styles/refero/demo");
  expect(interpreted.browse).toBe("/styles/refero/demo");
  expect(interpreted.tag("dense")).toBe("/styles?tag=dense");
  expect(new URL(interpreted.copy, "http://localhost:8845").href).toBe(
    "http://localhost:8845/media/demo.png",
  );
  expect(
    captureViewerLinks(
      { ...reference, source: "refero" },
      { ...media, url: "https://cdn.example.test/full.png" },
    ).copy,
  ).toBe("https://cdn.example.test/full.png");
});
