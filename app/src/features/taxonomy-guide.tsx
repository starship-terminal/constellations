"use client";
import { useState } from "react";
import { taxonomyGroups, taxonomySnapshots } from "@/contracts/taxonomy";
import styles from "./knowledge/knowledge.module.css";

const scopes = [
  ["", "Everything"],
  ["website", "Websites"],
  ["ios-app", "iOS apps"],
  ["web-screen", "Web screens"],
  ["ios-screen", "iOS screens"],
  ["style", "Styles"],
] as const;

export function TaxonomyGuide() {
  const [scope, setScope] = useState("");
  const [query, setQuery] = useState("");
  const groups = taxonomyGroups
    .filter((group) => !scope || group.appliesTo.includes(scope))
    .map((group) => ({
      ...group,
      terms: group.terms.filter((term) =>
        `${term.label} ${term.subgroup || ""} ${group.label}`
          .toLocaleLowerCase()
          .includes(query.trim().toLocaleLowerCase()),
      ),
    }))
    .filter((group) => group.terms.length);
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <h1>Categorisation guide</h1>
        <p>
          Use Refero’s vocabulary when adding websites, apps and screenshots.
          Choose the product category first, then describe each screen’s
          purpose, interaction patterns and UI elements. Apply labels only when
          the capture supports them.
        </p>
        <p>
          Styles search suggestions are inspiration prompts. Existing style
          classifications in this library are locally generated and remain
          separate from Refero’s vocabulary.
        </p>
      </header>
      <form
        className={styles.links}
        onSubmit={(event) => event.preventDefault()}
      >
        <label>
          Content type{" "}
          <select
            value={scope}
            onChange={(event) => setScope(event.target.value)}
          >
            {scopes.map(([value, label]) => (
              <option value={value} key={value}>
                {label}
              </option>
            ))}
          </select>
        </label>
        <label>
          Find a label{" "}
          <input
            type="search"
            value={query}
            placeholder="e.g. Dashboard"
            onChange={(event) => setQuery(event.target.value)}
          />
        </label>
        <a href="/api/taxonomy" download="refero-taxonomy.json">
          Download vocabulary
        </a>
      </form>
      <p className="muted" role="status" aria-live="polite">
        {groups.reduce((sum, group) => sum + group.terms.length, 0)} matching
        entries across {groups.length} groups. Labels may occur in more than one
        group.
      </p>
      <div className={styles.grid}>
        {groups.map((group) => (
          <section className={styles.card} key={group.id} id={group.id}>
            <h2>{group.label}</h2>
            <p>
              {group.appliesTo
                .map(
                  (value) =>
                    scopes.find(([key]) => key === value)?.[1] || value,
                )
                .join(", ")}
            </p>
            {group.kind === "search-preset" && (
              <strong>Search suggestions, not classification tags</strong>
            )}
            <ul>
              {group.terms.map((term) => (
                <li key={term.id}>
                  {term.label}
                  {term.subgroup && <small> · {term.subgroup}</small>}
                </li>
              ))}
            </ul>
            <a href={group.sourceUrl} target="_blank" rel="noreferrer">
              View original source
            </a>
          </section>
        ))}
      </div>
      {!groups.length && (
        <p>No labels match. Try another content type or search.</p>
      )}
      <details className={styles.section}>
        <summary>Source and coverage</summary>
        {taxonomySnapshots.map((snapshot) => (
          <p key={snapshot.source}>
            <a href={snapshot.source} target="_blank" rel="noreferrer">
              {snapshot.source}
            </a>
            {" · Captured "}
            {snapshot.capturedAt}. {snapshot.coverage}
          </p>
        ))}
        <p>
          This guide defines available labels. It does not assign them to
          existing captures. Keep uncertain items unclassified until reviewed.
        </p>
      </details>
    </div>
  );
}
