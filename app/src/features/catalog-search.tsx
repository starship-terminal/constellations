"use client";
import {
  useEffect,
  useMemo,
  useRef,
  useState,
  type KeyboardEvent,
} from "react";
import { useSearchParams } from "next/navigation";
import { createPortal } from "react-dom";
import {
  BookOpen,
  ChevronRight,
  Layers,
  LayoutPanelTop,
  Search,
  Shapes,
  Tags,
  Type,
  X,
} from "lucide-react";
import type { LibraryItem } from "@/contracts/library";
import type { TaxonomyGroup, TaxonomyTerm } from "@/contracts/taxonomy";
import type { ScreenResponse } from "@/contracts/screens";
import { api } from "@/components/shared";
import {
  groupCaption,
  legacyCategoryLabels,
  pickerGroups,
  productSearchPlatform,
  selectProductSearch,
} from "./catalog-search-state";
import styles from "./catalog-search.module.css";
import {
  enterSearchAction,
  screenCountScope,
  verticalChoiceIndex,
} from "./catalog-search-behavior";

type Choice = {
  id: string;
  label: string;
  caption: string;
  group?: TaxonomyGroup;
  term?: TaxonomyTerm;
  item?: LibraryItem;
  query?: boolean;
};
function GroupIcon({
  group,
  size = 22,
}: {
  group: TaxonomyGroup;
  size?: number;
}) {
  const Icon = group.id.endsWith("flows")
    ? Layers
    : group.id.endsWith("ux-patterns")
      ? Shapes
      : group.id.endsWith("ui-elements")
        ? LayoutPanelTop
        : group.id.endsWith("categories")
          ? Tags
          : group.id.endsWith("fonts")
            ? Type
            : BookOpen;
  return <Icon size={size} aria-hidden="true" />;
}
export function CatalogSearch({
  taxonomy,
  items,
  taxonomyLoading,
  taxonomyError,
  retryTaxonomy,
}: {
  taxonomy: readonly TaxonomyGroup[];
  items: readonly LibraryItem[];
  taxonomyLoading: boolean;
  taxonomyError: string;
  retryTaxonomy: () => void;
}) {
  const params = useSearchParams();
  const platform = params.get("platform") || "web";
  const kind = params.get("kind") === "crop" ? "crop" : "screenshot";
  const countScope = screenCountScope(platform, kind);
  const productPlatform = productSearchPlatform(params);
  const [open, setOpen] = useState(false),
    [draft, setDraft] = useState(""),
    [groupIndex, setGroupIndex] = useState(0),
    [highlight, setHighlight] = useState(-1);
  const [counts, setCounts] = useState<Record<string, number> | null>(null),
    [countsError, setCountsError] = useState(false),
    [countRetry, setCountRetry] = useState(0);
  const countCache = useRef(new Map<string, Record<string, number>>());
  const input = useRef<HTMLInputElement>(null),
    root = useRef<HTMLDivElement>(null),
    list = useRef<HTMLDivElement>(null);
  const groups = useMemo(
    () => pickerGroups(taxonomy, platform),
    [taxonomy, platform],
  );
  const activeGroup = groups[groupIndex] || groups[0];
  useEffect(() => {
    setGroupIndex(0);
    setHighlight(-1);
  }, [platform]);
  useEffect(() => {
    let alive = true;
    setCountsError(false);
    const cached = countCache.current.get(countScope.key);
    setCounts(cached || null);
    if (cached) return;
    api<ScreenResponse>(`/api/library/screens?${countScope.query}`)
      .then((result) => {
        const values = result.termCounts || {};
        countCache.current.set(countScope.key, values);
        if (alive) setCounts(values);
      })
      .catch(() => {
        if (alive) setCountsError(true);
      });
    return () => {
      alive = false;
    };
  }, [platform, kind, countScope.key, countRetry]);
  useEffect(() => {
    if (!open) return;
    function dismiss(event: PointerEvent) {
      if (!root.current?.contains(event.target as Node)) dismissPicker();
    }
    document.addEventListener("pointerdown", dismiss);
    return () => document.removeEventListener("pointerdown", dismiss);
  }, [open]);
  function dismissPicker() {
    setOpen(false);
    setHighlight(-1);
  }
  const selectedIds = params.getAll("term");
  const chips: (Choice & { key: string; value: string })[] = [];
  for (const [key, value] of params.entries()) {
    if (key === "term") {
      const group = taxonomy.find((group) =>
        group.terms.some((term) => term.id === value),
      );
      const term = group?.terms.find((term) => term.id === value);
      chips.push({
        id: `${key}:${value}`,
        key,
        value,
        label: term?.label || value,
        caption: group ? groupCaption(group.id) : "Filter",
        group,
      });
    } else if (key === "referenceId") {
      const item = items.find((item) => item.id === value);
      chips.push({
        id: `${key}:${value}`,
        key,
        value,
        label: item?.name || value,
        caption: item?.platform === "mobile" ? "iOS App" : "Website",
        item,
      });
    } else if (
      ["q", "category", "theme", "tag", "group", "scope", "kind"].includes(
        key,
      ) &&
      value
    ) {
      if (
        (key === "scope" && value === "all") ||
        (key === "kind" && value === "screenshot")
      )
        continue;
      chips.push({
        id: `${key}:${value}`,
        key,
        value,
        label:
          key === "category" ? legacyCategoryLabels(taxonomy, value) : value,
        caption:
          key === "q"
            ? "Search"
            : key === "category"
              ? "Category"
              : key[0].toUpperCase() + key.slice(1),
      });
    }
  }
  function navigate(next: URLSearchParams) {
    next.set("view", "screens");
    next.delete("screen");
    next.delete("offset");
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}?${next}${window.location.hash}`,
    );
  }
  function remove(key: string, value: string) {
    const next = new URLSearchParams(window.location.search);
    const retained = next.getAll(key).filter((entry) => entry !== value);
    next.delete(key);
    retained.forEach((entry) => next.append(key, entry));
    navigate(next);
  }
  function clear() {
    const next = new URLSearchParams(window.location.search);
    for (const key of [
      "term",
      "referenceId",
      "q",
      "category",
      "theme",
      "tag",
      "group",
      "scope",
      "kind",
    ])
      next.delete(key);
    setDraft("");
    dismissPicker();
    navigate(next);
  }
  const typed = draft.trim();
  const choices: Choice[] = useMemo(() => {
    if (!typed)
      return (activeGroup?.terms || []).map((term) => ({
        id: term.id,
        label: term.label,
        caption: groupCaption(activeGroup.id),
        group: activeGroup,
        term,
      }));
    const words = typed.toLowerCase().split(/\s+/);
    const matches = (text: string) =>
      words.every((word) => text.toLowerCase().includes(word));
    return [
      { id: "query", label: typed, caption: "Keyword search", query: true },
      ...items
        .filter(
          (item) =>
            (!productPlatform || item.platform === productPlatform) &&
            matches(`${item.name} ${item.slug}`),
        )
        .slice(0, 8)
        .map((item) => ({
          id: item.id,
          label: item.name,
          caption: item.platform === "mobile" ? "iOS App" : "Website",
          item,
        })),
      ...groups
        .flatMap((group) =>
          group.terms
            .filter((term) => matches(term.label))
            .map((term) => ({
              id: term.id,
              label: term.label,
              caption: groupCaption(group.id),
              group,
              term,
            })),
        )
        .slice(0, 16),
    ];
  }, [typed, activeGroup, groups, items, productPlatform]);
  const highlighted = typed ? Math.max(0, highlight) : highlight;
  useEffect(() => {
    if (open && highlighted >= 0)
      document
        .getElementById(`catalog-choice-${highlighted}`)
        ?.scrollIntoView({ block: "nearest" });
  }, [highlighted, open]);
  function choose(choice: Choice) {
    if (!open) return;
    const params = new URLSearchParams(window.location.search);
    const next = choice.item
      ? selectProductSearch(params, choice.item)
      : params;
    const key = choice.query ? "q" : choice.item ? "referenceId" : "term";
    const value = choice.query ? typed : choice.id;
    if (key === "q") next.set(key, value);
    else if (!next.getAll(key).includes(value)) next.append(key, value);
    navigate(next);
    setDraft("");
    setOpen(false);
    setHighlight(-1);
    input.current?.blur();
  }
  function onKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    // IME confirmation keys finish the composed word, not a search selection.
    if (event.nativeEvent.isComposing || event.nativeEvent.keyCode === 229)
      return;
    if (event.key === "Escape") {
      event.preventDefault();
      dismissPicker();
      return;
    }
    if (event.key === "Backspace" && !draft && chips.length) {
      const last = chips.at(-1)!;
      remove(last.key, last.value);
      return;
    }
    if (event.key === "Tab" && open && !typed && groups.length) {
      event.preventDefault();
      setGroupIndex(
        (value) =>
          (value + (event.shiftKey ? -1 : 1) + groups.length) % groups.length,
      );
      setHighlight(-1);
      list.current?.scrollTo({ top: 0 });
      return;
    }
    const movement: Record<string, number> = {
      ArrowDown: 1,
      ArrowUp: -1,
      ...(!typed ? { ArrowRight: 1, ArrowLeft: -1 } : {}),
    };
    if (event.key in movement && open && choices.length) {
      event.preventDefault();
      setHighlight((current) => {
        const previous = typed ? Math.max(0, current) : current;
        if (previous < 0) return 0;
        if (!typed && ["ArrowUp", "ArrowDown"].includes(event.key)) {
          const positions = Array.from(
            list.current?.querySelectorAll<HTMLElement>("[role=option]") || [],
          ).map((element) => {
            const rectangle = element.getBoundingClientRect();
            return {
              index: Number(element.id.split("-").at(-1)),
              x: rectangle.left + rectangle.width / 2,
              y: rectangle.top,
            };
          });
          return verticalChoiceIndex(
            positions,
            previous,
            event.key === "ArrowDown" ? 1 : -1,
          );
        }
        return (
          (previous + movement[event.key] + choices.length) % choices.length
        );
      });
      return;
    }
    if (event.key === "Enter") {
      event.preventDefault();
      const choice = choices[highlighted < 0 ? 0 : highlighted];
      if (choice && enterSearchAction(open, typed, highlight) === "choose")
        choose(choice);
      else {
        setOpen(true);
        setHighlight(-1);
      }
    }
  }
  function choiceButton(choice: Choice, index: number) {
    return (
      <button
        key={choice.id}
        id={`catalog-choice-${index}`}
        type="button"
        role="option"
        aria-selected={highlighted === index}
        tabIndex={-1}
        className={`${styles.choice} ${typed ? styles.suggestion : ""} ${highlighted === index ? styles.highlighted : ""}`}
        onMouseEnter={() => setHighlight(index)}
        onClick={() => choose(choice)}
      >
        {typed && (
          <span className={styles.choiceIcon}>
            {choice.item?.icon ? (
              <img src={choice.item.icon} alt="" />
            ) : choice.group ? (
              <GroupIcon group={choice.group} />
            ) : (
              <Search size={22} />
            )}
          </span>
        )}
        <span>
          {typed && <small>{choice.caption}</small>}
          <span>{choice.label}</span>
        </span>
        {!typed && (
          <span className={styles.count}>
            {counts === null ? "…" : (counts[choice.id] || 0).toLocaleString()}
          </span>
        )}
        {selectedIds.includes(choice.id) && (
          <span className="sr-only">Selected</span>
        )}
      </button>
    );
  }
  return (
    <div ref={root} className={`${styles.root} ${open ? styles.open : ""}`}>
      {open &&
        createPortal(
          <div
            className={styles.backdrop}
            aria-hidden="true"
            onClick={dismissPicker}
          />,
          document.body,
        )}
      <div className={styles.panel}>
        <div
          className={styles.search}
          onClick={(event) => {
            if (event.target === event.currentTarget) input.current?.focus();
          }}
        >
          {chips.map((chip) => (
            <button
              type="button"
              key={chip.id}
              className={styles.chip}
              onClick={() => remove(chip.key, chip.value)}
              aria-label={`Remove ${chip.label} filter`}
            >
              <span className={styles.chipIcon}>
                {chip.item?.icon ? (
                  <img src={chip.item.icon} alt="" />
                ) : chip.group ? (
                  <GroupIcon group={chip.group} />
                ) : chip.key === "q" ? (
                  <Search size={22} />
                ) : (
                  <Tags size={22} />
                )}
                <X size={19} className={styles.chipRemove} />
              </span>
              <span>
                <small>{chip.caption}</small>
                <strong>{chip.label}</strong>
              </span>
            </button>
          ))}
          <input
            ref={input}
            aria-label="Search references"
            role="combobox"
            aria-expanded={open}
            aria-controls="catalog-search-options"
            aria-autocomplete="list"
            aria-activedescendant={
              open && highlighted >= 0
                ? `catalog-choice-${highlighted}`
                : undefined
            }
            placeholder="Search"
            value={draft}
            onFocus={() => {
              if (!open) {
                setOpen(true);
                setGroupIndex(0);
                setHighlight(-1);
              }
            }}
            onClick={() => {
              if (!open) {
                setOpen(true);
                setGroupIndex(0);
                setHighlight(-1);
              }
            }}
            onChange={(event) => {
              setDraft(event.target.value);
              setOpen(true);
              setHighlight(-1);
            }}
            onKeyDown={onKeyDown}
          />
          {(chips.length > 0 || draft) && (
            <button
              type="button"
              className={styles.clear}
              aria-label="Clear all search filters"
              onClick={clear}
            >
              <X size={17} />
            </button>
          )}
          {!chips.length && !draft && (
            <Search
              className={styles.searchGlyph}
              size={20}
              aria-hidden="true"
            />
          )}
        </div>
        {open && (
          <div
            className={`${styles.picker} ${typed ? styles.typedPicker : ""}`}
          >
            {taxonomyLoading ? (
              <p role="status" className={styles.notice}>
                Loading search filters…
              </p>
            ) : taxonomyError ? (
              <div role="alert" className={styles.notice}>
                {taxonomyError}{" "}
                <button type="button" onClick={retryTaxonomy}>
                  Try again
                </button>
              </div>
            ) : (
              <>
                {!typed && (
                  <nav className={styles.groups} aria-label="Filter groups">
                    {groups.map((group, index) => (
                      <button
                        type="button"
                        key={group.id}
                        aria-pressed={activeGroup?.id === group.id}
                        onClick={() => {
                          setGroupIndex(index);
                          setHighlight(-1);
                          list.current?.scrollTo({ top: 0 });
                          input.current?.focus();
                        }}
                      >
                        <GroupIcon group={group} />
                        <span>{group.label}</span>
                        <ChevronRight size={16} />
                      </button>
                    ))}
                  </nav>
                )}
                <div
                  ref={list}
                  id="catalog-search-options"
                  className={`${styles.options} ${typed ? styles.typed : ""}`}
                  role="listbox"
                  aria-label={typed ? "Search suggestions" : activeGroup?.label}
                >
                  {countsError && !typed && (
                    <p className={styles.notice}>
                      Counts unavailable.{" "}
                      <button
                        type="button"
                        onClick={() => {
                          countCache.current.delete(countScope.key);
                          setCountRetry((value) => value + 1);
                        }}
                      >
                        Retry counts
                      </button>
                    </p>
                  )}
                  {typed
                    ? choices.map(choiceButton)
                    : [
                        ...new Set(
                          activeGroup?.terms.map(
                            (term) => term.subgroup || "",
                          ) || [],
                        ),
                      ].map((subgroup) => (
                        <section key={subgroup} className={styles.section}>
                          {subgroup && <h2>{subgroup}</h2>}
                          <div className={styles.termGrid}>
                            {choices.map((choice, index) =>
                              choice.term?.subgroup === subgroup ||
                              (!choice.term?.subgroup && !subgroup)
                                ? choiceButton(choice, index)
                                : null,
                            )}
                          </div>
                        </section>
                      ))}
                </div>
              </>
            )}
            <div className={styles.keyboardHints}>
              {!typed && (
                <span>
                  <kbd>Tab</kbd> <kbd>Shift + Tab</kbd> Switch tabs
                </span>
              )}
              <span>
                <kbd>↑</kbd> <kbd>↓</kbd>{" "}
                {!typed && (
                  <>
                    <kbd>←</kbd> <kbd>→</kbd>{" "}
                  </>
                )}
                Navigate
              </span>
              <span>
                <kbd>Enter</kbd> Select
              </span>
              <span>
                <kbd>Esc</kbd> Close
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
