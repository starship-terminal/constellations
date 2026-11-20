"use client";
import Link from "next/link";
import * as Dialog from "@radix-ui/react-dialog";
import referenceStyles from "./reference.module.css";
import styles from "@/design/reference-values.module.css";
import { Fragment, useEffect, useRef, useState } from "react";
import {
  ArrowRight,
  Bookmark,
  Check,
  ChevronLeft,
  ChevronRight,
  ExternalLink,
  Download,
  Palette,
  Layers,
  Tag,
  BookOpen,
  Pin,
  Plus,
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
  ErrorState,
  MediaPreview,
  Modal,
  Select,
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
            decoding="async"
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
          href={
            item.source === "systems"
              ? `/library/${item.slug}`
              : `/styles/refero/${item.slug}`
          }
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
  className,
}: {
  item: LibraryItem;
  compact?: boolean;
  className?: string;
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
        id = d.id;
        setSelected(id);
        setName("");
        setCollections((previous) => [d, ...previous]);
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
        className={`${compact ? "icon-button" : "pill"} ${className || ""}`}
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
              <Select
                label="Collection"
                value={selected}
                onChange={(value) => {
                  setSelected(value);
                  setName("");
                }}
                options={collections.map((c) => ({
                  value: c.id,
                  label: c.name,
                }))}
              />
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
/** A token name that wraps after its dots and dashes, so a narrow column
 * never splits a word ("text.primar y"). */
export function tokenNameParts(name: string) {
  return name.split(/(?<=[.\-_/])/);
}
export function breakableName(name: string) {
  return tokenNameParts(name).map((part, i) => (
    <Fragment key={i}>
      {i > 0 && <wbr />}
      {part}
    </Fragment>
  ));
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
              <strong>{breakableName(v.name)}</strong>
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
                <strong>{breakableName(v.name)}</strong>
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
    <div className={`detail-overview ${referenceStyles.overview}`}>
      <div className="detail-main-preview">
        <MediaPreview
          image={detail.image}
          video={detail.video}
          name={detail.name}
          always
        />
      </div>
      <div className="detail-title">
        <h1>{detail.name}</h1>
        {detail.icon ? (
          <img src={detail.icon} alt="" />
        ) : (
          <span className="reference-letter large">{detail.name[0]}</span>
        )}
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
            href={
              detail.source === "systems"
                ? `/library/${detail.slug}`
                : `/styles/refero/${detail.slug}`
            }
            className="pill"
          >
            {detail.source === "systems"
              ? "Package details"
              : "Style documentation"}
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
                decoding="async"
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
    <section
      className={`export-panel ${referenceStyles.exportPanel}`}
      aria-label="Reference exports"
    >
      <div className="export-tabs" role="tablist" aria-label="Export format">
        {keys.map((key) => (
          <button
            role="tab"
            aria-selected={tab === key}
            className={tab === key ? "active" : ""}
            key={key}
            onClick={() => setTab(key)}
          >
            {key === "variables.css"
              ? "CSS Variables"
              : key === "tokens.json"
                ? "Design Tokens"
                : key === "theme.css"
                  ? "Theme CSS"
                  : key}
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
          <code>
            {value.split("\n").map((line, index) => (
              <span
                key={index}
                className={
                  line.startsWith("#")
                    ? referenceStyles.codeHeading
                    : line.startsWith(">")
                      ? referenceStyles.codeQuote
                      : undefined
                }
              >
                {line}
                {"\n"}
              </span>
            ))}
          </code>
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
// Download through a Blob so a remote CDN's ignored download attribute can
// never navigate the research app away. CORS failures remain visible in the UI.
export async function fetchReferenceImage(
  url: string,
  fetchImage: typeof fetch = fetch,
  signal?: AbortSignal,
): Promise<Blob> {
  const response = await fetchImage(url, {
    mode: "cors",
    credentials: "omit",
    ...(signal ? { signal } : {}),
  });
  if (!response.ok) throw new Error("The image could not be downloaded.");
  const image = await response.blob();
  if (!image.size || !image.type.startsWith("image/"))
    throw new Error("The source did not return an image.");
  return image;
}

// A generated card thumbnail encodes its original path with double underscores.
// Upgrade only an exact path match, so opening a card never changes screens.
export function inspectorPreview(
  current: LibraryItem | null,
  detail: LibraryDetail | null,
): string | undefined {
  const image = current?.image || detail?.image;
  const media =
    detail?.id === current?.id
      ? detail?.media.filter((item) => item.type === "image") || []
      : [];
  if (!image) return media[0]?.url;
  try {
    const path = decodeURIComponent(
      new URL(image, "http://studio.invalid").pathname,
    );
    const name = path
      .split("/")
      .at(-1)
      ?.replace(/\.[^/.]+$/, "");
    if (
      !current ||
      !path.includes("/thumbs/") ||
      !name?.startsWith(`${current.source}__${current.slug}__`)
    )
      return image;
    const originalPath = name.replaceAll("__", "/");
    return (
      media.find(
        (item) =>
          decodeURIComponent(
            new URL(item.url, "http://studio.invalid").pathname,
          )
            .replace(/^\/media\//, "")
            .replace(/\.[^/.]+$/, "") === originalPath,
      )?.url || image
    );
  } catch {
    return image;
  }
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
  const inspectorElement = useRef<HTMLDivElement | null>(null);
  useEffect(() => {
    if (!current) return;
    let live = true;
    setDetail(null);
    setError("");
    api<LibraryDetail>(`/api/library/${current.source}/${current.slug}`)
      .then((d) => {
        if (live) setDetail(d);
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
      const target = e.target;
      if (e.defaultPrevented || !(target instanceof Element)) return;
      if (
        target.closest(
          'input, textarea, select, video, audio, button, a, [contenteditable="true"], [role="slider"], [role="combobox"], [role="listbox"], [role="tab"]',
        )
      )
        return;
      if (target.closest('[role="dialog"]') !== inspectorElement.current)
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
  const openingFocus = useRef<HTMLElement | null>(null);
  useEffect(() => {
    function rememberOpener(event: PointerEvent) {
      const target = event.target;
      if (!(target instanceof HTMLElement) || target.closest('[role="dialog"]'))
        return;
      const control = target.closest<HTMLElement>("button, a, [tabindex]");
      if (control) openingFocus.current = control;
    }
    document.addEventListener("pointerdown", rememberOpener, true);
    return () =>
      document.removeEventListener("pointerdown", rememberOpener, true);
  }, []);
  const [origin, setOrigin] = useState("");
  const [copied, setCopied] = useState("");
  const [showVideo, setShowVideo] = useState(false);
  const downloadRequest = useRef<AbortController | null>(null);
  const [downloading, setDownloading] = useState(false);
  const [downloadError, setDownloadError] = useState("");
  useEffect(() => {
    setOrigin(window.location.origin);
  }, []);
  useEffect(() => {
    setShowVideo(false);
    setCopied("");
    downloadRequest.current?.abort();
    downloadRequest.current = null;
    setDownloading(false);
    setDownloadError("");
    return () => {
      downloadRequest.current?.abort();
      downloadRequest.current = null;
    };
  }, [current?.id]);
  const reference = detail || current;
  const preview = inspectorPreview(current, detail);
  const href = reference
    ? `${origin}${reference.source === "systems" ? `/library/${reference.slug}` : `/styles/refero/${reference.slug}`}`
    : "";
  async function downloadPreview() {
    if (!preview || downloading) return;
    const request = new AbortController();
    downloadRequest.current = request;
    setDownloading(true);
    setDownloadError("");
    try {
      const image = await fetchReferenceImage(preview, fetch, request.signal);
      if (request.signal.aborted || downloadRequest.current !== request) return;
      const objectUrl = URL.createObjectURL(image);
      const anchor = document.createElement("a");
      anchor.href = objectUrl;
      anchor.download =
        new URL(preview, window.location.origin).pathname.split("/").at(-1) ||
        `${reference?.slug || "reference"}.png`;
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      setTimeout(() => URL.revokeObjectURL(objectUrl), 1000);
    } catch {
      if (!request.signal.aborted && downloadRequest.current === request)
        setDownloadError(
          "This image could not be downloaded. The source may not allow downloads from this app. Your reference is still open.",
        );
    } finally {
      if (downloadRequest.current === request) {
        downloadRequest.current = null;
        setDownloading(false);
      }
    }
  }
  async function copyColor(value: string) {
    try {
      await navigator.clipboard.writeText(value);
      setCopied(`Copied ${value}`);
    } catch {
      setCopied(
        "Clipboard unavailable. The color value is available in Recorded values.",
      );
    }
  }
  return (
    <Dialog.Root
      open={!!current}
      onOpenChange={(open) => {
        if (!open) onClose();
      }}
    >
      <Dialog.Portal>
        <Dialog.Overlay className={referenceStyles.inspectorOverlay} />
        <Dialog.Content
          className={referenceStyles.inspector}
          ref={inspectorElement}
          aria-describedby={undefined}
          onOpenAutoFocus={() => {
            const active = document.activeElement;
            if (
              active instanceof HTMLElement &&
              active !== document.body &&
              !active.closest('[role="dialog"]')
            )
              openingFocus.current = active;
          }}
          onCloseAutoFocus={(event) => {
            event.preventDefault();
            const opener = openingFocus.current;
            requestAnimationFrame(() => {
              if (opener?.isConnected) opener.focus();
            });
          }}
        >
          <div
            className={referenceStyles.inspectorMedia}
            tabIndex={0}
            aria-label="Captured reference preview"
          >
            {preview ? (
              showVideo && reference?.video ? (
                <video
                  src={reference.video}
                  poster={preview}
                  controls
                  autoPlay
                  muted
                  playsInline
                  className={referenceStyles.inspectorImage}
                />
              ) : (
                <img
                  src={preview}
                  alt={`${reference?.name} captured interface`}
                  className={referenceStyles.inspectorImage}
                />
              )
            ) : (
              <div className={referenceStyles.missingPreview}>
                <BookOpen size={32} />
                <span>Preview unavailable</span>
              </div>
            )}
            {reference?.video && (
              <button
                className={`pill ${referenceStyles.videoToggle}`}
                onClick={() => setShowVideo((value) => !value)}
              >
                {showVideo ? "Show screenshot" : "Play scrolling preview"}
              </button>
            )}
          </div>
          <div className={referenceStyles.inspectorPanel}>
            <header className={referenceStyles.inspectorBrand}>
              {reference?.icon ? (
                <img src={reference.icon} alt="" />
              ) : (
                <span className="reference-letter">{reference?.name[0]}</span>
              )}
              <div>
                <Dialog.Title>{reference?.name || "Reference"}</Dialog.Title>
                <p>
                  {reference?.evidence === "measured"
                    ? "Measured package"
                    : "Interpreted reference"}
                </p>
              </div>
              <Dialog.Close
                className={referenceStyles.inspectorClose}
                aria-label="Close reference"
              >
                <X size={20} />
              </Dialog.Close>
            </header>
            <div className={referenceStyles.inspectorContent}>
              {error ? (
                <ErrorState message={error} />
              ) : !detail ? (
                <Spinner label="Loading reference details…" />
              ) : (
                <>
                  <section className={referenceStyles.inspectorSection}>
                    <h3>
                      <Layers size={14} />
                      Reference
                    </h3>
                    <div className={referenceStyles.chips}>
                      {[detail.platform, detail.category, ...detail.themes]
                        .filter(Boolean)
                        .filter(
                          (value, index, values) =>
                            values.indexOf(value) === index,
                        )
                        .map((value) => (
                          <Link
                            key={value}
                            href={
                              detail.source === "systems"
                                ? `/library?view=screens&${value === detail.platform ? "platform" : value === detail.category ? "category" : "theme"}=${encodeURIComponent(value)}`
                                : `/styles?q=${encodeURIComponent(value)}`
                            }
                          >
                            {value}
                          </Link>
                        ))}
                    </div>
                  </section>
                  {detail.tags.length > 0 && (
                    <section className={referenceStyles.inspectorSection}>
                      <h3>
                        <Tag size={14} />
                        Tags
                      </h3>
                      <div className={referenceStyles.chips}>
                        {detail.tags.map((tag) => (
                          <Link
                            key={tag}
                            href={
                              detail.source === "systems"
                                ? `/library?view=screens&tag=${encodeURIComponent(tag)}`
                                : `/styles?q=${encodeURIComponent(tag)}`
                            }
                          >
                            {tag}
                          </Link>
                        ))}
                      </div>
                    </section>
                  )}
                  {detail.colors.length > 0 && (
                    <section className={referenceStyles.inspectorSection}>
                      <h3>
                        <Palette size={14} />
                        Colors
                      </h3>
                      <div className={referenceStyles.chips}>
                        {detail.colors.slice(0, 12).map((color, index) => (
                          <button
                            key={`${color.name}-${index}`}
                            title={`${color.value}${color.evidence ? ` · ${color.evidence}` : ""}`}
                            onClick={() => copyColor(color.value)}
                          >
                            <i
                              style={{
                                background:
                                  /^(#|rgb|hsl|oklch|color|transparent|white|black)/i.test(
                                    color.value,
                                  )
                                    ? color.value
                                    : undefined,
                              }}
                            />
                            {color.name}
                          </button>
                        ))}
                      </div>
                      <p className={referenceStyles.copyFeedback} role="status">
                        {copied}
                      </p>
                    </section>
                  )}
                  <details className={referenceStyles.recordedValues}>
                    <summary>Recorded values &amp; evidence</summary>
                    <p>
                      {detail.evidence === "measured"
                        ? "Consult each value’s evidence label. Images show layout and proportion."
                        : "Third-party interpretation. Use for inspiration; these values are not measured product evidence."}
                      {detail.captured ? ` Captured ${detail.captured}.` : ""}
                    </p>
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
                    <ReferenceValues
                      title="Shape & radius"
                      values={detail.radii}
                      previewLimit={5}
                    />
                    {detail.guidelines.length > 0 && (
                      <section>
                        <h3>Design notes</h3>
                        <ul>
                          {detail.guidelines.map((note, index) => (
                            <li key={index}>{note}</li>
                          ))}
                        </ul>
                      </section>
                    )}
                  </details>
                </>
              )}
            </div>
            <footer className={referenceStyles.inspectorActions}>
              <div className={referenceStyles.navigation}>
                <span>
                  {index >= 0 ? index + 1 : 1} of {Math.max(1, items.length)}
                </span>
                <button
                  onClick={() => move(-1)}
                  disabled={items.length < 2}
                  aria-label="Previous reference"
                >
                  <ChevronLeft size={18} />
                </button>
                <button
                  onClick={() => move(1)}
                  disabled={items.length < 2}
                  aria-label="Next reference"
                >
                  <ChevronRight size={18} />
                </button>
                {onPin && current && (
                  <button
                    onClick={() => onPin(current.id)}
                    aria-pressed={pinnedIds.includes(current.id)}
                    title="Pin direction"
                  >
                    <Pin size={15} />
                    {pinnedIds.includes(current.id) ? "Pinned" : "Pin"}
                  </button>
                )}
                {onExclude && current && (
                  <button onClick={() => onExclude(current.id)}>
                    {excludedIds.includes(current.id) ? "Restore" : "Exclude"}
                  </button>
                )}
              </div>
              <div className={referenceStyles.actionPair}>
                {preview && (
                  <button onClick={downloadPreview} disabled={downloading}>
                    <Download size={14} />
                    {downloading ? "Downloading…" : "Download"}
                  </button>
                )}
                <CopyButton value={href} label="Copy link" />
              </div>
              {downloadError && (
                <p className={referenceStyles.downloadError} role="alert">
                  {downloadError}
                </p>
              )}
              {reference && (
                <SaveReference
                  item={reference}
                  className={referenceStyles.saveAction}
                />
              )}
              {detail?.sourceUrl && (
                <a
                  className={referenceStyles.documentationLink}
                  href={detail.sourceUrl}
                  target="_blank"
                  rel="noreferrer"
                >
                  Visit website <ExternalLink size={13} />
                </a>
              )}
              {reference && (
                <Link
                  className={referenceStyles.documentationLink}
                  href={
                    reference.source === "systems"
                      ? `/library/${reference.slug}`
                      : `/styles/refero/${reference.slug}`
                  }
                >
                  {reference.source === "systems"
                    ? "Package details"
                    : "Style documentation"}{" "}
                  <ArrowRight size={13} />
                </Link>
              )}
            </footer>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
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
        if (live) setDetails(d);
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
