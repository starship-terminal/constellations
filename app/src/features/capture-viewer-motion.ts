export interface ViewerRect {
  left: number;
  top: number;
  width: number;
  height: number;
}

export interface CaptureViewerOrigin {
  id: string;
  element: HTMLElement;
  rect: ViewerRect;
  imageRect: ViewerRect;
  url: string;
  width: number;
  height: number;
}

function positionOffset(value: string, available: number, axis: "x" | "y") {
  if (value === "center") return available / 2;
  if (value === (axis === "x" ? "left" : "top")) return 0;
  if (value === (axis === "x" ? "right" : "bottom")) return available;
  const number = Number.parseFloat(value);
  if (!Number.isFinite(number)) return available / 2;
  return value.endsWith("%") ? (available * number) / 100 : number;
}

/** Resolve the pixels painted inside an img element, including letterboxing. */
export function renderedImageRect(
  box: ViewerRect,
  natural: { width: number; height: number },
  fit: string,
  position: string,
): ViewerRect {
  if (!natural.width || !natural.height || fit === "fill") return { ...box };
  const contain = Math.min(
    box.width / natural.width,
    box.height / natural.height,
  );
  const scale =
    fit === "cover"
      ? Math.max(box.width / natural.width, box.height / natural.height)
      : fit === "contain"
        ? contain
        : fit === "scale-down"
          ? Math.min(1, contain)
          : 1;
  const width = natural.width * scale,
    height = natural.height * scale;
  const words = position.trim().split(/\s+/);
  // Computed styles normally expose two percentage/length values. Retain
  // keyword support for callers and single-keyword styles as well.
  const [horizontal, vertical] =
    words.length === 1
      ? [
          words[0] === "top" || words[0] === "bottom" ? "50%" : words[0],
          words[0] === "top" || words[0] === "bottom" ? words[0] : "50%",
        ]
      : words;
  return {
    left: box.left + positionOffset(horizontal, box.width - width, "x"),
    top: box.top + positionOffset(vertical, box.height - height, "y"),
    width,
    height,
  };
}

/** Keep the full image's negative scroll offset inside its visible frame. */
export function viewerImageInFrame(image: ViewerRect, frame: ViewerRect) {
  return {
    frame,
    image: {
      ...image,
      left: image.left - frame.left,
      top: image.top - frame.top,
    },
  };
}

export function clippedViewerImage(image: ViewerRect, clip: ViewerRect) {
  const frame = {
    left: Math.max(image.left, clip.left),
    top: Math.max(image.top, clip.top),
    width: Math.max(
      0,
      Math.min(image.left + image.width, clip.left + clip.width) -
        Math.max(image.left, clip.left),
    ),
    height: Math.max(
      0,
      Math.min(image.top + image.height, clip.top + clip.height) -
        Math.max(image.top, clip.top),
    ),
  };
  return viewerImageInFrame(image, frame);
}

function readImageRect(image: HTMLImageElement) {
  const style = getComputedStyle(image);
  return renderedImageRect(
    image.getBoundingClientRect(),
    {
      width: image.naturalWidth || Number(image.getAttribute("width")),
      height: image.naturalHeight || Number(image.getAttribute("height")),
    },
    style.objectFit,
    style.objectPosition,
  );
}

/** Read the clipped thumbnail frame before the dialog locks page scrolling. */
export function captureViewerOrigin(
  trigger: HTMLElement,
  id: string,
): CaptureViewerOrigin | undefined {
  const image = trigger.querySelector("img");
  const element = image?.parentElement;
  if (!image || !element) return;
  const rect = element.getBoundingClientRect();
  if (!rect.width || !rect.height) return;
  return {
    id,
    element,
    rect: {
      left: rect.left,
      top: rect.top,
      width: rect.width,
      height: rect.height,
    },
    imageRect: readImageRect(image),
    url: image.currentSrc || image.src,
    width: image.naturalWidth,
    height: image.naturalHeight,
  };
}

function visibleOrigin(id: string) {
  const frame = [
    ...document.querySelectorAll<HTMLElement>("[data-viewer-source]"),
  ].find((element) => element.dataset.viewerSource === id);
  const origin =
    frame?.parentElement && captureViewerOrigin(frame.parentElement, id);
  if (!origin) return;
  const { left, top, width, height } = origin.rect;
  return left < innerWidth &&
    top < innerHeight &&
    left + width > 0 &&
    top + height > 0
    ? origin
    : undefined;
}

export function reducedViewerMotion() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

/** Retain the previous image independently while React changes capture URLs. */
export function animateViewerDeparture(stage: HTMLElement, direction: number) {
  const image = stage.querySelector<HTMLImageElement>("img");
  if (!image || reducedViewerMotion()) return () => {};
  const { frame: bounds, image: inner } = clippedViewerImage(
    readImageRect(image),
    stage.getBoundingClientRect(),
  );
  const frame = document.createElement("div");
  Object.assign(frame.style, {
    position: "fixed",
    pointerEvents: "none",
    zIndex: "152",
    overflow: "hidden",
    left: `${bounds.left}px`,
    top: `${bounds.top}px`,
    width: `${bounds.width}px`,
    height: `${bounds.height}px`,
  });
  frame.setAttribute("aria-hidden", "true");
  const copy = image.cloneNode() as HTMLImageElement;
  Object.assign(copy.style, {
    display: "block",
    maxWidth: "none",
    maxHeight: "none",
    width: `${inner.width}px`,
    height: `${inner.height}px`,
    margin: "0",
    visibility: "visible",
    objectFit: "fill",
    transform: `translate(${inner.left}px, ${inner.top}px)`,
  });
  frame.append(copy);
  document.body.append(frame);
  const animation = frame.animate(
    [
      { opacity: 1, transform: "translateX(0)" },
      { opacity: 0, transform: `translateX(${-direction * 18}px)` },
    ],
    { duration: 180, easing: "ease-out", fill: "both" },
  );
  const cancel = () => {
    animation.cancel();
    frame.remove();
  };
  void animation.finished.then(cancel, cancel);
  return cancel;
}

/** Geometry belongs to an independent clipped image, never the whole dialog. */
export function animateCaptureViewer({
  content,
  overlay,
  stage,
  id,
  phase,
  origin,
  direction = 1,
}: {
  content: HTMLElement;
  overlay: HTMLElement | null;
  stage: HTMLElement;
  id: string;
  phase: "open" | "close" | "change";
  origin?: CaptureViewerOrigin;
  direction?: number;
}) {
  const animations: Animation[] = [];
  let clone: HTMLDivElement | undefined;
  const image = stage.querySelector<HTMLImageElement>("img");
  let hiddenImage = false;
  let disposed = false;
  const cleanups: (() => void)[] = [];
  const duration = phase === "change" ? 180 : 340;
  const ease = "cubic-bezier(.22,1,.36,1)";
  function run(
    element: HTMLElement | null,
    frames: Keyframe[],
    ms: number,
    delay = 0,
  ) {
    if (!element) return;
    const animation = element.animate(frames, {
      duration: ms,
      easing: ease,
      delay,
      fill: "both",
    });
    animations.push(animation);
    return animation;
  }
  function cleanup() {
    if (disposed) return;
    disposed = true;
    for (const callback of cleanups) callback();
    for (const animation of animations) animation.cancel();
    clone?.remove();
    if (hiddenImage && image) image.style.visibility = "";
  }
  if (reducedViewerMotion())
    return { finished: Promise.resolve(), cancel: cleanup };
  if (phase !== "change") {
    run(
      overlay,
      [
        { opacity: phase === "open" ? 0 : 1 },
        { opacity: phase === "open" ? 1 : 0 },
      ],
      240,
    );
    run(
      content,
      [
        { opacity: phase === "open" ? 0 : 1 },
        { opacity: phase === "open" ? 1 : 0 },
      ],
      phase === "open" ? 200 : 260,
    );
    for (const chrome of content.querySelectorAll<HTMLElement>(
      "[data-viewer-chrome]",
    ))
      run(
        chrome,
        phase === "open"
          ? [
              { opacity: 0, transform: "translateX(18px)" },
              { opacity: 1, transform: "translateX(0)" },
            ]
          : [
              { opacity: 1, transform: "translateX(0)" },
              { opacity: 0, transform: "translateX(10px)" },
            ],
        phase === "open" ? 300 : 180,
        phase === "open" ? 50 : 0,
      );
  }
  const source =
    phase === "close"
      ? origin
        ? visibleOrigin(id)
        : undefined
      : origin?.id === id
        ? origin
        : undefined;
  if (image && source && phase !== "change") {
    const destination = clippedViewerImage(
      readImageRect(image),
      stage.getBoundingClientRect(),
    );
    const thumbnail = viewerImageInFrame(source.imageRect, source.rect);
    if (destination.frame.width && destination.frame.height) {
      const start = phase === "open" ? thumbnail : destination;
      const end = phase === "open" ? destination : thumbnail;
      clone = document.createElement("div");
      clone.setAttribute("aria-hidden", "true");
      clone.dataset.viewerProjection = phase;
      Object.assign(clone.style, {
        position: "fixed",
        zIndex: "153",
        pointerEvents: "none",
        overflow: "hidden",
        left: "0",
        top: "0",
        transformOrigin: "top left",
        background: "var(--surface)",
      });
      const copy = document.createElement("img");
      copy.src = phase === "open" ? source.url : image.currentSrc || image.src;
      copy.alt = "";
      Object.assign(copy.style, {
        display: "block",
        maxWidth: "none",
        maxHeight: "none",
        margin: "0",
        transformOrigin: "top left",
        objectFit: "fill",
      });
      clone.append(copy);
      document.body.append(clone);
      image.style.visibility = "hidden";
      hiddenImage = true;
      run(
        clone,
        [
          {
            transform: `translate(${start.frame.left}px, ${start.frame.top}px)`,
            width: `${start.frame.width}px`,
            height: `${start.frame.height}px`,
            borderRadius: phase === "open" ? "6px" : "0px",
          },
          {
            transform: `translate(${end.frame.left}px, ${end.frame.top}px)`,
            width: `${end.frame.width}px`,
            height: `${end.frame.height}px`,
            borderRadius: phase === "open" ? "0px" : "6px",
          },
        ],
        duration,
      );
      // Letterboxing and scroll clipping belong to the inner image. Moving
      // only the frame would reset a scrolled screenshot or crop a small icon.
      run(
        copy,
        [start.image, end.image].map((bounds) => ({
          transform: `translate(${bounds.left}px, ${bounds.top}px)`,
          width: `${bounds.width}px`,
          height: `${bounds.height}px`,
        })),
        duration,
      );
    }
  }
  if (!clone && image && phase !== "close")
    run(
      image,
      [
        {
          opacity: 0,
          transform: `translateX(${phase === "change" ? direction * 18 : 0}px)`,
        },
        { opacity: 1, transform: "translateX(0)" },
      ],
      phase === "change" ? duration : 200,
    );
  const finished = Promise.all(
    animations.map((animation) => animation.finished.catch(() => undefined)),
  ).then(() => {
    // A thumbnail is already available on card opens. Keep its final projected
    // frame until the original image is ready, then swap without a blank frame.
    if (phase === "open" && clone && image && !image.complete && !disposed) {
      const reveal = () => cleanup();
      image.addEventListener("load", reveal, { once: true });
      image.addEventListener("error", reveal, { once: true });
      cleanups.push(() => {
        image.removeEventListener("load", reveal);
        image.removeEventListener("error", reveal);
      });
    } else if (phase !== "close") cleanup();
  });
  return { finished, cancel: cleanup };
}
