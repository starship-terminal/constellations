import { getReference } from "@/server/sources";
import { HttpError } from "./http";
export async function validateReferences(
  pinnedIds: string[],
  excludedIds: string[],
) {
  if (pinnedIds.some((id) => excludedIds.includes(id)))
    throw new HttpError(400, "A reference cannot be both pinned and excluded.");
  for (const id of [...pinnedIds, ...excludedIds])
    if (!(await getReference(id)))
      throw new HttpError(400, `Unknown reference: ${id}`);
}
