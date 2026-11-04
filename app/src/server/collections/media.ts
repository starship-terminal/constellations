import type { CollectionMediaItem } from "@/contracts/research";
import type { LibraryDetail, LibraryItem } from "@/contracts/library";
import { getReference } from "@/server/sources";
import { z } from "zod";
import { identifier } from "@/server/research/http";

export const mediaSelection = z
  .object({ referenceId: identifier, mediaId: z.string().min(1).max(2000) })
  .strict();
type StoredMedia = {
  collectionId: string;
  referenceId: string;
  mediaId: string;
  addedAt: number;
};
function summary(detail: LibraryDetail): LibraryItem {
  const {
    media,
    colors,
    typography,
    spacing,
    radii,
    descriptionLong,
    guidelines,
    exports,
    related,
    measured,
    interpreted,
    ...reference
  } = detail;
  return reference;
}
/** Missing source assets remain visible as unavailable board entries. */
export async function hydrateCollectionMedia(
  rows: StoredMedia[],
): Promise<CollectionMediaItem[]> {
  const references = new Map<string, Promise<LibraryDetail | null>>();
  return Promise.all(
    rows.map(async (row) => {
      if (!references.has(row.referenceId))
        references.set(row.referenceId, getReference(row.referenceId));
      const reference = await references.get(row.referenceId)!;
      return {
        ...row,
        id: `${row.collectionId}:${row.referenceId}:${row.mediaId}`,
        reference: reference ? summary(reference) : null,
        name: reference?.name || row.referenceId,
        media: reference?.media.find((item) => item.id === row.mediaId) || null,
      };
    }),
  );
}
