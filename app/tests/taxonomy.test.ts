import { describe, expect, it } from "vitest";
import {
  createTaxonomySnapshots,
  findTaxonomyTerm,
  groupsForTaxonomy,
  taxonomyGroups,
  taxonomySnapshots,
  taxonomyTermId,
  validateTaxonomyLabels,
} from "@/contracts/taxonomy";

const snapshot = {
  source: "https://refero.design",
  capturedAt: "2026-11-04",
  coverage: "Observed vocabulary",
  groups: [
    {
      id: "web:page-types",
      label: "Page types",
      appliesTo: ["websites"],
      sourceUrl: "https://refero.design",
      coverage: "Observed terms",
      terms: [
        { label: "Sign up", subgroup: "Account", sourceIds: ["original-row"] },
      ],
    },
  ],
};

describe("shared Refero guide vocabulary", () => {
  it("keeps namespaced IDs deterministic across punctuation and Unicode", () => {
    expect(taxonomyTermId("web:pages", "Sign up / Log in")).toBe(
      "web:pages:sign-up-log-in",
    );
    expect(taxonomyTermId("ios:pages", "Sign up / Log in")).not.toBe(
      taxonomyTermId("web:pages", "Sign up / Log in"),
    );
    expect(taxonomyTermId("web:pages", "Cafe\u0301 東京")).toBe(
      "web:pages:café-東京",
    );
    expect(taxonomyTermId("web:pages", "!")).not.toBe(
      taxonomyTermId("web:pages", "?"),
    );
  });

  it("rejects duplicate group identities and labels that produce duplicate term IDs", () => {
    expect(() => createTaxonomySnapshots([snapshot, snapshot])).toThrow(
      "Duplicate taxonomy group ID",
    );
    expect(() =>
      createTaxonomySnapshots([
        {
          ...snapshot,
          groups: [
            {
              ...snapshot.groups[0],
              terms: [{ label: "Sign up" }, { label: "Sign-up" }],
            },
          ],
        },
      ]),
    ).toThrow("Duplicate taxonomy term ID");
    const other = {
      ...snapshot,
      groups: [{ ...snapshot.groups[0], id: "ios:page-types" }],
    };
    expect(createTaxonomySnapshots([snapshot, other])).toHaveLength(2);
  });

  it("retains capture provenance and subgroups without sharing mutable input arrays", () => {
    const input = structuredClone(snapshot);
    const result = createTaxonomySnapshots([input]);
    input.groups[0].terms[0].label = "Changed";
    input.groups[0].terms[0].sourceIds.push("another-row");
    expect(result[0].source).toBe(snapshot.source);
    expect(result[0].capturedAt).toBe(snapshot.capturedAt);
    expect(result[0].groups[0].terms[0]).toMatchObject({
      label: "Sign up",
      subgroup: "Account",
      sourceIds: ["original-row"],
    });
    expect(Object.isFrozen(result[0].groups[0].terms[0])).toBe(true);
    expect(Object.isFrozen(result[0].groups[0].terms[0].sourceIds)).toBe(true);
    expect(Object.isFrozen(result[0].groups[0].appliesTo)).toBe(true);
  });

  it("loads both captured sources with unique IDs and filters only stated applicability", () => {
    expect(taxonomySnapshots).toHaveLength(2);
    expect(taxonomyGroups.length).toBeGreaterThan(0);
    const ids = taxonomyGroups.flatMap((group) =>
      group.terms.map((term) => term.id),
    );
    expect(new Set(ids).size).toBe(ids.length);
    for (const scope of new Set(taxonomyGroups.flatMap((g) => g.appliesTo))) {
      const expected = taxonomyGroups.filter((g) =>
        g.appliesTo.includes(scope),
      );
      expect(groupsForTaxonomy(scope)).toEqual(expected);
    }
    expect(groupsForTaxonomy("unsupported-platform")).toEqual([]);
    expect(groupsForTaxonomy()).toBe(taxonomyGroups);
  });

  it("accepts recorded labels only inside the stated classification group", () => {
    const group = taxonomyGroups.find(
      (candidate) => candidate.kind === "taxonomy" && candidate.terms.length,
    )!;
    expect(group).toBeDefined();
    const label = group.terms[0].label;
    expect(findTaxonomyTerm(group.id, label)).toBe(group.terms[0]);
    expect(validateTaxonomyLabels(group.id, [label, label])).toEqual({
      valid: true,
      terms: [group.terms[0]],
      unknownLabels: [],
    });
    expect(validateTaxonomyLabels(group.id, [])).toEqual({
      valid: true,
      terms: [],
      unknownLabels: [],
    });
    const other = taxonomyGroups.find(
      (candidate) =>
        candidate.kind === "taxonomy" &&
        candidate.terms.some(
          (term) => !group.terms.some((known) => known.label === term.label),
        ),
    )!;
    const crossGroupLabel = other.terms.find(
      (term) => !group.terms.some((known) => known.label === term.label),
    )!.label;
    expect(findTaxonomyTerm(group.id, crossGroupLabel)).toBeUndefined();
    expect(validateTaxonomyLabels(group.id, [crossGroupLabel])).toEqual({
      valid: false,
      terms: [],
      unknownLabels: [crossGroupLabel],
    });
    expect(
      validateTaxonomyLabels(group.id, ["Unsupported taxonomy label"]).valid,
    ).toBe(false);
    expect(validateTaxonomyLabels("unknown-group", [label])).toMatchObject({
      valid: false,
      reason: "unknown-group",
    });
  });

  it("exposes search presets for the guide while excluding them from classification", () => {
    const presets = taxonomyGroups.filter((g) => g.kind === "search-preset");
    expect(presets.length).toBeGreaterThan(0);
    for (const group of presets) {
      const label = group.terms[0].label;
      expect(findTaxonomyTerm(group.id, label)).toBe(group.terms[0]);
      expect(validateTaxonomyLabels(group.id, [label])).toEqual({
        valid: false,
        terms: [],
        unknownLabels: [label],
        reason: "search-preset",
      });
    }
  });
});
