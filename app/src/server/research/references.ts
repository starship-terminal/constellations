import { getReferenceSummary } from "@/server/sources";
import { HttpError } from "./http";
export async function validateReferences(
  pinnedIds: string[],
  excludedIds: string[],
) {
  if (pinnedIds.some((id) => excludedIds.includes(id)))
    throw new HttpError(400, "A reference cannot be both pinned and excluded.");
  // Existence needs only the cached card, never a package's documents or media.
  const ids = [...new Set([...pinnedIds, ...excludedIds])];
  const found = await Promise.all(ids.map((id) => getReferenceSummary(id)));
  const missing = ids.find((_, index) => !found[index]);
  if (missing) throw new HttpError(400, `Unknown reference: ${missing}`);
}
