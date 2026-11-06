import catalogSnapshot from "@/data/refero-catalog-taxonomy.json";
import stylesSnapshot from "@/data/refero-styles-taxonomy.json";

export type TaxonomyGroupKind = "taxonomy" | "search-preset";
export interface TaxonomyTerm {
  readonly id: string;
  readonly label: string;
  readonly sourceUrl?: string;
  readonly subgroup?: string;
  readonly sourceIds?: readonly string[];
}
export interface TaxonomyGroup {
  readonly id: string;
  readonly label: string;
  readonly kind: TaxonomyGroupKind;
  readonly appliesTo: readonly string[];
  readonly sourceUrl: string;
  readonly coverage: string;
  readonly terms: readonly TaxonomyTerm[];
}
export interface TaxonomySnapshot {
  readonly source: string;
  readonly capturedAt: string;
  readonly coverage: string;
  readonly groups: readonly TaxonomyGroup[];
}
interface SnapshotInput {
  source: string;
  capturedAt: string;
  coverage: string;
  groups: {
    id: string;
    label: string;
    kind?: string;
    appliesTo: string[];
    sourceUrl: string;
    coverage: string;
    terms: {
      label: string;
      sourceUrl?: string;
      subgroup?: string;
      sourceIds?: string[];
    }[];
  }[];
}

/** Keep Unicode names readable while making punctuation safe in a term ID. */
export function taxonomyTermId(groupId: string, label: string): string {
  const normalized = label.normalize("NFKC").toLowerCase();
  const slug = normalized
    .replace(/[^\p{L}\p{N}]+/gu, "-")
    .replace(/^-|-$/g, "");
  const fallback = [...normalized]
    .map((character) => character.codePointAt(0)!.toString(16))
    .join("-");
  return `${groupId}:${slug || `u-${fallback}`}`;
}

/** A guide vocabulary never assigns classifications to existing assets. */
export function createTaxonomySnapshots(
  inputs: readonly SnapshotInput[],
): readonly TaxonomySnapshot[] {
  const groupIds = new Set<string>();
  const termIds = new Set<string>();
  return Object.freeze(
    inputs.map((snapshot) =>
      Object.freeze({
        source: snapshot.source,
        capturedAt: snapshot.capturedAt,
        coverage: snapshot.coverage,
        groups: Object.freeze(
          snapshot.groups.map((group): TaxonomyGroup => {
            if (groupIds.has(group.id))
              throw new Error(`Duplicate taxonomy group ID: ${group.id}`);
            groupIds.add(group.id);
            if (
              group.kind !== undefined &&
              group.kind !== "taxonomy" &&
              group.kind !== "search-preset"
            )
              throw new Error(`Unknown taxonomy group kind: ${group.kind}`);
            return Object.freeze({
              ...group,
              kind: group.kind || "taxonomy",
              appliesTo: Object.freeze([...group.appliesTo]),
              terms: Object.freeze(
                group.terms.map((term) => {
                  const id = taxonomyTermId(group.id, term.label);
                  if (termIds.has(id))
                    throw new Error(`Duplicate taxonomy term ID: ${id}`);
                  termIds.add(id);
                  return Object.freeze({
                    ...term,
                    id,
                    ...(term.sourceIds
                      ? { sourceIds: Object.freeze([...term.sourceIds]) }
                      : {}),
                  });
                }),
              ),
            });
          }),
        ),
      }),
    ),
  );
}

export const taxonomySnapshots = createTaxonomySnapshots([
  catalogSnapshot,
  stylesSnapshot,
]);
export const taxonomyGroups: readonly TaxonomyGroup[] = Object.freeze(
  taxonomySnapshots.flatMap((snapshot) => snapshot.groups),
);

/** Filter reference groups only; this does not filter or classify media. */
export function groupsForTaxonomy(
  appliesTo?: string,
): readonly TaxonomyGroup[] {
  return appliesTo
    ? taxonomyGroups.filter((group) => group.appliesTo.includes(appliesTo))
    : taxonomyGroups;
}

/** Accept only a recorded label in its stated group, without alias inference. */
export function findTaxonomyTerm(
  groupId: string,
  label: string,
): TaxonomyTerm | undefined {
  return taxonomyGroups
    .find((group) => group.id === groupId)
    ?.terms.find((term) => term.label === label);
}

export interface TaxonomyLabelValidation {
  readonly valid: boolean;
  readonly terms: readonly TaxonomyTerm[];
  readonly unknownLabels: readonly string[];
  readonly reason?: "unknown-group" | "search-preset";
}

/** Membership validates proposed labels, never the evidence for assigning them. */
export function validateTaxonomyLabels(
  groupId: string,
  labels: readonly string[],
): TaxonomyLabelValidation {
  const group = taxonomyGroups.find((candidate) => candidate.id === groupId);
  const unique = [...new Set(labels)];
  if (!group || group.kind === "search-preset")
    return {
      valid: false,
      terms: [],
      unknownLabels: unique,
      reason: group ? "search-preset" : "unknown-group",
    };
  const terms: TaxonomyTerm[] = [];
  const unknownLabels: string[] = [];
  for (const label of unique) {
    const term = group.terms.find((candidate) => candidate.label === label);
    if (term) terms.push(term);
    else unknownLabels.push(label);
  }
  return { valid: unknownLabels.length === 0, terms, unknownLabels };
}
