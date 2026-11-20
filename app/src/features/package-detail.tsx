"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import {
  Suspense,
  useCallback,
  useEffect,
  useLayoutEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
} from "react";
import * as Dialog from "@radix-ui/react-dialog";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  ArrowLeft,
  ChevronLeft,
  ChevronRight,
  Download,
  ExternalLink,
  X,
} from "lucide-react";
import type {
  LibraryDetail,
  LibraryItem,
  MeasuredPackageDetail,
  PackageDocumentContent,
  ReferenceMedia,
} from "@/contracts/library";
import {
  CopyButton,
  DownloadButton,
  Empty,
  ErrorState,
  Select,
  SkeletonGrid,
  Spinner,
  useResource,
} from "@/components/shared";
import { MediaBookmarkButton } from "@/components/media-bookmark";
import { MediaCollectionButton } from "@/components/media-collection";
import {
  ExportPanel,
  ReferenceValues,
  SaveReference,
} from "@/components/reference";
import {
  filterPackageMedia,
  mediaDetailHref,
  packageDocumentLink,
  packageFileHref,
  safeDecode,
} from "./package-detail-data";
import { headingId, nodeText } from "./markdown-heading";
import styles from "./package-detail.module.css";
import {
  animateCaptureViewer,
  animateViewerDeparture,
  captureViewerOrigin,
  reducedViewerMotion,
  type CaptureViewerOrigin,
} from "./capture-viewer-motion";
import { replaceSearch } from "./url-state";

type Tab =
  | "screenshots"
  | "components"
  | "icons"
  | "boards"
  | "values"
  | "readme"
  | "files"
  | "guide";
const tabs: [Tab, string][] = [
  ["screenshots", "Screenshots"],
  ["components", "Components"],
  ["icons", "Icons"],
  ["boards", "Boards"],
  ["values", "Recorded values"],
  ["readme", "README"],
  ["files", "Files"],
  ["guide", "Style guide"],
];
const size = (n: number) =>
  n < 1024
    ? `${n} B`
    : n < 1024 * 1024
      ? `${(n / 1024).toFixed(1)} KB`
      : `${(n / 1024 / 1024).toFixed(1)} MB`;
export function PackageDetailPage({ slug }: { slug: string }) {
  return (
    <Suspense
      fallback={
        <div className={styles.page}>
          <SkeletonGrid
            shape="tile"
            count={6}
            className={styles.grid}
            label="Opening captured package…"
          />
        </div>
      }
    >
      <PackageDetail slug={slug} />
    </Suspense>
  );
}
function PackageDetail({ slug }: { slug: string }) {
  const { data, loading, error } = useResource<LibraryDetail>(
    `/api/library/systems/${encodeURIComponent(slug)}`,
  );
  const params = useSearchParams();
  const rawTab = params.get("tab");
  const tab: Tab = tabs.some(([key]) => key === rawTab)
    ? (rawTab as Tab)
    : "screenshots";
  const [query, setQuery] = useState(""),
    [tag, setTag] = useState(""),
    [page, setPage] = useState(1);
  const [fileSearch, setFileSearch] = useState("");
  const viewerOrigin = useRef<CaptureViewerOrigin | undefined>(undefined);
  const detail = data,
    pkg = detail?.measured;
  const media = useMemo(
    () =>
      pkg
        ? tab === "components"
          ? pkg.crops
          : tab === "icons"
            ? pkg.icons
            : tab === "boards"
              ? pkg.boards
              : pkg.screenshots
        : [],
    [pkg, tab],
  );
  const filtered = useMemo(
    () => filterPackageMedia(media, query, tag),
    [media, query, tag],
  );
  const selected = params.get("media"),
    opened = selected
      ? filtered.find((m) => m.id === selected) ||
        detail?.media.find((m) => m.id === selected)
      : undefined;
  const lightboxItems =
    opened && !filtered.some((m) => m.id === opened.id) ? [opened] : filtered;
  function update(patch: Record<string, string>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(patch))
      value ? next.set(key, value) : next.delete(key);
    replaceSearch(next);
  }
  useEffect(() => {
    setQuery("");
    setTag("");
    setPage(1);
  }, [tab]);
  useEffect(() => {
    setPage(1);
  }, [query, tag]);
  useEffect(() => {
    const hash = window.location.hash;
    if (hash)
      requestAnimationFrame(() =>
        document.getElementById(safeDecode(hash.slice(1)))?.scrollIntoView(),
      );
  }, [params.get("file"), tab]);
  if (loading)
    return (
      <div className={styles.page}>
        <SkeletonGrid
          shape="tile"
          count={6}
          className={styles.grid}
          label="Opening captured package…"
        />
      </div>
    );
  if (error)
    return (
      <div className={styles.page}>
        <Empty
          title={
            /not found/i.test(error)
              ? "Package not found"
              : "Could not open this package"
          }
        >
          <p role="alert">{error}</p>
          <Link className="pill small" href="/library">
            Back to captured packages
          </Link>
        </Empty>
      </div>
    );
  if (!detail || !pkg) return <Empty title="Captured package unavailable" />;
  const counts: Partial<Record<Tab, number>> = {
    screenshots: pkg.screenshots.length,
    components: pkg.crops.length,
    icons: pkg.icons.length,
    boards: pkg.boards.length,
    files: pkg.documents.length,
  };
  const shown = filtered.slice(0, page * 36);
  const groups = [...new Set(shown.map((m) => m.group || "Captured media"))];
  const files = pkg.documents.filter((d) =>
    `${d.path}`.toLowerCase().includes(fileSearch.toLowerCase()),
  );
  return (
    <div className={styles.page}>
      <Link href="/library" className={styles.back}>
        <ArrowLeft size={15} /> Captured packages
      </Link>
      <header className={styles.header}>
        {detail.icon && (
          <img className={styles.icon} src={detail.icon} alt="" />
        )}
        <div>
          <p className={styles.kicker}>
            Measured product package · {detail.platform}
          </p>
          <h1>{detail.name}</h1>
          <p>{detail.description}</p>
          <p className={styles.meta}>
            {detail.themes.join(" · ")}
            {detail.captured ? ` · Captured ${detail.captured}` : ""}
            {pkg.access ? ` · ${pkg.access}` : ""}
          </p>
        </div>
        <div className={styles.actions}>
          <SaveReference item={detail} />
          {detail.sourceUrl && (
            <a
              href={detail.sourceUrl}
              target="_blank"
              rel="noreferrer"
              className="pill"
            >
              Visit product <ExternalLink size={14} />
            </a>
          )}
          <Link href={`/scorecard/${slug}`} className="pill">
            Package health
          </Link>
        </div>
      </header>
      <nav className={styles.tabs} aria-label="Package sections">
        {tabs
          .filter(([key]) => key !== "guide" || pkg.styleGuide)
          .map(([key, label]) => (
            <button
              key={key}
              aria-current={tab === key ? "page" : undefined}
              onClick={() => update({ tab: key, media: "" })}
            >
              {label}
              {counts[key] !== undefined && (
                <span>{counts[key].toLocaleString()}</span>
              )}
            </button>
          ))}
      </nav>
      {["screenshots", "components", "icons", "boards"].includes(tab) && (
        <section>
          <div className={styles.toolbar}>
            <label className={styles.search}>
              <span className="sr-only">Search captured media</span>
              <input
                type="search"
                placeholder="Search screen, state, component or folder…"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
            </label>
            <div
              className={styles.chips}
              role="group"
              aria-label="Capture filter"
            >
              {["", ...new Set(media.flatMap((m) => m.tags))].map((value) => (
                <button
                  className="pill small"
                  key={value}
                  aria-pressed={tag === value}
                  onClick={() => setTag(value)}
                >
                  {value || "All"}
                  <span>
                    {
                      (value
                        ? media.filter((m) => m.tags.includes(value))
                        : media
                      ).length
                    }
                  </span>
                </button>
              ))}
            </div>
          </div>
          <p className={styles.meta}>
            {filtered.length.toLocaleString()}{" "}
            {tab === "components" ? "component crops" : tab}
            {pkg.widths.length
              ? ` · Captured widths ${pkg.widths.join(", ")} px`
              : ""}
            . Images show layout and proportion. Consult token evidence for
            values.
          </p>
          {!filtered.length ? (
            <Empty title="No captures match these filters" />
          ) : (
            groups.map((group) => (
              <section key={group} className={styles.mediaGroup}>
                <h2>{group}</h2>
                <div
                  className={`${styles.grid} ${tab === "icons" ? styles.iconGrid : ""} ${detail.platform === "mobile" && tab === "screenshots" ? styles.phoneGrid : ""}`}
                >
                  {shown
                    .filter((m) => (m.group || "Captured media") === group)
                    .map((m) => (
                      <article key={m.id} className={styles.tile}>
                        <button
                          className={styles.tileOpen}
                          onClick={(event) => {
                            viewerOrigin.current = captureViewerOrigin(
                              event.currentTarget,
                              `${detail.id}:${m.id}`,
                            );
                            update({ media: m.id });
                          }}
                        >
                          <div
                            className={`${styles.frame} ${tab !== "screenshots" ? styles.contain : ""}`}
                            data-viewer-source={`${detail.id}:${m.id}`}
                          >
                            <img
                              loading="lazy"
                              decoding="async"
                              src={m.thumbnail || m.url}
                              alt={m.name}
                            />
                          </div>
                          <strong>{m.name}</strong>
                          <span>{m.tags.join(" · ")}</span>
                        </button>
                        <MediaBookmarkButton
                          referenceId={detail.id}
                          mediaId={m.id}
                          compact
                        />
                      </article>
                    ))}
                </div>
              </section>
            ))
          )}
          {shown.length < filtered.length && (
            <div className={styles.more}>
              <button className="pill" onClick={() => setPage((p) => p + 1)}>
                Show 36 more
              </button>
              <span>
                {shown.length} of {filtered.length}
              </span>
            </div>
          )}
        </section>
      )}
      {tab === "values" && (
        <div className={styles.valuesLayout}>
          <MeasuredValues pkg={pkg} detail={detail} />
          <ExportPanel detail={detail} />
        </div>
      )}
      {tab === "readme" && (
        <PackageMarkdown
          slug={slug}
          path={pkg.readmePath}
          text={pkg.readme || "README unavailable in this checkout."}
        />
      )}
      {tab === "guide" && pkg.styleGuide && (
        <section>
          <div className={styles.sectionHeading}>
            <h2>Rendered style guide</h2>
            <a
              className="pill"
              href={pkg.styleGuide}
              target="_blank"
              rel="noreferrer"
            >
              Open guide <ExternalLink size={14} />
            </a>
          </div>
          <iframe
            className={styles.guide}
            title={`${detail.name} style guide`}
            src={pkg.styleGuide}
            sandbox="allow-scripts"
          />
        </section>
      )}
      {tab === "files" && (
        <div className={styles.filesLayout}>
          <aside className={styles.fileList}>
            <label>
              <span className="sr-only">Search package files</span>
              <input
                type="search"
                placeholder="Find a package file…"
                value={fileSearch}
                onChange={(e) => setFileSearch(e.target.value)}
              />
            </label>
            <p className={styles.meta}>{files.length} readable files</p>
            {[...new Set(files.map((f) => f.group))].map((group) => (
              <details key={group} open>
                <summary>{group ? `${group}/` : "Package root"}</summary>
                {files
                  .filter((f) => f.group === group)
                  .map((f) => (
                    <Link
                      key={f.path}
                      aria-current={
                        params.get("file") === f.path ? "page" : undefined
                      }
                      href={packageFileHref(slug, f.path)}
                    >
                      <span>{f.path}</span>
                      <small>{size(f.size)}</small>
                    </Link>
                  ))}
              </details>
            ))}
          </aside>
          <div className={styles.document}>
            <PackageDocumentView
              slug={slug}
              path={params.get("file") || pkg.readmePath}
            />
          </div>
        </div>
      )}
      <PackageLightbox
        detail={detail}
        current={opened}
        items={lightboxItems}
        origin={viewerOrigin.current}
        onClose={() => update({ media: "" })}
        onChange={(item) => update({ media: item.id })}
      />
    </div>
  );
}
export function captureViewerLinks(
  detail: LibraryItem,
  current: ReferenceMedia,
) {
  const measured = detail.source === "systems";
  const documentation = measured
    ? `/library/${encodeURIComponent(detail.slug)}`
    : `/styles/refero/${encodeURIComponent(detail.slug)}`;
  return {
    documentation,
    browse: measured
      ? `/library?view=screens&referenceId=${encodeURIComponent(detail.id)}&platform=${encodeURIComponent(detail.platform)}`
      : documentation,
    copy: measured ? mediaDetailHref(detail.slug, current) : current.url,
    tag: (tag: string) =>
      measured
        ? `/library?view=screens&tag=${encodeURIComponent(tag)}&platform=${encodeURIComponent(detail.platform)}`
        : `/styles?tag=${encodeURIComponent(tag)}`,
    platform: measured
      ? `/library?view=screens&platform=${encodeURIComponent(detail.platform)}`
      : `/styles?q=${encodeURIComponent(detail.platform)}`,
    label: measured ? "Package details" : "Style documentation",
  };
}
export function PackageLightbox({
  detail,
  current,
  items,
  onClose,
  onChange,
  origin,
}: {
  detail: LibraryItem;
  current?: ReferenceMedia;
  items: ReferenceMedia[];
  onClose: () => void;
  onChange: (item: ReferenceMedia) => void;
  origin?: CaptureViewerOrigin;
}) {
  const links = current ? captureViewerLinks(detail, current) : null;
  const opener = useRef<HTMLElement | null>(null);
  const lightboxRef = useRef<HTMLDivElement | null>(null);
  const overlayRef = useRef<HTMLDivElement | null>(null);
  const stageRef = useRef<HTMLDivElement | null>(null);
  const transition = useRef<ReturnType<typeof animateCaptureViewer> | null>(
    null,
  );
  const previous = useRef<string | null>(null);
  const direction = useRef(1);
  const closing = useRef(false);
  const mounted = useRef(true);
  const departure = useRef<(() => void) | null>(null);
  const [content, setContent] = useState<HTMLDivElement | null>(null);
  const setLightbox = useCallback((node: HTMLDivElement | null) => {
    lightboxRef.current = node;
    setContent(node);
  }, []);
  useLayoutEffect(() => {
    if (!content || !current || !stageRef.current) {
      const canceled = transition.current;
      transition.current = null;
      canceled?.cancel();
      closing.current = false;
      previous.current = null;
      return;
    }
    const identity = `${detail.id}:${current.id}`;
    const animation = animateCaptureViewer({
      content,
      overlay: overlayRef.current,
      stage: stageRef.current,
      id: identity,
      phase: previous.current ? "change" : "open",
      origin,
      direction: direction.current,
    });
    previous.current = identity;
    transition.current = animation;
    return () => {
      if (transition.current === animation) transition.current = null;
      animation.cancel();
    };
  }, [content, current?.id, detail.id]);
  useEffect(() => {
    mounted.current = true;
    return () => {
      mounted.current = false;
      const canceled = transition.current;
      transition.current = null;
      canceled?.cancel();
      departure.current?.();
    };
  }, []);
  const close = async () => {
    if (closing.current) return;
    if (!current || !content || !stageRef.current || reducedViewerMotion()) {
      onClose();
      return;
    }
    closing.current = true;
    departure.current?.();
    const canceled = transition.current;
    transition.current = null;
    canceled?.cancel();
    const animation = animateCaptureViewer({
      content,
      overlay: overlayRef.current,
      stage: stageRef.current,
      id: `${detail.id}:${current.id}`,
      phase: "close",
      origin,
    });
    transition.current = animation;
    await animation.finished;
    if (mounted.current && transition.current === animation) onClose();
  };
  const index = items.findIndex((m) => m === current);
  const move = (delta: number) => {
    if (closing.current) return;
    if (items.length < 2) return;
    direction.current = delta;
    departure.current?.();
    const canceled = transition.current;
    transition.current = null;
    canceled?.cancel();
    if (stageRef.current)
      departure.current = animateViewerDeparture(stageRef.current, delta);
    if (items.length)
      onChange(items[(index + delta + items.length) % items.length]);
  };
  useEffect(() => {
    if (!current) return;
    const handler = (event: KeyboardEvent) => {
      if (
        event.defaultPrevented ||
        (event.target instanceof Element &&
          event.target.closest('[role="dialog"]') !== lightboxRef.current) ||
        (event.target instanceof Element &&
          event.target.closest("input,textarea,select,video"))
      )
        return;
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        move(-1);
      }
      if (event.key === "ArrowRight") {
        event.preventDefault();
        move(1);
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [current?.id, items]);
  return (
    <Dialog.Root
      open={!!current}
      onOpenChange={(open) => {
        if (!open) void close();
      }}
    >
      <Dialog.Portal>
        <Dialog.Overlay ref={overlayRef} className={styles.overlay} />
        <Dialog.Content
          ref={setLightbox}
          className={styles.lightbox}
          aria-describedby={undefined}
          onOpenAutoFocus={() => {
            const active = document.activeElement;
            if (
              active instanceof HTMLElement &&
              active !== document.body &&
              !active.closest('[role="dialog"]')
            )
              opener.current = active;
          }}
          onCloseAutoFocus={(event) => {
            event.preventDefault();
            const target = opener.current?.isConnected
              ? opener.current
              : document.querySelector<HTMLElement>(
                  'nav[aria-label="Package sections"] button[aria-current]',
                );
            requestAnimationFrame(() => target?.focus());
          }}
        >
          {current && (
            <>
              <header data-viewer-chrome>
                <div>
                  <Link href={links!.browse} className={styles.viewerProduct}>
                    {detail.icon && <img src={detail.icon} alt="" />}
                    <span>{detail.name}</span>
                  </Link>
                  <Dialog.Title>{current.name}</Dialog.Title>
                </div>
                <Dialog.Close
                  className="icon-button"
                  aria-label="Close screenshot"
                >
                  <X size={22} />
                </Dialog.Close>
              </header>
              <div
                key={`${detail.id}:${current.id}`}
                ref={stageRef}
                className={styles.lightboxStage}
              >
                {current.type === "video" ? (
                  <video src={current.url} controls />
                ) : (
                  <img
                    src={current.url}
                    alt={current.name}
                    width={
                      origin?.id === `${detail.id}:${current.id}`
                        ? origin.width || undefined
                        : undefined
                    }
                    height={
                      origin?.id === `${detail.id}:${current.id}`
                        ? origin.height || undefined
                        : undefined
                    }
                  />
                )}
              </div>
              <aside className={styles.viewerMetadata} data-viewer-chrome>
                <h3>Capture</h3>
                <p>{current.group || "Captured screen"}</p>
                <h3>Tags</h3>
                <div className={styles.viewerTags}>
                  {current.tags.length ? (
                    current.tags.map((tag) => (
                      <Link key={tag} href={links!.tag(tag)}>
                        {tag}
                      </Link>
                    ))
                  ) : (
                    <span className="muted">No capture tags</span>
                  )}
                </div>
                <h3>Product</h3>
                <div className={styles.viewerTags}>
                  <Link href={links!.platform}>{detail.platform}</Link>
                </div>
                <p className={styles.meta}>{detail.description}</p>
                <Link className="pill small" href={links!.documentation}>
                  {links!.label} <ExternalLink size={14} />
                </Link>
                <p className={styles.meta}>
                  {detail.captured ? `Captured ${detail.captured}` : ""}
                </p>
              </aside>
              <div className={styles.viewerNavigation} data-viewer-chrome>
                <span>
                  {index + 1} / {items.length}
                </span>
                <div className={styles.actions}>
                  <button
                    className="pill"
                    onClick={() => move(-1)}
                    disabled={items.length < 2}
                    aria-label="Previous screenshot"
                  >
                    <ChevronLeft size={18} />
                  </button>
                  <button
                    className="pill"
                    onClick={() => move(1)}
                    disabled={items.length < 2}
                    aria-label="Next screenshot"
                  >
                    <ChevronRight size={18} />
                  </button>
                </div>
              </div>
              <footer data-viewer-chrome>
                <div className={styles.actions}>
                  <a
                    className="pill"
                    href={current.url}
                    target="_blank"
                    rel="noreferrer"
                  >
                    Original <ExternalLink size={14} />
                  </a>
                  <a className="pill" href={current.url} download>
                    <Download size={14} /> Download
                  </a>
                  <CopyButton
                    value={
                      typeof window === "undefined"
                        ? ""
                        : new URL(links!.copy, window.location.origin).href
                    }
                    label="Copy image link"
                  />
                  <MediaBookmarkButton
                    referenceId={detail.id}
                    mediaId={current.id}
                    compact
                  />
                  <MediaCollectionButton
                    key={JSON.stringify([detail.id, current.id])}
                    referenceId={detail.id}
                    mediaId={current.id}
                  />
                </div>
              </footer>
            </>
          )}
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
export function PackageMarkdown({
  slug,
  path,
  text,
}: {
  slug: string;
  path: string;
  text: string;
}) {
  return (
    <article className={styles.markdown}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        urlTransform={(url) => url}
        components={{
          a: ({ href, children }) => {
            const url = href
              ? packageDocumentLink(slug, path, href)
              : undefined;
            return url ? (
              <a
                href={url}
                target={/^https?:/.test(url) ? "_blank" : undefined}
                rel="noreferrer"
              >
                {children}
              </a>
            ) : (
              <span>{children}</span>
            );
          },
          img: ({ src, alt }) => {
            const url =
              typeof src === "string"
                ? packageDocumentLink(slug, path, src, true)
                : undefined;
            return url ? (
              <a href={url} target="_blank" rel="noreferrer">
                <img
                  src={url}
                  alt={alt || "Package image"}
                  loading="lazy"
                  decoding="async"
                />
              </a>
            ) : (
              <span>{alt}</span>
            );
          },
          h1: ({ children }) => (
            <h1 id={headingId(nodeText(children))}>{children}</h1>
          ),
          h2: ({ children }) => (
            <h2 id={headingId(nodeText(children))}>{children}</h2>
          ),
          h3: ({ children }) => (
            <h3 id={headingId(nodeText(children))}>{children}</h3>
          ),
          h4: ({ children }) => (
            <h4 id={headingId(nodeText(children))}>{children}</h4>
          ),
          h5: ({ children }) => (
            <h5 id={headingId(nodeText(children))}>{children}</h5>
          ),
          h6: ({ children }) => (
            <h6 id={headingId(nodeText(children))}>{children}</h6>
          ),
        }}
      >
        {text}
      </ReactMarkdown>
    </article>
  );
}
function PackageDocumentView({ slug, path }: { slug: string; path: string }) {
  const { data, error, loading } = useResource<PackageDocumentContent>(
    `/api/packages/${encodeURIComponent(slug)}/files?path=${encodeURIComponent(path)}`,
  );
  const [source, setSource] = useState(false);
  useEffect(() => {
    setSource(false);
  }, [path]);
  useEffect(() => {
    const hash = window.location.hash;
    if (data && hash)
      requestAnimationFrame(() =>
        document.getElementById(safeDecode(hash.slice(1)))?.scrollIntoView(),
      );
  }, [data, path]);
  if (loading) return <Spinner label="Opening package file…" />;
  if (error) return <ErrorState message={error} />;
  if (!data) return null;
  let text = data.text;
  if (data.format === "json") {
    try {
      text = JSON.stringify(JSON.parse(text), null, 2);
    } catch {
      /* Show malformed JSON as stored. */
    }
  }
  return (
    <section>
      <div className={styles.sectionHeading}>
        <div>
          <h2>{data.name}</h2>
          <p className={styles.meta}>
            {data.path} · {size(data.size)}
          </p>
        </div>
        <div className={styles.actions}>
          {data.format === "markdown" && (
            <button
              className="pill small"
              aria-pressed={source}
              onClick={() => setSource((v) => !v)}
            >
              {source ? "Rendered" : "Source"}
            </button>
          )}
          {data.format === "html" && (
            <a
              className="pill small"
              href={`/api/packages/${encodeURIComponent(slug)}/guide/${data.path.split("/").map(encodeURIComponent).join("/")}`}
              target="_blank"
              rel="noreferrer"
            >
              Open rendered HTML
            </a>
          )}
          <CopyButton value={data.text} />
          <DownloadButton value={data.text} name={data.name} />
        </div>
      </div>
      {data.format === "markdown" && !source ? (
        <PackageMarkdown slug={slug} path={path} text={data.text} />
      ) : (
        <pre className={styles.source}>{text}</pre>
      )}
    </section>
  );
}
function MeasuredValues({
  pkg,
  detail,
}: {
  pkg: MeasuredPackageDetail;
  detail: LibraryDetail;
}) {
  const [theme, setTheme] = useState(pkg.tokenTheme);
  const palette = pkg.swatches[theme] || [];
  const color = (role: string, fallback: string) =>
    palette.find((s) => s.role === role)?.value || fallback;
  const gaps = Object.entries({ ...pkg.layoutGaps, ...pkg.omitted });
  return (
    <div className={styles.tokenContent}>
      <section>
        <div className={styles.sectionHeading}>
          <h2>Theme colors</h2>
          <Select
            compact
            label="Recorded color theme"
            value={theme}
            onChange={setTheme}
            options={Object.keys(pkg.swatches).map((name) => ({
              value: name,
              label: name,
            }))}
          />
        </div>
        <p className={styles.meta}>
          Recorded roles from the package. Check each token’s evidence before
          reuse.
        </p>
        <ReferenceValues
          title={theme}
          kind="color"
          values={palette
            .filter((s) => s.value !== null)
            .map((s) => ({
              name: s.token,
              value: s.value!,
              role: s.role,
              evidence: detail.colors.find((v) => v.name === s.token)?.evidence,
            }))}
        />
      </section>
      <section>
        <h2>Typography</h2>
        <div className={styles.fonts}>
          {pkg.fonts.map((f) => (
            <div key={f.token}>
              <strong style={{ fontFamily: f.stack }}>{f.family} Aa 123</strong>
              <code>{f.stack}</code>
              <small>{f.token}</small>
            </div>
          ))}
        </div>
        {pkg.typeStyles.map((t) => (
          <div className={styles.typeRow} key={t.name}>
            <div>
              <strong>{t.name}</strong>
              <code>
                {[
                  t.family,
                  t.size,
                  t.weight,
                  t.lineHeight && `line height ${t.lineHeight}`,
                  t.letterSpacing && `tracking ${t.letterSpacing}`,
                ]
                  .filter(Boolean)
                  .join(" · ")}
              </code>
            </div>
            <p
              style={{
                fontFamily:
                  pkg.fonts.find((f) => f.family === t.family)?.stack ||
                  t.family,
                fontSize: t.size,
                fontWeight: t.weight,
                lineHeight: t.lineHeight,
                letterSpacing: t.letterSpacing,
              }}
            >
              The quick brown fox
            </p>
          </div>
        ))}
      </section>
      <section>
        <h2>Spacing</h2>
        {pkg.spacing.map((s) => (
          <div className={styles.spaceRow} key={s.name}>
            <code>{s.name}</code>
            <span>
              <i style={{ width: s.value }} />
            </span>
            <code>{s.value}</code>
          </div>
        ))}
      </section>
      <section>
        <h2>Radius</h2>
        <div className={styles.radiusGrid}>
          {pkg.radii.map((r) => (
            <div key={r.name}>
              <i style={{ borderRadius: r.value }} />
              <strong>{r.name}</strong>
              <code>{r.value}</code>
            </div>
          ))}
        </div>
      </section>
      {!!pkg.shadows.length && (
        <section>
          <h2>Shadows</h2>
          <div
            className={styles.shadowGrid}
            style={
              {
                background: color("page", "#f6f6f6"),
                color: color("text", "#111"),
              } as CSSProperties
            }
          >
            {pkg.shadows.map((s) => (
              <figure key={s.token}>
                <div
                  style={{
                    boxShadow: s.css,
                    background: color("surface", "#fff"),
                  }}
                />
                <figcaption>
                  <strong>{s.token}</strong>
                  <code>{s.css}</code>
                </figcaption>
              </figure>
            ))}
          </div>
        </section>
      )}
      <details className={styles.allTokens}>
        <summary>All recorded token values and evidence</summary>
        <ReferenceValues title="Colors" values={detail.colors} kind="color" />
        <ReferenceValues
          title="Typography values"
          values={detail.typography}
          kind="type"
        />
        <ReferenceValues title="Spacing values" values={detail.spacing} />
        <ReferenceValues title="Radius values" values={detail.radii} />
      </details>
      {!!gaps.length && (
        <section>
          <h2>Known gaps</h2>
          {gaps.map(([name, reason]) => (
            <p key={name}>
              <code>{name}</code>: {reason}
            </p>
          ))}
        </section>
      )}
      {pkg.capture && (
        <details>
          <summary>Capture provenance</summary>
          <pre className={styles.source}>
            {JSON.stringify(pkg.capture, null, 2)}
          </pre>
        </details>
      )}
    </div>
  );
}
