import type { ScreenItem } from "@/contracts/screens";
/** Rotate across products before showing a second capture from the same one. */
export function sampleBrowseScreens(
  items: ScreenItem[],
  limit = 8,
): ScreenItem[] {
  const groups = new Map<string, ScreenItem[]>();
  for (const item of items) {
    const group = groups.get(item.reference.id) || [];
    group.push(item);
    groups.set(item.reference.id, group);
  }
  const chosen: ScreenItem[] = [];
  for (let round = 0; chosen.length < limit; round++) {
    let found = false;
    for (const group of groups.values()) {
      if (group[round]) {
        chosen.push(group[round]);
        found = true;
        if (chosen.length === limit) break;
      }
    }
    if (!found) break;
  }
  return chosen;
}
