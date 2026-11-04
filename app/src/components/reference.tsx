"use client";
import Link from "next/link";
import styles from "@/design/reference-values.module.css";
import { useEffect, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  Bookmark,
  Check,
  ChevronLeft,
  ChevronRight,
  ExternalLink,
  Pin,
  Plus,
  Minus,
  X,
} from "lucide-react";
import type {
  LibraryItem,
  LibraryDetail,
  ReferenceValue,
} from "@/contracts/library";
import {
  api,
  CopyButton,
  DownloadButton,
  Empty,
  ErrorState,
  MediaPreview,
  Modal,
  Spinner,
} from "./shared";
export function ReferenceCard({
  item,
  onOpen,
  onSelect,
  selected = false,
  style = false,
}: {
  item: LibraryItem;
  onOpen?: (item: LibraryItem) => void;
  onSelect?: (item: LibraryItem) => void;
  selected?: boolean;
  style?: boolean;
}) {
  const content = (
    <>
      <div className="card-picture">
        <MediaPreview image={item.image} video={item.video} name={item.name} />
      </div>
      <div className="card-meta">
        {item.icon ? (
          <img
            className="reference-icon"
            src={item.icon}
            alt=""
            loading="lazy"
          />
        ) : (
          <span className="reference-letter">{item.name.charAt(0)}</span>
        )}
        <div>
          <h3>{item.name}</h3>
          <p>
            {item.platform || item.category || "Design reference"}{" "}
            <span>·</span>{" "}
            {item.evidence === "measured" ? "Measured" : "Interpreted"}
          </p>
        </div>
        <ArrowRight className="card-arrow" size={17} />
      </div>
    </>
  );
  return (
    <article
      className={`reference-card ${style ? "style-card" : ""} ${selected ? "selected" : ""}`}
    >
      {onOpen ? (
        <button className="card-open" onClick={() => onOpen(item)}>
          {content}
        </button>
      ) : (
        <Link
          className="card-open"
          href={`/styles/${item.source}/${item.slug}`}
        >
          {content}
        </Link>
      )}
      {onSelect && (
        <button
          className={`card-select icon-button ${selected ? "selected" : ""}`}
          onClick={() => onSelect(item)}
          aria-label={`${selected ? "Remove" : "Add"} ${item.name} ${selected ? "from" : "to"} comparison`}
          aria-pressed={selected}
        >
          {selected ? <Check size={16} /> : <Plus size={16} />}
        </button>
      )}
    </article>
  );
}
interface Collection {
  id: string;
  name: string;
  itemCount?: number;
}
export function SaveReference({
  item,
  compact = false,
}: {
  item: LibraryItem;
  compact?: boolean;
}) {
  const [open, setOpen] = useState(false),
    [collections, setCollections] = useState<Collection[]>([]),
    [selected, setSelected] = useState(""),
    [name, setName] = useState(""),
    [note, setNote] = useState(""),
    [saved, setSaved] = useState(false),
    [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  useEffect(() => {
    if (open)
      api("/api/collections")
        .then((d) => {
          setCollections(d.collections || []);
          setSelected((current) =>
            d.collections?.some((c: Collection) => c.id === current)
              ? current
              : d.collections?.[0]?.id || "",
          );
        })
        .catch((e) => setError(e.message));
  }, [open]);
  async function save() {
    setBusy(true);
    setError("");
    try {
      let id = selected;
      if (name.trim()) {
        const d = await api("/api/collections", {
          method: "POST",
          body: JSON.stringify({ name: name.trim() }),
        });
        id = d.collection?.id || d.id;
        setSelected(id);
        setName("");
        setCollections((previous) => [d.collection || d, ...previous]);
      }
      if (!id) throw new Error("Choose a collection or create one.");
      await api(`/api/collections/${id}/items`, {
        method: "POST",
        body: JSON.stringify({
          referenceId: item.id,
          ...(note.trim() ? { note: note.trim() } : {}),
        }),
      });
      setSaved(true);
      setSelected(id);
      setName("");
      setNote("");
      setOpen(false);
      setTimeout(() => setSaved(false), 2500);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  return (
    <>
      <button
        className={compact ? "icon-button" : "pill"}
        onClick={() => setOpen(true)}
        aria-label={`Save ${item.name} to a collection`}
      >
        {saved ? <Check size={16} /> : <Bookmark size={16} />}{" "}
        {!compact && (saved ? "Saved" : "Save to collection")}
      </button>
      <Modal
        open={open}
        onOpenChange={setOpen}
        title={`Save ${item.name}`}
        description="Keep a reference together with the reason you chose it."
      >
        <form
          className="dialog-form"
          onSubmit={(e) => {
            e.preventDefault();
            save();
          }}
        >
          {collections.length > 0 && (
            <label>
              Collection
              <select
                value={selected}
                onChange={(e) => {
                  setSelected(e.target.value);
                  setName("");
                }}
              >
                {collections.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.name}
                  </option>
                ))}
              </select>
            </label>
          )}
          <label>
            {collections.length
              ? "Or create a new collection"
              : "New collection name"}
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g. Thoughtful onboarding"
              required={!collections.length}
            />
          </label>
          <label>
            Note <span className="muted">(optional)</span>
            <textarea
              rows={3}
              value={note}
              onChange={(e) => setNote(e.target.value)}
              placeholder="What makes this reference useful?"
            />
          </label>
          {error && (
            <p role="alert" className="error-text">
              {error}
            </p>
          )}
          <button className="primary" type="submit" disabled={busy}>
            {busy ? "Saving…" : "Save reference"}
          </button>
        </form>
      </Modal>
    </>
  );
}
export function ReferenceValues({
  title,
  values,
  kind,
  previewLimit,
}: {
  title: string;
  values: ReferenceValue[];
  kind?: "color" | "type";
  previewLimit?: number;
}) {
  const [expanded, setExpanded] = useState(false);
  const [copyStatus, setCopyStatus] = useState("");
  useEffect(() => {
    setExpanded(false);
    setCopyStatus("");
  }, [title, values]);
  if (!values?.length) return null;
  const initialCount = previewLimit ?? (kind === "color" ? 36 : 30);
  const visibleValues = expanded ? values : values.slice(0, initialCount);
  async function copy(value: string) {
    try {
      await navigator.clipboard.writeText(value);
      setCopyStatus(`Copied ${value}`);
    } catch {
      setCopyStatus(
        "Clipboard unavailable. Select the displayed value to copy it.",
      );
    }
  }
  return (
    <section className={`reference-section ${styles.values}`}>
      <div className="section-heading">
        <h2>{title}</h2>
        <small className="muted">{values.length} values</small>
      </div>
      <div className={kind === "color" ? styles.colorGrid : undefined}>
        {visibleValues.map((v, i) =>
          kind === "color" ? (
            <button
              className={styles.colorValue}
              key={`${v.name}-${i}`}
              title={`Copy ${v.name}: ${v.value}`}
              onClick={() => copy(v.value)}
            >
              <span
                className={styles.colorSwatch}
                style={{
                  background:
                    /^(#|rgb|hsl|oklch|color|transparent|white|black)/i.test(
                      v.value,
                    )
                      ? v.value
                      : "var(--surface-raised)",
                }}
              />
              <strong>{v.name}</strong>
              <code>{v.value}</code>
              {v.evidence && (
                <span className={styles.evidence}>{v.evidence}</span>
              )}
            </button>
          ) : (
            <div
              className={`${styles.valueRow} ${kind === "type" ? styles.typeRow : ""}`}
              key={`${v.name}-${i}`}
            >
              <div>
                <strong>{v.name}</strong>
                {v.role && <small>{v.role}</small>}
                {v.evidence && (
                  <span className={styles.evidence}>{v.evidence}</span>
                )}
              </div>
              <code>{v.value}</code>
            </div>
          ),
        )}
      </div>
      {values.length > initialCount && (
        <div className={styles.controls}>
          <button
            className="pill small"
            aria-expanded={expanded}
            onClick={() => setExpanded((v) => !v)}
          >
            {expanded
              ? `Show fewer ${kind === "color" ? "colors" : "values"}`
              : `Show all ${values.length} ${kind === "color" ? "colors" : "values"}`}
          </button>
          <span>
            {expanded ? values.length : initialCount} of {values.length}{" "}
            displayed
          </span>
        </div>
      )}
      <p className={styles.copyStatus} role="status" aria-live="polite">
        {copyStatus}
      </p>
    </section>
  );
}
export function DetailOverview({
  detail,
  inspector = false,
  onOpen,
}: {
  detail: LibraryDetail;
  inspector?: boolean;
  onOpen?: (item: LibraryItem) => void;
}) {
  return (
    <div className="detail-overview">
      <div className="detail-main-preview">
        <MediaPreview
          image={detail.image}
          video={detail.video}
          name={detail.name}
          always
        />
      </div>
      <div className="detail-title">
        {detail.icon ? (
          <img src={detail.icon} alt="" />
        ) : (
          <span className="reference-letter large">{detail.name[0]}</span>
        )}
        <div>
          <div className="eyebrow">
            {detail.source === "systems"
              ? "Measured package"
              : "Refero reference"}
          </div>
          <h1>{detail.name}</h1>
        </div>
      </div>
      <p className="detail-description">
        {detail.descriptionLong || detail.description}
      </p>
      <div className="tag-row">
        {[detail.platform, ...detail.themes, ...detail.tags]
          .filter(Boolean)
          .slice(0, 8)
          .map((x, i) => (
            <span className="tag" key={x + i}>
              {x}
            </span>
          ))}
      </div>
      <div className="detail-actions">
        <SaveReference item={detail} />
        {detail.sourceUrl && (
          <a
            href={detail.sourceUrl}
            className="pill"
            target="_blank"
            rel="noreferrer"
          >
            Visit website
            <ExternalLink size={14} />
          </a>
        )}
        {inspector && (
          <Link
            href={`/styles/${detail.source}/${detail.slug}`}
            className="pill"
          >
            Style documentation
            <ArrowRight size={14} />
          </Link>
        )}
      </div>
      <div className="evidence-note">
        <span className="evidence-dot" />
        <div>
          <strong>
            {detail.evidence === "measured"
              ? "Values measured from the product"
              : "Third-party interpretation"}
          </strong>
          <p>
            {detail.evidence === "measured"
              ? "Use the evidence labels with each value. Screenshots show layout and proportion."
              : "Use for inspiration. Prefer a measured package when the library holds the same value."}
            {detail.captured ? ` Captured ${detail.captured}.` : ""}
          </p>
        </div>
      </div>
      <ReferenceValues
        title="Color palette"
        values={detail.colors}
        kind="color"
      />
      <ReferenceValues
        title="Typography"
        values={detail.typography}
        kind="type"
      />
      <ReferenceValues title="Spacing" values={detail.spacing} />
      <ReferenceValues title="Shape & radius" values={detail.radii} />
      {detail.guidelines?.length > 0 && (
        <section className="reference-section">
          <h2>Design notes</h2>
          <ul className="guidelines">
            {detail.guidelines.map((x, i) => (
              <li key={i}>{x}</li>
            ))}
          </ul>
        </section>
      )}
      {detail.media
        ?.filter((m) => m.url !== detail.image && m.type === "image")
        .slice(0, 6)
        .map((m) => (
          <section className="reference-section" key={m.id}>
            <h2>{m.name}</h2>
            <a href={m.url} target="_blank" rel="noreferrer">
              <img
                className="detail-extra-media"
                src={m.url}
                alt={m.name}
                loading="lazy"
              />
            </a>
          </section>
        ))}
      {detail.related?.length > 0 && (
        <section className="reference-section">
          <h2>Keep exploring</h2>
          <div className="reference-grid related-grid">
            {detail.related.slice(0, 4).map((item) => (
              <ReferenceCard key={item.id} item={item} onOpen={onOpen} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
export function ExportPanel({ detail }: { detail: LibraryDetail }) {
  const keys = Object.keys(detail.exports || {}),
    [tab, setTab] = useState(
      keys.includes("DESIGN.md") ? "DESIGN.md" : keys[0] || "DESIGN.md",
    ),
    [wrap, setWrap] = useState(true),
    [value, setValue] = useState(""),
    [loading, setLoading] = useState(true),
    [error, setError] = useState("");
  useEffect(() => {
    const k = Object.keys(detail.exports || {});
    setTab(k.includes("DESIGN.md") ? "DESIGN.md" : k[0] || "DESIGN.md");
  }, [detail.id]);
  useEffect(() => {
    let live = true;
    const url = detail.exports?.[tab];
    setValue("");
    setError("");
    setLoading(true);
    if (!url) {
      setLoading(false);
      setError("No export is available for this reference.");
      return;
    }
    fetch(url)
      .then(async (r) => {
        if (!r.ok) throw new Error("The export could not be loaded.");
        return r.text();
      })
      .then((text) => {
        if (live) setValue(text);
      })
      .catch((e) => {
        if (live) setError(e.message);
      })
      .finally(() => {
        if (live) setLoading(false);
      });
    return () => {
      live = false;
    };
  }, [tab, detail.id]);
  return (
    <section className="export-panel" aria-label="Reference exports">
      <div className="export-tabs" role="tablist" aria-label="Export format">
        {keys.map((key) => (
          <button
            role="tab"
            aria-selected={tab === key}
            className={tab === key ? "active" : ""}
            key={key}
            onClick={() => setTab(key)}
          >
            {key}
          </button>
        ))}
      </div>
      <div className="export-toolbar">
        <button
          className="text-button"
          onClick={() => setWrap((v) => !v)}
          aria-pressed={wrap}
        >
          {wrap ? "Wrap on" : "Wrap off"}
        </button>
        <div className="spacer" />
        {!loading && !error && (
          <>
            <CopyButton value={value} />
            <DownloadButton value={value} name={`${detail.slug}-${tab}`} />
          </>
        )}
      </div>
      {loading ? (
        <Spinner label="Loading export…" />
      ) : error ? (
        <div className="export-error">
          <ErrorState message={error} />
        </div>
      ) : (
        <pre className={wrap ? "wrap" : ""} role="tabpanel" tabIndex={0}>
          <code>{value}</code>
        </pre>
      )}
      <div className="export-footnote">
        {detail.evidence === "measured"
          ? "Measured package · consult evidence labels before reuse"
          : "Interpreted reference · inspiration, not measured evidence"}
      </div>
    </section>
  );
}
export function ReferenceInspector({
  items,
  current,
  onClose,
  onChange,
  onPin,
  onExclude,
  pinnedIds = [],
  excludedIds = [],
}: {
  items: LibraryItem[];
  current: LibraryItem | null;
  onClose: () => void;
  onChange: (item: LibraryItem) => void;
  onPin?: (id: string) => void;
  onExclude?: (id: string) => void;
  pinnedIds?: string[];
  excludedIds?: string[];
}) {
  const [detail, setDetail] = useState<LibraryDetail | null>(null),
    [error, setError] = useState("");
  useEffect(() => {
    if (!current) return;
    let live = true;
    setDetail(null);
    setError("");
    api<LibraryDetail>(`/api/library/${current.source}/${current.slug}`)
      .then((d) => {
        if (live) setDetail((d as any).reference || d);
      })
      .catch((e) => {
        if (live) setError(e.message);
      });
    return () => {
      live = false;
    };
  }, [current?.id]);
  const index = items.findIndex((i) => i.id === current?.id);
  function move(step: number) {
    if (items.length > 1)
      onChange(items[(index + step + items.length) % items.length]);
  }
  useEffect(() => {
    if (!current) return;
    function key(e: KeyboardEvent) {
      if (
        ["INPUT", "TEXTAREA", "SELECT"].includes(
          (e.target as HTMLElement).tagName,
        )
      )
        return;
      if (e.key === "ArrowRight") {
        e.preventDefault();
        move(1);
      }
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        move(-1);
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [current?.id, items]);
  return (
    <Modal
      open={!!current}
      onOpenChange={(v) => {
        if (!v) onClose();
      }}
      title={current?.name || "Reference"}
      className="inspector-modal"
    >
      <div className="inspector-toolbar">
        <span className="muted small-text">
          {index + 1} of {items.length} references
        </span>
        <div className="spacer" />
        {onPin && current && (
          <button
            className={`pill small ${pinnedIds.includes(current.id) ? "active" : ""}`}
            onClick={() => onPin(current.id)}
          >
            <Pin size={14} />
            {pinnedIds.includes(current.id) ? "Pinned" : "Pin direction"}
          </button>
        )}
        {onExclude && current && (
          <button className="pill small" onClick={() => onExclude(current.id)}>
            <Minus size={14} />
            {excludedIds.includes(current.id) ? "Restore" : "Exclude"}
          </button>
        )}
        <button
          className="icon-button"
          onClick={() => move(-1)}
          disabled={items.length < 2}
          aria-label="Previous reference"
        >
          <ChevronLeft size={18} />
        </button>
        <button
          className="icon-button"
          onClick={() => move(1)}
          disabled={items.length < 2}
          aria-label="Next reference"
        >
          <ChevronRight size={18} />
        </button>
      </div>
      <div className="inspector-body">
        {error ? (
          <ErrorState message={error} />
        ) : detail ? (
          <DetailOverview detail={detail} inspector onOpen={onChange} />
        ) : (
          <Spinner label="Inspecting reference…" />
        )}
      </div>
    </Modal>
  );
}
export function Comparison({
  items,
  onClose,
}: {
  items: LibraryItem[];
  onClose: () => void;
}) {
  const [details, setDetails] = useState<LibraryDetail[]>([]),
    [error, setError] = useState("");
  useEffect(() => {
    let live = true;
    Promise.all(
      items.map((i) =>
        api<LibraryDetail>(`/api/library/${i.source}/${i.slug}`),
      ),
    )
      .then((d) => {
        if (live) setDetails(d.map((x) => (x as any).reference || x));
      })
      .catch((e) => setError(e.message));
    return () => {
      live = false;
    };
  }, [items]);
  return (
    <Modal
      open={true}
      onOpenChange={(v) => {
        if (!v) onClose();
      }}
      title="Compare references"
      description="Compare actual values side by side. Each reference keeps its evidence level."
      className="comparison-modal"
    >
      {error ? (
        <ErrorState message={error} />
      ) : details.length ? (
        <div
          className="comparison-grid"
          style={{
            gridTemplateColumns: `repeat(${details.length},minmax(0,1fr))`,
          }}
        >
          {details.map((d) => (
            <article key={d.id}>
              <MediaPreview image={d.image} name={d.name} />
              <h2>{d.name}</h2>
              <p className="muted">
                {d.evidence === "measured" ? "Measured" : "Interpreted"} ·{" "}
                {d.platform}
              </p>
              <p>{d.description}</p>
              <ComparisonValues detail={d} />
              <SaveReference item={d} />
            </article>
          ))}
        </div>
      ) : (
        <Spinner label="Loading comparison…" />
      )}
    </Modal>
  );
}

export function ComparisonValues({ detail }: { detail: LibraryDetail }) {
  return (
    <>
      <ReferenceValues
        title="Colors"
        values={detail.colors}
        kind="color"
        previewLimit={8}
      />
      <ReferenceValues
        title="Typography"
        values={detail.typography}
        kind="type"
        previewLimit={5}
      />
      <ReferenceValues
        title="Spacing"
        values={detail.spacing}
        previewLimit={5}
      />
    </>
  );
}
