import type { CollectionMediaItem } from "@/contracts/research";
import { getReferenceMedia } from "@/server/sources";
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
/** Missing source assets remain visible as unavailable board entries. */
export async function hydrateCollectionMedia(
  rows: StoredMedia[],
): Promise<CollectionMediaItem[]> {
  // One media read per distinct reference, all in flight together. The board
  // needs the card summary and the media list, not the full package detail.
  const references = new Map<string, ReturnType<typeof getReferenceMedia>>();
  return Promise.all(
    rows.map(async (row) => {
      if (!references.has(row.referenceId))
        references.set(row.referenceId, getReferenceMedia(row.referenceId));
      const found = await references.get(row.referenceId)!;
      return {
        ...row,
        id: `${row.collectionId}:${row.referenceId}:${row.mediaId}`,
        reference: found?.reference ?? null,
        name: found?.reference.name || row.referenceId,
        media:
          found?.media.find(
            (item) => item.id === row.mediaId && item.type === "image",
          ) || null,
      };
    }),
  );
}
