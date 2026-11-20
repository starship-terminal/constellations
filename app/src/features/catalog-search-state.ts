import type { LibraryItem } from "@/contracts/library";
import type { TaxonomyGroup } from "@/contracts/taxonomy";
import { matchesCategory, UNCATEGORISED } from "@/contracts/categories";

export function pickerGroups(
  groups: readonly TaxonomyGroup[],
  platform: string,
) {
  const prefix = platform === "mobile" ? "ios-" : "web-";
  return groups.filter(
    (group) => group.kind === "taxonomy" && group.id.startsWith(prefix),
  );
}
export function groupCaption(groupId: string) {
  if (groupId.endsWith("categories")) return "Category";
  if (groupId.endsWith("flows")) return "Flow";
  if (groupId.endsWith("ui-elements")) return "UI Element";
  if (groupId.endsWith("ux-patterns")) return "UX Pattern";
  if (groupId.endsWith("fonts")) return "Font";
  return groupId === "ios-screen-types" ? "Screen Type" : "Page Type";
}
export function legacyCategoryLabels(
  groups: readonly TaxonomyGroup[],
  query: string,
) {
  if (!query) return "";
  if (query === UNCATEGORISED) return "Uncategorised";
  return (
    [
      ...new Set(
        groups
          .filter((group) => group.id.endsWith("categories"))
          .flatMap((group) => group.terms)
          .filter((term) =>
            matchesCategory({ category: "", categoryIds: [term.id] }, query),
          )
          .map((term) => term.label),
      ),
    ].join(", ") || query
  );
}
/** Gallery suggestions cover every platform; screen search defaults to web. */
export function productSearchPlatform(params: Pick<URLSearchParams, "get">) {
  return (
    params.get("platform") || (params.get("view") === "screens" ? "web" : "")
  );
}
export function selectProductSearch(
  params: URLSearchParams,
  item: Pick<LibraryItem, "id" | "platform">,
) {
  const next = new URLSearchParams(params);
  if (!next.getAll("referenceId").includes(item.id))
    next.append("referenceId", item.id);
  if (!next.get("platform")) next.set("platform", item.platform);
  return next;
}

/** Legacy product links can supply platform scope once their records are known. */
export function inferredProductPlatform(
  params: Pick<URLSearchParams, "get" | "getAll">,
  items: readonly Pick<LibraryItem, "id" | "platform">[],
): string | undefined {
  const explicit = params.get("platform");
  if (explicit) return explicit;
  const ids = [...new Set(params.getAll("referenceId").filter(Boolean))];
  if (!ids.length) return undefined;
  const platforms = new Set<string>();
  for (const id of ids) {
    const item = items.find((candidate) => candidate.id === id);
    if (!item?.platform) return undefined;
    platforms.add(item.platform);
  }
  return platforms.size === 1 ? [...platforms][0] : undefined;
}
/** Keep filters with the same recorded meaning when changing platform. */
export function platformSearch(
  params: URLSearchParams,
  platform: string,
  groups: readonly TaxonomyGroup[],
  items: readonly LibraryItem[],
  productsComplete = false,
) {
  const next = new URLSearchParams(params);
  platform ? next.set("platform", platform) : next.delete("platform");
  const destinations = pickerGroups(groups, platform);
  const terms = params.getAll("term");
  next.delete("term");
  const retainTerm = (id: string) => {
    if (!next.getAll("term").includes(id)) next.append("term", id);
  };
  for (const id of terms) {
    const source = groups.find((group) =>
      group.terms.some((term) => term.id === id),
    );
    const term = source?.terms.find((term) => term.id === id);
    // Loading can expose only part of the vocabulary. Missing source evidence
    // cannot establish that a selected term is incompatible.
    if (!source || !term || !platform) {
      retainTerm(id);
      continue;
    }
    const kind = source?.id.replace(/^(web|ios)-/, "");
    const destination = destinations.find(
      (group) =>
        group.id.replace(/^(web|ios)-/, "") === kind ||
        (kind === "page-types" && group.id === "ios-screen-types") ||
        (kind === "screen-types" && group.id === "web-page-types"),
    );
    if (!destination) {
      // Refero's iOS vocabulary has no Fonts group. Other missing groups may
      // simply not have loaded yet, so keep their selections intact.
      if (!(platform === "mobile" && kind === "fonts")) retainTerm(id);
      continue;
    }
    const destinationLabel =
      destination.id === "ios-screen-types" && term.label === "Home Page"
        ? "Home"
        : destination.id === "web-page-types" && term.label === "Home"
          ? "Home Page"
          : term.label;
    const match = destination?.terms.find(
      (candidate) => candidate.label === destinationLabel,
    );
    if (match) retainTerm(match.id);
  }
  const category = params.get("category");
  if (category) {
    const categoryGroups = destinations.filter((group) =>
      group.id.endsWith("categories"),
    );
    const match = categoryGroups
      .flatMap((group) => group.terms)
      .filter((term) =>
        matchesCategory({ category: "", categoryIds: [term.id] }, category),
      );
    // A legacy alias can mean several alternatives. Keep that OR category
    // filter instead of turning its labels into an AND term selection.
    if (platform && match.length === 1) next.set("category", match[0].id);
    else if (
      platform &&
      !match.length &&
      categoryGroups.length &&
      groups
        .filter((group) => group.id.endsWith("categories"))
        .some((group) =>
          group.terms.some((term) =>
            matchesCategory({ category: "", categoryIds: [term.id] }, category),
          ),
        )
    )
      next.delete("category");
  }
  next.delete("referenceId");
  for (const id of params.getAll("referenceId")) {
    const item = items.find((candidate) => candidate.id === id);
    if (
      !platform ||
      (!item && !productsComplete) ||
      item?.platform === platform
    )
      next.append("referenceId", id);
  }
  next.delete("screen");
  next.delete("offset");
  return next;
}

/** Switching must wait until selected filters can actually be mapped. */
export function canSwitchPlatform(
  params: Pick<URLSearchParams, "has" | "getAll">,
  taxonomyReady: boolean,
  items: readonly Pick<LibraryItem, "id">[],
  productsLoading = true,
) {
  return (
    ((!params.has("term") && !params.has("category")) || taxonomyReady) &&
    (!productsLoading ||
      params
        .getAll("referenceId")
        .every((id) => items.some((item) => item.id === id)))
  );
}
