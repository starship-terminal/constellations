import type { LibraryItem } from "@/contracts/library";
import { getStore, type ResearchStore } from "@/server/db";

/** Apply app-owned classification without altering captured source evidence. */
export async function withReferenceCategories<T extends LibraryItem>(
  items: T[],
  store?: ResearchStore,
): Promise<T[]> {
  const referenceIds = items
    .filter((item) => item.source === "systems")
    .map((item) => item.id);
  if (referenceIds.length === 0) return items;
  const database = store || (await getStore());
  const assignments = await database.listReferenceCategoryDetails(referenceIds);
  const byReference = new Map<string, { id: string; label: string }[]>();
  for (const assignment of assignments) {
    const values = byReference.get(assignment.referenceId) || [];
    values.push({ id: assignment.termId, label: assignment.label });
    byReference.set(assignment.referenceId, values);
  }
  return items.map((item) => {
    if (item.source !== "systems") return item;
    const categories = byReference.get(item.id) || [];
    return {
      ...item,
      categoryIds: categories.map((term) => term.id),
      categories,
      category: categories[0]?.label || "",
    };
  });
}
